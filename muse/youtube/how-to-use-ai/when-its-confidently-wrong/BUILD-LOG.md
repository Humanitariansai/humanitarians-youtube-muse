# BUILD-LOG.md — When it's confidently wrong.

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 21:44 — Received the film assignment from the parent orchestrator:
  build "When it's confidently wrong" as a pre-render package; source
  NEW; slug `when-its-confidently-wrong`; write-repo path
  `muse/youtube/how-to-use-ai/when-its-confidently-wrong/`; suggested
  skill deep-explainer (switch allowed).
- 21:50 — Read `skills/make/deep-explainer/SKILL.md` end to end, then
  `skills/make/ai-explainer/SKILL.md`. Decision: **ai-explainer** — the
  film's teaching problem is one insight + one mechanism + one 4-step
  playbook, not the 4+ linked mechanisms deep-explainer is built for;
  the assignment's band (roughly 3–6 minutes, 13–22 beats, 12-file
  pre-render package) contradicts deep-explainer's natural band (5–10
  minutes, 30–50 beats, documentary library-first pipeline). Shipping a
  deep-explainer would have forced padding the film to fit the skill.
  The chat/composer window is ai-explainer's natural recurring visual
  anchor — and it is exactly where the AI insists. [judgment]
- 21:52 — Studied the finished package
  `~/workspace/film-builds/how-to-use-ai/ai-is-a-slot-machine/` (12-file
  structure, make_sheet.py assertions, scenes.py conventions,
  CHECKS-REPORT.md format) to keep the how-to series package identical.
- 21:55 — Fact-check research: verified next-token autoregressive
  generation (inference-engineering handbook; ckvermaai deep-learning
  notes), LLM overconfidence and confidence escalation when challenged
  (debate-calibration study via marginalrevolution; UC Irvine "calibration
  gap"; Kalai et al. via temperature2 on benchmarks rewarding confident
  guessing over abstention). The statistics stay in FACTCHECK.md only —
  the script carries no numbers that could date it. [record]
- 22:00 — Wrote ACTS.md (three acts: the problem / the recovery
  playbook / putting it to work), SHOTLIST.md, FACTCHECK.md, SOURCES.md,
  PROMPTS.md. Ran the ai-explainer card test against every beat: no beat
  passed (every idea is a thing/part/flow — a chat exchange, a gauge, a
  word chain, a playbook step — never an interface or a dataset) → zero
  cards, all drawings. [judgment]
- 22:05 — Wrote make_sheet.py: 14 beats, 8 body, asserts (13–22 band,
  B00/B01 bookends, BVDT/BHTF/BOUT tail, IN-FOR-BEAR line check, mechanism
  keyword check, recap coverage, 270–420 s band). First run clean:
  beats=14 body=8 total=317s (~5m17s).
- 22:10 — Wrote scenes.py (M01–M14) in the ai-explainer Claude palette
  (cream stage, warm ink, terracotta accent) with the chat window as the
  recurring cast object and an @NikBearBrown bug in every scene.
  Pre-gate fix before running QC: the reframed question in M07 was an
  AI bubble — semantically it is the user's message, so it became a
  kraft user bubble.
- 22:15 — Gate run 1: `python3 -m py_compile` clean on both files;
  `static_scene_check.py` per class for all 14 classes: **14 clean ·
  0 warnings · 0 errors** on the first run. No warnings or errors
  hidden or waived.
- Next: write CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md, README.md; push
  all 12 files via gh-put-file.py; verify each via the Contents API;
  return the FRICTIONAL.md entry text.
