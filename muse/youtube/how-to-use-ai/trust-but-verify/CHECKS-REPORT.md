# CHECKS-REPORT.md — Trust, but verify

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 10 clean · 0 warnings · 0 errors

| Scene | Class | Result |
|-------|-------|--------|
| M01 | M01_Bidea | clean |
| M02 | M02_Bdefs | clean |
| M03 | M03_B01Step1 | clean |
| M04 | M04_B02Demo | clean |
| M05 | M05_B03Crosscheck | clean |
| M06 | M06_B04Numbers | clean |
| M07 | M07_B05Stakes | clean |
| M08 | M08_B06Card | clean |
| M09 | M09_B07YourTurn | clean |
| M10 | M10_B08Outro | clean |

## Issues found and fixed

1. **M08 text-only rows never changed the shape signature.** First draft
   of the habit card had four text rows and one rounded rectangle; the
   checker excludes text from its shape signature, so it reported
   "shapes never change — 1 distinct shape-state across 7 frames".
   Fixed: each row now lands with a non-text ACCENT bullet circle.
   Re-ran all 10 classes — all clean.
2. **Pre-gate conventions carried over from the series:** every shape
   introduced with an explicit FadeIn/Create/GrowFromCenter/GrowArrow
   (no `.animate`-only introductions), all explicit coords inside the
   ±6.3/±3.4 safe area, no generic_art template, stub-only attributes
   avoided.

## nopunt classification (per-beat exit condition)

10 SHOW / 0 justified-HOLD / 0 PUNT-flagged. Every beat's narration makes
a factual or structural claim AND names its on-screen artifact in the
beat sheet's `screen` field (chat card, term plates, meters, demo card,
source cards, number card, stakes bar, habit card, composer, title
card) — each carried by an animated Manim scene with distinct evolving
shapes. No bare cards, no unresolved punts.

Teaching arc: FRAMEWORK ✓ (BDEFS vocabulary before the habit) |
WORKED EXAMPLE ✓ (B02 demo: the claim that dies on step 2) |
FALSIFIABILITY ✓ (each step is a test that can fail the claim) |
SCAFFOLDED TASK ✓ (B07 Your-turn prompt, read verbatim + discussed) |
BOOKENDS ✓ (BIDEA cold open, B07 handoff, B08 title-restate outro) |
NO-SOURCE-NO-VERDICT ✓ (the habit IS the verdict: four sourced checks).

## Deferred to Bear's Mac render pass

`manim_layout_audit.py --curve-strict` cannot run in this VM (no
Manim/pangocairo) — deferred to the render pass per CLAUDE-CODE-RENDER.md.
