# PEDAGOGY — Survivorship Bias in Financial Datasets (hai ai-explainer)

A single-concept explainer: a historical dataset built from today's surviving companies silently omits the ones that failed, making a backtested strategy's past performance look better than it actually was. Presenter intro included per current fellow requirements.

## Act structure

- B00A presenter intro — states the fellow's name and the video's actual topic ✓
- B00 cold open, ClaudeComposerAsk, the confident "12% annually" claim shown as if simply true ✓
- PROBLEM beat (B01) before any fix is shown — states what's actually missing from the dataset ✓
- CONCEPT beat (B02) — the fix: point-in-time data construction ✓
- CONCEPT beat (B03) — the real stakes, with genuine cited research rather than an invented statistic ✓
- HANDOFF (B04) — a runnable prompt, read and discussed ✓
- OUTRO (B05) — title restate, Humanitarians AI branding ✓
- `folderLabel` set to `@HumanitariansAI` on every ClaudeComposerAsk beat from the start (lesson carried over from the two prior videos' reviewer feedback) ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| "This strategy returned 12% annually over 20 years" (B00) | Illustrative example, explicitly built to demonstrate the concept — not a real fund's real result | OK — presented as illustrative, not attributed to any real fund |
| Grinblatt & Titman (1989) found survivorship effect of 0.1-0.4 percentage points/year | Stephen J. Brown, "Survivorship Bias in Performance Studies," New York University, citing Grinblatt and Titman (1989) directly | OK — real, named study, verified via web search before drafting this line |
| Kothari, Shanken & Sloan (1995) found excluded-firm returns differed by 9-10 percentage points | Econrsa working paper citing Kothari, Shanken and Sloan (1995) | OK — real, named study, verified via web search |
| Amin & Kat (2001) estimated survivorship bias in hedge fund peer indices averages ~2% per annum | USPTO patent filing citing Gaurav S. Amin and Harry M. Kat, "Welcome to the Dark Side," working paper, Dec. 2001 | OK — real, named study, verified via web search; note the source is a patent filing quoting the study, not the original paper directly, so the figure should be treated as a secondary citation |
| "The size of the distortion varies... but the direction is always the same" | Direct synthesis of the three cited studies' actual findings, not an independent claim | OK — accurately reflects that all three found the same directional effect despite very different magnitudes |

## Friction protected

- Kept: the honest range across three real studies (0.1-0.4 points, 9-10 points, ~2% per year) rather than collapsing it into one falsely precise average number — the spread itself is the accurate finding.
- Kept: the Amin & Kat figure is flagged as sourced via a secondary citation (a patent filing quoting the original working paper), not presented as if verified against the original paper directly.
- Removed: an earlier draft line claiming a single specific inflation percentage with no real source — replaced entirely once a real search was run, rather than softened or hedged while keeping the invented number.

VERDICT: PASS
