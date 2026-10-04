# Pictures from Words

Film 19 of the humanitarians-channel "How to AI" series — image generation
basics for non-designers. A pre-render package: script, Manim visuals, and
docs. Everything except the final MP3/MP4.

**Core idea:** describing a picture in words is a learnable skill. The film
teaches the ladder: vague prompt → generic result; add subject + style +
mood → much better; iterate like texting a friend ("warmer light",
"wider shot"). Plus the five-slot prompt recipe, practical uses (slides,
invitations, mockups, visualizing ideas), and one honest beat on limits:
text in images, hands/faces, and saying when a picture is AI-made.

## Files

| File | What it is |
|------|-----------|
| `ACTS.md` | Three-act structure, core promise, tone, source facts |
| `SHOTLIST.md` | Scene → beat → what the viewer sees → data source |
| `FACTCHECK.md` | Every checkable claim, verified 2026-10-03, [record]/[judgment] labeled |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and total duration |
| `beat_sheet.json` | 14 beats, 9 body, 282 s (~4m42s) — the narration script |
| `scenes.py` | 12 Manim scene classes (M01–M12), one per visual beat |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, including failures and decisions |
| `CHECKS-REPORT.md` | QC gate results: 12 clean · 0 warnings · 0 errors |
| `PROMPTS.md` | Prompts and briefs that shaped the film |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (Manim + Kokoro) |
| `README.md` | This file |

## Film identity

Persona Liam ("Liam, in for Bear"); Kokoro voice `am_onyx`; Teardown
register; channel `claude-liam`; watermark `@NikBearBrown`.

## Companion film

`fellows/rohan-v/2026-09-25-how-ai-image-generators-turn-noise-into-a-picture`
in the mirror repo explains HOW image generators work; this film teaches
HOW TO USE one. Reference only — not a refactor.
