# Point-in-Time vs. Restated Data — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video walks through why training on today's version of historical financial data can quietly teach a model information it wouldn't have actually had at the time.

## B00 — Cold open
A company's Q1 earnings, as reported today: $340 million. As reported at the time: $310 million. The model was trained on the first number.

## B01 — Problem
Method: financial data gets revised after the fact — restated earnings, corrected filings, updated economic indicators. The version you pull today often isn't the version that existed on the date it claims to describe. Where it fails: a model trained or backtested on today's restated numbers is quietly given information from the future relative to the date it's supposedly predicting. This isn't a hypothetical edge case — restatements are a routine, ongoing part of financial reporting.

## B02 — Concept: what point-in-time data actually preserves
The fix: point-in-time data stores the value as it was known on that date, alongside any later revisions as separate, dated entries — never overwriting history with the corrected number. A model trained on this can only ever see what someone actually could have seen at the time.

## B03 — Concept: the real stakes
How much does this actually matter? This isn't a hypothetical concern — commercial databases exist specifically to solve it. The Compustat Point-In-Time database tracks both a company's originally reported numbers and every later restatement as separate, dated records, letting researchers reconstruct exactly what was known at any past month-end rather than what's known now. Its stated purpose is helping researchers avoid survivorship and look-ahead bias. A dedicated product built around this one problem is a strong sign of how routinely restatements actually distort naive backtests.

## B04 — Handoff
Your turn. Take a financial dataset you're using, and ask Claude: does this reflect the value as it was reported on the date in question, or has it been silently updated with later corrections? If you can't tell, treat any backtest built on it as potentially using information from the future.

## B05 — Outro
Point-in-Time vs. Restated Data. Built with Claude, for Humanitarians AI.
