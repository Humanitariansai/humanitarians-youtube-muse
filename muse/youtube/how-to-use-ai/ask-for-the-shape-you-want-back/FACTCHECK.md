# FACTCHECK.md — "Ask for the Shape You Want Back"

Real claims only; no invented statistics. Verdicts: PASS / CORRECTED / EXEMPT
(EXEMPT = how-to instruction or general pedagogical framing, not a factual claim).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B06 | Prefilling exists: you can put the start of the assistant's reply in the API call and Claude continues from there. | PASS | Anthropic docs, "Prefill Claude's response" (docs.anthropic.com / platform.claude.com build-with-claude/prompt-engineering/prefill-claudes-response) | — |
| 2 | B06 | Prefill is an API/developer technique; narration presents it as "for developers" calling Claude "through its API". | PASS | Same docs: the technique is documented for the Messages API (assistant message in `messages[]`). | — |
| 3 | B06 | "Anthropic, who build Claude, document this trick as prefilling." | PASS | Same docs page title: "Prefill Claude's response for greater output control". | — |
| 4 | B06 | Prefilling a `{` steers Claude toward JSON output. | PASS | Docs list "enforce specific formats like JSON or XML" as a purpose; worked examples prefill `"{"` for raw JSON. | — |
| 5 | B06 | A prefilled answer "cannot dodge the format" — Claude cannot add a preamble before the prefill. | CORRECTED | Docs: "Claude continues from exactly where you left off — it cannot backtrack or add a preamble." Narration says "cannot dodge the format", which is the plain-language version of the documented claim. | Wording kept as-is; it restates the documented guarantee, not a stronger one. |
| 6 | B05 | JSON is "a strict format machines read, written in curly braces". | EXEMPT | General, stable definition (JavaScript Object Notation). | — |
| 7 | B05 | "If a program will use the answer, ask for JSON." | EXEMPT | How-to instruction, not a factual claim. | — |
| 8 | B02/B03/B04 | Asking Claude for a table / a word limit / a tone produces that shape. | EXEMPT | Practical prompting instructions; verifiable by the viewer in one try (and BHTF makes them verify). | — |
| 9 | B07 | "The format never makes the facts true" — a tidy table can be wrong. | EXEMPT | General reasoning guidance, not a factual claim. | — |
| 10 | B01 | Without format instructions Claude "answers in prose". | EXEMPT | Describes typical default behaviour as the film's setup; the voice frames it as "here is what happens", illustrative. | — |

No numerical, historical, legal, medical, or version claims in the film. No claims
marked `[VERIFY]` remain open. Note: prefill is documented as unavailable with
extended thinking; the film does not claim otherwise and keeps the topic at the
concept level for a general audience.
