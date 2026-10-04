# BUILD-LOG.md — Trust, but verify

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 21:44 — Received subagent task: build Film 21 ("trust-but-verify",
  "Trust, but verify") as a pre-render package; REFACTOR of
  `fellows/aujaswi-a/2026-08-19-how-to-spot-unreliable-ai-research`;
  assigned skill ai-explainer.
- Skill choice: **ai-explainer, as assigned** — the film is a
  concept explainer (a verification habit for a general audience), not
  a CLI build (claude-cli), not a skill teardown, not a student lesson.
  Fits the ai-explainer lane: vox-style middle, Teardown register,
  Claude bookends at render time. No switch.
- Read `skills/make/ai-explainer/SKILL.md` (bookend spine, Teardown
  register, IN-FOR-BEAR law, handoff/outro laws) and the QC checker
  contract (`static_scene_check.py`: runs construct() under a stub,
  shapes-must-evolve per scene, 16:9 frame bounds, no generic_art).
- Fetched the refactor source via the Contents API (surrogate
  custom.github): 7-beat sheet on spotting unreliable AI research
  (recency / authority / corroboration) + source README. Generalized
  the argument per the brief: the 60-second habit (confidence
  question, open the source, independent search, numbers show work)
  + stakes calibration, for everyday claims.
- Grounded the hook fact via web search: the "10% of the brain" myth
  is a documented neuromyth (CNRS, Scientific American / Barry
  Gordon). Logged in FACTCHECK.md. The B02 demo claim is a
  *constructed illustration* of a hallucinated answer — documented as
  such, never endorsed.
- Authored the 12-file package in
  `~/workspace/film-builds/how-to-ai/trust-but-verify/`: ACTS,
  SHOTLIST, FACTCHECK, make_sheet.py, beat_sheet.json (generated),
  scenes.py (10 scenes), SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS,
  CLAUDE-CODE-RENDER, README.
- QC gate: `python3 -m py_compile` clean on both files first try.
  Static checker: 9/10 clean first try; M08_B06Card failed with
  "shapes never change" — its rows were text-only and text is excluded
  from the checker's shape signature. Fixed by giving each recap row a
  non-text ACCENT bullet circle that lands with the row. Re-ran all 10
  classes: **10 clean · 0 warnings · 0 errors.**
- Pushed all 12 files to
  `muse/youtube/how-to-use-ai/trust-but-verify/` on
  Humanitariansai/humanitarians-youtube-muse via gh-put-file.py, and
  verified every file live with a Contents API read. No
  FRICTIONAL.md / README.md / QUEUE.md touched (explicitly out of
  scope for this task).
