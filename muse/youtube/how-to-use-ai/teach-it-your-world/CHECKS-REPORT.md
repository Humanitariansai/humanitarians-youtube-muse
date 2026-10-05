# CHECKS-REPORT.md — "Teach it your world"

QC gate run 2026-10-04, in `~/workspace/film-builds/how-to-ai/teach-it-your-world/`.

## 1. `python3 -m py_compile`

- `make_sheet.py` — clean.
- `scenes.py` — clean.

## 2. `static_scene_check.py scenes.py --class <ClassName>` (all 7 classes)

| Class | Result |
|---|---|
| B02_TheGap | 1 clean · 0 warn · 0 error |
| B03_TheFix | 1 clean · 0 warn · 0 error |
| B04_TheLibrarian | 1 clean · 0 warn · 0 error |
| B05_MeaningMap | 1 clean · 0 warn · 0 error |
| B06_WhatToUpload | 1 clean · 0 warn · 0 error |
| B07_ThreeHabits | 1 clean · 0 warn · 0 error |
| B08_WhereItBites | 1 clean · 0 warn · 0 error |

**Total: 7 clean · 0 warnings · 0 errors.** The check ran with
`beat_sheet.json` beside `scenes.py`, so the `until()` narration pacing
executed against the real sheet (no fallbacks).

## 3. Beat/narration/visual cross-checks (scripted, all passing)

- Every `until(self, "phrase")` in `scenes.py` is present verbatim in its
  beat's `narration_text` (7/7).
- Every on-screen word (`T(...)` / `label(...)` strings, length > 2) is
  spoken in its beat's narration (the word-coverage audit).
- `make_sheet.py` assertions: 13 beats in the exact spine order
  (B00, B01, BDEFS, B02–B08, BVDT, BHTF, BOUT); 7 GRAPHIC beats whose
  `shot.manim.class` starts with the beat id and matches a class in
  `scenes.py`; total 341.2 s inside the 180–360 s window; B01 ≥ 9 s.

## 4. Failures and fixes

- Word-coverage audit (after the first clean QC pass) found four on-screen
  words with no spoken match: B02's "docs" (label "your docs"), B04's
  "rota" (question card), B06's "docs"/"know" ("work docs", "only-you-know"),
  B07's "this" (card line "only from this"), B08's "blind spots". Fixed by
  editing the narration in `make_sheet.py` (B02, B04, B06, B08) and the card
  line in `scenes.py` (B07: "only from this" → "only from these"). Re-ran
  the audit (clean) and the full QC pass (still 0/0). No checker failures at
  any point; nothing waived.

## 5. Noted, not defects

- **B00's composer exchange is illustrative.** The command and the generic
  packing-list output are a drawn demonstration ("Watch:"), not a recorded
  AI session. This is disclosed in BUILD-LOG.md, FACTCHECK.md, and PROMPTS.md.
  The cc-explainer REAL-SESSION LAW does not apply — this film is
  ai-explainer (skill switch recorded in BUILD-LOG.md).
- **BUILD-SHOW slots:** not armed — concept film (no build), per the
  cc-explainer contract inherited by the series' bookend conventions.
- **BDEFS skipped?** No — the film has genuine jargon (knowledge base,
  upload, grounding, RAG), so the definitions beat stays.

## 6. Deferred (cannot run in this VM)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict` —
  requires Manim/pangocairo, not installed here. Deferred to Bear's Mac
  render pass (see CLAUDE-CODE-RENDER.md). Mitigation: all explicit
  coordinates inside ±6.2 × ±3.3, all type ≥ 30 px (labels ≥ 32, body ≥ 36),
  labels beside objects with leader gaps, terracotta only for
  tape/checks/rings/glow (never under text), every scene's motion completes
  in the first ~40% of its beat (GATE T samples the midpoint), and the
  `@NikBearBrown` bug sits inside the safe area on every scene.
