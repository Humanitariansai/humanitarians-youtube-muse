#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Think one step ahead" (how-to-ai #6).

SHOW-TELL (Bear, 2026-09-26). REFACTOR of the mirror repo's
claude/claude-for-education/claude-liam-prompt-tutorial-lesson-06-precognition
("Precognition: Give Claude a Scratchpad Before the Answer"), rebuilt for a
smart general audience: the source's <thinking>-tag scratchpad argument becomes
"ask Claude to think before it answers, and ask for what you'll need next" —
shown as a concrete before/after on one cast of objects (a Claude window,
a prompt slip, a thinking page, an answer page).

Every body beat is ONE drawn illustration (flat Manim, Claude palette) with
at most a few words of label; Liam's narration carries the explanation.
No composer cold open, no verdict card (bookend_exempt); the spoken
@NikBearBrown outro stays (never exempt).

Source argument: Anthropic Prompt Engineering Interactive Tutorial, Ch. 6
"Precognition (Thinking Step by Step)" — thinking out loud (a scratchpad)
before the answer makes Claude more accurate on hard tasks; token-by-token
generation means early tokens constrain later ones, so an early guess gets
defended instead of corrected.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "think-one-step-ahead"
TITLE = "Think one step ahead"


def beat(bid, narration, cls, image, show):
    est = round(len(narration.split()) / 2.5, 1)
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": est,
            "audio_file": f"mp3/beat-{bid}.mp3",
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "audio_file": f"mp3/beat-{bid}.mp3",
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


B = [
 beat("B00",
      "Here is what most people never notice. Claude does not think, then write. "
      "It thinks by writing. An answer comes out one word at a time, left to right. "
      "And once a word is written, it is written. There is no going back to change it.",
      "B00_Window",
      "A Claude window: a prompt slip drops in; an answer page slides out and words fill in left to right, one word at a time.",
      [{"at": 0.05, "event": "window lands"},
       {"at": 0.3, "event": "prompt slip drops in"},
       {"at": 0.5, "event": "words appear left to right, one at a time"}]),
 beat("B01",
      "Now watch what that means. Ask a hard question — 'which job offer should I take?' — "
      "and demand the answer straight away. The very first line is a guess. "
      "And every word after it has to follow that line. So Claude does not check its first guess. It defends it.",
      "B01_Before",
      "The same page: a terracotta dot lands on the first word and a bracket arcs from it across the page; the remaining words print out underneath.",
      [{"at": 0.1, "event": "terracotta dot lands on the first word"},
       {"at": 0.35, "event": "bracket arcs from the first word across the page"},
       {"at": 0.6, "event": "the rest of the words print underneath"}]),
 beat("B02",
      "Try it differently. Give Claude a working page before the answer page — a scratchpad. "
      "'Think it through first, step by step, then answer.' On the scratchpad, Claude is allowed to be wrong. "
      "It tries one idea, crosses it out, catches the mistake — all before one word of the answer exists.",
      "B02_Scratchpad",
      "Two page slots: a thinking page where lines scribble in, one idea gets crossed out in ink, and a correction line draws; the answer slot stays empty.",
      [{"at": 0.1, "event": "thinking page and empty answer slot land"},
       {"at": 0.35, "event": "ideas scribble onto the thinking page"},
       {"at": 0.65, "event": "one idea crossed out; a correction line draws"}]),
 beat("B03",
      "Then the answer gets written once, on top of the thinking. "
      "You can see what it weighed, and why it chose. Same question. Same Claude. Better answer. "
      "Because this time, it thought before it spoke.",
      "B03_After",
      "The thinking page rests to the side; the answer page prints cleanly left to right and a terracotta check lands beside it.",
      [{"at": 0.15, "event": "answer page prints cleanly"},
       {"at": 0.7, "event": "terracotta check lands"}]),
 beat("B04",
      "So when do you ask for the thinking page? Use the scratch-paper rule. "
      "If you would reach for scratch paper — weighing two options, a math problem, a tricky decision — "
      "ask Claude to think first. For a simple lookup, skip it. 'What is the capital of Peru' needs no thinking page. "
      "That is just extra words for nothing.",
      "B04_When",
      "Three cards: a lookup, a choice, a math problem. A thinking page drops onto the choice and the math problem; the lookup stays bare.",
      [{"at": 0.15, "event": "three cards land"},
       {"at": 0.45, "event": "thinking page drops onto 'a choice'"},
       {"at": 0.65, "event": "thinking page drops onto 'a math problem'"}]),
 beat("B05",
      "And one step further. Do not just ask for today's answer. Ask for what you will need next. "
      "'Think through the whole trip, then tell me what to pack — and what to buy before I leave.' "
      "The thinking looks ahead, so the answer arrives with tomorrow's answer already on it. "
      "Ask for tomorrow's answer, today.",
      "B05_Ahead",
      "The window again: the slip drops in, the answer page prints, then a second page — 'next' — slides out below it with a terracotta dot.",
      [{"at": 0.1, "event": "slip drops in"},
       {"at": 0.3, "event": "answer page prints"},
       {"at": 0.6, "event": "'next' page slides out below with a terracotta dot"}]),
]

OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. Everyone wants better answers from Claude. "
    "But the real trick is not asking a better question. It is asking Claude to think before it answers.",
    "BrutalistHesitantWriter",
    {"text": "How do I get Claude\nto answer better?", "triggerWords": "answer better", "replacementWords": "think first",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I get Claude'"},
     {"at": 0.55, "event": "backspaces 'answer better' → 'think first' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question and corrects it to the real one: get Claude to think first.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. A prompt: the message you type to Claude. A scratchpad: Claude's working notes, written before the answer. "
    "And word by word: how Claude writes — left to right, with no going back.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "prompt", "meaning": "the message you type to Claude"},
               {"term": "scratchpad", "meaning": "Claude's working notes, written before the answer"},
               {"term": "word by word", "meaning": "how Claude writes: left to right, no going back"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'prompt' lands"}, {"at": 0.5, "event": "'scratchpad' lands"}, {"at": 0.78, "event": "'word by word' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("I'm weighing a decision: [describe it in two sentences]. First, think it through step by step "
             "on your scratchpad: list what matters, try each side, and note anything I should double-check. "
             "Only then give me your take — and tell me what I would need next if I follow your advice.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "First: run it once more without the 'think it through first' line. Does the answer change? "
    "Second: look for the moment it changed its mind on the scratchpad. That crossed-out idea is the thinking doing the work.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Think Before It Answers", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: run it without the 'think first' line — does the answer change?",
                "Check: find where it changed its mind — that is the thinking working."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Claude", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, with the voice carrying the explanation. "
                 "The negative space is the style, so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0,
          "audio_file": "mp3/beat-BOUT.mp3",
          "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · THINK ONE STEP AHEAD",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro", "watermark": "@NikBearBrown",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience — not AI experts; every term explained, shown not told",
    "source_doc": "nikbearbrown/humanitarians-youtube-muse: claude/claude-for-education/claude-liam-prompt-tutorial-lesson-06-precognition (Anthropic Prompt Engineering Interactive Tutorial, Ch. 6: Precognition (Thinking Step by Step)); refactored for a general audience",
    "playlist": "How to AI", "chapter_number": 6,
    "tags": ["Claude", "prompting", "think step by step", "scratchpad", "chain of thought", "How to AI", "Nik Bear Brown"]},
    "beats": B}

# ── assertions ──────────────────────────────────────────────────────────────
MANIM_BEATS = [b for b in B if b["lane"] == "manim"]
assert len(B) == 10, f"expected 10 beats (BIDEA, BDEFS, B00-B05, BHTF, BOUT), got {len(B)}"
assert len(MANIM_BEATS) == 6, f"expected 6 manim body beats, got {len(MANIM_BEATS)}"
assert [b["beat_id"] for b in B] == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05", "BHTF", "BOUT"]
assert [b["shot"]["manim"]["class"] for b in MANIM_BEATS] == [
    "B00_Window", "B01_Before", "B02_Scratchpad", "B03_After", "B04_When", "B05_Ahead"]
assert all(b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_") for b in MANIM_BEATS)
total = sum(b["estimated_duration_s"] for b in B)
assert 170 <= total <= 260, f"total {total}s outside 170–260 s band"
for b in MANIM_BEATS:
    assert b.get("qc", {}).get("sparse_by_design") is True, f"{b['beat_id']} missing sparse_by_design"
    assert b.get("audio_file"), f"{b['beat_id']} missing audio_file"
# BIDEA correction contract: trigger appears verbatim in text, no trailing punctuation
bid_props = B[0]["shot"]["remotion"]["props"]
assert bid_props["triggerWords"] in bid_props["text"]
assert not bid_props["triggerWords"][-1] in "?!." and not bid_props["replacementWords"][-1] in "?!"
# BDEFS: terms short enough for ClaudeDefinitions (≤ ~17 chars, no truncation)
for t in B[1]["shot"]["remotion"]["props"]["terms"]:
    assert len(t["term"]) <= 17, f"term too long for BDEFS card: {t['term']!r}"
# narration is the only script: no empty beats
assert all(b["narration_text"].strip() for b in B)
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats;", len(MANIM_BEATS), "manim scenes; est", round(total, 1), "s")
