# CHECKS-REPORT.md — "You can't beat AI."

Written before the QC gate run; the gate results are below.

## Pre-gate classification

- 11 SHOW / 1 justified-HOLD (S12 outro title card) / 0 PUNT-flagged
- Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
  SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓

## Gate results (2026-10-03)

- `python3 -m py_compile make_sheet.py scenes.py` — clean.
- `static_scene_check.py scenes.py --class <each>`, 12 classes:

| Scene | Result |
|---|---|
| S01_ColdOpen | clean — 6 distinct / 12 |
| S02_WriterOverview | clean — 3 distinct / 12 |
| S03_ThePattern | clean — 4 distinct / 12 |
| S04_GpsMetaphor | clean — 8 distinct / 12 |
| S05_TheDistinction | clean — 5 distinct / 12 |
| S06_TheScenario | clean — 9 distinct / 12 |
| S07_FiveSteps | clean — 8 distinct / 12 |
| S08_TheSignal | clean — 3 distinct / 12 |
| S09_TheTrap | clean — 5 distinct / 12 |
| S10_Verdict | clean — 7 distinct / 12 |
| S11_Handoff | clean — 2 distinct / 12 |
| S12_Outro | **ERROR on first run** — 1 distinct / 12 (shapes never change) |

**Total: 12 clean · 0 warnings · 0 errors** (after the S12 fix).

## Failures and fixes

1. S12_Outro failed the distinctness check on the first run: a text-only
   outro produced 1 shape-state across 4 frames (text is excluded from
   shape states). Fix: added evolving non-text shapes — a spark star at
   open and a terracotta underline that grows (short line FadeOut →
   long line Create). Re-ran: clean, 3 distinct / 12. [record]
2. make_sheet.py self-assertions caught two authoring bugs before any
   file was written: overview word count (48 > 45) and five beats under
   the speech floor. Fixed in make_sheet.py (see BUILD-LOG.md). [record]
3. Latent bug fixed before QC: S09 used an inline `__import__("math")`
   hack for tick positions; replaced with module-level `import math`.
   [record]

No failures concealed; no check was relaxed to pass.
