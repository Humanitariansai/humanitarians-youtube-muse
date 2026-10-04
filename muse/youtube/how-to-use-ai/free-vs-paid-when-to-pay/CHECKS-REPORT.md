# CHECKS-REPORT.md — Free vs paid: when to pay.

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.
`manim_layout_audit.py --curve-strict` could not run in this VM (no
Manim/pangocairo) — deferred to Bear's Mac render pass.

## Result: 14 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_Bidea | clean |
| M02_Bdefs | clean |
| M03_FreeTier | clean |
| M04_Wall | clean |
| M05_FourThings | clean |
| M06_SharpModel | clean |
| M07_LimitMath | clean |
| M08_FreeEnough | clean |
| M09_Payoff | clean |
| M10_TwoQuestions | clean |
| M11_Trap | clean |
| M12_Verdict | clean |
| M13_YourTurn | clean |
| M14_Outro | clean |

## Issues found and fixed

1. **make_sheet.py class-matching assertion bug (pre-run).** Compared the
   beat's shot class against `"M" + scene` (producing `"MM01"`). Fixed to
   a startswith check before the first generation run. [record]
2. **M05_FourThings TypeError (first QC run).** `P(1.75, 0.75, 0)` passed
   three arguments to the two-argument `P()` helper. Fixed to
   `p + np.array([1.75, 0.75, 0])`; all 14 scenes clean on re-run. [record]
3. **Narration tuning (pre-QC).** Four narration lines rewritten so every
   on-screen word is read aloud in its beat (BIDEA card text, B03 panel
   labels, B05 "stay free" tag, B07 yes/no branches matching the
   flowchart); B07 duration 27→28 s. The lines were correct before the
   checker ran. [record]

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 14 beats (13–22 band), 9 body beats, total 359 s (3–6 min
band), BIDEA names the voice ("Liam, in for Bear"), BVDT covers the four
menu items plus the wall, the fee, the two-question test, and the
one-month-before-annual rule, BHTF carries the paste-into-your-AI prompt.

## ai-explainer classification

- BIDEA / BDEFS / BVDT / BHTF / BOUT carry `qc.sparse_by_design` with a
  reason (ai-explainer bookend beats: one card or a few lines on cream).
  The card test was run per beat; no beat passed it — zero cards, all
  drawings. `bookend_exempt: ["cold-open", "bvdt"]` is declared in
  metadata with the ai-explainer reason (hesitant-writer open, recap beat).
- BUILD-SHOW: not armed — concept film, no build; no BFLOW/BSHOW slots.
- Skill switch (cc-explainer → ai-explainer) is justified in BUILD-LOG.md:
  no terminal session exists to show; inventing one would violate
  REAL-SESSION / DOUBLE-CHECK.
