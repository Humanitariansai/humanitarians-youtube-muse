# CHECKS-REPORT.md — "Show It an Example"

## Gate results (2026-10-03, this VM)

- `python3 -m py_compile make_sheet.py` — clean.
- `python3 -m py_compile scenes.py` — clean.
- `static_scene_check.py scenes.py --class <C>` for all 7 scene classes —
  **0 warnings, 0 errors** (run twice: once from a scratch folder holding ONLY
  `scenes.py`, once with `beat_sheet.json` beside it so `until()`/`finish()`
  pacing is live, matching what `art run`'s Gate A sees).

| Class | Result (scratch-only) | Result (with beat sheet) |
|---|---|---|
| B00_TheBox | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B01_RuleStack | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B02_ExamplesIn | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B03_FiveThings | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B04_BadCard | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B05_ThreeChecks | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| B06_ShortVsTall | clean · 0 warn · 0 error | clean · 0 warn · 0 error |

## Pre-checker review (caught before running the checker)
- B03's card row was first laid out in raw iso coordinates, which would have
  rendered as a diagonal staircase (iso x runs right-up). Fixed with a
  `_place()` helper that lands each card's centre at an explicit screen
  coordinate, so the row is level. [fixed before first run]
- B04's bad card at iso-x 4.1 initially overshot the frame; re-seated the row
  at screen x = 0.7 / 2.25 / 3.8 / 5.35 with 0.9×1.1 cards. [fixed before first run]
- B06 labels sat 0.2 below the card bottoms; moved to y=-2.85 (0.3 clearance)
  and dropped the shadow to y=-3.2. [fixed before first run]

## Deferred to Bear's Mac render pass
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo installed). Bear runs it per `CLAUDE-CODE-RENDER.md`
  before the review cut.
- Real-Manin text metrics, Gate T midpoint sampling, and Gate V contrast are
  render-time gates; the scenes were written against the skill's drawing laws
  (labels beside objects, ≥0.3 leader gaps, text ≥32, all motion in the first
  ~40% of each clip) to pass them.
