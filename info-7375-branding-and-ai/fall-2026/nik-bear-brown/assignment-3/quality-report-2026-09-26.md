# Lectern run — 2026-09-26 (final pass)

## Executive summary

**What ran.** 18 job boards, three applicant-tracking systems, **3,446 postings**, **97 kept**. Data: [`all-jobs-2026-09-26.json`](all-jobs-2026-09-26.json) (every posting, with the reject reason) and [`jobs-of-interest-2026-09-26.json`](jobs-of-interest-2026-09-26.json) (the kept ones, with the words that matched and the full text).

**What the target became.** It started as "advocate or educator roles." It is now **any job whose product is teaching materials** — for universities, for the public, or for the company's own staff. Anthropic's *Technical Documentation and Content Engineer, Claude Docs* is the model, and the two roles that best fit it were both invisible to the first filter:

| Found this pass | Where | Caught by |
|---|---|---|
| **Anthropic — Technical Documentation and Content Engineer, Claude Docs** | SF · NYC | title word `documentation` / `content engineer` |
| **Replit — Learning Experiences Creator** | Foster City, CA | title word `learning experiences` / `creator` |
| **Stripe — Training Program Manager** | Mexico City | body: *instructional design* |
| **OpenAI — AI Deployment Manager (Builder)** ×2 | SF · Tokyo | body: *instructional design* |
| **OpenAI — Developer Experience Engineer, Cyber** | SF | body: *create tutorials* |

**The one that should not have been missed.** Replit's *Learning Experiences Creator* is as close to a bullseye as this board has, and the filter rejected it because the list held `learning designer` and not `learning experiences`. One word.

**Three rules, and only one of them was ever measured honestly.** A posting is kept on a role word in its title, on three teaching words in its body, or — new this pass — on the body saying it produces teaching materials. The third rule had to be measured because it failed loudly: the first version kept **101 extra postings at roughly one-in-ten precision**, including all 15 Anthropic *Applied AI Architects* (matched *technical content* + *our users*) and four IT Support Engineers (matched *how-to guides*). Nine phrase groups were cut and it now contributes **5 postings, 4 of them right**. The other two rules have never been measured this way.

**A false positive that turned out not to be one.** The previous pass called 13 sales-enablement postings errors. They are not: building curriculum and running training for a company's own staff is the work, and an internal audience does not change that. `SALES_ENABLEMENT` now expects *keep*, and the 9 education-sales roles moved to *judge* — an account executive with only a quota is still a reject, one who builds the materials the sale runs on is not.

---

## Counts

| | |
|---|---:|
| Postings fetched | 3,446 |
| **Kept** | **97** |
| Rejected | 3,349 |
| Duplicates collapsed | 0 |
| Completeness (title, url, date, location, department) | 3,446 / 3,446 |

### How the 97 were kept

| Rule | Count |
|---|---:|
| role word in title | 83 |
| 3 topic words in body (>= 3) | 5 |
| body says it produces teaching materials for a named audience | 5 |
| 4 topic words in body (>= 3) | 4 |

### Rejections

| Reason | Count |
|---|---:|
| no-keyword-match | 2,341 |
| only 1 topic words, no role word in title | 945 |
| only 2 topic words, no role word in title | 63 |

## What this run does not tell you

- **The two older rules are unmeasured.** The body-materials rule has a precision figure because it failed obviously. "Role word in title" and "three topic words" do not, beyond what the title audit surfaced.
- **`enablement` is still the most-matched word** and still means several different jobs. It is now expected to keep, which is a decision about what the searcher wants, not a fact about the postings.
- **Five words are known false friends here:** `training` (model training), `enablement` (sales support, or a system gaining a capability), `education` (a degree requirement in Anthropic's footer, a sales vertical at Canva), `learning` (machine learning — never added), `content` (SEO marketing).
- **535 postings sit in *judge* families** in [`title-audit-2026-09-26.md`](title-audit-2026-09-26.md), unresolved.
- **The watch list is incomplete.** Nine companies cannot be read at all; four are Tier 1 education players. See [`ATS.md`](ATS.md).
- **One day.** These counts are a snapshot; the state file exists so tomorrow reports only what changed.

## Reproduce

```bash
python3 collect.py                    # fetch 18 boards, filter, write both files
python3 collect.py --from-raw raw/    # no network; re-filter the saved responses
python3 audit_titles.py --all-jobs all-jobs-2026-09-26.json --out title-audit-2026-09-26.md
```
