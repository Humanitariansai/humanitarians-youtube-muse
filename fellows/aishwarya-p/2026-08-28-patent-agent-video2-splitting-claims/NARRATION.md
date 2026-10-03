# Video 2: Splitting the Claims — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video walks through building the real claim-splitting logic for the patent Claims Agent, and testing it against real BigQuery data.

## B00 — Cold open
Twenty claims, one real patent, one regex. The question wasn't whether it would run — it was whether it would get every single one right.

## B01 — The build
Method: real claims text is numbered sequentially — "1. A semiconductor system..." followed eventually by "2. The semiconductor system of claim 1..." — and a dependent claim almost always names the claim it depends on directly in its own text. A regex can split on the numbering and check each claim's text for a "claim N" reference to classify it as independent or dependent.

## B02 — The first real test
Running it against US-11791319-B2 — a real semiconductor patent, twenty claims, three independent, seventeen dependent, including chained dependencies three levels deep. Every single one came back correctly classified, verified by hand against the raw text.

## B03 — Stress-testing against more patents
One clean result on one patent proves the code runs — it doesn't prove the logic holds. Three more real patents, forty-four more claims. The parser held up: every independent claim identified correctly, every dependency chain traced correctly, even through claims depending on other dependent claims.

## B04 — The honest catch
The stress test flagged two claims as possible multi-dependencies — patents can legally have a claim depend on "claim 1 or 2" at once, and the parser only ever captures the first number it sees. Checking the actual raw text by hand: it was a false alarm. The claim said "claim 3," plainly — the flag had triggered on an unrelated "or" later in the same sentence, about bumps or projections, nothing to do with the dependency at all. The dependency parsing was right. The false-positive detector was too eager.

## B05 — Handoff
Your turn. Take any patent's claims text, run it through the same split-and-classify logic, and check the flagged claims by hand before trusting any of it — a parser that runs without crashing is not the same as a parser that's correct.

## B06 — Outro
Splitting the Claims. Built with Claude, for Humanitarians AI.
