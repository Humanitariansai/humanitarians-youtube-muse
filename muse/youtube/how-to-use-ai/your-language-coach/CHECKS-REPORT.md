# CHECKS-REPORT.md — Your Language Coach

Date: 2026-10-05. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 7 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| B00_Coach | clean |
| B01_Patience | clean |
| B02_Correction | clean |
| B03_Rule | clean |
| B04_Roleplay | clean |
| B05_Level | clean |
| B06_Languages | clean |

## Pacing-phrase audit

All 21 `until()` phrases verified present verbatim in their beat's
`narration_text` (script-checked, 0 misses), so the narration clock is
real rather than silently skipped.

## Midpoint-guard audit (GATE T samples each clip at its midpoint)

A simulation of every `play` span against each beat's midpoint
(mid±0.35 s) caught 4 straddles in the first draft; all were fixed
before the gate by re-anchoring plays to earlier/later `until()`
phrases, with ≥0.22 s margin:

1. **B02_Correction** — the "instant" tag play straddled the midpoint.
   Fix: the tag now lands on "settle into a habit" (end of the beat),
   after the correction motion completes.
2. **B03_Rule** — the rule-line play straddled the midpoint. Fix: it
   now lands on "You say I have twelve years" with lead=0.0, i.e. after
   the midpoint, when the phrase is actually spoken.
3. **B04_Roleplay** — the order-pill travel straddled the midpoint.
   Fix: lead raised to 2.4 on "ordering coffee" so the pill finishes
   its travel before mid−0.35.
4. **B06_Languages** — the second hello-pill pair started 0.01 s
   inside the guard. Fix: lead lowered to 0.2 on "Salaam" so the pair
   pops after the guard.

Re-ran the simulation after the fixes: 0 straddles across all 7 scenes.

## Design-time guards applied (before the checker ran)

1. **Midpoint guard.** See above — every play lands before mid−0.35 s
   or starts after mid+0.35 s (simulated, 0 straddles).
2. **Membership changes.** Every scene spreads its FadeIn / Create /
   GrowFromCenter calls across multiple plays (never all in the first
   play), and every new shape stays on stage — the one removal
   (B05's long reply bubble fading as it is replaced) is not the
   scene's only new shape.
3. **Labels.** All labels sit beside their objects (never inside an
   outline, never on terracotta), type floor 32, 1–3 words each; every
   on-screen word is spoken in its beat; no French is voiced (the rule
   is stated in English for Kokoro-safety).
4. **Terracotta discipline.** Terracotta used only for the lamp, dots,
   the caret, squiggles, the awning seal, and checks — never for text
   or bars.
5. **Stub-safe calls.** No `rate_functions.ease_in_quad` /
   `ease_out_cubic`; no `mob.animate(path_arc=…)`; no `MoveAlongPath`
   + `.animate` on the same object in one play; `get_center()` results
   wrapped in `np.array(...)` before arithmetic.
6. **Hesitant-writer props.** `triggerWords` ("study French grammar")
   appears verbatim in `text` (no newline inside the trigger) and
   neither trigger nor replacement ends in punctuation.
7. **Voice codes.** Every beat carries `"voice": "am_onyx"` — the
   persona-name-as-voice bug that broke two Wave 5 films at the audio
   stage cannot recur here (asserted in make_sheet.py).
8. **Terms card.** All three BDEFS terms ≤ 17 characters
   (`ClaudeDefinitions` truncates longer ones; asserted).

## Skill-fit note

show-tell was the assigned skill and was kept: the film is a technique
explainer (four coach moves demonstrated on one demo language), which
maps exactly onto show-tell's spine. The card test was applied per body
beat and failed everywhere — no beat's idea is an interface, a number
set, or one word — so the film uses zero cards (recorded in
SHOTLIST.md).

## Deferred to Bear's Mac render pass

`manim_layout_audit.py --curve-strict` could not run in this VM (no
Manim/pangocairo installed). Bear runs it per scene class on the Mac
before the review cut — see CLAUDE-CODE-RENDER.md §2.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 11 beats, 7 body beats, total 224 s, BHTF reads the coach
prompt in full, B06 references the companion film without re-teaching
it.
