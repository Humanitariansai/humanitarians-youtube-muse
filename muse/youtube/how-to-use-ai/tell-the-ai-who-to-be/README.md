# Tell the AI who to be

Film #2 of the **How to AI** series for the Humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai).

- **Slug:** `tell-the-ai-who-to-be`
- **Pitch:** Role prompting — "act as a …" — and why it works.
- **Skill:** show-tell (kept; the film is a pure show-tell: one isometric
  drawing per beat, the voice explains, zero ShowTellCards).
- **Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx` ·
  **Register:** Teardown · **Channel:** claude-liam · **Watermark:** @NikBearBrown
- **Beats:** 11 (BIDEA, BDEFS, 7 drawn body beats B00–B06, BHTF, BOUT)
- **Estimated runtime:** ~242 s (≈ 4 min; measured Kokoro audio sets the final clock)
- **Source:** REFACTOR of `claude/claude-for-education/claude-liam-prompt-tutorial-lesson-03-role-prompting`
  (Anthropic Prompt Engineering Interactive Tutorial, Lesson 03) — argument and
  facts kept, script and visuals rewritten for a general audience.

## The argument in one paragraph

A role prompt ("act as a chef") isn't a costume — the AI doesn't become the
chef. It's a calibration dial for the *register*: word choice, assumed
knowledge, tone, and depth. Same facts in, different answer out. A role is
small and functional; a persona is the whole costume with a voice. Use a role
when it changes what counts as a good answer; skip it when it can't.

## Files

| File | What it is |
|---|---|
| `ACTS.md` | act structure |
| `SHOTLIST.md` | shot-by-shot visual plan (incl. why no cards) |
| `FACTCHECK.md` | claim table — no invented statistics |
| `make_sheet.py` | generates `beat_sheet.json`; asserts 11 beats + duration band |
| `beat_sheet.json` | the sheet (generated) |
| `scenes.py` | 7 Manim scene classes (iso kit pasted at top) |
| `SOURCES.md` | refactor source + toolkit references |
| `BUILD-LOG.md` | decisions and build notes |
| `CHECKS-REPORT.md` | QC gate results (7/7 clean; layout audit deferred to Mac) |
| `PROMPTS.md` | no generation prompts (all visuals drawn) |
| `CLAUDE-CODE-RENDER.md` | render instructions for Bear's Mac |
| `README.md` | this file |

## Status

Pre-render package. Static QC passed (py_compile clean; `static_scene_check.py`
7/7 scenes, 0 warnings, 0 errors). `manim_layout_audit.py --curve-strict`
could not run in the build VM (no Manim/pangocairo) — deferred to the Mac
render pass. Never render, publish, or stage from this package without Bear's
explicit instruction.
