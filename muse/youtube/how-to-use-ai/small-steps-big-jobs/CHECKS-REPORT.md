# CHECKS-REPORT.md — Small steps, big jobs

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 9 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| B00_GiantBox | clean |
| B01_MushOut | clean |
| B02_WhyFails | clean |
| B03_StepOne | clean |
| B04_StepTwo | clean |
| B05_Materials | clean |
| B06_Timeline | clean |
| B07_SideBySide | clean |
| B08_OneJob | clean |

## Issues found and fixed (pre-gate review)

1. **B05 covered two real steps.** First draft had one beat for materials
   + timeline ("Same for materials. Same for the timeline."). The skill's
   law 9 forbids merging two real steps to come in shorter, and the film
   ran 179 s — under the brief's ~3-minute floor. Split into B05
   (materials) and B06 (timeline, carrying the "handoff is the whole
   trick" payoff); side-by-side → B07, habit → B08. Final: 13 beats,
   9 body, 195 s.
2. **Card labels would have left the frame.** First draft put each step
   name `next_to(card, RIGHT)`; cards 3–4 sit far enough right that the
   labels would cross the ±6.3 safe area. Fixed: one top-center step
   label per beat ("step two: layout", "step three: materials",
   "step four: timeline"), each replacing the last.
3. **Animate-only shapes.** B01/B06 move groups via `.animate().shift()`
   — the stub records no membership change for `animate`, so every such
   play also Fades in a genuinely new shape (the page in B01, card4 in
   B06). Verified in the checker output: no "shapes never change" errors.
4. **Stub/real `get_center()` mismatch.** The design avoids `get_center()`
   arithmetic entirely; all check/arrow/label positions are explicit
   coordinates, hand-verified against the safe area, so the stub and the
   real render agree.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 13 beats, 9 body (B00–B08), total 195 s (2.5–6 min band).

## Known deferrals (for the Mac render pass)

- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo). Deferred to Bear's Mac per CLAUDE-CODE-RENDER.md.
- Gate T midpoint sampling (no animation in flight at 45–55%, a label
  settled by the midpoint) was designed for: plays are timed off the
  midpoint window wherever the narration allows. One known soft spot:
  B02's five job-name labels land at ~77% of the beat (they follow the
  spoken list "budget, layout, materials, the timeline, and your
  taste"); the beat's early label "five small jobs" (19%) keeps type on
  screen at the midpoint. Confirm on the review cut.
