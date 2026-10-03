# CHECKS-REPORT.md — "Claude, Not Your Answer."

QC gate run 2026-10-03, before pushing. Requirement: 0 warnings and
0 errors on every scene class.

## 1. py_compile

```
python3 -m py_compile make_sheet.py scenes.py   -> clean (no output)
```

## 2. make_sheet.py self-assertions (run at generation)

- 13 beats, unique ids, BIDEA first / BOUT last
- every beat: non-empty narration, duration > 0, voice am_onyx, engine kokoro
- body beats exactly B00–B08, each with `shot.manim.class` matching the
  scenes.py class name (B00_ThePaste … B08_Enterprise)
- BIDEA: lead_silence_s 0.8; triggerWords in text; neither trigger nor
  replacement ends in punctuation
- BOUT: kind outro_voice, tail_silence_s 1.0
- BHTF topic contains "YOUR TURN"
- total estimated duration 186.4 s, inside the 150–240 s band
- result: all assertions passed

## 3. Static scene QC (manim-stub, render-free)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

| Class | Result |
|---|---|
| B00_ThePaste | clean · 0 warn · 0 error |
| B01_Samsung | clean · 0 warn · 0 error |
| B02_TheMechanism | clean · 0 warn · 0 error |
| B03_TheToggle | clean · 0 warn · 0 error |
| B04_Everywhere | clean · 0 warn · 0 error |
| B05_GoingForward | clean · 0 warn · 0 error |
| B06_Legal | clean · 0 warn · 0 error |
| B07_CleanRoom | clean · 0 warn · 0 error |
| B08_Enterprise | clean · 0 warn · 0 error |

**9 clean · 0 warn · 0 error, first run — no failures, no fixes.**

Pre-gate review notes (applied during writing, before the checker ran):
- All new shapes enter via Create / FadeIn / GrowFromCenter (never via
  `.animate()` alone), so the stub's scene graph sees them.
- `until()` phrases verified verbatim against each beat's narration_text.
- Coordinates held inside ±6.2 × ±3.3 (safe area); no explicit coord outside
  the hard frame.
- No `generic_art`, no `rate_functions.ease_in_quad`, no
  `animate(path_arc=...)`, no `Transform` of polygons.

## 4. Push verification

All 12 files pushed to
`muse/youtube/how-to-use-ai/claude-not-your-answer/` on
Humanitariansai/humanitarians-youtube-muse and re-read via the Contents API
(HTTP 200 each). No MP3/MP4/WAV/`.pyc`/`__pycache__`/`.DS_Store` committed;
no tokens, secrets, emails, or personal information in any file.
