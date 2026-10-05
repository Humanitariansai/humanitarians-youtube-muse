#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for slides-without-the-slog.

SHOW-TELL (Bear, 2026-09-26): one drawn illustration per body beat, minimal
labels, Liam's narration carries the explanation. NEW film (no mirror
source): the deck-building habit — outline first, then one slide per
prompt, then polish — dramatized with a friend's meeting notes.
Companion to the-long-game: that film's outline/contract idea is
referenced once by name in B03 and never re-taught.

Spine: BIDEA (hesitant writer) + BDEFS (terms card) bookends, 9 drawn body
beats (B00–B08), the Claude.ai composer Your Turn, and the spoken outro.
No cold open, no verdict card (bookend_exempt). No cards in the body: every
beat is a thing, a part, or a flow, so each passes the card test toward
"draw it" (reasons in SHOTLIST.md).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "slides-without-the-slog"
TITLE = "Slides without the slog"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00",
      "Start with the goal. A pile of rough notes in \u2014 a five-slide deck out, every slide clean enough to read from the back row. No walls of text, no tiny print. That is a deck without the slog.",
      "B00_Goal",
      "A messy notes page lands on the left; an arrow draws to three clean slide cards in a row on the right; the label 'the goal' lands.",
      [{"at": 0.1, "event": "notes page drops in"}, {"at": 0.3, "event": "arrow draws"}, {"at": 0.5, "event": "slide cards land"}, {"at": 0.8, "event": "label"}]),
 beat("B01",
      "So he pasted the notes and asked for the whole deck at once. Out came eighteen slides in about a minute \u2014 and every single one was a wall of text. Asked for everything at once, the AI did not know what mattered. So it kept everything.",
      "B01_Walls",
      "One big slide card lands covered in many text lines; stacked cards sit behind it; the label 'all at once' lands; terracotta dots flag the walls of text.",
      [{"at": 0.1, "event": "big slide lands, text lines fill it"}, {"at": 0.35, "event": "stacked cards behind"}, {"at": 0.55, "event": "label"}, {"at": 0.7, "event": "flag dots"}]),
 beat("B02",
      "Here\u2019s why. A slide is not a page. The moment a slide fills with words, the room reads the slide instead of listening to you. And an AI building the whole deck at once guesses what matters most \u2014 it cannot know what you would cut.",
      "B02_WhyRead",
      "A big slide on a screen; three audience dots at the side; their sight lines draw to the slide, not the speaker; the label 'walls get read' lands.",
      [{"at": 0.1, "event": "slide on screen"}, {"at": 0.3, "event": "audience dots"}, {"at": 0.5, "event": "sight lines draw"}, {"at": 0.8, "event": "label"}]),
 beat("B03",
      "Move one: the outline. Before a single slide exists, ask the AI for a one-line-per-slide skeleton \u2014 the whole deck, no prose. Then you do the most important job in this film: read it, fix it, approve it. The outline is the contract, same as in The long game.",
      "B03_Outline",
      "The outline card lands; its five slide rows draw in; a terracotta check stamps your approval; the label 'move one: outline'.",
      [{"at": 0.1, "event": "outline card lands"}, {"at": 0.35, "event": "slide rows draw"}, {"at": 0.8, "event": "approval check"}, {"at": 0.9, "event": "label"}]),
 beat("B04",
      "Move two: one slide per prompt. The AI drafts slide one \u2014 only slide one \u2014 with the outline beside it. Small enough to check in one sitting, because you read it before slide two starts.",
      "B04_OneSlide",
      "The outline card slides left; slide one drops in; an arrow draws card to slide; the label 'move two: one slide'; a check lands on the slide.",
      [{"at": 0.1, "event": "card slides left, slide drops"}, {"at": 0.3, "event": "arrow draws, label"}, {"at": 0.7, "event": "check lands"}]),
 beat("B05",
      "Then the polish. Read each slide and cut the words \u2014 a headline plus a few short lines, nothing more. And the words you cut are not lost: they move where they belong, into the speaker notes \u2014 the lines only you see.",
      "B05_Polish",
      "A full slide card; its text lines lift out and fade one by one; a notes card appears below and catches them; the label 'the polish: cut'.",
      [{"at": 0.1, "event": "full slide lands"}, {"at": 0.35, "event": "lines lift out"}, {"at": 0.65, "event": "notes card appears"}, {"at": 0.8, "event": "label"}]),
 beat("B06",
      "Last move: the back-row test. Step back from the screen and read the slide. If you cannot catch the headline in a few seconds, it is still too full. Cut again, then step back once more.",
      "B06_BackRow",
      "The slide shrinks toward the back of the room; the headline stays readable; a terracotta check stamps it; the label 'the back-row test'.",
      [{"at": 0.1, "event": "slide on screen"}, {"at": 0.35, "event": "slide shrinks to the back"}, {"at": 0.7, "event": "check lands"}, {"at": 0.85, "event": "label"}]),
 beat("B07",
      "Same notes, same AI. On the left: the one-prompt deck \u2014 eighteen slides of walls of text. On the right: outline first, one slide per prompt, polished at the end. A deck people can actually read.",
      "B07_SideBySide",
      "Left: the wall-of-text slides return with the label 'one giant prompt'. Right: a neat checked deck with the label 'outline, slides, polish'.",
      [{"at": 0.1, "event": "wall slides left"}, {"at": 0.25, "event": "left label"}, {"at": 0.55, "event": "neat deck right"}, {"at": 0.9, "event": "right label"}]),
 beat("B08",
      "Make it a habit. Outline first. One slide per prompt. Polish last. Anything you would show a room is a deck without the slog \u2014 build it in three moves.",
      "B08_Habit",
      "One big card lands: 'outline first' / 'one slide per prompt' / 'polish last'; a check drops on it.",
      [{"at": 0.15, "event": "rule card lands"}, {"at": 0.3, "event": "row one"}, {"at": 0.45, "event": "row two"}, {"at": 0.6, "event": "row three"}, {"at": 0.9, "event": "check"}]),
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
    "Hallo. This is Liam, in for Bear. A friend of mine dumped his meeting notes into an AI and said, make me a slide deck. What came back was eighteen slides of walls of text. Here is the three-move way from rough notes to a deck people can actually read.",
    "BrutalistHesitantWriter",
    {"text": "Make my notes into a slide deck.", "triggerWords": "Make my notes into a slide deck",
     "replacementWords": "Turn my notes into a slide deck, one move at a time",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Make my notes into a slide deck.'"},
     {"at": 0.6, "event": "backspaces the trigger and types 'Turn my notes into a slide deck, one move at a time.' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive make-the-whole-deck question and corrects it into the film's method: one move at a time.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. An outline: the skeleton of the deck, one line per slide. A slide: one idea on one card \u2014 a headline, not an essay. And the polish: cutting every slide down until it reads from the back row. That\u2019s all you need for this film.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "outline", "meaning": "the skeleton of the deck, one line per slide"},
               {"term": "slide", "meaning": "one idea on one card: a headline, not an essay"},
               {"term": "polish", "meaning": "cutting each slide down until it reads from the back row"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'outline' lands"}, {"at": 0.5, "event": "'slide' lands"}, {"at": 0.78, "event": "'polish' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]
YT_PROMPT = ("I\u2019m turning rough notes into a five-slide deck. Don\u2019t build any slides yet. "
             "First, draft a one-line-per-slide outline from my notes, then wait for my approval. "
             "My notes: [paste them here].")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Does the AI give you an outline, not slides? And is every note on it \u2014 "
    "nothing missing, nothing invented?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN", "segment": "Your First Deck Outline", "command": YT_PROMPT,
     "runningText": "paste this into Claude\u2026",
     "output": ["Check: the AI gives you an outline, not slides.", "Check: every note is on it \u2014 nothing missing, nothing invented."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Sonnet", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, with the voice carrying the explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 5.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE \u00b7 HOW TO AI", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "English-adjacent (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience, not AI experts",
    "source_doc": "NEW \u2014 built from scratch from the series brief (2026-10-05); no mirror source",
    "playlist": "How to AI",
    "companion_to": "the-long-game",
    "tags": ["AI", "prompts", "how to AI", "slide decks", "outlining", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

n_beats = len(B)
n_body = sum(1 for b in B if b["lane"] == "manim")
total = round(sum(b["estimated_duration_s"] for b in B))
assert n_beats == 13, f"expected 13 beats, got {n_beats}"
assert n_body == 9, f"expected 9 body beats, got {n_body}"
assert 150 <= total <= 360, f"total {total}s outside the 2.5\u20136 min band"
manim_beats = [b["beat_id"] for b in B if b["lane"] == "manim"]
assert manim_beats == [f"B0{i}" for i in range(9)], f"body beat ids off: {manim_beats}"
print(n_beats, "beats;", n_body, "body;", "est", total, "s")
