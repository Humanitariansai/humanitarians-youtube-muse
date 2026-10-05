# Give it a voice — pre-render package

A show-tell film for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): your slides are finished,
and they are silent — so let AI do the talking. Suno's Speech beta
(launched Oct 1, 2026) reads your script and mixes original background
music under it in one track; Google Vids already has AI voiceovers
built into the editor. The voice reads exactly what you wrote, typos
included — so the one real skill is writing a script worth reading
aloud.

- **Slug:** `give-it-a-voice`
- **Series:** How to AI · Wave 6 "Making things" · film #36
- **Persona:** Liam ("Liam, in for Bear") · Kokoro `am_onyx` · Teardown
- **Channel:** claude-liam · watermark @NikBearBrown
- **Skill:** show-tell — one drawing per beat, minimal labels, the voice
  explains
- **Beats:** 11 (BIDEA, BDEFS, B00–B06, BHTF, BOUT) · est. 181.6 s
- **Scenes:** 7 Manim scene classes in `scenes.py`, static-QC clean

## Files

| File | What it is |
|---|---|
| `ACTS.md` | film shape, redo notes, tone |
| `SHOTLIST.md` | one drawing per beat + the card-test verdicts |
| `FACTCHECK.md` | 17 claims, verdicts, sources — no invented statistics |
| `SOURCES.md` | build sources (Suno launch coverage, Google Workspace Updates) |
| `make_sheet.py` | generates `beat_sheet.json` (asserts beats, classes, duration) |
| `beat_sheet.json` | the sheet: narration, shots, bookends |
| `scenes.py` | 7 Manim scenes (iso_kit pasted at top) |
| `BUILD-LOG.md` | build decisions and timeline |
| `CHECKS-REPORT.md` | QC gate results |
| `PROMPTS.md` | no generation prompts |
| `CLAUDE-CODE-RENDER.md` | Mac render instructions for Bear |
| `README.md` | this file |

Pre-render package only: no audio, no video, nothing staged or published.
