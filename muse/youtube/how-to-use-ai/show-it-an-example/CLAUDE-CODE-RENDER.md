# CLAUDE-CODE-RENDER.md — "Show It an Example"

Render instructions for Bear's Mac (Manim + Kokoro). This package is
pre-render: everything except the final MP3/MP4.

## 0. Fetch the package
Download `muse/youtube/how-to-use-ai/show-it-an-example/` from
`Humanitariansai/humanitarians-youtube-muse` into a reel folder, e.g.
`books/show-it-an-example/`, next to your `brutalist.art` checkout.

## 1. Narration audio (Kokoro `am_onyx`)
```bash
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel> --voice am_onyx
```
- Pad BOUT with a 1.0 s silent tail (the sheet already declares
  `tail_silence_s: 1.0`; re-pad after any full re-voice).
- Write the ffprobe-measured durations back into `beat_sheet.json` as
  `actual_duration_s` (keep `audio_file` on every beat — `art run` needs it).
- Whisper-check BIDEA ("Hallo" — known-clean) and skim the rest; the script
  avoids version numbers and spelled-out acronyms.

## 2. Layout audit (deferred — could not run in the build VM)
```bash
python3 brutalist.art/runtime/qc/manim_layout_audit.py scenes.py --class <ClassName> --curve-strict
```
Run for all 7 classes (`B00_TheBox` … `B06_ShortVsTall`) **before** the review
cut. The static checker passed clean (see CHECKS-REPORT.md), but real Manim
text metrics, Gate T midpoint sampling, and Gate V contrast are render-time
gates. Design notes: all motion finishes in the first ~40% of each clip; every
label is up and settled by the midpoint; leader gaps ≥0.3; text ≥32.

## 3. Stills first, then the review cut
```bash
# low-res last-frame stills into a scratchpad; eyeball the contact sheet
./brutalist.art/art run <reel> --height 2160   # Gates A, B, V + review cut
```
`scenes.py` is assembled as `templates/iso_kit.py` (pasted at top, Gate A
copies only this file) + the film body. The film body is also kept locally as
`_scenes_body_mine.py` (not pushed); if you edit scenes, re-audit the class.

## 4. Final
```bash
./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape
```
Check the master: sha, 3840×2160, silent tail on BOUT. **Do not** re-run
`make_sheet.py` after the final (it wipes build stamps). **Do not** stage
(`art post`) or publish — only on Bear's explicit word, and only from TOPOST.

## 5. Standing rules reminder
Never commit MP3/MP4/WAV, `__pycache__`, or `.DS_Store` to the repo. This film
uses zero ShowTellCards (all beats are drawings); if you add one, re-check it
against the card test and note the reason in SHOTLIST.md.
