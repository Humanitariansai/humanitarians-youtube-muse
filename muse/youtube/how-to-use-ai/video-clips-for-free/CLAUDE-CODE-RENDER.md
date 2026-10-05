# CLAUDE-CODE-RENDER.md — "Video clips for free"

Render instructions for Bear's Mac. This package is pre-render only: no MP3,
no MP4, nothing staged for publication. Publish only on Bear's explicit word.

Film: `video-clips-for-free` · 13 beats · 9 Manim scenes · ~190 s estimated ·
Kokoro voice `am_onyx` · channel `claude-liam` · Teardown register.

## 0. Get the package

Download the folder `muse/youtube/how-to-use-ai/video-clips-for-free/` from
Humanitariansai/humanitarians-youtube-muse into your local reel workspace
(all file activity stays inside
`/Users/bear/Documents/CoWork/bear-textbooks/books/` on your Mac).

Full package (12 files): `make_sheet.py`, `beat_sheet.json`, `scenes.py`,
`ACTS.md`, `SHOTLIST.md`, `FACTCHECK.md`, `SOURCES.md`, `PROMPTS.md`,
`BUILD-LOG.md`, `CHECKS-REPORT.md`, `CLAUDE-CODE-RENDER.md`, `README.md`.

## 1. Narration audio (Kokoro `am_onyx`)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>
```

- This re-voices EVERY beat on each run. For re-voices use
  `--only <BID>` — but note `--only` silently drops BOUT's 1.0 s pad, so
  re-pad and re-measure BOUT after any full run.
- Pad BOUT with a 1.0 s silent tail. BIDEA carries a 0.8 s lead silence
  (already in the sheet; keep it).
- Write the ffprobe durations back into `beat_sheet.json` as
  `actual_duration_s` per beat (the scenes' `until()`/`finish()` pacing reads
  them at render time). Keep `audio_file` on every beat or `art run` refuses.
- Greeting is "Hallo" (Kokoro-clean). Pronunciation checks: "vids.new" must
  read as "vids dot new" (not "vidsnew"); "Veo" as "VAY-oh". Whisper-check
  B00 and BDEFS, which carry both. No pricing or acronyms are spoken
  anywhere, so no other overrides are expected.

## 2. Manim scenes

```bash
# stills first, one scene at a time, low res, into a scratchpad:
manim -ql -s scenes.py B00_VidsWindow   # …repeat for all 9 classes
```

Look at the contact sheet before any 4K render. Then:

```bash
./brutalist.art/art run <reel> --height 2160
```

- Gate A runs from a scratch folder holding ONLY `scenes.py` (plus
  `beat_sheet.json` beside it for `until()` pacing). Scene classes are written
  literally as `class BNN_Name(Scene):` — `run.sh` finds them by that text.
- `manim_layout_audit.py --curve-strict` **cannot run in this VM**
  (no Manim/pangocairo here) — run it on your Mac in the reel folder for every
  class before the 4K pass:

  ```bash
  python3 runtime/qc/manim_layout_audit.py scenes.py --class <ClassName> --curve-strict
  ```

  By construction: all coordinates inside ±6.2 × ±3.3, type ≥ 36 px (labels
  38 px, pill text 32 px), labels beside objects, terracotta only for
  dots/checks/glow/arrows, motion complete in the first ~40% of each beat.
  Watch in particular: B00 (the "vids.new" label sits below the window, clear
  of the clip frame), B06 (the jar at right must not collide with the
  extended frame or the "extend" label), B08 (the gauge needle's two
  positions both stay inside the arc).
- After editing a scene, move its old `manim/<BID>.mp4` to `_superseded/` and
  re-run; also move the stale Manim cache in `<reel>/media/videos` or clips
  can land 1–4 frames past the audio. Leave ~0.05 s of slack for 4K frame
  rounding.
- Parallel manim renders sharing one media dir collide on the Text cache —
  give each scratch render its own `--media_dir`.

## 3. Bookends (Remotion)

BIDEA (`BrutalistHesitantWriter`; lead silence 0.8 s), BDEFS
(`ClaudeDefinitions`), BHTF (`ClaudeComposerAsk`; modelLabel "Opus 5.5",
effortLabel "High"), BOUT (`ClaudeTitleOutro`, `kind: "outro_voice"`) build
from the `remotion` props in `beat_sheet.json` via
`runtime/scripts/remotion_scenes.py`. BDEFS terms are all ≤ 17 characters
(`ClaudeDefinitions` truncates longer terms silently). Remotion does not
render in the build VM — the bookends stay labeled slates until your Mac
render pass.

## 4. Final

```bash
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape
```

Check the master: sha, 3840×2160, 1.0 s silent tail on BOUT. Then STOP —
send the master to review. Do NOT run `make_sheet.py` again after the final
(it wipes the build stamps; recover with `art final`). Stage (`art post`) and
publish only from TOPOST, only on Bear's word.

## 5. Watch the review cut

Check: the clip frame grows out of the window in B00; the play triangle
lands second in B01; three clips drop into the jar in B02; the volcano
check lands in B03; the jar stays full beside the stock box in B04; the
hero clip takes the middle slot in B05; one clip leaves the jar as the
"extend" label lands in B06; the music/avatar cards stay dim in B07; the
gauge needle swings to a new mark in B08.

## Film facts

- 13 beats, ~3m10s estimated (190.0 s; measured audio sets the clock). 9
  Manim scenes, all static-QC clean (0 warn, 0 error). Zero ShowTellCards.
- Deliberately no hard quota numbers in the film (they churn): the
  build-time numbers (10 clips/month, 1080p, ~8 s) live in FACTCHECK.md
  only. If the audio re-measures far off the 190 s estimate, re-check
  FACTCHECK.md against vids.new before final — the B08 beat ("check
  vids.new") stays true regardless.
- No MP3/MP4/WAV or `__pycache__` files are committed to the repo. Narration
  audio and renders live on the Mac only.
