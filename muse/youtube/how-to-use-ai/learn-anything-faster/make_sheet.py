#!/usr/bin/env python3
"""make_sheet.py — Learn Anything Faster (Film 13, how-to-ai lane).

SHOW-TELL (Bear, 2026-09-26): one drawn isometric illustration per body
beat, minimal labels, Liam's narration (Kokoro am_onyx) explaining the
action. Claude palette. Bookends: hesitant writer, key terms, Your Turn
composer, spoken @NikBearBrown outro; no verdict card, no cold open
(bookend_exempt).

Source: NEW — built from scratch, no mirror source. The three tutor
moves (explain-it-simple / one-at-a-time quiz / Socratic mode) are
demonstrated on one concrete topic: how a mortgage works.

Run: python3 make_sheet.py
Durations: narration at ~150 wpm (words / 2.5), matching the reel clock.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "learn-anything-faster"
TITLE = "Learn Anything Faster"

YT_PROMPT = ("Be my tutor on [your topic]. First, explain it like I am smart but new to it. "
             "Then quiz me, one question at a time, and do not move on until I get it right. "
             "When I ask why, do not give me the answer - ask me leading questions instead.")


def beat(bid, act, narration, cls, image, show):
    return {"beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}


B = [
    beat("B00", "show-tell",
         "Our demo topic: how a mortgage works. Almost everyone signs one, and almost no one feels "
         "they understand it. So it makes the perfect student. Here is the house. Watch what the "
         "three moves do to it.",
         "B00_House",
         "A kraft isometric house drops onto the stage with a landing shadow; the label 'a mortgage' lands beside it.",
         [{"at": 0.1, "event": "landing shadow grows, house drops in"}, {"at": 0.35, "event": "label 'a mortgage' lands"}]),
    beat("B01", "show-tell",
         "Move one: explain it like I am smart but new to it. That one line changes everything the AI "
         "gives you. A mortgage, plainly: you borrow a large sum to buy the house. Interest is the price "
         "of borrowing, a little extra on top. And you pay it all back, bit by bit, over many years. "
         "Three blocks. That is the whole machine.",
         "B01_ExplainSimple",
         "The tutor card fades in; the house opens and three kraft blocks drop into a row beneath it, "
         "labelled 'borrow', 'interest', 'pay back'; a terracotta dot hops block to block as the voice walks the three.",
         [{"at": 0.08, "event": "tutor card fades in"}, {"at": 0.3, "event": "three blocks drop from the house"},
          {"at": 0.55, "event": "dot hops to 'borrow'"}, {"at": 0.7, "event": "dot hops to 'interest'"},
          {"at": 0.85, "event": "dot hops to 'pay back'"}]),
    beat("B02", "show-tell",
         "Move two: quiz me, one question at a time, and do not move on until I get it. The AI asks: "
         "what is interest, in a mortgage? You answer, in your own words. It checks you, and only when "
         "you are right does the next question arrive. A wrong answer is not punished. It is just not yet. "
         "The AI stays on the question until the idea is yours.",
         "B02_QuizMode",
         "A '?' pill drops from the tutor to the learner; an answer line runs back; a terracotta check "
         "stamps it; only then does the second '?' pill arrive. Tag: 'one at a time'.",
         [{"at": 0.35, "event": "'?' pill drops to the learner"}, {"at": 0.45, "event": "answer line runs back"},
          {"at": 0.65, "event": "terracotta check stamps it"}, {"at": 0.85, "event": "second '?' pill arrives"}]),
    beat("B03", "show-tell",
         "Move three: Socratic mode. Do not give me the answer. Ask me leading questions. You ask: why "
         "does a little extra each month save so much? A plain answer would just tell you. A tutor asks "
         "back: when you pay, where does the money go first, the loan itself, or the interest on it? You "
         "answer. It asks a sharper question. And the insight lands, because you built it. The AI never "
         "hands you the answer. It walks you to it.",
         "B03_Socratic",
         "Two option pills, 'the loan' / 'the interest', land by the learner; the learner's terracotta "
         "answer dot taps 'the interest'; a sharper question arrow cycles; the 'aha' dot lands above the learner.",
         [{"at": 0.2, "event": "option pills 'the loan' / 'the interest' land"},
          {"at": 0.6, "event": "answer dot taps 'the interest'"},
          {"at": 0.8, "event": "sharper question arrow cycles"},
          {"at": 0.92, "event": "'aha' dot lands above the learner"}]),
    beat("B04", "show-tell",
         "The house was only the demo. The moves transfer to anything: the new rule at work, the tool "
         "everyone assumes you know, the topic you keep avoiding. Same three moves. Different house. "
         "Tonight, pick yours.",
         "B04_YourTopic",
         "The house slides aside and shrinks; a white card with '?' lands in its place, labelled 'your "
         "topic'; three terracotta dots pop in beside it.",
         [{"at": 0.15, "event": "house slides aside, '?' card lands"}, {"at": 0.4, "event": "label 'your topic' lands"},
          {"at": 0.75, "event": "three terracotta dots pop in"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
    remotion("BIDEA", "the question",
             "Hallo. This is Liam, in for Bear. Most of us open the AI the same way: we ask for the "
             "answer. But the fastest way to learn anything is to ask it to teach you. So the question "
             "is not give me the answer. It is teach me like a tutor.",
             "BrutalistHesitantWriter",
             {"text": "Give me the answer\nabout mortgages",
              "triggerWords": "Give me the answer", "replacementWords": "Teach me like a tutor",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
              "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'Give me the answer'"},
              {"at": 0.6, "event": "backspaces 'Give me the answer' -> 'Teach me like a tutor' on the spoken correction"}],
             lead_silence_s=0.8, motion_claim="The writer types the naive answer-ask and corrects it to the tutor ask.",
             qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms, plainly. Tutor mode: telling the AI to teach you, instead of doing the work "
             "for you. Quiz mode: the AI asks one question at a time, and waits until you get it. "
             "Socratic mode: the AI teaches by asking questions, never handing you the answer, named "
             "for Socrates, the Greek philosopher who taught that way.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "tutor mode", "meaning": "the AI teaches you instead of doing the work for you"},
                        {"term": "quiz mode", "meaning": "one question at a time, and it waits until you get it"},
                        {"term": "Socratic mode", "meaning": "it asks questions instead of giving answers, named for Socrates"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'tutor mode' lands"}, {"at": 0.5, "event": "'quiz mode' lands"},
              {"at": 0.78, "event": "'Socratic mode' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Paste this into the AI, with your own topic where it says your topic. Be my tutor on "
    "your topic. First, explain it like I am smart but new to it. Then quiz me, one question at a time, "
    "and do not move on until I get it right. When I ask why, do not give me the answer. Ask me leading "
    "questions instead. Then check two things yourself. Did you answer in your own words, before looking? "
    "And did you let it stay on a question you got wrong, instead of rushing past it?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "AI \u00b7 YOUR TURN", "segment": "Learn Anything Faster",
     "command": YT_PROMPT,
     "runningText": "paste this into the AI\u2026",
     "output": ["Check: you answered in your own words, before looking.",
                "Check: you let it stay on a question you got wrong."],
     "folderLabel": "@NikBearBrown", "modelLabel": "any AI", "effortLabel": "Low"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
     {"at": 0.1, "event": "the tutor prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
                 "minimal labels, with the voice carrying the explanation. The negative space is the style, "
                 "so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. Liam, in for Bear. At Nik Bear Brown.",
          "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "AI \u00b7 LEARNING", "skill": "show-tell",
    "style_preset": "show-tell", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24,
    "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience — not AI experts; every term explained plainly",
    "source_doc": "NEW — built from scratch, no mirror source. Mortgage mechanics checked against CFPB/Federal Reserve glossaries and amortization references (see SOURCES.md); Socratic method checked against standard references.",
    "playlist": "How to AI", "chapter_number": 13,
    "tags": ["AI tutor", "learn faster", "Socratic method", "quizzing", "how mortgages work", "Nik Bear Brown"]},
    "beats": B}

if __name__ == "__main__":
    beats = sheet["beats"]
    assert len(beats) == 9, len(beats)
    assert [b["beat_id"] for b in beats] == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "BHTF", "BOUT"]
    body = [b for b in beats if b["lane"] == "manim"]
    assert len(body) == 5, len(body)
    for b in body:
        assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), b["beat_id"]
    htf = next(b for b in beats if b["beat_id"] == "BHTF")
    assert "Be my tutor on your topic" in htf["narration_text"], "handoff prompt read in full"
    assert "Ask me leading questions instead" in htf["narration_text"], "Socratic line read in full"
    b04 = next(b for b in beats if b["beat_id"] == "B04")
    assert "transfer" in b04["narration_text"].lower(), "transfer beat must say the moves transfer"
    total = sum(b["estimated_duration_s"] for b in beats)
    assert 170 <= total <= 240, f"total {total}s outside 170-240s band"
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
    print(f"beats={len(beats)} body={len(body)} total={total}s (~{int(total//60)}m{int(total%60):02d}s)")
    print("beat_sheet.json written")
