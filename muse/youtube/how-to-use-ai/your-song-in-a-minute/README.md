# Your song in a minute

A **How to AI** film (#37, Wave 6 "Making things") for the Humanitarians AI
YouTube channel (https://www.youtube.com/@humanitariansai).

- **Slug:** `your-song-in-a-minute`
- **Pitch:** Birthday songs, jingles, bedtime stories: describe it and get a
  finished song back. AI music generation for normal people — what to ask
  for, how to iterate, where the results shine and where they don't. No
  pricing tiers.
- **Skill:** show-tell (kept; the film is a pure show-tell: one isometric
  drawing per beat, the voice explains, zero ShowTellCards).
- **Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx` ·
  **Register:** Teardown · **Channel:** claude-liam · **Watermark:** @NikBearBrown
- **Beats:** 12 (BIDEA, BDEFS, 8 drawn body beats B00–B07, BHTF, BOUT)
- **Estimated runtime:** ~254 s (≈ 4 min; measured Kokoro audio sets the final clock)
- **Source:** NEW film (no mirror-repo source). The one number (44% of new
  Deezer uploads fully AI-generated, ~75,000/day, Apr 2026) verified
  2026-10-05: Deezer newsroom, corroborated by TechCrunch (Jul 2026) —
  attributed aloud and captioned "per Deezer".

## The argument in one paragraph

An AI music tool turns your description into a finished song — words in, song
out, in about a minute. What to ask for: three ingredients — the occasion, the
subject, the style. The first song is a draft: listen to it all the way
through (you're the only quality check it gets), then ask for a fix —
describe, listen, fix, two or three rounds. It shines at short, personal
things: a birthday song with the kid's name in the chorus, a jingle for your
club's video, a lullaby from a bedtime story. It doesn't shine at long songs
(they lose the plot) or mangled words — keep it under three minutes, and never
send a song you haven't heard all the way through.

## Files

| File | What it is |
|---|---|
| `ACTS.md` | act structure |
| `SHOTLIST.md` | shot-by-shot visual plan (incl. why no cards) |
| `FACTCHECK.md` | claim table — one attributed number, no invented statistics |
| `make_sheet.py` | generates `beat_sheet.json`; asserts 12 beats + duration band + voice codes |
| `beat_sheet.json` | the sheet (generated) |
| `scenes.py` | 8 Manim scene classes (iso kit pasted at top + music helpers) |
| `SOURCES.md` | sources + toolkit references |
| `BUILD-LOG.md` | decisions and build notes |
| `CHECKS-REPORT.md` | QC gate results (8/8 clean; layout audit deferred to Mac) |
| `PROMPTS.md` | no generation prompts (all visuals drawn) |
| `CLAUDE-CODE-RENDER.md` | render instructions for Bear's Mac |
| `README.md` | this file |

## Status

Pre-render package. Static QC passed (py_compile clean; `static_scene_check.py`
8/8 scenes, 0 warnings, 0 errors). `manim_layout_audit.py --curve-strict`
could not run in the build VM (no Manim/pangocairo) — deferred to the Mac
render pass. Never render, publish, or stage from this package without Bear's
explicit instruction.
