# Assignment Review — Wk1: Help Beary Navigate the Forest to Collect Honey

Independent audit of the assignment notebook
(`Wk1_Help_Beary_Navigate_Forest_Collect_Honey_Pathfinding_Assignment.ipynb`),
performed by solving it three different ways and cross-checking every claim.
All findings below are verified by running code in `solution.py` /
`test_solution.py` in this folder — nothing here is asserted by hand-waving.

## Finding 1 (CONFIRMED ERROR): the example's expected output is wrong

The assignment states:

> `find_shortest_path(grid)  # Expected output: 6`

for

```python
grid = [
    ['B', '.', 'H'],
    ['O', 'O', '.'],
    ['H', '.', 'H']
]
```

**6 is not the correct answer under the assignment's own specification.**
The objective says Beary must "collect all honey pots in the forest **and
return to his starting position** in the shortest number of steps", and the
output spec says "the minimum number of steps required to collect all honey
pots **and return to the starting position**".

- Shortest tour collecting all 3 honey pots **without** returning: **6**
  (B → H(0,2) → H(2,2) → H(2,0): 2 + 2 + 2).
- Shortest tour collecting all 3 honey pots **and returning to B**: **12**
  (any optimal order, e.g. B → (0,2) → (2,2) → (2,0) → B: 2+2+2+6).

Verified by two independent optimal implementations in this folder
(`solve_dp` and `solve_state_bfs` agree on 12; a 300-grid randomized
fuzz test shows they agree everywhere). The stated expected output of 6
corresponds exactly to the no-return tour, so the example was almost
certainly computed without the return leg.

**Recommended fix (pick one):**
- (a) Change the expected output to `12`, keeping the return requirement; or
- (b) keep `6` but rewrite the objective/output spec to drop the return
  requirement.

Option (a) is recommended: the return leg is what makes the problem a
genuine traveling-salesperson-style challenge rather than a plain
multi-target BFS exercise.

## Finding 2 (CONTRADICTION): "always a valid path" vs "return -1"

Constraints say:

> "There is always a valid path for Beary to collect all honey pots and return."

but the output spec says:

> "If it's impossible, return `-1`."

Both cannot be operative at once: if a valid path always exists, the `-1`
branch is dead code that no test can ever exercise. As written, a student
who implements `-1` correctly gets no credit for it, and a student who
omits it loses nothing.

**Recommended fix:** either delete the `-1` requirement, or soften the
constraint to "in the provided test cases a valid path exists, but your
function must still return -1 for impossible inputs" — and include at
least one impossible test grid (e.g. a honey pot fully walled off by `O`)
in the grading tests. The solutions in this folder implement `-1` for
unreachable honey pots and it is covered by `test_unreachable_honey` and
`test_unreachable_return`.

## Finding 3 (AMBIGUITY): movement model is never stated

The notebook never says whether Beary moves 4-directionally or
8-directionally (diagonals). The grading rubric's "BFS for shortest path in
an unweighted grid" strongly implies 4-directional adjacency, and the
reference solutions here assume it — but a student using 8-directional
movement would get different answers on some grids through no fault of
their own.

**Recommended fix:** add one line, e.g. "Beary moves one cell at a time:
up, down, left, or right (no diagonal moves)."

## Finding 4 (AMBIGUITY): exactly one 'B' is assumed, never stated

Constraints guarantee "at least one `'B'`" — "at least" leaves multiple
start cells legal, with no rule for which one Beary starts from. The
reference solutions use the first `B` in scan order.

**Recommended fix:** change to "exactly one `'B'`".

## What checks out fine

- Grading weights sum to 100 (40 + 30 + 10 + 10 + 10). ✓
- The function signature is consistent with the I/O description. ✓
- The 50×50 cap keeps the intended BFS + bitmask-DP approach tractable
  (verified: 50×50 with 8 honey pots solves in ~0.03 s). ✓
- Criterion 2's emphasis on BFS for the unweighted legs is the right
  nudge; the greedy-nearest-honey trap is real — `test_greedy_counterexample`
  exhibits a grid where greedy needs 10 steps against an optimum of 8. ✓

## Bottom line

One hard error (expected output 6 vs correct 12), one contradiction
(always-valid-path vs return -1), and two ambiguities worth one sentence
each (movement model, number of start cells). Findings 1 and 2 should be
fixed before this assignment ships; 3 and 4 are one-line clarifications.
