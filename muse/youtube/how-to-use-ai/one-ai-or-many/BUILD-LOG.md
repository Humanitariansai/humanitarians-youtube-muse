# BUILD-LOG.md — "One AI or many?"

Build date: 2026-10-03. Builder: Muse (film-package subagent).
Skill used: **ai-explainer** (switched from the assigned cc-explainer:
this film compares AI tools for a general audience — there is no Claude
Code terminal session, so cc-explainer's TERMINAL-FIRST law does not fit;
ai-explainer is the same skill the companion film used).

## Decisions

- **Title**: working title "One AI or many?" kept verbatim — generic,
  vendor-free, undated; retitling would only narrow it. [judgment]
- **Greeting rotation**: companion used "Hola, Liam"; this film opens
  "Ciao, Liam" (ai-explainer world-language-hello rotation, one-word
  budget for Liam). [record]
- **No vendors named**: unlike the companion (Claude vs ChatGPT), this film
  speaks only of "AI tools" — the decision rule is vendor-independent, and
  naming strengths per vendor would date it. The podium icons are
  anonymous shapes. [judgment]
- **Beat count**: 12 beats (B00–B08, BVDT, BHTF, BOUT), 7 body beats,
  287 s (~4m47s). M10 covers the three closing beats in three phases.
  [record]
- **Consistency with companion**: read the companion's ACTS.md and
  BUILD-LOG.md before authoring; verdicts aligned ("the stack is the
  answer" → "build the stack slowly"); the 30-minute test cited, not
  re-litigated. Logged in FACTCHECK.md §6. [record]

## Failures and fixes

- make_sheet.py's narration-clock assertion: all beats passed first run
  after trimming B07 to 65 words (27 s budget covers 26.0 s) and setting
  BVDT to 32 s for the 76-word verdict. No assertion failures in the
  final run. [record]
- Static QC: all 10 scene classes passed first try, 0 warnings, 0 errors
  (see CHECKS-REPORT.md). [record]
- Pre-QC review (from the FRICTIONAL.md film-1 lesson): every mobject is
  introduced via add()/FadeIn()/Write()/Create()/GrowFrom* — nothing
  enters the scene through .animate() alone (M06/M09 use .animate() only
  on already-added mobjects); no stub-only attribute hacks; on-screen
  text lines kept short (≤ ~45 chars); coordinates inside the safe area.
  [my input]

## Not done here (for Bear / the render step)

- Narration MP3s (Kokoro am_onyx), Manim renders, assembly, publication —
  pre-render package only, per the brief. See CLAUDE-CODE-RENDER.md.
- `manim_layout_audit.py --curve-strict` could not run in this VM
  (no Manim/pangocairo) — deferred to Bear's Mac render pass.
