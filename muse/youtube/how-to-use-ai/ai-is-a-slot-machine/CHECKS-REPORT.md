# CHECKS-REPORT.md — AI is a slot machine.

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 16 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_Bidea | clean |
| M02_Bdefs | clean |
| M03_Machine | clean |
| M04_Probabilistic | clean |
| M05_Stages | clean |
| M06_Denial | clean |
| M07_Anger | clean |
| M08_Bargaining | clean |
| M09_Depression | clean |
| M10_Gambler | clean |
| M11_ThreeVersions | clean |
| M12_Intern | clean |
| M13_Batches | clean |
| M14_Recap | clean |
| M15_YourTurn | clean |
| M16_Outro | clean |

## Issues found and fixed (pre-gate review)

1. **BOLD/NORMAL missing from the QC stub.** The stub's fake manim
   module does not export `BOLD`/`NORMAL` (real Manim does), so 14 of 16
   classes raised NameError on the first gate run. Fixed: defined
   `BOLD = "BOLD"` / `NORMAL = "NORMAL"` at module top — identical values
   to the real Manim constants, so the real render is unaffected.
2. **M16 "shapes never change".** Text is excluded from the checker's
   shape signatures, so the title (Write), period dot (one FadeIn), and
   handle (text) produced only one shape-state across three plays.
   Fixed: a terracotta rule line now draws under the title before the
   period dot lands — two new non-text shapes in later plays.
3. **make_sheet.py assertion bug.** The body-beat assertion filtered only
   `act == "1"` (3 beats) instead of acts 1+2+3 (11). Fixed the filter;
   beat_sheet.json then generated cleanly (16 beats, 11 body, 286 s).
4. **Pre-gate drawing fixes (before first QC run):** removed a redundant
   half-width shift after `aligned_edge=LEFT` move_to; dropped
   `stroke_dash_array` (not a Manim CE RoundedRectangle kwarg); B01 and
   B10 narration lines extended/adjusted so every on-screen word is read
   aloud ("a poem, a list, a joke"; "pull enough times").

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 16 beats (13–22 band), 11 body beats, total 286 s (4.5–7 min
band), BIDEA names the voice ("Liam, in for Bear"), BVDT covers the
mechanism, all five stages, and all three playbook rules, BHTF names the
paste-into-Claude prompt.

## Show-tell classification

- BIDEA / BDEFS / BVDT / BHTF / BOUT carry `qc.sparse_by_design` with a
  reason (show-tell bookend beats: one card or a few lines on cream).
  The card test was run per beat; no beat passed it — zero cards, all
  drawings. `bookend_exempt: ["cold-open", "bvdt"]` is declared in
  metadata with the show-tell reason (hesitant-writer open, recap beat).
