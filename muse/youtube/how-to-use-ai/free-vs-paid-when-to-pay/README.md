# Free vs paid: when to pay.

An ai-explainer concept film for the humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): what the paid tiers of AI
chatbots actually buy you, and the two-question test that tells you whether
paying is worth it. A decision framework, not a price list — no prices are
quoted, so the film cannot go stale.

**Identity:** channel `claude-liam` · persona Liam ("Liam, in for Bear")
· Kokoro voice `am_onyx` · Teardown register · watermark `@NikBearBrown`.

## Package (pre-render; everything except the final MP3/MP4)

| File | What it is |
|------|------------|
| `ACTS.md` | Three-act structure, core promise, what the film is not |
| `SHOTLIST.md` | Scene → beat → what the viewer sees → data source |
| `FACTCHECK.md` | Every claim checked: verdicts PASS / CORRECTED / EXEMPT; no prices quoted |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 14 beats, 9 body, 359 s (~5m59s) — the build source of truth |
| `scenes.py` | 14 Manim scene classes (M01–M14), one per beat |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, including the cc-explainer → ai-explainer switch |
| `CHECKS-REPORT.md` | QC gate result: 14 clean · 0 warnings · 0 errors |
| `PROMPTS.md` | The prompts that shaped this film; no generation prompts used |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (Manim + Kokoro) |
| `README.md` | This file |

## The film in brief

- **BIDEA/BDEFS** — "Ciao. This is Liam, in for Bear." The hesitant writer
  corrects "Paid AI is for AI people" → "Paid AI is for people who keep
  hitting the wall"; four terms defined in plain language (free tier,
  usage limit, model, context).
- **Act 1 — the wall** — the free tier is the real thing with a meter; the
  limit is the price of free, because every answer costs real money.
- **Act 2 — what the money buys** — the four-item menu (sharper model,
  higher limits, longer memory, early features); the sharper model only
  matters on hard questions; the limit arithmetic (the free tier costs
  time — the moment your time is worth more than the fee, paying is a
  refund).
- **Act 3 — the decision** — when free is enough vs. when paying pays off;
  the two-question flowchart; the trap (never buy the annual plan before
  the one-month experiment).
- **BVDT / BHTF / BOUT** — recap; your-turn prompt ("ask your AI to judge
  your own usage, then grade it against the two-question test"); spoken
  title restate and the locked @NikBearBrown outro.
