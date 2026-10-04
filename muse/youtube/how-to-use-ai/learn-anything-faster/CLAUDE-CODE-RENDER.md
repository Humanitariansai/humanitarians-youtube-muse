# CLAUDE-CODE-RENDER.md — Learn Anything Faster

Render this film on the Mac with Claude Code + the brutalist.art toolkit.

## 0. Get the files

Clone or pull `https://github.com/Humanitariansai/humanitarians-youtube-muse`, then:

```
cd muse/youtube/how-to-use-ai/learn-anything-faster/
```

Files: `beat_sheet.json`, `scenes.py`, `ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`.

## 1. Narration (Kokoro, am_onyx)

For each beat in `beat_sheet.json`, synthesize the `narration_text` field
with Kokoro voice `am_onyx`. Save as `audio/BIDEA.mp3`, `audio/BDEFS.mp3`,
`audio/B00.mp3` … `audio/BOUT.mp3` (9 files). Persona: "Liam, in for
Bear"; register: Teardown. Greeting note: BIDEA opens "Hallo." (Kokoro
says it cleanly — do not substitute "Hej"). Read the BOUT line exactly:
"Learn Anything Faster. Liam, in for Bear. At Nik Bear Brown."

Read the BHTF prompt in full, exactly as written in the beat sheet
("Be my tutor on your topic…"), pausing slightly before and after the
quoted prompt. The bracketed "[your topic]" is voiced as "your topic".

## 2. Pre-render QC (Mac only — could not run in the build VM)

`manim_layout_audit.py --curve-strict` needs Manim/pangocairo and was
NOT run during the build (the build VM has neither). Before the review
cut, run it per scene class from the reel folder:

```
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B00_House --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B01_ExplainSimple --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B02_QuizMode --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B03_Socratic --curve-strict
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class B04_YourTopic --curve-strict
```

Also run `static_scene_check.py` per class from a scratch folder holding
ONLY `scenes.py` (+ `beat_sheet.json` beside it so `until()` pacing
runs) — that is exactly what `art run`'s Gate A sees. Then render each
scene's last frame at low resolution (`manim -ql -s`) and eyeball the
contact sheet, especially label spacing beside the blocks and pills.

## 3. Review cut

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art
./art run --reel learn-anything-faster \
  --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py \
  --audio <film-dir>/audio/
```

Watch the review slate. Check: the naive ask is corrected to the tutor
ask in BIDEA; the house drops in with its "a mortgage" label in B00;
the three blocks land labelled "borrow" / "interest" / "pay back" in
B01 with the terracotta dot hopping block to block; the "?" pill, answer
line, terracotta check, and second "?" pill sequence in B02 with the
"one at a time" tag; the "the loan" / "the interest" option pills, the
answer dot tapping "the interest", and the "aha" landing in B03; the
house sliding aside for the "?" card labelled "your topic" in B04; the
full tutor prompt fits the composer card in BHTF.

## 4. Final 4K master

```
./art final --reel learn-anything-faster
```

## 5. Publish

Only on Bear's explicit instruction. The film is not published by default.

## Film facts

- 9 beats, ~3m20s. 5 Manim scenes (B00–B04) + 4 Remotion bookends.
  All 5 scenes static-QC clean (0 warn, 0 error).
- No MP3/MP4/WAV files are committed to the repo. Narration audio and
  renders live on the Mac only.
