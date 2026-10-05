#!/usr/bin/env python3
"""make_sheet.py — "Give it a voice" (show-tell, general audience).

Source: NEW — built from scratch for the humanitarians AI YouTube
channel "How to AI" series, Wave 6 "Making things", film #36. Skill:
show-tell (assigned, fits: one simple drawing per beat, the voice
explains). cc-explainer excluded per the build brief (no real
`claude` CLI session exists here).

The argument: your slides are silent, and the voiceover used to be
you, a microphone, and twenty takes. Now AI reads your script aloud —
Suno's Speech beta (public beta, launched 2026-10-01) reads the script
and mixes original background music under it in one track; Google
Vids already has AI voiceovers built into the editor. The voice
reads exactly what you wrote, so the one real skill is writing a
script worth reading aloud.

Run: python3 make_sheet.py   -> writes beat_sheet.json (11 beats).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "give-it-a-voice"
TITLE = "Give it a voice"

WPS = 2.5  # words per second (~150 wpm)


def est(narration):
    return round(len(narration.split()) / WPS, 1)


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim",
            "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": est(narration),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image,
                     "show": show, "manim": {"class": cls},
                     "motion_claim": image},
            "qc": {"sparse_by_design": True,
                   "sparse_reason": "show-tell body: one hero object per beat "
                                    "on the cream stage, by design"}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


EM = "\u2014"  # em dash


B = [
 remotion("BIDEA", "the question",
  "Hallo. This is Liam, in for Bear. I need to record a voiceover for my "
  "slides. Well, actually, I need the AI to do it. Because now, your slides "
  "can talk for themselves.",
  "BrutalistHesitantWriter",
  {"text": "I need to\nrecord a voiceover for my slides.",
   "triggerWords": "record a voiceover for my slides",
   "replacementWords": "need AI to voice my slides",
   "fontSize": 70, "charSize": 22, "charMs": 22,
   "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2,
   "jitter": 20, "seed": "give-it-a-voice", "banner": ""},
  [{"at": 0.0, "event": "types 'I need to record a voiceover for my slides.'"},
   {"at": 0.55, "event": "backspaces 'record a voiceover for my slides' -> 'need AI to voice my slides'"}],
  lead_silence_s=0.8,
  motion_claim="The writer types the naive plan and corrects it to the film's claim: the AI voices the slides.",
  qc={"sparse_by_design": True,
      "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),

 remotion("BDEFS", "terms",
  "Three terms for this film. A voiceover: spoken narration that runs over "
  "slides or video. Text-to-speech: software that reads written words aloud. "
  "And beta: an early test version, still a little rough around the edges.",
  "ClaudeDefinitions",
  {"title": "Terms In This Film",
   "terms": [
    {"term": "Voiceover",
     "def": "spoken narration that runs over slides or video"},
    {"term": "Text-to-speech",
     "def": "software that reads written words aloud"},
    {"term": "Beta",
     "def": "an early test version, still a little rough"}],
   "durationSeconds": 14.0},
  [{"at": 0.0, "event": "title lands"},
   {"at": 0.2, "event": "term 1 lands"},
   {"at": 0.5, "event": "term 2 lands"},
   {"at": 0.75, "event": "term 3 lands"}]),

 beat("B00",
  "The starting point is simple. Your slides are finished, and they are "
  "silent. Someone has to read them out loud, and that someone used to be "
  "you, a microphone, and twenty takes.",
  "B00_SilentSlides",
  "Three slide pages land in a stack; a muted speaker lands beside them; the deck is tagged 'needs a voice'.",
  [{"at": 0.05, "event": "three slide pages land in a stack"},
   {"at": 0.35, "event": "muted speaker lands beside the stack"},
   {"at": 0.7, "event": "'needs a voice' pill lands on 'silent'"}]),

 beat("B01",
  "Meet Suno Speech. Suno is the company known for making songs from text. "
  "This October they opened a public beta that speaks instead of sings. You "
  "give it your script. It gives you back a voice reading it, with background "
  "music mixed underneath, in one track.",
  "B01_SunoSpeech",
  "The top page slides into the Suno Speech box; a voice wave and a music trail stream out and merge into one track bar.",
  [{"at": 0.05, "event": "Suno Speech box lands"},
   {"at": 0.3, "event": "the deck page slides into the box"},
   {"at": 0.6, "event": "voice wave and music trail stream out"},
   {"at": 0.85, "event": "the two streams merge into one track bar"}]),

 beat("B02",
  "There are two ways to use it. Simple mode: you describe what you want, "
  "like a pirate captain rallying his crew. Advanced mode: you paste in your "
  "exact script, and fine-tune the voice, its gender, its style, how much "
  "variety it uses.",
  "B02_TwoWays",
  "Two cards land side by side: 'Simple — describe it' and 'Advanced — your script'; voice sliders rise on the Advanced card.",
  [{"at": 0.08, "event": "the 'Simple — describe it' card lands"},
   {"at": 0.45, "event": "the 'Advanced — your script' card lands"},
   {"at": 0.7, "event": "voice sliders rise on the Advanced card"}]),

 beat("B03",
  "The workflow is three steps. One: write the script, or just describe the "
  "vibe. Two: pick the voice and the music style, soft piano under a bedtime "
  "story, stadium drums under a pep talk. Three: generate. Voice and music "
  "land in one track, mixed and ready.",
  "B03_Workflow",
  "Three step pills chain across; the merged track bar lands at the end of the chain.",
  [{"at": 0.05, "event": "step pill 'script or vibe' lands"},
   {"at": 0.35, "event": "step pill 'voice + music style' lands"},
   {"at": 0.6, "event": "step pill 'generate' lands"},
   {"at": 0.85, "event": "the merged track bar lands at the end"}]),

 beat("B04",
  "The honest part. Beta means rough, and Suno's own team says so. Accents "
  "can wander: a British voice may come back Australian. And dramatic pauses "
  "can get very dramatic. So listen to the whole take before it goes anywhere "
  "public.",
  "B04_BetaRough",
  "The track bar returns; a 'wandering accent' tag arcs away and back; one pause gap stretches wide.",
  [{"at": 0.05, "event": "the track bar returns"},
   {"at": 0.35, "event": "'wandering accent' tag arcs away and back"},
   {"at": 0.6, "event": "one pause gap stretches wide"},
   {"at": 0.85, "event": "the tag settles on 'beta means rough'"}]),

 beat("B05",
  "And if you edit in Google Vids, you don't need a second app. Vids already "
  "has AI voiceovers built in. You type the script per scene, pick one of "
  "thirty voices, and steer the delivery with bracket tags, like open bracket, "
  "excitedly, close bracket. The voiceover lives inside the video: no separate "
  "audio file to line up.",
  "B05_VidsBuiltIn",
  "The Vids browser window lands; the deck page and a script pill enter; the '[excitedly]' tag pill lands; a check stamps 'no separate audio file'.",
  [{"at": 0.05, "event": "Vids browser window lands"},
   {"at": 0.3, "event": "deck page and script pill enter"},
   {"at": 0.55, "event": "'[excitedly]' tag pill lands"},
   {"at": 0.85, "event": "check stamps 'no separate audio file'"}]),

 beat("B06",
  "One rule before you generate. The voice reads exactly what you wrote: "
  "typos, weird punctuation, all of it. So proofread like the voice is "
  "watching. Short sentences. Numbers written the way they sound. And read "
  "it aloud yourself first: if you stumble, the AI will too.",
  "B06_TheRule",
  "A page lands with one typo word on its lines; sound-wave arcs read it aloud; the typo takes a terracotta X; the clean page earns the check.",
  [{"at": 0.05, "event": "the page with the typo lands"},
   {"at": 0.4, "event": "sound-wave arcs read the page aloud"},
   {"at": 0.65, "event": "the typo takes the terracotta X"},
   {"at": 0.88, "event": "the clean page earns the check"}]),

 remotion("BHTF", "your turn",
  "Your turn. Paste this into Claude: Turn my script into a voiceover-ready "
  "script. Use short sentences. Write numbers and acronyms the way they "
  "sound. Then read it back to me, exactly as it will be spoken. Now check "
  "it yourself. Read the script out loud: if you stumble on a line, the AI "
  "will too. And always listen to the first ten seconds before you generate "
  "the whole thing.",
  "ClaudeComposerAsk",
  {"greeting": "Your turn.",
   "topic": "HOW TO AI " + EM + " YOUR TURN",
   "segment": "Give it a voice",
   "command": "Turn my script into a voiceover-ready script. Use short "
              "sentences. Write numbers and acronyms the way they sound. "
              "Then read it back to me, exactly as it will be spoken.",
   "runningText": "paste this into Claude" + EM,
   "output": ["you can read your own script aloud without stumbling",
              "the first ten seconds sound right before the full take"]},
  [{"at": 0.0, "event": "Composer opens " + EM + " 'Your turn.'"},
   {"at": 0.1, "event": "the prompt types in full"},
   {"at": 0.8, "event": "two check lines land"}]),

 remotion("BOUT", "outro",
  "Give it a voice. At Nik Bear Brown.",
  "ClaudeTitleOutro",
  {"title": "Give it a voice", "slug": "give-it-a-voice",
   "handle": "@NikBearBrown", "subline": ""},
  [{"at": 0.0, "event": "title restates; handle; mascot"}],
  kind="outro_voice", tail_silence_s=1.0),
]

SHEET = {
 "metadata": {
  "slug": SLUG, "title": TITLE, "topic": "HOW TO AI \u00b7 WAVE 6 MAKING THINGS",
  "skill": "show-tell", "style_preset": "show-tell",
  "channel": "claude-liam", "persona": "Liam (in for Bear)",
  "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
  "clock": "narration", "palette": "claude", "register": "Teardown",
  "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
  "caption_policy": "none", "greeting_language": "Hallo (German)",
  "playlist": "How to AI", "wave": "Wave 6: Making things", "film_no": 36,
  "tags": ["voiceover", "text-to-speech", "suno", "google vids"],
  "bookend_exempt": ["cold-open", "bvdt"],
  "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the "
   "hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai "
   "composer; spoken outro stays.",
 },
 "beats": B,
}

# ═══════════════════════ self-assertions (the gate) ═══════════════════════
_body_ids = [f"B{i:02d}" for i in range(7)]
_scene_classes = ["B00_SilentSlides", "B01_SunoSpeech", "B02_TwoWays",
                  "B03_Workflow", "B04_BetaRough", "B05_VidsBuiltIn",
                  "B06_TheRule"]

assert len(B) == 11, f"expected 11 beats, got {len(B)}"
assert [b["beat_id"] for b in B] == ["BIDEA", "BDEFS"] + _body_ids + ["BHTF", "BOUT"]
assert len({b["beat_id"] for b in B}) == 11, "beat ids must be unique"

for b in B:
    assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    assert b["estimated_duration_s"] > 0, f"{b['beat_id']}: non-positive duration"
    assert b["voice"] == "am_onyx", f"{b['beat_id']}: voice must be am_onyx"
    assert b["engine"] == "kokoro", f"{b['beat_id']}: engine must be kokoro"
    assert b["shot"]["show"], f"{b['beat_id']}: missing show block"
    assert b.get("actual_duration_s") or b.get("estimated_duration_s"), \
        f"{b['beat_id']}: needs a duration field"

for bid, cls in zip(_body_ids, _scene_classes):
    b = next(x for x in B if x["beat_id"] == bid)
    assert b["shot"]["type"] == "GRAPHIC", f"{bid}: body shot type must be GRAPHIC"
    assert b["shot"]["manim"]["class"] == cls, f"{bid}: class mismatch"
    assert b["lane"] == "manim", f"{bid}: lane must be manim"

for bid in ("BIDEA", "BDEFS", "BHTF", "BOUT"):
    b = next(x for x in B if x["beat_id"] == bid)
    assert b["shot"]["type"] == "REMOTION", f"{bid}: bookend shot type must be REMOTION"
    assert b["shot"]["remotion"]["pattern"], f"{bid}: missing remotion pattern"

bidea = B[0]
assert bidea["lead_silence_s"] == 0.8, "BIDEA needs lead_silence_s 0.8"
assert bidea["shot"]["remotion"]["props"]["triggerWords"] in \
    bidea["shot"]["remotion"]["props"]["text"], "triggerWords must appear in text"
for k in ("triggerWords", "replacementWords"):
    w = bidea["shot"]["remotion"]["props"][k]
    assert w[-1] not in ".?!", f"BIDEA {k} must not end in punctuation"

bdefs = next(x for x in B if x["beat_id"] == "BDEFS")
assert bdefs["shot"]["remotion"]["props"]["durationSeconds"] == \
    bdefs["estimated_duration_s"], "BDEFS durationSeconds must match narration"
for t in bdefs["shot"]["remotion"]["props"]["terms"]:
    assert len(t["term"]) <= 17, f"BDEFS term too long: {t['term']}"

bhtf = next(x for x in B if x["beat_id"] == "BHTF")
assert "YOUR TURN" in bhtf["shot"]["remotion"]["props"]["topic"], "BHTF topic needs YOUR TURN"
cmd = bhtf["shot"]["remotion"]["props"]["command"]
assert cmd in bhtf["narration_text"], "BHTF prompt must be read verbatim in narration"

bout = B[-1]
assert bout["kind"] == "outro_voice" and bout["tail_silence_s"] == 1.0

total = round(sum(b["estimated_duration_s"] for b in B), 1)
assert 150 <= total <= 240, f"total {total}s outside the 150-240 s band"

(HERE / "beat_sheet.json").write_text(json.dumps(SHEET, indent=1, ensure_ascii=False) + "\n")
print(f"wrote beat_sheet.json: 11 beats, {total} s")
