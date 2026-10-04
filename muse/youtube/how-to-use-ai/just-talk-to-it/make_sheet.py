#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Just talk to it" (film 18 of the How-to-AI series).

SHOW-TELL (Bear, 2026-09-26): one drawn illustration per beat, minimal labels,
Liam's narration (Kokoro am_onyx) carries the explanation. No composer cold
open, no verdict card (bookend_exempt); spoken @NikBearBrown outro stays.

Premise: many people don't know they can just talk to the AI. Show how to
start a voice conversation (the microphone/waveform icon pattern, kept generic
so the film doesn't rot), when voice wins, when typing wins, and three tips.
Source: built from scratch (NEW). Facts verified 2026-10-03 (see FACTCHECK.md).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "just-talk-to-it"
TITLE = "Just talk to it"

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

B = [
 beat("B00", "Voice mode starts with one tap. Most AI apps, including Claude's, have it. Look for a microphone or waveform icon in the app you use. Tap it, and you are talking.",
      "B00_MicHero", "A phone-style card holds a big mic button; three sound-wave arcs grow out of it; the label 'mic' sits beside it.",
      [{"at": 0.1, "event": "card + mic button land"}, {"at": 0.4, "event": "label 'mic' with leader"}, {"at": 0.6, "event": "wave arcs grow"}]),
 beat("B01", "Tap the icon and speak in full sentences, the way you would to a person. The app writes down your words, the AI answers out loud, and you go back and forth like a phone call.",
      "B01_StartTalk", "A 'you' head on the left and a 'claude' panel on the right; waves travel from you to Claude, then back the other way.",
      [{"at": 0.1, "event": "you + claude land, labelled"}, {"at": 0.4, "event": "waves you → claude"}, {"at": 0.65, "event": "waves claude → you"}]),
 beat("B02", "Talking wins when you are thinking out loud. Brainstorming a project, naming a business, planning a trip. Say half-formed ideas and let the AI catch them, sort them, and play them back to you.",
      "B02_Brainstorm", "A head with thought dots rising; waves carry them to an idea bulb that lights with a terracotta glow.",
      [{"at": 0.1, "event": "head + bulb land"}, {"at": 0.4, "event": "thought dots rise"}, {"at": 0.6, "event": "waves reach the bulb, it lights"}]),
 beat("B03", "It wins when your hands are busy. Cooking is the classic: flour on your fingers, a recipe question in your head. Ask out loud, get the answer out loud, and never touch the screen.",
      "B03_KitchenHands", "A steaming pot beside a head; waves travel between them while the steam keeps rising.",
      [{"at": 0.1, "event": "pot + steam + head land"}, {"at": 0.4, "event": "steam rises"}, {"at": 0.6, "event": "waves pot ↔ head"}]),
 beat("B04", "It wins when you need to rehearse. A job interview, a hard conversation, a phone call you are dreading. Say it out loud to the AI first, and hear how it lands.",
      "B04_ToughTalk", "Two heads face each other with waves between them; a terracotta check lands above the listener.",
      [{"at": 0.1, "event": "two heads land, 'rehearse' label"}, {"at": 0.5, "event": "waves between the heads"}, {"at": 0.7, "event": "check lands on the listener"}]),
 beat("B05", "And it wins for language practice. Pick a language and talk. The AI answers in that language: a patient conversation partner who never gets bored and corrects you gently.",
      "B05_Language", "A head talks to a speech bubble that answers with sound; the label 'bonjour' sits beside the bubble.",
      [{"at": 0.1, "event": "head + bubble land"}, {"at": 0.5, "event": "waves head → bubble, answer arcs inside"}]),
 beat("B06", "But typing wins when you need to keep something. A plan, an address, a recipe. Voice vanishes, text stays. If you will need it later, type it, or ask for it in writing.",
      "B06_KeepIt", "A page slides down into an open tray; a terracotta check lands on the tray; the label 'keep' sits beside it.",
      [{"at": 0.1, "event": "tray lands"}, {"at": 0.4, "event": "page drops in"}, {"at": 0.7, "event": "check lands"}]),
 beat("B07", "Typing wins when the instructions must be exact. A password, a number, a name spelled right. Speech recognition still mishears things. Ears make mistakes that eyes do not.",
      "B07_Precise", "Two cards: 'typed' with straight grey lines, 'heard' with garbled arcs and an ink X over it.",
      [{"at": 0.1, "event": "both cards land"}, {"at": 0.6, "event": "X lands on the 'heard' card"}]),
 beat("B08", "And typing wins in public. On a train, in a waiting room, at your desk among coworkers. Nobody wants to hear your side of the conversation, so type quietly.",
      "B08_PublicPlaces", "Three heads in a row; a mic button with a slash gives way to a keyboard bar; the label 'type quietly' sits below.",
      [{"at": 0.1, "event": "three heads land"}, {"at": 0.4, "event": "mic crossed out"}, {"at": 0.65, "event": "mic becomes a keyboard"}]),
 beat("B09", "Three tips for talking well. One: speak in full thoughts, not fragments. Finish the idea before you pause. A complete sentence gives the AI something real to work with.",
      "B09_FullThoughts", "Broken dim wave fragments on the left; one complete ink wave on the right, running into a page.",
      [{"at": 0.1, "event": "fragments land, 'fragments' label"}, {"at": 0.5, "event": "the full wave grows; 'full thoughts' label"}]),
 beat("B10", "Two: interrupt freely. If it starts rambling, just talk over it. Say shorter, or skip to the point. A voice conversation is allowed to be rude in a way typing never is.",
      "B10_Interrupt", "A long wave runs across the stage; an ink arrow slashes through it and the far half fades out; the label 'interrupt' sits above.",
      [{"at": 0.1, "event": "the long wave lands"}, {"at": 0.5, "event": "arrow cuts it; the far half fades"}]),
 beat("B11", "Three: when you are done, ask for a summary. Say, summarize what we decided, in text. The spoken part did the thinking. The written part does the remembering.",
      "B11_Summarize", "Dim talk-waves on the left, an arrow, and a summary page on the right with the label 'summary' below it.",
      [{"at": 0.1, "event": "waves + page land"}, {"at": 0.5, "event": "arrow draws; page lines settle"}]),
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
    "Hola. This is Liam, in for Bear. Most people type to the AI. But sometimes talking beats typing. The real question is not only how you talk to it, but when.",
    "BrutalistHesitantWriter",
    {"text": "How do I turn on voice mode\nin the AI app?", "triggerWords": "How do I turn on voice mode", "replacementWords": "when should I talk to the AI instead of typing",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I turn on voice mode'"}, {"at": 0.6, "event": "backspaces the how-to into 'when should I talk to the AI instead of typing' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive how-to question and corrects it to the real one: when to talk instead of type.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Voice mode: talking to the AI out loud instead of typing. A transcript: the written record of everything said in a voice conversation. A summary: the short text version of that conversation.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "voice mode", "meaning": "talking to the AI out loud instead of typing"},
               {"term": "transcript", "meaning": "the written record of everything said in a voice conversation"},
               {"term": "summary", "meaning": "the short text version of a conversation"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'voice mode' lands"}, {"at": 0.5, "event": "'transcript' lands"}, {"at": 0.78, "event": "'summary' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Open voice mode in the AI app you use, and brainstorm out loud with me for two minutes: "
             "a weekend trip, a project, or a gift idea. Then say: summarize our plan in text.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Did speaking beat typing for getting ideas out? And is the summary something you would actually keep?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Talk To It Once",
     "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: did speaking beat typing for getting ideas out?", "Check: is the summary something you would actually keep?"],
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

# ── assertions ──────────────────────────────────────────────────────────────
assert len(B) == 16, f"expected 16 beats, got {len(B)}"
body = [b for b in B if b.get("lane") == "manim"]
assert len(body) == 12, f"expected 12 manim body beats, got {len(body)}"
assert [b["beat_id"] for b in body] == [f"B{i:02d}" for i in range(12)], "body beat ids out of order"
for b in body:
    assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class name must start with beat id"
    assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    assert 6 <= b["estimated_duration_s"] <= 20, f"{b['beat_id']}: duration {b['estimated_duration_s']}s out of band"
total = sum(b["estimated_duration_s"] for b in B)
assert 170 <= total <= 280, f"total {total}s outside 170–280s band"
# hesitant-writer trigger contract
hw = OPEN[0]["shot"]["remotion"]["props"]
assert hw["triggerWords"] in hw["text"], "trigger must appear verbatim in text"
assert not hw["triggerWords"].endswith(("?", ".", "!")), "trigger must not end in punctuation"
assert not hw["replacementWords"].endswith(("?", ".", "!")), "replacement must not end in punctuation"
# bookend contract
assert B[0]["beat_id"] == "BIDEA" and B[1]["beat_id"] == "BDEFS"
assert B[-2]["beat_id"] == "BHTF" and B[-1]["beat_id"] == "BOUT"
assert B[-1]["kind"] == "outro_voice" and B[-1]["tail_silence_s"] == 1.0
for b in B:
    assert b.get("voice") == "am_onyx", f"{b['beat_id']}: voice must be am_onyx"

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · VOICE MODE", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Spanish (Hola)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
    "source_doc": "Built from scratch (NEW). Voice-mode availability verified against Anthropic support docs and press, 2026-10-03 (see FACTCHECK.md).",
    "playlist": "how-to-use-ai", "film_number": 18, "series_total": 24,
    "tags": ["voice mode", "show-tell", "how-to-ai", "Claude", "general-audience", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats;", len(body), "manim;", "est", round(total), "s")
