# BUILD-LOG.md — "ChatGPT or Claude?" (general-audience redo)

Build date: 2026-10-03. Builder: Muse (film-package subagent).
Skill used: **ai-explainer** (chosen over cc-explainer: this film compares
AI chat products for a general audience — there is no Claude Code terminal
session, so cc-explainer's TERMINAL-FIRST law does not fit; the source
README also recommends ai-explainer).

## Decisions

- **Retitle**: "ChatGPT-5.5 or Claude 4.7?" → "ChatGPT or Claude?". Version
  numbers churn weekly (press has GPT-5.5 entering ChatGPT 2026-04-23 and
  leaving 2026-10-14; Anthropic shipped eight Claude versions in twelve
  months). A versioned title would date the film before it ships. Logged
  in FACTCHECK.md §1. [judgment]
- **Persona/voice/register**: Kore/af_kore/Pragmatist → Liam/am_onyx/
  Teardown, per film identity constants. Greeting "Bula, Kore" → "Hola,
  Liam" (world-language hello, Liam's one-word cue budget). [record]
- **Dropped for the general audience**: "AskUserQuestion" magic prompt
  (Claude Code tool, wrong surface), "Connectors", "multi-agent Cowork
  sessions" — replaced with plain descriptions. "Gemini for non-English /
  Gamma for slides" compressed to one verdict line making no benchmark
  claim. "That April week" undated. All logged in FACTCHECK.md. [judgment]
- **Kept from the source**: the argument spine — the one rule, persistent
  context as Claude's edge, ChatGPT's images/sheets/search lane, the two
  exits, the test-it-yourself close. [record]
- **Beat count**: 12 beats (B00, B01, B02, B03, B04, B05, B06, B07, B08,
  BVDT, BHTF, BOUT), 7 body beats, 273 s (~4m33s). M10 covers the three
  closing beats in three phases. [record]

## Failures and fixes

- make_sheet.py's narration-clock assertion failed on first run: B05 had
  66 words against a 26 s budget (needs ≥26.4 s at 150 wpm). Fixed by
  cutting one word ("a good default work brain" → "a default work brain");
  the line is unchanged in meaning. Reran: 12 beats, 273 s, all asserts
  pass. [record]
- No QC failures: all 10 scene classes passed static_scene_check first
  try, 0 warnings, 0 errors (see CHECKS-REPORT.md). [record]
- Pre-QC review (from the FRICTIONAL.md film-1 lesson): every mobject is
  introduced via add()/FadeIn()/Write()/Create() — nothing enters the
  scene through .animate() alone; no stub-only attribute hacks; on-screen
  text lines kept short. [my input]

## Not done here (for Bear / the render step)

- Narration MP3s (Kokoro am_onyx), Manim renders, assembly, publication —
  pre-render package only, per the brief. See CLAUDE-CODE-RENDER.md.
