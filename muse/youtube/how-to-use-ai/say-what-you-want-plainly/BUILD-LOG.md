# BUILD-LOG.md — Say what you want, plainly

Dated build steps, including failures and fixes. Skill choice: **show-tell**
(the assigned skill). I read the full SKILL.md before writing; the film is
a single behavioral habit for non-experts — "one image per beat, the voice
explains" — and every beat passed the drawing side of the card test, so no
skill switch and zero cards. [judgment]

## 2026-10-03

- Read `show-tell/SKILL.md`, `templates/iso_kit.py`, and
  `reference/example-make_sheet.py` end to end. [record]
- Fetched the REFACTOR source from the mirror repo
  (`nikbearbrown/humanitarians-youtube-muse`,
  `claude/claude-for-education/claude-liam-prompt-tutorial-lesson-02-clear-and-direct/`)
  via the GitHub Contents API with the surrogate credential flow: 10-beat
  `beat_sheet.json` (Kore persona, course audience) plus `README.md`. No
  PEDAGOGY.md in the source folder; ignored the `mp3/` folder, downloaded
  no audio. [record]
- Rewrote the source's argument for the general audience: "degree of
  freedom" → "a guess it has to make"; "required components" →
  "must-haves / what must be in it"; the golden rule kept as the
  new-employee test. [judgment]
- Wrote `make_sheet.py` (11 beats / 7 manim at first): bookends via the
  `remotion()` helper, body beats via `manim_beat()` with the sparse
  waiver, assertions on beat count / manim count / voice / class names /
  no-audio-references / total duration. First run: 11 beats, 176.8 s.
  [record]
- Added a real content beat the film needed (B02 "the default is not
  wrong, just not yours" — why the AI's most-common guess fails *you*
  specifically), renumbered to 12 beats / 8 manim, 195.2 s (~3m15s). This
  was a missing step, not padding: the film previously never explained
  why the default guess misses. [judgment]
- Wrote `scenes_body.py` (8 scene classes), concatenated after the kit
  template into `scenes.py`. `py_compile` clean on both files. [record]
- QC run 1: 7/8 clean; `B04_FourQuestions` failed "shapes never change".
  Diagnosis: the stub only counts membership-changing animations, and
  `RoundedRectangle` was not tracked as a shape at all. [record]
- Fix attempt 1 (wrong): swapped `RoundedRectangle` → `Rectangle` in the
  `_chip` helper. Still failed — the real cause was `chip.animate.shift()`,
  which the stub treats as move-only (no membership change), so chips never
  entered `scene.mobjects`. [judgment]
- Fix attempt 2 (correct): replaced every `.animate.shift()` drop/rise with
  `FadeIn(x, shift=...)` (B00, B03, B04, B05 chips, B05 page). This is also
  the correct real-Manim pattern — the animate-only plays would have left
  those objects un-added in a real render too. [judgment]
- Also attached the kit's pacing helpers as `Scene.until` / `Scene.finish`
  in `scenes_body.py` — the kit defines them as plain functions and the
  first QC run failed with `no attribute 'until'`. [record]
- QC run 2 (final): 8/8 clean · 0 warnings · 0 errors, both with
  `beat_sheet.json` beside `scenes.py` and from a scratch folder holding
  only `scenes.py` (what Gate A sees). See CHECKS-REPORT.md. [record]
- Wrote the remaining docs (ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS,
  CLAUDE-CODE-RENDER, README). [record]
- Pushed all 12 files to
  `Humanitariansai/humanitarians-youtube-muse`,
  `muse/youtube/how-to-use-ai/say-what-you-want-plainly/`, via
  `gh-put-file.py`; verified each live with a Contents API read
  afterwards. [record]

Not done by design: no Kokoro audio generated, no Manim render, no
`manim_layout_audit.py --curve-strict` (no Manim/pangocairo in this VM —
deferred to Bear's Mac render pass), nothing published. [record]
