# BUILD-LOG.md — "Think one step ahead" (how-to-ai #6)

## Decisions

- **Skill: show-tell (kept).** The assigned skill fits: the film is one
  concrete before/after on a small cast of drawn objects (window, slip,
  thinking page, answer page), minimal labels, the voice explains. No other
  skill in the set is a better match.
- **"Precognition" is translated, never taught.** The task brief says the
  word is jargon; the film says "think one step ahead" / "ask for tomorrow's
  answer, today" and never says "precognition" on screen. [judgment]
- **No XML tags on screen.** The source's `<thinking>`-tag mechanic is the
  developer-facing form of the same idea; a general-audience viewer on
  claude.ai gets the benefit from "think it through first, step by step,
  then answer." FACTCHECK.md #5 records the mapping. [judgment]
- **The B01 "before" uses a job-offer question; B05 uses a trip.** Two
  concrete, everyday situations instead of the source's classification
  exercises. [judgment]
- **BDEFS term shortened:** "one word at a time" (18 chars) → "word by
  word" — the skill warns `ClaudeDefinitions` truncates past ~17 chars with
  no gate catching it. Caught by make_sheet.py's own assertion. [record]
- **BHTF `modelLabel`:** "Opus 5.5" (copied from the skill example) →
  "Claude" — the version number is unverifiable; the label is cosmetic.
  [record]
- **Zero Remotion cards in the body** — every body beat passed as a drawing
  of the film's own cast, so no beat met the card test. SHOTLIST.md records
  the reason per beat. [record]

## Failures and fixes

- make_sheet.py assertion failure on first run: BDEFS term "one word at a
  time" is 18 characters, over the ~17-char `ClaudeDefinitions` truncation
  limit. Fixed by renaming the term to "word by word" (narration and show
  events updated); the sheet regenerates clean. [record]
- Pre-write layout pass caught two drawing-law violations before the QC
  gate: B05's prompt slip overlapped the answer page (re-stacked the
  window's vertical layout with clear gaps), and B05 placed a "next" label
  inside the page outline (removed — the terracotta dot and the "tomorrow's
  answer" label carry it). [record]
- B04's check mark sat on the thinking page's corner outline; moved fully
  inside the page. [record]

## QC gate

- `python3 -m py_compile make_sheet.py scenes.py` — clean.
- `static_scene_check.py scenes.py --class <C>` for all 6 scene classes,
  run from a scratch folder holding only scenes.py + beat_sheet.json —
  **6 clean · 0 warnings · 0 errors, first run.**
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo) — deferred to Bear's Mac render pass per the task
  brief; noted in CLAUDE-CODE-RENDER.md. [record]
