# Slides without the slog

A **How to AI** film (Wave 6, "Making things") for the humanitarians AI
YouTube channel (https://www.youtube.com/@humanitariansai). Companion to
`the-long-game`: that film keeps a long document from falling apart with
outline → sections → stitching; this one applies the same shape to slide
decks — outline first, then slides, then polish — referenced once by
name, never re-taught.

**The idea:** asking an AI for a whole slide deck in one prompt gets you
eighteen slides of walls of text — the AI doesn't know what matters, so
it keeps everything. Play the three moves instead: the outline (a
one-line-per-slide skeleton you read, fix, and approve before any slide
exists), one slide per prompt (each slide small enough to check), and
the polish (cut the words off the slides into the speaker notes, then
run the back-row test).

**Package:** pre-render only — script, beat sheet, Manim scenes, and docs.
No audio, no video, nothing staged for publication.

| File | What it is |
|------|------------|
| `ACTS.md` | The film's structure and promise (2 acts) |
| `SHOTLIST.md` | Scene → beat → what the viewer sees |
| `FACTCHECK.md` | Every claim checked; no invented statistics |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 13 beats, 9 drawn body beats, ~3m33s (213 s) |
| `scenes.py` | 9 Manim scene classes (show-tell isometric drawings) |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, failures, and fixes |
| `CHECKS-REPORT.md` | QC gate results (9 clean · 0 warn · 0 error) |
| `PROMPTS.md` | The prompts that shaped this film |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac |
| `README.md` | This file |

**Film identity:** persona "Liam, in for Bear" · Kokoro voice `am_onyx` ·
Teardown register · channel `claude-liam` · watermark `@NikBearBrown` ·
skill `show-tell`.

**Render prompt:** see `CLAUDE-CODE-RENDER.md` — narration with Kokoro
`am_onyx`, then `./art run` / `./art final` on Bear's Mac.
