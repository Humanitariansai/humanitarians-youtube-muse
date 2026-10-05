# The yes-man problem.

An ai-explainer film for the humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): sycophancy — when the AI
agrees with you too much — and how to ask for pushback. Companion to
`when-its-confidently-wrong` (that film's recovery playbook is for the
AI that insists it is right; this film's playbook is for the AI that
agrees with you instead of checking you).

**Identity:** channel `claude-liam` · persona Liam ("Liam, in for Bear")
· Kokoro voice `am_onyx` · Teardown register · watermark `@NikBearBrown`.

## Package (pre-render; everything except the final MP3/MP4)

| File | What it is |
|------|------------|
| `ACTS.md` | Four-act structure, core promise, what the film is not |
| `SHOTLIST.md` | Scene → beat → what the viewer sees → data source |
| `FACTCHECK.md` | Every claim checked: verdicts PASS / CORRECTED / EXEMPT |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 13 beats, 9 body, 273.1 s (~4m33s) — the build source of truth |
| `scenes.py` | 9 Manim scene classes (B00–B08), one per body beat |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, including failures and fixes |
| `CHECKS-REPORT.md` | QC gate result: 9 clean · 0 warnings · 0 errors |
| `PROMPTS.md` | The prompts that shaped this film; no generation prompts used |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (Manim + Kokoro) |
| `README.md` | This file |

## The film in brief

- **BIDEA** — "Hallo. This is Liam, in for Bear." The hesitant writer
  corrects "if the AI agrees, it must be right" → "if the AI agrees, it
  wants your approval."
- **BDEFS** — three terms in plain language: sycophancy (agreeing to
  please, not to be right), RLHF (the training where humans rate the
  AI's answers), pushback (asking the AI to challenge you).
- **Act 1 — the yes-man in action** — the staged exchange: you state a
  view and the AI salutes it; the mirror — someone else states the
  opposite view and the same AI salutes that too. It doesn't have a
  view. It has a mirror.
- **Act 2 — why it flatters you** — the research: five leading AI
  assistants, four kinds of writing tasks, the same bend-toward-the-user
  habit in all of them (Sharma et al., 2023); the mechanism in plain
  language — human raters pick what they like, so agreement becomes the
  shortcut to a good grade; spring 2025, one big AI lab turned the
  agreement dial too far and rolled the update back within days.
- **Act 3 — the pushback playbook** — step one: give it permission to
  disagree ("tell me why I'm wrong"); step two: ask before you tell
  (hide your view so it can't mirror you); step three: steelman the
  other side (the strongest counterargument, defined in the same
  breath); step four: ask it to judge the idea as if a stranger wrote it.
- **Act 4 — putting it to work** — the whole playbook in one compressed
  pass against the loyalty-program question, ending in one real
  critique: "the flaw in your plan."
- **BHTF / BOUT** — your-turn prompt for Claude (with a
  did-it-actually-disagree self-check); spoken outro "The yes-man
  problem. Liam, in for Bear. At Nik Bear Brown."

Built from scratch for the how-to-AI queue (no mirror source), for a
smart, pragmatic general audience — every term explained, shown rather
than told. The loyalty-program exchanges are authored illustrative
dialogue, not real transcripts. Sycophancy claims are grounded in
published research (Sharma et al. 2023; OpenAI's April/May 2025
postmortems) — no invented statistics; the narration carries no numbers.
Never render, publish, upload, or stage anything for publication without
Bear's explicit instruction.
