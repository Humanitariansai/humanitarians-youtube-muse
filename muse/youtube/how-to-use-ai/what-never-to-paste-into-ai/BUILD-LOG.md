# BUILD-LOG.md — What never to paste into AI.

Dated build steps, including failures. Times in America/New_York.

## 2026-10-03

- 21:45 — Received the build task from the parent orchestrator: film #20 of
  24, slug `what-never-to-paste-into-ai`, working title "What never to
  paste into AI", pitch "privacy rules of thumb for everyday use",
  companion to `personal-ai-at-work` (do not contradict; may reference its
  argument). Source: NEW, build from scratch. Assigned skill cc-explainer,
  switch allowed. [record]
- 21:50 — Read cc-explainer/SKILL.md in full, plus the finished sibling
  package `~/workspace/film-builds/how-to-use-ai/personal-ai-at-work/` end
  to end (ACTS, SHOTLIST, FACTCHECK, make_sheet.py, scenes.py, SOURCES,
  PROMPTS, CLAUDE-CODE-RENDER, CHECKS-REPORT conventions), and the lecture
  SKILL.md. [record]
- 21:52 — Skill decision: **lecture**, not cc-explainer. cc-explainer's
  TERMINAL-FIRST law requires a real Claude Code session as the body of the
  film — this film has no terminal, no build, no session to reconstruct;
  forcing one would be a punt. The sibling `personal-ai-at-work` made the
  same call for the same reason on the same day, and the lecture spine
  (BIDEA/BDEFS/BVDT/BHTF/BOUT) is the package convention this build
  follows. [judgment]
- 21:55 — Fact-checking (web, 2026-10-03): verified the "why" beat's three
  claims in general terms — chats may be stored (Anthropic up to 5 years
  opted in / ~30 days opted out), reviewed by staff or contractors (OpenAI
  FAQ + 404 Media Sep 2026 reporting; Anthropic confirms human reviewers
  for opted-in users; Google discloses review of saved Gemini chats), and
  used for training depending on product and settings (consumer opt-out on
  the major chatbots; business plans no training by default). Narration
  phrased evergreen ("depending on the product and its settings") so it
  degrades gracefully as policies change. [record]
- 22:00 — Wrote make_sheet.py: 14 beats, three acts, BIDEA/BDEFS/BVDT/BHTF/
  BOUT. Narration in Teardown for a smart general audience, every term
  explained, no invented statistics, all example data obviously fake.
  Recap carries the required keywords (postcard/password/money/consent/
  redact). Companion consistency checked: same training/opt-out mechanism,
  one self-contained nod to the work film in B06, no contradiction.
- 22:02 — make_sheet.py first run PASSED all assertions:
  beats=14 body=9 total=317s (~5m17s).
- 22:05 — Wrote scenes.py (M01–M12) in the house style, reusing the
  sibling package's helpers (check_mark, bullet, tag_plate, ban_sign,
  toggle_switch) plus cross_out and person_icon. M09 (redaction) and M10
  (anonymize) are the show-don't-tell centerpieces: black bars cover the
  lines; real labels are crossed out and replaced with [CLIENT X] / [R].
- 22:08 — QC gate: `python3 -m py_compile` clean; static_scene_check.py per
  class: 12 clean · 0 warn · 0 error on the first full run. No fixes needed
  — the cross_out/person_icon helpers were written against the stub's
  supported mobjects (Line, Circle, RoundedRectangle, Arc, Text) from the
  start.
- Next: write the remaining docs, push all 12 files via gh-put-file.py,
  verify each with a Contents API read, return the FRICTIONAL.md entry in
  the final report (never push FRICTIONAL.md — concurrent edits).
