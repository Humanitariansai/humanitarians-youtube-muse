# BUILD-LOG.md — "Claude making a film about Muse" (general-audience redo)

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 16:35 — Started redo B after pushing redo A (`muse/youtube/muse-for-everyone/`).
  This is the heavier lift: the original is a 6-act, 23-body-beat analysis
  (what it does, costs, business model, 12-point security critique, Bear's
  resolution, open questions).
- 16:40 — Re-read the original's ACTS.md (full), FACTCHECK.md
  (attribution map), SOURCES.md. The document itself wasn't re-read; the
  original package is the source of record. Kept the attribution
  discipline: Liam narrates Bear & Claude's opinion, never his own facts.
- 16:45 — Redo decisions: 5 acts (open-questions act cut as too technical;
  its honesty survives in the attributed voicing + BHTF); 16 body beats;
  two money beats merged; token allowances cut; BDEFS 5→4 terms; the
  security critique translated to pictures (two bouncers for deny-list,
  hidden-text demo for prompt injection, "a promise, not a wall").
  Skill: deep-explainer shape (it's an argument), lecture discipline.
  Folder: `muse/youtube/claude-on-muse-for-everyone/`.
- 16:50 — Wrote ACTS.md (framing + redo notes), SHOTLIST.md (19 scenes),
  FACTCHECK.md (attribution map preserved, judgments labeled).
- 16:55 — Wrote make_sheet.py. First run FAILED the duration assert:
  426 s vs the 420 s cap. Trimmed five beats honestly (B07 −4 words,
  B09 −7 words, B04/B14 durations to match their word counts, BVDT
  tightened): 21 beats, 16 body, 418 s (~6m58s). Logged — the cap did
  its job.
- 17:00 — Wrote scenes.py (M01–M19) in two chunks. Pre-gate review
  caught two issues: `DashedRectangle` is not in the checker's stub
  (NameError at construct) — replaced with a plain Rectangle; and a
  `FadeIn(finger)` + `finger.animate` in the same play() would fight
  over one mobject in real Manim — split into separate plays.
- 17:05 — Gate: py_compile clean; static checker 19 clean · 0 warn ·
  0 error on the first full run.
- M19 note: the recap shows 6 visual lines for 5 acts — act four's
  content wraps to two lines (the lecture skill's "never 5" pagination
  rule is satisfied as a side effect). The spoken BVDT covers all five
  acts.
- Next: push the 11 files + folder README, verify via Contents API,
  log FRICTIONAL.md.
