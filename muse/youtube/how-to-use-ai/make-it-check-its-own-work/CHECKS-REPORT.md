# CHECKS-REPORT.md — "Make It Check Its Own Work."

QC gate run 2026-10-03, before pushing. Requirement: 0 warnings and
0 errors on every scene class.

## 1. py_compile

```
python3 -m py_compile make_sheet.py scenes.py   -> clean (no output)
```

## 2. make_sheet.py self-assertions (run at generation)

- 13 beats, unique ids, BIDEA first / BOUT last
- every beat: non-empty narration, duration > 0, voice am_onyx, engine kokoro, non-empty `shot.show`
- body beats exactly B00–B08, each with `shot.manim.class` matching the scenes.py class name
- BIDEA: lead_silence_s 0.8; triggerWords verbatim in text
- BHTF topic contains "YOUR TURN"
- BOUT: kind outro_voice, tail_silence_s 1.0
- total estimated duration 190.4 s, inside the 150–240 s band
- result: all assertions passed

## 3. Static scene QC (manim-stub, render-free)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

**First run:** 6 clean, 3 errored — B05_WhereItPays, B06_TheLimit,
B07_ProMove all raised `TypeError: lab() got an unexpected keyword argument
'bold'`. Root cause: my `lab()` helper didn't forward `bold` to `T()`.
Fix: `lab(s, x, y, size=34, color=INK, bold=False)` now passes
`bold=bold` through. One-line fix, no design change.

**Second run:**

| Class | Result |
|---|---|
| B00_TheSecondLook | clean · 0 warn · 0 error |
| B01_ThreeQuestions | clean · 0 warn · 0 error |
| B02_TheTrap | clean · 0 warn · 0 error |
| B03_TheCatch | clean · 0 warn · 0 error |
| B04_TheEmail | clean · 0 warn · 0 error |
| B05_WhereItPays | clean · 0 warn · 0 error |
| B06_TheLimit | clean · 0 warn · 0 error |
| B07_ProMove | clean · 0 warn · 0 error |
| B08_TheHabit | clean · 0 warn · 0 error |

**9 clean · 0 warn · 0 error.**

Pre-gate review notes (applied during writing, before the checker ran):
- All new shapes enter via Create / FadeIn / GrowFromCenter (never via
  `.animate()` alone), so the stub's scene graph sees them; `.animate()`
  is used only to move shapes already on screen.
- Every `until()` phrase verified verbatim against its beat's
  `narration_text` (scripted check, all passed).
- Coordinates held inside ±6.2 × ±3.3 (safe area); no explicit coord outside
  the hard frame. One terracotta moment at a time (B02's February glow is
  faded out before the X lands).
- No `generic_art`; labels sit beside objects; no text on terracotta fill.

## 4. Push verification

All 12 files pushed to
`muse/youtube/how-to-use-ai/make-it-check-its-own-work/` on
Humanitariansai/humanitarians-youtube-muse and re-read via the Contents API
(HTTP 200 each). No MP3/MP4/WAV/`.pyc`/`__pycache__`/`.DS_Store` committed;
no tokens, secrets, emails, or personal information in any file.
