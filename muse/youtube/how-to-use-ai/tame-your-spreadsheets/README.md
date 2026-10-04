# Tame Your Spreadsheets

Pre-render film package — film **#15 of 24** in the "How to AI" series for
the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai).

- **Slug:** `tame-your-spreadsheets`
- **Skill:** `show-tell` (assigned; kept — one drawing per beat, the voice
  explains)
- **Beats:** 11 (2 bookends in, 7 Manim body scenes, Your Turn, outro)
- **Runtime:** ~303 s estimated (~5:03; measured audio sets the master clock)
- **Persona / voice:** Liam ("Liam, in for Bear") · Kokoro `am_onyx` ·
  Teardown register · channel `claude-liam` · watermark `@NikBearBrown`

## The film

Most people fear spreadsheets. The AI is a patient spreadsheet coach. Three
moves, one relatable example (Lena's fictional bake shop sales list):
1. "Write me the formula that…" — describe it in plain English, the AI
   writes `=SUM(B2:B31)` and explains each part.
2. Paste messy data, ask it to clean and standardize it.
3. "What's interesting in this data?" — simple analysis, no pivot tables.

Standing warning throughout: sanity-check every formula on a small sample —
the AI can be confidently wrong about cell references. The AI proposes; you
decide.

## Files

| File | What it is |
|---|---|
| `ACTS.md` | act structure and through-line |
| `SHOTLIST.md` | one row per beat; card-test verdicts (0 card beats) |
| `FACTCHECK.md` | real fact-check; no invented statistics; fictional data labeled |
| `make_sheet.py` | generates `beat_sheet.json`; asserts 11 beats, 7 manim, 180–390 s |
| `beat_sheet.json` | the sheet: narration, shots, pacing (estimates; audio pending) |
| `scenes.py` | 7 Manim scene classes (iso kit pasted at top) |
| `SOURCES.md` | refactor source + provenance |
| `BUILD-LOG.md` | choices, QC, push record |
| `CHECKS-REPORT.md` | QC gate detail: 7 clean · 0 warn · 0 error |
| `PROMPTS.md` | no generation prompts |
| `CLAUDE-CODE-RENDER.md` | Mac render instructions (audio + gates + master) |
| `README.md` | this file |

Status: **pre-render complete, unrendered.** Next: Bear renders narration
(Kokoro `am_onyx`) and the review cut on his Mac per CLAUDE-CODE-RENDER.md.
Never publish without Bear's explicit instruction.
