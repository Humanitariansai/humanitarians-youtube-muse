# Make It Check Its Own Work. — pre-render package

A show-tell film for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): after the AI answers, ask it to
attack its own answer — "what's wrong with this?", "what did you assume?",
"what's the strongest objection?" — shown in a worked demo where the
critique pass catches a real flaw, with an honest limit: fewer errors,
never zero.

- **Slug:** `make-it-check-its-own-work`
- **Persona:** Liam ("Liam, in for Bear") · Kokoro `am_onyx` · Teardown
- **Channel:** claude-liam · watermark @NikBearBrown
- **Skill:** show-tell — one drawing per beat, minimal labels, the voice
  explains (switched from the assigned ai-explainer for series consistency;
  see BUILD-LOG.md)
- **Beats:** 13 (BIDEA, BDEFS, B00–B08, BHTF, BOUT) · est. 190.4 s
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
