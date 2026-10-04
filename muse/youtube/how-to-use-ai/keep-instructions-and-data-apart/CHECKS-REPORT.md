# CHECKS-REPORT.md — Keep instructions and data apart

Written before any render (no render happens in this VM; this is the
pre-render QC gate per the ai-explainer proof gate).

## Static scene gate (mandatory)
`python3 -m py_compile` clean on `make_sheet.py` and `scenes.py`.
`static_scene_check.py scenes.py --class <ClassName>` for every Manim class:

| Class | Warnings | Errors | Notes |
|---|---|---|---|
| B02_SneakyEmail | 0 | 0 | clean |
| B03_FlatBlob | 0 | 0 | clean |
| B04_FenceFix | 0 | 0 | clean |
| B05_MultiDocs | 0 | 0 | clean |
| B06_WhyTags | 0 | 0 | clean |
| B07_FenceNotVault | 0 | 0 | clean |
| B08_Verdict | 0 | 0 | clean after fix (see failures) |

Failures found and fixed (nothing concealed):
1. All 7 classes initially errored: `BOLD` undefined in the QC stub.
   Fixed with a try/except shim (`BOLD = "BOLD"` fallback).
2. `B08_Verdict` failed the shape-distinctness check (1 distinct
   shape-state — static card only). Fixed by adding terracotta bullet Dots
   that appear with each verdict line.
3. B03 used `DashedRectangle` (exists in neither Manim nor the stub);
   replaced with `Rectangle` before the first checker run.

Deferred to Bear's Mac render pass: `manim_layout_audit.py --curve-strict`
(no Manim/pangocairo in this VM), full visual QC on sampled frames,
Kokoro audio timing conform.

## Proof-gate classification (ai-explainer, nopunt-style)
- SHOW: B02, B03, B04, B05, B06, B07, B08 (each beat's `show` block names
  the on-screen artifact; evidence lives on screen; motion enacts the
  narration — e.g. the sneaky line is trapped inside the fence AS the
  voice says it).
- Bookend CARD/HOLD (justified): B00 (cold-open ask), B01 (hesitant-writer
  overview — the writing IS the visual), B09 (handoff prompt held while
  read aloud), B10 (title-restate outro). No PUNT-flagged beats.
- Teaching arc: FRAMEWORK ✓ (B01 BLUF) | WORKED EXAMPLE ✓ (B02 email) |
  FALSIFIABILITY ✓ (B07 fence-not-vault) | SCAFFOLDED TASK ✓ (B09 handoff
  prompt) | BOOKENDS ✓ (ask/overview/verdict/handoff/outro) |
  NO-SOURCE-NO-VERDICT ✓ (B08 verdict rests on B02–B07 evidence).
