# Assignment 2, Part 1 — Appendix: one board is not a search

## Executive summary

**What this is.** After picking my Figma dream job I asked the obvious next question: *what if the right posting is at a company I didn't check?* So I widened the search to the seven design-tool companies I could reach with a public job-board feed — Figma, Writer, Canva, Miro, Webflow, Notion, Jasper — and pulled every open posting from all of them on the same afternoon: 643 postings across three different applicant-tracking systems. This appendix shows how, what it cost, and what changed.

**Why read it.** Because the assignment says "find one real job posting," and the trap in that sentence is *one*. A student who picks the first plausible posting has done Part 1; a student who looks at the field and then picks has done Part 1 *and* Part 2's homework. This is also the honest record of building a scraper for a system nobody had wired up yet (Canva's SmartRecruiters) — the kind of "Excellence: research the actual tech stack" work the rubric rewards.

**What changed.** The wider look found a better fit than the one I chose from Figma alone: **Webflow's Senior Developer Educator** — a new position, US-remote, $113K–$155K, on camera, building the reference sites behind Webflow University. My Figma pick stands as the Assignment 2 dream job (it is the company my students use), but the gap analysis in Part 2 now has a second column to compare against. The sweep also found that **the title I should be searching is "Educator," not "Advocate"** — two of the six best matches never use the word.

**What it did not find.** A part-time, contract, or consulting education role in the US at any of the seven. Canva posts 23 contract roles and Writer one, so the shape exists — it just is not being posted for the work I do, in my geography, this month.

---

## Three ATSs, one script

Every big company runs its careers page on an applicant-tracking system, and most of those expose a public JSON feed of open postings — no key, no login. The reallocation engine's `greenhouse-watch` skill started as a Greenhouse-only watcher; today it reads three:

| ATS | How you spot it | Feed | Companies here |
|---|---|---|---|
| Greenhouse | `boards.greenhouse.io/<slug>` or `job-boards.greenhouse.io/<slug>` | `boards-api.greenhouse.io/v1/boards/<slug>/jobs?content=true` — one call, full ad text | Figma, Webflow, Miro (slug `realtimeboardglobal`, their old name) |
| Ashby | `jobs.ashbyhq.com/<name>` | `api.ashbyhq.com/posting-api/job-board/<name>` — one call; names can have spaces (`Jasper AI` → `Jasper%20AI`) | Writer, Notion, Jasper |
| SmartRecruiters | `careers.smartrecruiters.com/<Company>` | `api.smartrecruiters.com/v1/companies/<Company>/postings` — paged, 100 at a time, **no ad text**; one more call per posting for the description | Canva |

The SmartRecruiters provider was the new work. Its listing feed gives you titles, locations, employment type, and a `remote` flag, but not the job description — so matching against a résumé means one extra call per posting. Canva has 248 open jobs; the run took 3 minutes 38 seconds and 251 requests to one host. That is the cost of "research the actual tech stack": not hard, just patient.

Three companies on my list could not be read this way, and saying so is part of the answer: **Framer** hand-builds job pages on its own site (no feed); **Adobe** is on Workday, which needs a different scraper and a title filter before you touch a board that size; **Sketch, InVision, Mural** are unconfirmed (InVision wound down its design products in 2024).

## What the seven boards look like side by side

| Company | Postings | Word-matched to my CV | Remote | Contract / contingent | Advocate or educator roles |
|---|---:|---:|---|---|---|
| Figma | 152 | 55 | 85 "US hubs or remote" | 0 | 3 |
| Writer | 51 | 24 | 0 remote-only; 51 hybrid | 1 | 1 |
| Canva | 248 | 64 | 47, all outside the US | 23 + 43 | 0 in the US |
| Notion | 128 | 43 | 0 remote-only; 84 hybrid | 1 (+1 temp, 2 interns) | 2 |
| Webflow | 29 | 21 | 22 | 0 | 1 |
| Miro | 28 | 3 | 4 | 0 | 0 |
| Jasper | 7 | 6 | 7 | 0 | 0 |

"Word-matched" is exactly that — a rule set matching skill words on my CV to words in the posting. It is a filter for my reading, not a judgment. At Writer it flagged 51 of 51 on the first pass because *generative AI*, *AI agents*, and *learning* are in every posting's company blurb; ignoring those three words (a change to the rules, not the résumé) brought it to 24. That is the kind of failure a student should expect to hit and write down.

## The six roles that fit the criterion

See [`../advocate/advocate-roles-2026-09-19.md`](../advocate/advocate-roles-2026-09-19.md) for the full table with links and my status on each. In one line each:

1. **Webflow — Senior Developer Educator** (US remote, new, $113K–$155K) — keep; closest to my work at a location I can hold.
2. **Figma — Designer Advocate** (US hubs, $153K–$317K) — keep; the Assignment 2 dream job.
3. **Notion — Technical Education Specialist** (NYC, 3 days in office) — keep; best description, wrong geography.
4. **Notion — Developer Advocate** (NYC/SF, posted May) — keep; check whether it is still real.
5. **Writer — Senior AI learning designer, rapid content** (hybrid, 6 hubs, $153K–$200K) — keep; no AI voice allowed, I'd be on camera.
6. **Figma — Designer Advocate, Partnerships** (SF) — consider.

## Evidence

- `evidence/smartrecruiters-canva-report.md` — the Canva pass (248 postings, 64 flagged), the first run of the new provider.
- The reallocation engine holds the per-company ALL / TENTATIVE / KEEP files and the code: `github.com/nikbearbrown/the-reallocation-engine`, `reports/greenhouse-watch/` and `.claude/skills/greenhouse-watch/`.
- My CV JSON is not in either repo. Only skill words already on my public CV appear in any report.
