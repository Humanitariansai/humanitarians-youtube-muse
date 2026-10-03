# ACTS.md — Muse proves it scales

Film 3 of 4. Assignment 4, Part 3: test at scale — single request, 10x, 50x,
the breaking point, rate limits, timeouts, memory, cost, production readiness.

**Exact title:** Muse proves it scales

**Core promise:** By the end, the viewer knows the real numbers (3.72 ms per
record, linear to 32,000), knows the breaking point was honestly not found,
knows what was NOT tested, and knows the cost is effectively zero — measured
and estimated clearly separated.

**Structure:** Four acts.

- Act I — The test design (2 beats): what we measured; the honest method.
- Act II — The results (3 beats): the table; the linear line; the fetch side.
- Act III — What we didn't break (2 beats): the missing breaking point;
  cost per 100 and monthly.
- Act IV — The verdict (1 beat): production readiness, judged.

**Tone:** engineering honesty. The film's hero moment is a negative result —
the breaking point wasn't found — reported as such, with the untested
territory named, not hidden.

**What this film is not:** not a rebuild of scoring (film 1); not the gallery
(film 2); not the sales pitch (film 4).

**Source facts:** SCALE-TESTS.md (2026-10-03): 640 → 2.37 s; 6,400 → 23.8 s;
32,000 → 119.1 s; 3.72 ms/record constant; peak RSS 52–65 MB; fetch 640 jobs /
9.2 MB / 6.2 s, HTTP 200, no rate limit. Breaking point: not found. Cost:
$0.00 (zero API/LLM calls). Untested: n8n at scale, 429 behavior, brief writes
at scale. Blocker before production: scheduled delivery unimplemented.
