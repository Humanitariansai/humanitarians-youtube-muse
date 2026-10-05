# CHECKS-REPORT — Code without coding

QC gate per the show-tell skill, run 2026-10-04 in this VM.

## Gate 1 — py_compile

`python3 -m py_compile make_sheet.py scenes.py` — clean, no output.

## Gate 2 — static_scene_check.py (per scene class)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`
run with `beat_sheet.json` beside `scenes.py` (as Gate A sees it).

| Scene class | Result | Warnings | Errors |
|---|---|---|---|
| B00_YourPage | clean | 0 | 0 |
| B01_HowItWorks | clean | 0 | 0 |
| B02_Checkable | clean | 0 | 0 |
| B03_OnlyYou | clean (after fix) | 0 | 0 |
| B04_TooBig | clean | 0 | 0 |
| B05_NoSecrets | clean (after fix) | 0 | 0 |
| B06_TestIt | clean | 0 | 0 |
| B07_DescribeItBack | clean | 0 | 0 |
| B08_WhyNow | clean | 0 | 0 |

Total: 9 clean · 0 warnings · 0 errors.

### Failures found and fixed (nothing concealed)

1. **B03_OnlyYou / B05_NoSecrets — coords outside the safe area (first run).**
   The "password" `name_tag` started at y=3.6 (above the ±3.3 safe area) so it
   could drop in from off-stage. The checker flagged 3 coords in each scene.
   Fix: re-staged both drops to start inside the frame (B03: y=2.94 with a
   smaller ring; B05: y=2.9 with the window lowered to cy=0.2). Re-ran: clean.
2. **Latent template bug (pre-gate).** The pasted `iso_kit.py` `open_box`
   had a duplicated point making a degenerate quad; fixed while pasting
   (unused by this film's scenes, fixed for truthfulness).

## Deferred (cannot run in this VM — no Manim/pangocairo)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict`
  (GATE T layout audit). Deferred to Bear's Mac render pass per
  CLAUDE-CODE-RENDER.md.
- Full `art run` / `art final` Gates A, B, V, T. Deferred to Bear's Mac.

## Design notes for the render pass

- Every scene keys all motion to narration phrases inside the first ~35% of
  the beat via `until()`, so no animation is mid-flight at the clip midpoint
  under real (shorter-than-estimate) Kokoro audio. Estimated durations use the
  house `words/2.5` convention and are deliberately conservative; the measured
  audio sets the real clock.
- B04's clean page lands at ~68% of its beat and B07's fix at ~63% — both
  start motion well clear of the midpoint margin window; verified in SHOTLIST.
- B08's curve is drawn in ink with `Create()` and a terracotta end dot (per
  the skill: never a half-drawn terracotta curve); the hero "25%" is ink,
  never terracotta text.
- B03's "password" tag bounces off the ring with two separate
  `animate.shift` plays (never `animate` + another animation on the same
  object in one play).
- B06's buttons are CARD pills with ink outlines (white needs the outline for
  Gate V contrast on the cream stage).
