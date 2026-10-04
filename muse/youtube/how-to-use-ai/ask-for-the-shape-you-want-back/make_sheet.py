#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Ask for the Shape You Want Back" (How to AI #4).

SHOW-TELL (Bear, 2026-09-26): one simple isometric Manim drawing per body beat,
minimal on-screen labels, Liam's narration (Kokoro am_onyx) carrying every idea.
Teardown register, channel claude-liam, general audience (not AI experts).

REFACTOR of claude/claude-for-education/claude-liam-prompt-tutorial-lesson-05-formatting-output
in nikbearbrown/humanitarians-youtube-muse. Note: the source folder's beat_sheet.json
carries mismatched narrations (about grounding/hallucinations, likely pasted from another
lesson); the topic, README and description.txt all describe formatting output — tables,
bullets, length, tone, and the prefill technique. This refactor rebuilds from the intended
argument (description.txt) plus Anthropic's Lesson 05 source material ("Prefill Claude's
response" docs). See SOURCES.md and FACTCHECK.md.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "ask-for-the-shape-you-want-back"
TITLE = "Ask for the Shape You Want Back"

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

B = [
 beat("B00", "Everything starts with the facts. Picture them as loose blocks in a box. Two laptops, their prices, their batteries, their weights. Your prompt decides what those blocks come out as. Same facts, any shape. This film is about how to ask for the one you actually need.",
      "B00_BlocksBox", "An open cardboard box; four fact blocks drop in one by one; the label 'the facts' lands beside it.",
      [{"at": 0.1, "event": "open box lands"}, {"at": 0.25, "event": "blocks drop in"}, {"at": 0.6, "event": "label 'the facts'"}]),
 beat("B01", "Here is what happens when you do not ask for a shape. You ask which laptop to buy, and Claude answers in prose. Every fact is in there, but it is buried. The price hides in the middle of a paragraph, and you have to read the whole thing to find the one number you came for.",
      "B01_BuriedInProse", "A page dense with grey text lines; one terracotta dot buried mid-page; a scan line sweeps down to it; the label 'buried' lands beside the page.",
      [{"at": 0.1, "event": "prose page lands"}, {"at": 0.35, "event": "the number, buried"}, {"at": 0.55, "event": "scan line finds it"}]),
 beat("B02", "So name the shape. Write: compare the two laptops in a table, with columns for price, battery, and weight. Same facts. But now they line up in rows and columns, and your eye finds the winner in seconds instead of minutes.",
      "B02_AskForATable", "A prompt pill reads 'table: price, battery, weight'; a table card builds beneath it — grey header band, three columns, three rows — and a check lands on the winning row, labelled 'the winner'.",
      [{"at": 0.1, "event": "prompt pill"}, {"at": 0.3, "event": "table builds"}, {"at": 0.7, "event": "check on the winner"}]),
 beat("B03", "Next, give the answer a size. Write: keep it under a hundred words. The long answer shrinks to the short one. Nothing important falls off. You just get the answer, not the guided tour around it. If it is still too long, ask again with a smaller number. You set the budget.",
      "B03_GiveItASize", "A tall page of many lines with a '340' word counter; an ink trim line draws across it; the lower half falls away; the counter becomes '96'; the label 'under 100 words' lands beside.",
      [{"at": 0.1, "event": "long page + 340 words"}, {"at": 0.35, "event": "trim line"}, {"at": 0.55, "event": "page shortens, 96 words"}]),
 beat("B04", "Then pick the tone. Write this as a friendly email, or write this as a formal letter: same facts, two different suits. Claude can wear either one. Just tell it which suit to put on. A bedtime story, a business memo, a text to a friend — the tone is yours to choose, but only if you say so.",
      "B04_PickTheTone", "Two letter pages side by side, labelled 'friendly email' and 'formal letter'; a terracotta check grows on the friendly one.",
      [{"at": 0.1, "event": "two letters"}, {"at": 0.3, "event": "tone labels"}, {"at": 0.55, "event": "check picks one"}]),
 beat("B05", "Match the shape to where the answer is going. Something you will read on your phone wants short steps or bullets. A school report wants headings and paragraphs. And if a program will use the answer, ask for JSON — a strict format machines read, written in curly braces.",
      "B05_MatchTheDestination", "Three containers labelled 'phone', 'report', 'code': bullets drop into the phone, a heading bar into the report, and an opening curly brace with JSON lines into the code panel.",
      [{"at": 0.1, "event": "three destinations"}, {"at": 0.35, "event": "labels land"}, {"at": 0.6, "event": "each shape drops into its home"}]),
 beat("B06", "For developers, there is an even stronger version of this. When you call Claude through its API — the programming interface — you can write the first character of the answer yourself: an opening curly brace. Claude has to continue from there, so it cannot dodge the format. Anthropic, who build Claude, document this trick as prefilling.",
      "B06_Prefill", "A blank page; a large ink opening brace fades in at its top; JSON lines fill in below it with one terracotta dot; the label 'prefill' lands beside the page.",
      [{"at": 0.1, "event": "blank page"}, {"at": 0.35, "event": "the brace"}, {"at": 0.6, "event": "JSON fills in from it"}]),
 beat("B07", "One caution before we finish. A tidy table is easier to trust, and that is exactly the danger. The format never makes the facts true. If the answer matters — money, medicine, anything with consequences — check the numbers before you copy the layout.",
      "B07_CheckTheFacts", "A small table with a check for its format; a terracotta circle draws around one number cell; the label 'check the facts' lands beside it.",
      [{"at": 0.1, "event": "tidy table + check"}, {"at": 0.45, "event": "circle around one number"}]),
 beat("B08", "And do not over-engineer the ask. A table, four columns, under forty words, written like a pirate — congratulations, you have spent more effort designing the answer than reading it would have taken. Give the shape, the size, and the tone. Then stop.",
      "B08_ThenStop", "A prompt pill collects clutter labels ('table', '40 words', 'pirate voice') that pile up; they fall away and one clean pill 'table, 100 words, friendly' remains, labelled 'then stop'.",
      [{"at": 0.1, "event": "the ask piles up"}, {"at": 0.45, "event": "clutter falls away"}, {"at": 0.7, "event": "one clean ask"}]),
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
    "Hallo. This is Liam, in for Bear. Ask Claude a vague question, and you will get a vague answer back. The fix is simple. Ask for the shape you want back.",
    "BrutalistHesitantWriter",
    {"text": "Which laptop should I buy — tell me everything\ncompare the two in a table: price, battery, weight, under 120 words",
     "triggerWords": "tell me everything", "replacementWords": "ask for the shape",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types the vague ask"}, {"at": 0.6, "event": "backspaces 'tell me everything' → 'ask for the shape' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the vague ask and corrects it to the film's thesis: ask for the shape.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms, before we start. A prompt: the text you send Claude — your question plus your instructions. Output format: the shape of Claude's reply — a table, a list, a paragraph, or code. And prefill: writing the first few words of Claude's answer yourself, so it has to continue your shape.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "prompt", "meaning": "the text you send Claude — your question plus your instructions"},
               {"term": "output format", "meaning": "the shape of Claude's reply — a table, a list, a paragraph, or code"},
               {"term": "prefill", "meaning": "writing the first words of Claude's answer yourself, so it continues your shape"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'prompt' lands"}, {"at": 0.5, "event": "'output format' lands"}, {"at": 0.78, "event": "'prefill' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Compare two phones I am choosing between in a table with columns for price, battery life, "
             "and camera. Keep the whole answer under 120 words, in a friendly tone.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. Does every column "
    "you asked for actually show up? And is the answer roughly the length you asked for? If not, point at the "
    "exact part that is wrong, and ask again.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "HOW TO AI · YOUR TURN", "segment": "Ask for the Shape", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: every column you asked for actually shows up.", "Check: the answer is roughly the length you asked for."],
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

total_s = sum(b["estimated_duration_s"] for b in B)
manim_beats = [b for b in B if b["lane"] == "manim"]
bookend_beats = [b for b in B if b["lane"] == "bookend"]
assert len(B) == 13, f"expected 13 beats, got {len(B)}"
assert len(manim_beats) == 9, f"expected 9 manim beats, got {len(manim_beats)}"
assert len(bookend_beats) == 4, f"expected 4 bookend beats, got {len(bookend_beats)}"
assert 200 <= total_s <= 360, f"total {total_s:.1f}s outside the 3–6 minute target"
ids = [b["beat_id"] for b in B]
assert ids == ["BIDEA", "BDEFS"] + [f"B{i:02d}" for i in range(9)] + ["BHTF", "BOUT"], f"beat order wrong: {ids}"
assert all(b["voice"] == "am_onyx" for b in B), "every beat must voice am_onyx"
for b in B:
    assert b["narration_text"].strip(), f"{b['beat_id']} has empty narration"

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · FORMATTING", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience — NOT AI experts; every term explained in plain language, shown rather than told",
    "source_doc": "mirror repo nikbearbrown/humanitarians-youtube-muse: claude/claude-for-education/claude-liam-prompt-tutorial-lesson-05-formatting-output (README.md, description.txt; beat_sheet.json narrations mismatched — see SOURCES.md) + Anthropic docs 'Prefill Claude's response' (read 2026-10-03)",
    "playlist": "How to AI", "chapter_number": 4,
    "tags": ["prompting", "output format", "tables", "prefill", "Claude", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats;", len(manim_beats), "manim;", "est", round(total_s), "s")
