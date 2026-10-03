# Frictional — Assignment 4

The process log for this assignment. The folder-level log across all of Professor Bear's work in this class is [`../FRICTIONAL.md`](../FRICTIONAL.md); this one stays on Assignment 4.

## Executive summary

**What this is.** The process log for the Assignment 4 Part 1 build: the
opportunity matcher, in two implementations (Python `matcher.py` and n8n
`workflow_v2.json`), plus extended board coverage (Anthropic live,
Meta investigated). Written the way the course asks students to write
theirs.

**Why read it.** It records what was tried, what went wrong, and what was
measured — including two tuning iterations where the first run exposed
exactly the false-friend problems the 2026-09-26 audits found.

**What it records so far.** 2026-10-03: one session. Anthropic's live
Greenhouse board (640 postings) pulled and scored; the direct equivalents
of the Figma advocate target identified. Meta's board investigated and
recorded as unreadable, same category as Google. The matcher built, run on
714 postings (97 kept + 640 fresh, deduped): 22 PURSUE, 37 NETWORK, 325
WATCH, 330 SKIP, 0 quarantined, 3.1s.

## Entries

### 2026-10-03 — Extending coverage: Anthropic live, Meta investigated

- **Date and what I was working on:** Professor Bear asked for the equivalent
  of the Figma advocate roles at Anthropic, and "why not Meta."

- **I tried / expected:** I expected Anthropic to be readable (the 2026-09-26
  run already used its Greenhouse feed) and Meta to be an open question.

- **What happened:**
  - **Anthropic worked first try.** `boards-api.greenhouse.io/v1/boards/anthropic/jobs`
    returned 640 postings. The direct equivalents are live right now:
    *Developer Education Lead, Claude Platform*; *Head of Technical Training*;
    *Technical Documentation and Content Engineer, Claude Docs* (the 2026-09-26
    bullseye — still open); *Software Engineer, Education*; plus a bench of
    enablement leads.
  - **Meta is unreadable.** `metacareers.com/jobsearch/` is a JS shell — no
    server-rendered job data, search on internal authenticated GraphQL with
    rotating doc IDs, no public JSON feed. Same category as Google in the
    2026-09-26 log. I stopped after three shapes rather than guessing more,
    per the course's own precedent.
  - **No "Muse for Education" role found.** A web search surfaced Meta's
    education-adjacent recruiting programs but no staffed advocate/educator
    function for Muse. Absence from the table is a measurement gap, not
    evidence of no demand.

- **What I did:** Saved the live Anthropic pull as `anthropic-live.json`
  (evidence, dated); wrote `anthropic-equivalents-2026-10-03.md` with the
  ranked equivalents; wrote `meta-board-note-2026-10-03.md` recording the
  unreadable finding and the manual re-check path.

- **What Claude or another person contributed:** Muse (me) ran the pulls,
  read the board, and wrote the notes. Professor Bear set the direction:
  Anthropic equivalents, and "why not Meta."

- **What I understand now / still do not understand:** Anthropic is where
  the demand is most legible right now — it staffs the exact function the
  search targets. Meta remains a question mark by method, not by evidence.
  Still open: whether a browser-driven reader for Meta (and Google, Adobe,
  Salesforce, GitHub) is worth building, or monthly hand-checks.

- **Evidence and next step:** `anthropic-live.json`, `anthropic-equivalents-2026-10-03.md`,
  `meta-board-note-2026-10-03.md`. Next: the matcher itself.

### 2026-10-03 — Building the opportunity matcher, two ways

- **Date and what I was working on:** Assignment 4, Part 1 — the intelligence
  layer on the Assignment 3 collector. Built as `matcher.py` (Python) and
  `workflow_v2.json` (n8n): same weights, thresholds, vocabulary, routing.
  Two implementations, one spec.

- **I tried / expected:** Score each posting on five dimensions (role 0.30,
  audience 0.20, materials 0.20, gap-close 0.15, company 0.15), route to
  PURSUE / NETWORK / WATCH / SKIP, generate a per-role rationale and a
  weekly digest. I expected the ranking to work first try.

- **What happened:**
  - **First run: 633 of 714 in WATCH.** The band was noise. Cause: generic
    business words (partner/customer/public/community) counted as "audience,"
    and bare "conference"/"workshop" matched boilerplate — the same
    false-friend class the 2026-09-26 audits found.
  - **Fix 1 — the pairing rule**, from the course's own open question:
    a discounted title word (training/enablement/education/learning/content)
    only counts when the text confirms it with a named audience or a
    materials phrase. This operationalizes the "train their own people"
    reversal: confirmed teaching counts, pure process does not.
  - **Fix 2 — audience and gap tightened.** Audience words re-weighted:
    education audiences 0.4–0.5, developers 0.3, generic business words
    0.1–0.15. Gap phrases now require the posting to *ask for* the activity
    ("give talks," "run workshops") instead of matching "we publish at
    conferences."
  - **The bullseye failed, then passed.** The Claude Docs role scored 0.46
    (NETWORK) because no materials phrase matched "own the documentation."
    Measured across 737 postings: "own the documentation" hit twice, both
    the right role — added. "documentation for" hit 8 times, mostly tax and
    AV boilerplate — rejected, same reason "how-to guides" was cut. The
    role now scores 0.66 → PURSUE.
  - **Final: 22 PURSUE, 37 NETWORK, 325 WATCH, 330 SKIP, 0 quarantined,
    3.1 seconds.** Top of PURSUE: Developer Education Lead (Anthropic),
    Designer Advocate Partnerships (Figma), Senior Developer Educator
    (Webflow), Native Learning Experiences (OpenAI), Learning Experiences
    Creator (Replit).

- **What I did:** Wrote `matcher.py`, `workflow_v2.json` (validated: 11
  nodes, no dangling refs), `ERROR-HANDLING.md` (retry/backoff, error
  branches, quarantine, cached-data fallback), and ran it on real data:
  `digest-2026-10-03.md` + `.html`, 15 per-role briefs, `run-report.json`.

- **What Claude or another person contributed:** Muse (me) designed the
  scoring, found the WATCH-band problem in the first run's output, and made
  the three tuning calls — all measured before changing anything. Nothing
  here has been reviewed by Professor Bear; thresholds and weights are
  judgment, labeled as such in the code.

- **What I understand now / still do not understand:** The matcher
  reproduces the course's findings rather than contradicting them — the
  false friends bit in exactly the predicted places, and the fixes are the
  ones the log had already proposed. Still open: whether NETWORK's 37 are
  conversation-worthy (his call), and the LLM upgrade path for rationales.

- **Evidence and next step:** `matcher.py`, `workflow_v2.json`,
  `ERROR-HANDLING.md`, `outputs/` (digest, 15 briefs, run report). Next:
  Part 2 gallery polish, Part 3 scale numbers, Part 4 Figma materials —
  and Professor Bear's review of the thresholds.
