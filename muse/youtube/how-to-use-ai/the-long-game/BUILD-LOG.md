# BUILD-LOG.md — The long game

Dated build steps, including failures. Times in America/New_York.

## 2026-10-04

- 20:20 — Received the film task: slug `the-long-game`, NEW source
  (build from scratch), assigned skill show-tell, pitch "Long documents:
  outline first, then sections, then stitching — writing anything big
  without it falling apart. Companion to the existing film
  small-steps-big-jobs."
- 20:22 — Read `skills/make/show-tell/SKILL.md` end to end (spine,
  bookends, the 9 laws, drawing kit, drawing laws, card test, Gate A/B/T/V
  traps, workflow).
- Skill decision: KEEP show-tell (the assigned skill). The film is a
  single-habit explainer — "an image every beat, minimal text, the voice
  explains" fits exactly. No beat passes the card test toward a card
  (every idea is a thing, a part, or a flow — the outline card's rows and
  the rule card's lines are the documents' own content, not interface
  ideas), so the film uses zero cards, which the skill calls a normal,
  complete show-tell film. [judgment]
- 20:25 — Read the sibling film `small-steps-big-jobs` package in full
  (make_sheet.py, scenes.py kit + scene patterns, SHOTLIST/FACTCHECK/
  SOURCES/BUILD-LOG/CHECKS-REPORT/PROMPTS/CLAUDE-CODE-RENDER/README
  formats) and the static QC checker source, to match conventions exactly.
- 20:30 — Wrote make_sheet.py. First run: 13 beats, 9 body, 202 s
  (~3m22s) — inside the 3–6 min band on the first pass. Assertions
  (13 beats, 9 body, 150–360 s, B00–B08 ids) all pass.
- 20:35 — Extracted the iso_kit block byte-identical from the sibling's
  scenes.py (never imported, per the skill), then wrote the 9 scene
  classes. Design notes: the outline card is an iso page carrying its
  four numbered section rows as content; B04 pairs the card's
  `.animate().shift()` with a genuine FadeIn (the section page) per the
  sibling's Gate A lesson; the scan line's sweep is a move-only play but
  the scene has membership changes in four other plays; plays were kept
  out of each beat's 45–55% midpoint window wherever the narration
  allows (two known soft spots flagged in CHECKS-REPORT.md).
- 20:38 — Fixed `_outline_card` to return `(group, rows)` instead of
  reaching into `submobjects` for the row Create plays (cleaner and
  stub-safe).
- 20:40 — Gate: `python3 -m py_compile` clean on make_sheet.py and
  scenes.py; static_scene_check.py per class: 9 clean · 0 warn · 0 error
  on the first full run.
- Known deferrals (not concealments): `manim_layout_audit.py
  --curve-strict` cannot run in this VM (no Manim/pangocairo) — deferred
  to Bear's Mac render pass, noted in CLAUDE-CODE-RENDER.md. Gate T
  midpoint-type compliance was designed for but cannot be verified here;
  two soft spots flagged in CHECKS-REPORT.md for the Mac pass.
- Next: write CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md; push
  all 12 files via gh-put-file.py to
  `muse/youtube/how-to-use-ai/the-long-game/`; verify each with a
  Contents API read.
