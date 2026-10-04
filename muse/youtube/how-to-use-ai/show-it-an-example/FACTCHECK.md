# FACTCHECK.md — "Show It an Example"

Every claim in the narration, checked against the source. No invented
statistics; nothing in this film is a number that needs attributing.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | BDEFS | "few-shot" = teaching the AI by showing it a few examples instead of writing instructions | PASS | Anthropic Prompt Engineering Interactive Tutorial, Lesson 07 (via mirror repo source folder) — few-shot prompting defined as adding completed examples before the target input | — |
| 2 | B00–B02 | Examples can replace written instructions as the way to specify what you want | PASS | Source L07: "Examples do more work per token than any instruction"; "The pattern is the prompt" | — |
| 3 | B02 | Three examples (rule of thumb: three to five is usually enough) | PASS | Source L07 B01: "Three to five examples is usually sufficient" | kept "three" as the film's concrete demo count, inside the source's 3–5 band |
| 4 | B03 | Each example carries length, tone/vocabulary, structure, domain conventions, and edge-case handling simultaneously | PASS | Source L07: examples "communicate format, tone, length, vocabulary, and domain conventions simultaneously"; B02: "encodes length, vocabulary register, structural template, domain jargon, and edge-case handling" | reworded to plain language (length · tone · shape · words · tricky bits) |
| 5 | B04 | One bad example contaminates the pattern; example quality matters more than count | PASS | Source L07 B03: "One bad example contaminates the pattern"; "Example quality matters more than example count" | — |
| 6 | B05 | Good examples are representative (not edge cases), internally consistent, and matched to the real target | PASS | Source L07 B03: "representative… internally consistent… matched to the real target distribution" | reworded to plain language; "distribution" → "the thing you're about to ask for" |
| 7 | B06 | Three examples are almost always shorter than the paragraphs they'd replace | EXEMPT | Plain-language simplification, no numeric claim made; follows from claims 2–4 (compression). Stated qualitatively ("almost always", "fewer words") — a judgment, not a statistic | — |
| 8 | BHTF | Running examples-vs-description yourself will show the example version matching your style more closely | EXEMPT | Pedagogical exercise, framed as "compare" / "check", not a guaranteed outcome | worded as a test the viewer runs, with two checks, not a promise |

Deliberately NOT claimed: any percentage improvement, token counts, cost
figures, or "studies show" language. The source lesson contains none, and the
film invents none.
