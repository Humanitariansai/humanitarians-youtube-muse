# CHECKS-REPORT.md — "Claude, When Not."

QC gate per the film-builder task: `python3 -m py_compile` clean on
`make_sheet.py` and `scenes.py`, plus
`python3 ~/workspace/brutalist.art/runtime/qc/static_scene_check.py
scenes.py --class <ClassName>` for every scene class, requiring 0 warnings
and 0 errors.

## Gate 1 — py_compile

- `make_sheet.py`: clean.
- `scenes.py`: clean (after the B08 card-position fix; the fix was
  coordinate-only, no syntax change).

## Gate 2 — static scene check (13/13 classes)

| Class | Result |
|---|---|
| BIDEA_HesitantWriter | 1 clean · 0 warn · 0 error |
| BDEFS_Terms | 1 clean · 0 warn · 0 error |
| B01_Thesis | 1 clean · 0 warn · 0 error |
| B02_UseList | 1 clean · 0 warn · 0 error |
| B03_DontList | 1 clean · 0 warn · 0 error |
| B04_HideTest | 1 clean · 0 warn · 0 error |
| B05_DraftExample | 1 clean · 0 warn · 0 error |
| B06_Verify | 1 clean · 0 warn · 0 error |
| B07_Predict | 1 clean · 0 warn · 0 error |
| B08_Answer | 1 clean · 0 warn · 0 error (after fix below) |
| B09_Line | 1 clean · 0 warn · 0 error |
| BHTF_YourTurn | 1 clean · 0 warn · 0 error |
| BOUT_Outro | 1 clean · 0 warn · 0 error |

## Failure and fix

- **B08_Answer — 1 error on first run:** "6 explicit coord(s) outside the
  frame, e.g. (7.2, 0.9) in move_to." Cause: the four option cards were laid
  out at x = -1.5 + i*2.9 with width 2.6, so card D's right edge reached 8.5,
  past the ±7.12 hard frame bound. Fix: x = -4.35 + i*2.9 (card edges at
  ±5.65, inside the ±6.2 safe area). Re-ran: 1 clean · 0 warn · 0 error.
- Also pre-empted before QC: the BHTF composer header band overlapped the
  window's top edge; repositioned to y=1.925 (see BUILD-LOG.md).

## Gate 3 — make_sheet.py assertions

- 13 beats, unique beat ids, every scene class name starts with its beat id.
- BIDEA narration starts with "Hallo." and contains "Liam, in for Bear".
- Total 244 s, inside the 170–260 s assertion band.

**Gate status: PASS — 13 clean · 0 warn · 0 error.**
