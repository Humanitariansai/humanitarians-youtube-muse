# CHECKS-REPORT.md — Don't get fooled.

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 13 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_ColdOpen | clean |
| M02_Bluf | clean |
| M03_Mechanism | clean |
| M04_ConfidentTone | clean |
| M05_LawyerStory | clean |
| M06_Grounding | clean |
| M07_IDontKnow | clean |
| M08_CitationAudit | clean |
| M09_CrossCheck | clean |
| M10_ThreeSentences | clean |
| M11_Recap | clean |
| M12_YourTurn | clean |
| M13_Outro | clean |

## Issues found and fixed (pre-gate review)

1. **Text-metric overflow pass.** The static checker does not measure
   text widths, so a layout audit was done by hand against real-Manim
   text metrics before the gate run. Fixed: the B00 ask and both output
   lines split/repositioned; the B01 naive line shortened to "AI lies
   because it's badly trained." and the correction split into two lines;
   the B02 sentence stem split into two lines; the B03 quote shortened to
   "“Signed in 1847.”"; the B04 brief widened to 10.4 with an ellipsized
   citation line; the B05 instruction split into two lines; the B06
   question/answer cards widened and the "I don't know" ring changed to a
   terracotta ellipse; the B07 answer/doc cards widened; the B08 claim
   card widened to 8.8; the B09 sentence cards became two-line cards with
   checks beside them; the BVDT recap lines shortened; the BHTF composer
   widened to 12.4 with the prompt wrapped to four lines; the BOUT title
   set at size 64. No on-screen word was changed in meaning — every
   on-screen word is still read aloud in its beat.
2. **M02 strike positioning.** As in the sibling films, the strike-through
   is built from `t_b.get_left()`/`get_right()` after the Write plays —
   no estimated coordinates.
3. **make_sheet.py asserts.** The sheet generator asserts: 13 beats
   (13–22 band), 8 body beats each 45–70 words, B01 BLUF 20–35 words with
   `lead_silence_s: 0.8`, "Liam, in for Bear" in B00, the handoff prompt
   read aloud in BHTF, recap keyword coverage in BVDT, total 180–360 s.
   Generated: 13 beats, 311 s (~5m11s).

No checker warnings or errors were hidden or waived. `manim_layout_audit.py
--curve-strict` could not run in the build VM (no Manim/pangocairo); it is
deferred to Bear's Mac render pass (see CLAUDE-CODE-RENDER.md §3).

## ai-explainer classification

- B00 is the composer cold open (ask → result); B01 is the hesitant-writer
  BLUF (≥ 9 s, lead_silence_s 0.8, the reel's actual misconception
  corrected); BVDT is the verdict recap page; BHTF is the handoff
  (greeting "Your turn.", the suggested prompt read aloud verbatim and
  discussed); BOUT is the title-restate outro. B01 / BVDT / BHTF / BOUT
  carry `qc.sparse_by_design` with reasons (bookend beats: one card or a
  few lines on cream). The composer appears only where the interface is
  the subject (cold open, handoff); every inner beat illustrates its
  idea.
