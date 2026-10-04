# BUILD-LOG.md — "Plan anything."

## 2026-10-03 — package build (subagent, pre-render only)

- Read the skill: `show-tell` kept as assigned (no switch). The film is a
  drawn explainer — one picture per beat, the voice carries the argument; no
  code, no CLI loop, no product UI to demonstrate — so show-tell's "one drawn
  image per beat" fits and no other make skill fits better. [judgment]
- No mirror source: this film is NEW, built from scratch per the brief (film
  17 of 24). The demo arc (weekend trip: constraints → draft → revise →
  checklist) and the four-step loop are the film's own constructs; all trip
  details are fictional. Recorded as FICTIONAL in FACTCHECK.md, never as
  price or availability claims. [record]
- Wrote `make_sheet.py` (with self-assertions: 12 beats, 176.8 s total,
  hesitant-writer trigger verbatim, BDEFS term lengths ≤ 17, outro kind/tail,
  composer greeting); generated `beat_sheet.json`. First run failed its own
  trigger-verbatim assertion (case mismatch: trigger "plan my whole weekend
  trip" vs text "Plan my whole weekend trip for me?"); fixed the trigger's
  capitalization and re-ran clean. [record]
- Wrote `scenes.py`: iso_kit pasted at top (not imported), 8 scene classes,
  one per body beat, cast kept whole-film (white plan pages, kraft constraint
  chips in an open box, ink revision arc, terracotta dots/checks, ink human
  figure). [record]
- Beat design decisions: B05 (projects) and B06 (budgets) share the
  constraint-box + draft-page layout deliberately — the repetition IS the
  point ("the pattern travels"), with distinct labels (a project / a budget,
  launch / payday) and distinct draft pictures (timeline bars vs a bar split
  into three segments). B01 keeps three individually labelled chips
  (budget/dates/interests) because naming the constraints is that beat's job;
  B05/B06 use one "constraints" label since the voice names deadline/team and
  income/goals aloud (law 2: the voice explains). [judgment]
- Card test: no cards used — every beat's idea is a thing, a part, or a flow
  (loop blocks, box, pages, arc, pills, magnifier). Recorded in SHOTLIST.md. [judgment]
- Kept the narration free of statistics, dates, version numbers, and current
  prices on purpose: nothing to date, nothing for Kokoro to misread. The one
  factual claim (B07: model memory goes stale) is qualitative and grounded in
  the published knowledge-cutoff documentation (see SOURCES.md); no date is
  quoted in the film. [judgment]
- Final: `py_compile` clean on both files; static QC 8/8 scenes, 0 warnings,
  0 errors (run per class, in the build folder with `beat_sheet.json`
  beside `scenes.py` so `until()` pacing is live). [record]
- Wrote the remaining 9 docs (ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS,
  CHECKS-REPORT, CLAUDE-CODE-RENDER, README, this log). [record]
- Pushed all 12 files to `muse/youtube/how-to-use-ai/plan-anything/` on
  Humanitariansai/humanitarians-youtube-muse via the gh-put-file.py helper;
  every push verified with a Contents API read afterwards. [record]

Not done (by design, pre-render package): audio generation, stills, render,
Gates A/B/V/T on Bear's Mac. See CLAUDE-CODE-RENDER.md.
