# CHECKS-REPORT.md — Claude, Allowed.

QC gate run 2026-10-03, package dir `~/workspace/film-builds/how-to-use-ai/claude-allowed/`.

## 1. py_compile

```
python3 -m py_compile make_sheet.py scenes.py
```
Result: **clean** (exit 0, no output). No failures.

## 2. Static scene QC

```
python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py scenes.py --class <C>
```

| Class | Result |
|-------|--------|
| `B00_PolicyPage` | clean · 0 warn · 0 error |
| `B01_Scope` | clean · 0 warn · 0 error |
| `B02_Trap` | clean · 0 warn · 0 error |
| `B03_Fluency` | clean · 0 warn · 0 error |
| `B04_Predict` | clean · 0 warn · 0 error |
| `B05_Reveal` | clean · 0 warn · 0 error |

**6/6 scenes: 0 warnings, 0 errors.** First run — nothing to fix, nothing concealed.
(Verified separately that `beat_sheet.json` sits next to `scenes.py` so the kit's
`until()`/`finish()` pacing resolves; every `until()` phrase was checked verbatim
against its beat's `narration_text`.)

## 3. make_sheet.py asserts

- beat ids exactly `["BIDEA","BDEFS","B00","B01","B02","B03","B04","B05","BHTF","BOUT"]` ✓
- 6 Manim body beats; each `shot.manim.class` starts with its beat id ✓
- total estimated duration 170.0 s inside the 120–240 s band ✓
- `bookend_exempt == ["cold-open","bvdt"]` ✓

## 4. GitHub push verification

All 12 files pushed with `gh-put-file.py` to
`Humanitariansai/humanitarians-youtube-muse` under
`muse/youtube/how-to-use-ai/claude-allowed/`, then each re-read via the Contents API
(HTTP 200). See the push table in the final report. No MP3/MP4/WAV/`.pyc`/
`__pycache__`/`.DS_Store` anywhere in the package; no secrets, tokens, emails, or
personal information in any film file.

## Not covered by pre-render QC (for Bear's render step)

- GATE T midpoint sampling, Gate V contrast/fill, `manim_layout_audit.py` — need real frames.
- Kokoro `am_onyx` pronunciation of the narration (whisper-check BIDEA/BHTF in particular).
- Measured audio durations → write back to `actual_duration_s` before `art run`.
