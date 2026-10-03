# Error Handling — Opportunity Matcher v1

## What could go wrong

- Greenhouse API rate limit or timeout (HTTP 429 / socket timeout)
- Greenhouse API returns an error page or empty body
- A posting is malformed (no title, no text, unexpected shape)
- The CV facts file is missing or unattested
- The kept-postings file is missing or unparseable
- The live pull is unloadable mid-run

## How we handle it

| Failure | matcher.py | workflow_v2.json (n8n) |
|---|---|---|
| API rate limit / timeout | `fetch_with_retry`: 3 tries, exponential backoff (2s, 4s, 8s); then `FetchError` → run continues on the cached Assignment 3 file, digest flagged "cached" | HTTP node: `retryOnFail`, `maxRetries: 3`, 30s timeout; on final failure the error-output branch fires |
| Error page / empty body | JSON parse guarded; unloadable live data → logged in `errors`, run continues on kept postings | Error branch → "Log the failure" code node → fallback to cached file |
| Malformed posting | Per-record try/except → `quarantine.log` with reason + preview; counted in run report; never crashes | Per-item try/catch in the Normalize code node; bad items pushed to a quarantine list |
| Missing title | Quarantined as "missing title" | Same — normalize drops it with a logged reason |
| CV missing / unattested | Fatal, exit 2 — the gaps come from attested record; refusing to score without it is the correct behavior | Sticky note: connect a "Check attestation" IF before scoring in production |
| Kept file missing | Fatal, exit 2 — there is no run without input data | Same — workflow stops with a clear error, no silent empty digest |

## What happens when things go wrong (the promise)

1. The run never dies silently: every failure is counted and named in the run report.
2. The digest still ships on cached data rather than shipping nothing — but it says so.
3. Nothing is invented to fill a gap: a missing field gets a documented default (company demand 0.5, empty text), never a guessed value.
