# BUILD-LOG.md — Keep instructions and data apart

## Skill choice
Assigned skill `ai-explainer`; kept it. This film is a concept walkthrough
(one technique, one mechanism, one worked illustration) — the ai-explainer
lane. No switch: nothing about the film wants the cli build loop
(claude-cli), a profile subject, a skill teardown, or an audit verdict.

## Decisions
- Source resolution: the assigned base-name path
  `claude/claude-for-education/prompt-tutorial-lesson-04-separating-data`
  404s on the Contents API. Listed the parent; the closest
  `*separating-data*` match is
  `claude/claude-for-education/claude-liam-prompt-tutorial-lesson-04-separating-data`
  (full lesson: beat sheet, README, description, scenes). Used as the
  refactor source and recorded in `beat_sheet.json` metadata.
  [judgment]
- General-audience rewrite: the source was written for a course audience
  ("PROMPT ENGINEERING · ANTHROPIC", XML-tag mechanics). The film keeps the
  argument but replaces the demo with a concrete visual a non-expert follows:
  a pasted email whose buried line orders Claude to forward the email.
  Technical terms ("attack surface", "prompt injection", "XML tags") are
  defined in plain language on first use. [judgment]
- Structure: 11 beats, 3 acts (mix-up → fence → honesty/takeaway),
  273.8s total. Bookends per ai-explainer law: cold-open ask →
  hesitant-writer BLUF → body → verdict → handoff → title-restate outro.
- Greeting: "Hej, Liam" (Swedish, world-language rotation; one word fits
  the Liam word budget). IN-FOR-BEAR LAW: B00 narration says "this is Liam,
  in for Bear" in its first breath; B10 signs off "Liam, in for Bear."
- The B06 "mother tongue" line is register color, not a training-data
  claim; FACTCHECK.md marks it QUALIFY.
- B07 deliberately undercuts the fix ("a fence, not a vault") — the
  falsifiability/honesty beat, grounded in OWASP LLM01.

## Failures and fixes
- `static_scene_check.py` initial run: all 7 classes errored —
  `NameError: name 'BOLD' is not defined` (the QC stub doesn't define
  `BOLD`, though real Manim does). Fix: try/except shim defining
  `BOLD = "BOLD"` when absent. [record]
- `B08_Verdict` failed the distinctness check (1 distinct shape-state
  across 5 frames — the card never changes; text is excluded from shape
  states). Fix: added terracotta bullet Dots that FadeIn with each verdict
  line, giving distinct shape states per frame. [record]
- B03 originally used `DashedRectangle`, which exists neither in real Manim
  nor the stub; replaced with `Rectangle` before the first checker run.
  [record]
- `manim_layout_audit.py --curve-strict` cannot run in this VM (no
  Manim/pangocairo); deferred to Bear's Mac render pass per the task spec
  and noted in CLAUDE-CODE-RENDER.md. [record]
