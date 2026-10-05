# CHECKS-REPORT — Your song in a minute

QC gate per the show-tell skill, run 2026-10-05 in this VM.

## Gate 1 — py_compile

`python3 -m py_compile make_sheet.py scenes.py` — clean, no output.

## Gate 2 — static_scene_check.py (per scene class)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`
run with `beat_sheet.json` beside `scenes.py` (as Gate A sees it).

| Scene class | Result | Warnings | Errors |
|---|---|---|---|
| B00_BirthdaySong | clean | 0 | 0 |
| B01_HowItWorks | clean | 0 | 0 |
| B02_ThreeIngredients | clean | 0 | 0 |
| B03_ListenFirst | clean (after fix) | 0 | 0 |
| B04_TheLoop | clean | 0 | 0 |
| B05_SweetSpot | clean | 0 | 0 |
| B06_KeepItShort | clean | 0 | 0 |
| B07_WhyNow | clean | 0 | 0 |

Total: 8 clean · 0 warnings · 0 errors.

### Failures found and fixed (nothing concealed)

1. **B03_ListenFirst — "shapes never change" (first run).** The playhead
   sweep uses `MoveAlongPath`, which is move-only; Gate A's stub snapshots
   only after each `play` and ignores moves, so the scene read as a repeated
   animation. Fix per the skill's documented pattern: the playhead now joins
   the opening `FadeIn` (so it is on screen from the start), and after the
   sweep a terracotta ring `GrowFromCenter`s on the play pill and then
   `FadeOut`s — a membership change after the first play. Re-ran: clean.

## Deferred (cannot run in this VM — no Manim/pangocairo)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict`
  (GATE T layout audit). Deferred to Bear's Mac render pass per
  CLAUDE-CODE-RENDER.md.
- Full `art run` / `art final` Gates A, B, V, T. Deferred to Bear's Mac.

## Design notes for the render pass

- Every scene keys all motion to narration phrases inside the first ~35% of
  the beat via `until()`, so no animation is mid-flight at the clip midpoint
  under real (shorter-than-estimate) Kokoro audio. Estimated durations use the
  house `words/2.5` convention and are deliberately conservative; the measured
  audio sets the real clock.
- Late payoffs (B02's banner ~54%, B03's label ~88%, B04's fix ~71%, B06's
  "under three minutes" ~68%) all start motion well clear of the midpoint
  margin window; verified in SHOTLIST.
- B07's curve is drawn in ink with `Create()` and a terracotta end dot (per
  the skill: never a half-drawn terracotta curve); the hero "44%" is ink,
  never terracotta text.
- B06's wandering track is also ink with `Create()` (a decaying-amplitude
  sine) — no terracotta mid-draw; the cross marks the fizzle.
- B03's playhead uses `MoveAlongPath` alone (never `.animate` on the same
  object in one play).
- B05's three song cards land in one `AnimationGroup` with lag (all motion
  before ~20% of the beat); B02's three tags drop on their spoken ingredient
  phrases, each a short 0.5 s play ending clear of the midpoint window.
- B04's fixed card swaps the draft via `FadeOut(draft, dlab)` + `FadeIn(fixed)`
  in one play (different objects — no animate-plus-another trap).
- `make_sheet.py` asserts every beat's `voice == "am_onyx"` (the Wave 5
  invalid-voice bug cannot recur).
