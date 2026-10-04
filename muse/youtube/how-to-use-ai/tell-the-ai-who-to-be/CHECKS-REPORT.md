# CHECKS-REPORT — Tell the AI who to be

QC gate per the show-tell skill, run 2026-10-03 in this VM.

## Gate 1 — py_compile

`python3 -m py_compile make_sheet.py scenes.py` — clean, no output.

## Gate 2 — static_scene_check.py (per scene class)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`
run with `beat_sheet.json` beside `scenes.py` (as Gate A sees it).

| Scene class | Result | Warnings | Errors |
|---|---|---|---|
| B00_RoleLine | clean | 0 | 0 |
| B01_Calibrate | clean | 0 | 0 |
| B02_DialsMove | clean | 0 | 0 |
| B03_TwoDoctors | clean | 0 | 0 |
| B04_RoleVsPersona | clean | 0 | 0 |
| B05_WhenItHelps | clean | 0 | 0 |
| B06_SpecificBeatsVague | clean | 0 | 0 |

Total: 7 clean · 0 warnings · 0 errors. No failures, no fixes needed — nothing
concealed.

## Deferred (cannot run in this VM — no Manim/pangocairo)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict`
  (GATE T layout audit). Deferred to Bear's Mac render pass per
  CLAUDE-CODE-RENDER.md.
- Full `art run` / `art final` Gates A, B, V, T. Deferred to Bear's Mac.

## Design notes for the render pass

- Every scene keys all motion to narration phrases inside the first ~30% of the
  beat via `until()`, so no animation is mid-flight at the clip midpoint under
  real (shorter-than-estimate) Kokoro audio. Estimated durations use the house
  `words/2.5` convention and are deliberately conservative; the measured audio
  sets the real clock.
- B05's left-box cards drop via `animate.shift` (not Transform) after the
  polygon-Transform crumple trap noted in the skill.
- B04's giant quote mark is GHOST grey (never terracotta text); B05's check is
  terracotta (allowed: checks); all other text is ink ≥ 32.
