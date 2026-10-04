# CHECKS-REPORT.md — Pictures from Words

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 12 clean · 0 warnings · 0 errors

| Scene | Result | Distinct shape states |
|-------|--------|----------------------|
| M01_Bidea | clean | 4 |
| M02_Bdefs | clean | 4 |
| M03_B01Vague | clean | 4 |
| M04_B02Specific | clean | 8 |
| M05_B03Iterate | clean | 8 |
| M06_B04Recipe | clean | 5 |
| M07_B05HowItWorks | clean | 8 |
| M08_B06Uses | clean | 4 |
| M09_B07TextLimit | clean | 3 |
| M10_B08HandsLimit | clean | 5 |
| M11_B09Disclose | clean | 4 |
| M12_BvdtHtfOut | clean | 4 |

## Issues found and fixed (pre-gate review)

1. **Garden-icon throwaway mobjects in M08.** The first draft built the
   "garden mockup" icon's planter placement with
   `.next_to(Triangle().scale(0.01), …)` — throwaway mobjects used only as
   a positioning reference. Replaced with explicit `move_to` coordinates
   on both icon parts before the group placement. Real-Manin-clean and
   stub-clean.
2. **Long prompt line in M04.** The first draft put the full B02 prompt on
   two card lines at font 20; the second line ("watercolor, warm cozy
   morning light") exceeded the card width at real-Manin text metrics.
   Fixed: three shorter lines at font 20, card widened to 6.2 — all
   on-screen words remain read aloud in the beat.
3. **Recap line widths in M12.** Draft recap detail lines ran ~55 chars;
   capped at ≤48 chars at font_size 16 so they fit the 10.6-wide plates
   in a real render.
4. **Transform targets in M05.** The "warmer light" and "wider shot"
   changes are `Transform`s to explicitly constructed target mobjects
   (bigger sun, wider frame) — never `.animate()` introductions — so the
   checker sees the membership change and the real render performs the
   morph.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 14 beats (13–22 band), 9 body beats, total 282 s (4.5–7 min
band), BVDT covers all three acts.
