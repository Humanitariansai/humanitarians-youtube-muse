# CHECKS-REPORT.md — The long game

Date: 2026-10-04. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 9 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| B00_Stack | clean |
| B01_AllAtOnce | clean |
| B02_Drift | clean |
| B03_Outline | clean |
| B04_SectionOne | clean |
| B05_Handoff | clean |
| B06_Stitching | clean |
| B07_SideBySide | clean |
| B08_Habit | clean |

## Issues found and fixed (pre-gate review)

1. **Row access via `submobjects`.** First draft of B03 reached into
   `oc.submobjects[1:]` to Create the outline card's rows. Reworked
   `_outline_card` to return `(group, rows)` — cleaner, and safe under
   both the stub and real Manim.
2. **Animate-only shapes.** B04 moves the outline card via
   `.animate().shift()` — the stub records no membership change for
   `animate`, so that play also Fades in the genuinely new section page
   (the sibling film's Gate A lesson). B06's scan-line sweep is a
   move-only play, but that scene has membership changes in four other
   plays. Verified in the checker output: no "shapes never change"
   errors.
3. **Stub/real `get_center()` mismatch.** The design avoids `get_center()`
   arithmetic entirely; all check/arrow/label positions are explicit
   coordinates, hand-verified against the safe area, so the stub and the
   real render agree. (The one exception is `_outline_card`'s
   left-anchored row text, which reads `t.width` after creation — a
   plain property read, not center arithmetic.)
4. **Text-on-card judgment.** The outline card's section rows (B03) and
   the B08 rule card's three lines are the documents' own content
   written on the card — recorded as a judgment in SHOTLIST.md, not a
   label-inside-an-outline violation. All on-card text is ink, size 32.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 13 beats, 9 body (B00–B08), total 202 s (2.5–6 min band).

## Known deferrals (for the Mac render pass)

- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo). Deferred to Bear's Mac per CLAUDE-CODE-RENDER.md.
- Gate T midpoint sampling (no animation in flight at 45–55%, a label
  settled by the midpoint) was designed for: plays are timed off the
  midpoint window wherever the narration allows. Two known soft spots:
  (1) B02's drift dots FadeIn at ~52–55% of the beat (they follow the
  spoken "Facts drift") — they are small terracotta dots, not text, and
  the "it drifts" label plus page numbers are already settled; (2) B07's
  right-side stack FadesIn at ~52–58% (it follows the spoken "On the
  right") — the left label is settled by then. Confirm both on the
  review cut.
