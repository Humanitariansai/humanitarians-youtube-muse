# CHECKS-REPORT.md — "The yes-man problem."

## Static QC (2026-10-04)

- `python3 -m py_compile make_sheet.py scenes.py` — clean.
- `~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`,
  run for every Manim scene class with `beat_sheet.json` beside `scenes.py`
  (so `until()` / `finish()` pacing executed against the real sheet).
  Bookend beats (BIDEA/BDEFS/BHTF/BOUT) are REMOTION and have no Manim class.

| class | result |
|---|---|
| B00_YesMan | clean · 0 warn · 0 error |
| B01_Mirror | clean · 0 warn · 0 error |
| B02_FiveModels | clean · 0 warn · 0 error |
| B03_ThumbsUpSchool | clean · 0 warn · 0 error |
| B04_PermissionToDisagree | clean · 0 warn · 0 error |
| B05_AskBeforeTell | clean · 0 warn · 0 error |
| B06_Steelman | clean · 0 warn · 0 error |
| B07_JudgeTheIdea | clean · 0 warn · 0 error |
| B08_PlaybookPass | clean · 0 warn · 0 error |

Totals: **9 clean · 0 warn · 0 error.**

## make_sheet.py assertions (all pass)

- 13 beats; band 13–22 ✓
- `BIDEA` / `BDEFS` bookends first; `BHTF` / `BOUT` last ✓
- 9 GRAPHIC body beats (`B00`–`B08`), 4 REMOTION bookends ✓
- every Manim class named `<BID>_<Name>`, all unique ✓
- IN-FOR-BEAR: "Liam, in for Bear" in BIDEA narration ✓
- BHTF: greeting "Your turn."; narration names "Paste this into Claude" ✓
- BOUT: "At Nik Bear Brown" in narration ✓
- total estimated runtime 273.1s (~4m33s), inside the 270–420s band ✓

## Failures found and fixed (not concealed)

None — all 9 scene classes passed the static gate on the first run.
Two layout hazards were caught by hand before the check ran and are
recorded here rather than concealed:

1. B08 first draft laid the three request chips in one row at fs=26 —
   the "honest bottom line" chip would have run past the ±6.3 safe
   area. Reworked to a two-row cluster (two chips at y=2.5, one at
   y=1.35) at fs=22, all inside safe.
2. Three terracotta tag lines ("five assistants, four tasks — same
   habit", "spring 2025 — rolled back", "grade the idea — not your
   feelings") exceeded the safe width at 32pt. Shortened/re-centered
   ("five assistants — same habit"; "spring 2025: rolled back" at
   28pt, x=1.2; "grade the idea") — all spoken words, all inside safe.

## Not run (deferred)

- `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict`: cannot run
  in this VM (no Manim/pangocairo installed). Deferred to Bear's Mac render pass —
  see CLAUDE-CODE-RENDER.md. The drawings follow the kit's drawing laws (labels
  beside objects, ≥30pt, inside ±6.3×±3.4, sparse_by_design waivers on all 13 beats),
  so the audit is expected to be a formality, not a rescue.
