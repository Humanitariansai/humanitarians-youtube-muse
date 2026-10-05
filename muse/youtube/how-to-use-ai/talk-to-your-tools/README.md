# README.md — Talk to your tools

Pre-render film package for the **Humanitarians AI** YouTube channel
(https://www.youtube.com/@humanitariansai).

- **Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx`
- **Register:** Teardown · **Channel:** `claude-liam` · **Watermark:** `@NikBearBrown`
- **Skill:** show-tell (one drawn image per beat, minimal text, the voice explains)
  — switched from the assigned cc-explainer; reasoning in BUILD-LOG.md
- **Length:** 13 beats, ~4:03 (estimated; the measured Kokoro audio is the clock)
- **Audience:** smart, pragmatic general audience — not AI experts; every term explained

## The film in one line

A connector is a plug between Claude and one of your apps — grant it like a
key, start read-only, and keep the send button yours. Three automations
worth setting up (morning brief, inbox triage, meeting prep) and three
warnings (supervised sending, least privilege, strangers' invites).
Companion to the `meetings-into-notes` film.

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
| `scenes.py` | 9 Manim scene classes (`B00_TheGap` … `B08_StrangerInvite`) + iso kit |

## Status

Pre-render package only. `py_compile` clean; `static_scene_check` 0 warnings /
0 errors for all 9 scene classes. Audio (Kokoro `am_onyx`) and the 4K render
happen on Bear's Mac — see `CLAUDE-CODE-RENDER.md`. **Nothing staged or
published.**
