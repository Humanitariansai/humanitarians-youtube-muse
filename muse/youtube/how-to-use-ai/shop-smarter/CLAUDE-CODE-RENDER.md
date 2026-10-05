# CLAUDE-CODE-RENDER.md — "Shop smarter"

Render instructions for Bear's Mac. This package is pre-render only: no MP3,
no MP4, nothing staged for publication. Publish only on Bear's explicit word.

Film: `shop-smarter` · 13 beats · 9 Manim scenes · ~205 s estimated ·
Kokoro voice `am_onyx` · channel `claude-liam` · Teardown register.

## 0. Get the package

Download the folder `muse/youtube/how-to-use-ai/shop-smarter/` from
Humanitariansai/humanitarians-youtube-muse into your local reel workspace
(all file activity stays inside
`/Users/bear/Documents/CoWork/bear-textbooks/books/` on your Mac).

## 1. Narration audio (Kokoro `am_onyx`)

```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>
```

- This re-voices EVERY beat on each run. For re-voices use
  `--only <BID>` — but note `--only` silently drops BOUT's 1.0 s pad, so
  re-pad and re-measure BOUT after any full run.
- Pad BOUT with a 1.0 s silent tail.
- Write the ffprobe durations back into `beat_sheet.json` as
  `actual_duration_s` per beat (the scenes' `until()`/`finish()` pacing reads
  them at render time). Keep `audio_file` on every beat or `art run` refuses.
- Greeting is "Hallo" (Kokoro-clean). No version numbers or acronyms are
  spoken anywhere, so no pronunciation overrides are expected — whisper-check
  BIDEA anyway. Watch B04's "four thousand" — Kokoro is fine with plain
  numbers here, but whisper-check it lands cleanly.

## 2. Manim scenes

```bash
# stills first, one scene at a time, low res, into a scratchpad:
manim -ql -s scenes.py B00_ThreeOptions   # …repeat for all 9 classes
```

Look at the contact sheet before any 4K render. Then:

```bash
./brutalist.art/art run <reel> --height 2160
```

- Gate A runs from a scratch folder holding ONLY `scenes.py` (+
  `beat_sheet.json` beside it for `until()` pacing). Scene classes are written
  literally as `class BNN_Name(Scene):` — `run.sh` finds them by that text.
  (`table_grid_v`/`table_grid_h` are plain helpers, not scenes.)
- `manim_layout_audit.py --curve-strict` **cannot run in this VM**
  (no Manim/pangocairo here) — run it on your Mac in the reel folder for every
  class before the 4K pass. By construction: all coordinates inside
  ±6.2 × ±3.3, type ≥ 40 px, labels beside objects, terracotta only for
  dots/checks/rings/X-marks, ink numerals, midpoint settled in every scene.
- After editing a scene, move its old `manim/<BID>.mp4` to `_superseded/` and
  re-run; also move the stale Manim cache in `<reel>/media/videos` or clips
  can land 1–4 frames past the audio. Leave ~0.05 s of slack for 4K frame
  rounding.
- Parallel manim renders sharing one media dir collide on the Text cache —
  give each scratch render its own `--media_dir`.

## 3. Bookends (Remotion)

BIDEA (`BrutalistHesitantWriter`), BDEFS (`ClaudeDefinitions`), BHTF
(`ClaudeComposerAsk`), BOUT (`ClaudeTitleOutro`, `kind: "outro_voice"`) build
from the `remotion` props in `beat_sheet.json` via
`runtime/scripts/remotion_scenes.py`. BDEFS terms are all ≤ 17 characters
(`ClaudeDefinitions` truncates longer terms silently).

## 4. Final

```bash
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape
```

Check the master: sha, 3840×2160, 1.0 s silent tail on BOUT. Then STOP — send
the master to review. Do NOT run `make_sheet.py` again after the final (it
wipes the build stamps; recover with `art final`). Stage (`art post`) and
publish only from TOPOST, only on Bear's word.
