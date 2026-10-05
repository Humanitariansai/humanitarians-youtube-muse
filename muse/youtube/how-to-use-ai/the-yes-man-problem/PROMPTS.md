# PROMPTS.md — The yes-man problem.

Prompts Muse was given (by the parent orchestrator) that shaped this
film, in order.

1. The film-builder assignment (2026-10-04): build ONE pre-render film
   package for the humanitarians AI YouTube channel — slug
   `the-yes-man-problem`, working title "The yes-man problem", pitch
   "Sycophancy: when AI agrees with you too much, and how to ask for
   pushback. Companion to the existing film `when-its-confidently-
   wrong`", assigned skill deep-explainer (switch allowed, recorded).
2. The film identity lock: persona Liam ("Liam, in for Bear"); Kokoro
   voice `am_onyx`; Teardown register; channel `claude-liam`;
   watermark `@NikBearBrown`. Never render, publish, upload, or stage
   anything for publication. Pre-render package only.
3. The audience rule: smart, pragmatic general audience, NOT AI experts
   — explain every technical term (sycophancy, RLHF, etc.) in plain
   language, by showing wherever possible; roughly 3–6 minutes; never
   quote pricing tiers; ground the sycophancy claims in real research —
   published papers found and cited, no invented findings.
4. The workflow: 12 files in
   `~/workspace/film-builds/how-to-ai/the-yes-man-problem/`;
   `make_sheet.py` generates `beat_sheet.json` and asserts beat counts
   and duration; every beat carries `beat_id`, `narration_text`,
   `estimated_duration_s`, and a `shot` object (`GRAPHIC` +
   `shot.manim.class` for Manim beats; `REMOTION` +
   `shot.remotion.pattern` for bookend beats); `scenes.py` with one
   Manim scene class per visual beat named `<BID>_<Name>(Scene)`;
   `CLAUDE-CODE-RENDER.md` notes the deferred `manim_layout_audit`;
   mandatory QC gate (`py_compile` + `static_scene_check.py` per class,
   0 warnings / 0 errors); push all 12 files via `gh-put-file.py` and
   verify each with a Contents API read; never commit MP3/MP4/WAV/
   `.pyc`/`__pycache__`/`.DS_Store`; do not touch
   `muse/FRICTIONAL.md`, `muse/README.md`, or `muse/QUEUE.md` —
   coordinator's; return a seven-field FRICTIONAL.md entry after
   reading the existing file's format.

No generation prompts were used in this build — all narration and all
visuals are hand-authored. (The ai-explainer card test was run: no beat
passed it; the film uses zero cards, all drawings.)
