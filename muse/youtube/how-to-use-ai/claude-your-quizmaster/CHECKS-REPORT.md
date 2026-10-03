# CHECKS-REPORT.md — Claude, Your Quizmaster

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 8 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| M01_Bidea | clean |
| M02_Bdefs | clean |
| M03_B01WhyQuiz | clean |
| M04_B02Predict | clean |
| M05_B03Space | clean |
| M06_B04ExplainBack | clean |
| M07_B05YourWork | clean |
| M08_BvdtHtfOut | clean |

## Issues found and fixed (pre-gate review)

None at the gate itself — all 8 scenes passed on the first full run.
The following were caught in the author's pre-flight review, before the
checker ever ran:

1. **Animate-only shapes.** The M04 card flip was first drafted as a
   single `cover.animate.scale(...)` in one play — under the stub that
   records no membership change, and under real Manim it would leave the
   revealed definition never added. Rewrote as FadeOut(cover) +
   FadeIn(reveal) crossfade, then a separate FadeIn for the "wrong
   guesses count" note: two real membership changes.
2. **Recap line widths.** First-draft M08 recap lines were ~55 chars at
   font_size 20 — wider than the plate at real-Manin text widths.
   Shortened all four lines to ≤44 chars (the sibling package's proven
   bound).
3. **Composer prompt line widths.** The BHTF prompt was first drafted as
   full sentences; split into ≤30-char lines at font_size 18 so every
   line fits the 11.6-wide composer card with margin.
4. **Beat-count band.** make_sheet.py asserts exactly 10 beats and a
   200–320 s total band (beats=10 body=5 total=243s). The band is
   film-specific, not inherited: show-tell law 9 sets no length target,
   so the sheet asserts what the content needs.

## Skill-fit note

cc-explainer was considered and rejected: its TERMINAL-FIRST law,
REAL-SESSION law, and CONDUCT/HUMAN closing block are built for Claude
Code session reconstructions; this film is a chat-product technique
explainer with no terminal in it. show-tell's spine (hesitant writer →
key terms → drawn body → Your Turn composer → spoken outro) was used in
full.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 10 beats, 5 body beats, total 243 s, BVDT covers both acts,
BHTF reads the handoff prompt in full.
