# Say what you want, plainly

A show-tell film for the humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): the single highest-leverage
prompting habit — be clear and direct. A vague prompt ("write a summary")
leaves blank lines the AI fills with guesses from its most common
default; a brief answers four questions (how long, what shape, who it's
for, what must be in it). Same job, two prompts: the brief gets the page
that fits.

**Identity:** channel `claude-liam` · persona Liam ("Liam, in for Bear")
· Kokoro voice `am_onyx` · Teardown register · watermark `@NikBearBrown`.

## Package (pre-render; everything except the final MP3/MP4)

| File | What it is |
|------|------------|
| `ACTS.md` | Three-act structure, core promise, what the film is not |
| `SHOTLIST.md` | Scene → beat → what the viewer sees → claim it carries |
| `FACTCHECK.md` | Every claim checked: verdicts PASS / CORRECTED / EXEMPT |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 12 beats, 8 body, 195.2 s (~3m15s) — the build source of truth |
| `scenes.py` | 8 Manim scene classes (B00–B07), one per visual beat |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, including failures and fixes |
| `CHECKS-REPORT.md` | QC gate result: 8 clean · 0 warnings · 0 errors |
| `PROMPTS.md` | The prompts that shaped this film; no generation prompts used |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (Manim + Kokoro) |
| `README.md` | This file |

## The film in brief

- **BIDEA/BDEFS** — "Hallo. This is Liam, in for Bear." The hesitant
  writer corrects "write a summary" → "a three-sentence summary of this
  page, in plain words, for a teammate"; three terms defined in plain
  language (prompt, brief, default).
- **Act 1 — the problem** — the prompt slip arrives (the biggest lever);
  the vague prompt slides into the AI and mismatched pages pop out
  (every blank is a guess); the guesses come from the default — the most
  common answer, not yours.
- **Act 2 — the fix** — say it plainly, like to a person; the four
  questions (length, format, audience, must-haves) drop in as chips; the
  new-hire test (brilliant employee, day one, zero context).
- **Act 3 — the proof** — the vague prompt rewritten into a brief line by
  line; the split-frame comparison (vague: three pages that fit nobody;
  brief: one page that fits, with a check).
- **BHTF / BOUT** — your-turn: audit one of your own prompts against the
  four questions, run both versions, compare; spoken outro "Say what you
  want, plainly. At Nik Bear Brown."

Rewritten from the mirror-repo source
(`claude/claude-for-education/claude-liam-prompt-tutorial-lesson-02-clear-and-direct`,
Anthropic Prompt Engineering Interactive Tutorial Lesson 02) for a smart,
pragmatic general audience — every term explained, shown rather than told.
Never render, publish, upload, or stage anything for publication.
