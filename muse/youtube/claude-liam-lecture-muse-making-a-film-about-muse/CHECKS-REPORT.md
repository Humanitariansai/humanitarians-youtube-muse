# CHECKS-REPORT.md — "Muse making a film about Muse"

## PROOF GATE (before first compile)

- Body beats: 17 SHOW · 0 HOLD · 0 CARD.
- Bookends: BIDEA SHOW (hesitant writer), BDEFS CARD (terms card),
  BVDT SHOW (recap artifact), BHTF SHOW (composer ask), BOUT SHOW (outro).
- Teaching arc: the film answers its title in order — what Muse is
  (Act I) → what it does (Act II) → where you reach it (Act III) →
  how it's paid for (Act IV) → recap → your turn. Each act's claim is
  carried by motion, not type. No beat repeats another's idea.

## Lane histogram (information, not a quota)

Manim diagram ×11, Manim lesson ×3, Manim chart ×2, Manim misc ×1.
Every pick won on motion-carries-the-claim (see SHOTLIST.md).

## Static gates (run on the build VM)

- `python3 -m py_compile scenes.py`: OK.
- `static_scene_check.py` per class: 17/17 clean, 0 warnings, 0 errors.

## Gates not yet run (need Bear's Mac)

- Audio generation (Kokoro) + measured durations.
- `./art run` review cut (Gates A, B, W, V, T on rendered frames).
- `./art final` 4K master + bookend check.
