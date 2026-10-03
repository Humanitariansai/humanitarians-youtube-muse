# BUILD-LOG.md — Stop using your own Claude at work.

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 17:21 — Received the build task from the parent orchestrator: film from
  mirror-repo source `claude-for-artificial-intelligence/how-to-use-your-
  personal-ai-at-work`, output slug `personal-ai-at-work`, write path
  `muse/youtube/how-to-use-ai/personal-ai-at-work/`, working title "Stop
  using your own Claude at work.", skill deep-explainer or cc-explainer
  suggested.
- 17:22 — Read the source beat sheet (Kore persona, 11 beats incl. GREETING
  + VERDICT + B01B tangent cards), README rebuild guide, and PEDAGOGY.md
  (empty) via the GitHub Contents API with the surrogate credential flow.
- 17:25 — Read the finished sibling package
  `~/workspace/film-builds/register-muse-privacy-card/` end to end to copy
  its 12-file convention exactly (make_sheet.py assertions, scenes.py house
  palette and helpers, CHECKS-REPORT conventions).
- 17:30 — Skill decision: **lecture**, not deep-explainer or cc-explainer.
  cc-explainer is about real terminal sessions — this film has no terminal.
  deep-explainer's parent laws already bind through lecture's lineage, but
  lecture's BDEFS key-terms beat is exactly what the audience rewrite needs
  (every technical term defined in plain language up front), and lecture's
  BIDEA/BVDT/BHTF/BOUT spine is the one this package convention implements.
  [judgment]
- 17:35 — Read the existing `muse/FRICTIONAL.md` via the Contents API to
  match the seven-field entry format. Confirmed the target path
  `muse/youtube/how-to-use-ai/` does not exist yet in the write repo; the
  Contents API will create it on first file push.
- 17:40 — Fact-checking (web): Samsung April 2023 three-leak story verified
  (TechSpot, Communications Today, TechTimes); Anthropic toggle + 5-year
  retention + forward-only opt-out verified (c-ai.chat, Engadget,
  theaicareerlab); ChatGPT / Grok / Gemini toggle paths verified against
  current guides; Team/Enterprise no-training defaults verified. Dropped two
  garbled attributions from the source ("the not a lawyer", "one additional
  guide") — the guide could not be identified, so the film carries Liam's
  own "I'm no lawyer — talk to yours" instead. [judgment]
- 17:50 — Wrote make_sheet.py: 14 beats, five acts, BIDEA/BDEFS/BVDT/BHTF/
  BOUT. Narration rewritten for Teardown: ~150 wpm, every term explained,
  no "chapter"/"book" references, no invented numbers. Added a per-beat
  ~150-wpm duration sanity assertion alongside the band assertions.
- 17:52 — make_sheet.py first run PASSED all assertions:
  beats=14 body=9 total=284s (~4m44s).
- 17:55 — Wrote scenes.py (M01–M12) in the house style, reusing the sibling
  package's helpers (check_mark, bullet, tag_plate) plus ban_sign and
  toggle_switch. M10 is the show-don't-tell centerpiece: confidential lines
  crossed out and replaced with placeholders. No real UI screenshots
  anywhere — settings panels are drawn sketches.
- 18:00 — QC gate: `python3 -m py_compile` clean; static_scene_check.py per
  class: 12 clean · 0 warn · 0 error on the first full run. (Two sloppy
  lines fixed before the run: an unused variable in M07 and a redundant
  move_to in M10 — caught in self-review, not by the checker.)
- Next: write the remaining docs, push all 12 files via gh-put-file.py,
  verify each with a Contents API read, return the FRICTIONAL.md entry in
  the final report (never push FRICTIONAL.md — concurrent edits).
