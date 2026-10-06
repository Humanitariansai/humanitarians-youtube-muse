# FACTCHECK.md — Muse Does the Assignment

Gate F. Every number and named claim checked against the source (the
assignment notebook, the reference solution runs) and fixed where wrong.
Rows: claim | verdict | source | fix.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B01–B03 | Example grid is B(0,0), H(0,2),(2,0),(2,2), O(1,0),(1,1) | PASS | Assignment notebook, Example section | — |
| 2 | B03/B13 | Assignment's expected output is 6 | PASS (as a quote) | Assignment notebook | Framed as the assignment's claim, then refuted: 6 = no-return tour |
| 3 | B06/B13 | Correct optimum with return is 12 | PASS | `solution.py`: `solve_dp` and `solve_state_bfs` both return 12 on the example; brute-force permutation check in audit | — |
| 4 | B04 | BFS distances B→H are 2, 4, 6 | PASS | Computed by `_bfs_dist` in solution.py; distance matrix printed in audit | — |
| 5 | B05 | Subset cheapest costs: {H1}=2,{H2}=4,{H3}=6,{H1H2}=4,{H1H3}=6,{H2H3}=6,all=6 | PASS | Hand-derived from the distance matrix, cross-checked against Held–Karp DP internals | Corrected during build: full-set min is 6 (was 8 in first draft) |
| 6 | B09/B10 | Greedy pays 10, optimal pays 8 on the trap grid | PASS | `test_greedy_counterexample`: greedy==10, dp==8, state_bfs==8 | — |
| 7 | B08 | "300 random grids, zero disagreements" | PASS | `test_fuzz_dp_vs_state_bfs`: 300 trials, seed 20261006, dp==state_bfs on all; greedy never beats optimal | — |
| 8 | B08 | Terminal shows "25 passed, 0 failed" / "ALL TESTS PASSED" | PASS | Verbatim stdout of `python3 test_solution.py` run 2026-10-06 in `~/workspace/algo-wk1/wk1-beary-pathfinding/` | On-screen text is character-identical to the run |
| 9 | B06 | "a fraction of a second" | PASS | 50×50, 8-honey timing: 0.03 s (well under a second); example grid is far smaller | Kept vague ("fraction of a second") — no false precision |
| 10 | B11 | K=8 → 256 subsets; K=30 → over a billion (1,073,741,824) | PASS | 2^8=256, 2^30=1073741824 by arithmetic | "over a billion" is the spoken form; exact figure in SOURCES.md |
| 11 | B11 | "NP-hard — no known method escapes the exponential" | PASS | Standard result: TSP (hence grid multi-target tour) is NP-hard; the film claims "no known", not "none exists" | Worded to avoid P-vs-NP overclaim |
| 12 | B14 | Four audit findings | PASS | `ASSIGNMENT-REVIEW.md` findings 1–4, each code-verified | — |
| 13 | B14 | "All four now fixed, in a corrected notebook" | PASS | `Wk1_Beary_Pathfinding_Assignment_FIXED.ipynb` pushed to the repo 2026-10-06 (expected output 12, -1 contradiction resolved, 4-directional + exactly-one-B stated) | — |
| 14 | BIDEA | Course is "INFO 6205" | PASS | Assignment notebook context (INFO 6205 Program Structure and Algorithms, Northeastern) | Spoken as "INFO 6205"; full course name in metadata |

Strip-the-datable: no model version numbers, no "2026" dates, no pricing, no
tool versions in narration. "Three hundred random grids" and "twenty-five
tests" are properties of this build's run, stated as the build's own
evidence — they do not date the film's claims.
