# BUILD-LOG.md — Small steps, big jobs

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 21:44 — Received the Film 11 task: slug `small-steps-big-jobs`, NEW
  source (build from scratch), assigned skill show-tell, core idea from
  the brief (giant prompt → mush; budget → layout → materials →
  timeline steps, each building on the last; side-by-side comparison).
- 21:45 — Read `skills/make/show-tell/SKILL.md` end to end (spine,
  bookends, the 9 laws, drawing kit, drawing laws, card test, Gate A/B/T/V
  traps, workflow).
- Skill decision: KEEP show-tell (the assigned skill). The film is a
  single-habit explainer — "an image every beat, minimal text, the voice
  explains" fits exactly. No beat passes the card test toward a card
  (every idea is a thing, a part, or a flow — the side-by-side is two
  drawings, not a `tabs` card), so the film uses zero cards, which the
  skill calls a normal, complete show-tell film. [judgment]
- 21:50 — Read the reference package (`example-make_sheet.py`), the
  `iso_kit.py` template (pasted verbatim at the top of scenes.py — never
  imported, per the skill), the static QC checker source, and the
  sibling film `register-muse-privacy-card` docs (ACTS/SHOTLIST/FACTCHECK/
  SOURCES/BUILD-LOG/CHECKS-REPORT/PROMPTS/CLAUDE-CODE-RENDER formats).
- 21:55 — Fetched `muse/FRICTIONAL.md` from the write repo via the
  Contents API (surrogate credential flow) to match the seven-field
  entry format.
- 22:00 — Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md,
  PROMPTS.md. FACTCHECK keeps the brief's rule: no invented statistics,
  claims behavioral and modest — the "why now" number beat is replaced
  by the takeaway beat (B08), recorded as a judgment.
- 22:05 — Wrote make_sheet.py. First run: 12 beats / 8 body / 179 s —
  under the brief's ~3-minute floor, and B05 was covering two real steps
  (materials + timeline) in one beat, which law 9 forbids merging.
  Split B05 into B05 (materials) and B06 (timeline, carrying the
  "handoff is the whole trick" payoff); side-by-side → B07, habit →
  B08. Re-ran: 13 beats, 9 body, 195 s (~3m15s) — inside the 3–6 min
  band. Assertions (13 beats, 9 body, 150–360 s, B00–B08 ids) all pass.
- 22:10 — Wrote the scenes body (9 classes, literal
  `class BNN_Name(Scene):`), prepended the kit byte-identical, wrote
  scenes.py. Pre-gate self-review: all explicit coordinates checked
  against the ±6.3 × ±3.4 safe area; labels placed beside objects with
  ≥0.3-unit leader gaps; no `rate_functions.ease_in_quad` (kit `ease_in`
  used); no `path_arc` animates; no `get_center()` arithmetic; every new
  shape enters via FadeIn/Create/GrowFromCenter before any `.animate()`
  motion; plays kept out of each beat's 45–55% midpoint window where the
  narration allows.
- 22:12 — Gate: `python3 -m py_compile` clean on make_sheet.py and
  scenes.py; static_scene_check.py per class: 9 clean · 0 warn · 0 error
  on the first full run.
- Known deferrals (not concealments): `manim_layout_audit.py
  --curve-strict` cannot run in this VM (no Manim/pangocairo) — deferred
  to Bear's Mac render pass, noted in CLAUDE-CODE-RENDER.md. Gate T
  midpoint-type compliance (a label settled by each beat's midpoint)
  was designed for but cannot be verified here; B02's five job-name
  labels land at ~77% of the beat by narration pacing — flagged in
  CHECKS-REPORT.md for the Mac pass.
- Next: write CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md; push
  all 12 files via gh-put-file.py to
  `muse/youtube/how-to-use-ai/small-steps-big-jobs/`; verify each with
  a Contents API read.
