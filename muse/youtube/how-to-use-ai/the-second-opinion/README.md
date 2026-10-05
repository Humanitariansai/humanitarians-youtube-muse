# The Second Opinion — pre-render package

A show-tell film for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): for a big decision, never stop
at the first answer — get a second opinion. Ask a second AI, or make one AI
argue against itself: steel-manning, the strongest version of the other
side, stated fairly. Shown in a worked demo (the night-shift job) with an
honest limit: a second opinion widens the view; it is not the truth.
Companion to `make-it-check-its-own-work`.

- **Slug:** `the-second-opinion`
- **Persona:** Liam ("Liam, in for Bear") · Kokoro `am_onyx` · Teardown
- **Channel:** claude-liam · watermark @NikBearBrown
- **Skill:** show-tell — one drawing per beat, minimal labels, the voice
  explains (switched from the assigned ai-explainer for series consistency;
  see BUILD-LOG.md)
- **Beats:** 13 (BIDEA, BDEFS, B00–B08, BHTF, BOUT) · est. 238.4 s
- **Scenes:** 9 Manim scene classes in `scenes.py`, static-QC clean

## Files

| File | What it is |
|---|---|
| `ACTS.md` | film shape, redo notes, tone |
| `SHOTLIST.md` | one drawing per beat + the card-test verdicts |
| `FACTCHECK.md` | 8 claims, verdicts, sources — no invented statistics |
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
