# BUILD-LOG.md — Muse Does the Assignment

Built 2026-10-06 by Muse, lecture skill, for INFO 6205. Single-session build:
assignment in the morning, film by the evening.

- Read the assignment notebook (1 markdown cell: the Beary pathfinding spec).
- Audited it by solving: found 4 defects (expected output 6 vs correct 12;
  always-valid-path vs return -1; unstated movement model; "at least one B").
  Fixes verified by two independent optimal implementations + 300-grid fuzz.
- Bear approved the fixes; pushed `Wk1_Beary_Pathfinding_Assignment_FIXED.ipynb`
  to `Coursera Info 6205 Algorithms/wk1-beary-pathfinding/` (original kept).
- Bear: "use the lecture skill with the Liam persona to make a film on Muse
  doing a assignment one for info 6205 algorithms."
- Wrote `make_sheet.py` (19 beats: 5 bookends + 14 Manim body beats, ~385 s
  estimated), `scenes.py` (14 scene classes + Grid helper + checkmark helper).
- Static QC (`static_scene_check.py`, per-class): first pass 8/14 clean.
  - `BOLD` NameError (stub has no BOLD) → string weights, as in wave-6 reels.
  - 5 scenes failed the distinct-shape gate for stub-legitimate reasons:
    in-place `set_fill` doesn't register; `Axes.plot` returns the axes in the
    stub; `SurroundingRectangle` reads as text in the stub; text glyphs
    ("✓", "○", subscripts) don't count as shapes.
  - Fixed by making the motion real shapes: overlay highlight rects, split
    tour Creates, drawn check marks (two-stroke VMobjects), explicit
    Rectangle boxes, hand-built 2^K curve from screen coordinates, drawn
    circles → checks. Second pass: 14/14 clean, 0 warnings, 0 errors.
  - Note for the Mac pass: these changes are render-identical or better in
    real Manim (drawn checks and explicit boxes were always the safer choice).
- Render smoke test (VM, 1080p): B01_Grid and B11_Wall rendered; frames
  inspected — grid, labels, palette, and the 2^K explosion all correct.
- `manim_layout_audit.py --curve-strict` NOT run (no pangocairo in this VM) —
  Bear's Mac runs it per CLAUDE-CODE-RENDER.md before the review cut.
- Estimated runtime ~6m25s (narration clock). Lane histogram: 14 Manim,
  5 bookend slates. No paid steps; no approval gates tripped (all free).
- Course credit: `metadata.course` set; INFO 6205 named in BIDEA narration.
  Outro stays the locked claude-liam `ClaudeTitleOutro`.
