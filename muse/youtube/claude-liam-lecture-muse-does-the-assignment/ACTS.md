# ACTS.md — Muse Does the Assignment

Lecture film (skill: `lecture`) for INFO 6205 Program Structure and Algorithms.
Source: the Week 1 assignment notebook "Help Beary Navigate the Forest to
Collect Honey" (uploaded 2026-10-06), Muse's three-approach reference solution
(`solution.py`, `test_solution.py` — 25 tests, all passing), and the
independent assignment audit (`ASSIGNMENT-REVIEW.md`, 4 findings).

Premise: Bear hands Muse the assignment with the instruction "do your best
work, and check the assignment itself for errors." The film follows Muse
doing the assignment three ways, teaches when to pick which approach, and
closes on the twist: Muse found four defects in the assignment — including a
wrong example answer.

## Coverage map

| Source section | Act | Notes |
|---|---|---|
| Assignment: objective, grid legend (B/H/O/.), function signature | Act I (B01–B02) | The grid, the four rules, the -1 case |
| Assignment: constraints (50×50, ≥1 B, ≥1 H) | Act I (B02), Act VI (B14) | Constraints stated in B02; "always valid path" vs -1 revisited as a defect in B14 |
| Assignment: example grid + expected output 6 | Act I (B03), Act VI (B13) | B03 plants the "6" as a Chekhov's number; B13 resolves it (6 = no-return tour, 12 = correct) |
| Assignment: grading criterion 2 (BFS for shortest path) | Act II (B04) | BFS legs → distance table |
| Reference solution: pairwise BFS + Held–Karp bitmask DP | Act II (B04–B06) | Legs, ordering as TSP, the 12-step optimum |
| Reference solution: state-space BFS over (cell, mask) | Act III (B07–B08) | The obviously-correct search; 300-grid fuzz agreement; verbatim test output |
| Reference solution: greedy nearest-honey heuristic | Act IV (B09–B10) | The tempting approach; the 10-vs-8 counterexample |
| Tradeoff analysis (why pick one over another) | Act V (B11–B12) | NP-hardness, the 2^K wall, the rule of thumb |
| Assignment audit: 4 findings | Act VI (B13–B14) | The wrong example, the -1 contradiction, unstated diagonals, "at least one B" |
| Submission instructions ("submit the .ipynb on Canvas") | LEFT OUT | Course logistics, teaches nothing on film |

No act reorder: the source's own order (spec → example → solution approaches →
audit) is already the film's narrative order.

## Cast per act (ONE CAST PER ACT)

- The 3×3 example grid (B top-left terracotta, H ink, O dim grey) recurs in
  Acts I, II, VI — same cell size, same marks, same colors throughout.
- The 4×4 greedy-trap grid recurs in Act IV (B09–B10) — same marks.
- Beary's dot: terracotta, ink-stroked, identical in every walking beat.
- The hero numbers ("12", "10 vs 8", "256", "over a billion") are always
  terracotta bold; dim grey is reserved for the wrong/dead option.

## BIDEA correction

Naive framing typed: "Can an AI\nsolve a pathfinding puzzle?"
Trigger: "can an AI solve a pathfinding puzzle" →
Replacement: "what happens when Muse does the whole assignment"
(the trigger appears verbatim in `text`; neither ends in punctuation).

## BDEFS terms (in act order of need)

BFS, shortest path, heuristic, bitmask DP, NP-hard — 5 terms, each ≤17 chars,
one plain line each. "Traveling salesperson" is taught inside Act II (B05)
where it is earned, not in BDEFS.
