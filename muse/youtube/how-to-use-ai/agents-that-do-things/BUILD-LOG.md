# BUILD-LOG.md — Agents: AI that does things.

Dated build steps, including failures, fixes, and judgment calls.

## 2026-10-04 — build

- **Skill: ai-explainer, as assigned.** This film is a general-audience
  concept explainer (what "agentic" means, where it helps, where it goes
  wrong, how to supervise) — exactly the ai-explainer lane (vox-style
  middle, concept-illustrated beats, Claude bookends). No switch needed.
  [judgment]
- Read the ai-explainer SKILL.md, the prior film's package
  (free-vs-paid-when-to-pay) for house conventions, and the static QC
  checker's source to author to its actual rules (coords in safe area,
  evolving shape states per play, text excluded from shape signatures).
  [record]
- Researched the factual spine with three web searches (agentic-AI
  definition, Anthropic's "Building effective agents", indirect prompt
  injection). Grounded seven verifiable claims; left out vendor forecasts
  and adoption stats as churn-prone and unnecessary. All factual claims
  are hedged where behavior varies (B06's "might just do it"; B08's
  illustrative "forty times"). [record]
- Wrote make_sheet.py (12 beats, 7 body, 324 s) with contract assertions
  (10–16 beats, 6–10 body, 180–360 s, every beat carries beat_id /
  narration_text / estimated_duration_s / shot.type, GRAPHIC beats carry a
  show block and a <BID>_<Name> class in the manifest, B00 names the voice,
  B09 restates the three-rule framework, B10 carries the viewer prompt).
  First run passed all assertions — no authoring bugs before generation.
  [record]
- Wrote scenes.py (8 classes: B02_Agent, B03_Loop, B04_Rules, B05_Helps,
  B06_WrongPlace, B07_Compound, B08_Runs, B09_Verdict). Fixed three layout
  issues before the first QC run: (1) B02's ingredient cards animate-moved
  while their labels stayed behind — regrouped as VGroups and dropped the
  motion so labels travel with cards; (2) B05's per-step arrows were
  degenerate (nearly identical start/end points) — re-anchored from the
  goal card's bottom edge to each chip's top edge; (3) B07's third error
  bar overlapped the wreck card — shrunk and raised it. [record]
- QC gate: `python3 -m py_compile` clean on both files. Static checker:
  **8/8 clean on the first run · 0 warnings · 0 errors.** No warnings or
  errors hidden or waived. [record]
- `manim_layout_audit.py --curve-strict` could not run in this VM (no
  Manim/pangocairo installed) — deferred to Bear's Mac render pass, noted
  in CLAUDE-CODE-RENDER.md. [record]
- Wrote the 9 docs (ACTS, SHOTLIST, FACTCHECK, SOURCES, BUILD-LOG,
  CHECKS-REPORT, PROMPTS, CLAUDE-CODE-RENDER, README). [record]
- Pushed all 12 files via gh-put-file.py to
  `muse/youtube/how-to-use-ai/agents-that-do-things/` and verified each
  with a Contents API read (HTTP 200). [record]
