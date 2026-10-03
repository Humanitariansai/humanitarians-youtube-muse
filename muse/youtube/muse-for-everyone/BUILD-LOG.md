# BUILD-LOG.md — "Muse making a film about Muse" (general-audience redo)

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 15:58 — Bear's redo directive arrived: redo the two films under
  `muse/youtube/` for the humanitarians AI YouTube channel; standing
  rules — general audience (smart, pragmatic, not AI experts), explain
  every term, show rather than tell; pick the right skill per film from
  show-tell / cc-explainer / ai-explainer / deep-explainer / lecture.
  Also: push finished work to the humanitarians GitHub; that's where he
  looks.
- 16:00 — Found the two films: `claude-liam-lecture-claude-making-a-film-about-muse/`
  (Bear & Claude's analysis: what it does, costs, business model,
  12-point security critique, how Bear resolved it; 6 acts) and
  `claude-liam-lecture-muse-making-a-film-about-muse/` (product
  explainer: what it is / does / where / how paid; 4 acts).
- 16:05 — Read both ACTS.md files, both FACTCHECK.md files, and the
  SOURCES.md of the analysis film (attribution map). Noted the second
  film's folder has a committed `__pycache__/scenes.cpython-314.pyc`
  and `.DS_Store` files — minor standing-rule violations from a previous
  session; left untouched (not mine to clean without being asked).
  Its `mp3/` holds only timings.json — no audio was committed. Good.
- 16:10 — Redo plan: new folders (originals untouched), same titles, same
  act spines; narration rewritten for non-experts; visuals redrawn
  show-don't-tell. Skill: lecture for this product explainer (whole-product
  coverage); deep-explainer for the analysis film (it's an argument).
  Folder: `muse/youtube/muse-for-everyone/`.
- 16:15 — Wrote ACTS.md (redo notes: what changed), SHOTLIST.md (17
  scenes, every beat drawn), FACTCHECK.md (13 verified claims, all to
  docs/muse.md; judgments labeled).
- 16:20 — Wrote make_sheet.py: 22 beats, 17 body, 404 s (~6m44s) —
  inside the 13–22 beat and 4.5–7 min bands. Generated beat_sheet.json.
- 16:25 — Wrote scenes.py (M01–M17). Applied the film-1 lessons:
  explicit adds before any `.animate()`; collected-mobs FadeOut in M17;
  short on-screen lines. Verified `_Mob` supports indexing/iteration/
  slicing before using them.
- 16:30 — Gate: py_compile clean; static checker 17 clean · 0 warn ·
  0 error on the first full run.
- Next: push the 11 files + folder README, verify via Contents API,
  log FRICTIONAL.md. Then redo the analysis film.
