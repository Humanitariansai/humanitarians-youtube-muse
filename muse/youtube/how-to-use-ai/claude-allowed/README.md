# Claude, Allowed. — pre-render film package

**Slug:** `claude-allowed` · **Skill:** show-tell · **Register:** Teardown
**Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx`
**Channel:** `claude-liam` · **Watermark:** `@NikBearBrown`
**Write repo:** `Humanitariansai/humanitarians-youtube-muse` → `muse/youtube/how-to-use-ai/claude-allowed/`

## What it is

A show-tell explainer (~2:50, 10 beats) that takes apart AI-use bans — at school and
at work. One sentence, drawn six ways: **the ban is a rule about work you submit as
your own; it is not a ban on getting good at AI.**

Rewrites `hai-claude-allowed` ("Claude, For Students" H1, mirror repo) for the
humanitarians AI general audience: smart, pragmatic, not necessarily AI experts.
The school policy stays as the concrete running example; the point generalizes.

## Package (12 files)

| File | What |
|------|------|
| `make_sheet.py` | generates `beat_sheet.json`; asserts beat ids, scene-class names, duration band |
| `beat_sheet.json` | the film: 10 beats, narration, shot/motion intents, Remotion props |
| `scenes.py` | 6 Manim scene classes (`B00_PolicyPage` … `B05_Reveal`) + the iso drawing kit |
| `ACTS.md` | structure + the general-audience reframing vs the source |
| `SHOTLIST.md` | per-beat visuals + the card-test result (body is 100% drawings) |
| `FACTCHECK.md` | 8-claim audit table (PASS ×6, EXEMPT ×2) |
| `SOURCES.md` | mirror-repo source + 2026-10-03 fact-check sources |
| `PROMPTS.md` | "no generation prompts" |
| `BUILD-LOG.md` | decisions and build steps |
| `CHECKS-REPORT.md` | QC results: py_compile clean; 6/6 scenes 0 warnings, 0 errors |
| `CLAUDE-CODE-RENDER.md` | Bear's local render instructions (Manim + Kokoro) |
| `README.md` | this file |

## Status

Pre-render package only. No MP3/MP4/WAV committed. **Never render, publish, upload,
or stage anything for publication** — publishing is Bear's explicit call only.

## House red line

This film teaches: read the policy, ask in writing, disclose AI help, build fluency
on your own time. It never teaches evasion, detection-dodging, or ban-circumvention.
