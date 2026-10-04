# FACTCHECK.md — "Think one step ahead"

Audited 2026-10-03 against the primary sources in SOURCES.md. Verdicts:
PASS (supported), CORRECTED (fixed in the sheet), EXEMPT (house definition /
illustrative advice, not a factual claim). No statistics are invented; every
number the film avoids, it avoids on purpose.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Claude produces an answer one word at a time, left to right. | PASS | Standard autoregressive generation: each new token is conditioned on the tokens before it. Anthropic's Ch. 6 tutorial is built on this mechanism. | "Word" is the plain-language rendering of "token"; the simplification is deliberate for a general audience (defined in BDEFS as "word by word"). |
| 2 | B00 | Once a word is written, it is written — no going back to change it. | PASS | Within a single response, generation is left-to-right; earlier tokens become fixed context for later ones. | None. |
| 3 | B01 | The first line of a demanded answer is a guess, and every word after it has to follow that line. | PASS | Plain-language rendering of the source lesson: "once the first answer token is written it constrains everything after." | None. |
| 4 | B01 | Claude "does not check its first guess — it defends it." | PASS | Plain-language rendering of the source lesson's "commit too early and the model rationalizes rather than reasons." | Framed as narration, not as a quoted finding. |
| 5 | B02 | Asking Claude to "think it through first, step by step, then answer" — a scratchpad before the answer — improves answers on hard tasks. | PASS | Anthropic Prompt Engineering Interactive Tutorial, Ch. 6 "Precognition (Thinking Step by Step)": "Giving Claude time to think step-by-step makes it more accurate, especially for complex tasks... thinking only works when it's 'out loud' in the output." (github.com/anthropics/prompt-eng-interactive-tutorial) | The film teaches the plain-language form ("think it through first"); the tutorial's `<thinking>` XML tags are the developer-facing form, noted in SOURCES.md, not taught on screen. |
| 6 | B02 | On the scratchpad Claude can try an idea, cross it out, and catch a mistake before the answer exists. | PASS | The source lesson's scratchpad is for "intermediate steps and corrections" (source description.txt); the tutorial's exercises have Claude argue both sides before answering. | The crossed-out line is an illustrative visual of "corrections", labeled as such in SHOTLIST.md. |
| 7 | B03 | "Same question. Same Claude. Better answer." — reasoning first improves the answer. | PASS | Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (2022), arxiv.org/abs/2201.11903: generating intermediate reasoning steps significantly improves large models' complex-reasoning performance. | The film states the practical upshot without the paper's numbers; no benchmark figures are quoted. |
| 8 | B04 | The scratch-paper rule: use think-first for choices, math, tricky decisions; skip it for simple lookups ("extra words for nothing"). | PASS | The source lesson's rule: "if a human expert would reach for scratch paper, add the thinking tag. Otherwise skip it and save the tokens." | "What is the capital of Peru" is an illustrative example of a simple lookup. |
| 9 | B05 | "Ask for what you'll need next" — have the thinking look ahead so the answer includes follow-ups. | EXEMPT | Prompting advice (anticipatory prompting), not a factual claim. The trip-packing example is illustrative. | None. |
| 10 | BDEFS | Definitions of "prompt", "scratchpad", "word by word". | EXEMPT | House definitions written for this film; consistent with standard usage. | None. |
| 11 | BHTF | The viewer's prompt and the two self-checks. | EXEMPT | Advice to the viewer, not a factual claim. The with/without comparison is a fair self-test, not a cited experiment. | None. |

## Notes

- No model version numbers, no benchmark figures, and no Anthropic-internal
  claims appear in the narration — nothing that can date or needs attribution
  aloud (show-tell law 8).
- The film never teaches XML tags; BDEFS defines "scratchpad" as "Claude's
  working notes", which is what a general-audience viewer needs.
