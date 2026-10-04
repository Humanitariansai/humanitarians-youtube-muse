# Make It Interview You First

Pre-render film package for the **Humanitarians AI** YouTube channel
(https://www.youtube.com/@humanitariansai). Film #9 of the How-to-AI queue.

- **Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx`
- **Register:** Teardown · **Channel:** `claude-liam` · **Watermark:** `@NikBearBrown`
- **Skill:** show-tell (one drawn image per beat, minimal text, the voice explains)
- **Length:** 12 beats, ~3:14 (estimated; the measured Kokoro audio is the clock)
- **Audience:** smart, pragmatic general audience — not AI experts; may have typed one-line requests into an AI chat tool

## The film in one line

Before giving the AI a task, tell it **"ask me 5 questions first"** — a
trip-planning demo (plus a difficult-email second demo) shows the interview
surfacing the missing context, and the tailored answer that comes back.

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
| `beat_sheet.json` | the sheet: 12 beats with narration, shots, Remotion props, QC waivers |
| `scenes.py` | 8 Manim scene classes (`B00_AskOnce` … `B07_TheRule`) + iso kit |

## Status

Pre-render package only. `py_compile` clean; `static_scene_check` 0 warnings /
0 errors for all 8 scene classes. Audio (Kokoro `am_onyx`) and the 4K render
happen on Bear's Mac — see `CLAUDE-CODE-RENDER.md`. **Nothing staged or
published.**
