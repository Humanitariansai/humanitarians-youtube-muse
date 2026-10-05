#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for your-song-in-a-minute (How to AI).

SHOW-TELL (Bear, 2026-09-26): one simple isometric drawing per body beat,
minimal labels, Liam's narration carries every idea. No composer cold open,
no verdict card (bookend_exempt); the spoken @NikBearBrown outro stays.

Topic: AI music generation for normal people — birthday songs, jingles,
bedtime stories: describe it and get a finished song back. What to ask for
(occasion, subject, style), how to iterate (describe, listen, fix), where the
results shine (short, personal) and where they don't (long songs wander;
synthetic voices mangle words). Never quotes pricing tiers.
The one number (44% of new Deezer uploads fully AI-generated, ~75,000/day)
is attributed aloud and captioned. General audience; every term explained
on first use.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "your-song-in-a-minute"
TITLE = "Your song in a minute"

YT_PROMPT = ("Make a cheerful birthday song for a seven-year-old named Mia who loves dinosaurs. "
             "Upbeat and easy to sing along to, under two minutes. Sing her name clearly.")


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


B = [
 beat("B00",
      "A birthday song, written for one kid, about dinosaurs — ready in about a minute. "
      "That is the whole trick. You describe the song you want; a minute later you have "
      "something you can actually play at the party. Words, music, singing — all of it made "
      "from your description.",
      "B00_BirthdaySong",
      "The hero object: a vinyl record drops in, music notes pop around it, labeled 'your song', with a terracotta check.",
      [{"at": 0.05, "event": "record drops in"}, {"at": 0.3, "event": "notes pop; 'your song' label lands"},
       {"at": 0.6, "event": "terracotta check"}]),
 beat("B01",
      "Here's how it works. Your description goes in: the occasion, who it's for, what style. "
      "The tool writes the music and the words, and sings them with a synthetic voice — "
      "a singing voice made by software. What comes back is a finished song. "
      "You didn't play an instrument. You didn't sing. You just described it.",
      "B01_HowItWorks",
      "The pipeline: a 'your words' card slides into the music-tool window, a song card (record + note) drops out.",
      [{"at": 0.05, "event": "words card slides into the tool"}, {"at": 0.3, "event": "tool window hums; note pops"},
       {"at": 0.6, "event": "finished song card drops out"}]),
 beat("B02",
      "So what do you actually ask for? Three ingredients. One: the occasion — a birthday. "
      "Two: the subject — dinosaurs, and the birthday kid's name. "
      "Three: the style — cheerful, upbeat, easy to sing along to. "
      "Occasion, subject, style. Give it all three and the tool has something to work with. "
      "Leave one out and you get something generic — a song that could be about anything, for anyone.",
      "B02_ThreeIngredients",
      "Three name-tags — 'a birthday', 'dinosaurs', 'cheerful' — drop into the tool window one by one; a note pops.",
      [{"at": 0.05, "event": "'a birthday' tag drops in"}, {"at": 0.3, "event": "'dinosaurs' tag drops in"},
       {"at": 0.5, "event": "'cheerful' tag drops in"}, {"at": 0.7, "event": "note pops; 'occasion, subject, style' banner"}]),
 beat("B03",
      "The first song is a draft. Always listen to it all the way through before you send it anywhere. "
      "You'll catch things: a name it mangles, a line that doesn't quite fit, a verse that drags. "
      "Nobody hears these problems but you — and you're the only quality check the song gets. "
      "So listen first. That's your job in this.",
      "B03_ListenFirst",
      "A song card with a waveform; a playhead sweeps across it left to right; label 'listen first'.",
      [{"at": 0.05, "event": "song card + waveform"}, {"at": 0.25, "event": "playhead sweeps the waveform"},
       {"at": 0.75, "event": "'listen first' label lands"}]),
 beat("B04",
      "Then ask for a fix. 'Sing her name slower.' 'Make the ending happier.' "
      "It makes another version — same song, better. Describe, listen, fix. "
      "That's the loop, and it usually takes two or three rounds. "
      "The first answer is a draft. The third one is the song you send.",
      "B04_TheLoop",
      "A draft song card; an arrow draws back to the tool; a fixed song card lands with a check ('describe, listen, fix').",
      [{"at": 0.05, "event": "draft song card, 'a draft'"}, {"at": 0.35, "event": "arrow draws back to the tool"},
       {"at": 0.6, "event": "fixed card lands, check, 'describe, listen, fix'"}]),
 beat("B05",
      "Where does this shine? Short, personal things. A birthday song with the kid's name right in the chorus. "
      "A jingle for your club's video — a jingle is just a short, catchy tune. "
      "A lullaby version of your kid's favorite bedtime story. "
      "Short, specific, made for someone you know. That is the sweet spot: one idea, two minutes, for one person.",
      "B05_SweetSpot",
      "Three small song cards spring up — 'birthday', 'a jingle', 'a lullaby' — each with a note.",
      [{"at": 0.1, "event": "'birthday' card"}, {"at": 0.35, "event": "'a jingle' card"},
       {"at": 0.6, "event": "'a lullaby' card"}]),
 beat("B06",
      "And where doesn't it shine? Long songs. Ask for a five-minute epic and it loses the plot halfway through — "
      "the verses wander, the ending fizzles. And the words: that synthetic voice can mangle a name or rhyme pure nonsense. "
      "So keep it short — under three minutes is the safe zone — and never send a song you haven't heard all the way through.",
      "B06_KeepItShort",
      "A long track line wanders and fizzles out under a cross ('too long'); then 'under three minutes' lands.",
      [{"at": 0.05, "event": "long track draws, wanders, fizzles"}, {"at": 0.4, "event": "cross, 'too long'"},
       {"at": 0.65, "event": "'under three minutes' lands"}]),
 beat("B07",
      "Why learn this now? Deezer — one of the big music streaming services — says nearly half of the new music "
      "uploaded to its platform is fully AI-generated. Around seventy-five thousand songs a day that no human "
      "wrote or played. The flood is already here — which is exactly why knowing how to steer it is worth learning.",
      "B07_WhyNow",
      "The number beat: hero '44%' in ink, an ink curve sweeps up with a terracotta end dot, caption 'per Deezer'.",
      [{"at": 0.05, "event": "'44%' lands"}, {"at": 0.15, "event": "ink curve sweeps up, terracotta end dot"},
       {"at": 0.3, "event": "'per Deezer' caption"}]),
]

OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. You want a song — for a birthday, a joke, a bedtime. "
    "The question isn't whether an AI can make one. It's what you should ask for.",
    "BrutalistHesitantWriter",
    {"text": "Make me a song", "triggerWords": "a song",
     "replacementWords": "a happy birthday song about dinosaurs",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Make me a song'"},
     {"at": 0.6, "event": "backspaces 'a song' → 'a happy birthday song about dinosaurs' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive make-me-a-song request and corrects it into a full three-ingredient ask.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. An AI music tool: an AI you describe the music you want to, and it writes the song — "
    "music, words, and singing, all of it. A prompt: your written description. "
    "And a synthetic voice: a singing voice made by software, no singer required.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "AI music tool", "meaning": "an AI you describe the music you want to, and it writes the song"},
               {"term": "prompt", "meaning": "your written description"},
               {"term": "synthetic voice", "meaning": "a singing voice made by software, no singer required"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'AI music tool' lands"}, {"at": 0.5, "event": "'prompt' lands"},
     {"at": 0.78, "event": "'synthetic voice' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into an AI music tool: " + YT_PROMPT + " "
    "Then check two things yourself. Listen to the whole song — does the name come out right? "
    "And does it match your three ingredients: the occasion, the subject, the style? "
    "If not, ask for a fix and try again.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Your Song In A Minute", "command": YT_PROMPT,
     "runningText": "paste this into an AI music tool…",
     "output": ["Check: listen to the whole song — does the name come out right?",
                "Check: occasion, subject, style — does the song match all three?"],
     "folderLabel": "@NikBearBrown", "modelLabel": "Claude", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
                 "minimal labels, with the voice carrying the explanation. The negative space is the style, "
                 "so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.5, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

# ---- assertions: beat count + total duration + structural sanity ----
assert len(B) == 12, f"expected 12 beats, got {len(B)}"
total = sum(b["estimated_duration_s"] for b in B)
assert 180 <= total <= 300, f"total estimated duration {total}s outside 180-300s band"
manim_beats = [b for b in B if b["lane"] == "manim"]
assert len(manim_beats) == 8, f"expected 8 manim body beats, got {len(manim_beats)}"
for b in manim_beats:
    assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), b["beat_id"]
    assert b["shot"]["type"] == "GRAPHIC" and "manim" in b["shot"], b["beat_id"]
    assert b.get("estimated_duration_s") or b.get("actual_duration_s"), b["beat_id"]
    assert b["voice"] == "am_onyx", f"{b['beat_id']}: voice must be a Kokoro voice code, got {b['voice']!r}"
idea = next(b for b in B if b["beat_id"] == "BIDEA")
tw = idea["shot"]["remotion"]["props"]["triggerWords"]
assert tw in idea["shot"]["remotion"]["props"]["text"], "triggerWords must appear verbatim in text"
assert not tw.rstrip().endswith(("?", "!", ".")), "triggerWords must not end in punctuation"
rw = idea["shot"]["remotion"]["props"]["replacementWords"]
assert not rw.rstrip().endswith(("?", "!", ".")), "replacementWords must not end in punctuation"
defs = next(b for b in B if b["beat_id"] == "BDEFS")
assert all(len(t["term"]) <= 17 for t in defs["shot"]["remotion"]["props"]["terms"]), "BDEFS term too long"
for bid in ("BIDEA", "BDEFS", "BHTF", "BOUT"):
    bb = next(b for b in B if b["beat_id"] == bid)
    assert bb["lane"] == "bookend" and "remotion" in bb["shot"], bid
    assert bb["voice"] == "am_onyx", f"{bid}: voice must be a Kokoro voice code, got {bb['voice']!r}"
assert "YOUR TURN" in YOURTURN["shot"]["remotion"]["props"]["topic"], "BHTF topic must contain YOUR TURN"

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · AI MUSIC FOR NORMAL PEOPLE",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hallo (German/Dutch)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + "
                             "terms card, no verdict card; Your Turn is the Claude.ai composer; "
                             "spoken outro stays.",
    "audience": "smart general audience — curious non-experts; every term explained on first use",
    "source_doc": "NEW film (no mirror-repo source). The one number (44% of new Deezer uploads fully "
                  "AI-generated, ~75,000/day, Apr 2026) verified 2026-10-05 via web search: Deezer newsroom "
                  "(Apr 2026: 'more than 44% of the total daily delivery … nearly 75,000 fully AI-generated "
                  "tracks every day'), corroborated by TechCrunch (Jul 2026, >50% on peak days). "
                  "Attribution is spoken aloud ('Deezer … says') and captioned on screen ('per Deezer').",
    "playlist": "How to AI", "chapter_number": 37,
    "tags": ["AI music", "music generation", "birthday song", "AI basics", "how to AI",
             "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(total, 1), "s")
