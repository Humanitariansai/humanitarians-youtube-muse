# CHECKS-REPORT.md — Agents: AI that does things.

Date: 2026-10-04. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.
`manim_layout_audit.py --curve-strict` could not run in this VM (no
Manim/pangocairo) — deferred to Bear's Mac render pass.

## Result: 8 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| B02_Agent | clean |
| B03_Loop | clean |
| B04_Rules | clean |
| B05_Helps | clean |
| B06_WrongPlace | clean |
| B07_Compound | clean |
| B08_Runs | clean |
| B09_Verdict | clean |

## Issues found and fixed

1. **B02 label/card separation (pre-QC).** Ingredient cards were
   `.animate()`-moved while their text labels stayed at the original
   positions. Regrouped each ingredient as a `VGroup(card, title, sub)`
   and replaced the motion with the AGENT card stamping in beneath the
   landed ingredients. [record]
2. **B05 degenerate arrows (pre-QC).** Per-step arrows had nearly identical
   start/end points. Re-anchored from the goal card's bottom edge
   `(xs[i], 2.0)` to each chip's top edge `(xs[i], 1.85)`. [record]
3. **B07 bar/card overlap (pre-QC).** The third error bar's base sat inside
   the wreck card. Shrunk it (2.6 → 2.2) and raised it (y −1.4 → −1.1) so
   the wreck card sits cleanly beneath the last bar. [record]

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 12 beats (10–16 band), 7 body beats (6–10 band), total 324 s
(3–6 min band), B00 names the voice ("Liam, in for Bear"), B09 restates
the three-rule framework (delegating only checkable work, approving the
irreversible, starting on low stakes), B10 carries the paste-into-your-AI
prompt.

## ai-explainer classification

8 SHOW / 4 justified-HOLD / 0 PUNT-flagged.
Body beats B02–B09 all classify SHOW: each names its on-screen artifact in
`shot.show`, ~15–35% negative space by construction (one idea per beat on
a cream stage), no comparison side that fades below ~40% opacity, and the
two comparisons (B02 chatbot-vs-agent chips; B03 node sequence) are held
on screen through their narration. B00/B01/B10/B11 are justified-HOLD:
ai-explainer bookend beats (the composer ask, the hesitant-writer BLUF,
the handoff composer, the locked title outro) — the Claude interface is
the subject there per ILLUSTRATE LAW's bookend exception. No beat passed
the card test; zero cards, all drawings. The PPT test: every body beat
animates its narration's argument (cards converging, the dot traveling
the loop, steps checking off, the hidden line flagged, the error bars
swelling, the counter climbing) — no slide-beats.

Teaching arc: FRAMEWORK ✓ (B04's three rules precede B05's example) |
WORKED EXAMPLE ✓ (B05 Saturday evening, approval gate before the booking)
| FALSIFIABILITY ✓ (B06's wrong-instructions failure mode and B07's
"catch it at step three" are checkable supervision claims) |
SCAFFOLDED TASK ✓ (B10's your-turn prompt walks the viewer through the
three rules on their own errand) | BOOKENDS ✓ (B00/B01 cold open+BLUF,
B09 verdict, B10 handoff, B11 outro) | NO-SOURCE-NO-VERDICT ✓ (B09's
verdict derives only from the episode's own claims).
