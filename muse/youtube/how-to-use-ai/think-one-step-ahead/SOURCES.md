# SOURCES.md — "Think one step ahead"

## Refactor source (read-only mirror repo)

`nikbearbrown/humanitarians-youtube-muse` —
`claude/claude-for-education/claude-liam-prompt-tutorial-lesson-06-precognition/`
(beat_sheet.json, README.md, description.txt; mp3/ ignored, never downloaded).
The source's argument, kept: token-by-token generation constrains later
output; a thinking scratchpad before the answer fixes early commitment; use
it when a human expert would reach for scratch paper, skip it on simple
lookups. The source's script, audience (technical/course), and XML-tag
mechanics were rewritten, not reused.

## Verification sources (read 2026-10-03)

1. Anthropic, "Prompt Engineering Interactive Tutorial",
   https://github.com/anthropics/prompt-eng-interactive-tutorial —
   Chapter 6: "Precognition (Thinking Step by Step)". Key line: "Giving
   Claude time to think step-by-step makes it more accurate, especially for
   complex tasks. However, thinking only works when it's 'out loud' in the
   output." Implementation: ask Claude to think through the problem; use
   `<thinking>` / `<brainstorm>` / `<scratchpad>` XML tags for the reasoning.
2. AWS / Anthropic, "Prompt engineering techniques and best practices: Learn
   by doing with Anthropic's Claude 3 on Amazon Bedrock",
   https://aws.amazon.com/blogs/machine-learning/prompt-engineering-techniques-and-best-practices-learn-by-doing-with-anthropics-claude-3-on-amazon-bedrock/ —
   "Give Claude time to think through its response before producing the final
   answer... include the phrase 'Think step by step' in your prompt."
3. Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language
   Models" (2022), https://arxiv.org/abs/2201.11903 — generating intermediate
   reasoning steps significantly improves large language models' complex
   reasoning; reasoning tokens become context for the final-answer tokens.
4. Simon Willison's notes on the tutorial (2024-08-30),
   https://simonwillison.net/2024/Aug/30/anthropic-prompt-engineering-interactive-tutorial/ —
   the `<scratchpad>` / `<answer>` tag pattern for evidence-first answers.

## Deliberate simplifications for the general audience

- "Token" → "word" (defined on screen as "word by word").
- The `<thinking>` XML tag → "a scratchpad: Claude's working notes, written
  before the answer". Viewers on claude.ai get the benefit from the plain
  instruction "think it through first, step by step, then answer".
- "Rationalizes rather than reasons" → "defends its first guess instead of
  checking it".
