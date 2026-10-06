# Muse Does the Assignment

Lecture film (skill: `lecture`) for INFO 6205 Program Structure and
Algorithms. Liam, in for Bear (Kokoro `am_onyx`, Teardown register,
@NikBearBrown).

**Premise:** Bear hands Muse the Week 1 assignment — "Help Beary Navigate
the Forest to Collect Honey" — with the instruction: do your best work, and
check the assignment itself for errors. The film follows Muse solving the
pathfinding problem three ways (bitmask DP, state-space BFS, greedy
nearest-honey), teaches when to pick which, and closes on the twist: Muse
found four defects in the assignment, including a wrong example answer
(stated 6, correct 12).

**Course credit:** INFO 6205 named in BIDEA; `metadata.course` set. The
companion work (reference solution, tests, audit, both notebooks) lives in
the `Coursera Info 6205 Algorithms` folder of this repo.

| File | What it is |
|------|------------|
| ACTS.md | Act structure, coverage map, cast per act, BIDEA/BDEFS notes |
| SHOTLIST.md | Per-beat lane auditions with runner-ups |
| FACTCHECK.md | 14 claim rows, all PASS, with sources and fixes |
| SOURCES.md | Fact → source table |
| PROMPTS.md | "No generation prompts" |
| make_sheet.py | Generates `beat_sheet.json`; asserts 19 beats / 14 Manim |
| beat_sheet.json | The sheet: 19 beats with narration and shot notes |
| scenes.py | 14 Manim scene classes (B01–B14) + Grid/checkmark helpers |
| BUILD-LOG.md | Dated build steps, including QC failures and fixes |
| CHECKS-REPORT.md | Static gate: 14 clean · 0 warnings · 0 errors; PROOF GATE |
| CLAUDE-CODE-RENDER.md | Render instructions for Bear's Mac |
| README.md | This file |

## Status

Pre-render package + VM slate cut. The 5 Remotion bookends are labeled
slates in the slate cut (Remotion can't render in the build VM); Bear's Mac
renders the real ones per CLAUDE-CODE-RENDER.md. Never render, publish,
upload, or stage anything for publication without Bear's explicit
instruction. No audio, video, or cache files are committed.
