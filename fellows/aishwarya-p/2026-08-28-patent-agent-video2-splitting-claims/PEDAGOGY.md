# PEDAGOGY — Splitting the Claims (hai cli-explainer, patent agent progress video 2/3)

A progress-recap video documenting the real build and stress-test of the Claims Agent's claim-splitting logic, including a genuine false-positive investigation. Presenter intro included per current fellow requirements.

## Act structure

- B00A presenter intro — states the fellow's name and the video's actual topic ✓
- B00 cold open, ClaudeComposerAsk, states the real stakes (20 claims, one regex, all-or-nothing correctness) ✓
- B01 — the real split/classify method, as actually implemented ✓
- B02 — the real first test result: 20/20 correct on US-11791319-B2, verified by hand ✓
- B03 — the real stress test: 3 more patents, 44 more claims, all held up ✓
- B04 — the real, honest false-positive catch: a flagged claim traced by hand and found to be a false alarm, with the actual root cause named (an unrelated "or" in the claim body, not a real multi-dependency) ✓
- B05 — HANDOFF, a runnable prompt that includes checking flagged claims by hand, not just trusting the parser ✓
- B06 — OUTRO, title restate ✓
- `folderLabel` set to `@HumanitariansAI` and greeting kept short from the start ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| "20 claims... 3 independent, 17 dependent" on US-11791319-B2 | Real test run this session, output verified by hand against raw BigQuery text | OK — genuinely verified, not asserted |
| "44 more claims" across 3 more patents (7+17+20) | Real test run this session (test_multi_dependent.py output) | OK — real counts from real output |
| The false-positive detail (Claim 5, "bumps or projections") | Real raw text pulled and inspected by hand this session | OK — the actual quoted fragment matches the real BigQuery response |

## Friction protected

- Kept: the false-positive is presented honestly as a flaw in the *detector*, not glossed over as if the parser were flawless — the video's whole B04 beat exists specifically to show a real mistake being found and correctly diagnosed.
- Kept: B05's handoff explicitly tells the viewer to check flagged claims by hand rather than trust the tool blindly — the same discipline the video itself just demonstrated.

VERDICT: PASS
