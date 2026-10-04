# CHECKS-REPORT.md — "One AI or many?"

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 10 clean · 0 warnings · 0 errors

| Scene | Beats | Result |
|-------|-------|--------|
| M01_ColdOpen | B00 | clean |
| M02_BlufWriter | B01 | clean |
| M03_Definitions | B02 | clean |
| M04_TwoGaps | B03 | clean |
| M05_Podium | B04 | clean |
| M06_SkillTransfers | B05 | clean |
| M07_TheRule | B06 | clean |
| M08_FourWalls | B07 | clean |
| M09_TheCost | B08 | clean |
| M10_Closing | BVDT, BHTF, BOUT | clean |

## SHOW / HOLD / CARD classification (ai-explainer PROOF GATE)

- SHOW: B00 (composer sketch, ask→result), B01 (writer correction),
  B02 (term cards), B03 (two gap bar-pairs), B04 (podium swapping across
  three rounds), B05 (skill toolbox sliding between tools), B06 (rule card
  + checklist), B07 (four wall bricks + second tool), B08 (hours draining
  into shopping vs feeding "getting good"), BVDT (verdict lines), BHTF
  (prompt card), BOUT (title card).
- HOLD: none. CARD: none. PUNT: none.
- Teaching arc: FRAMEWORK ✓ (B01 BLUF, B03 two gaps) | WORKED EXAMPLE ✓
  (B07 four walls applied to the viewer's situation, B08 cost of shopping)
  | FALSIFIABILITY ✓ (verdict: "If a leaderboard ever changes what you do
  on a Tuesday, believe the leaderboard") | SCAFFOLDED TASK ✓ (BHTF
  interview prompt: "name the wall") | BOOKENDS ✓ (B00/B01/BVDT/BHTF/BOUT)
  | NO-SOURCE-NO-VERDICT ✓ (verdict grounded in B03–B08).

## Pre-gate notes

- make_sheet.py asserts: 12 beats (11–16 band), 7 body beats, every beat's
  dur_s covers its word count at 150 wpm, total 287 s inside the 240–360 s
  (4–6 min) band, all voices Liam. No assertion failures in the final run;
  B07 trimmed and BVDT budgeted during authoring — see BUILD-LOG.md.
- No version numbers, rankings, prices, or vendor names anywhere in the
  package (narration, screen text, metadata) — the one datable risk (the
  podium) carries anonymous shapes only; see FACTCHECK.md.
- Consistency with the companion film `everyone-wants-one-ai` checked
  (no contradiction); see FACTCHECK.md §6.
- BUILD-SHOW: not armed — concept film, no build output to show.
- `manim_layout_audit.py --curve-strict` could not run in this VM
  (no Manim/pangocairo); deferred to the render pass on Bear's Mac.
