# CHECKS-REPORT.md — Learn Anything Faster

Date: 2026-10-03. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 5 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| B00_House | clean |
| B01_ExplainSimple | clean |
| B02_QuizMode | clean |
| B03_Socratic | clean |
| B04_YourTopic | clean |

## Pacing-phrase audit

All 14 `until()` phrases verified present verbatim in their beat's
`narration_text` (script-checked, 0 misses), so the narration clock is
real rather than silently skipped.

## Design-time guards applied (before the checker ran)

1. **Midpoint guard.** Every `play` was timed to finish before its
   beat's midpoint minus 0.3 s or start after the midpoint plus 0.3 s
   (GATE T samples each clip at its midpoint). The midpoint frame of
   every beat shows settled objects and settled labels, never a
   mid-flight animation.
2. **Membership changes.** Every scene spreads its FadeIn / Create /
   GrowFromCenter calls across multiple plays (never all in the first
   play), and every new shape stays on stage — no create-move-remove
   sequences.
3. **Labels.** All labels sit beside their objects (never inside an
   outline, never on terracotta), type floor 32, 1–3 words each; the
   "?" marks are content, not labels.
4. **Terracotta discipline.** Terracotta used only for dots, the lamp,
   and one check — never for text or bars.
5. **Stub-safe calls.** No `rate_functions.ease_in_quad` /
   `ease_out_cubic` (kit's `ease_in` available); no
   `mob.animate(path_arc=…)` (plain shifts and `MoveAlongPath` only);
   no `MoveAlongPath` + `.animate` on the same object in one play;
   `get_center()` results never subtracted without `np.array`.
6. **Hesitant-writer props.** `triggerWords` ("Give me the answer")
   appears verbatim in `text` and neither trigger nor replacement ends
   in punctuation.

## Skill-fit note

show-tell was the assigned skill and was kept: the film is a technique
explainer (three moves demonstrated on one topic), which maps exactly
onto show-tell's spine. The card test was applied per body beat and
failed everywhere — no beat's idea is an interface, a number set, or
one word — so the film uses zero cards (recorded in SHOTLIST.md).

## Deferred to Bear's Mac render pass

`manim_layout_audit.py --curve-strict` could not run in this VM (no
Manim/pangocairo installed). Bear runs it per scene class on the Mac
before the review cut — see CLAUDE-CODE-RENDER.md §2.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 9 beats, 5 body beats, total 200 s, BHTF reads the tutor
prompt in full, B04 states the moves transfer.
