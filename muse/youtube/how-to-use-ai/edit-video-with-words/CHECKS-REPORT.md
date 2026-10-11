# CHECKS-REPORT.md — Edit video with words

## Static gate (Gate A pre-audit)

`runtime/qc/static_scene_check.py scenes.py --class <C>`, run 2026-10-07
from a scratch folder holding only `scenes.py` + `beat_sheet.json` (what
Gate A sees):

- B00_HeroChat: clean (4 distinct shape states)
- B01_TenHours: clean (5)
- B02_Announced: clean (3)
- B03_Demo: clean (4)
- B04_Fiddly: clean (6)
- B05_YourHands: clean (4)
- B06_Early2027: clean (2)
- B07_MetaShips: clean (4)
- B08_TheLine: clean (4)
- B09_Today: clean (4) — one safe-area warning fixed (clip row ran to
  x=6.9; re-centered to -1.225..5.025), re-run clean.

**10/10 clean · 0 warnings · 0 errors.**

`manim_layout_audit.py --curve-strict` NOT run (no pangocairo in this VM)
— Bear's Mac runs it per CLAUDE-CODE-RENDER.md before the review cut.

## PROOF GATE (per-beat SHOW / HOLD / CARD)

All 10 body beats classify SHOW: each beat's drawing is the beat's claim
in motion (chat reorders clips; clock spins 1h→10h; takes are picked;
gaps shrink; cursor drags; bars feed the bubble; chips fan; clips
auto-arrange). No HOLD beats. No CARD beats (no beat passed the card
test — see SHOTLIST.md). No punts: every beat has a runner-up recorded.

## Teaching arc

Question (BIDEA) → terms (BDEFS) → the idea, drawn (B00) → why it matters
(B01) → YouTube's announcement, demo, capabilities, control, timing
(B02–B06) → the other player + the line (B07–B08) → start today (B09) →
Your Turn (BHTF) → outro (BOUT). One idea per beat; no recaps; nothing
repeated to fill.

## Lane histogram

10 Manim · 4 Remotion bookends (slated in the VM cut; rendered on the
Mac). Sparse-by-design declared on all 14 beats with reasons.
