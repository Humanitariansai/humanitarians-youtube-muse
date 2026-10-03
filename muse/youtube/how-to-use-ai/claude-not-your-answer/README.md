# Claude, Not Your Answer. — pre-render package

A show-tell film for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): your personal AI account can
train on your chats — here is the one toggle that stops it, and the rule
for what never goes in.

- **Slug:** `claude-not-your-answer`
- **Persona:** Liam ("Liam, in for Bear") · Kokoro `am_onyx` · Teardown
- **Channel:** claude-liam · watermark @NikBearBrown
- **Skill:** show-tell — one drawn illustration per beat, minimal labels,
  the voice explains
- **Beats:** 13 (BIDEA, BDEFS, B00–B08, BHTF, BOUT) · est. 186.4 s
- **Scenes:** 9 Manim scene classes in `scenes.py`, static-QC clean

## Files

| File | What it is |
|---|---|
| `ACTS.md` | film shape, redo notes, tone |
| `SHOTLIST.md` | one drawing per beat + the card-test verdicts |
| `FACTCHECK.md` | 12 claims, verdicts, sources |
| `SOURCES.md` | build source + primary sources |
| `make_sheet.py` | generates `beat_sheet.json` (asserts beats, classes, duration) |
| `beat_sheet.json` | the sheet: narration, shots, bookends |
| `scenes.py` | 9 Manim scenes (iso_kit pasted at top) |
| `BUILD-LOG.md` | build decisions and timeline |
| `CHECKS-REPORT.md` | QC gate results |
| `PROMPTS.md` | no generation prompts |
| `CLAUDE-CODE-RENDER.md` | Mac render instructions for Bear |
| `README.md` | this file |

Pre-render package only: no audio, no video, nothing staged or published.
