# CHECKS-REPORT.md — "The Second Opinion"

QC gate run 2026-10-04, before pushing. Requirement: 0 warnings and
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
- BDEFS: durationSeconds (21.2) matches narration estimate
- BHTF topic contains "YOUR TURN"; the prompt is read verbatim in narration
- BOUT: kind outro_voice, tail_silence_s 1.0
- total estimated duration 238.4 s, inside the 150–240 s band
- result: all assertions passed (one fix during authoring: BDEFS
  durationSeconds corrected 22.0 → 21.2 to match the word count)

## 3. Static scene QC (manim-stub, render-free)

`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>`

**First run:** 8 clean, 1 errored — B07_ProMove raised
`NameError: name 'flag' is not defined`. Root cause: my film-helpers draft
didn't carry the `flag()` helper over (it lived in the companion's film
helpers, not in iso_kit). Fix: added the `flag()` definition to scenes.py.
No design change.

**Verbatim-until check (scripted):** one case mismatch —
`until(self, "Steelman the opposite case")` vs the narration's lowercase
"steelman the opposite case" (the check is case-sensitive; the wait would
have silently no-op'd). Fixed the phrase to lowercase. Re-ran: all
until() phrases verbatim in their beats' narration_text.

**Second run:**

| Class | Result |
|---|---|
| B00_TheMove | clean · 0 warn · 0 error |
| B01_TwoRoutes | clean · 0 warn · 0 error |
| B02_FirstAnswer | clean · 0 warn · 0 error |
| B03_TheSteelman | clean · 0 warn · 0 error |
| B04_BothSides | clean · 0 warn · 0 error |
| B05_WhereItPays | clean · 0 warn · 0 error |
| B06_TheLimit | clean · 0 warn · 0 error |
| B07_ProMove | clean · 0 warn · 0 error |
| B08_TheHabit | clean · 0 warn · 0 error |

**9 clean · 0 warn · 0 error.**

Pre-gate review notes (applied during writing, before the checker ran):
- All new shapes enter via Create / FadeIn / GrowFromCenter (never via
  `.animate()` alone), so the stub's scene graph sees them; `.animate()` is
  not used at all in this film.
- Every `until()` phrase verified verbatim against its beat's
  `narration_text` (scripted check, all passed).
- Coordinates held inside ±6.2 × ±3.3 (safe area); no explicit coord outside
  the hard frame. One terracotta moment at a time (B06's shopping-row glow
  is faded out before the X lands).
- No `generic_art`; labels sit beside objects; no text on terracotta fill.

## 4. Push verification

All 12 files pushed to
`muse/youtube/how-to-use-ai/the-second-opinion/` on
Humanitariansai/humanitarians-youtube-muse and re-read via the Contents API
(HTTP 200 each). No MP3/MP4/WAV/`.pyc`/`__pycache__`/`.DS_Store` committed;
no tokens, secrets, emails, or personal information in any file.
