# CHECKS-REPORT.md — Slides without the slog

Date: 2026-10-05. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode), run
from a scratch folder holding only `scenes.py` — exactly what Gate A
sees. `python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 9 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| B00_Goal | clean |
| B01_Walls | clean |
| B02_WhyRead | clean |
| B03_Outline | clean |
| B04_OneSlide | clean |
| B05_Polish | clean |
| B06_BackRow | clean |
| B07_SideBySide | clean |
| B08_Habit | clean |

## Issues found and fixed (pre-gate review)

1. **Iso-rise layout bug (B00).** First draft placed the three slide
   cards at increasing x0 with a fixed y0 and oy=1.2; in this
   projection screen-y rises with x, so card C reached y≈4.25 — past
   the ±3.3 safe area. Fixed by laying the row on a constant (x0+y0),
   so all three cards sit at the same screen height, inside bounds.
   The layout math is recorded in the scenes.py header comment.
   [record]
2. **Animate-only shapes.** B04 moves the outline card via
   `.animate().shift()` — the stub records no membership change for
   `animate`, so that play also Fades in the genuinely new slide (the
   companion film's Gate A lesson). B05's lines were kept out of the
   initial `self.add()` so their FadeIn/FadeOut reads as membership
   changes; B06's shrink is a FadeOut/FadeIn swap. Verified in the
   checker output: no "shapes never change" errors.
3. **Stub/real `get_center()` mismatch.** The design avoids
   `get_center()` arithmetic entirely; all check/arrow/label positions
   are explicit coordinates, hand-verified against the safe area, so the
   stub and the real render agree. (The exceptions are `_outline_card`'s
   and B08's left-anchored row text, which read `t.width` after
   creation — a plain property read, not center arithmetic.)
4. **Terracotta ring cut (B06).** The draft had a terracotta ring
   around the back-row zone; a ring is not one of the skill's
   sanctioned terracotta uses (tape, dots, lights, one curve, a check,
   a scan line), so it was removed — the shrink swap carries the
   motion on its own. [judgment]
5. **Sight lines in deep kraft (B02).** The audience sight lines are
   drawn in deep kraft `#9C8462`, not ink, so they don't join the dots
   and the slide into one wide "text" blob (skill: pipes/cables edged
   in ink fail GATE T). [record]
6. **Text-on-card judgment.** The outline card's slide rows (B03/B04),
   the notes card's lines (B05), and the B08 rule card's three lines
   are the documents' own content written on the card — recorded as a
   judgment in SHOTLIST.md, not a label-inside-an-outline violation.
   All on-card text is ink, size 32.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 13 beats, 9 body (B00–B08), total 213 s (2.5–6 min band).
Every beat's `voice` field is `am_onyx` (Kokoro code, not a persona name).

## Known deferrals (for the Mac render pass)

- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo). Deferred to Bear's Mac per CLAUDE-CODE-RENDER.md.
- Gate T midpoint sampling (no animation in flight at 45–55%, a label
  settled by the midpoint) was designed for: labels FadeIn early in
  each beat and no motion is mid-flight at the midpoint. Confirm on the
  review cut.
