# Your Language Coach

A pre-render film package for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai).

**The film:** conversation practice in any language with infinite
patience and instant corrections. Four concrete moves (just start
talking; stumble freely, the coach waits; instant corrections with the
rule in plain English; roleplay real situations + turn the level dials)
demonstrated on one demo language — French — plus a copy-paste coach
prompt the viewer runs tonight in their own language. Companion to
`learn-anything-faster` (the tutor film): referenced in B06, never
re-taught.

- Persona: Liam ("Liam, in for Bear"); Kokoro voice `am_onyx`;
  register Teardown; channel claude-liam; watermark @NikBearBrown.
- Skill: show-tell. 11 beats, ~3m44s, 7 Manim scenes + 4 Remotion
  bookends. Zero cards — every body beat is a drawing of the film's
  own cast (your bubble, the coach bubble, word pills, the caret and
  check, the rule card, the café awning, hello pills).
- Source: NEW — built from scratch. The one grammar demo (French age
  takes "have", not "am") checked against French grammar references;
  the narration speaks no French (Kokoro-safety); no language counts,
  no pricing quoted anywhere.

## Package contents

| File | What it is |
|------|------------|
| ACTS.md | Act structure and the companion-film framing |
| SHOTLIST.md | Scene table: beat → what the viewer sees → data source |
| FACTCHECK.md | Claim-by-claim fact check with verdicts and sources |
| SOURCES.md | Fact → source table |
| PROMPTS.md | Prompts that shaped the film; "no generation prompts" |
| make_sheet.py | Generates `beat_sheet.json`; asserts beats and duration |
| beat_sheet.json | The sheet: 11 beats with narration lines and shot notes |
| scenes.py | 7 Manim scene classes (B00–B06), one per body beat |
| BUILD-LOG.md | Dated build steps, including failures |
| CHECKS-REPORT.md | QC gate results (static_scene_check, per class) |
| CLAUDE-CODE-RENDER.md | Render instructions for Bear's Mac |
| README.md | This file |

## Status

Pre-render package only: everything except the final MP3/MP4. Never render,
publish, upload, or stage anything for publication without Bear's explicit
instruction. No audio, video, or cache files are committed.
