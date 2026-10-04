# PROMPTS.md — When it's confidently wrong.

Prompts Muse was given (by the parent orchestrator) that shaped this
film, in order.

1. The film-builder assignment (2026-10-03): build ONE pre-render film
   package for the humanitarians AI YouTube channel — film #12 of 24,
   slug `when-its-confidently-wrong`, working title "When it's
   confidently wrong", pitch "The recovery playbook: what to do when the
   AI insists", source NEW (build from scratch), suggested skill
   deep-explainer (switch allowed, recorded).
2. The film identity lock: persona Liam ("Liam, in for Bear"); Kokoro
   voice `am_onyx`; Teardown register; channel `claude-liam`;
   watermark `@NikBearBrown`. Never render, publish, upload, or stage
   anything for publication. Pre-render package only.
3. The audience rule: smart, pragmatic general audience, NOT AI experts
   — every technical term explained in plain language, by showing
   wherever possible; roughly 3–6 minutes; the playbook (restart / ask
   for sources and check one / narrow until cornered / verify
   elsewhere); explain WHY it doubles down plainly (predicts plausible
   text; "confidence" is fluency, not knowledge) without getting overly
   technical.
4. The workflow: 12 files in
   `~/workspace/film-builds/how-to-ai/when-its-confidently-wrong/`;
   `make_sheet.py` generates `beat_sheet.json` and asserts beat counts
   and duration; `scenes.py` with one Manim scene class per visual beat;
   mandatory QC gate (`py_compile` + `static_scene_check.py` per class,
   0 warnings / 0 errors); push all 12 files via `gh-put-file.py` and
   verify each with a Contents API read; never commit MP3/MP4/WAV/
   `.pyc`/`__pycache__`/`.DS_Store`; do not touch other films, logs, or
   indexes.

No generation prompts were used in this build — all narration and all
visuals are hand-authored. (The ai-explainer card test was run: no beat
passed it; the film uses zero cards, all drawings.)
