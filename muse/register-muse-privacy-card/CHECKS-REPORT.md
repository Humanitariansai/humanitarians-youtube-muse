# CHECKS-REPORT.md — Register for Muse with a privacy.com card

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 13 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_Bidea | clean |
| M02_Bdefs | clean |
| M03_B01Platforms | clean |
| M04_B02Fork | clean |
| M05_B03Hold | clean |
| M06_B04VirtualCard | clean |
| M07_B05NewCard | clean |
| M08_B06Limit | clean |
| M09_B07UseIt | clean |
| M10_B08Names | clean |
| M11_B09Connect | clean |
| M12_B10YoureIn | clean |
| M13_BvdtHtfOut | clean |

## Issues found and fixed (pre-gate review)

1. **Animate-only shapes never enter the scene graph.** In M01, M05, M08
   and M12, shapes were introduced via `obj.animate....` inside `play()`
   without ever being added. Real Manim auto-adds animated mobjects, but
   the stub records no membership change for `animate` kind, so the
   checker would never see them — and the scenes would have failed
   "shapes never change". Fixed: every shape gets an explicit
   FadeIn/Create/GrowFromCenter in its own play call before any
   `.animate()` motion.
2. **Stub-only attribute in M13.** The first draft removed on-screen text
   with `hasattr(m, '_text')` — `_text` exists only on the checker's stub
   `_Text`, not on real Manim mobjects, so the cleanup would silently do
   nothing in the real render and leave recap text under the watermark.
   Fixed: collect recap mobjects in a list and FadeOut the whole group.
3. **Recap line widths.** First-draft M13 recap lines were ~60 chars at
   font_size 24 (≈17 units wide) — wider than the 16:9 frame in a real
   render. Fixed: lines shortened to ≤48 chars at font_size 20, plate
   widened to 12.4.
4. **make_sheet.py assertion bug.** The recap-coverage assertion counted
   lowercase "act " but the line uses "Act two"/"Act three".
   Fixed to case-insensitive; beat_sheet.json then generated cleanly
   (15 beats, 10 body, 296 s).

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 15 beats (13–22 band), 10 body beats, total 296 s (4.5–7 min
band), BVDT covers all three acts.
