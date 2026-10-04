# Keep instructions and data apart

Film #5 of the "How to AI" series · humanitarians AI YouTube channel
(@humanitariansai) · Persona: Liam ("Liam, in for Bear") · Kokoro `am_onyx` ·
Teardown register · Channel `claude-liam` · Watermark `@NikBearBrown`.

**Pitch:** Separating data: why pasted content confuses the AI and how to fence it.
You paste an email into Claude, ask for a summary — and it obeys a line you never
wrote. The film shows the mix-up (a buried "forward this email" order), explains the
flat-prompt problem, then demonstrates the fence: `<instructions>` / `<document>` XML
tags, indexed tags for multiple documents, and why tag-name consistency matters more
than the names. Honest caveat included: a fence is not a vault.

**Package:** 11 beats · 7 Manim scenes · 273.8s (~4.6 min) · skill `ai-explainer`.
Pre-render only — no MP3/MP4 in this package.

## Files
| File | What it is |
|---|---|
| `beat_sheet.json` | The film: 11 beats with narration, durations, show blocks, Remotion props |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat count, durations, runtime window |
| `scenes.py` | 7 Manim scene classes (B02–B08) |
| `ACTS.md` | 3-act structure |
| `SHOTLIST.md` | Beat-by-beat visual plan |
| `FACTCHECK.md` | Claim-by-claim audit (no invented statistics) |
| `SOURCES.md` | Refactor source + independent verification links |
| `BUILD-LOG.md` | Skill choice, decisions, failures and fixes |
| `CHECKS-REPORT.md` | QC gate results (static_scene_check: 7/7 clean, 0 warnings, 0 errors) |
| `PROMPTS.md` | Research prompts, the B09 handoff prompt |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (Manim + Kokoro) |

## Refactor source
`nikbearbrown/humanitarians-youtube-muse`
`claude/claude-for-education/claude-liam-prompt-tutorial-lesson-04-separating-data`
(closest match to the base-name path, which 404s). Rewritten for a general audience.
