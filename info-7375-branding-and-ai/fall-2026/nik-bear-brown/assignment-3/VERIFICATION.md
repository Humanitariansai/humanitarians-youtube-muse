# Verification of the shipped candidate — Assignment 3

**Nothing has been verified yet.** This file holds the acceptance criteria, fixed **before** anything runs. Every other field gets filled in from an actual run, never from an expectation.

**Candidate version or content identifier:** _pending — the commit hash of the shipped collector and data file goes here and in Canvas._

**Input sources and fixture/simulation/live labels:** Three **live** public APIs — Greenhouse (`boards-api.greenhouse.io`), Ashby (`api.ashbyhq.com`), SmartRecruiters (`api.smartrecruiters.com`) — each response saved dated under `raw/`. The tests run **offline** against saved responses and are labelled as fixtures. No key, no login, no account for any of the three.

**Environment and exact commands:** _pending — the actual `python3 collect.py …` invocation, the test command, the Python version, and the n8n version used for the workflow export._

**Acceptance criteria fixed before checking:**
1. **Re-derivable.** Running the filter again over the saved `raw/` responses reproduces `jobs-of-interest.json` byte-identically. If it cannot be re-derived from the raw files, it is not evidence.
2. **Field names unchanged.** Every field in a kept record appears with the same key and value as in that source's raw response. A diff of each kept record against its raw original shows changes only in the one added `matched` key.
3. **Completeness enforced, not claimed.** No written record is missing title, link, or date. The quality report states completeness for the *optional* fields, which is the number that actually varies.
4. **Duplicates.** Two runs in one day, and a job appearing on two boards, both collapse on source + id. The count of collapsed duplicates is reported.
5. **A dead source does not kill the run.** With one source pointed at an unreachable host, the other two still produce a file, the failure is logged as unavailable, and the state file is **not** written.
6. **Dates.** Every record's normalised date parses as `YYYY-MM-DD`, and the source's original date string is kept beside it.
7. **Counted, not estimated.** Fetched, kept, rejected-by-reason, and duplicate counts come from the script. Fetched is asserted against the count the API itself reported (`totalFound` on SmartRecruiters, the array length elsewhere).
8. **Two records checked by hand.** Two kept postings opened in a browser and compared field by field against the shipped row — including confirming the matched words really appear where the record says they do.
9. **Rejects read, not just counted.** At least 20 rejected postings read by eye to classify the false negatives, and the finding written up whether or not it flatters the filter.

**Expected result from independent source or calculation:** The two hand-checked postings in (8) and the reject sample in (9). The script's own counts are not a check on the script.

**Observed result and evidence path:** _pending._

**Checks that failed and subsequent revision:** _pending. Failures are recorded with the repair, not edited out._

**Shared assumptions or possible common errors:** The collector, its tests, and the fixtures would be written in one session by one agent, so all three can share a wrong belief about a source's shape — especially Ashby's `isRemote`, which is a listing flag and does **not** mean the role is remote (that error was already made once, on 2026-09-19, and caught). The hand checks in (8) exist for that.

**Remaining limits:** The tool matches words. Culture-blurb false positives and keyword-free false negatives are both expected and neither is reported as accuracy. No number here says whether a job is good. Record counts describe seven-plus companies' boards on one day, not the job market.

**Actual reviewer or automated checker:** _pending._

**Final handoff decision and owner:** _pending — Professor Bear._

Put the final Git commit hash in Canvas after committing this file. Do not invent a human signature or claim checks that were not run.
