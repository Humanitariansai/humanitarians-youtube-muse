# README.md — Posters and Flyers

**Film #38** · Wave 6 "Making things" · Humanitarians AI — How to AI

Image generation for real-world printables: your garage sale, your bake
sale, your side business. Companion to film 19 `pictures-from-words`
(which taught the image-generation ladder and the five-slot recipe) — this
film uses them without re-teaching.

## The film in one paragraph

A poster has three jobs — a headline readable across the room, details
readable up close, and a picture that makes people look. The AI can't
design it, but it can draw the art; you do the words. The four-step
workflow: (1) say the real job first — what, when, where; (2) make the
words exact, in quotes, because generators draw letters as shapes and
misspell them; (3) split the job — AI draws a text-free picture, you add
the words in any simple poster tool; (4) run the print checklist (tall
shape, dark on light, the three-second arm's-length test) and label the
picture AI-made.

## Package contents

| file | what it is |
|---|---|
| `ACTS.md` | Three-act structure, core promise, tone, source facts |
| `SHOTLIST.md` | Beat-by-beat shots; card-test reasoning (zero cards) |
| `FACTCHECK.md` | Every claim, verdict, source, fix |
| `SOURCES.md` | Companion film + paper sizes + craft guidance |
| `BUILD-LOG.md` | Skill decision, voice-code fix, QC notes |
| `CHECKS-REPORT.md` | Full QC gate results (9 classes, 0 warn / 0 error) |
| `PROMPTS.md` | No generation prompts (all visuals hand-drawn) |
| `CLAUDE-CODE-RENDER.md` | Bear's Mac render instructions (Kokoro + Manim) |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beats and duration |
| `beat_sheet.json` | Render-ready beat sheet (13 beats, 254.2 s ≈ 4m14s) |
| `scenes.py` | 9 Manim scene classes (`<BID>_<Name>(Scene)`), one per GRAPHIC beat |
| `README.md` | This file |

## Film identity

Persona Liam ("Liam, in for Bear") · Kokoro voice `am_onyx` · Teardown
register · channel `claude-liam` · watermark `@NikBearBrown` · greeting
"Hallo" · skill `show-tell` · bookends exempt: cold-open, verdict card.
No pricing tiers quoted. Never publish without Bear's explicit instruction.

## Render

See `CLAUDE-CODE-RENDER.md`. Note: `manim_layout_audit.py --curve-strict`
could not run in the build VM and is deferred to the Mac render pass.
