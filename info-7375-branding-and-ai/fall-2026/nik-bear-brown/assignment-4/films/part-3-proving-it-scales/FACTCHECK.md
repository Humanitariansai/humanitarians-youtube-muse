# FACTCHECK.md — Muse proves it scales

## Verified (record)

1. 640 records → 2.37 s; 6,400 → 23.8 s; 32,000 → 119.1 s; 3.72 ms/record
   constant; peak RSS 52–65 MB → SCALE-TESTS.md, measured 2026-10-03 on the
   build VM. [record]
2. Fetch: 640 jobs, 9.2 MB, 6.2 s, HTTP 200, no rate limit → live curl to
   boards-api.greenhouse.io, 2026-10-03. [record]
3. The matcher makes zero API calls and zero LLM calls in scoring →
   matcher.py source inspection. [record]
4. Breaking point not found up to 32,000 records; n8n at scale, 429 behavior,
   and brief writes at scale untested → SCALE-TESTS.md "honest" section.
   [record]
5. Scheduled delivery (approval → weekly digest → email) specified but
   unimplemented → workflow_v2.json. [record]

## Judgments (judgment)

- "Production volume sits two orders of magnitude below anything tested"
   extrapolates from measured linearity to ~1,000 postings/week. [judgment]
- "Scale is boring; delivery is the blocker" is the film's verdict, argued
  from the measurements. [judgment]
- Cost $0.00/month is estimated from zero measured API/LLM spend, labeled as
  estimated in the film. [judgment]

## Cut

- No claim that n8n handles 50x — untested, not in the film.
- No claim about Greenhouse rate limits beyond the single measured fetch.
