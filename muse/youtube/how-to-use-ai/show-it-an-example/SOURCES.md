# SOURCES.md — "Show It an Example"

## Primary source (refactored, read-only)
- `nikbearbrown/humanitarians-youtube-muse`:
  `claude/claude-for-education/claude-liam-prompt-tutorial-lesson-07-few-shot-prompting/`
  — `beat_sheet.json` (narration + argument), `README.md`, `description.txt`,
  `scenes.py` (reference only). Read via the GitHub Contents API, 2026-10-03.
  The `mp3/` folder was ignored; no audio was downloaded.

## Upstream origin of the source's argument
- Anthropic Prompt Engineering Interactive Tutorial — Lesson 07: Few-Shot
  Prompting ("Implicit Style Encoding via Examples"), as credited in the
  source folder's metadata (`"source": "Anthropic Prompt Engineering
  Interactive Tutorial — Lesson 07: Few-Shot Prompting"`).

## What was kept vs. rewritten
- Kept: the full argument (examples as input-output pairs; 3–5 usually enough;
  five encoded specs; quality > count; contamination; the three selection
  rules) and every fact above.
- Rewritten: all narration, for a smart pragmatic general audience (not AI
  experts); every technical term explained in plain words on first use;
  "distribution" → "the thing you're about to ask for", "register" → "tone",
  "target input" → "your new note".

## Toolkit
- Skill: `show-tell` (`~/workspace/brutalist.art/skills/make/show-tell/SKILL.md`);
  drawing kit `templates/iso_kit.py` pasted at the top of `scenes.py`;
  QC: `runtime/qc/static_scene_check.py`.
