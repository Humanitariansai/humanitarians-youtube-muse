# CHECKS-REPORT.md — Captions That Write Themselves

Date: 2026-10-05. Checker:
`runtime/qc/static_scene_check.py` (render-free, per-class mode), run
from a scratch folder holding ONLY `scenes.py` (+ `beat_sheet.json`
beside it, so `until()` pacing runs — exactly what `art run`'s Gate A
sees).
`python3 -m py_compile` clean on scenes.py and make_sheet.py.

## Result: 8 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| B00_PhoneVideo | clean |
| B01_WhatCaptions | clean |
| B02_ThePass | clean |
| B03_OpenIt | clean |
| B04_PressButton | clean |
| B05_CheckIt | clean |
| B06_TwoWays | clean |
| B07_WhoWatches | clean |

## Pacing-phrase audit

All 24 `until()` phrases verified present verbatim in their beat's
`narration_text` (script-checked, 0 misses), so the narration clock is
real rather than silently skipped.

## Design-time guards applied (before the checker ran)

1. **Midpoint guard.** Every `play` was timed to finish before its
   beat's midpoint minus 0.3 s or start after the midpoint plus 0.3 s
   (GATE T samples each clip at its midpoint / the 45–55% window). The
   midpoint frame of every beat shows settled objects and settled
   labels, never a mid-flight animation. Phrases for plays were chosen
   at character shares clear of the window (e.g. B04's line-2 play
   waits for "Then play it back", ~63%).
2. **Membership changes.** Every scene spreads its FadeIn / Create /
   GrowFromCenter calls across multiple plays (never all in the first
   play), and every new shape stays on stage — no create-move-remove
   sequences.
3. **Labels.** All labels sit beside their objects (never inside an
   outline, never on terracotta), type floor 32, 1–3 words each; the
   "captions" word on the tool button is the button's own UI text.
4. **Terracotta discipline.** Terracotta used only for timing ticks,
   the check stamps, the B06 choice dot, and the B05 underline — never
   for text or bars. B07's hero number "9 in 10" is ink (numerals are
   never terracotta).
5. **Stub-safe calls.** No `rate_functions.ease_in_quad` /
   `ease_out_cubic` (kit's `ease_in` available); no
   `mob.animate(path_arc=…)` (plain shifts and `MoveAlongPath` only);
   no `MoveAlongPath` + `.animate` on the same object in one play;
   `get_center()` results passed to `Line()`, never subtracted.
6. **Hesitant-writer props.** `triggerWords` ("type out") appears
   verbatim in `text` and neither trigger nor replacement ends in
   punctuation.
7. **Term lengths.** All three BDEFS terms are under the ~17-character
   `ClaudeDefinitions` truncation limit ("auto-captioning" = 16).
8. **Voice codes.** Every beat's `voice` is `am_onyx` (asserted in
   `make_sheet.py` — the Wave 5 "Muse"-as-voice failure is a generator
   assertion now, not just a convention).

## Skill-fit note

show-tell was the assigned skill and was kept: the film is a practical
walkthrough (four steps demonstrated on a phone-shot video), which
maps exactly onto show-tell's spine. The card test was applied per
body beat and failed everywhere — the B07 numbers are one attributed
figure carried better by bars and a hero number than by any card kind
— so the film uses zero cards (recorded in SHOTLIST.md).

## Deferred to Bear's Mac render pass

`manim_layout_audit.py --curve-strict` could not run in this VM (no
Manim/pangocairo installed). Bear runs it per scene class on the Mac
before the review cut — see CLAUDE-CODE-RENDER.md §2. Measured audio
still needs writing back to `actual_duration_s` after Kokoro voicing.

No checker warnings or errors were hidden or waived. beat_sheet.json
validates: 12 beats, 8 body beats, total 214.4 s, BHTF reads the
caption-check prompt in full, every beat voiced `am_onyx`.
