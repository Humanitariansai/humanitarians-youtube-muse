# CHECKS-REPORT.md — "ChatGPT or Claude?" (general-audience redo)

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 10 clean · 0 warnings · 0 errors

| Scene | Beats | Result |
|-------|-------|--------|
| M01_ColdOpen | B00 | clean |
| M02_BlufWriter | B01 | clean |
| M03_Definitions | B02 | clean |
| M04_TheRule | B03 | clean |
| M05_ChartsLie | B04 | clean |
| M06_ContextFolder | B05 | clean |
| M07_ChatgptLane | B06 | clean |
| M08_TwoExits | B07 | clean |
| M09_TheTest | B08 | clean |
| M10_Closing | BVDT, BHTF, BOUT | clean |

## SHOW / HOLD / CARD classification (ai-explainer PROOF GATE)

- SHOW: B00 (composer sketch, ask→result), B01 (writer correction),
  B02 (term cards), B03 (two doors + chart X), B04 (leaderboard X +
  driveway), B05 (retype loop vs folder feed), B06 (three tiles),
  B07 (two exits, held), B08 (stopwatch + side-by-side outputs),
  BVDT (verdict lines), BHTF (prompt card), BOUT (title card).
- HOLD: none. CARD: none. PUNT: none.
- Teaching arc: FRAMEWORK ✓ (B01 BLUF) | WORKED EXAMPLE ✓ (B05 folder,
  B08 test) | FALSIFIABILITY ✓ (verdict: "if the test ever says the chart
  was right, believe the chart — but run the test first") | SCAFFOLDED
  TASK ✓ (BHTF interview prompt) | BOOKENDS ✓ (B00/B01/BVDT/BHTF/BOUT) |
  NO-SOURCE-NO-VERDICT ✓ (verdict grounded in B03–B08).

## Pre-gate notes

- make_sheet.py asserts: 12 beats (11–16 band), 7 body beats, every beat's
  dur_s covers its word count at 150 wpm, total 273 s inside the 270–420 s
  (4.5–7 min) band, all voices Liam. One assertion failure during build
  (B05 word count) — fixed by trimming one word; see BUILD-LOG.md.
- No version numbers anywhere in the package (narration, screen text,
  metadata) — the one datable element (the source title) was retitled;
  see FACTCHECK.md §1.
- BUILD-SHOW: not armed — concept film, no build output to show.
