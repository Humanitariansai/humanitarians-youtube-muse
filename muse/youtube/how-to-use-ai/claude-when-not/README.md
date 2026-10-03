# Claude, When Not. — pre-render package

**Slug:** `claude-when-not` · **Skill:** show-tell · **Register:** Teardown ·
**Playlist:** How to use AI

**Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx` ·
**Channel:** claude-liam · **Watermark:** @NikBearBrown

**Thesis:** Knowing when NOT to use Claude is the AI skill.

## The film

A general-audience rebuild of the "Claude, For Students" season finale
("Claude, When Not."). The source argument survives — scaffold vs. crutch,
the use/don't-use lists, the "would you hide this use?" test, a predict
beat — reframed for bosses, clients, and readers instead of teachers.

**13 beats, ~4:04.** One drawing per beat: a ladder (the skill you're
building), a figure (you), a scaffold frame (AI as support), a crutch (AI as
replacement), and pages (the work). The voice explains; labels are 1–3 words.

## Files

| File | What it is |
|---|---|
| `make_sheet.py` | Generates `beat_sheet.json`; asserts 13 beats + 170–260 s total |
| `beat_sheet.json` | The sheet (beat_id / narration_text / durations / shot / qc) |
| `scenes.py` | 13 Manim scenes (show-tell iso_kit pasted at top) |
| `ACTS.md` | Thesis, cast, act map, runtime |
| `SHOTLIST.md` | Every shot + why-no-card column |
| `FACTCHECK.md` | 14 claims audited (PASS / EXEMPT) |
| `SOURCES.md` | Source beat sheet + verification sources |
| `PROMPTS.md` | "No generation prompts" + the viewer's BHTF prompt |
| `BUILD-LOG.md` | Decisions, failures, fixes |
| `CHECKS-REPORT.md` | QC gate results: 13 clean · 0 warn · 0 error |
| `CLAUDE-CODE-RENDER.md` | Bear's local render instructions (Manim + Kokoro) |

## Status

Pre-render package only. No MP3/MP4 committed or staged. Nothing published.
Render: see CLAUDE-CODE-RENDER.md.
