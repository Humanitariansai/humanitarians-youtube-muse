# CHECKS-REPORT.md — When it's confidently wrong.

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 14 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_B00 | clean |
| M02_B01 | clean |
| M03_B02 | clean |
| M04_WrongAnswer | clean |
| M05_Insist | clean |
| M06_Mechanism | clean |
| M07_Restart | clean |
| M08_Sources | clean |
| M09_Narrow | clean |
| M10_Stop | clean |
| M11_WorkedExample | clean |
| M12_Verdict | clean |
| M13_YourTurn | clean |
| M14_Outro | clean |

## Issues found and fixed (pre-gate review)

1. **M07 bubble semantics.** The reframed question ("give me three
   possible dates…") was first authored as an AI bubble (white card);
   it is the user's message, so it became a kraft user bubble before
   the first checker run. No checker warning involved — a pedagogy fix.
2. **BOLD/NORMAL at module top.** As in the sibling film, defined
   `BOLD = "BOLD"` / `NORMAL = "NORMAL"` at module top because the QC
   stub's fake manim module does not export them (real Manim does) —
   identical values, harmless under the real import.
3. **M14 outro shape evolution.** Following the sibling film's M16 fix,
   the title (Write), rule line (Create), period dot (FadeIn), and
   handle (FadeIn) give distinct shape-states across plays, so the
   "shapes never change" error cannot fire. The bug() watermark is also
   self.add'ed in every scene including the outro.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 14 beats (13–22 band), 8 body beats, total 317 s (4.5–7 min
band), B00 names the voice ("Liam, in for Bear"), B05 names the
next-word-prediction mechanism, BVDT covers fluency + all four playbook
steps, BHTF names the paste-into-Claude prompt.

## ai-explainer classification

- B00 / B01 / B02 / BVDT / BHTF / BOUT carry `qc.sparse_by_design` with
  a reason (ai-explainer bookend beats: composer cards, term cards,
  verdict lines, title card on cream). The card test was run per beat;
  no beat passed it — zero cards, all drawings.
