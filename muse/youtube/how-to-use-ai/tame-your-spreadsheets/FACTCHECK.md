# FACTCHECK.md — Tame Your Spreadsheets

Real fact-check. No invented statistics, studies, or quotations. All example
data is fictional (Lena's Bake Shop) and labeled illustrative. Verdicts: PASS,
CORRECTED, EXEMPT.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02, B06 | `=SUM(B2:B31)` adds up the values in cells B2 through B31; B2:B31 is a cell reference (a range address) | PASS | Standard Excel / Google Sheets syntax (illustrative example, not a study). The narration reads the formula left to right exactly as the functions are documented. | none |
| 2 | B03 | The AI can be confidently wrong about cell references (e.g. pointing at a price column instead of a quantity column) | EXEMPT | Illustrative caution, not a measured error rate. Framed in the film as the film's own standing warning ("can be"), not as research. The film prescribes the check (hand-add five rows), not the statistic. | none — kept as cautionary judgment, no rate claimed |
| 3 | B03 | Adding up five rows by hand and comparing is a sufficient sanity check before trusting a column total | CORRECTED | Judgment call, not a proof: five matching rows do not guarantee the rest. Film wording adjusted to "If those five match, you can trust the other twenty-six" — flagged here as pragmatic advice, not a guarantee. | none — labeled as the film's practical rule, stated plainly |
| 4 | B04 | Pasting messy data and asking the AI to "clean this up and make everything consistent" standardizes dates/spellings while leaving numbers untouched | EXEMPT | Capability/how-to claim in line with the source film's argument (AI does the spreadsheet mechanics). Presented as a workflow to try, with the viewer's own data. Numbers-untouched is a promptable constraint, not a guaranteed behavior — the film does not promise it. | none |
| 5 | B05 | "Saturday sales are nearly double your weekday average" | EXEMPT | Fictional illustrative data (Lena's Bake Shop). The film's point is the *move* (ask "what's interesting in this data?"), not the numbers. | none — data is fictional by design |
| 6 | B05 | You do not need to know what a pivot table is to get simple analysis from the AI | PASS | Logical: the film's demonstrated move is a plain-English question, not a feature tutorial. | none |
| 7 | B01 | You can describe a wanted formula in plain English and the AI writes it and explains each part | EXEMPT | The core how-to of the film; matches the source film's premise (AI writes real formulas). Viewer-verifiable on their own sheet. | none |

Unresolved: none. No [VERIFY] items — the film makes no empirical claims
beyond standard formula syntax and illustrative fiction.
