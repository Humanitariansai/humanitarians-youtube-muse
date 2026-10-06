"""
Week 1 — Help Beary Navigate the Forest to Collect Honey.

Problem: on a grid with Beary's start ('B'), honey pots ('H'), obstacles ('O')
and free cells ('.'), find the minimum number of steps for Beary to collect
every honey pot and RETURN to his starting cell. Movement is 4-directional
(up/down/left/right), one cell per step. Return -1 if it is impossible.

Three approaches are implemented below:

  1. solve_dp          — pairwise BFS + Held-Karp bitmask DP (the "textbook"
                         optimal" solution). Best when the number of honey
                         pots K is small; exponential in K.
  2. solve_state_bfs   — one BFS over the state space (row, col, collected
                         mask). Equally optimal, simpler to write, also
                         exponential in K (state space is R*C*2^K).
  3. solve_greedy      — nearest-uncollected-honey heuristic. Fast
                         (polynomial), but NOT always optimal. Included to
                         demonstrate why the problem needs the DP/BFS
                         treatment: see test_greedy_counterexample.

Conventions / documented assumptions (the assignment leaves these unstated):
  * Movement is 4-directional (no diagonals).
  * Exactly one 'B' is expected; the first one found is used.
  * Zero honey pots -> 0 steps (nothing to collect).
  * -1 is returned when any honey pot is unreachable, even though the
    assignment's constraints claim a valid path always exists.
"""

from collections import deque
from typing import List, Tuple, Dict, Set

INF = float("inf")
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

Grid = List[List[str]]
Cell = Tuple[int, int]


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _parse(grid: Grid) -> Tuple[Cell, List[Cell], int, int]:
    """Return (beary, honey_cells, n_rows, n_cols)."""
    beary: Cell = (-1, -1)
    honey: List[Cell] = []
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    for r in range(rows):
        for c in range(cols):
            v = grid[r][c]
            if v == "B" and beary == (-1, -1):
                beary = (r, c)
            elif v == "H":
                honey.append((r, c))
    if beary == (-1, -1):
        raise ValueError("grid must contain a 'B' start cell")
    return beary, honey, rows, cols


def _bfs_dist(grid: Grid, src: Cell) -> Dict[Cell, int]:
    """Shortest-path distances from src to every reachable cell (4-dir BFS)."""
    rows, cols = len(grid), len(grid[0])
    dist: Dict[Cell, int] = {src: 0}
    q: deque[Cell] = deque([src])
    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "O":
                if (nr, nc) not in dist:
                    dist[(nr, nc)] = dist[(r, c)] + 1
                    q.append((nr, nc))
    return dist


def _pairwise(grid: Grid, points: List[Cell]) -> List[List[float]]:
    """All-pairs shortest distances between key points (BFS per point)."""
    n = len(points)
    mat: List[List[float]] = [[INF] * n for _ in range(n)]
    for i, p in enumerate(points):
        d = _bfs_dist(grid, p)
        for j, q in enumerate(points):
            mat[i][j] = d.get(q, INF)
    return mat


# ---------------------------------------------------------------------------
# Approach 1 — pairwise BFS + Held-Karp bitmask DP (primary solution)
# ---------------------------------------------------------------------------

def solve_dp(grid: Grid) -> int:
    """Minimum steps to collect all honey and return to 'B'; -1 if impossible.

    Method: BFS from each key point (B + every H) gives the shortest leg
    distances. The problem then reduces to a traveling-salesperson tour over
    K+1 points starting and ending at B, solved exactly with the Held-Karp
    bitmask DP: dp[mask][i] = shortest path from B visiting exactly the honey
    set `mask` and ending at honey i.

    Complexity: O((K+1) * R * C) for the BFS legs + O(K^2 * 2^K) for the DP.
    Optimal. Exponential in K, so best for a modest number of honey pots.
    """
    beary, honey, _, _ = _parse(grid)
    k = len(honey)
    if k == 0:
        return 0

    points = [beary] + honey          # index 0 = B, 1..K = honey pots
    dist = _pairwise(grid, points)

    # Every honey pot must be reachable from B, otherwise impossible.
    if any(dist[0][i] == INF for i in range(1, k + 1)):
        return -1

    # dp[mask][i]: min cost, start at B, visit honey set `mask` (bit j -> honey
    # j+1), end at honey i (0-based over honey list).
    dp = [[INF] * k for _ in range(1 << k)]
    for i in range(k):
        dp[1 << i][i] = dist[0][i + 1]

    for mask in range(1 << k):
        for last in range(k):
            if not (mask & (1 << last)) or dp[mask][last] == INF:
                continue
            for nxt in range(k):
                if mask & (1 << nxt):
                    continue
                leg = dist[last + 1][nxt + 1]
                if leg == INF:
                    continue
                nmask = mask | (1 << nxt)
                cand = dp[mask][last] + leg
                if cand < dp[nmask][nxt]:
                    dp[nmask][nxt] = cand

    full = (1 << k) - 1
    best = INF
    for last in range(k):
        back = dist[last + 1][0]
        if dp[full][last] != INF and back != INF:
            best = min(best, dp[full][last] + back)
    return int(best) if best != INF else -1


# ---------------------------------------------------------------------------
# Approach 2 — BFS over (row, col, collected-mask) state space
# ---------------------------------------------------------------------------

def solve_state_bfs(grid: Grid) -> int:
    """Minimum steps via a single BFS on the expanded state space.

    A state is (row, col, mask) where mask records which honey pots have been
    collected so far. BFS from (B_r, B_c, 0) finds the shortest walk to any
    state (B_r, B_c, full_mask) — collecting a pot is "free" the first time a
    state enters its cell. The first time BFS reaches the goal state, its
    distance is optimal (BFS on an unweighted graph).

    Complexity: O(R * C * 2^K) states. Optimal and conceptually the simplest
    correct solution; the state space blows up with many honey pots.
    """
    beary, honey, rows, cols = _parse(grid)
    k = len(honey)
    if k == 0:
        return 0
    honey_index = {cell: i for i, cell in enumerate(honey)}
    full = (1 << k) - 1

    start = (beary[0], beary[1], 0)
    dist: Dict[Tuple[int, int, int], int] = {start: 0}
    q: deque[Tuple[int, int, int]] = deque([start])
    while q:
        r, c, mask = q.popleft()
        d = dist[(r, c, mask)]
        if (r, c) == beary and mask == full:
            return d
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] == "O":
                continue
            nmask = mask
            if (nr, nc) in honey_index:
                nmask |= 1 << honey_index[(nr, nc)]
            key = (nr, nc, nmask)
            if key not in dist:
                dist[key] = d + 1
                q.append(key)
    return -1


# ---------------------------------------------------------------------------
# Approach 3 — greedy nearest-honey heuristic (fast but NOT optimal)
# ---------------------------------------------------------------------------

def solve_greedy(grid: Grid) -> int:
    """Nearest-uncollected-honey heuristic.

    Repeatedly BFS from the current cell to the nearest uncollected honey pot
    (ties broken by scan order), walk there, and finally return to B. Runs in
    polynomial time but can be strictly worse than optimal — see
    test_greedy_counterexample in test_solution.py. Included as a cautionary
    baseline: "greedy feels right" is exactly the trap this assignment's
    grading rubric (criterion 2) warns against.
    """
    beary, honey, _, _ = _parse(grid)
    remaining: Set[Cell] = set(honey)
    if not remaining:
        return 0

    total = 0
    cur = beary
    while remaining:
        d = _bfs_dist(grid, cur)
        # nearest uncollected honey; ties -> row-major scan order for determinism
        target = min(remaining, key=lambda h: (d.get(h, INF), h))
        leg = d.get(target, INF)
        if leg == INF:
            return -1
        total += leg
        cur = target
        remaining.discard(target)

    back = _bfs_dist(grid, cur).get(beary, INF)
    if back == INF:
        return -1
    return total + back


# ---------------------------------------------------------------------------
# Convenience: run all three on a grid
# ---------------------------------------------------------------------------

def compare(grid: Grid) -> Dict[str, int]:
    """Run every approach on the same grid; return {name: steps}."""
    return {
        "dp (Held-Karp)": solve_dp(grid),
        "state BFS": solve_state_bfs(grid),
        "greedy": solve_greedy(grid),
    }


if __name__ == "__main__":
    example = [
        ["B", ".", "H"],
        ["O", "O", "."],
        ["H", ".", "H"],
    ]
    print("example grid ->", compare(example))
    print("note: assignment says 6; 6 is the no-return tour. With the required")
    print("return to B, the optimum is 12 (see ASSIGNMENT-REVIEW.md).")
