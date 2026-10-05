# The long game

A **How to AI** film for the humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai). Companion to film 11,
"Small steps, big jobs": that film breaks a big job into steps; this one
keeps a long document from falling apart.

**The idea:** asking an AI to write a whole long document in one prompt
gets you twenty pages that fall apart on reading — repeats,
contradictions, wandering tone. Play the long game instead: outline
first (and approve the outline before any prose), write one section at a
time against the outline, then stitch the sections into one document.

**Package:** pre-render only — script, beat sheet, Manim scenes, and docs.
No audio, no video, nothing staged for publication.

| File | What it is |
|------|------------|
| `ACTS.md` | The film's structure and promise (2 acts) |
| `SHOTLIST.md` | Scene → beat → what the viewer sees |
| `FACTCHECK.md` | Every claim checked; no invented statistics |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 13 beats, 9 drawn body beats, ~3m22s (202 s) |
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
