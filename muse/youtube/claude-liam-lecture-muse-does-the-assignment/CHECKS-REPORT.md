# CHECKS-REPORT.md — Muse Does the Assignment

Date: 2026-10-06. Checker: `runtime/qc/static_scene_check.py`
(render-free, per-class mode).

## Result: 14 clean · 0 warnings · 0 errors

| Scene | Result |
|-------|--------|
| B01_Grid | clean |
| B02_Rules | clean |
| B03_Example | clean |
| B04_Legs | clean |
| B05_Order | clean |
| B06_Twelve | clean |
| B07_States | clean |
| B08_Crosscheck | clean |
| B09_Greedy | clean |
| B10_Trap | clean |
| B11_Wall | clean |
| B12_Rule | clean |
| B13_SixVsTwelve | clean |
| B14_Fixes | clean |

## PROOF GATE (SHOW / HOLD / CARD)

14 body beats SHOW (Manim, motion carries the claim in every beat);
5 bookends: BIDEA SHOW (hesitant-writer pattern), BDEFS CARD (terms card),
BVDT CARD (verdict card), BHTF SHOW (composer pattern), BOUT SHOW (locked
outro). No HOLDs. In this VM the 5 Remotion bookends compile as labeled
slates; Bear's Mac renders the real patterns.

## Teaching-arc checklist

- Every body beat's motion lands on its spoken point (verified against the
  `show` event lists in beat_sheet.json).
- No beat repeats another's visual: 6 grid-walk variants are distinguished
  by purpose (legend / rules / mystery / legs / optimum / greedy / trap /
  6-vs-12), plus lattice, layers, terminal, curve, decision card, checklist.
- Terms are defined before use (BDEFS) or at first use (traveling
  salesperson, B05). Nothing references outside films or books.

## Deferred to the Mac

`manim_layout_audit.py --curve-strict` (needs pangocairo) — run per class
before the review cut; the render prompt lists the exact commands.
