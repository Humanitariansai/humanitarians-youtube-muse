# BUILD-LOG.md — Your personal research assistant

Dated build steps, including failures. Times in America/New_York.

## 2026-10-04

- 20:17 — Received subagent task: build one pre-render film package
  ("personal-research-assistant", "Your personal research assistant"):
  deep-research features — how to brief it well, read its answers,
  what to distrust; companion to Film 21 `trust-but-verify`; assigned
  skill show-tell.
- Skill choice: **show-tell, as assigned** — the film is a step-by-step
  explainer where each beat is one motion on a small cast (the research
  desk, source pages, the report), exactly the show-tell lane. No
  switch. Read the show-tell SKILL.md (bookend spine, nine laws, card
  test, drawing kit + GATE traps) and studied the sibling films
  `make-it-interview-you-first` (show-tell package conventions) and
  `trust-but-verify` (companion film, fact-check conventions).
- Card test applied per body beat (SHOTLIST.md "why a card" column):
  every body beat is a thing, a part, or a flow from the film's own
  cast — zero cards, all drawings. Recorded the reasoning here.
- Fact research (web, 2026-10-04): deep-research modes across the major
  chat AIs browse the web, read dozens of sources, return cited
  reports in minutes (SOURCES.md items 1–3); Tow Center study —
  generative search tools cite wrongly without flagging uncertainty
  (item 4); Lily Ray's "AI slop loop" — AI misinformation entering
  retrieval corpora and getting cited back (item 5, the "echo" beat);
  Stanford study — chatbots draw on a narrower source set than web
  search (item 6, the "thin research" beat). No statistics, prices,
  versions, or menu paths anywhere in narration — the durability rule.
- Authored the 12-file package in
  `~/workspace/film-builds/how-to-ai/personal-research-assistant/`:
  ACTS, SHOTLIST, FACTCHECK (real table, PASS/EXEMPT verdicts),
  make_sheet.py, beat_sheet.json (generated, 14 beats, 240.0 s),
  scenes.py (iso kit pasted verbatim + original helpers + 10 scene
  classes B00–B09), SOURCES, BUILD-LOG, CHECKS-REPORT, PROMPTS,
  CLAUDE-CODE-RENDER, README.
- QC gate: `python3 -m py_compile` clean on both files first try.
  Static checker: **10/10 clean first try · 0 warnings · 0 errors.**
  Two authoring fixes were caught by hand before the QC run (B01's
  decision card landed exactly on the dimmed topic card — re-laid-out
  so the decision drops into the brief box at left; B02's dimmed
  replacements were misaligned with the shifted out-of-scope pile —
  re-anchored to the shifted positions).
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo) — deferred to Bear's Mac render pass, noted in
  CLAUDE-CODE-RENDER.md and CHECKS-REPORT.md.
- Pushed all 12 files to
  `muse/youtube/how-to-use-ai/personal-research-assistant/` on
  Humanitariansai/humanitarians-youtube-muse via gh-put-file.py, and
  verified every file live with a Contents API read. No FRICTIONAL.md
  / README.md / QUEUE.md touched (coordinator's scope).
