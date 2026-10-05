# BUILD-LOG.md — "Fix your photos" (slug `fix-your-photos`)

## Skill choice

Assigned skill: `show-tell`. Kept — the film is a plain explainer (one idea
per beat, voice carries the explanation, minimal labels), which is exactly the
show-tell brief. No beat passed the card test (every idea is a thing, a part,
or a flow), so the film uses zero ShowTellCards; all ten body beats are
drawings. Recorded as required.

## 2026-10-05 — build session

1. Read `show-tell/SKILL.md` end to end. Studied the companion film's package
   (`~/workspace/film-builds/how-to-ai/ai-that-sees/`, 12 files) as the
   working example and conformed to its conventions exactly (same iso_kit,
   same bookend props, same `modelLabel: "Opus 5.5"` house chrome).
2. Key design decision: the pitch says "AI cleanup of your own photos", but
   fact-grounding showed Claude does NOT edit photos itself (leaked Sonnet
   4.5 system-prompt mirrors: Claude describes, it does not edit). So the
   film frames every edit as "the AI tools in your photo app" with Google
   Photos' Magic Eraser / Enhance / Crop named as the verified example, and
   Claude appears only in the Your-Turn prompt — asked for a described
   opinion ("tell me what you would change"), which matches its verified
   see-and-describe ability from the companion film's FACTCHECK. [record,
   judgment]
3. Fact-checked the photo-app tools against Google's Photos editing page and
   four Magic Eraser guides on 2026-10-05: tap-or-circle removal, background
   reconstruction from surroundings, photobombs as the named use case,
   one-tap Enhance suggestions, Crop+Rotate, non-destructive save-as-copy,
   and visible flaws on complex detail (see FACTCHECK.md).
4. Authored `make_sheet.py` (14 beats: BIDEA, BDEFS, 10 manim body, BHTF,
   BOUT; ~216 s estimated). First run passed all its assertions — no count
   errors this time. [record]
5. Authored `scenes.py`: iso_kit pasted verbatim from
   `brutalist.art/skills/make/show-tell/templates/iso_kit.py` + local helpers
   (kraft photo card with the companion's hills motif, dark ink person
   figures, dashed terracotta eraser ring, fill patch, dim overlay, crop
   frame, magnifier, printer, document card) + 10 scene classes. Midpoint
   discipline: all motion completes in the first ~40% of each beat, fully
   opaque; `until()` holds on a settled labelled frame (every `until()` phrase
   verified verbatim-present in its beat's narration by script).
6. QC gate: `py_compile` clean on both files; `static_scene_check.py` run for
   all 10 classes — 10 clean · 0 warnings · 0 errors, first pass. No failures
   to fix; nothing concealed (see CHECKS-REPORT.md).
7. `manim_layout_audit.py --curve-strict` cannot run in this VM (no
   Manim/pangocairo) — deferred to Bear's Mac render pass per the assignment.
   Coordinates were kept inside ±6.2 × ±3.3 and type ≥ 40 px by construction.
8. Wrote docs: ACTS, SHOTLIST, FACTCHECK, SOURCES, PROMPTS ("no generation
   prompts"), BUILD-LOG, CHECKS-REPORT, CLAUDE-CODE-RENDER, README.
9. Pushed all 12 files to `muse/youtube/how-to-use-ai/fix-your-photos/` on
   Humanitariansai/humanitarians-youtube-muse via `gh-put-file.py`; verified
   every file live with a Contents API read afterwards.

Did NOT touch: FRICTIONAL.md, muse/README.md, muse/QUEUE.md (per assignment).
No MP3/MP4/WAV/.pyc/__pycache__/.DS_Store committed. No secrets or PII in any
file.
