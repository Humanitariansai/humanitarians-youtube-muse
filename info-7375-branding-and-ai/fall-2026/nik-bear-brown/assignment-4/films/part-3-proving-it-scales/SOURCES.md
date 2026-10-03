# SOURCES.md — Muse proves it scales

| Fact | File |
|------|------|
| Scale numbers (640→2.37s, 6400→23.8s, 32000→119.1s, 3.72ms, 52–65MB) | `assignment-4/SCALE-TESTS.md` |
| Fetch (640 jobs, 9.2MB, 6.2s, HTTP 200) | live curl, 2026-10-03; also in SCALE-TESTS.md |
| Zero API/LLM calls in scoring | `assignment-4/matcher.py` source |
| Untested: n8n at scale, 429 behavior, brief writes at scale | SCALE-TESTS.md "honest" section |
| Scheduled delivery unimplemented | `assignment-4/workflow_v2.json` |
