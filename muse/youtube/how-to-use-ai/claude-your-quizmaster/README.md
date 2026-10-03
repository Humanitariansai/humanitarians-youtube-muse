# Claude, Your Quizmaster

A pre-render film package for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai).

**The film:** stop asking Claude for answers — make it ask you questions.
Four lab-backed moves (quiz-don't-ask, predict-first, spaced reviews,
explain-it-back) that turn the chat window into a quizmaster, plus a
copy-paste prompt the viewer runs tonight.

- Persona: Liam ("Liam, in for Bear"); Kokoro voice `am_onyx`;
  register Teardown; channel claude-liam; watermark @NikBearBrown.
- Skill: show-tell. 10 beats, ~4m03s, 8 Manim scenes.
- Source: `claude-for-artificial-intelligence/hai-your-quizmaster` in the
  mirror repo (read-only reference), rewritten for a general audience.

## Package contents

| File | What it is |
|------|------------|
| ACTS.md | Act structure and the audience rewrite rationale |
| SHOTLIST.md | Scene table: beat → what the viewer sees → data source |
| FACTCHECK.md | Claim-by-claim fact check with verdicts and sources |
| SOURCES.md | Fact → source table |
| PROMPTS.md | Prompts that shaped the film; "no generation prompts" |
| make_sheet.py | Generates `beat_sheet.json`; asserts beats and duration |
| beat_sheet.json | The sheet: 10 beats with narration lines and shot notes |
| scenes.py | 8 Manim scene classes (M01–M08), one per visual beat |
| BUILD-LOG.md | Dated build steps, including failures |
| CHECKS-REPORT.md | QC gate results (static_scene_check, per class) |
| CLAUDE-CODE-RENDER.md | Render instructions for Bear's Mac |
| README.md | This file |

## Status

Pre-render package only: everything except the final MP3/MP4. Never render,
publish, upload, or stage anything for publication without Bear's explicit
instruction. No audio, video, or cache files are committed.
