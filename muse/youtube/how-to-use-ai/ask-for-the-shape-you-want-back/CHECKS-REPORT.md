# CHECKS-REPORT.md — "Ask for the Shape You Want Back"

## Static QC (2026-10-03)

- `python3 -m py_compile make_sheet.py scenes.py` — clean.
- `~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`,
  run for every scene class with `beat_sheet.json` beside `scenes.py` (so `until()` /
  `finish()` pacing executed against the real sheet):

| class | result |
|---|---|
| B00_BlocksBox | clean · 0 warn · 0 error |
| B01_BuriedInProse | clean · 0 warn · 0 error |
| B02_AskForATable | clean · 0 warn · 0 error |
| B03_GiveItASize | clean · 0 warn · 0 error |
| B04_PickTheTone | clean · 0 warn · 0 error |
| B05_MatchTheDestination | clean · 0 warn · 0 error |
| B06_Prefill | clean · 0 warn · 0 error |
| B07_CheckTheFacts | clean · 0 warn · 0 error |
| B08_ThenStop | clean · 0 warn · 0 error |

Totals: **9 clean · 0 warn · 0 error.**

## Failures found and fixed (not concealed)

1. B03 first draft: `lower = VGroup(page[1][4:], page[2])` — the kit page only has
   3 text lines, so the slice was empty and the "lower half falls away" moment would
   have removed just the dot. Fixed by building the page with 9 explicit lines split
   into `upper`/`lower` groups before the checker ran.
2. B02/B07 first draft: header bands at full card width, poking past the rounded
   card corners (GATE T reads dark bands inside ink-outlined cards as overlapping
   labels). Fixed by insetting bands to 5.9 / 5.2 units; both bands are BAR1 grey,
   never dark.

## Not run (deferred)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict`: cannot run
  in this VM (no Manim/pangocairo installed). Deferred to Bear's Mac render pass —
  see CLAUDE-CODE-RENDER.md. The drawings follow the kit's drawing laws (labels
  beside objects, ≥38pt, inside ±6.3×±3.4, sparse_by_design waivers on all 9 body
  beats), but the audit is the real check and must run before 4K.
