# AI is a slot machine.

A show-tell film for the humanitarians AI YouTube channel
(https://www.youtube.com/@humanitariansai): why everyone reacts to AI the
way they do, and the one mental model that fixes it — AI is a slot
machine. Probabilistic, not deterministic. Pull the lever many times;
keep the best.

**Identity:** channel `claude-liam` · persona Liam ("Liam, in for Bear")
· Kokoro voice `am_onyx` · Teardown register · watermark `@NikBearBrown`.

## Package (pre-render; everything except the final MP3/MP4)

| File | What it is |
|------|------------|
| `ACTS.md` | Three-act structure, core promise, what the film is not |
| `SHOTLIST.md` | Scene → beat → what the viewer sees → data source |
| `FACTCHECK.md` | Every claim checked: verdicts PASS / CORRECTED / EXEMPT |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and duration |
| `beat_sheet.json` | 16 beats, 11 body, 286 s (~4m46s) — the build source of truth |
| `scenes.py` | 16 Manim scene classes (M01–M16), one per beat |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, including failures and fixes |
| `CHECKS-REPORT.md` | QC gate result: 16 clean · 0 warnings · 0 errors |
| `PROMPTS.md` | The prompts that shaped this film; no generation prompts used |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac (Manim + Kokoro) |
| `README.md` | This file |

## The film in brief

- **BIDEA/BDEFS** — "Hallo. This is Liam, in for Bear." The hesitant
  writer corrects "AI is a truth machine" → "AI is a slot machine";
  four terms defined in plain language (prompt, probabilistic,
  hallucination, the AI gambler).
- **Act 1 — the machine** — the slot machine arrives; the same prompt
  gives three different answers (probabilistic); the five-stage pattern,
  borrowed from Kübler-Ross's stages of grief.
- **Act 2 — the four stuck stages** — denial, anger, bargaining (the
  perfect-prompt fallacy), depression.
- **Act 3 — the gambler** — acceptance: pull a hundred times, keep five,
  trash the rest; the three-rule playbook (ask for three versions;
  manage it like an intern; think in batches).
- **BVDT / BHTF / BOUT** — recap; your-turn prompt for Claude; spoken
  outro "AI is a slot machine. Liam, in for Bear. At Nik Bear Brown."

Rewritten from the mirror-repo source
(`claude-for-artificial-intelligence/ai-is-a-slot-machine`) for a smart,
pragmatic general audience — every term explained, shown rather than told.
Never render, publish, upload, or stage anything for publication without
Bear's explicit instruction.
