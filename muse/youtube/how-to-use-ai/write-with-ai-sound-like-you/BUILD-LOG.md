# BUILD-LOG.md — "Write with AI, Still Sound Like You"

## Skill choice
**show-tell** (as assigned). The film is a behavioral how-to: four fixes, one demo,
each a thing/part/flow best shown as a drawing with the voice explaining. The card
test ran per body beat — no beat is an interface, a set of numbers, or a single word —
so the film uses **zero cards, all drawings**. No skill switch; nothing in the film
wanted another skill's lane.

## Build record
- 2026-10-03: wrote `make_sheet.py` (11 beats: 4 bookends + 7 body; assertions for
  beat count/order, class-name prefixes, voice lock, sparse waivers, trigger-word
  verbatim rule, 17-char term cap, BOUT 1.0 s tail, total 180–360 s). First run:
  11 beats, 7 body, est 224 s (~3.7 min). All assertions passed first run.
- Wrote `scenes.py` = show-tell `iso_kit.py` pasted at top (not imported, per Gate A)
  + 7 body scene classes (`B00_RobotDraft` … `B06_TheEmail`), literal
  `class BNN_Name(Scene):` form, `until(self, …)` / `finish(self)` module-level pacing
  calls reading `beat_sheet.json`.
- QC gate: `python3 -m py_compile` clean on `make_sheet.py` and `scenes.py`.
  `static_scene_check.py` run per class:
  - Run 1: 7/7 classes errored — `construct() raised AttributeError:
    'B00_RobotDraft' object has no attribute 'until'`. Cause: I called
    `self.until(...)` / `self.finish()`; the kit defines them as module-level
    functions and SKILL.md documents the call form `until(self, "phrase")`.
    Fixed with sed (`self.until(` → `until(self, `, `self.finish()` → `finish(self)`),
    regenerated `scenes.py` from the kit + class file. [record]
  - Run 2: 7/7 clean — 0 warnings, 0 errors. [record]
- `manim_layout_audit.py --curve-strict` **not run**: this VM has no Manim/pangocairo.
  Deferred to Bear's Mac render pass (noted in CLAUDE-CODE-RENDER.md). [record]
- Docs written: ACTS, SHOTLIST, FACTCHECK (10 claims; no statistics by design),
  SOURCES (original script, no external source), PROMPTS ("no generation prompts"),
  CHECKS-REPORT, CLAUDE-CODE-RENDER, README.
- Pushed all 12 files to
  `Humanitariansai/humanitarians-youtube-muse:muse/youtube/how-to-use-ai/write-with-ai-sound-like-you/`
  via `gh-put-file.py`; every file verified afterwards with a Contents API read
  (HTTP 200, byte-identical). [record]
- Did NOT touch `muse/README.md`, `muse/QUEUE.md`, `muse/FRICTIONAL.md` (per task).
  Nothing rendered, published, uploaded, or staged. No MP3/MP4/WAV/`.pyc` committed.

## Judgments
- Kept B03's banned-words beat gentle ("None of them are wrong. They are just the
  uniform.") — the film teaches voice, not AI-detection, and naming the words as
  proof of AI authorship would be a claim the film can't stand on. [judgment]
- No statistics anywhere: the film's claims are behavioral ("most people…", "it is
  easier to…"), which keeps FACTCHECK honest without invented numbers. [judgment]
- B06's demo emails are staged illustrations, flagged as such in FACTCHECK (#9). [judgment]
