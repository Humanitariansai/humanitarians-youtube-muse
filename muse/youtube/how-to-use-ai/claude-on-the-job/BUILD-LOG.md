# BUILD-LOG.md — "Claude, On the Job."

## 2026-10-03 — package build (subagent, pre-render only)

- Read the skill: `show-tell` chosen over `cc-explainer`. The film is a
  concept explainer (a tier map, a practice, a boundary) with no code,
  no CLI loop, and no product UI to demonstrate — show-tell's "one drawn
  image per beat, the voice explains" fits; cc-explainer's prompt→code→
  output machinery does not. [judgment]
- Fetched the source from the mirror repo via the GitHub Contents API with
  the `custom.github` surrogate credential: `beat_sheet.json` (11 beats),
  `README.md`, `PEDAGOGY.md` under
  `claude-for-artificial-intelligence/hai-on-the-job/`. Ignored `mp3/`
  (never download audio). [record]
- Rewrote for the channel's general audience: dropped the "Claude, For
  Students" framing, the "am I too late?" cold open, and classroom-integrity
  material; kept the tier map, the scarce-skill reframe, the daily loop, the
  never-delegate list, and the fire-the-vendor quiz. Every technical term
  (tier, conduct, hallucination, audit) is defined aloud in BDEFS. [judgment]
- Cut the word "distrust-calibration" from the narration: a series neologism
  that would need its own definition beat for a general audience. The idea
  survives as the B06 practice ("name one thing it got wrong") — shown,
  not named. [judgment]
- Folded the source's PREDICT/VERDICT pair into one drawn beat (B08):
  show-tell drops the verdict card, and a four-pill quiz with a cursor tap
  teaches better as a drawing than as a card. [judgment]
- Kept the narration free of statistics, dates, and version numbers on
  purpose: nothing to date, nothing for Kokoro to misread. [judgment]
- Wrote `make_sheet.py` (with self-assertions: 13 beats, 176 s total,
  hesitant-writer trigger verbatim, BDEFS term lengths ≤ 17, outro kind/tail);
  generated `beat_sheet.json`. First run passed all assertions. [record]
- Wrote `scenes.py`: iso_kit pasted at top (not imported), 9 scene classes,
  one per body beat, cast kept whole-film (dark machine block, ink human
  figure, white output pages, terracotta checks/dots).
- FAILURE (caught by static QC): `B01_TierOne` first failed with
  "shapes never change — 1 distinct shape-state across 11 frames." Cause: the
  five pages entered via `animate.shift()` (moves), which the stub ignores,
  and the ghost figure swap was shape-identical to the original. Fix: pages
  now enter with `FadeIn(..., shift=DOWN*1.4)` — a new non-text shape per
  play, and the fast drop is the beat's motion claim ("superhuman recall").
  Also updated the beat's `visual_intent` in `make_sheet.py` to match
  ("drop in fast" instead of "fly in fast") and regenerated the sheet.
  [record]
- Avoided stub traps found while writing: VGroup indexing replaced with
  plain Python lists (`tasks_list`, `pill_list`, `cap_list`); all label
  placement uses fixed coordinates (no `get_center()` arithmetic); no
  `rate_functions` easings, no `path_arc`, no `Indicate`, no group slices.
  [record]
- Final: `py_compile` clean on both files; static QC 9/9 scenes, 0 warnings,
  0 errors (run per class, in the build folder with `beat_sheet.json`
  beside `scenes.py` so `until()` pacing is live). [record]
- Wrote the remaining 9 docs (ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS,
  CHECKS-REPORT, CLAUDE-CODE-RENDER, README, this log). [record]

Not done (by design, pre-render package): audio generation, stills, render,
Gates A/B/V/T on Bear's Mac. See CLAUDE-CODE-RENDER.md.
