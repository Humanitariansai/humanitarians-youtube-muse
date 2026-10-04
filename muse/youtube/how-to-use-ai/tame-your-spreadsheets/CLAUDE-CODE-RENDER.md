# CLAUDE-CODE-RENDER.md — Tame Your Spreadsheets

Render instructions for Bear's Mac. This package is **pre-render only**:
`beat_sheet.json` (script + shot plan), `scenes.py` (7 Manim scene classes),
and the paperwork. Nothing here is staged for publication; publish only on
Bear's explicit word.

Film identity: persona Liam ("Liam, in for Bear"), Kokoro voice `am_onyx`,
Teardown register, channel `claude-liam`, watermark `@NikBearBrown`.
Working files live in the repo at
`muse/youtube/how-to-use-ai/tame-your-spreadsheets/`; render from a local
checkout of that folder (the toolkit expects a reel folder).

## Render steps

1. **Audio.** From the reel folder:
   `python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>`
   (voice `am_onyx`). Pad BOUT with the 1.0 s silent tail, then write the
   ffprobe-measured durations back to `actual_duration_s` in
   `beat_sheet.json` (the sheet currently carries `estimated_duration_s`
   only — estimates total ~303 s / ~5:03).
2. **Stills first.** Render each scene's last frame at low resolution
   (`manim -ql -s`) into a scratchpad; look at a contact sheet before any
   4K render.
3. **Pre-audit Gate A.** From a scratch folder holding ONLY `scenes.py`
   (that is exactly what `art run`'s Gate A sees), run
   `runtime/qc/static_scene_check.py scenes.py --class <C>` for each of the
   7 classes. Then, in the reel folder, run the layout audit that could not
   run in the build VM (no Manim/pangocairo there):
   `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict`
   for each class; fix any warnings before rendering.
4. **Review cut.** `./brutalist.art/art run <reel> --height 2160`
   (Gates A, B, V and the review cut). Watch the frames — check the B02
   formula text fits its cell and the B04 scan sweep lands before the beat
   midpoint.
5. **Master.** `./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape`
   (GATE T, then the master). Verify: sha, 3840×2160, silent tail on BOUT.
6. **STOP.** Send the master to Bear. Stage (`art post`) and publish only on
   his word, and only from TOPOST.

## Known build-VM limitations (already handled)

- No Manim/pangocairo in the build VM: static QC only (7 clean · 0 warn ·
  0 error). The layout audit and all rendering are deferred to this Mac pass.
- No audio generated in the build VM: `beat_sheet.json` has estimated
  durations; the measured audio sets the master clock (regenerate + remeasure
  if narration changes).

## Scene classes

`B00_MessySheet`, `B01_Coach`, `B02_Formula`, `B03_Check`, `B04_Cleanup`,
`B05_Insight`, `B06_Payoff` — one per body beat, in `scenes.py` (kit pasted
at top; do not import).
