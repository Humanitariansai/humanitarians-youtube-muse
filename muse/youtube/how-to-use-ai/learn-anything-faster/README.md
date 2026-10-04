# Learn Anything Faster

A pre-render film package for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai).

**The film:** stop asking the AI for answers — ask it to teach you.
Three concrete moves (explain-it-simple, one-at-a-time quiz, Socratic
mode) demonstrated on one topic — how a mortgage works — plus a
copy-paste tutor prompt the viewer runs tonight on their own topic.

- Persona: Liam ("Liam, in for Bear"); Kokoro voice `am_onyx`;
  register Teardown; channel claude-liam; watermark @NikBearBrown.
- Skill: show-tell. 9 beats, ~3m20s, 5 Manim scenes + 4 Remotion
  bookends. Zero cards — every body beat is a drawing of the film's
  own cast (the house, the tutor card, the learner, question pills).
- Source: NEW — built from scratch, no mirror source. Mortgage
  mechanics checked against CFPB/Federal Reserve glossaries; Socratic
  method checked against standard references (see SOURCES.md).

## Package contents

| File | What it is |
|------|------------|
| ACTS.md | Act structure and the demo-topic rationale |
| SHOTLIST.md | Scene table: beat → what the viewer sees → data source |
| FACTCHECK.md | Claim-by-claim fact check with verdicts and sources |
| SOURCES.md | Fact → source table |
| PROMPTS.md | Prompts that shaped the film; "no generation prompts" |
| make_sheet.py | Generates `beat_sheet.json`; asserts beats and duration |
| beat_sheet.json | The sheet: 9 beats with narration lines and shot notes |
| scenes.py | 5 Manim scene classes (B00–B04), one per body beat |
| BUILD-LOG.md | Dated build steps, including failures |
| CHECKS-REPORT.md | QC gate results (static_scene_check, per class) |
| CLAUDE-CODE-RENDER.md | Render instructions for Bear's Mac |
| README.md | This file |

## Status

Pre-render package only: everything except the final MP3/MP4. Never render,
publish, upload, or stage anything for publication without Bear's explicit
instruction. No audio, video, or cache files are committed.
