# Frictional — Assignment 4

The process log for this assignment. The folder-level log across all of Professor Bear's work in this class is [`../FRICTIONAL.md`](../FRICTIONAL.md); this one stays on Assignment 4.

## Executive summary

**What this is.** The process log for the Assignment 4 Part 1 build: the
opportunity matcher, in two implementations (Python `matcher.py` and n8n
`workflow_v2.json`), plus extended board coverage (Anthropic live,
Meta investigated). Written the way the course asks students to write
theirs.

**Why read it.** It records what was tried, what went wrong, and what was
measured — including two tuning iterations where the first run exposed
exactly the false-friend problems the 2026-09-26 audits found.

**What it records so far.** 2026-10-03: one session. Anthropic's live
Greenhouse board (640 postings) pulled and scored; the direct equivalents
of the Figma advocate target identified. Meta's board investigated and
recorded as unreadable, same category as Google. The matcher built, run on
714 postings (97 kept + 640 fresh, deduped): 22 PURSUE, 37 NETWORK, 325
WATCH, 330 SKIP, 0 quarantined, 3.1s.

## Entries

### 2026-10-03 — Extending coverage: Anthropic live, Meta investigated

- **Date and what I was working on:** Professor Bear asked for the equivalent
  of the Figma advocate roles at Anthropic, and "why not Meta."

- **I tried / expected:** I expected Anthropic to be readable (the 2026-09-26
  run already used its Greenhouse feed) and Meta to be an open question.

- **What happened:**
  - **Anthropic worked first try.** `boards-api.greenhouse.io/v1/boards/anthropic/jobs`
    returned 640 postings. The direct equivalents are live right now:
    *Developer Education Lead, Claude Platform*; *Head of Technical Training*;
    *Technical Documentation and Content Engineer, Claude Docs* (the 2026-09-26
    bullseye — still open); *Software Engineer, Education*; plus a bench of
    enablement leads.
  - **Meta is unreadable.** `metacareers.com/jobsearch/` is a JS shell — no
    server-rendered job data, search on internal authenticated GraphQL with
    rotating doc IDs, no public JSON feed. Same category as Google in the
    2026-09-26 log. I stopped after three shapes rather than guessing more,
    per the course's own precedent.
  - **No "Muse for Education" role found.** A web search surfaced Meta's
    education-adjacent recruiting programs but no staffed advocate/educator
    function for Muse. Absence from the table is a measurement gap, not
    evidence of no demand.

- **What I did:** Saved the live Anthropic pull as `anthropic-live.json`
  (evidence, dated); wrote `anthropic-equivalents-2026-10-03.md` with the
  ranked equivalents; wrote `meta-board-note-2026-10-03.md` recording the
  unreadable finding and the manual re-check path.

- **What Claude or another person contributed:** Muse (me) ran the pulls,
  read the board, and wrote the notes. Professor Bear set the direction:
  Anthropic equivalents, and "why not Meta."

- **What I understand now / still do not understand:** Anthropic is where
  the demand is most legible right now — it staffs the exact function the
  search targets. Meta remains a question mark by method, not by evidence.
  Still open: whether a browser-driven reader for Meta (and Google, Adobe,
  Salesforce, GitHub) is worth building, or monthly hand-checks.

- **Evidence and next step:** `anthropic-live.json`, `anthropic-equivalents-2026-10-03.md`,
  `meta-board-note-2026-10-03.md`. Next: the matcher itself.

### 2026-10-03 — Building the opportunity matcher, two ways

- **Date and what I was working on:** Assignment 4, Part 1 — the intelligence
  layer on the Assignment 3 collector. Built as `matcher.py` (Python) and
  `workflow_v2.json` (n8n): same weights, thresholds, vocabulary, routing.
  Two implementations, one spec.

- **I tried / expected:** Score each posting on five dimensions (role 0.30,
  audience 0.20, materials 0.20, gap-close 0.15, company 0.15), route to
  PURSUE / NETWORK / WATCH / SKIP, generate a per-role rationale and a
  weekly digest. I expected the ranking to work first try.

- **What happened:**
  - **First run: 633 of 714 in WATCH.** The band was noise. Cause: generic
    business words (partner/customer/public/community) counted as "audience,"
    and bare "conference"/"workshop" matched boilerplate — the same
    false-friend class the 2026-09-26 audits found.
  - **Fix 1 — the pairing rule**, from the course's own open question:
    a discounted title word (training/enablement/education/learning/content)
    only counts when the text confirms it with a named audience or a
    materials phrase. This operationalizes the "train their own people"
    reversal: confirmed teaching counts, pure process does not.
  - **Fix 2 — audience and gap tightened.** Audience words re-weighted:
    education audiences 0.4–0.5, developers 0.3, generic business words
    0.1–0.15. Gap phrases now require the posting to *ask for* the activity
    ("give talks," "run workshops") instead of matching "we publish at
    conferences."
  - **The bullseye failed, then passed.** The Claude Docs role scored 0.46
    (NETWORK) because no materials phrase matched "own the documentation."
    Measured across 737 postings: "own the documentation" hit twice, both
    the right role — added. "documentation for" hit 8 times, mostly tax and
    AV boilerplate — rejected, same reason "how-to guides" was cut. The
    role now scores 0.66 → PURSUE.
  - **Final: 22 PURSUE, 37 NETWORK, 325 WATCH, 330 SKIP, 0 quarantined,
    3.1 seconds.** Top of PURSUE: Developer Education Lead (Anthropic),
    Designer Advocate Partnerships (Figma), Senior Developer Educator
    (Webflow), Native Learning Experiences (OpenAI), Learning Experiences
    Creator (Replit).

- **What I did:** Wrote `matcher.py`, `workflow_v2.json` (validated: 11
  nodes, no dangling refs), `ERROR-HANDLING.md` (retry/backoff, error
  branches, quarantine, cached-data fallback), and ran it on real data:
  `digest-2026-10-03.md` + `.html`, 15 per-role briefs, `run-report.json`.

- **What Claude or another person contributed:** Muse (me) designed the
  scoring, found the WATCH-band problem in the first run's output, and made
  the three tuning calls — all measured before changing anything. Nothing
  here has been reviewed by Professor Bear; thresholds and weights are
  judgment, labeled as such in the code.

- **What I understand now / still do not understand:** The matcher
  reproduces the course's findings rather than contradicting them — the
  false friends bit in exactly the predicted places, and the fixes are the
  ones the log had already proposed. Still open: whether NETWORK's 37 are
  conversation-worthy (his call), and the LLM upgrade path for rationales.

- **Evidence and next step:** `matcher.py`, `workflow_v2.json`,
  `ERROR-HANDLING.md`, `outputs/` (digest, 15 briefs, run report). Next:
  Part 2 gallery polish, Part 3 scale numbers, Part 4 Figma materials —
  and Professor Bear's review of the thresholds.

### 2026-10-03 — Film 1: "Muse builds the opportunity matcher"

- **Date and what I was working on:** Assignment 4, Part 1 film — the first
  of four lecture films, one per assignment part. Covers the matcher build:
  the problem, the five-dimension scoring, Python + n8n, what went wrong
  (the WATCH-band noise, the bullseye fix), results, error handling, and an
  evaluation of Muse's work.

- **I tried / expected:** Full pre-render package in one pass: ACTS, shot
  list, fact check, beat sheet generator, 17 Manim scenes, all static gates
  clean, pushed to GitHub with a Claude Code render prompt. Expected the
  scenes to pass QC first try.

- **What happened:**
  - 22 beats (~5m24s), 17 scenes (M01–M17), six acts. py_compile passed.
  - Static checker initially flagged repeated-animation errors on
    text-heavy scenes — fixed with progressive non-text shapes.
  - Two accidental `__pycache__/` `.pyc` files were pushed to GitHub, then
    deleted via the API. Recorded, not hidden.
  - Final: **17 clean, 0 warnings, 0 errors**. All 11 package files pushed
    to `assignment-4/films/part-1-opportunity-matcher/`.
  - No MP3/MP4 rendered — per the workflow, Bear renders locally with
    Claude Code + Kokoro. Awaiting his render.

- **What I did:** Wrote every file of the package (script, beats, scenes,
  docs, QC report, render prompt) and pushed each to GitHub immediately,
  per the standing rule.

- **What Claude or another person contributed:** Muse (me) authored the
  whole package. Bear set the title, the four-film structure, the
  evaluation brief, and the render workflow (his Mac, his Claude Code).

- **What I understand now / still do not understand:** The film pipeline
  works: fact-check first, then script, then scenes, then gates, then push.
  The QC stub's "shapes never change" rule is the binding constraint on
  scene design — every beat needs evolving non-text geometry. Still open:
  whether the rendered cut lands (Bear's step).

- **Evidence and next step:** `films/part-1-opportunity-matcher/` on GitHub
  (11 files). Next: Bear's local render; films 2–4.

### 2026-10-03 — Film 2: "Muse shows the output"

- **Date and what I was working on:** Assignment 4, Part 2 film — the
  end-to-end flow and the human-usable outputs gallery: the digest, three
  brief cards, the run report, the quality check, the honest gap.

- **I tried / expected:** 15 beats (~5m16s), 13 scenes, all gates clean
  first try. Expected the brief-card scenes to be straightforward.

- **What happened:**
  - Caught a script error before filming: the draft claimed "37 network
    notes" as files — the briefs directory holds only the 15 PURSUE briefs;
    NETWORK roles live in the digest. Fixed the line to say what the files
    prove.
  - First QC pass: `Checkmark` is not defined in the QC stub (replaced with
    a custom two-line check mark); four scenes failed "shapes never change"
    (text-only reveals); one text-only warning. Fixed with dot bullets,
    square row markers, per-bar grows, background plates.
  - Final: **13 clean, 0 warnings, 0 errors**. All 11 files pushed to
    `assignment-4/films/part-2-showing-the-output/`.

- **What I did:** Read the actual outputs (digest, three briefs, run report)
  before writing a word, so every beat cites a real file. Wrote the package
  and pushed it.

- **What Claude or another person contributed:** Muse authored the package.
  Bear set the title "Muse shows the output" and the Part 2 scope (10–15
  usable outputs, quality checks, non-technical usability).

- **What I understand now / still do not understand:** Grounding the script
  in the files first is what caught the 37-briefs error — the FACTCHECK
  discipline pays. The custom check-mark helper is now a reusable pattern.

- **Evidence and next step:** `films/part-2-showing-the-output/` on GitHub.
  Next: films 3–4.

### 2026-10-03 — Scale tests: "Muse proves it scales" (measurements + Film 3)

- **Date and what I was working on:** Assignment 4, Part 3 — honest scale
  tests first (single request → 10x → 50x, breaking point, rate limits,
  memory, cost, production readiness), then the film.

- **I tried / expected:** Replicate real Anthropic records with unique ids
  at 1x/10x/50x, time the full pipeline, record peak RSS, measure a live
  fetch. Expected to find the breaking point somewhere in 10x–50x.

- **What happened:**
  - Measured: 640 → 2.37 s; 6,400 → 23.8 s; 32,000 → 119.1 s.
    **3.72 ms/record, perfectly linear, peak RSS 52–65 MB.** No breaking
    point found — at 50x the run takes two minutes and works.
  - A second run with fully distinct (deep-copied) records confirmed the
    same memory figure; a shallow-copy caveat was checked, not assumed.
  - Fetch measured live: 640 jobs / 9.2 MB / 6.2 s, HTTP 200, no rate
    limit.
  - Honest gaps named in SCALE-TESTS.md: n8n at scale, 429 behavior, and
    brief-file writes at scale untested; production volume sits two orders
    of magnitude below anything tested.
  - Cost: $0.00/month — zero API calls, zero LLM calls in scoring —
    labeled estimated, computed from a measured zero.
  - Film: 14 beats (~4m54s), 12 scenes. First QC pass: 2 repeated-animation
    errors (M09, M11), fixed with coin dots and sequenced verdict cards.
    Final: **12 clean, 0 warnings, 0 errors**. Pushed to
    `assignment-4/films/part-3-proving-it-scales/`.

- **What I did:** Wrote scale_test.py, ran all three lanes, verified the
  memory caveat with a second method, wrote SCALE-TESTS.md, then authored
  and gated the film package.

- **What Claude or another person contributed:** Muse ran the tests and
  authored the film. Bear set the title and the Part 3 scope, including the
  requirement to separate measured from estimated.

- **What I understand now / still do not understand:** The negative result
  (no breaking point) is the story — and reporting it with the untested
  territory named is what makes the film honest. Still untested: the n8n
  runtime at load; that stays disclosed, not claimed.

- **Evidence and next step:** `assignment-4/SCALE-TESTS.md` and
  `films/part-3-proving-it-scales/` on GitHub. Next: film 4.

### 2026-10-03 — Package artifacts + Film 4: "Muse packages it"

- **Date and what I was working on:** Assignment 4, Part 4 — the
  professional package first (executive summary, architecture diagram),
  then the film, including the series evaluation of Muse.

- **I tried / expected:** One-page executive summary, a Figma-importable
  SVG architecture diagram with AI components labeled and failure paths
  drawn, then a 13-beat film with the five-dimension Muse evaluation.
  Expected the diagram to be the hard part.

- **What happened:**
  - `package/exec-summary.md`: problem, solution, measured results,
    business value, the delivery TODO, "Built with n8n + Python" badge.
  - `package/architecture.svg`: left-to-right flow, the scoring box labeled
    with weights and the pairing rule, red dashed failure paths
    (quarantine, cached fallback), dashed planned-delivery lane, legend.
    Validated as well-formed SVG (69 elements); plain SVG, no scripts —
    Figma-importable. Bear assembles the actual Figma board.
  - Film: 13 beats (~4m44s), 11 scenes. QC: **11 clean, 0 warnings,
    0 errors on the first pass** — the progressive-shape discipline from
    films 2–3 applied from the start.
  - The B08 evaluation grades Muse on scripting, agents, analysis,
    repo-based work, and film production — written as the assistant's
    assessment for Bear to judge, including the owned failure (the push
    script `json` scoping bug from Part 1).

- **What I did:** Built both artifacts, validated the SVG, pushed them to
  `assignment-4/package/`, then authored, gated, and pushed the film to
  `assignment-4/films/part-4-packaging-it/`.

- **What Claude or another person contributed:** Muse built the artifacts
  and the film. Bear set the title, the Part 4 scope, and the rule that he
  assembles the Figma board himself.

- **What I understand now / still do not understand:** A professional
  package is mostly disclosure: the diagram's most important lane is the
  dashed one (not built), and the evaluation's most important line is the
  owned failure. Still open: Bear's verdict on the renders and the grades.

- **Evidence and next step:** `assignment-4/package/` (exec-summary.md,
  architecture.svg) and `films/part-4-packaging-it/` on GitHub. Next:
  Bear's local renders of all four films; nothing is published.
