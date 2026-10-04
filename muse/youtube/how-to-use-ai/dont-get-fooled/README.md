# Don't get fooled.

An ai-explainer film for the humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): why AI sounds sure when it's
wrong, and the three habits that keep you safe — grounding, citing, and
cross-checking.

**Identity:** channel `claude-liam` · persona Liam ("Liam, in for Bear")
· Kokoro voice `am_onyx` · Teardown register · watermark `@NikBearBrown`.

## Package (pre-render; everything except the final MP3/MP4)

| File | What it is |
|------|------------|
| `ACTS.md` | Three-act structure, core promise, what the film is not |
| `SHOTLIST.md` | Scene → beat → what the viewer sees → data source |
| `FACTCHECK.md` | Every claim checked: verified / judgments / illustrative |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 13 beats, 8 body, 311 s (~5m11s) — the build source of truth |
| `scenes.py` | 13 Manim scene classes (M01–M13), one per beat |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, including the mislabeled-source catch |
| `CHECKS-REPORT.md` | QC gate result (per-class static check) |
| `PROMPTS.md` | The prompts that shaped this film; no generation prompts used |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (Manim + Kokoro) |
| `README.md` | This file |

## The film in brief

- **B00 / B01** — "Olá. This is Liam, in for Bear." The composer asks the
  film's question and answers it; the hesitant writer corrects "AI lies to
  you because it's badly trained" → "AI guesses the most likely words,
  not the truth."
- **Act 1 — why it lies to you** — the next-word-prediction mechanism
  (most likely ≠ always right); habit zero (the confident tone tells you
  nothing); the true story of the lawyer who filed six invented court
  cases (Mata v. Avianca, 2023 — $5,000 fine).
- **Act 2 — the three-sentence fix** — grounding: paste the source,
  answer only from it; give it permission to say "I don't know."
- **Act 3 — the audit habits** — quote the exact sentence and check it
  (hallucinated citations are catchable); cross-check anything that
  matters; the three-sentence card to keep.
- **BVDT / BHTF / BOUT** — recap; your-turn prompt ("Answer only from the
  text above…", read aloud, for Claude); spoken outro "Don't get fooled.
  Liam, in for Bear. At Nik Bear Brown."

Rewritten from the mirror-repo source (Anthropic Prompt Engineering
Tutorial · Lesson 8, Avoiding Hallucinations — via the true
`claude-liam-prompt-tutorial-lesson-08-avoiding-hallucinations` sheet and
its PEDAGOGY.md verdict; the base folder's beat sheet was a mislabeled
copy of lesson 07 and was not used) for a smart, pragmatic general
audience — every term explained, shown rather than told.
Never render, publish, upload, or stage anything for publication without
Bear's explicit instruction.
