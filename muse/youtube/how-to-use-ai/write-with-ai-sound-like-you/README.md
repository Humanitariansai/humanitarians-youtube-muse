# "Write with AI, Still Sound Like You" — pre-render film package

How to AI #14 · slug `write-with-ai-sound-like-you` · skill **show-tell**

**Pitch:** Drafting with AI without the robotic aftertaste. AI drafts sound generic
because people accept the default voice. The film shows four fixes — (1) paste a sample
of your own writing and say "match this voice", (2) ban the telltale phrases, (3) dictate
rough thoughts and have the AI clean them up, (4) do the final pass in your own words —
then demos them on a real email.

**Identity:** Liam ("Liam, in for Bear,") · Kokoro `am_onyx` · Teardown register ·
channel `claude-liam` · watermark `@NikBearBrown`

**Package:** 11 beats, 7 Manim body scenes, est. 224 s (~3.7 min). General audience;
every term explained; zero cards (card test: all drawings); no statistics by design.

## Files

| File | What it is |
|------|------------|
| `ACTS.md` | Beat spine: question → terms → 7 body beats → your turn → outro |
| `SHOTLIST.md` | One drawing per beat; card-test result per beat (zero cards) |
| `FACTCHECK.md` | 10 claims checked (PASS / EXEMPT); no invented statistics |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts, order, voice lock, waivers, duration |
| `beat_sheet.json` | The sheet (11 beats, est 224 s) |
| `scenes.py` | `iso_kit.py` + 7 scene classes `B00_RobotDraft` … `B06_TheEmail` |
| `SOURCES.md` | Original script — no external source |
| `BUILD-LOG.md` | Skill choice, build record, failures and fixes, judgments |
| `CHECKS-REPORT.md` | QC gate: 7 clean · 0 warnings · 0 errors (plus the run-1 failure and fix) |
| `PROMPTS.md` | "No generation prompts" |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (audio → audit → stills → `art run` → `art final`) |
| `README.md` | This file |

## Status
Pre-render package complete. QC gate passed. **Nothing rendered, published, uploaded,
or staged.** Bear renders on his Mac per `CLAUDE-CODE-RENDER.md`. Never publish without
his explicit instruction.
