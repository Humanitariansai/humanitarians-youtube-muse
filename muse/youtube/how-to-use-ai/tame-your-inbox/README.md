# README.md — Tame your inbox

Pre-render film package for the **Humanitarians AI** YouTube channel
(https://www.youtube.com/@humanitariansai).

- **Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx`
- **Register:** Teardown · **Channel:** `claude-liam` · **Watermark:** `@NikBearBrown`
- **Skill:** show-tell (one drawn image per beat, minimal text, the voice explains)
- **Length:** 10 beats, ~3:10 (estimated; the measured Kokoro audio is the clock)
- **Audience:** smart, pragmatic general audience — not AI experts; every term explained

## The film in one line

Use AI as your email first-pass — triage, summarize, draft replies — and
keep two rules unbroken: never let it auto-send, never let it auto-delete.
Companion to the `talk-to-your-tools` film.

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
| `make_sheet.py` | generates `beat_sheet.json`; asserts beats, order, duration band, bookend contracts, voice codes |
| `beat_sheet.json` | the sheet: 10 beats with narration, shots, Remotion props, QC waivers |
| `scenes.py` | 6 Manim scene classes (`B00_ThePile` … `B05_NeverAutoDelete`) + iso kit |

## Status

Pre-render package only. `py_compile` clean; `static_scene_check` 0 warnings /
0 errors for all 6 scene classes. Audio (Kokoro `am_onyx`) and the 4K render
happen on Bear's Mac — see `CLAUDE-CODE-RENDER.md`. **Nothing staged or
published.**
