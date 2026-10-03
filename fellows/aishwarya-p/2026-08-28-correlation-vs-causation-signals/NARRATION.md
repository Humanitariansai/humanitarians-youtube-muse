# Correlation vs. Causation in Signal-Finding — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video walks through why a real statistical correlation in market data doesn't mean you've found a tradeable signal.

## B00 — Cold open
Two variables moved together for eight straight years, with a correlation of 0.91. A model flagged it as a signal. Nobody asked why.

## B01 — Problem
Method: correlation measures whether two variables move together. It says nothing about whether one causes the other, or whether both are being driven by something else entirely. Where it fails: with enough variables and enough time, you will always find some pair that correlates strongly by pure chance — this is a known, measurable effect called spurious correlation, and it gets worse the more variables you test.

## B02 — Concept: what causation actually requires
The fix: causation requires a real mechanism — a reason A would actually move B — plus a way to rule out a shared underlying driver. Correlation alone can never supply either of those; it can only tell you two things happened to move together in the data you have.

## B03 — Concept: the real stakes
How much does this actually matter? Tyler Vigen's widely covered Spurious Correlations project compiled a decade of real data — roughly 1999 to 2009 — and found a strong, statistically significant correlation between the number of people who drowned in swimming pools each year and the number of films Nicolas Cage appeared in that year. The correlation itself is real. The causal story is absurd. Financial signal-finding faces the same risk at scale: testing many variable pairs against historical price data will surface some strong-looking correlations by chance alone, indistinguishable on the numbers from a real signal.

## B04 — Handoff
Your turn. Take a correlation you've found or been shown, and ask Claude: is there a plausible causal mechanism connecting these two variables, or could a shared third factor explain both? List what evidence would actually distinguish a real signal from a coincidental one.

## B05 — Outro
Correlation vs. Causation in Signal-Finding. Built with Claude, for Humanitarians AI.
