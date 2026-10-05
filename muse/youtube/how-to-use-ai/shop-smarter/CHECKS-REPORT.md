# CHECKS-REPORT.md — "Shop smarter"

QC gate run 2026-10-05, in `~/workspace/film-builds/how-to-ai/shop-smarter/`.

## 1. `python3 -m py_compile`

- `make_sheet.py` — clean.
- `scenes.py` — clean (also clean after the B02 fix below).

## 2. `static_scene_check.py scenes.py --class <ClassName>` (all 9 classes)

| Class | Result |
|---|---|
| B00_ThreeOptions | 1 clean · 0 warn · 0 error |
| B01_Priorities | 1 clean · 0 warn · 0 error |
| B02_TheTable | 1 clean · 0 warn · 0 error (after fix; see §3) |
| B03_Tradeoffs | 1 clean · 0 warn · 0 error |
| B04_ReviewFunnel | 1 clean · 0 warn · 0 error |
| B05_FinePrint | 1 clean · 0 warn · 0 error |
| B06_MoneyTraps | 1 clean · 0 warn · 0 error |
| B07_StalePrices | 1 clean · 0 warn · 0 error |
| B08_TheMethod | 1 clean · 0 warn · 0 error |

**Total: 9 clean · 0 warnings · 0 errors.** The check ran with
`beat_sheet.json` beside `scenes.py`, so the `until()` narration pacing
executed against the real sheet (no fallbacks, no missing-phrase silences —
every `until()` phrase was additionally verified present verbatim in its
beat's narration; see BUILD-LOG.md).

## 3. Failures and fixes

- **B02_TheTable — "shapes never change" (1 error, first pass).** The grid
  was drawn with a single `Create(grid)` play, which the Gate A stub did not
  register as a membership change ("1 distinct shape-state across 4 frames").
  Fixed by splitting the draw into two plays — `Create(verticals)` then
  `Create(horizontals)` via two new helpers (`table_grid_v`/`table_grid_h`;
  `table_grid()` still composes the full grid for B03's continuity fade-in).
  The visual is unchanged: the full grid is still completely drawn well
  before the midpoint. Re-ran the checker: clean. Nothing waived.
- No other failures. The `voice: am_onyx` assertion in `make_sheet.py` (the
  Wave 5 bug class) passed for all 13 beats, and the BDEFS terms-length guard
  (≤17 chars) passed.

## 4. Deferred (cannot run in this VM)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict` —
  requires Manim/pangocairo, not installed here. Deferred to Bear's Mac render
  pass (see CLAUDE-CODE-RENDER.md). Mitigation: all explicit coordinates are
  inside ±6.2 × ±3.3, all type ≥ 40 px, labels sit beside objects with leader
  gaps ≥ 0.3, terracotta is used only for dots/checks/rings/X-marks, numerals
  are ink, connector cable uses deep kraft `#9C8462`, and every scene's motion
  completes in the first ~40% of its beat (GATE T samples the midpoint).
