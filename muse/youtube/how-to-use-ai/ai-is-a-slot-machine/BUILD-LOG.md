# BUILD-LOG.md — AI is a slot machine.

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 17:21 — Received the film assignment from the parent orchestrator:
  build "AI is a slot machine." as a pre-render package; source
  `claude-for-artificial-intelligence/ai-is-a-slot-machine` in the mirror
  repo; output `muse/youtube/how-to-use-ai/ai-is-a-slot-machine/` in the
  write repo Humanitariansai/humanitarians-youtube-muse.
- 17:22 — Read `skills/make/ai-explainer/SKILL.md` and
  `skills/make/show-tell/SKILL.md` end to end. Decision: **show-tell** —
  the film is a concept piece, not a tool demo; its whole argument rides
  on one visual metaphor (the slot machine), which is exactly the
  show-tell "one drawing per beat, voice explains" lane. The ai-explainer
  spine (Claude UI bookends, ask→result) would have buried the metaphor
  under interface wallpaper. [judgment]
- 17:23 — Studied the finished package
  `~/workspace/film-builds/register-muse-privacy-card/` (11-file
  structure, make_sheet.py assertions, scenes.py conventions,
  CHECKS-REPORT.md format) and the mirror source: fetched
  `beat_sheet.json` (11 beats, Kore persona, remotion cards), README.md,
  PEDAGOGY.md via the GitHub Contents API with the surrogate credential
  flow. Ignored the source `mp3/` folder (never download audio).
- 17:26 — Fact-check research: verified the Kübler-Ross DABDA model
  (1969 *On Death and Dying*; denial/anger/bargaining/depression/
  acceptance; not a fixed sequence) and LLM output non-determinism
  (next-token sampling; not fully deterministic even at temperature 0.0
  per Anthropic docs). Correction applied to the source: the film frames
  the stages as a *borrowed pattern*, not "everyone goes through five
  stages"; the narration hedges "never quite answers the same way twice"
  and "you often get three different answers."
- 17:30 — Wrote ACTS.md (three acts: the machine / the four stuck stages
  / the gambler and the playbook), SHOTLIST.md, FACTCHECK.md, SOURCES.md,
  PROMPTS.md. Ran the show-tell card test against every beat: no beat
  passed (every idea is a thing/part/flow, never an interface or dataset)
  → zero cards, all drawings. [judgment]
- 17:35 — Wrote make_sheet.py: 16 beats, 11 body, asserts (13–22 band,
  BIDEA/BDEFS bookends, BVDT/BHTF/BOUT tail, IN-FOR-BEAR line check,
  recap coverage, 270–420 s band). First run FAILED on my own assertion:
  body-beat filter counted only act "1" (3 beats) instead of acts 1+2+3
  (11). Fixed the filter, re-ran: beats=16 body=11 total=286s (~4m46s).
  Logged because the failure was mine, not the data's.
- 17:40 — Wrote scenes.py (M01–M16) in the show-tell Claude palette
  (cream stage, warm ink, terracotta accent) with the slot machine as the
  recurring cast object and an @NikBearBrown bug in every scene.
  Pre-gate fixes before running QC: `aligned_edge=LEFT` move_to does not
  need the extra half-width shift (removed); dropped `stroke_dash_array`
  (not a Manim CE RoundedRectangle kwarg); every on-screen word is read
  aloud in its beat — B01 line extended to name "a poem, a list, a joke,"
  and B10's ending changed to "pull enough times" to match the M04/M13
  tags.
- 17:45 — Gate run 1: `python3 -m py_compile` clean on both files, but
  static_scene_check reported NameError on 14/16 classes — the QC stub's
  fake manim module does not define BOLD/NORMAL (real Manim does).
  Fixed by defining BOLD="BOLD"/NORMAL="NORMAL" at module top (identical
  values to real Manim; harmless under the real import).
- 17:47 — Gate run 2: 15 clean, M16_Outro errored "shapes never change"
  — text is excluded from shape signatures, so the title/dot/handle had
  only one shape-state across three plays. Fixed: added a terracotta
  rule line that draws under the title before the period dot lands.
- 17:50 — Gate run 3: **16 clean · 0 warnings · 0 errors.** No warnings
  or errors hidden or waived.
- Next: write CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md; push
  all 12 files via gh-put-file.py; verify each via the Contents API;
  return the FRICTIONAL.md entry text.
