#!/usr/bin/env python3
"""make_sheet.py — Your Language Coach (How to AI, Wave 6 "Making things").

SHOW-TELL (Bear, 2026-09-26): one drawn isometric illustration per body
beat, minimal labels, Liam's narration (Kokoro am_onyx) explaining the
action. Claude palette. Bookends: hesitant writer, key terms, Your Turn
composer, spoken @NikBearBrown outro; no verdict card, no cold open
(bookend_exempt).

Companion to `learn-anything-faster` (the tutor film): there the AI was
the tutor for any subject; here it is the coach for any language. The
companion's three moves are referenced, never re-taught.

Source: NEW — built from scratch. The coach moves (conversation practice,
instant corrections, roleplay, level dials) are prescribed user actions;
the one concrete grammar demo (French age takes "have", not "am") is
checked against French grammar references (see FACTCHECK.md).

Kokoro-safety: the narration speaks NO French — the one French rule is
stated in English ("I have twelve years"). Greeting is "Hallo" (clean
per the skill). No acronyms, no version numbers, no pricing tiers.

Run: python3 make_sheet.py
Durations: narration at ~150 wpm (words / 2.5), matching the reel clock.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "your-language-coach"
TITLE = "Your Language Coach"

YT_PROMPT = ("Be my French conversation coach. Speak to me mostly in French. "
             "When I make a mistake, correct it right away, and explain the rule in plain English. "
             "Start by asking me to introduce myself. If I say slower, slow down. "
             "If I say roleplay, become a waiter in a cafe in Paris.")


def beat(bid, act, narration, cls, image, show):
    return {"beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}


B = [
    beat("B00", "show-tell",
         "Meet your coach. This bubble is you. This one is the AI, your language coach. "
         "Pick the language you want to speak. Then just start talking, the way you would with a real person. "
         "There is no lesson plan, no vocabulary list. The conversation is the lesson.",
         "B00_Coach",
         "Two speech bubbles face off on the stage: yours (kraft) and the coach's (white, terracotta lamp). "
         "A dotted line hops from you to the coach and a reply dot comes back; labels 'you' and 'coach' land beside them.",
         [{"at": 0.1, "event": "coach bubble drops in with its lamp"},
          {"at": 0.3, "event": "your bubble fades in; labels land"},
          {"at": 0.6, "event": "dots travel you-to-coach and back"}]),
    beat("B01", "show-tell",
         "First, the coach gives you patience. In real life, you would be embarrassed to stumble. "
         "Here, you stammer, you back up, you try the sentence a third time, and the coach just waits. "
         "There is no clock, no eye roll, nobody getting bored. The AI has nowhere else to be.",
         "B01_Patience",
         "Your bubble sends three try-lines to the coach; the first two get a gentle terracotta squiggle over them "
         "and only the third lands a terracotta check. The coach bubble never moves. Tag beside: 'no clock'.",
         [{"at": 0.25, "event": "first try-line; squiggle over it"},
          {"at": 0.5, "event": "second try-line; squiggle over it"},
          {"at": 0.75, "event": "third try-line; terracotta check; 'no clock' tag lands"}]),
    beat("B02", "show-tell",
         "Second, corrections, instant ones. You tell it your age in French. You say: I am twelve. "
         "Wrong verb. The coach swaps it for the right words, immediately, before the mistake can settle into a habit.",
         "B02_Correction",
         "Your 'I am twelve' pill travels to the coach; a terracotta caret strikes it; the corrected "
         "'I have twelve years' pill travels back with a terracotta check. Tag beside the arrow: 'instant'.",
         [{"at": 0.2, "event": "'I am twelve' pill travels to the coach"},
          {"at": 0.5, "event": "terracotta caret strikes it"},
          {"at": 0.7, "event": "'I have twelve years' pill returns with a check; 'instant' tag lands"}]),
    beat("B03", "show-tell",
         "And it doesn't just fix the word. It tells you the rule, in plain English: in French you don't say "
         "I am twelve. You say I have twelve years. A fix teaches the sentence. The rule teaches every sentence after it.",
         "B03_Rule",
         "The corrected pill stays on stage; a white rule card grows beside it carrying the line "
         "'I have twelve years', labelled 'the rule'.",
         [{"at": 0.15, "event": "corrected pill already on stage"},
          {"at": 0.4, "event": "rule card grows; the line 'I have twelve years' lands on it"},
          {"at": 0.75, "event": "label 'the rule' lands beside the card"}]),
    beat("B04", "show-tell",
         "Third: roleplay. Tell it: you are the waiter, I am the customer, we are in a cafe in Paris. "
         "Suddenly you are not practicing French, you are ordering coffee, in French, with someone playing along. "
         "The situation makes the words stick, because this time you actually needed them.",
         "B04_Roleplay",
         "A striped awning drops over the coach card, which sits behind a kraft counter; label 'cafe' lands. "
         "Your order pill travels to the coach; a reply pill comes back.",
         [{"at": 0.2, "event": "awning drops over the coach; 'cafe' label lands"},
          {"at": 0.55, "event": "order pill travels to the coach"},
          {"at": 0.8, "event": "reply pill comes back"}]),
    beat("B05", "show-tell",
         "Fourth: it meets you where you are. Too fast? Say slower, and it slows down. Lost? Ask it to explain "
         "in English. Bored? Tell it to raise the level. You turn the dials: the speed, the difficulty, the mix "
         "of your language and the new one. A human tutor reads your face. This one reads your words, and adjusts.",
         "B05_Level",
         "A 'slower' pill travels from you to the coach; the coach's long reply bubble slides aside and a short "
         "reply bubble grows in its place. Label beside: 'your level'.",
         [{"at": 0.2, "event": "'slower' pill travels to the coach"},
          {"at": 0.5, "event": "long reply bubble slides aside"},
          {"at": 0.65, "event": "short reply bubble grows; 'your level' label lands"}]),
    beat("B06", "show-tell",
         "And the coach is not only French. Tonight it is French. Tomorrow, you just name the language: Spanish, "
         "Japanese, the language your grandmother spoke, and it answers. Hola. Bonjour. Konnichiwa. Salaam. "
         "This film has a companion: Learn Anything Faster, where the AI was your tutor for any subject. "
         "There, a tutor. Here, a coach. Same instinct, different game.",
         "B06_Languages",
         "The coach card sits center; four hello pills pop in around it in turn: 'hola', 'bonjour', "
         "'konnichiwa', 'salaam'. Tag beside: 'name it'.",
         [{"at": 0.15, "event": "coach card on stage"},
          {"at": 0.45, "event": "'hola' and 'bonjour' pop in"},
          {"at": 0.65, "event": "'konnichiwa' and 'salaam' pop in; 'name it' tag lands"}]),
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
             "Hallo. This is Liam, in for Bear. Most of us learn a language the app way: flashcards, "
             "grammar drills, streaks. But what makes a language stick is saying it out loud, to someone, "
             "who fixes you gently. So the question isn't: how do I study French grammar. "
             "The question is: how do I practice speaking French.",
             "BrutalistHesitantWriter",
             {"text": "How do I\nstudy French grammar?", "triggerWords": "study French grammar",
              "replacementWords": "practice speaking French",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2,
              "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'How do I study'"},
              {"at": 0.6, "event": "backspaces 'study French grammar' -> 'practice speaking French' on the spoken correction"}],
             lead_silence_s=0.8,
             motion_claim="The writer types the naive study question and corrects it to the real one: practicing speaking.",
             qc={"sparse_by_design": True,
                 "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms, plainly. Practice: speaking the language with the AI, back and forth, out loud or "
             "in text. Correction: the AI fixing your mistake the moment you make it, and telling you why. "
             "And roleplay: pretending a scene is real, a shop, a cafe, so you practice a situation, not just words.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "practice",
                         "meaning": "speaking the language with the AI, back and forth, out loud or in text"},
                        {"term": "correction",
                         "meaning": "the AI fixing your mistake the moment you make it, and telling you why"},
                        {"term": "roleplay",
                         "meaning": "pretending a scene is real, so you practice a situation, not just words"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'practice' lands"},
              {"at": 0.5, "event": "'correction' lands"},
              {"at": 0.78, "event": "'roleplay' lands"}], gate="CARD",
             qc={"sparse_by_design": True,
                 "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]
YT_NARRATION = ("Your turn. Paste this into the AI: " + YT_PROMPT +
                " Then check two things yourself. Did it correct you the moment you slipped, "
                "with the rule in plain English? And did you say something in French that you would "
                "not have dared to say to a real person? If yes twice, you have a coach.")
YOURTURN = remotion("BHTF", "your turn", YT_NARRATION,
                    "ClaudeComposerAsk",
                    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN",
                     "segment": "Your Language Coach", "command": YT_PROMPT,
                     "runningText": "paste this into the AI\u2026",
                     "output": ["Check: it corrected you the moment you slipped, with the rule in plain English.",
                                "Check: you said something in French you would not have dared with a real person."],
                     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
                    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
                     {"at": 0.1, "event": "the prompt types in full"},
                     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
                 "minimal labels, with the voice carrying the explanation. The negative space is the style, so "
                 "only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
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
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI \u00b7 MAKING THINGS", "skill": "show-tell",
    "style_preset": "show-tell", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9",
    "width": 3840, "height": 2160, "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card "
                              "(Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses "
                              "as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays."),
    "audience": "smart, pragmatic general audience, not AI experts; every term explained in-line",
    "source_doc": "NEW (built from scratch); French age grammar checked against French grammar references (see FACTCHECK.md)",
    "series_note": "How to AI, Wave 6 'Making things'; companion to learn-anything-faster (the tutor film) \u2014 referenced, not re-taught",
    "playlist": "How to AI", "chapter_number": 44,
    "tags": ["language learning", "conversation practice", "AI tutor", "roleplay", "French", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

# ── assertions: the sheet must be render-ready ─────────────────────────────
n_body = sum(1 for b in B if b["lane"] == "manim")
total = sum(b["estimated_duration_s"] for b in B)
assert len(B) == 11, f"expected 11 beats, got {len(B)}"
assert n_body == 7, f"expected 7 manim body beats, got {n_body}"
assert B[0]["beat_id"] == "BIDEA" and B[-1]["beat_id"] == "BOUT" and B[-2]["beat_id"] == "BHTF"
assert all(b["voice"] == "am_onyx" for b in B), "every beat must carry the Kokoro voice code am_onyx"
for b in B:
    assert b["beat_id"] and b["narration_text"], f"beat {b['beat_id']} missing id/narration"
    assert b.get("estimated_duration_s") or b.get("actual_duration_s"), f"beat {b['beat_id']} missing duration"
    sh = b["shot"]
    if sh["type"] == "GRAPHIC":
        assert sh["manim"]["class"].startswith(b["beat_id"]), f"{b['beat_id']}: manim class name mismatch"
    else:
        assert sh["remotion"]["pattern"], f"{b['beat_id']}: remotion pattern missing"
bhtf = B[-2]
assert YT_PROMPT in bhtf["narration_text"], "BHTF must read the viewer prompt in full"
assert "YOUR TURN" in bhtf["shot"]["remotion"]["props"]["topic"]
# hesitant-writer law: trigger must appear verbatim in text; neither may end in punctuation
hw = B[0]["shot"]["remotion"]["props"]
assert hw["triggerWords"] in hw["text"], "triggerWords must appear verbatim in text"
assert not hw["triggerWords"][-1] in "?!.," and not hw["replacementWords"][-1] in "?!.,"
# terms card law: no term longer than ~17 chars (ClaudeDefinitions truncates)
for t in OPEN[1]["shot"]["remotion"]["props"]["terms"]:
    assert len(t["term"]) <= 17, f"term too long: {t['term']}"
assert 170 <= total <= 280, f"total {total}s outside the 3-6 min band"
print(len(B), "beats;", n_body, "manim;", "est", round(total), "s")
