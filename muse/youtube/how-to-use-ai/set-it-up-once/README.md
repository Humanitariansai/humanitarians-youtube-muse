# set-it-up-once

Pre-render film package for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai). Film #23 of the "How to use AI"
series. Skill: show-tell. Persona: Liam ("Liam, in for Bear"); Kokoro
`am_onyx`; Teardown register; channel `claude-liam`; watermark
`@NikBearBrown`.

**Exact title:** Set it up once
**Pitch:** Custom instructions — teach the AI your preferences a single
time, so every chat starts informed.
**Package:** 13 beats (~3m31s), 9 Manim scenes + 4 Remotion bookends, QC
clean (0 warn, 0 error). Zero ShowTellCards (all drawings).

## Files

- `ACTS.md` — three-act structure, tone, what the film is not, source facts
- `SHOTLIST.md` — scene → beat → what the viewer sees → data source
- `FACTCHECK.md` — every claim checked 2026-10-03; judgments labeled
- `make_sheet.py` — generates `beat_sheet.json`; asserts beat order, counts,
  durations, and the bookend contracts
- `beat_sheet.json` — the 13-beat sheet (generated)
- `scenes.py` — iso_kit + 9 scene classes (B00–B08)
- `SOURCES.md` — fact → source table
- `BUILD-LOG.md` — dated build steps, including the one QC failure and fix
- `CHECKS-REPORT.md` — full QC gate record
- `PROMPTS.md` — the prompts that shaped this film
- `CLAUDE-CODE-RENDER.md` — render instructions for Bear's Mac
- `README.md` — this file

Nothing is rendered or published from here; MP3/MP4/WAV files are never
committed. **Never publish without explicit instruction.**
