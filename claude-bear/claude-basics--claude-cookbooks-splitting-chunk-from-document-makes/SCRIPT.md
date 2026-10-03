# SCRIPT — Why splitting a chunk from its document makes it retrieve for the wrong question

Register: Plain. Voice: Liam (Kokoro am_onyx). Mode: redo of
`anthropics/youtube/claude-basics/claude-cookbooks-splitting-chunk-from-document-makes`
(source register: Teardown → re-registered here as Plain: same facts, no verdict).

## B00 — Hesitant writer (the question, typed and corrected)

On screen (typed, then corrected): "Why does shrinking a chunk\nmake it retrieve for the wrong question?" — "shrinking" is typed, reconsidered, and replaced with "splitting."

Narration (Liam):
> You might think a chunk retrieves badly because it got shrunk too small. It isn't size — it's this: why does splitting a chunk from its document make it retrieve for the wrong question?

## S01 — Stakes (the anchor, planted)

> A medical paper is split into twenty chunks for search. Chunk seven reads: "This treatment reduced mortality by twelve percent" — with no disease named anywhere in it.

## S02 — The wrong guess

> The natural assumption is that search matches on words, so a chunk about "mortality" should surface for any mortality question, right disease or not.

## S03 — Breaking it

> A word-matching search hands that chunk to a "diabetes mortality" query on the word match alone — it has nothing to do with diabetes, but nothing in the chunk says so.

## S04 — The mechanism

> The fix: generate a short summary of the whole document, and prepend it to the chunk before embedding. The vector then carries the chunk's own words plus its place in the document, so an ambiguous phrase resolves against real context.

## S05 — Anchor payoff

> Prepend "Context: hypertension study in elderly patients" to chunk seven, and it stops matching diabetes queries. Across ten test queries, precision on that chunk moved from thirty-three percent to ninety.

## S06 — Both directions (A)

> That gain only shows up if the chunk was ambiguous to begin with — a chunk that already names its subject gets nothing from the extra context.

## S07 — Both directions (B)

> And it doesn't fix a document summarized badly, or a search built on a broken chunking strategy in the first place — this repairs one specific failure, not retrieval in general.

## BCRY — Carry-out

> A chunk answers the question inside it. Prepending its document's context is what lets it also answer the right question.

## BHTF — Your turn (Claude prompt, read aloud)

> Your turn. Here's the prompt — read it with me. I have a research paper being split into chunks for RAG. A chunk says "This treatment reduced mortality by twelve percent" with no disease name in context. Show me how to prepend a context header to each chunk before embedding, what fields belong in that header, and how I'd verify the fix is actually preventing false matches on unrelated queries.

## BOUT — Outro (Humanitarians AI skin)

OutroSeries:
> Why splitting a chunk from its document makes it retrieve for the wrong question. This is Claude Basics, from Humanitarians AI.

OutroCTA:
> Find more at humanitarians.ai. …Liam, in for Bear.
