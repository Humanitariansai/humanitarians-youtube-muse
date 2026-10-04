# Show It an Example

Film 3 of 24 · How to AI · show-tell · ~3.5 min (209 s est.)

**Pitch.** Few-shot: one example beats a paragraph of instructions. A general-
audience refactor of the few-shot prompting lesson: your prompt is a box, and
you can fill it by describing what you want — or by showing three finished
examples. The examples quietly carry length, tone, shape, words, and tricky
cases all at once. One sloppy example teaches the wrong lesson.

**Identity.** Persona Liam ("Liam, in for Bear"); Kokoro voice `am_onyx`;
Teardown register; channel `claude-liam`; watermark `@NikBearBrown`.

**Package (pre-render — everything except the final MP3/MP4):**

| File | What it is |
|---|---|
| `ACTS.md` | act structure and the argument |
| `SHOTLIST.md` | shot-by-shot plan, motion, labels, continuity |
| `FACTCHECK.md` | every claim checked (PASS / CORRECTED / EXEMPT) |
| `make_sheet.py` | generates `beat_sheet.json`; asserts beats + duration |
| `beat_sheet.json` | 11 beats, narration, shots, bookends |
| `scenes.py` | 7 Manim scene classes (iso_kit pasted at top) |
| `SOURCES.md` | source folder + what was kept vs. rewritten |
| `BUILD-LOG.md` | build record, incl. skill choice and QC |
| `CHECKS-REPORT.md` | QC gate results (0 warn / 0 error) |
| `PROMPTS.md` | no generation prompts (all visuals hand-drawn) |
| `CLAUDE-CODE-RENDER.md` | render instructions for Bear's Mac |
| `README.md` | this file |

**Beats.** BIDEA (hesitant writer) · BDEFS (prompt / example / few-shot) ·
B00 the box · B01 the rule stack · B02 examples drop in · B03 five things ·
B04 the sloppy example · B05 three checks · B06 short vs tall · BHTF (composer)
· BOUT (spoken outro).

**Render.** See `CLAUDE-CODE-RENDER.md`. Note: `manim_layout_audit.py
--curve-strict` is deferred to the Mac render pass (no Manim/pangocairo in the
build VM).
