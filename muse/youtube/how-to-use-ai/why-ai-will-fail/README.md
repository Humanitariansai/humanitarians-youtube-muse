# AI will fail. — pre-render film package

**Slug:** `why-ai-will-fail` · **Series:** `muse/youtube/how-to-use-ai/`
**Channel:** https://www.youtube.com/@humanitariansai (`claude-liam`)
**Persona:** Liam ("Liam, in for Bear") · **Voice:** Kokoro `am_onyx`
**Register:** Teardown · **Watermark:** `@NikBearBrown`
**Skill:** ai-explainer · **Beats:** 14 (B00–B13) · **Runtime:** ~5.6 min est.

## The film

For over a century, credentialed experts have confidently declared new
technologies dead — and been wrong nearly every time. The mechanism is the
**insider trap**: the better you know the current game, the worse you are
at seeing the next one. Today's loudest version is "AI will fail." The
film shows the pattern (Olsen, Metcalfe, Ballmer, Keyes, Ellison, Valenti,
Krugman, the BMJ on penicillin), names the mechanism, maps today's AI
skepticism onto its historical twins, and lands the asymmetric bet:
learning is cheap, dismissing is expensive.

Rewritten from the mirror-repo source
(`nikbearbrown/humanitarians-youtube-muse:claude-for-artificial-intelligence/why-ai-will-fail`)
for a smart, pragmatic general audience: every term explained in plain
language, show-don't-tell Manim visuals, Teardown register.

## Package contents (12 files)

| File | What it is |
|---|---|
| `ACTS.md` | Act structure, the one insight, terms explained |
| `SHOTLIST.md` | Per-beat shot descriptions + visual grammar |
| `FACTCHECK.md` | Claim-by-claim verification, verdicts, cuts |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beats + durations |
| `beat_sheet.json` | The 14-beat sheet (generated) |
| `scenes.py` | 14 Manim scene classes, one per beat |
| `SOURCES.md` | Sources, verification links, credits |
| `BUILD-LOG.md` | Decisions, gate signatures, failures + fixes |
| `CHECKS-REPORT.md` | QC gate report (SHOW/HOLD/CARD, teaching arc) |
| `PROMPTS.md` | Per-beat Kokoro narration prompts + handoff prompt |
| `CLAUDE-CODE-RENDER.md` | Bear's local render instructions (Manim + Kokoro) |
| `README.md` | This file |

## Status

- [x] Beat sheet authored + generated (14 beats, 335.2 s est.)
- [x] `py_compile` clean (make_sheet.py, scenes.py)
- [x] Static QC: 14/14 scene classes, 0 warnings, 0 errors
- [x] Fact-check complete (3 apocryphal quotes cut, figures softened)
- [ ] Narration audio (Bear renders locally, Kokoro am_onyx)
- [ ] Manim renders (Bear renders locally)
- [ ] Review cut / publish — only on Bear's explicit instruction

## Regenerate

```bash
python3 make_sheet.py   # rewrites beat_sheet.json, runs all assertions
```
