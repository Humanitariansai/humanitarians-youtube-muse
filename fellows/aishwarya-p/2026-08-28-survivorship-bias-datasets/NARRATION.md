# Survivorship Bias in Financial Datasets — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya from the Mycroft team. This video walks through survivorship bias: how a dataset can quietly drop the companies that failed, and make a strategy's past performance look better than it ever actually was.

## B00 — Cold open
"This strategy returned 12% annually over 20 years." That number is true — for the companies still around to measure it against.

## B01 — Problem
Method: a historical dataset built from today's list of companies only ever includes the ones that survived to be on that list. Where it fails: if a company went bankrupt, got delisted, or was acquired out of distress along the way, it's often silently missing — not flagged as absent, just never there. A backtest run against that dataset isn't measuring "how this strategy would have performed." It's measuring "how this strategy performed, among companies that happened to survive" — a very different, much rosier question.

## B02 — Concept: what a bias-free dataset requires
The fix: a survivorship-bias-free dataset includes delisted and bankrupt companies at the point in time they were still active — not erased from history because they later failed. This means the dataset has to be built forward from a real point-in-time company list, not backward from today's survivors.

## B03 — Concept: the real stakes
How much does this actually matter? The honest answer: it depends heavily on the dataset. Grinblatt and Titman found the effect as small as a few tenths of a percentage point per year in one mutual fund study. Kothari, Shanken, and Sloan found excluded firms' returns differed by nine to ten percentage points in equity data. Hedge fund researchers have estimated an average closer to two percent per year across peer indices. The size of the distortion varies by asset class and time period — but the direction is always the same: leaving out the failures makes the past look safer and more profitable than it actually was.

## B04 — Handoff
Your turn. Take a historical dataset you're using or considering, and ask Claude: does this dataset include delisted, bankrupt, or acquired companies at the point in time they were active, or does it only reflect companies that exist today? If you can't answer that confidently, treat any backtest on it as optimistic until proven otherwise.

## B05 — Outro
Survivorship Bias in Financial Datasets. Built with Claude, for Humanitarians AI.
