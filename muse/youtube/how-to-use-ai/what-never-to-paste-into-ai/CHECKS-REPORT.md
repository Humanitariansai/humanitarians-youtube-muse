# CHECKS-REPORT.md — What never to paste into AI.

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.
`manim_layout_audit.py --curve-strict` cannot run in this VM (no Manim /
pangocairo); deferred to Bear's Mac render pass per CLAUDE-CODE-RENDER.md.

## Result: 12 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_Bidea | clean |
| M02_Bdefs | clean |
| M03_B01Why | clean |
| M04_B02Settings | clean |
| M05_B03Passwords | clean |
| M06_B04Money | clean |
| M07_B05OtherPeople | clean |
| M08_B06Work | clean |
| M09_B07Redact | clean |
| M10_B08Anonymize | clean |
| M11_B09Pause | clean |
| M12_RecapHtfOut | clean |

## Issues found and fixed (pre-gate review)

None required. The helpers (`cross_out`, `person_icon`) were written
against the stub's supported mobject set on the first draft, and every
explicit coordinate was kept inside the safe area (±6.3 x, ±3.4 y) — the
widest elements are the M12 recap plate (12.4 wide at UP*0.7) and the
do-today card (9.4 wide at DOWN*2.7), copied from the sibling package's
verified geometry.

## Notes

- Recap line 2 is 48 chars at font_size 18 — at the sibling package's
  measured limit for the 12.4-wide plate; kept because it reads aloud
  verbatim ("Pasted text can be stored, reviewed, trained on."). Flagged
  here so the Mac render pass can confirm the fit.
- No text block in any scene is narration set as type: on-screen text is
  labels, tags, and example lines, all read aloud in their beat.
- beat_sheet.json validates: 14 beats (13–22 band), 9 body beats, total
  317 s (4–6 min band), BVDT covers postcard / passwords / money numbers /
  other people's details / work secrets / redact-anonymize-describe.
- Teaching arc: the BIDEA postcard image is the film's single memorable
  rule; each never-list item is shown struck out or locked away before the
  fix is shown; the HUMAN-equivalent close (B09) turns the rule into a
  3-second reflex; BHTF makes the viewer generate their own checklist.
