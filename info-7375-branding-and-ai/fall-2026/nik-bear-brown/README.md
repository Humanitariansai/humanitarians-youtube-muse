# nik-bear-brown

A place for the public work of Nik Bear Brown's examples — INFO 7375 Branding and AI, Fall 2026.

## Executive summary

**What this is.** Professor Bear's worked examples for **INFO 7375 Branding and AI**, Fall 2026 — the assignments done the way students do them, on the same cadence, logged the way students log them. This is the submission location the course asks for: `fall-2026/<name>/assignment-XX/`.

**What we are doing now.** Two things at once, and they are the same thing.
- **Assignment 2 — "Plan Your Madison Project Like a Pro."** A step-by-step **recipe for finding a dream job**: here, Designer Advocate or education-advocate work, ideally on flexible terms (summer, contract, part-time) — for example running or developing workshops for universities. The recipe is below; `figma/` and `greenhouse-watch-demo/` are its output so far.
- **Assignment 3 — the visual identity system.** Design tokens, a generator, an SVG specimen. It closes the exact gap the job search found in the CV: *never shipped a design system with tokens*.

**Why read it.** The search is real, so the gaps are real. Every value in this folder is labeled **record** (it came from a saved file or the CV facts), **judgment** (someone read the records and decided), or **your input** (only Professor Bear can supply it). Nothing is invented; anything not built is a typed TODO. A machine ranks words — a person decides.

**Where it stands.**
- **Step 0 done:** the CV as a facts file, personal information removed, checked by Professor Bear on 2026-09-23.
- **Step 1 done for Figma:** the board saved by date and scanned. **2 Designer Advocate roles, both full-time, no posting mentions universities, and nothing is part-time or contract.** So the flexible-terms question is a networking question, not an application question.
- **Step 2 first pass:** a five-row gap table, requirements quoted from the posting against quoted CV facts.
- **Steps 3–8 planned.** Step 3 (other companies) is partly done elsewhere — see below.
- **Assignment 3:** not started; the folder holds the plan.

**Where this came from.** `figma/`, `facts/`, and `greenhouse-watch-demo/` were built for the Prompt Engineering class and copied here on **2026-09-26** at Professor Bear's direction, because the recipe's target — Assignment 2, "Plan Your Madison Project Like a Pro" — is *this* course's assignment. The same search runs in both classes; this folder is where it is graded.

| Folder or file | What it is |
|---|---|
| [`figma/`](figma/) | Figma's open jobs saved by date, the scan, the two relevant postings, and the Figma-only recipe |
| [`greenhouse-watch-demo/`](greenhouse-watch-demo/) | The Reallocation Engine's job-board watcher run on Figma with Professor Bear's CV: what's new, what matches, and what the rules miss |
| [`facts/`](facts/) | Professor Bear's CV as structured JSON, personal information removed, checked by him on 2026-09-23 |
| [`assignment-3/`](assignment-3/) | The visual identity system: creative brief, `tokens.json`, generator, specimen, rationale |
| [`FRICTIONAL.md`](FRICTIONAL.md) | The process log: what was tried, what went wrong, who did what, and every push |
| [`CLAUDE.md`](CLAUDE.md) | Rules Claude Code follows in this folder |

---

## Recipe: find a dream job (advocate and education work)

```yaml
status: DRAFT          # step 1 runs for one company; steps 3–8 not built
todos_open: 7
last_gate: null
attestation: null
recipe_version: 0.1.0
```

**The rule for every step:** every value is labeled **record**, **judgment**, or **your input**. Nothing is invented. Anything not built yet is a typed TODO.

### Step 0 — The CV as facts ✅ done

The CV becomes [`facts/professor-bear-cv.json`](facts/professor-bear-cv.json), personal information removed, `attested: true` (checked by Professor Bear, 2026-09-23). The gap analysis compares job requirements against *this file*, not against memory.

### Step 1 — Watch one company: Figma ✅ done for 2026-09-23 · feeds **Part 1, the dream job**

1. **Save the day's board** as readable JSON: [`figma/figma-jobs-2026-09-23.json`](figma/figma-jobs-2026-09-23.json) (160 postings).
2. **Scan it** with [`figma/find_roles.py`](figma/find_roles.py) for role words in titles (advocate, educator, enablement…), topic words in the text (university, workshop, educate…), and flexible-terms words (part-time, contract, summer…) → [`figma/roles-2026-09-23.md`](figma/roles-2026-09-23.md).
3. **Keep the relevant postings** with [`figma/pick_postings.py`](figma/pick_postings.py) → [`figma/professor-bear-figma.json`](figma/professor-bear-figma.json) and [`.md`](figma/professor-bear-figma.md).

**What it found (record).** 2 Designer Advocate roles, both stating full time from a US hub, travel up to 25%, $153,000–$317,000. No posting mentions universities or campuses. No posting offers part-time, contract, or temporary terms.

**Two candidate picks, and they disagree — on purpose.**

| Pick | Which | Why | Where it was argued |
|---|---|---|---|
| Step 1's suggestion (judgment) | **Designer Advocate, Partnerships** | The only role that builds *certification and enablement programs* and represents Figma *at workshops* — closest to teaching | [`figma/README.md`](figma/README.md) |
| The Assignment 2 write-up (judgment) | **Designer Advocate** (the US-hubs posting) | Broader community teaching, and the better-known posting; Partnerships kept as "consider" | [`advocate/figma-advocate-roles.md`](advocate/figma-advocate-roles.md) |

Both are defensible and the disagreement is kept rather than resolved quietly. `[TODO: DEFINE]` Professor Bear picks one for the submission, and says in one sentence why.

`[TODO: DEFINE]` The "why this role" sentence, in his words. **Excellence — the hiring manager:** by hand on LinkedIn; names and notes stay **out of this public repo**.

### Step 2 — Gap analysis against the CV 🟡 first pass · feeds **Part 2, the gap analysis (20 pts)**

**They want** is quoted from the posting (record). **I have** is quoted from the facts file (record); "not in the CV" means a word search found nothing. The last two columns are judgments and proposals for Professor Bear to confirm or rewrite.

| They want (Designer Advocate, Partnerships) | I have (CV facts) | Gap to fill (judgment) | Madison could help by… (proposal) |
|---|---|---|---|
| "deep, hands-on expertise in Figma" | Not in the CV — the word *Figma* never appears | Public, visible Figma work | Building Madison's own board and design in Figma, published as a worked example |
| "design systems, design tokens, and AI-assisted design or prototyping" | Not in the CV. Closest: MS, Information Design and Visualization | A design-system or AI-prototyping artifact to show | **Assignment 3 is this** — tokens → specimen, plus an agent that audits a design file against a small design system |
| "Build, evolve, and deliver certification programs, and scalable enablement programs" for partners | "Co-developed and filmed INFO 6205… full Coursera platform course (13 modules)"; "ENGR 0201… 700+ learners"; "25+ AI-powered course assistants" | Mostly a **strength**. The gap is the word: none of it is framed as *certification* or *partner enablement* | An agent that turns one Figma workflow into a short certification module (lesson, quiz, rubric) |
| "delivering compelling presentations and effectively engaging audiences of all sizes" | Workshops (Institute for Experiential AI); a 700+ learner course; conference *papers* (ICLR, BMVC) | No **talks** or community events are listed in the CV | An agent that turns each course film into a meetup-talk outline |
| "travel of up to 25%" and full-time terms | "Associate Teaching Professor," 2022–present; the CV doesn't state hours | **Terms, not skills** — the flexible-work gap | Nothing to build. This is a networking question (step 6) |

`[TODO: DEFINE]` Professor Bear confirms the gaps and adds what the CV leaves out.

### Step 3 — Similar roles at other companies ⬜ planned, partly done elsewhere

The Reallocation Engine's `greenhouse-watch` skill reads **Greenhouse, Ashby, and SmartRecruiters** boards and has already been run on **Canva, Miro, Webflow, Notion, Writer, and Jasper** (2026-09-19). That sweep found **six advocate/educator roles at four companies — only one of them US-remote** (Webflow's Senior Developer Educator). It is written up in [`advocate/`](advocate/).

`[TODO: DEV]` Fold those results into this folder's shape — one folder per company with a dated board, a scan report, and kept postings — and make `find_roles.py` read any saved board, not only Figma's layout.

### Step 4 — Gaps across roles, not just one ⬜ planned

Pool the requirement lines from every kept posting and count how often each appears (record: a count). Gaps that recur across companies come first; a gap that appears once is one employer's taste. `[TODO: DEV]`

### Step 5 — Close the top gaps with credibility work ⬜ planned · the "3 hours building"

One public artifact per top gap. **Assignment 3 is the first one.** Log each as it ships.

### Step 6 — Network where the terms aren't posted ⬜ planned · the "3 hours networking"

Figma's board names the Advocacy team but never flexible terms. A conversation is the route, not an application. `[TODO: DEFINE]` by hand; names and notes stay private, never in this repo.

### Step 7 — Apply only when the terms fit ⬜ planned · the "2 hours applying"

Apply when a kept posting's stated terms fit; otherwise network or skip. Only Professor Bear clears this gate. `[TODO: DEV]` a day-over-day diff so a new advocate or flexible posting stands out the day it appears.

### Step 8 — Log every run ♻️ ongoing

Every substantive change goes in [`FRICTIONAL.md`](FRICTIONAL.md), per [`CLAUDE.md`](CLAUDE.md).

---

## What this recipe gives Assignment 2

The assignment lives on a **Figma board**. This folder supplies checked material; the board, the writing, and the choices are Professor Bear's.

| Assignment part | From this recipe | Still his to do |
|---|---|---|
| **1. Dream job (10)** | Step 1: the posting, link, and top 3 requirements, quoted | Choose between the two candidate picks; write the "why this role" sentence; the hiring-manager research |
| **2. Gap analysis (20)** | Step 2: five rows, requirements and CV evidence quoted | Confirm the gaps. Excellence needs research into Figma's actual stack beyond the posting, with sources |
| **3. PRD (40)** | The problem, from the posting: Figma needs "scalable enablement programs" for service and distribution partners. The users: partners and their customers | Write the PRD; find real industry metrics with sources. Don't invent numbers |
| **4. Technical architecture (30)** | The proposal below | Choose, research the n8n nodes, draw the diagram |

**A starting proposal for Part 4 (judgment; adapt or replace):**

- **Agent 1, Board Watcher** — fetches one company's public job board daily, saves it as readable JSON (step 1.1).
- **Agent 2, Role Scout** — scans the saved board for role, topic, and flexible-terms words; keeps the relevant postings (steps 1.2–1.3).
- **Agent 3, Gap Analyst** — compares kept requirements against the CV facts and drafts the gap table, every row labeled record or judgment (step 2).
- **How they talk:** each hands the next a JSON file, and those formats already exist — `figma-jobs-*.json` → `professor-bear-figma.json` → a gap table. That is the "data schema between agents" the excellence points ask for.
- **n8n MVP (one workflow):** Schedule Trigger → HTTP Request (the Greenhouse boards API) → Code (the scan) → IF (anything new and relevant?) → notification or sheet row. `[TODO: DEFINE]` confirm each node against n8n's own documentation before it goes on the board.
- **Out of scope for Week 3:** multi-company sweeps, automatic applying, anything that contacts a person.

---

## Everything is in this one folder

As of 2026-09-26 there is a single folder for this work, matching the Computational Skepticism and Prompt Engineering repos, where the instructor's folder is `fall-2026/nik-bear-brown/` and nothing of his sits anywhere else. Assignment 2's write-up and the seven-company advocate sweep were originally put under `assignments/nik-bear-brown/` and have been moved here:

| Folder | What it is |
|---|---|
| [`assignment-2/`](assignment-2/) | The dream-job write-up, its three quoted requirements, and the machine reports it was chosen from in [`assignment-2/evidence/`](assignment-2/evidence/) |
| [`advocate/`](advocate/) | The advocate-role portfolio: six advocate/educator roles across four companies, only one US-remote, plus [the narrowed Figma list](advocate/figma-advocate-roles.md) |
| `brutalist-figma-claude/` | The Figma API practitioner book — its own GitHub repository, checked out here for convenience and **not committed from this repo** |
