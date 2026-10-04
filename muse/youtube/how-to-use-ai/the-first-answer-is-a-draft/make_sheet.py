#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "The first answer is a draft".

SHOW-TELL (Bear, 2026-09-26): every body beat is ONE drawn isometric
illustration with minimal labels; Liam's narration carries the explanation.
The film's cast is a single object — the draft page — which evolves from
B02 to B05 so the viewer watches iteration happen. Zero ShowTellCards.

Built from scratch (NEW): no mirror source.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "the-first-answer-is-a-draft"
TITLE = "The first answer is a draft"

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

B = [
 beat("B00", "Picture every AI answer as a page stamped draft one. Not the answer. Just the first try.",
      "B00_DraftOne", "A white draft page drops onto the stage; a DRAFT 1 tag clips onto its corner; the label 'draft one' lands beside it.",
      [{"at": 0.1, "event": "page drops in"}, {"at": 0.5, "event": "DRAFT 1 tag clips on"}, {"at": 0.8, "event": "label lands"}]),
 beat("B01", "Most people treat that page like it's final. They read it, nod, and move on. But that first answer is a rough guess — it doesn't know your life yet.",
      "B01_TooEarly", "A rubber stamp reading FINAL slams down onto the draft page from above, too early.",
      [{"at": 0.1, "event": "page with DRAFT 1 tag"}, {"at": 0.45, "event": "stamp descends"}, {"at": 0.6, "event": "stamp lands"}]),
 beat("B02", "Say you ask Claude: plan my dinners this week. Draft one comes back long and vague — full of dishes you'll never cook.",
      "B02_FirstTry", "A question pill 'plan dinners' sits above the page; six long pale ghost lines draw in one by one — the vague answer.",
      [{"at": 0.1, "event": "question pill"}, {"at": 0.35, "event": "ghost lines draw in"}]),
 beat("B03", "Now push back. Type one word: shorter. The page trims itself. Same plan, half the words.",
      "B03_Shorter", "A pushback pill 'shorter' pops in; three of the six lines get ink X marks and fade out — the page trims itself.",
      [{"at": 0.15, "event": "'shorter' pill pops in"}, {"at": 0.55, "event": "X marks draw"}, {"at": 0.75, "event": "lines fade"}]),
 beat("B04", "Push back again: more concrete. The vague lines sharpen into real dinners — taco night, soup, a stir-fry you'll actually buy for.",
      "B04_Concrete", "A pushback pill 'more concrete' pops in; the three pale lines become solid ink lines, each labelled with a real dinner.",
      [{"at": 0.15, "event": "'more concrete' pill pops in"}, {"at": 0.5, "event": "lines sharpen"}, {"at": 0.7, "event": "dinner labels land"}]),
 beat("B05", "Then steer it: try again, but for a busy parent. Now each dinner gets a clock: fifteen minutes, twenty minutes. The plan fits your life, not a stranger's.",
      "B05_BusyParent", "A pushback pill 'for a busy parent' pops in; a clock drops in; '15 min' tags land beside each dinner.",
      [{"at": 0.15, "event": "'for a busy parent' pill pops in"}, {"at": 0.5, "event": "clock drops in"}, {"at": 0.7, "event": "15 min tags land"}]),
 beat("B06", "Set draft one next to draft three. The first was generic. The last is yours. The AI didn't get smarter — you steered it.",
      "B06_SideBySide", "The greyed draft-one page slides left; a crisp page with a DRAFT 3 tag and an ink check drops in on the right.",
      [{"at": 0.1, "event": "draft one slides left"}, {"at": 0.45, "event": "draft three drops in"}, {"at": 0.8, "event": "check draws"}]),
 beat("B07", "Sometimes pushback goes too far, and the plan drifts off track. Fine. You're the boss. One line brings it back: keep it simple, stick to weeknights.",
      "B07_Drift", "A stray off-topic line wanders onto the page; a steering pill 'stick to weeknights' pops in; the stray line fades away.",
      [{"at": 0.15, "event": "stray line drifts in"}, {"at": 0.55, "event": "steering pill pops in"}, {"at": 0.8, "event": "stray line fades"}]),
 beat("B08", "Three pushbacks do most of the work. Shorter: cut the fluff. More concrete: name the thing. For someone: say whose life this is for. Remember those three.",
      "B08_Recipe", "Three pills spring in left to right — 'shorter', 'more concrete', 'for someone' — with an ink arrow drawing beneath them.",
      [{"at": 0.15, "event": "'shorter' pill"}, {"at": 0.4, "event": "'more concrete' pill"}, {"at": 0.65, "event": "'for someone' pill"}, {"at": 0.85, "event": "arrow draws"}]),
]

def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b

OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. Most people ask Claude for the perfect workout plan, read the answer, and stop there. But the first answer is not the answer. It's a draft.",
    "BrutalistHesitantWriter",
    {"text": "Give me the perfect workout plan for my week", "triggerWords": "perfect workout plan",
     "replacementWords": "first draft of a workout plan",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Give me the perfect workout plan for my week'"},
     {"at": 0.6, "event": "backspaces 'perfect workout plan' → 'first draft of a workout plan' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive 'perfect' question and corrects it to a first draft.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Two terms. A first draft: the AI's first try at your answer — rough and generic, meant to be rewritten. And pushback: your corrections — shorter, more concrete, try again — the part that turns the draft into the answer.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "first draft", "meaning": "the AI's first try at your answer — rough and generic, meant to be rewritten"},
               {"term": "pushback", "meaning": "your corrections that turn the draft into the answer"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'first draft' lands"}, {"at": 0.55, "event": "'pushback' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: two prerequisites, one line each."}),
]
YT_PROMPT = ("Plan my dinners for the coming week. Treat your first answer as draft one, then ask me for three "
             "rounds of pushback: shorter, more concrete, and rewritten for my exact life. Keep iterating until "
             "I'd actually cook every night.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Does draft three mention something true only for you? And would you actually cook every night it lists? "
    "If yes twice, keep it. If not, push back again.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Run The Three-Pushback Drill", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: draft three mentions something true only for you.", "Check: you would actually cook every night."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, with the voice carrying the explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · HOW TO AI", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience, not AI experts",
    "source_doc": "NEW — built from scratch from the film brief (see SOURCES.md)",
    "playlist": "How to AI", "chapter_number": 8,
    "tags": ["iterate", "pushback", "prompting", "Claude", "first draft", "how to AI", "Nik Bear Brown"]},
    "beats": B}

# ── assertions ──
assert len(B) == 13, f"expected 13 beats, got {len(B)}"
manim_beats = [b for b in B if b["lane"] == "manim"]
assert len(manim_beats) == 9, f"expected 9 manim beats, got {len(manim_beats)}"
for b in manim_beats:
    cls = b["shot"]["manim"]["class"]
    assert cls.startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class {cls} must start with beat id"
    assert b["proof_gate"] == "SHOW"
    assert "qc" in b and b["qc"]["sparse_by_design"], f"{b['beat_id']}: missing sparse_by_design waiver"
total = sum(b["estimated_duration_s"] for b in B)
assert 140 <= total <= 360, f"total {total}s outside 140–360 s window"
idea = next(b for b in B if b["beat_id"] == "BIDEA")
props = idea["shot"]["remotion"]["props"]
assert props["triggerWords"] in props["text"], "BIDEA trigger must appear verbatim in text"
assert not props["triggerWords"].endswith(("?", ".", "!")), "trigger must not end in punctuation"
assert not props["replacementWords"].endswith(("?", ".", "!")), "replacement must not end in punctuation"
defs = next(b for b in B if b["beat_id"] == "BDEFS")
for t in defs["shot"]["remotion"]["props"]["terms"]:
    assert len(t["term"]) <= 17, f"BDEFS term too long (truncates): {t['term']!r}"
htf = next(b for b in B if b["beat_id"] == "BHTF")
assert YT_PROMPT in htf["narration_text"], "BHTF must read the prompt in full"
out = next(b for b in B if b["beat_id"] == "BOUT")
assert out["tail_silence_s"] == 1.0, "BOUT needs the 1.0 s tail"
assert out["kind"] == "outro_voice"
assert sheet["metadata"]["bookend_exempt"] == ["cold-open", "bvdt"]

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats;", len(manim_beats), "manim scenes; est", round(total), "s")
