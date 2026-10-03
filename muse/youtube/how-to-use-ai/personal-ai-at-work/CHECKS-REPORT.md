# CHECKS-REPORT.md — Stop using your own Claude at work.

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 12 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_Bidea | clean |
| M02_Bdefs | clean |
| M03_B01Samsung | clean |
| M04_B02Ban | clean |
| M05_B03Mechanism | clean |
| M06_B04Retention | clean |
| M07_B05ClaudeToggle | clean |
| M08_B06FourToggles | clean |
| M09_B07Legal | clean |
| M10_B08CleanRoom | clean |
| M11_B09Enterprise | clean |
| M12_RecapHtfOut | clean |

## Issues found and fixed (pre-gate review)

1. **Redundant move_to in M10.** First draft positioned each placeholder
   with `move_to([y - y, 0, 0])` then moved it again — the first call was
   dead code. Fixed: single `move_to([4.6, y, 0])`.
2. **Unused variable in M07.** `tog_knob_start` captured the knob position
   and was never read. Removed.
3. **Recap line widths.** Draft BVDT line 3 was 51 chars; kept all six recap
   lines ≤ 48 chars at font_size 18 so they fit the 12.4-wide plate at
   real-Manin text metrics (same rule as the sibling package).
4. **M12 plate/do-card overlap.** Draft had the do-today card overlapping the
   recap plate's bottom edge; the plate was resized to 12.4×5.0 at UP*0.7
   and the do-card moved to DOWN*2.7 so they never overlap before the
   FadeOut to the watermark.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 14 beats (13–22 band), 9 body beats, total 284 s (4.5–7 min
band), BVDT covers Samsung / training / five-year retention / toggles /
NDA / enterprise.
