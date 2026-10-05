# Captions That Write Themselves

A pre-render film package for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai).

**The film:** subtitles and captions for your own videos, generated in
a pass — accessibility and reach without the typing. A practical
four-step walkthrough for a normal person with phone-shot video (open a
captioning tool, press the button, check names and odd words, choose
burned-in or a caption file), plus a copy-paste prompt that hands the
AI your caption draft for a second look.

- Persona: Liam ("Liam, in for Bear"); Kokoro voice `am_onyx`;
  register Teardown; channel claude-liam; watermark @NikBearBrown.
- Skill: show-tell. 12 beats, ~3m34s, 8 Manim scenes + 4 Remotion
  bookends. Zero cards — every body beat is a drawing of the film's
  own cast (the phone video, caption lines, the dark AI block, the
  captioning tool, check stamps).
- Source: NEW — built from scratch, no mirror source. The two quoted
  numbers (92% of mobile viewers watch with the sound off; 430 million
  with disabling hearing loss) are verified and attributed aloud and
  on screen (see SOURCES.md). No pricing tiers quoted.

## Package contents

| File | What it is |
|------|------------|
| ACTS.md | Act structure and the four-step walkthrough rationale |
| SHOTLIST.md | Scene table: beat → what the viewer sees → data source |
| FACTCHECK.md | Claim-by-claim fact check with verdicts and sources |
| SOURCES.md | Fact → source table |
| PROMPTS.md | Prompts that shaped the film; "no generation prompts" |
| make_sheet.py | Generates `beat_sheet.json`; asserts beats and duration |
| beat_sheet.json | The sheet: 12 beats with narration lines and shot notes |
| scenes.py | 8 Manim scene classes (B00–B07), one per body beat |
| BUILD-LOG.md | Dated build steps, including failures |
| CHECKS-REPORT.md | QC gate results (static_scene_check, per class) |
| CLAUDE-CODE-RENDER.md | Render instructions for Bear's Mac |
| README.md | This file |

## Status

Pre-render package only: everything except the final MP3/MP4. Never render,
publish, upload, or stage anything for publication without Bear's explicit
instruction. No audio, video, or cache files are committed.
