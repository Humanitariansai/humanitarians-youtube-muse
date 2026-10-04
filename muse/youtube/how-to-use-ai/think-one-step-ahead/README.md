# Think one step ahead — pre-render package

**Slug:** `think-one-step-ahead` · **Skill:** show-tell · **Register:** Teardown ·
**Playlist:** How to AI (chapter 6)

**Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx` ·
**Channel:** claude-liam · **Watermark:** @NikBearBrown

**Thesis:** Claude writes one word at a time, so the first word locks the
rest. Ask it to think first — and ask for what you'll need next — and you get
tomorrow's answer, today.

## The film

A general-audience refactor of the mirror repo's prompt-tutorial lesson 06
("Precognition: Give Claude a Scratchpad Before the Answer"). The jargon is
gone: no "precognition", no XML tags on screen. Instead, a concrete
before/after on one cast of drawn objects — a Claude window, a prompt slip,
a thinking page, an answer page. Before: demand the answer straight away and
Claude defends its first guess. After: give it a scratchpad, let it cross
out the wrong idea, and the answer gets written once, on top of the thinking.
Then the scratch-paper rule (when to think first, when to skip it) and the
one-step-further move: ask for what you'll need next.

**10 beats, ~3:10.** One drawing per beat; the voice explains; labels are
1–3 words.

## Files

| File | What it is |
|---|---|
| `make_sheet.py` | Generates `beat_sheet.json`; asserts 10 beats + 170–260 s total |
| `beat_sheet.json` | The sheet (beat_id / narration_text / durations / shot / qc) |
| `scenes.py` | 6 Manim scenes (show-tell iso_kit pasted at top) |
| `ACTS.md` | Thesis, cast, act map, runtime |
| `SHOTLIST.md` | Every shot + why-no-card column |
| `FACTCHECK.md` | 11 claims audited (PASS / EXEMPT) |
| `SOURCES.md` | Source beat sheet + verification sources |
| `PROMPTS.md` | "No generation prompts" + the viewer's BHTF prompt |
| `BUILD-LOG.md` | Decisions, failures, fixes |
| `CHECKS-REPORT.md` | QC gate results: 6 clean · 0 warn · 0 error |
| `CLAUDE-CODE-RENDER.md` | Bear's local render instructions (Manim + Kokoro) |

## Status

Pre-render package only. No MP3/MP4 committed or staged. Nothing published.
Render: see CLAUDE-CODE-RENDER.md.
