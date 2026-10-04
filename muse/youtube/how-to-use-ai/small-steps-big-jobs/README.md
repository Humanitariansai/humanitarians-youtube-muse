# Small steps, big jobs

Film 11 of 24 in the **How to AI** series for the humanitarians AI YouTube
channel (https://www.youtube.com/@humanitariansai).

**The idea:** one giant prompt ("plan my whole kitchen renovation") gets
you mush. Break the job into small steps — budget, then layout, then
materials, then timeline — each one checked, each one feeding the next,
and you get something usable. The film shows the giant-prompt failure and
the step-by-step success side by side.

**Package:** pre-render only — script, beat sheet, Manim scenes, and docs.
No audio, no video, nothing staged for publication.

| File | What it is |
|------|------------|
| `ACTS.md` | The film's structure and promise (2 acts) |
| `SHOTLIST.md` | Scene → beat → what the viewer sees |
| `FACTCHECK.md` | Every claim checked; no invented statistics |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 13 beats, 9 drawn body beats, ~3m15s (195 s) |
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
