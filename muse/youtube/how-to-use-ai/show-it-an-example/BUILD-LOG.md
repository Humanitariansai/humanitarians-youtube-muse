# BUILD-LOG.md — "Show It an Example" (film 3 of 24, How to AI)

## 2026-10-03 — pre-render package built

**Skill choice.** Kept the assigned `show-tell` skill. The film teaches one
technique with a small cast of concrete objects (prompt box, example pages,
rule stack) — exactly the skill's home ground: one drawing per beat, the voice
explains. No card passed the card test (nothing here is an interface, a
dataset, or a single word), so the film uses zero ShowTellCards. [judgment]

**Source.** Refactored `nikbearbrown/humanitarians-youtube-muse`:
`claude/claude-for-education/claude-liam-prompt-tutorial-lesson-07-few-shot-prompting`
(beat_sheet.json, README.md, description.txt, scenes.py as reference) via the
GitHub Contents API with the `custom.github` surrogate credential. Ignored
`mp3/`; downloaded no audio. The source's argument and facts are kept whole;
all narration rewritten for a general audience. [record]

**Package.** 11 beats (BIDEA, BDEFS, 7 drawn body beats B00–B06, BHTF, BOUT),
~209 s estimated (3.5 min). `make_sheet.py` generates `beat_sheet.json` and
asserts: 11 beats, 7 manim body beats with unique `BNN_`-prefixed classes,
narration/voice/engine on every beat, bookend order, "few-shot" never used
before BDEFS explains it, total in the 3–6 min band.

**Mid-build incident (no harm done).** While assembling `scenes.py` I staged
the film's scene code in `/tmp/scenes_body.py` — and a sibling film-builder
agent was using the same filename for a different film. My first assembly
pulled in their body code (a Claude-window film). Caught immediately by the
class-count check (6 classes, wrong names). Fixed by writing the body to a
uniquely named file (`_scenes_body_mine.py`, kept locally, not pushed) and
reassembling `scenes.py` = iso_kit.py paste + that body. Lesson recorded:
never use generic `/tmp` staging names when sibling builders run concurrently.
[record]

**QC.** `py_compile` clean on both files; `static_scene_check.py` 0 warnings /
0 errors on all 7 classes, run both with and without `beat_sheet.json` beside
`scenes.py`. Three layout bugs caught and fixed in pre-checker review (see
CHECKS-REPORT.md). `manim_layout_audit.py --curve-strict` deferred to Bear's
Mac (no Manim/pangocairo in this VM). [record]

**Push.** All 12 files pushed to
`Humanitariansai/humanitarians-youtube-muse` under
`muse/youtube/how-to-use-ai/show-it-an-example/`, each verified live via a
Contents API read afterwards. No MP3/MP4/WAV, no `.pyc`/`__pycache__`, no
secrets. Did not touch `muse/FRICTIONAL.md`, `muse/README.md`, `muse/QUEUE.md`.
[record]

**Open for Bear.** Render narration (Kokoro `am_onyx`) + review cut on his Mac
per CLAUDE-CODE-RENDER.md; whisper-check BIDEA's "Hallo" and the acronym-free
script as usual.
