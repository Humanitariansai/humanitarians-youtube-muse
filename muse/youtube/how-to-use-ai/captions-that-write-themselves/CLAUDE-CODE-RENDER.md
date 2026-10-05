# CLAUDE-CODE-RENDER.md — Captions That Write Themselves

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/how-to-use-ai/captions-that-write-themselves/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (12 files). Persona: "Liam, in for
Bear"; register: Teardown. Greeting note: BIDEA opens "Hallo." (Kokoro
says it cleanly — do not substitute "Hej"). Read the BOUT line exactly:
"Captions That Write Themselves. Liam, in for Bear. At Nik Bear Brown."

Pronunciation notes: numbers are spelled out ("nine in ten", "four
hundred thirty million") — read them as written. The BHTF prompt is read
in full, exactly as written ("find any line where the words do not make
sense in context, and suggest the fix. List the five lines you are least
sure about."), pausing slightly before and after the quoted prompt.

Voice check: every beat in `beat_sheet.json` carries `"voice":
"am_onyx"` (generator-asserted). Never substitute a persona or assistant
name as the voice — the audio stage rejects unknown voice codes.

## 2. Pre-render QC (Mac only — could not run in the build VM)

`manim_layout_audit.py --curve-strict` needs Manim/pangocairo and was
NOT run during the build (the build VM has neither). Before the review
cut, run it per scene class from the reel folder:

```
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B00_PhoneVideo --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B01_WhatCaptions --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B02_ThePass --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B03_OpenIt --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B04_PressButton --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B05_CheckIt --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B06_TwoWays --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B07_WhoWatches --curve-strict
```

Also run `static_scene_check.py` per class from a scratch folder holding
ONLY `scenes.py` (+ `beat_sheet.json` beside it so `until()` pacing
runs) — that is exactly what `art run`'s Gate A sees. Then render each
scene's last frame at low resolution (`manim -ql -s`) and eyeball the
contact sheet, especially: the caption cards inside the phone in B01,
the B05 corrected line ("see you on Main street"), the B06 dot position,
and the B07 attributions ("per Verizon survey, 2019" / "per WHO").

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel captions-that-write-themselves \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the naive job is corrected to the AI ask
in BIDEA; the phone drops in with its "your video" label in B00; the
three caption lines land on the phone in B01 as the voice reads them;
the sound arcs, the streaming lines, and the terracotta timing ticks in
B02 with the "one pass" tag; the phone sliding into the tool and the
button tap in B03; the three generated lines and the stamped check in
B04; the underline, the "Maine street" → "Main street" correction, and
the stamped check in B05; the dot hopping between "burned in" and
"caption file" in B06; the bars, the "9 in 10" hero number, and the two
attributions in B07; the full caption-check prompt fits the composer
card in BHTF.

## 4. Final 4K master

```
./art final --reel captions-that-write-themselves
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 12 beats, ~3m34s. 8 Manim scenes (B00–B07) + 4 Remotion bookends.
  All 8 scenes static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
