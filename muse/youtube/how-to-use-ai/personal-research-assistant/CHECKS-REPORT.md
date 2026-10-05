# CHECKS-REPORT.md — Your personal research assistant

Date: 2026-10-04. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode, run
from the film folder with `beat_sheet.json` beside `scenes.py` so the
`until()`/`finish()` pacing path executes).
`python3 -m py_compile` clean on `make_sheet.py` and `scenes.py`.

## Result: 10 clean · 0 warnings · 0 errors

| Scene | Class | Result |
|-------|-------|--------|
| B00 | B00_HeroDesk | clean |
| B01 | B01_TheDecision | clean |
| B02 | B02_TheScope | clean |
| B03 | B03_DemandProof | clean |
| B04 | B04_ThreeLayers | clean |
| B05 | B05_SpotCheck | clean |
| B06 | B06_HollowCitations | clean |
| B07 | B07_TheEcho | clean |
| B08 | B08_CheckDates | clean |
| B09 | B09_TheMap | clean |

## Issues found and fixed

No checker failures: all 10 classes passed on the first run. Two
layout defects were caught by hand-review before the QC run and fixed
in `scenes.py`:
1. **B01 card overlap.** First draft dropped the "your decision" card
   onto exactly the dimmed "the topic" card's position. Fixed: the
   brief box sits at left, the decision card drops into it, and the
   topic card slides away at right.
2. **B02 pile misalignment.** The dimmed replacements for the
   out-of-scope pile were authored at the pre-shift x positions while
   the pile had shifted right. Fixed: dimmed copies anchored to the
   shifted positions (2.25 / 3.55 / 4.85).

## Pre-gate conventions (carried over from the series)

- Every shape introduced with an explicit FadeIn / Create /
  GrowFromCenter (no `.animate`-only introductions); moves, fills and
  Transforms never the only change in a play.
- All explicit coordinates inside the ±6.2 / ±3.4 safe area; type
  floor 32; labels beside objects (or adjacent captions), never inside
  an outline; leader lines keep ≥0.3 gap from their labels; terracotta
  only for dots, checks, the scan-line-like strike, and accents.
- `until()` phrases verified verbatim against each beat's
  `narration_text`; `finish()` closes every scene.
- Stub-only attributes avoided; class names literal
  `class BNN_Name(Scene):` to match `shot.manim.class`.

## Deferred to Bear's Mac render pass

`manim_layout_audit.py --curve-strict` cannot run in this VM (no
Manim/pangocairo) — deferred to the render pass per
CLAUDE-CODE-RENDER.md. The static check does not measure real text
extents, so Bear's pass should also eyeball label/caption fit (notably
the B09 "a map, not the answer" caption and the B02 pile labels) before
the 4K render.
