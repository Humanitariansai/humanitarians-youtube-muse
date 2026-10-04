# "One AI or many?" — pre-render film package

Film #24 of the humanitarians "How to AI" series, for the
[humanitarians AI YouTube channel](https://www.youtube.com/@humanitariansai).
Companion to "ChatGPT or Claude?" (`../everyone-wants-one-ai/`) in the same
series folder — consistent with it, not contradicting it.

- **Skill:** ai-explainer (switched from assigned cc-explainer — see
  BUILD-LOG.md) · **Persona:** Liam ("Liam, in for Bear") ·
  **Voice:** Kokoro `am_onyx` · **Register:** Teardown ·
  **Watermark:** @NikBearBrown
- **Beats:** 12 (B00, B01, B02, B03, B04, B05, B06, B07, B08, BVDT, BHTF,
  BOUT) · **Runtime:** 287 s (~4m47s) · **Manim scenes:** M01–M10
- **QC:** `python3 -m py_compile` clean; static scene check 10/10 clean,
  0 warnings, 0 errors (see CHECKS-REPORT.md).

## The film in one breath

The liberating truth: for most everyday work, the differences between top
AI tools are smaller than the difference between using one well and using
one badly. So stop shopping. Pick the AI you already have, learn it
properly (this series teaches you how — ask well, show examples, check the
draft), and add a second only when you hit a specific wall: serious image
work, heavy coding, your files and team living in another tool's world, or
price. The leaderboard changes monthly; your skill transfers. The companion
film said the stack is the answer — this film says build the stack slowly.

The film names no vendors, versions, rankings, or prices — every comparison
is generic and framework-level, so it stays true when the leaderboard
turns over (see FACTCHECK.md).

## Files

| File | What it is |
|------|------------|
| ACTS.md | Act structure, core promise, companion-film relationship |
| SHOTLIST.md | Scene → beat → visual table |
| FACTCHECK.md | Claim-by-claim audit (8 items) |
| SOURCES.md | References consulted, verbatim |
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
