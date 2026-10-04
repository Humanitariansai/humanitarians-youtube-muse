# CLAUDE-CODE-RENDER.md — Keep instructions and data apart

Paste-ready render instructions for Bear's Mac (Manim + Kokoro TTS voice `am_onyx`).
Run from the film folder after downloading it from
`muse/youtube/how-to-use-ai/keep-instructions-and-data-apart/` in
Humanitariansai/humanitarians-youtube-muse.

## 0. Preconditions
- Manim installed with pangocairo (needed for the layout audit below).
- Kokoro TTS available; voice `am_onyx`.
- This package contains NO audio and NO video — pre-render only.

## 1. Layout audit (deferred from the VM build)
The VM build ran `static_scene_check.py` (7/7 clean, 0 warnings, 0 errors)
but could NOT run the real layout audit — no Manim/pangocairo in the VM.
Run it here before rendering:

```bash
python3 ~/workspace/brutalist.art/runtime/qc/manim_layout_audit.py --curve-strict scenes.py
```

Fix any layout failures in `scenes.py` at the source; do not loosen the checker.

## 2. Generate narration audio
One MP3 per beat from `beat_sheet.json` narration_text, Kokoro `am_onyx`,
Teardown register pacing. Measure each file's duration; the beat sheet's
`duration_s` values are estimates (words/2.3 per sec) — re-time the visual
beats to the measured audio (audio is the master clock).

## 3. Render the Manim beats
```bash
manim render -qm --format=mp4 scenes.py B02_SneakyEmail B03_FlatBlob B04_FenceFix \
  B05_MultiDocs B06_WhyTags B07_FenceNotVault B08_Verdict
```
Conform each to its beat's measured audio duration.

## 4. Build the Remotion bookends
- B00: `ClaudeComposerAsk` — greeting "Hej, Liam", command
  "Why is Claude following a line I never wrote?", runningText
  "checking the prompt boundary…", the three output lines from the sheet.
- B01: `BrutalistHesitantWriter` — text/triggerWords/replacementWords/seed
  from the sheet; `lead_silence_s: 0.8`; verify the beat's media ≥ 8s and the
  correction lands on screen before the cut.
- B09: `ClaudeComposerAsk` — greeting "Your turn.", runningText
  "paste this into Claude…", the full handoff command typed in.
- B10: `ClaudeTitleOutro` — title "Keep instructions and data apart.",
  handle `@NikBearBrown`, one of the 18 crisp-safe mascots (slug-seeded),
  NO subline. Liam re-reads the title, then "At Nik Bear Brown" — spoken,
  never scored.

## 5. Assemble, caption, QC
Conform to audio, mux, generate captions (faster-whisper pipeline), then the
frame-level VISUAL QC pass (ffmpeg ≥2fps + 15/50/85% beat samples, 9-point
rubric). Fix root causes in scene source until zero BLOCKER/MAJOR defects.

## 6. Never publish
The build stays local for human review. Publish only on Bear's explicit instruction.
