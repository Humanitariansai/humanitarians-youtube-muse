#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Plan anything." (slug: plan-anything).

SHOW-TELL (Bear, 2026-09-26): every body beat is ONE drawn isometric Manim
illustration (Claude palette) with at most a few words of label; Liam's
narration carries the explanation. No composer cold open, no verdict card
(bookend_exempt); the spoken @NikBearBrown outro stays (never exempt).

Source: NEW — built from scratch. No mirror source. The demo arc (a weekend
trip planned iteratively: constraints first, then a draft, then a revision,
then a packing checklist) is the film's own worked example; the trip details
are fictional, not price or availability claims. The constraints -> draft ->
revise -> checklist loop is the film's pedagogical construct, not a citation.
Every technical term (constraint, draft, itinerary) is defined aloud in BDEFS.

Film 17 of 24 in the "How to AI" queue. Skill: show-tell (chosen over the
other make skills because the film is a drawn explainer — no code, no CLI
loop, no product UI to demonstrate; the pattern teaches as a loop of
pictures, one per beat).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "plan-anything"
TITLE = "Plan anything."

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

B = [
    manim(
        "B00", "the loop",
        "Planning is where AI shines. It never gets tired of revising, so you can ask for ten "
        "versions instead of settling for the first one. Every good plan runs the same loop: "
        "constraints in, a draft out, revisions, then a checklist.",
        "B00_TheLoop",
        "Four kraft blocks drop in one by one — constraints, draft, revise, checklist — while a "
        "terracotta arrow sweeps along the row.",
        [{"at": 0.1, "event": "constraints block drops"},
         {"at": 0.35, "event": "draft block drops"},
         {"at": 0.6, "event": "revise block drops"},
         {"at": 0.8, "event": "checklist block drops; terracotta arrow sweeps"}],
        SPARSE),
    manim(
        "B01", "constraints",
        "Start with your constraints, not your dream trip. Say two days, a hundred and fifty "
        "dollars of spending money, and what you like: hiking, museums, cheap eats. Give the "
        "machine all of it, up front.",
        "B01_Constraints",
        "Three kraft chips — budget, dates, interests — drop into an open kraft box one by one, "
        "each labelled as it lands.",
        [{"at": 0.1, "event": "open box; 'budget' chip drops"},
         {"at": 0.45, "event": "'dates' chip drops"},
         {"at": 0.7, "event": "'interests' chip drops"}],
        SPARSE),
    manim(
        "B02", "the draft",
        "Now ask for a draft. 'Here are my budget, my dates, my interests: sketch a two-day trip.' "
        "Out comes an itinerary: day one, day two, a morning hike, a lunch stop, an evening at a "
        "museum. Not final. Raw material.",
        "B02_DraftItinerary",
        "Two itinerary pages drop in fast — 'day one', 'day two' — and a terracotta dot lands on "
        "the plan with the words 'raw material'.",
        [{"at": 0.1, "event": "'day one' page drops"},
         {"at": 0.45, "event": "'day two' page drops"},
         {"at": 0.8, "event": "terracotta dot; 'raw material' lands"}],
        SPARSE),
    manim(
        "B03", "revise",
        "Now do the thing no travel book ever did: complain. 'Too rushed, slow it down, and drop "
        "the early start.' The whole plan rewrites itself in seconds. No sighing, no erasing. "
        "That is the superpower: the machine never gets tired of revising.",
        "B03_Revise",
        "An ink arc sweeps across the draft as the complaint lands; a terracotta dot marks the "
        "first stop, which fades out; the remaining stops spread apart; a terracotta check lands "
        "with the word 'slower'.",
        [{"at": 0.25, "event": "arc sweeps the draft; dot marks the first stop"},
         {"at": 0.55, "event": "first stop fades; the rest spread apart"},
         {"at": 0.8, "event": "terracotta check; 'slower' lands"}],
        SPARSE),
    manim(
        "B04", "the checklist",
        "Last step: turn the plan into a checklist. What to pack, what to book before you go, "
        "what to double-check the day before. A plan you can hold in your hand, and check off.",
        "B04_Checklist",
        "A plan page beside three pills — pack, book, day before — each getting a terracotta "
        "check as the voice names it.",
        [{"at": 0.2, "event": "'pack' pill; terracotta check"},
         {"at": 0.5, "event": "'book' pill; terracotta check"},
         {"at": 0.8, "event": "'day before' pill; terracotta check"}],
        SPARSE),
    manim(
        "B05", "projects",
        "The pattern travels. Planning a project? Same loop. Constraints: your deadline, your "
        "team. A draft timeline. Revisions when the scope slips. And a launch checklist at the end.",
        "B05_Projects",
        "Two chips drop into the constraint box; a project page with a three-bar timeline lands; "
        "one bar fades as the scope slips; a terracotta check lands with the word 'launch'.",
        [{"at": 0.1, "event": "chips drop into the constraint box"},
         {"at": 0.4, "event": "project page; three timeline bars"},
         {"at": 0.7, "event": "one bar fades; arc sweeps"},
         {"at": 0.9, "event": "terracotta check; 'launch' lands"}],
        SPARSE),
    manim(
        "B06", "budgets",
        "A budget is a plan for money, and it runs the same loop. Constraints: your income, your "
        "goals. A draft: the first split of every dollar. Revisions when life happens. The "
        "checklist: payday, bills paid, savings moved, done.",
        "B06_Budgets",
        "Two chips drop into the constraint box; a budget page lands with one bar split into "
        "three grey segments; one segment fades as life happens; a terracotta check lands with "
        "the word 'payday'.",
        [{"at": 0.1, "event": "chips drop into the constraint box"},
         {"at": 0.4, "event": "budget page; bar split into three"},
         {"at": 0.7, "event": "one segment fades; arc sweeps"},
         {"at": 0.9, "event": "terracotta check; 'payday' lands"}],
        SPARSE),
    manim(
        "B07", "verify",
        "One rule never changes. AI prices and opening hours come from memory, and memory goes "
        "stale. Before you book anything, check it yourself. The machine plans. You verify.",
        "B07_YouVerify",
        "A magnifier appears over the plan page and sweeps it; a terracotta check lands; a small "
        "figure arrives with the words 'you verify'.",
        [{"at": 0.2, "event": "magnifier appears over the plan"},
         {"at": 0.5, "event": "sweep; terracotta check"},
         {"at": 0.8, "event": "figure arrives; 'you verify' lands"}],
        SPARSE),
]

OPEN = [
    remotion(
        "BIDEA", "the question",
        "Hallo. This is Liam, in for Bear. Don't ask the machine to plan everything in one go. "
        "Plan with it instead, step by step, like a partner that never gets tired of revising.",
        "BrutalistHesitantWriter",
        {"text": "Plan my whole weekend trip for me?",
         "triggerWords": "Plan my whole weekend trip", "replacementWords": "help me plan it step by step",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
         "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Plan my whole weekend trip for me?'"},
         {"at": 0.6, "event": "backspaces 'plan my whole weekend trip' -> 'help me plan it step by step' on the spoken correction"}],
        lead_silence_s=0.8,
        motion_claim="The writer types the naive one-shot planning request and corrects it to the film's real one: planning with the machine, step by step.",
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion(
        "BDEFS", "terms",
        "Three terms. A constraint: a limit the plan must respect, your budget, your dates, your "
        "interests. A draft: a first version built to be changed. An itinerary: the trip's "
        "day-by-day schedule.",
        "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [
             {"term": "constraint",
              "meaning": "a limit the plan must respect: budget, dates, interests"},
             {"term": "draft",
              "meaning": "a first version, built to be changed"},
             {"term": "itinerary",
              "meaning": "the trip's day-by-day schedule"}],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'constraint' lands"},
         {"at": 0.5, "event": "'draft' lands"},
         {"at": 0.78, "event": "'itinerary' lands"}], gate="CARD",
        qc={"sparse_by_design": True,
            "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("I'm planning a weekend trip. My constraints are: two days, one hundred fifty dollars "
             "of spending money, and I like hiking, museums, and cheap eats. Give me a first draft "
             "itinerary, then I'll tell you what's wrong with it. Keep it simple.")
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Did it respect every constraint you gave it? And did it ask what it got wrong? If it didn't "
    "ask, invite the revision yourself: 'too rushed, slow it down.'",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Plan Your First Trip",
     "command": YT_PROMPT, "runningText": "paste this into Claude…",
     "output": ["Check: it respected every constraint you gave it.",
                "Check: nothing is booked until you verify it yourself."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE} At Nik Bear Brown.", "estimated_duration_s": 4.0,
          "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                               "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown",
                                         "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · HOW TO AI", "skill": "show-tell",
    "style_preset": "show-tell", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24,
    "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "English (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience — not necessarily AI experts",
    "source_doc": "NEW — built from scratch; no mirror source. The demo arc (weekend trip: constraints → draft → revise → checklist) is the film's own fictional worked example. See SOURCES.md.",
    "playlist": "How to Use AI", "chapter_number": 17,
    "tags": ["Claude", "AI planning", "trip planning", "productivity", "AI fluency", "itinerary", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

# ── self-assertions: the sheet is derived, this generator is the source of truth ──
beats = sheet["beats"]
assert len(beats) == 12, f"expected 12 beats, got {len(beats)}"
total = sum(b["estimated_duration_s"] for b in beats)
assert 120 <= total <= 360, f"total {total}s outside 120–360 s"
for b in beats:
    assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    assert b["voice"] == "am_onyx" and b["engine"] == "kokoro", f"{b['beat_id']}: voice/engine"
    assert b["estimated_duration_s"] > 0, f"{b['beat_id']}: bad duration"

BODY = [b for b in beats if b["lane"] == "manim"]
assert [b["beat_id"] for b in BODY] == ["B00", "B01", "B02", "B03", "B04", "B05", "B06", "B07"]
for b in BODY:
    assert b["shot"]["type"] == "GRAPHIC" and b["shot"]["source"] == "own"
    cls = b["shot"]["manim"]["class"]
    assert cls.startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class {cls}"
    assert b.get("qc", {}).get("sparse_by_design"), f"{b['beat_id']}: missing sparse waiver"

idea = beats[0]
props = idea["shot"]["remotion"]["props"]
assert props["triggerWords"] in props["text"], "BIDEA trigger not verbatim in writer text"
assert not props["triggerWords"].endswith(("?", ".", "!")), "BIDEA trigger has trailing punctuation"
assert not props["replacementWords"].endswith(("?", ".", "!")), "BIDEA replacement has trailing punctuation"
assert idea.get("lead_silence_s") == 0.8, "BIDEA lead_silence_s"

defs = beats[1]
terms = defs["shot"]["remotion"]["props"]["terms"]
assert 2 <= len(terms) <= 4, "BDEFS term count"
assert all(len(t["term"]) <= 17 for t in terms), "BDEFS term too long (ClaudeDefinitions truncates)"

htf = [b for b in beats if b["beat_id"] == "BHTF"][0]
assert htf["shot"]["remotion"]["pattern"] == "ClaudeComposerAsk"
assert htf["shot"]["remotion"]["props"]["greeting"] == "Your turn."
assert "YOUR TURN" in htf["shot"]["remotion"]["props"]["topic"]

out = beats[-1]
assert out["beat_id"] == "BOUT" and out.get("kind") == "outro_voice"
assert out.get("tail_silence_s") == 1.0, "BOUT tail"

print(len(beats), "beats; est", round(total, 1), "s; assertions passed")
