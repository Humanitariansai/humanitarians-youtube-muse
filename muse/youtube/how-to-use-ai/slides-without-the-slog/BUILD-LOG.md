# BUILD-LOG.md — Slides without the slog

Dated build steps, including failures. Times in America/New_York.

## 2026-10-05

- 17:19 — Received the film task: slug `slides-without-the-slog`,
  title "Slides without the slog", film #41, Wave 6 "Making things",
  assigned skill show-tell, pitch "Turn rough notes into a real deck:
  outline first, then slides, then polish. Companion to the existing
  film the-long-game — reference it as the companion, don't re-teach
  it. Never quote pricing tiers."
- 17:20 — Read `skills/make/show-tell/SKILL.md` end to end (spine,
  bookends, the 9 laws, drawing kit, drawing laws, card test, Gate A/B/T/V
  traps, workflow).
- Skill decision: KEEP show-tell (the assigned skill). The film is a
  single-habit explainer — "an image every beat, minimal text, the voice
  explains" fits exactly. No beat passes the card test toward a card
  (every idea is a thing, a part, or a flow — the outline card's rows,
  the notes card's lines, and the rule card's lines are the documents'
  own content, not interface ideas), so the film uses zero cards, which
  the skill calls a normal, complete show-tell film. [judgment]
- 17:25 — Read the companion film `the-long-game` package in full
  (make_sheet.py, scenes.py kit + scene patterns, SHOTLIST/FACTCHECK/
  SOURCES/BUILD-LOG/CHECKS-REPORT/PROMPTS/CLAUDE-CODE-RENDER/README
  formats) and the static QC checker source, to match conventions exactly.
- 17:30 — Wrote ACTS.md (two acts: the one-prompt trap / the three
  moves) and make_sheet.py. First run: 13 beats, 9 body, 213 s
  (~3m33s) — inside the 2.5–6 min band on the first pass. Assertions
  (13 beats, 9 body, 150–360 s, B00–B08 ids) all pass. All per-beat
  `voice` fields are `am_onyx` (the Wave 5 persona-as-voice bug
  explicitly checked for — not present here).
- 17:35 — Extracted the iso_kit block byte-identical from the
  companion's scenes.py (never imported, per the skill), then wrote the
  9 scene classes. Design notes: B04 pairs the outline card's
  `.animate().shift()` with a genuine FadeIn (the slide) in one play,
  per the companion's Gate A lesson; B05 keeps the slide's lines out of
  the initial `add()` so their FadeIn/FadeOut reads as membership
  changes; B06 drops the planned terracotta ring (a ring is not one of
  the sanctioned terracotta uses) and lets the shrink swap carry the
  motion; sight lines use deep kraft `#9C8462` so they don't fuse into
  an ink blob (skill: pipes edged in ink fail).
- 17:40 — Pre-gate layout review caught one real bug before the QC
  run: in the first B00 draft the three slide cards drifted up out of
  the safe area (screen-y rises with x in this projection, so card C at
  x0=4.1 with oy=1.2 reached y≈4.25, past the ±3.3 safe area). Fixed by
  laying the row on a constant (x0+y0) so all three cards sit at the
  same screen height, inside bounds. [record]
- 17:45 — Gate: `python3 -m py_compile` clean on make_sheet.py and
  scenes.py; static_scene_check.py per class from a scratch folder
  holding only scenes.py (what Gate A sees): 9 clean · 0 warn ·
  0 error on the first full run.
- Known deferrals (not concealments): `manim_layout_audit.py
  --curve-strict` cannot run in this VM (no Manim/pangocairo) — deferred
  to Bear's Mac render pass, noted in CLAUDE-CODE-RENDER.md. Gate T
  midpoint-type compliance was designed for (labels settle early;
  nothing fades mid-flight at the midpoint) but cannot be verified here;
  all explicit coordinates were hand-checked against the safe area, and
  the layout math is recorded in the scenes.py header comment.
- Next: write CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md; push
  all 12 files via gh-put-file.py to
  `muse/youtube/how-to-use-ai/slides-without-the-slog/`; verify each with a
  Contents API read.
