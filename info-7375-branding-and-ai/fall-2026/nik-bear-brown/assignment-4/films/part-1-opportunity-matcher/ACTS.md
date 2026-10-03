# ACTS.md — "Muse builds the opportunity matcher" (Assignment 4, Part 1 film)

Lecture skill. Channel: claude-liam (Liam, in for Bear · Kokoro am_onyx · @NikBearBrown).
Title (exact, used verbatim in BOUT): "Muse builds the opportunity matcher".
Reel: `info-7375-branding-and-ai/fall-2026/nik-bear-brown/assignment-4/films/part-1-opportunity-matcher/`

## Framing

This film tells the Part 1 build story: the opportunity matcher, what it
does, what went wrong, and the results. It is also, on purpose, an
evaluation of Muse doing agentic work — writing the scripts, running the
analysis, tuning from evidence, pushing to the repo. The evaluation is
honest: what worked and what failed are both in the film. Liam narrates.

Source: `assignment-4/FRICTIONAL.md`, `matcher.py`, `workflow_v2.json`,
`outputs/run-report-2026-10-03.json`, `anthropic-equivalents-2026-10-03.md`,
`meta-board-note-2026-10-03.md`. Every number below is record from those
files; weights and thresholds are judgment, labeled as such.

## Bookends (fixed)

- **BIDEA** — hesitant writer. Liam's greeting, then the topic: from
  collecting jobs to judging them. Correction pair: trigger
  "a job scraper" → replacement "a job judge".
- **BDEFS** — "Terms In This Lecture", 5 terms:
  1. `matcher` — the program that scores postings
  2. `fit score` — one number, five dimensions
  3. `PURSUE` — the top routing decision
  4. `pairing rule` — weak words need confirmation
  5. `quarantine` — where malformed records go
- **BVDT** — "Let's recap." 6 lines, one per act.
- **BHTF** — "Your turn." Score one posting by hand on the five dimensions;
  compare with the machine. Checks: your score within 0.1 of the machine's;
  you can name the deciding signal.
- **BOUT** — ClaudeTitleOutro, @NikBearBrown.

## ACT I — The problem

1. Assignment 3 collected: 3,446 postings across 18 boards, 97 kept.
   Collecting isn't judging — which of the 97 matter?
2. Part 1's demand: add real intelligence. The machine must decide, not
   just store. Collect → judge.

## ACT II — The design

1. Five dimensions, one fit score: role title 0.30, audience 0.20,
   materials 0.20, gap-close 0.15, company demand 0.15. Weights are
   judgment, labeled in the code.
2. Routing, not just scoring: 0.65+ PURSUE, 0.45+ NETWORK, 0.25+ WATCH,
   else SKIP. Decisions a human can act on.
3. Every score carries its evidence: the rationale quotes what fired —
   "title matches 'developer education'", "rewards CV gap: certification".

## ACT III — Two implementations, new coverage

1. `matcher.py`: Python, runs anywhere, 3.1 seconds for 714 postings.
2. `workflow_v2.json`: the n8n equivalent — schedule, fetch, normalize,
   score, route, briefs, email. Same spec, 11 nodes, validated.
3. Anthropic's board is live: 640 postings pulled. Equivalents found —
   Developer Education Lead, Claude Platform at 0.91.
4. Meta's board is unreadable: JS shell, private GraphQL. Recorded
   honestly, like Google. No "Muse for Education" role found by hand.

## ACT IV — What went wrong

1. First run: 633 of 714 landed in WATCH — noise from generic business
   words ("partner", "customer", "public").
2. The pairing rule: discounted title words (training, enablement…)
   only count with audience or materials confirmation. It operationalizes
   Bear's own "train their own people" reversal.
3. The bullseye failed: the Claude Docs role scored 0.46. Measured "own
   the documentation" — 2 hits on 737 postings, both right — added it.
   Now 0.66, PURSUE. "Documentation for" measured 8 hits, mostly
   boilerplate — rejected.

## ACT V — Results, and when things break

1. Final: 22 PURSUE, 37 NETWORK, 325 WATCH, 330 SKIP. 0 quarantined.
   Top of PURSUE: Developer Education Lead (Anthropic), Designer
   Advocate Partnerships (Figma), Senior Developer Educator (Webflow).
2. Outputs a human can open: the digest (markdown + HTML), 15 per-role
   briefs, the run report with timings.
3. Error handling: fetch retries with backoff, per-record quarantine,
   cached-data fallback. The run never dies silently — failures are
   counted and named.

## ACT VI — The evaluation

1. This film is also an evaluation of Muse doing this kind of work:
   wrote the scripts, ran the analysis, tuned from measured evidence,
   pushed everything to the repo where Bear can see it.
2. What failed: my own push script had a scoping bug — 25 files failed,
   zero went up. Fixed, re-ran, all 25 landed. Logged, not hidden.
   That is the standard being demonstrated.

## LEFT OUT (with reasons)

- The full 15-brief gallery — Part 2's film covers outputs in depth.
- Line-by-line code walkthrough — the film is about decisions, not syntax.
- The NETWORK 37 verdicts — they are Bear's call (your input), not the film's.

## Runtime estimate (information only)

17 body beats × ~10 s ≈ 170 s + bookends ≈ 70 s → roughly 4 minutes.
Length is an output; no target.
