# How to Use Claude

Pre-render film package for the **Humanitarians AI** YouTube channel
(https://www.youtube.com/@humanitariansai).

- **Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx`
- **Register:** Teardown · **Channel:** `claude-liam` · **Watermark:** `@NikBearBrown`
- **Skill:** show-tell (one drawn image per beat, minimal text, the voice explains)
- **Length:** 13 beats, ~3:16 (estimated; the measured Kokoro audio is the clock)
- **Audience:** smart, pragmatic general audience — may never have used an AI chat tool

## The film in one line

Claude's output quality scales with **context**, not prompt templates: feed it
your project, your constraints and an example (best done once, in a Project),
use it for artifacts / analysis / rewriting, and check important facts.

## Files (12)

| file | what it is |
|---|---|
| `README.md` | this file |
| `ACTS.md` | act structure and the show-tell spine |
| `SHOTLIST.md` | one row per beat: motion, labels, why no card, timing notes |
| `FACTCHECK.md` | claim table with verdicts and sources |
| `SOURCES.md` | source doc + fact-check URLs + provenance |
| `PROMPTS.md` | "no generation prompts" (Gate F) |
| `BUILD-LOG.md` | decisions, failures, fixes |
| `CHECKS-REPORT.md` | QC gate results |
| `CLAUDE-CODE-RENDER.md` | Mac render instructions for Bear (Manim + Kokoro) |
| `make_sheet.py` | generates `beat_sheet.json`; asserts beats, order, duration band, bookend contracts |
| `beat_sheet.json` | the sheet: 13 beats with narration, shots, Remotion props, QC waivers |
| `scenes.py` | 9 Manim scene classes (`B00_ChatWindow` … `B08_CheckIt`) + iso kit |

## Status

Pre-render package only. `py_compile` clean; `static_scene_check` 0 warnings /
0 errors for all 9 scene classes. Audio (Kokoro `am_onyx`) and the 4K render
happen on Bear's Mac — see `CLAUDE-CODE-RENDER.md`. **Nothing staged or
published.**
