# Assignment 3 — Collect Data for Your Madison Agent

## Executive summary

**What it does.** `collect.py` fetches every open job posting from three different applicant-tracking systems, keeps the ones about teaching — education, workshops, curriculum, developer advocacy — and writes them to one file of jobs worth my time.

Three steps, once a day:
1. **Download.** For each company on the list, fetch its public job-board JSON and save the response untouched, dated. Greenhouse (`boards-api.greenhouse.io`), Ashby (`api.ashbyhq.com`), SmartRecruiters (`api.smartrecruiters.com`) — three separate APIs with three different shapes and no key required.
2. **Filter.** Scan each posting's title for role words (`advocate, educator, education, enablement, evangelist, developer relations, community, instructor, trainer, curriculum`) and its text for topic words (`university, campus, student, workshop, educate, teach`) and flexible-terms phrases (`part-time, contract role, temporary, fixed-term, freelance, summer, hourly`).
3. **Write.** Save the matches to `jobs-of-interest.json` — **and to `jobs-of-interest.csv`** for the spreadsheet the assignment wants.

**The field names are the source's own.** A kept record carries Greenhouse's `id`, `title`, `absolute_url`, `location`, `content`, `first_published`, `updated_at`, `departments` exactly as Greenhouse wrote them — not renamed, not reshaped. Anything the tool works out for itself goes under one clearly separate key (`matched`), so a reader can always tell what the company said from what my script decided. Ashby's and SmartRecruiters' records keep *their* own names too, which is why the file also records which source each record came from rather than pretending all three are the same.

**What it refuses.** A posting with no title, no link, or no date is not written out — those three fields are what make a record usable, and a record missing them is filler. Duplicates (the same job posted to two boards, or the same board fetched twice in a day) collapse on source + id. A source that times out or returns nothing is logged as unavailable and the other two keep going.

**What it is for.** Figma has no part-time advocate role today. Neither does Writer, Notion, Webflow, Canva, Miro, or Jasper. Checking that by hand, one careers page at a time, costs an hour a week and is the first thing to get skipped. This runs in six steps and tells me only what changed.

**What it does not do.** It never applies to anything, never contacts anyone, and makes no judgment about fit — it matches words and hands me a list. Which of these is worth a day of my life stays my decision.

**Status: built and run once, 2026-09-26.** [`collect.py`](collect.py) works. It read **18 boards, 3,446 postings, and kept 88**. Both data files are here so anyone can check the filter:

- **[`all-jobs-2026-09-26.json`](all-jobs-2026-09-26.json)** · [`.csv`](all-jobs-2026-09-26.csv) — every posting found, kept or rejected, with the reject reason. Ad text omitted for size.
- **[`jobs-of-interest-2026-09-26.json`](jobs-of-interest-2026-09-26.json)** · [`.csv`](jobs-of-interest-2026-09-26.csv) — the 69 kept, with the words that matched, where they matched, and the full posting text.
- **[`quality-report-2026-09-26.md`](quality-report-2026-09-26.md)** — counts, rejects by reason, completeness, and what the run does not tell you.

The prediction ([`PREDICTIONS.md`](PREDICTIONS.md)) and acceptance criteria ([`VERIFICATION.md`](VERIFICATION.md)) were written before any of it ran, and the prediction was right: widening the company list, not loosening the keywords, is what cleared the record floor.

---

## Which assignment this is

The live Assignment 3 is **"Build Your Data Pipeline — Collect Data for Your Madison Agent"** (due October 2, 2026): an n8n workflow, 3+ data sources, 50–300 clean records, plus documentation, a demo, and quality numbers.

⚠️ **The brief in this repo says something else.** [`assignments/fall-2026/assignment-03.md`](../../../assignments/fall-2026/assignment-03.md) is "Visual identity system" — design tokens and an SVG specimen. That is the same mismatch Assignment 2 had. This folder follows the live assignment; the repo brief needs replacing.

## The Madison project this feeds

**Problem:** I am looking for advocate, educator, or education-adjacent work I can do while remaining a professor — remote, part-time, contract, or workshop-based. The companies whose tools I teach are the obvious place to look, and their job boards are public. Nobody is going to email me when a part-time Developer Educator opens at Webflow.

**From Assignment 2:** the dream job is a Figma Designer Advocate posting, and the gap analysis is [`../assignment-2/`](../assignment-2/). The seven-company sweep is in [`../advocate/`](../advocate/).

## Requirements checklist

Scored against the live brief. **Nothing is checked off yet** — this is the target, not a claim.

### Part 1 — Working data collection workflow (40 pts)

| Requirement | Plan | Done |
|---|---|---|
| Collects data that directly addresses the Assignment 2 problem | Job postings from the companies whose tools I teach and whose AI I teach with, filtered to advocate/education roles | ☑ |
| **At least 3 different data sources** | **Greenhouse API · Ashby API · SmartRecruiters API** — three services, three JSON shapes, three normalisers | ☑ |
| Saves in an organized format | `.json` and `.csv` for both files, plus the dated raw responses in `raw/` | ☑ |
| Runs on my computer and is repeatable | `python3 collect.py`; `--from-raw` re-filters with no network and reproduced both files | ☑ |
| 50–300 clean, relevant records | **88 kept** from 3,446 — the top of the "good enough" band and nearly "strong work" (100–200) | ☑ |
| Workflow runs without major errors (15) | 18 of 18 boards answered; a dead source is isolated per source | ☑ |
| Data relevant to the problem (15) | Every kept record names the words that matched and the field they matched in | ☑ |
| Usable, organized format (10) | Same columns every row, dates `YYYY-MM-DD` with the original string kept, source named per record | ☑ |

### Part 2 — Data documentation & demo (24 pts)

| Requirement | Plan | Done |
|---|---|---|
| Data inventory, template followed (8) | `DATA-INVENTORY.md`, one block per source with type, amount, purpose, method, quality, then the statistics block | ☐ |
| Setup guide (8) | `SETUP.md`: install, run, what needs installing first, common errors. **No API keys needed for any of the three** — worth saying explicitly, since that is why these sources were chosen | ☐ |
| Demo (8) | Screenshot walkthrough PDF, 5–8 annotated shots: workflow overview, key node configs, the run, sample output | ☐ |

### Part 3 — Data quality (16 pts)

| Requirement | Plan | Done |
|---|---|---|
| 80%+ records complete (8) | A record without title, link, or date is never written — so completeness on those three is 100% by construction, and the **real** number to report is completeness on the optional fields | ☐ |
| Essential info in every record (8) | title, date, source enforced at write time | ☐ |
| Duplicates removed | Collapse on source + posting id | ☐ |
| Consistent dates | All three sources' dates converted to `YYYY-MM-DD`; the original string kept alongside | ☐ |
| Quality numbers documented | [`quality-report-2026-09-26.md`](quality-report-2026-09-26.md) — script-counted: 3,446 fetched, 88 kept, rejects by reason, 0 duplicates, 100% completeness | ☑ |

### Excellence (20 pts, comparative)

| What they look for | What I intend |
|---|---|
| Clearly structured, easy to read (5) | Every column means one thing; source's own field names preserved so a reader can check any row against the live posting |
| Checks that catch mistakes (3) | Validators: non-empty title, parseable date, well-formed URL, expected record count asserted against what the API said it had |
| Quality numbers documented in detail (2) | A counts table the script writes, including rejects by reason — not just a pass rate |
| Handles problems without crashing (3) | Per-source try/except; unavailable source logged and skipped; the state file is never written on a failed run |
| Sources connected coherently (2) | Not three bolted-on feeds — three ATSs normalised to one record shape, which is the actual engineering problem |
| Thorough, professional documentation (3) | Executive summary first, annotated screenshots, clean layout |
| A peer could replicate it (2) | No keys, public endpoints, one command, the dated raw responses shipped so anyone can re-derive the filtered file |

### Submission

| Item | File | Done |
|---|---|---|
| n8n workflow export | `Brown_Nik_A3_Workflow.json` | ☐ |
| Documentation PDF | inventory + setup + quality numbers | ☐ |
| Data file | `jobs-of-interest.csv` | ☐ |
| Demo | screenshot walkthrough PDF | ☐ |

## The watch list

[`sources.json`](sources.json) — 13 boards across the three systems, probed 2026-09-26. [`ATS.md`](ATS.md) — which system each company uses, and a plain "unknown" for the five where it has not been verified.

**Every company is checked on every run whether or not it has a matching role today** — and that rule paid off within hours. **Vercel matched nothing in the morning run and had a *DevRel Engineer, Agentic Infrastructure* by the afternoon.** Miro, Airtable, and Jasper AI still match nothing and stay on the list.

| Source | Boards | Postings | Kept |
|---|---|---:|---:|
| Greenhouse | Anthropic, **Stripe**, **GitLab**, Figma, **Twilio**, HubSpot (`hubspotjobs`), Vercel, Miro (`realtimeboardglobal`), Webflow, **Netlify**, Airtable | 2,075 | 49 |
| Ashby | OpenAI, Notion, Replit, **Supabase**, Writer, Jasper AI | 1,146 | 29 |
| SmartRecruiters | Canva | 197 | 10 |
| **Total** | **18** | **3,446** | **88** |

**Six of the 88 are both remote and genuinely advocacy** — the answer to the question the tool exists to ask: **GitLab Senior Developer Advocate** (Remote US), **Supabase Developer Relations Engineer ×3** (Remote SF / NY / London), **Webflow Senior Developer Educator** (US Remote), **HubSpot Academy Professor** (Remote Ireland).

**That clears the 50-record floor without loosening a single keyword** — the prediction said widening the company list would do it, and it did. The biggest boards are the newest additions: **OpenAI 830** and **Anthropic 618**, which between them supply 40 of the 69.

**What Anthropic and OpenAI are actually hiring for** is the finding that matters beyond the assignment: *Developer Education Lead (Claude Platform)*, *Lead Technical Instructor*, *Head of Technical Training*, *Full Stack Engineer (Education Labs)* at Anthropic; *Tech Lead Manager, Education*, *Account Director, Higher Education*, *Full-Stack Engineer, ChatGPT Education & Learning* at OpenAI.

**Five companies cannot be read at all, and four are Tier 1** — Adobe, Salesforce, GitHub, Google (plus Shopify). No board on any of the three APIs under any slug tried, and I have not verified what they use instead, so `ATS.md` says *unknown* rather than naming a system. That gap is risk R9 in the SDD.

## On "three data sources" — the thing worth deciding

The brief says **at least 3 different data sources.** Two readings:

- **Three companies on one API** — Figma, Webflow, Miro, all Greenhouse. Simplest, but it is one source three times, and a grader could fairly say so.
- **Three different APIs** — Greenhouse, Ashby, SmartRecruiters. Genuinely three services with three different JSON shapes, three normalisers, three failure modes. **This is the stronger answer, and the work is already done** in the Reallocation Engine's `greenhouse-watch`.

Going with the second. Companies get added *within* each source to reach the record count:

| Source | Companies | Postings seen 2026-09-19 |
|---|---|---:|
| Greenhouse | Figma, Webflow, Miro (`realtimeboardglobal`) | 209 |
| Ashby | Notion, Writer, Jasper AI | 186 |
| SmartRecruiters | Canva | 248 |

That is 643 postings across three sources, of which the advocate/education filter kept a handful. **643 raw is more than the assignment wants and the filtered set is fewer than 50** — so the records that get shipped are the filtered set *widened by adding companies*, which is the honest way to reach 150–300: more boards, same filter. Companies to add are AI and developer-tool firms that actually hire advocates. `[TODO: DEFINE]` the list.

**A fourth source is available if 150 records proves hard from ATSs alone:** RSS feeds from company engineering and careers blogs, which are Tier 1 in the brief and need no key.

## Planned files

| File | What it will be | Status |
|---|---|---|
| [`collect.py`](collect.py) | Fetch → normalise → filter → dedupe → validate → write, one command, three sources | **done** |
| [`sources.json`](sources.json) | The watch list per ATS — adding a board is a data change, not a code change | **done** |
| [`keywords.json`](keywords.json) | Role, topic, and flexible-terms lists, plus per-company boilerplate to ignore | **done** |
| `raw/<provider>-<slug>-<date>.json` | Each response exactly as the API sent it. 32 MB/run, so **local only** — regenerate with `collect.py` | **done, not committed** |
| [`all-jobs-2026-09-26.json`](all-jobs-2026-09-26.json) · [`.csv`](all-jobs-2026-09-26.csv) | **Every** posting found, with kept/rejected and the reason | **done** |
| [`jobs-of-interest-2026-09-26.json`](jobs-of-interest-2026-09-26.json) · [`.csv`](jobs-of-interest-2026-09-26.csv) | The 69 kept, with matched words and full text | **done** |
| [`quality-report-2026-09-26.md`](quality-report-2026-09-26.md) | Counts, rejects by reason, completeness, limits | **done** |
| `DATA-INVENTORY.md` | The brief's inventory template, filled from real counts | not started |
| `SETUP.md` | Install, run, common errors | not started |
| `workflow.json` | The n8n export: Schedule → 3× HTTP Request → Code (filter) → Write File | not started |
| `test_collect.py` | Offline tests against saved responses: empty board, dead source, missing title, duplicate id, bad date | not started |

## The design document

[`SDD.md`](SDD.md) — the full Software Design Document for **Lectern**, the collector described above, generated by Gru in silent mode (`/g1 silent`) on 2026-09-26. Sixteen sections: problem summary, four architecture principles with a collision test, the three flows, eight needs mapped to components, six components with edge cases, the three API contracts with risk ratings, the data and domain models with six invariants, the CLI and output contracts, three sequence diagrams, a 21-component priority list with an MVS statement, ten out-of-scope decisions, infrastructure, an eight-row risk register, and eight open questions.

Its appendix states what silent mode skipped: no `/v0` gate, no phase gates, no pushback — so the V0 sentence is Gru's, not mine, and the open company list (Q1) would have stopped intake in interactive mode.

**Two findings from writing it.** The P1/CSV collision (source field names versus one header row) forced an explicit decision: the JSON is the evidence, the CSV is declared derived. And exactly one invariant — that a kept record's `original` stays byte-identical to the raw response — has no runtime enforcement, which is now risk R4 with a test instead of a shrug.

## The standard submission files

| File | What it holds | Status |
|---|---|---|
| [`PREDICTIONS.md`](PREDICTIONS.md) | The expectation and its measurable failure condition, dated before the first run | needs rewriting for this assignment |
| [`VERIFICATION.md`](VERIFICATION.md) | Acceptance criteria fixed in advance, and the checks as actually run | needs rewriting for this assignment |
| [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) | What the human did, what Claude did, what is still unreviewed | current |
| [`FRICTIONAL.md`](FRICTIONAL.md) | This assignment's process log (folder-level: [`../FRICTIONAL.md`](../FRICTIONAL.md)) | current |

## The honest note about scope

The tool matches words. A posting that says "we love teaching" in its culture blurb will match; a Developer Educator role that never uses any of my keywords will be missed. Both errors are real and neither is reported as accuracy. **No number this produces is a measure of how good a job is** — it produces a shorter list to read, and I do the reading.
