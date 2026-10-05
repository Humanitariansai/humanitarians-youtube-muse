# CLAUDE-CODE-RENDER.md — "Teach it your world"

Render instructions for Bear's Mac. This package is pre-render only: no MP3,
no MP4, nothing staged for publication. Publish only on Bear's explicit word.

Film: `teach-it-your-world` · 13 beats · 7 Manim scenes · ~341 s estimated ·
Kokoro voice `am_onyx` · channel `claude-liam` · Teardown register · skill
ai-explainer.

## 0. Get the package

Download the folder `muse/youtube/how-to-use-ai/teach-it-your-world/` from
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
- Greeting is "Konnichiwa" (Kokoro-clean). No version numbers or acronyms are
  spoken anywhere, so no pronunciation overrides are expected — whisper-check
  B00 and B01 anyway.
- B01 has `lead_silence_s: 0.8` on the beat — keep it; the hesitant writer
  needs the head start for the typing + correction.

## 2. Manim scenes

```bash
# stills first, one scene at a time, low res, into a scratchpad:
manim -ql -s scenes.py B02_TheGap   # …repeat for all 7 classes
```

Look at the contact sheet before any 4K render. Then:

```bash
./brutalist.art/art run <reel> --height 2160
```

- Gate A runs from a scratch folder holding ONLY `scenes.py` (+
  `beat_sheet.json` beside it for `until()` pacing). Scene classes are written
  literally as `class BNN_Name(Scene):` — `run.sh` finds them by that text.
  The iso kit block is pasted at the top of `scenes.py` (do not import it).
- `manim_layout_audit.py --curve-strict` **cannot run in this VM**
  (no Manim/pangocairo here) — run it on your Mac in the reel folder for every
  class before the 4K pass. By construction: all coordinates inside
  ±6.2 × ±3.3, type ≥ 30 px (labels ≥ 32, body ≥ 36), labels beside objects,
  terracotta only for tape/checks/rings/glow, motion complete in the first
  ~40% of each beat.
- After editing a scene, move its old `manim/<BID>.mp4` to `_superseded/` and
  re-run; also move the stale Manim cache in `<reel>/media/videos` or clips
  can land 1–4 frames past the audio. Leave ~0.05 s of slack for 4K frame
  rounding.
- Parallel manim renders sharing one media dir collide on the Text cache —
  give each scratch render its own `--media_dir`.

## 3. Bookends (Remotion)

B00 + BHTF (`ClaudeComposerAsk`), B01 (`BrutalistHesitantWriter`),
BDEFS (`ClaudeDefinitions`), BVDT (`ClaudeVerdictArtifact`),
BOUT (`ClaudeTitleOutro`, `kind: "outro_voice"`) build from the `remotion`
props in `beat_sheet.json` via `runtime/scripts/remotion_scenes.py`.
- `ClaudeVerdictArtifact` paginates two lines per page: the sheet gives it
  exactly 4 lines (2 pages) — do not add a fifth.
- BDEFS terms are all ≤ 17 characters (`ClaudeDefinitions` truncates longer
  terms silently).
- B00's composer output is an illustrative drawn list, not a recorded
  session — see CHECKS-REPORT.md §5.

## 4. Final

```bash
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape
```

Check the master: sha, 3840×2160, 1.0 s silent tail on BOUT. Then STOP — send
the master to review. Do NOT run `make_sheet.py` again after the final (it
wipes the build stamps; recover with `art final`). Stage (`art post`) and
publish only from TOPOST, only on Bear's word.
