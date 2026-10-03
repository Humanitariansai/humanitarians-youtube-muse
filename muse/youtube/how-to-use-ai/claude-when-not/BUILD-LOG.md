# BUILD-LOG.md — "Claude, When Not."

2026-10-03 — pre-render package build (subagent).

## Decisions

- **Skill: show-tell.** The film is one argument in thirteen images:
  scaffold vs. crutch, drawn as a ladder, a scaffold frame, a crutch, and a
  figure. The image shows, Liam's voice tells. `cc-explainer` was the other
  candidate, but the topic has no interface mechanics to explain — it is a
  judgment film, and show-tell's one-drawing-per-beat law fits exactly.
- **Bookends drawn, not Remotion.** `metadata.bookend_exempt` is declared
  with a reason: BIDEA (hesitant writer), BDEFS (term cards), BHTF (drawn
  composer), and BOUT (spoken outro) are Manim scenes in the film's flat
  house style — a single-renderer pipeline on Bear's Mac, consistent with the
  earlier general-audience redos. The beat sheet carries this in
  `bookend_exempt_reason`.
- **Series arc removed.** The source was the H5 season finale (H1–H5 recap).
  Reframed standalone for the "How to use AI" playlist: no season
  references, "boss, client, or readers" instead of "teacher or boss."
- **Narration durations** computed in `make_sheet.py` at 150 wpm + 1 s beat
  pause; BOUT gets the 1.0 s spoken-outro tail. Total: 13 beats, 244 s (~4:04).

## Failures and fixes

- **B08_Answer static QC error (1 error):** 6 explicit coords outside the
  frame, e.g. (7.2, 0.9) in `move_to` — the four predict cards were spaced
  2.9 apart starting at x=-1.5, pushing card D off-frame. Fixed: cards now at
  x = -4.35 + i*2.9 (edges at ±5.65, inside the ±6.2 safe area). Re-ran QC:
  1 clean · 0 warn · 0 error. [record]
- **BHTF composer header band** sat 0.175 above the window's top edge in the
  first draft (band center y=2.1, window top at 2.35). Moved band and header
  text to y=1.925 before the first QC run. [record]
- No other QC failures: all 13 scenes passed the static checker on the first
  run except B08 (above).

## What was not done (pre-render package only)

- No narration audio generated (Bear renders Kokoro `am_onyx` locally).
- No Manim render, no Remotion, no MP3/MP4 committed or staged.
- `beat_sheet.json` holds `estimated_duration_s` only; `actual_duration_s`
  will be written back after Bear generates audio (the kit's `until()` /
  `finish()` pacing reads whichever is present).
