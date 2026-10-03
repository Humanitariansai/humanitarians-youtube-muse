#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Claude, On the Job." (slug: claude-on-the-job).

SHOW-TELL (Bear, 2026-09-26): every body beat is ONE drawn isometric Manim
illustration (Claude palette) with at most a few words of label; Liam's
narration carries the explanation. No composer cold open, no verdict card
(bookend_exempt); the spoken @NikBearBrown outro stays (never exempt).

Source: "Claude, On the Job." (episode H4 of the "Claude, For Students"
series) in the mirror repo nikbearbrown/humanitarians-youtube-muse at
claude-for-artificial-intelligence/hai-on-the-job/ — rewritten here for the
humanitarians AI general audience (smart, pragmatic, not necessarily AI
experts). The four-tier framework and "distrust-calibration" are the series'
own pedagogical framing; the tier labels are the film's construct, not a
citation. Every technical term is explained aloud in plain words.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "claude-on-the-job"
TITLE = "Claude, On the Job."

WPS = 2.5  # Kokoro words-per-second planning estimate


def est(text):
    return round(len(text.split()) / WPS, 1)


def manim(bid, act, narration, cls, image, show, qc_reason):
    return {
        "beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW",
        "narration_text": narration, "estimated_duration_s": est(narration),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image,
                 "show": show, "manim": {"class": cls}, "motion_claim": image},
        "qc": {"sparse_by_design": True, "sparse_reason": qc_reason},
    }


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


SPARSE = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
          "minimal labels, with the voice carrying the explanation. The negative space is the style, "
          "so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")

OPEN = [
    remotion(
        "BIDEA", "the question",
        "Hallo. This is Liam, in for Bear. Everyone asks whether AI will take their job. "
        "Wrong race. The real question: how do you conduct the machine instead of racing it?",
        "BrutalistHesitantWriter",
        {"text": "Will AI take my job?\nHow do I win the race?",
         "triggerWords": "win the race", "replacementWords": "conduct the machine",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
         "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Will AI take my job?'"},
         {"at": 0.5, "event": "backspaces 'win the race' -> 'conduct the machine' on the spoken correction"}],
        lead_silence_s=0.8,
        motion_claim="The writer types the naive job-loss question and corrects the race into the film's real one: conducting the machine.",
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion(
        "BDEFS", "terms",
        "Four terms. A tier: one level of a four-level map of work — machine or human, who does it better. "
        "To conduct: to direct the machine instead of racing it. A hallucination: a confident made-up answer "
        "that sounds right and isn't. An audit: reading the output line by line before you sign off.",
        "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [
             {"term": "tier",
              "meaning": "one level of a four-level map of work: machine or human, who does it better"},
             {"term": "conduct",
              "meaning": "directing the machine instead of racing it"},
             {"term": "hallucination",
              "meaning": "a confident made-up answer; sounds right, isn't"},
             {"term": "audit",
              "meaning": "reading the output line by line before you sign off"}],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'tier' lands"},
         {"at": 0.35, "event": "'conduct' lands"},
         {"at": 0.6, "event": "'hallucination' lands"},
         {"at": 0.8, "event": "'audit' lands"}],
        gate="CARD",
        qc={"sparse_by_design": True,
            "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

B = [
    manim(
        "B00", "hero",
        "Here is the whole film in one picture: a four-tier map of work. The machine owns the bottom. "
        "You own the top. And most people are fighting on the wrong level.",
        "B00_TierMap",
        "A four-block tier stack drops in level by level; a small figure races at Tier 1, then climbs to the top tiers.",
        [{"at": 0.05, "event": "tier blocks drop in, labels '1'-'4'"},
         {"at": 0.45, "event": "figure appears at Tier 1"},
         {"at": 0.7, "event": "figure climbs to Tiers 3-4"}],
        SPARSE),
    manim(
        "B01", "tier one",
        "Tier one is recall: facts, syntax, finding things. The machine is superhuman here, right now. "
        "No one memorizes or searches faster than it. Racing it here is a race you already lost.",
        "B01_TierOne",
        "A dark machine block; output pages drop in fast and stack; the human figure beside it fades to ghost.",
        [{"at": 0.1, "event": "machine block lands, 'machine' label"},
         {"at": 0.35, "event": "pages fly in, fast"},
         {"at": 0.75, "event": "human figure fades to ghost"}],
        SPARSE),
    manim(
        "B02", "tier two",
        "Tier two is synthesis: drafts, summaries, spotting patterns. This is contested space — human and "
        "machine both play here. Let the machine do the rough work; you keep the judgment.",
        "B02_Contested",
        "Machine block and human figure share one page; the page slides back and forth between them, then settles at the human.",
        [{"at": 0.1, "event": "machine, human, shared page"},
         {"at": 0.4, "event": "page shuttles between them"},
         {"at": 0.75, "event": "page settles with the human"}],
        SPARSE),
    manim(
        "B03", "tier three",
        "Tier three is judgment. Read the output and decide: is it right, is it good, does it serve the real "
        "goal? Only a person knows what matters here. That is yours.",
        "B03_Judgment",
        "A page on the desk; the human inspects it with a magnifier sweeping line by line; a terracotta check lands.",
        [{"at": 0.1, "event": "page lands, 'the output' label"},
         {"at": 0.35, "event": "magnifier sweeps the page"},
         {"at": 0.7, "event": "terracotta check"}],
        SPARSE),
    manim(
        "B04", "tier four",
        "Tier four is the part no model touches: deciding which problem is worth solving, and whether to trust "
        "the answer at all. That is irreducible. Yours today, and for a long while.",
        "B04_Irreducible",
        "The machine block dims to ghost at the back; the human faces two question pages, pins one with a terracotta dot.",
        [{"at": 0.1, "event": "machine dims to ghost"},
         {"at": 0.4, "event": "two question pages appear before the human"},
         {"at": 0.7, "event": "human pins one; terracotta dot"}],
        SPARSE),
    manim(
        "B05", "the scarce skill",
        "So what is actually scarce? Not recall — the machine has that. Conducting: knowing what to ask, "
        "catching the mistakes, deciding what a human must touch. That is the job now.",
        "B05_Conducting",
        "The human figure stands before the machine with a baton; a page flows from the machine to the human as the baton lifts.",
        [{"at": 0.1, "event": "machine, human with baton"},
         {"at": 0.45, "event": "page flows machine to human"},
         {"at": 0.75, "event": "baton lifts"}],
        SPARSE),
    manim(
        "B06", "the daily loop",
        "The practice: one real task a day — not a demo, a thing you actually have to do. Run it through "
        "Claude. Read every line. Name one thing it got wrong. One rep of judgment, every day.",
        "B06_DailyLoop",
        "A row of task pills; the first drops into the machine, a page comes out; a scan line reads it and a weak spot is marked.",
        [{"at": 0.05, "event": "task pills queue up"},
         {"at": 0.35, "event": "one task enters the machine, a page exits"},
         {"at": 0.6, "event": "scan line reads the page"},
         {"at": 0.8, "event": "a weak spot is circled"}],
        SPARSE),
    manim(
        "B07", "never delegate",
        "Know what never leaves your desk. Anything you sign your name to. Any call where you bear the cost. "
        "Your reputation. Your name on it means your judgment owns it.",
        "B07_NeverDelegate",
        "A page with a signature line; a stamp comes down; three pills — 'you sign', 'your cost', 'your name' — each earn an ink check.",
        [{"at": 0.05, "event": "page with signature line"},
         {"at": 0.3, "event": "three pills land"},
         {"at": 0.55, "event": "stamp comes down"},
         {"at": 0.75, "event": "checks land on each pill"}],
        SPARSE),
    manim(
        "B08", "the one that's yours",
        "Quick check. Four jobs: draft an email, answer a fact question, fire a vendor, summarize a meeting. "
        "Which one is yours alone? The vendor call. The machine can research it; only you can own the decision.",
        "B08_YoursAlone",
        "Four task pills in a row; a cursor taps 'fire a vendor'; a terracotta check lands; the other three dim to ghost.",
        [{"at": 0.1, "event": "four pills land"},
         {"at": 0.45, "event": "cursor taps 'fire a vendor'"},
         {"at": 0.7, "event": "terracotta check; others dim"}],
        SPARSE),
]

YT_PROMPT = ("Here is a real task from my job. Help me do it, then read your own output "
             "and name one thing you are least sure about.")

YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Paste this into Claude with one real task from today: \"" + YT_PROMPT + "\" "
    "Then audit the output yourself: read every line and name one weak spot. That is your first rep.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Your First Audit Rep",
     "command": YT_PROMPT, "runningText": "paste this into Claude…",
     "output": ["Check: the model's output, read line by line.",
                "Check: name one weak spot — one thing it got wrong or weak."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Claude", "effortLabel": "One task"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

BOUT = {"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
        "narration_text": f"{TITLE} At Nik Bear Brown.", "estimated_duration_s": 4.0,
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "REMOTION", "source": "own",
                 "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                 "remotion": {"pattern": "ClaudeTitleOutro",
                              "props": {"title": TITLE, "slug": SLUG,
                                        "handle": "@NikBearBrown", "subline": ""}}},
        "kind": "outro_voice", "tail_silence_s": 1.0}

BEATS = OPEN + B + [YOURTURN, BOUT]

# ── assertions (the package's own gate) ──────────────────────────────────────
assert len(BEATS) == 13, f"expected 13 beats, got {len(BEATS)}"
total = sum(b["estimated_duration_s"] for b in BEATS)
assert 120 <= total <= 360, f"total estimated duration out of bounds: {total}s"

MANIM_IDS = ["B00", "B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08"]
for b in BEATS:
    assert b["narration_text"].strip(), f'{b["beat_id"]}: empty narration'
    assert b["voice"] == "am_onyx" and b["engine"] == "kokoro", f'{b["beat_id"]}: voice/engine'
    assert b["estimated_duration_s"] > 0, f'{b["beat_id"]}: zero duration'
for b in B:
    assert b["lane"] == "manim", f'{b["beat_id"]}: lane'
    assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), f'{b["beat_id"]}: class name'
    assert b["shot"]["type"] == "GRAPHIC" and b["shot"]["source"] == "own", f'{b["beat_id"]}: shot'
    assert b["qc"]["sparse_by_design"] and b["qc"]["sparse_reason"], f'{b["beat_id"]}: sparse waiver'
assert [b["beat_id"] for b in B] == MANIM_IDS, "body beat order"
idea = next(b for b in OPEN if b["beat_id"] == "BIDEA")
txt = idea["shot"]["remotion"]["props"]["text"]
trig, rep = idea["shot"]["remotion"]["props"]["triggerWords"], idea["shot"]["remotion"]["props"]["replacementWords"]
assert trig in txt and rep not in txt, "hesitant-writer trigger not verbatim in text"
assert not trig.endswith((".", "?", "!")) and not rep.endswith((".", "?", "!")), "trigger/replacement punctuation"
assert idea["lead_silence_s"] == 0.8, "BIDEA lead silence"
defs = next(b for b in OPEN if b["beat_id"] == "BDEFS")
terms = defs["shot"]["remotion"]["props"]["terms"]
assert 2 <= len(terms) <= 4, "BDEFS term count"
assert all(len(t["term"]) <= 17 for t in terms), "ClaudeDefinitions truncation (>17 chars)"
assert BOUT["kind"] == "outro_voice" and BOUT["tail_silence_s"] == 1.0, "outro"

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · AI AT WORK", "skill": "show-tell",
    "style_preset": "show-tell", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "English (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card "
                              "(Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), "
                              "no verdict card; Your Turn is the Claude.ai composer; spoken outro stays."),
    "audience": "smart, pragmatic general audience — not necessarily AI experts",
    "source_doc": ("mirror repo nikbearbrown/humanitarians-youtube-muse, "
                   "claude-for-artificial-intelligence/hai-on-the-job/ (episode H4, 'Claude, For Students' series) — "
                   "rewritten for the humanitarians AI channel; the four-tier framework and 'distrust-calibration' "
                   "are the series' own pedagogical framing, not a citation"),
    "playlist": "How to Use AI", "chapter_number": 0,
    "tags": ["Claude", "AI at work", "AI fluency", "future of work", "human judgment",
             "AI hallucination", "AI audit", "Nik Bear Brown"]},
    "beats": BEATS}

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(BEATS)} beats; est {total:.0f} s ({total/60:.1f} min)")
