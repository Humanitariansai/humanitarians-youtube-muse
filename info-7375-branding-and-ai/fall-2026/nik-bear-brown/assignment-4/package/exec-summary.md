# Opportunity Matcher — Executive Summary

**What it is:** a deterministic job-opportunity matcher that scores postings
from 18 job boards plus a live Anthropic feed against a fixed CV profile,
routes each to PURSUE / NETWORK / WATCH / SKIP, and produces human-readable
outputs: a weekly digest, per-role briefs, and a run report.

**Problem:** 3,446 raw postings is not a job search — it's a pile. Manual
triage doesn't scale and keyword search returns noise.

**Solution:** five weighted scoring dimensions (role fit 0.30, audience fit
0.20, materials signal 0.20, CV-gap reward 0.15, company demand 0.15) with
open thresholds (PURSUE ≥ 0.65, NETWORK ≥ 0.45, WATCH ≥ 0.25). Two
implementations, one spec: a Python script and an equivalent n8n workflow.

**Measured results (2026-10-03):**

- 714 postings scored in 3.1 s; 22 PURSUE, 37 NETWORK, 325 WATCH, 330 SKIP.
- Scale-tested to 32,000 records: 3.72 ms/record, linear, peak memory 65 MB.
- Operating cost: $0.00/month — zero API calls, zero LLM calls in scoring.
- Outputs: one digest (markdown + HTML), 15 role briefs, one run report.

**Business value:** turns a weekly firehose into a 22-item action list with
reasons, links, and next steps — readable by a non-technical user, auditable
by an engineer. Every decision carries its rationale; every number traces to
a run report.

**What remains:** the scheduled delivery loop (human approval → weekly digest
→ email) is specified but not yet implemented — the single blocker before
this is a production service.

---

*Built with n8n + Python · deterministic scoring · no black boxes*
