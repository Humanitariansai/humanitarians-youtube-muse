# BUILD-LOG.md — "AI that sees" (slug `ai-that-sees`)

## Skill choice

Assigned skill: `show-tell`. Kept — the film is a plain explainer (one idea
per beat, voice carries the explanation, minimal labels), which is exactly the
show-tell brief. No beat passed the card test (every idea is a thing, a part,
or a flow), so the film uses zero ShowTellCards; all twelve body beats are
drawings. Recorded as required.

## 2026-10-04 — build session

1. Read `show-tell/SKILL.md` end to end. Studied the companion film's package
   (`~/workspace/film-builds/how-to-ai/just-talk-to-it/`, 12 files) as the
   working example and conformed to its conventions exactly.
2. Checked `muse/QUEUE.md` and `muse/README.md` in the write repo via the
   GitHub Contents API: all 24 How-to-AI films are Done; `ai-that-sees` is not
   in the queue. Treated it as an extra film (companion to #18 "Just talk to
   it") and wrote that into the beat sheet's `series_note` instead of
   inventing a series number. [record]
3. Fact-checked image-attachment support against two mirrored Anthropic
   developer docs (verified 2026-10-04): attachment button + drag-and-drop for
   images, "Claude sees attached photos directly as part of your message",
   screenshots-of-bugs named as an attach use case. The six use cases and
   three photo rules are original craft guidance (see FACTCHECK.md).
4. Authored `make_sheet.py` (16 beats: BIDEA, BDEFS, 12 manim body, BHTF,
   BOUT; ~247 s estimated). First run passed all its assertions — no count
   errors this time. [record]
5. Authored `scenes.py`: iso_kit pasted verbatim from
   `brutalist.art/skills/make/show-tell/templates/iso_kit.py` + local helpers
   (the AI eye, kraft photo card with hills/leaf/receipt motifs, plus attach
   button, terracotta scan line, chat window, answer page, error dialog, form,
   ID card, scribbles, crop frame) + 12 scene classes. Midpoint discipline:
   all motion completes in the first ~40% of each beat, fully opaque;
   `until()` holds on a settled labelled frame (every `until()` phrase
   verified verbatim-present in its beat's narration by script).
6. QC gate: `py_compile` clean on both files; `static_scene_check.py` run for
   all 12 classes — 12 clean · 0 warnings · 0 errors, first pass. No failures
   to fix; nothing concealed (see CHECKS-REPORT.md).
7. `manim_layout_audit.py --curve-strict` cannot run in this VM (no
   Manim/pangocairo) — deferred to Bear's Mac render pass per the assignment.
   Coordinates were kept inside ±6.2 × ±3.3 and type ≥ 40 px by construction.
8. Wrote docs: ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS ("no generation
   prompts"), BUILD-LOG, CHECKS-REPORT, CLAUDE-CODE-RENDER, README.
9. Pushed all 12 files to `muse/youtube/how-to-use-ai/ai-that-sees/` on
   Humanitariansai/humanitarians-youtube-muse via `gh-put-file.py`; verified
   every file live with a Contents API read afterwards.

Did NOT touch: FRICTIONAL.md, muse/README.md, muse/QUEUE.md (per assignment).
No MP3/MP4/WAV/.pyc/__pycache__/.DS_Store committed. No secrets or PII in any
file.
