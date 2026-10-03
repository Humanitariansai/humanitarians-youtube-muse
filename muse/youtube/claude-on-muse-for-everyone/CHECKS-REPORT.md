# CHECKS-REPORT.md — "Claude making a film about Muse" (general-audience redo)

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 19 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_Bidea | clean |
| M02_Bdefs | clean |
| M03_B01Acts | clean |
| M04_B02Launch | clean |
| M05_B03CloudComputer | clean |
| M06_B04Errands | clean |
| M07_B05Connectors | clean |
| M08_B06Pricing | clean |
| M09_B07Money | clean |
| M10_B08Disk | clean |
| M11_B09Bouncers | clean |
| M12_B10Shield | clean |
| M13_B11Cloud | clean |
| M14_B12Injection | clean |
| M15_B13Approvals | clean |
| M16_B14WebOnly | clean |
| M17_B15Sandbox | clean |
| M18_B16Rules | clean |
| M19_BvdtHtfOut | clean |

## Issues found and fixed (pre-gate)

1. `DashedRectangle` is not a class in the checker's Manim stub —
   `construct()` would raise NameError. Replaced with a plain
   `Rectangle` (ACCENT stroke). Real Manim has DashedRectangle, but the
   gate is the contract.
2. M15 played `FadeIn(finger)` and `finger.animate.shift()` in one
   `play()` — two animations on one mobject fight in real Manim. Split
   into separate plays.
3. make_sheet.py duration assert caught 426 s > 420 s cap on the first
   run; five beats trimmed (words cut to match): final 418 s.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 21 beats (13–22 band), 16 body beats, total 418 s (4.5–7 min
band), BVDT covers all five acts.
