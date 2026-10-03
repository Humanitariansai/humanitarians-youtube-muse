# SCALE-TESTS.md — Opportunity Matcher scale measurements

Date: 2026-10-03. Method: replicate real Anthropic live records (same shape
as production data) with unique ids at 1x / 10x / 50x; time the full
dedup + score + route pipeline; record peak RSS. Fetch measured separately
with a live Greenhouse pull.

## Measured (record)

| Scale | Records | Total time | Per record | Peak RSS |
|-------|---------|-----------|------------|----------|
| 1x | 640 | 2.37 s | 3.71 ms | 51.9 MB |
| 10x | 6,400 | 23.8 s | 3.72 ms | 52.7 MB |
| 50x | 32,000 | 119.1 s | 3.72 ms | 64.7 MB |

- Per-record cost is constant: **3.72 ms**, perfectly linear to 32k records.
- Memory grows gently (52 → 65 MB); no memory cliff observed. A second run
  with fully distinct (deep-copied) records at 10x showed the same 52 MB —
  records are small and scoring accumulates nothing.
- Fetch side: one live Greenhouse pull returned **640 jobs / 9.2 MB in
  6.2 s** (HTTP 200, no rate limit, no retry needed).

## Breaking point (honest)

- **Not found in scoring.** At 50x the run takes two minutes and works.
  Extrapolating the linear rate, 100k records ≈ 6.2 minutes — boring, not
  broken.
- **Not tested:** n8n-side execution at scale; rate-limit behavior beyond one
  board per ~6 s (we did not hammer the API to find the 429); brief-file
  writes at scale (15 files at 1x; a 50x run would emit ~1,000 briefs —
  disk I/O unmeasured).
- The realistic production volume (dozens of boards, low thousands of
  postings weekly) sits two orders of magnitude below anything measured here.

## Cost (estimated — clearly separated from measured)

- Measured: the matcher makes **zero API calls and zero LLM calls**. Cost per
  100 postings = 0.37 s of CPU on commodity hardware ≈ **$0.00**.
- Estimated: a weekly production run (~1,000 postings, one live fetch) costs
  ~4 s CPU + one 6 s HTTP fetch ≈ **$0.00/month** on existing infrastructure.
  The only real cost is engineering time to maintain the vocabulary tables.

## Production-readiness assessment (judgment)

- Scoring: production-ready at any realistic volume.
- Fetching: single-threaded, polite; add retry/backoff per board before
  scheduling (error handling is documented in ERROR-HANDLING.md).
- Delivery: the scheduled approval + weekly digest + email step is specified
  but unimplemented — the one blocker before this is a real service.
