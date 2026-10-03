#!/usr/bin/env python3
"""matcher.py — Opportunity Matcher v1 (Assignment 4, Part 1: Add Real Intelligence).

Takes the Assignment 3 collector output (kept postings) plus a fresh pull,
scores each posting for fit against the CV facts and the stated target
("makes the materials" — advocate / educator / enablement / materials-maker
roles), routes each to a decision (PURSUE / NETWORK / WATCH / SKIP), and
generates human-readable rationales and a weekly digest.

This is the Python equivalent of workflow_v2.json (the n8n workflow).
Same scoring, same routing, same decisions — two implementations, one spec.

Labels (course rule): values from saved files are RECORD; weights and
thresholds are JUDGMENT; anything only Professor Bear can supply is YOUR INPUT.

Usage:
    python3 matcher.py --kept jobs-of-interest-2026-09-26.json \
        --cv professor-bear-cv.json --out outputs/
    python3 matcher.py --help
"""
import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

# ── Judgment: weights and thresholds (tune openly, never silently) ───────────
WEIGHTS = {
    "role_fit": 0.30,      # title vocabulary — the target, in the title
    "audience_fit": 0.20,  # a named audience in the text (who is taught)
    "materials": 0.20,     # make-materials phrase + named audience (two-part rule)
    "gap_close": 0.15,     # rewards one of the CV gaps from the gap table
    "company": 0.15,       # company demand score (record, from company-demand report)
}
THRESHOLDS = {"PURSUE": 0.65, "NETWORK": 0.45, "WATCH": 0.25}  # else SKIP

# ── Judgment: role vocabulary, weighted toward the stated target ─────────────
# "makes the materials" is the target (FRICTIONAL 2026-09-26). False friends
# (training/enablement/education/learning/content) are discounted, not cut,
# per the audit findings.
ROLE_WORDS = {
    "developer education": 1.0, "developer educator": 1.0,
    "advocate": 1.0, "evangelist": 1.0,
    "learning experience": 1.0, "learning experiences": 1.0,
    "education lead": 1.0, "head of education": 1.0,
    "educator": 0.9, "curriculum": 0.8, "instructional": 0.8,
    "content engineer": 0.8, "documentation": 0.7,
    "education": 0.7, "workshop": 0.6, "technical writer": 0.6,
    "enablement": 0.6,   # false friend: sales support as often as teaching
    "training": 0.4,     # false friend: model training at AI companies
    "professor": 0.5, "teacher": 0.5,
    "learning": 0.3,     # false friend: machine learning
    "content": 0.3,      # false friend: SEO marketing
}
# Judgment, revised 2026-10-03 after the first run: generic business words
# (partner/customer/public/community) appear in every B2B posting and are NOT
# teaching audiences. Only education audiences carry real weight now.
AUDIENCE_WEIGHTS = {
    "university": 0.5, "universities": 0.5, "college": 0.5, "campus": 0.5,
    "student": 0.5, "students": 0.5, "school": 0.4, "schools": 0.4,
    "developer": 0.3, "developers": 0.3,
    "partner": 0.15, "partners": 0.15, "community": 0.15,
    "customer": 0.1, "customers": 0.1, "public": 0.1,
}
MATERIALS_PHRASES = ["develop curriculum", "create curriculum", "build curriculum",
                     "own the curriculum", "create tutorials", "write documentation",
                     "develop training", "build training", "create course",
                     "develop course", "instructional design", "learning experience",
                     "enablement program", "certification program",
                     # added 2026-10-03: measured 2 hits on 737 postings,
                     # both the Claude Docs role. "documentation for" was
                     # rejected: 8 hits, mostly boilerplate (tax, AV).
                     "own the documentation"]
# Record: the CV gap table (README, Step 2). Revised 2026-10-03: bare
# "conference"/"workshop" match boilerplate ("we publish at conferences"),
# so only phrases where the posting ASKS FOR the gap activity count.
GAP_PHRASES = ["design system", "design token", "certification",
               "give talks", "public speaking", "keynote",
               "evangelist", "developer relations",
               "run workshops", "lead workshops", "host workshops",
               "facilitat"]
# Record: company demand, five-kind score / 5 (company-demand-2026-09-26.md).
# Unknown companies get 0.5 — neither rewarded nor punished (judgment).
COMPANY_DEMAND = {
    "anthropic": 1.0, "stripe": 0.6, "canva": 0.6, "openai": 0.6,
    "notion": 0.6, "figma": 0.4, "webflow": 0.4, "writer": 0.4,
    "miro": 0.4, "jasper": 0.4, "replit": 0.6, "meta": 0.5,
}

# ── Error handling ──────────────────────────────────────────────────────────
class FetchError(Exception):
    pass


class Quarantine(list):
    """Malformed records go here, never crash the run."""
    def add(self, raw, reason):
        self.append({"reason": reason,
                     "preview": str(raw)[:200]})


def fetch_with_retry(url, tries=3, base_delay=2.0, timeout=30):
    """Exponential backoff. Raises FetchError after `tries` attempts."""
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "opportunity-matcher/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8")
        except Exception as exc:  # network, timeout, HTTP error
            last = exc
            time.sleep(base_delay * (2 ** attempt))
    raise FetchError(f"GET {url} failed after {tries} tries: {last}")


def strip_html(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def normalize_greenhouse_live(job, quarantine):
    """Greenhouse boards API shape -> our record shape. Never raises."""
    try:
        dept = ""
        for m in job.get("metadata") or []:
            if m.get("name", "").lower() == "department":
                dept = m.get("value") or ""
        return {
            "source": "greenhouse-live",
            "company": job.get("company", "Anthropic"),
            "source_id": str(job.get("id", "")),
            "title": job.get("title", ""),
            "url": job.get("absolute_url", ""),
            "location_text": (job.get("location") or {}).get("name", ""),
            "department": dept,
            "text": strip_html(job.get("content", "")),
            "fetched": date.today().isoformat(),
        }
    except Exception as exc:
        quarantine.add(job, f"normalize failed: {exc}")
        return None


# ── Scoring (the intelligence) ──────────────────────────────────────────────
def score(record):
    """Return (fit, signals) where signals is a list of (name, evidence)."""
    title = (record.get("title") or "").lower()
    text = (record.get("text") or "").lower()
    signals = []

    role_hits = [(w, wt) for w, wt in ROLE_WORDS.items() if w in title]
    # Pairing rule (judgment, from the course's own open question 2026-09-26):
    # a DISCOUNTED title word (weight < 0.7 — the false friends: training,
    # enablement, education, learning, content) only counts when the text
    # confirms it with a named audience or a materials phrase. Otherwise the
    # whole board floats into WATCH on the company score alone.
    aud_hits = sorted({a for a in AUDIENCE_WEIGHTS
                       if re.search(r"\b" + a + r"\b", text)})
    mat_hits = [p for p in MATERIALS_PHRASES if p in text]
    if role_hits:
        w, wt = max(role_hits, key=lambda h: h[1])
        if wt < 0.7 and not aud_hits and not mat_hits:
            signals.append(("role",
                            f"title word '{w}' is discounted and unconfirmed — not counted"))
            role_fit = 0.0
        else:
            role_fit = wt
            signals.append(("role", f"title matches '{w}' (weight {wt})"))
    else:
        role_fit = 0.0
    audience_fit = min(1.0, sum(AUDIENCE_WEIGHTS[a] for a in aud_hits))
    if aud_hits:
        signals.append(("audience", f"text names audience: {', '.join(aud_hits[:4])}"))

    materials = (0.5 if mat_hits else 0.0) + (0.5 if (mat_hits and aud_hits) else 0.0)
    if mat_hits:
        signals.append(("materials",
                        f"'{mat_hits[0]}'" + (" + named audience" if aud_hits else " (no named audience)")))

    gap_hits = sorted({g for g in GAP_PHRASES if g in text})
    gap_close = min(1.0, 0.34 * len(gap_hits))
    if gap_hits:
        signals.append(("gap", f"rewards CV gap: {', '.join(gap_hits[:3])}"))

    company = (record.get("company") or "").lower()
    comp_score = COMPANY_DEMAND.get(company, 0.5)
    signals.append(("company", f"{record.get('company') or '?'} demand {comp_score:.1f}"))

    fit = (WEIGHTS["role_fit"] * role_fit
           + WEIGHTS["audience_fit"] * audience_fit
           + WEIGHTS["materials"] * materials
           + WEIGHTS["gap_close"] * gap_close
           + WEIGHTS["company"] * comp_score)
    return round(fit, 3), signals


def route(fit):
    if fit >= THRESHOLDS["PURSUE"]:
        return "PURSUE"
    if fit >= THRESHOLDS["NETWORK"]:
        return "NETWORK"
    if fit >= THRESHOLDS["WATCH"]:
        return "WATCH"
    return "SKIP"


def rationale(record, fit, decision, signals):
    lines = [f"**{record.get('title','?')}** — {record.get('company','?')} "
             f"({record.get('location_text','?')})",
             f"Fit {fit:.2f} → **{decision}**."]
    for name, ev in signals:
        lines.append(f"- {name}: {ev}")
    if record.get("url"):
        lines.append(f"- posting: {record['url']}")
    return "\n".join(lines)


def slug(title, company):
    s = re.sub(r"[^a-z0-9]+", "-", f"{company}-{title}".lower()).strip("-")
    return s[:60]


# ── Run ─────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description="Opportunity Matcher v1")
    ap.add_argument("--kept", required=True, help="jobs-of-interest JSON (Assignment 3 output)")
    ap.add_argument("--live", default=None, help="fresh Greenhouse JSON (optional, extends coverage)")
    ap.add_argument("--live-company", default="Anthropic")
    ap.add_argument("--cv", required=True, help="professor-bear-cv.json (checked, not scored)")
    ap.add_argument("--out", required=True, help="output folder")
    args = ap.parse_args()

    t0 = time.time()
    out = Path(args.out)
    (out / "briefs").mkdir(parents=True, exist_ok=True)
    quarantine = Quarantine()
    errors = []

    # The CV is attested record used for gap definitions, not parsed for PII.
    try:
        cv = json.load(open(args.cv))
        assert cv.get("attested"), "CV facts file is not attested"
    except Exception as exc:
        print(f"FATAL: cannot load attested CV: {exc}", file=sys.stderr)
        sys.exit(2)

    records = []
    try:
        kept = json.load(open(args.kept))
        records.extend(kept["records"])
    except Exception as exc:
        print(f"FATAL: cannot load kept postings: {exc}", file=sys.stderr)
        sys.exit(2)

    live_n = 0
    if args.live:
        try:
            live = json.load(open(args.live))
            for job in live.get("jobs", []):
                rec = normalize_greenhouse_live(job, quarantine)
                if rec:
                    rec["company"] = args.live_company
                    records.append(rec)
                    live_n += 1
        except Exception as exc:
            errors.append(f"live data unloadable, continuing on kept only: {exc}")

    seen, uniq = set(), []
    for r in records:
        key = (r.get("company", ""), r.get("source_id", ""), r.get("title", ""))
        if key in seen:
            continue
        seen.add(key)
        uniq.append(r)

    scored = []
    for r in uniq:
        if not r.get("title"):
            quarantine.add(r, "missing title")
            continue
        try:
            fit, signals = score(r)
        except Exception as exc:
            quarantine.add(r, f"scoring failed: {exc}")
            continue
        decision = route(fit)
        scored.append({**r, "fit": fit, "decision": decision,
                       "signals": signals,
                       "rationale": rationale(r, fit, decision, signals)})
    scored.sort(key=lambda s: -s["fit"])

    by_decision = {}
    for s in scored:
        by_decision.setdefault(s["decision"], []).append(s)

    today = date.today().isoformat()
    # Digest (human-readable output, not JSON)
    digest = [f"# Opportunity digest — {today}", "",
              f"Scored {len(scored)} postings "
              f"({len(uniq) - live_n} from Assignment 3, {live_n} fresh) "
              f"in {time.time() - t0:.1f}s.",
              f"Quarantined {len(quarantine)} malformed, {len(errors)} load errors.",
              ""]
    for dec in ["PURSUE", "NETWORK", "WATCH"]:
        group = by_decision.get(dec, [])
        digest.append(f"## {dec} ({len(group)})")
        for s in group[:10]:
            digest.append(f"### {s['title']} — {s['company']} (fit {s['fit']:.2f})")
            for name, ev in s["signals"]:
                digest.append(f"- {name}: {ev}")
            if s.get("url"):
                digest.append(f"- {s['url']}")
            digest.append("")
    (out / f"digest-{today}.md").write_text("\n".join(digest))

    # Per-role briefs for the gallery (PURSUE + NETWORK, up to 15)
    gallery = [s for s in scored if s["decision"] in ("PURSUE", "NETWORK")][:15]
    for s in gallery:
        body = (f"# {s['title']}\n\n{s['company']} — {s.get('location_text','')}\n\n"
                f"Fit {s['fit']:.2f} → **{s['decision']}**\n\n"
                f"## Why\n\n" +
                "\n".join(f"- {name}: {ev}" for name, ev in s["signals"]) +
                f"\n\n## Posting\n\n{s.get('url','')}\n\n"
                f"## Suggested next step\n\n" +
                ("Draft the application; it names the target directly.\n"
                 if s["decision"] == "PURSUE" else
                 "Find the human; the terms or the team need a conversation first.\n"))
        (out / "briefs" / f"{slug(s['title'], s['company'])}.md").write_text(body)

    report = {
        "date": today, "scored": len(scored), "live_added": live_n,
        "decisions": {k: len(v) for k, v in by_decision.items()},
        "quarantined": len(quarantine), "errors": errors,
        "elapsed_s": round(time.time() - t0, 1),
        "weights": WEIGHTS, "thresholds": THRESHOLDS,
    }
    (out / f"run-report-{today}.json").write_text(json.dumps(report, indent=2) + "\n")
    if quarantine:
        (out / f"quarantine-{today}.log").write_text(
            "\n".join(f"{q['reason']} :: {q['preview']}" for q in quarantine))

    print(f"scored={len(scored)} "
          + " ".join(f"{k}={len(v)}" for k, v in sorted(by_decision.items()))
          + f" quarantined={len(quarantine)} elapsed={report['elapsed_s']}s")


if __name__ == "__main__":
    main()
