# When it's confidently wrong.

An ai-explainer film for the humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): why the AI doubles down when
it's wrong — and the four-step recovery playbook: restart, ask for
sources, narrow the question, verify elsewhere.

**Identity:** channel `claude-liam` · persona Liam ("Liam, in for Bear")
· Kokoro voice `am_onyx` · Teardown register · watermark `@NikBearBrown`.

## Package (pre-render; everything except the final MP3/MP4)

| File | What it is |
|------|------------|
| `ACTS.md` | Three-act structure, core promise, what the film is not |
| `SHOTLIST.md` | Scene → beat → what the viewer sees → data source |
| `FACTCHECK.md` | Every claim checked: verdicts PASS / CORRECTED / EXEMPT |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 14 beats, 8 body, 317 s (~5m17s) — the build source of truth |
| `scenes.py` | 14 Manim scene classes (M01–M14), one per beat |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, including failures and fixes |
| `CHECKS-REPORT.md` | QC gate result: 14 clean · 0 warnings · 0 errors |
| `PROMPTS.md` | The prompts that shaped this film; no generation prompts used |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (Manim + Kokoro) |
| `README.md` | This file |

## The film in brief

- **B00/B01/B02** — "Hallo. This is Liam, in for Bear." The composer
  cold-open ask ("Why does the AI insist when it's wrong?"); the
  hesitant writer corrects "when the AI insists, argue harder" → "when
  the AI insists, run the playbook"; three terms defined in plain
  language (hallucination, model, double down).
- **Act 1 — the problem** — the staged exchange: the AI confidently
  states a wrong answer (the confidence gauge fills to full); challenged,
  it doubles down; the mechanism in plain language — the model picks the
  most likely next word, has no fact-checker and no honesty meter, and
  the most consistent reply to "I was right" is "I'm still right," so
  arguing feeds the loop.
- **Act 2 — the recovery playbook** — step one: don't argue, restart in
  a fresh chat with new framing; step two: ask for sources and actually
  check one; step three: narrow the question until the error is cornered
  between small checkable facts; step four: know when to stop and verify
  elsewhere (search, a book, a person).
- **Act 3 — putting it to work** — the whole playbook in one compressed
  pass against the staged exchange: one recovered truth.
- **BVDT / BHTF / BOUT** — recap; your-turn prompt for Claude; spoken
  outro "When it's confidently wrong. Liam, in for Bear. At Nik Bear
  Brown."

Built from scratch for the how-to-AI queue (no mirror source), for a
smart, pragmatic general audience — every term explained, shown rather
than told. The Riverside Library exchange is authored illustrative
dialogue, not a real transcript. Never render, publish, upload, or
stage anything for publication without Bear's explicit instruction.
