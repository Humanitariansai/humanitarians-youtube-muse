# Assignment 2, Part 1 — My Dream Job at Figma (worked example)

## Executive summary

**What this is.** The instructor's own answer to Part 1 of Assignment 2 ("find one real job posting you could apply to in 6–12 months"). I did it for real: I want remote part-time, consulting, or educational-material work with a company whose tools I already teach, and Figma is that company. This page shows the posting I chose, the three requirements I will be measured against, and how I found it.

**Why read it.** Because the point of the assignment is not the job — it is the honesty. Students tend to pick a posting that flatters them. This example picks one that exposes a real gap (I have never shipped a design system in Figma), documents a real disappointment (Figma has no part-time or consulting roles at all), and shows a machine ranking 55 postings *and then a human overriding it*. That override is what Part 2 and the rest of the course are about.

**The answer.** **Designer Advocate, Figma** — full-time, US hubs, $153K–$317K, posted September 1, 2026. The job is making written, visual, and video teaching material for the design community, which is what I already do; the gap is hands-on Figma design-systems depth, which the Madison project will close. Runner-up: Researcher, Figma Agentic Experiences (the one remote-OK role that reads like my Computational Skepticism course, but wants 7+ years of UX research).

**Student:** Nik Bear Brown · **Board:** Figma (Greenhouse) · **Checked:** 2026-09-19 · **Part 1 of 4** · 10 pts

**Appendix:** [one board is not a search](part-1-appendix-seven-boards.md) — the same method run on seven companies and three ATSs, which found a closer fit (Webflow's Senior Developer Educator, US remote) and changed what word I search for.

---

## How I found it (method, so you can repeat it)

I did not scroll the careers page. I ran the `greenhouse-watch` skill from
*The Reallocation Engine* against Figma's public Greenhouse board
(`https://boards-api.greenhouse.io/v1/boards/figma/jobs`) with a JSON version of my CV
and a matching scheme I wrote for this pass (`evidence/scheme.bear-figma.json`).

- One fetch, 152 open postings, raw response saved.
- Scheme `bear-figma-0.1` flagged 49 as relevant, 103 skipped. Every flag is a
  string-match rule between a named résumé field and a named posting field — no model
  judgment. Full list with justifications: `evidence/greenhouse-watch-figma-report.md`.
- The machine stops there. Choosing among the 49 was my call, and the choice below is
  **not** the top score. The top scores (AI Applied Scientist, Forward Deployed Engineer,
  Marketing Engineer, all 11.5) are full-time engineering roles; they match my skills but
  not my goal.

**What the board does not have (honest finding):** zero part-time, contract, freelance,
or consulting roles. 85 of 152 postings allow "remotely in the United States," so remote
is common — but every one of them is a full-time employee role. The Designer Advocate
posting is one of the hub-only ones. No "Education", "Learning",
"Curriculum", or "Content" titles exist; the nearest family is *Advocacy*
(3 Designer Advocate postings) and *Customer Enablement* (5, all non-US).

## The posting

| | |
|---|---|
| **Company** | Figma |
| **Title** | Designer Advocate |
| **Link** | https://boards.greenhouse.io/figma/jobs/6176134004?gh_jid=6176134004 |
| **Location** | San Francisco, CA · New York, NY · United States (full time, US hub) |
| **Department** | Marketing → Advocacy team |
| **Posted / updated** | 2026-09-01 / 2026-09-09 |
| **Pay band (posted)** | $153,000 – $317,000 base |
| **Greenhouse job id** | 6176134004 |

**Runner-up, kept for Part 2:** *Researcher, Figma Agentic Experiences* (id 5651744004) —
the one posting on the board that is explicitly "remotely in the United States" and is
about evaluating AI experiences "where the output is nondeterministic and 'did it work?'
is a judgment call." That sentence is my Computational Skepticism course in one line.
It wants 7+ years of UX research at a B2B SaaS company, which I do not have.

## Top 3 technical requirements (quoted from the posting)

1. **"Deep, hands-on expertise in Figma, modern product and visual design workflows, and
   design systems, with a strong understanding of how design translates into development."**
2. **"Comfortable navigating evolving workflows and technologies, including design systems,
   tokens, AI-assisted design, and prototyping."**
3. **"Develop written, visual, and video resources that reflect how modern teams actually
   design and build, from early exploration to production-ready systems."**

Plus a non-technical gate I have to be honest about: public speaking at meetups and
conferences, and **travel up to 25%**.

## Why this one (one sentence)

It is the only US posting on Figma's board whose *job* is what I already do all day —
make written, visual, and video teaching material and champion a community of builders —
and the scheme's own justification lines (`video`, `community`, `design systems`,
`Figma`, `prototyping`) are the five words I would put on the cover letter.

## Why this is "6–12 months," not "now"

The posting wants design-practitioner depth in Figma itself. I teach *Branding and AI*
with Figma boards and have an MS in Information Design and Visualization, but I have
never shipped a design system in Figma with tokens and Dev Mode handoff. That is the
first gap in Part 2, and Madison is how I close it.

## Excellence: hiring manager

Not yet found. The posting names the team (Advocacy, reporting into Marketing) but no
person. Next step is a LinkedIn search for "Designer Advocate" + "Figma" to find the
current advocates and who they report to — **I will do that by hand and record the name
here; no tool in this pipeline scrapes LinkedIn.**

## Evidence in this folder

| File | What it is |
|---|---|
| `evidence/greenhouse-watch-figma-report.md` | the human report: 49 relevant / 103 skipped, with a justification line per rule hit |
| `evidence/greenhouse-watch-figma-run.json` | the machine record of the same run |
| `evidence/scheme.bear-figma.json` | the matching rules I wrote; the comment explains each change from the default |
| `evidence/figma-advocate-roles.md` | the narrowed list — only Figma's three Designer Advocate postings and their enablement neighbours, with keep / consider / pass |

My résumé JSON is **not** in this folder — it lives in the engine's gitignored
`search/resume.json`, which is the rule for real résumés. The scheme and the report
contain only skill words that are already on my public CV.
