"""Tests for the Beary pathfinding assignment (solution.py).

Run:  python3 test_solution.py

Covers: the assignment's example, single-honey and no-obstacle basics,
unreachable honey (-1), a greedy-is-suboptimal counterexample, randomized
cross-validation of the two optimal approaches, and a 50x50 performance check.

IMPORTANT: test_example asserts 12, NOT the assignment's stated expected
output of 6. The value 6 is the shortest tour that does NOT return to B;
the assignment's own objective and output spec require the return trip,
for which the optimum is 12. See ASSIGNMENT-REVIEW.md.
"""

import random
import time

from solution import solve_dp, solve_state_bfs, solve_greedy

PASS = []
FAIL = []


def check(name, actual, expected):
    if actual == expected:
        PASS.append(name)
    else:
        FAIL.append(f"{name}: expected {expected}, got {actual}")


# ---------------------------------------------------------------- 1. example
def test_example():
    grid = [
        ["B", ".", "H"],
        ["O", "O", "."],
        ["H", ".", "H"],
    ]
    check("example dp == 12", solve_dp(grid), 12)
    check("example state_bfs == 12", solve_state_bfs(grid), 12)
    # Greedy happens to be optimal on this particular grid.
    check("example greedy == 12", solve_greedy(grid), 12)


# ------------------------------------------------------- 2. tiny basics
def test_single_honey_adjacent():
    grid = [["B", "H"]]
    for fn in (solve_dp, solve_state_bfs, solve_greedy):
        check(f"adjacent {fn.__name__} == 2", fn(grid), 2)


def test_same_row_no_obstacles():
    grid = [["B", ".", ".", "H"]]
    for fn in (solve_dp, solve_state_bfs, solve_greedy):
        check(f"same-row {fn.__name__} == 6", fn(grid), 6)  # 3 out + 3 back


def test_no_honey():
    grid = [["B", ".", "."], [".", "O", "."]]
    for fn in (solve_dp, solve_state_bfs, solve_greedy):
        check(f"no-honey {fn.__name__} == 0", fn(grid), 0)


# ------------------------------------------------------- 3. impossible
def test_unreachable_honey():
    grid = [
        ["B", "O", "H"],
        ["O", "O", "O"],
        [".", ".", "."],
    ]
    for fn in (solve_dp, solve_state_bfs, solve_greedy):
        check(f"unreachable {fn.__name__} == -1", fn(grid), -1)


def test_unreachable_return():
    # Honey reachable, but the statement also covers weird maps; here the
    # return leg is what fails (B boxed in after the fact is impossible in
    # 4-dir movement, so we wall B off from one honey instead).
    grid = [
        ["B", ".", "O", "H"],
        [".", ".", "O", "."],
    ]
    for fn in (solve_dp, solve_state_bfs, solve_greedy):
        check(f"walled-honey {fn.__name__} == -1", fn(grid), -1)


# ------------------------------------------------------- 4. greedy counterexample
def test_greedy_counterexample():
    # B=(0,0); honey at (2,0), (1,1), (3,1). Greedy goes B -> (1,1) -> (2,0)
    # -> (3,1) -> B = 2+2+2+4 = 10. Optimal: B -> (2,0) -> (3,1) -> (1,1)
    # -> B = 2+2+2+2 = 8.
    grid = [
        ["B", ".", ".", "."],
        [".", "H", ".", "."],
        ["H", ".", ".", "."],
        [".", "H", ".", "."],
    ]
    check("counterexample dp == 8", solve_dp(grid), 8)
    check("counterexample state_bfs == 8", solve_state_bfs(grid), 8)
    check("counterexample greedy == 10 (suboptimal)", solve_greedy(grid), 10)


# ------------------------------------------------------- 5. fuzz cross-validation
def _random_grid(rng, rows, cols, n_honey, obstacle_p):
    cells = [(r, c) for r in range(rows) for c in range(cols)]
    rng.shuffle(cells)
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    br, bc = cells.pop()
    grid[br][bc] = "B"
    for _ in range(n_honey):
        hr, hc = cells.pop()
        grid[hr][hc] = "H"
    for r, c in cells:
        if rng.random() < obstacle_p:
            grid[r][c] = "O"
    return grid


def test_fuzz_dp_vs_state_bfs():
    rng = random.Random(20261006)
    mismatches = 0
    greedy_beats_opt = 0
    for trial in range(300):
        rows = rng.randint(3, 7)
        cols = rng.randint(3, 7)
        n_honey = rng.randint(1, 4)
        grid = _random_grid(rng, rows, cols, n_honey, 0.18)
        a = solve_dp(grid)
        b = solve_state_bfs(grid)
        if a != b:
            mismatches += 1
            if mismatches <= 3:
                FAIL.append(f"fuzz trial {trial}: dp={a} state_bfs={b}\n"
                            + "\n".join("".join(row) for row in grid))
        g = solve_greedy(grid)
        if a != -1 and g != -1 and g < a:
            greedy_beats_opt += 1
    check("fuzz: dp == state_bfs on 300 grids", mismatches, 0)
    check("fuzz: greedy never beats optimal", greedy_beats_opt, 0)


# ------------------------------------------------------- 6. performance
def test_performance_50x50():
    rng = random.Random(7)
    rows = cols = 50
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    grid[0][0] = "B"
    placed = 0
    while placed < 8:
        r, c = rng.randrange(rows), rng.randrange(cols)
        if grid[r][c] == ".":
            grid[r][c] = "H"
            placed += 1
    t0 = time.perf_counter()
    ans = solve_dp(grid)
    dt = time.perf_counter() - t0
    check("50x50 8-honey dp finishes < 5s", dt < 5.0, True)
    check("50x50 8-honey dp finds a tour", ans > 0, True)
    print(f"    (50x50, 8 honey: answer={ans}, dp took {dt:.2f}s)")


# ------------------------------------------------------- runner
def main():
    for name, fn in sorted(
        [(k, v) for k, v in globals().items() if k.startswith("test_")]
    ):
        fn()
    print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
    for f in FAIL:
        print("FAIL:", f)
    if FAIL:
        raise SystemExit(1)
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    main()
