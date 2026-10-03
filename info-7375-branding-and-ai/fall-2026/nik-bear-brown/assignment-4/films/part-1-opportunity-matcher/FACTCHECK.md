# FACTCHECK.md — "Muse builds the opportunity matcher" (Gate F)

Source of truth: `assignment-4/FRICTIONAL.md`, `matcher.py`,
`workflow_v2.json`, `outputs/run-report-2026-10-03.json`,
`anthropic-equivalents-2026-10-03.md`, `meta-board-note-2026-10-03.md`.
Every number below is record from those files.

## Beat-by-beat claims

| # | Beat | Claim | Verdict |
|---|---|---|---|
| 1 | B01 | Assignment 3: 3,446 postings, 18 boards, 97 kept | record (`jobs-of-interest-2026-09-26.json` counts) |
| 2 | B02 | Part 1 demands decisions, not storage | the assignment brief (judgment framing) |
| 3 | B03 | Five dimensions with weights 0.30/0.20/0.20/0.15/0.15 | record (`matcher.py` WEIGHTS); voiced as judgment |
| 4 | B04 | Thresholds 0.65/0.45/0.25 → PURSUE/NETWORK/WATCH/SKIP | record (`matcher.py` THRESHOLDS); voiced as judgment |
| 5 | B05 | Rationales quote the fired signals | record (brief files show this) |
| 6 | B06 | 714 postings in 3.1 s | record (run report `elapsed_s`) |
| 7 | B07 | n8n: 11 nodes, same spec, validated | record (node count checked, no dangling refs) |
| 8 | B08 | Anthropic: 640 postings live; Developer Education Lead at 0.91 | record (live pull + digest) |
| 9 | B09 | Meta board unreadable; no "Muse for Education" role found | record (meta-board-note; the negative search result is stated as such) |
| 10 | B10 | First run: 633 of 714 in WATCH | record (first run-report, superseded) |
| 11 | B11 | Pairing rule; operationalizes the "train their own people" reversal | judgment, attributed to the 2026-09-26 log |
| 12 | B12 | Claude Docs 0.46 → 0.66; "own the documentation" 2/737 hits, both right; "documentation for" 8 hits rejected | record (measured counts in FRICTIONAL.md) |
| 13 | B13 | Final 22/37/325/330, 0 quarantined | record (run report) |
| 14 | B14 | Digest md+html, 15 briefs, run report | record (outputs/ listing) |
| 15 | B15 | Retry/backoff, quarantine, cached fallback | record (ERROR-HANDLING.md + code) |
| 16 | B16 | Muse wrote scripts, ran analysis, tuned, pushed | record (the repo) |
| 17 | B17 | Push script bug: 25 failed, 0 up; fixed, all landed | record (yesterday's session, logged) |

## Deliberately cut / never claimed

- **"The matcher is AI"** — it is deterministic scoring; the film calls it
  the intelligence layer and notes the LLM seam, never claims reasoning.
- **Precision/recall figures** — none measured; the film does not invent any.
- **Meta demand** — absence is labeled a measurement gap, never "no demand".

## PROMPTS.md

No paid generation prompts. All visuals are Manim (free) or library Remotion
components (free). No Higgsfield or other paid beats.
