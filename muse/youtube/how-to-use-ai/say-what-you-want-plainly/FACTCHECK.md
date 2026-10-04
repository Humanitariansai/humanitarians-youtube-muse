# FACTCHECK.md — Say what you want, plainly

Every claim in the narration, checked. Verdicts: PASS (supported),
CORRECTED (fixed in the script), EXEMPT (teaching claim / plain-language
restatement — no external fact asserted). No statistics are used anywhere
in this film, so there is nothing numerical to verify.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00 | "A prompt is the single biggest thing deciding what comes back." | EXEMPT | Teaching claim: restates the source lesson's premise that specificity is the highest-leverage prompting variable. No comparative study cited; framed as the film's thesis, not a measured fact. | None — kept as thesis language ("the single biggest thing"), not a statistic. |
| 2 | B01 | A vague prompt like "write a summary" leaves unspecified dimensions that the AI fills with guesses. | PASS | Anthropic Prompt Engineering Interactive Tutorial, Lesson 02 (mirror-repo source beat B02): "Each unspecified dimension is a degree of freedom Claude fills with a default." | "Degree of freedom" restated as "a guess it has to make" for the general audience; meaning preserved. |
| 3 | B01/B02 | Guesses come from "the default": the most common answer, not necessarily the one you needed. | PASS | Source lesson: unspecified dimensions are filled with "a default that may not be what you needed." | "Most common answer" is the film's plain-language gloss of the lesson's "default"; BDEFS defines the term in the same breath. |
| 4 | B04 | Specificity has four dimensions: length, format, audience, required components. | PASS | Source lesson B02 names exactly these four: "length, format, audience, and required components." | "Required components" rendered as "must-haves" / "what must be in it" on screen; narration keeps the plain words, B04 names all four. |
| 5 | B05 | The golden rule: treat the AI like a capable new employee with no context; tell it your style, audience, edge cases explicitly. | PASS | Source lesson B03: "treat Claude like a capable new employee who has no context… Tell them explicitly." | "House style, audience assumptions, edge-case preferences" (source) → "your style, your reader, the edge cases" (film). Meaning preserved. |
| 6 | B06 | The rewrite example: "write a summary of this document" → three sentences, plain words, for a teammate; include the finding, the method, the limit. | PASS | Source lesson B01's own example: "Write a 3-sentence summary of the following document in plain language suitable for a non-expert reader. Include the main finding, the method, and the limitation." | Audience "non-expert reader" → "a teammate"; "limitation" → "the limit". The example's structure (length/register/audience/components) is unchanged. |
| 7 | BHTF | Auditing a prompt against the four dimensions and re-running both versions shows the difference. | EXEMPT | Practical exercise, not a factual claim. The source lesson's own "Your turn" beat does the same audit. | None. |
| 8 | BIDEA | "Hallo" as the greeting. | EXEMPT | Show-tell law 6: world-language greeting; "Hallo" is on the skill's whisper-checked-clean list. | None. |

**Deliberately not claimed:** the film never says vague prompts *always*
fail, never cites a study, and never quantifies improvement ("10x
better prompts" etc.). The "new employee" is framed as a mental model
("think of the AI as…"), not a factual description of how models work.
