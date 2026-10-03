# CHECKS-REPORT.md — "Claude making a film about Muse"

Run on Muse's Linux VM, 2026-10-03.

## Static gates (local)

| Check | Result |
|---|---|
| `python3 -m py_compile scenes.py make_sheet.py` | pass |
| `static_scene_check.py` — all 23 classes (M01–M23) | **23 clean, 0 warnings, 0 errors** |
| beat_id ↔ class-name match (B01↔M01 … B23↔M23) | all match |
| `beat_sheet.json` parses; 28 beats; unique manim classes | pass |

## Fixes during the build

- M04: stub `get_x()` returns a mobject, not a float — rewrote tick
  coordinates from known row positions.
- M17: tag string reached y=4.4 (outside frame) — lowered the assembly;
  then a safe-area warning at y=3.9 — lowered again, now inside 3.4.
- M07, M23: text-only scenes warned — added column cards (M07) and
  question badges (M23); both now record shapes.

## Not run here (Bear's Mac)

- Kokoro narration audio (MP3s) — Claude Code step 2.
- `./art run` review cut and gate suite — Claude Code step 3.
- `./art final` 4K master — Claude Code step 5.
- `bookend_check.py` — Claude Code step 6.

MP3s and MP4s are git-ignored and never committed.
