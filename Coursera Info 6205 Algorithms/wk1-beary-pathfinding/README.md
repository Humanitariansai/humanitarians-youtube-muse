# Wk1 — Help Beary Navigate the Forest to Collect Honey

Reference solution + audit for the Week 1 pathfinding assignment
(original notebook kept here as
`Wk1_Help_Beary_Navigate_Forest_Collect_Honey_Pathfinding_Assignment.ipynb`).

## Problem (one line)

On a grid of `B` (start), `H` (honey), `O` (obstacle), `.` (free), find the
minimum steps for Beary to collect **every** honey pot **and return to `B`**;
return `-1` if impossible. Movement is 4-directional.

## Files

| File | What it is |
|---|---|
| `solution.py` | Three approaches: `solve_dp` (pairwise BFS + Held–Karp bitmask DP — primary), `solve_state_bfs` (BFS over `(row, col, collected-mask)` — equally optimal), `solve_greedy` (nearest-honey heuristic — fast, not always optimal). Run `python3 solution.py` for a quick demo. |
| `test_solution.py` | 25 tests: the example, tiny basics, unreachable cases, a greedy-is-suboptimal counterexample, 300 randomized cross-validation trials (both optimal methods agree; greedy never beats optimal), and a 50×50 performance check. Run `python3 test_solution.py`. |
| `ASSIGNMENT-REVIEW.md` | Independent audit of the assignment itself — **4 findings**: the example's expected output (6) is wrong under the stated spec (correct: 12); "always a valid path" contradicts "return -1"; movement model unstated; number of `B` cells unstated. Each finding is code-verified. |
| `Wk1_...ipynb` | The original assignment notebook, unmodified. |
| `Wk1_Beary_Pathfinding_Assignment_FIXED.ipynb` | Student-facing notebook with all four `ASSIGNMENT-REVIEW.md` findings fixed (expected output 12, -1 contradiction resolved, movement model and single-`B` stated). Original kept as `Wk1_...ipynb`. |

## Key result

The assignment's example says the answer is **6**. That is the shortest tour
*without* returning to start. The assignment's own objective and output spec
both require the return trip, for which the verified optimum is **12**.
See `ASSIGNMENT-REVIEW.md` Finding 1 for the full evidence and the
recommended fix.

## Approaches at a glance

| Approach | Optimal? | Complexity | When to use it |
|---|---|---|---|
| Bitmask DP (Held–Karp) | Yes | O(K·R·C + K²·2^K) | Primary solution; K = # honey pots |
| State-space BFS | Yes | O(R·C·2^K) | Simplest correct code |
| Greedy nearest-honey | No | Polynomial | Baseline only — provably suboptimal (see counterexample test) |

All three agree on the example (12) and on 300 randomized grids
(where defined); greedy is strictly worse on the counterexample grid
(10 vs 8).
