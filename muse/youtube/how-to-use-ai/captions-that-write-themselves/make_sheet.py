#!/usr/bin/env python3
"""make_sheet.py — Captions That Write Themselves (Film 40, how-to-ai lane, Wave 6).

SHOW-TELL (Bear, 2026-09-26): one drawn isometric illustration per body
beat, minimal labels, Liam's narration (Kokoro am_onyx) explaining the
action. Claude palette. Bookends: hesitant writer, key terms, Your Turn
composer, spoken @NikBearBrown outro; no verdict card, no cold open
(bookend_exempt).

Source: NEW — built from scratch, no mirror source. The four-step
walkthrough (open a captioning tool / press the button / check names and
odd words / burned-in or caption file) is the film's own. The two
numbers quoted are attributed aloud and on screen (thin-numbers law);
no pricing tiers anywhere.

Run: python3 make_sheet.py
Durations: narration at ~150 wpm (words / 2.5), matching the reel clock.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "captions-that-write-themselves"
TITLE = "Captions That Write Themselves"

YT_PROMPT = ("Find any line where the words do not make sense in context, and "
             "suggest the fix. List the five lines you are least sure about.")


def beat(bid, act, narration, cls, image, show):
    return {"beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}


B = [
    beat("B00", "show-tell",
         "This is your video. You shot it on your phone: the birthday toast, the school play, the "
         "thing you filmed for your channel. The words are already in it, in the sound. Now they need "
         "to be on the screen.",
         "B00_PhoneVideo",
         "A phone with a play triangle drops onto the stage with a landing shadow; the label 'your "
         "video' lands beside it.",
         [{"at": 0.1, "event": "landing shadow grows, phone drops in"}, {"at": 0.35, "event": "label 'your video' lands"}]),
    beat("B01", "show-tell",
         "Captions are the words being spoken, written at the bottom of the frame, each line appearing "
         "as it is said. Read them, and the video makes sense with the sound off. That is the whole "
         "idea: every spoken word, on the screen, on time.",
         "B01_WhatCaptions",
         "The phone stays; three white caption lines land at the bottom of its screen one by one, each "
         "as the voice reads it; the label 'captions' sits beside.",
         [{"at": 0.25, "event": "first caption line lands"}, {"at": 0.4, "event": "second caption line lands"},
          {"at": 0.62, "event": "third caption line lands"}, {"at": 0.8, "event": "label 'captions' lands"}]),
    beat("B02", "show-tell",
         "The AI does the boring part in one pass. It listens to the speech in your video and writes "
         "down what it hears, line by line, with each line timed to the moment it is said. The draft "
         "is ready in about the time it takes to watch the video once. By hand, pausing, typing, "
         "rewinding, would take you far longer.",
         "B02_ThePass",
         "Sound arcs travel from the phone into a dark AI block; three timed caption lines stream out "
         "the other side with terracotta timing ticks; the label 'one pass' sits beside.",
         [{"at": 0.16, "event": "sound arcs travel phone -> AI block"}, {"at": 0.32, "event": "timed caption lines stream out"},
          {"at": 0.6, "event": "timing ticks pop onto each line"}]),
    beat("B03", "show-tell",
         "Step one: open your video in a captioning tool. Almost everything that edits video on your "
         "phone has a captions button built in now. Look for it where the text tools live. Your video "
         "goes in. The captions come out.",
         "B03_OpenIt",
         "A kraft captioning-tool card with a 'captions' button fades in; the phone video slides into "
         "it; a cursor taps the button; three caption lines stream out below.",
         [{"at": 0.1, "event": "tool card and 'captions' button fade in"}, {"at": 0.35, "event": "phone slides into the tool"},
          {"at": 0.72, "event": "cursor taps the button"}, {"at": 0.85, "event": "caption lines stream out"}]),
    beat("B04", "show-tell",
         "Step two: press the captions button and let it run. The AI writes the whole draft itself, "
         "every line, timed. Then play it back and read along. The timing will be close. The words will "
         "be nearly right.",
         "B04_PressButton",
         "The cursor taps the 'captions' button; three caption lines generate one by one below it; a "
         "terracotta check stamps the draft; the label 'the draft' sits beside.",
         [{"at": 0.2, "event": "cursor taps the captions button"}, {"at": 0.35, "event": "first caption line generates"},
          {"at": 0.6, "event": "second and third lines generate"}, {"at": 0.82, "event": "terracotta check stamps the draft"}]),
    beat("B05", "show-tell",
         "Step three: the one job left for you. The AI guesses from sound alone, so it fumbles names, "
         "places, and unusual words, anything it has never heard. Scan the draft for those. Fix your "
         "sister's name, fix the street, fix the jargon. Everything else is usually right.",
         "B05_CheckIt",
         "Three draft lines sit on stage; a terracotta underline grows under the misheard word in line "
         "two; the line fades and returns corrected, 'Maine street' becomes 'Main street'; a terracotta "
         "check stamps it; the labels 'names' and 'odd words' sit beside.",
         [{"at": 0.08, "event": "three draft lines land"}, {"at": 0.38, "event": "underline grows under the wrong word"},
          {"at": 0.66, "event": "line fades out, corrected line lands"}, {"at": 0.85, "event": "terracotta check stamps it"}]),
    beat("B06", "show-tell",
         "Step four: choose how the captions live. Burned in means they are part of the video itself, "
         "everyone sees them, always. A caption file means they sit beside the video, and the viewer "
         "can turn them on or off. For short feeds, burn them in. For YouTube, keep the file.",
         "B06_TwoWays",
         "Two boxes side by side: a video with its captions locked on ('burned in') vs a video with a "
         "separate caption page beside it ('caption file'); a terracotta dot hops between the two as "
         "the voice chooses.",
         [{"at": 0.08, "event": "both boxes land"}, {"at": 0.15, "event": "dot lands on 'burned in'"},
          {"at": 0.4, "event": "dot hops to 'caption file'"}, {"at": 0.78, "event": "dot back to 'burned in'"},
          {"at": 0.88, "event": "dot to 'caption file'"}]),
    beat("B07", "show-tell",
         "Why bother? Two reasons. Nine in ten viewers watch phone video with the sound off. That is a "
         "Verizon survey of mobile viewers talking. And for the four hundred thirty million people "
         "worldwide with disabling hearing loss, says the World Health Organization, captions are not "
         "a convenience. They are the video.",
         "B07_WhoWatches",
         "A short 'sound on' bar and a tall 'sound off' bar with the ink hero number '9 in 10'; "
         "on-screen attributions: 'per Verizon survey, 2019' and 'per WHO'.",
         [{"at": 0.06, "event": "short 'sound on' bar lands"}, {"at": 0.2, "event": "'sound off' bar grows, '9 in 10' lands"},
          {"at": 0.68, "event": "attribution lines land"}]),
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
             "Hallo. This is Liam, in for Bear. You shot the video on your phone, and now it needs words "
             "on screen. The instinct is to type out every word yourself. So the question is not type out "
             "the captions. It is let the AI write the captions.",
             "BrutalistHesitantWriter",
             {"text": "type out\nthe captions",
              "triggerWords": "type out", "replacementWords": "let the AI write",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
              "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'type out the captions'"},
              {"at": 0.6, "event": "backspaces 'type out' -> 'let the AI write' on the spoken correction"}],
             lead_silence_s=0.8, motion_claim="The writer types the naive do-it-yourself ask and corrects it to the AI ask.",
             qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms, plainly. Captions: the words being said, written on screen, timed to the "
             "sound. Subtitles: the same idea, but translated into another language. Auto-captioning: an "
             "AI listens to your video and writes the captions for you, line by line.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "captions", "meaning": "the words being said, written on screen, timed to the sound"},
                        {"term": "subtitles", "meaning": "the same idea, but translated into another language"},
                        {"term": "auto-captioning", "meaning": "the AI writes the captions for you, line by line"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'captions' lands"}, {"at": 0.5, "event": "'subtitles' lands"},
              {"at": 0.78, "event": "'auto-captioning' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. This week, caption one video. Generate the draft, then paste it into the AI and ask: "
    "find any line where the words do not make sense in context, and suggest the fix. List the five "
    "lines you are least sure about. Then check two things yourself. Are the names and unusual words "
    "spelled right? And does it read cleanly when you watch with the sound off?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "AI \u00b7 YOUR TURN", "segment": "Captions That Write Themselves",
     "command": YT_PROMPT,
     "runningText": "paste this into the AI\u2026",
     "output": ["Check: the names and unusual words are spelled right.",
                "Check: it reads cleanly when you watch with the sound off."],
     "folderLabel": "@NikBearBrown", "modelLabel": "any AI", "effortLabel": "Low"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
     {"at": 0.1, "event": "the caption-check prompt types in full"},
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
    "slug": SLUG, "title": TITLE, "topic": "AI \u00b7 VIDEO", "skill": "show-tell",
    "style_preset": "show-tell", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24,
    "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience — not AI experts; every term explained plainly",
    "source_doc": "NEW — built from scratch, no mirror source. The four-step walkthrough is the film's own; the two quoted numbers (92% sound-off viewing, 430 million with disabling hearing loss) are attributed aloud and on screen (see SOURCES.md). No pricing tiers quoted.",
    "playlist": "How to AI", "chapter_number": 40,
    "tags": ["captions", "subtitles", "auto-captioning", "accessibility", "phone video", "speech to text", "Nik Bear Brown"]},
    "beats": B}

if __name__ == "__main__":
    beats = sheet["beats"]
    assert len(beats) == 12, len(beats)
    assert [b["beat_id"] for b in beats] == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05",
                                            "B06", "B07", "BHTF", "BOUT"]
    body = [b for b in beats if b["lane"] == "manim"]
    assert len(body) == 8, len(body)
    for b in body:
        assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), b["beat_id"]
        assert b["shot"]["type"] == "GRAPHIC", b["beat_id"]
    for b in beats:  # the Wave 5 lesson: every per-beat voice must be a Kokoro code
        assert b.get("voice") == "am_onyx", (b["beat_id"], b.get("voice"))
    htf = next(b for b in beats if b["beat_id"] == "BHTF")
    assert "find any line where the words do not make sense in context" in htf["narration_text"].lower(), "prompt read in full"
    assert "list the five lines you are least sure about" in htf["narration_text"].lower(), "second prompt line read in full"
    assert YT_PROMPT.split(".")[0] in htf["shot"]["remotion"]["props"]["command"], "composer carries the prompt"
    total = sum(b["estimated_duration_s"] for b in beats)
    assert 190 <= total <= 250, f"total {total}s outside 190-250s band"
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
    print(f"beats={len(beats)} body={len(body)} total={total}s (~{int(total//60)}m{int(total%60):02d}s)")
    print("beat_sheet.json written")
