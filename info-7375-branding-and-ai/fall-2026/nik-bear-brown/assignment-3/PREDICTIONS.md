# Predictions — Assignment 3, the job-collection pipeline

Written **before** the collector is built or run. Nothing below has been executed.

## Before the run

**Date:** 2026-09-26

**Question:** Will three public job-board APIs, filtered on education and advocacy words, produce 150–300 clean records — and will the filter's mistakes be the ones I expect?

**Expected result:**
1. **The record count will be the problem, not the plumbing.** The three ATSs return plenty of postings (643 across seven companies on 2026-09-19), but the education/advocate filter keeps very few — six roles across four companies in the sweep. I expect to need roughly **20–30 companies**, not seven, to reach 150 kept records honestly.
2. **The false positives will come from culture blurbs.** Postings that say "we love to teach each other" or list "community" as a value will match on topic words while being ordinary engineering jobs. I expect **more than a quarter** of raw matches to be this.
3. **The false negatives will be title-only matches I never see.** A "Technical Curriculum Lead" whose body text never uses my topic words will match on title alone and score as weakly as a culture-blurb hit, so a threshold tuned to kill the blurbs will also kill real roles.
4. **SmartRecruiters will be the slowest and most fragile source** — its listing feed carries no ad text, so it needs one extra HTTP call per posting (248 calls for Canva alone, about 3½ minutes).

**Confidence and reason:** High on (1) and (4) — both are measured facts from the 2026-09-19 run, not guesses. Medium on (2). Low on (3): it is a claim about the shape of the errors, and the only way to know is to read the rejects.

**Assumptions:**
- All three APIs stay open and keyless. If one starts requiring a key, that source is replaced by an RSS feed, not worked around.
- "Clean" means title, link, and date present and a parseable date — not that the posting is a good job.
- The dated raw responses are the evidence. Any kept record must be re-derivable from them.

**Measurable failure condition:** If the filter keeps fewer than 50 records after the company list is widened to 20+, the approach has failed as stated and I will say so, rather than loosening the keywords until the number looks right. **Loosening the filter to hit a record count is the specific dishonesty this prediction exists to catch.**

**Observation that would change my mind:** A clean 150+ from seven companies, meaning the filter is much looser than I think — which I would then have to check by reading rejects, because it would more likely mean the filter is broken than that the market is generous.

## After the run — append, do not rewrite above

**Actual output and evidence path:** _not run yet_

**Difference from prediction:** _not run yet_

**Revised understanding and remaining uncertainty:** _not run yet_
