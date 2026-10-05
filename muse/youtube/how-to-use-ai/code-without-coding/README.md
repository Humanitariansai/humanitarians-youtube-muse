# Code without coding

A **How to AI** film for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai).

- **Slug:** `code-without-coding`
- **Pitch:** What a non-programmer can safely build with AI coding tools — and
  the three mistakes that bite beginners.
- **Skill:** show-tell (kept; the film is a pure show-tell: one isometric
  drawing per beat, the voice explains, zero ShowTellCards).
- **Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx` ·
  **Register:** Teardown · **Channel:** claude-liam · **Watermark:** @NikBearBrown
- **Beats:** 13 (BIDEA, BDEFS, 9 drawn body beats B00–B08, BHTF, BOUT)
- **Estimated runtime:** ~248 s (≈ 4 min; measured Kokoro audio sets the final clock)
- **Source:** NEW film (no mirror-repo source). The one number (25% of Y
  Combinator's Winter 2025 batch on 95% AI-written codebases) verified
  2026-10-04: TechCrunch, Mar 2025, reporting YC's Jared Friedman and Garry
  Tan — attributed aloud and captioned "per Y Combinator".

## The argument in one paragraph

An AI coding tool turns your plain description into working code — words in,
a page out. What's safe for a non-programmer: things you can check by looking
(a page, a quiz, a tracker), and things that only touch you and your stuff.
The three mistakes: starting too big (start with one small thing), pasting
secrets (never paste what you wouldn't pin to a noticeboard), and trusting
without testing (click every button yourself). When it breaks, describe the
problem back in plain words — describe, check, repeat. The tools are good
enough that startups ship whole products on AI-written code; your one page is
well within reach.

## Files

| File | What it is |
|---|---|
| `ACTS.md` | act structure |
| `SHOTLIST.md` | shot-by-shot visual plan (incl. why no cards) |
| `FACTCHECK.md` | claim table — one attributed number, no invented statistics |
| `make_sheet.py` | generates `beat_sheet.json`; asserts 13 beats + duration band |
| `beat_sheet.json` | the sheet (generated) |
| `scenes.py` | 9 Manim scene classes (iso kit pasted at top) |
| `SOURCES.md` | sources + toolkit references |
| `BUILD-LOG.md` | decisions and build notes |
| `CHECKS-REPORT.md` | QC gate results (9/9 clean; layout audit deferred to Mac) |
| `PROMPTS.md` | no generation prompts (all visuals drawn) |
| `CLAUDE-CODE-RENDER.md` | render instructions for Bear's Mac |
| `README.md` | this file |

## Status

Pre-render package. Static QC passed (py_compile clean; `static_scene_check.py`
9/9 scenes, 0 warnings, 0 errors). `manim_layout_audit.py --curve-strict`
could not run in the build VM (no Manim/pangocairo) — deferred to the Mac
render pass. Never render, publish, or stage from this package without Bear's
explicit instruction.
