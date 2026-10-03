# How to outsource everything to AI & get dumb

Pre-render film package for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai). Everything except the final MP3/MP4.

- **Slug:** `how-to-rot-your-brain-with-ai`
- **Skill:** show-tell (one isometric drawing per beat, Liam's voice explains)
- **Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx` · **Register:** Teardown
- **Channel:** `claude-liam` · **Watermark:** `@NikBearBrown`
- **Beats:** 14 (BIDEA, BDEFS, B00–B09, BHTF, BOUT) · **Estimated runtime:** ~239 s
- **Audience:** smart general audience, not necessarily AI experts — every term explained.

## The film in one breath

Most people paste a problem into AI and hope it understands — like following GPS until
you can't navigate your own city. The rule: outsource *work*, never *understanding*.
The five-step method (constraints → rough draft → paste both → three versions →
pick and edit) keeps the AI working *inside* your thinking. Evidence: the UCL 2017
satnav study and MIT's 2025 "Your Brain on ChatGPT" preprint, both attributed on screen.

## Files (12)

| File | What it is |
|---|---|
| `ACTS.md` | act structure |
| `SHOTLIST.md` | per-beat shots, labels, and the card-test column |
| `FACTCHECK.md` | claim table (PASS / QUALIFY / EXEMPT) |
| `make_sheet.py` | generates `beat_sheet.json`; asserts beat counts + total duration |
| `beat_sheet.json` | the sheet (generated — do not hand-edit after audio) |
| `scenes.py` | 10 Manim scene classes, one per visual beat (iso kit pasted at top) |
| `SOURCES.md` | source beat sheet, studies, toolkit, rights |
| `BUILD-LOG.md` | decisions taken while building |
| `CHECKS-REPORT.md` | QC gate record |
| `PROMPTS.md` | "no generation prompts" |
| `CLAUDE-CODE-RENDER.md` | how Bear renders this locally on his Mac |
| `README.md` | this file |

## Status

Pre-render package, QC'd 2026-10-03: py_compile clean; static scene check 10/10 clean,
0 warnings, 0 errors. Not rendered, not published — render via CLAUDE-CODE-RENDER.md.
