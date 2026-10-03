# "ChatGPT or Claude?" — pre-render film package

General-audience redo of
`claude-for-artificial-intelligence/everyone-wants-one-ai`
("ChatGPT-5.5 or Claude 4.7?") for the
[humanitarians AI YouTube channel](https://www.youtube.com/@humanitariansai).

- **Skill:** ai-explainer · **Persona:** Liam ("Liam, in for Bear") ·
  **Voice:** Kokoro `am_onyx` · **Register:** Teardown ·
  **Watermark:** @NikBearBrown
- **Beats:** 12 (B00, B01, B02, B03, B04, B05, B06, B07, B08, BVDT, BHTF,
  BOUT) · **Runtime:** 273 s (~4m33s) · **Manim scenes:** M01–M10
- **QC:** `python3 -m py_compile` clean; static scene check 10/10 clean,
  0 warnings, 0 errors (see CHECKS-REPORT.md).

## The film in one breath

Stop shopping for the smartest AI on a leaderboard. The one rule: use the
tool your company pays for (or both). Claude's edge is boring — a folder
of context it reads every session so you stop repeating yourself.
ChatGPT's lane is images, spreadsheets, and deep search. The two exits:
writing → Claude, images/sheets/research → ChatGPT. And the only honest
benchmark is your own work: one real task, both tools, thirty minutes.

The film names vendors and approaches, never model version numbers — the
source's "ChatGPT-5.5 / Claude 4.7" title is retired in FACTCHECK.md §1
because version availability churns faster than a film's shelf life.

## Files

| File | What it is |
|------|------------|
| ACTS.md | Act structure, core promise, redo notes |
| SHOTLIST.md | Scene → beat → visual table |
| FACTCHECK.md | Claim-by-claim audit (12 items) |
| SOURCES.md | URLs consulted, verbatim |
| make_sheet.py | Generates beat_sheet.json; asserts beats + durations |
| beat_sheet.json | The 12-beat sheet (generated — do not hand-edit) |
| scenes.py | 10 Manim scene classes (M01–M10) |
| BUILD-LOG.md | Decisions, failures, fixes |
| CHECKS-REPORT.md | QC results: 10 clean · 0 warn · 0 error |
| PROMPTS.md | Prompts/directives that shaped the film |
| CLAUDE-CODE-RENDER.md | Render instructions for Bear's Mac |
| README.md | This file |

Pre-render package only: no MP3/MP4/WAV here. Render locally per
CLAUDE-CODE-RENDER.md. Never publish without Bear's explicit instruction.
