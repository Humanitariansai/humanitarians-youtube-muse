# CHECKS-REPORT.md — Say what you want, plainly

QC gate: `python3 -m py_compile` clean on `make_sheet.py` and `scenes.py`,
then `runtime/qc/static_scene_check.py scenes.py --class <ClassName>` for
every scene class. Required: 0 warnings, 0 errors. (2026-10-03)

## Final result — 8/8 clean, 0 warnings, 0 errors

| Scene class | With `beat_sheet.json` beside `scenes.py` | Scratch folder, `scenes.py` only (what Gate A sees) |
|---|---|---|
| `B00_PromptSlip` | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| `B01_Guesses` | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| `B02_MostCommon` | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| `B03_TheFix` | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| `B04_FourQuestions` | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| `B05_NewHire` | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| `B06_BriefRewrite` | clean · 0 warn · 0 error | clean · 0 warn · 0 error |
| `B07_Compare` | clean · 0 warn · 0 error | clean · 0 warn · 0 error |

`make_sheet.py` assertions also pass: 12 beats, 8 manim, all voices
`am_onyx`, every manim class name starts with its beat id, no audio file
referenced, total estimated duration 195.2 s (within 120–300 s).

## Failures and fixes (nothing concealed)

1. **Run 1 — `AttributeError: no attribute 'until'` on all 8 classes.**
   The kit's `iso_kit.py` defines `until`/`finish` as plain module-level
   functions; scenes call them as `self.until(...)`. Fixed by attaching
   them in `scenes_body.py`: `Scene.until = until` / `Scene.finish = finish`.
2. **Run 2 — `B04_FourQuestions`: "shapes never change — 1 distinct
   shape-state across 13 frames".** Two stacked causes, fixed in order:
   - (a) the Gate A stub does not track `RoundedRectangle` in shape
     signatures at all; the `_chip` helper was changed to plain `Rectangle`.
     Still failed, because —
   - (b) the real cause: `chip.animate.shift(...)` is move-only and the
     stub's `_apply_anim` changes scene membership only for `_ADD` /
     `_REMOVE` / `_REPLACE` animation kinds, so the chips never entered
     `scene.mobjects` in any snapshot. Worse, this pattern would also
     leave the objects un-added in a real Manim render.
   - Fix: every drop/rise now uses `FadeIn(x, shift=...)` (B00 slip,
     B03 slip, B04 chips, B05 chips, B05 page). Run 3: 8/8 clean in both
     modes.

## Deferred (not run in this VM)

- `manim_layout_audit.py --curve-strict`: needs Manim + pangocairo, which
  this VM lacks. Deferred to Bear's Mac render pass (noted in
  `CLAUDE-CODE-RENDER.md`).
- Real Manim render, Kokoro audio, whisper transcript check, GATE T/V —
  all render-time steps on Bear's Mac.
