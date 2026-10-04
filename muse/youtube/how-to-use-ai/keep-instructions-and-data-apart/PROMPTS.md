# PROMPTS.md — Keep instructions and data apart

Prompts used in this build (recorded so the work is reproducible and the
AI's contributions are inspectable).

## Research / fact-check (browser_search, 2026-10-03)
1. "Anthropic prompt engineering XML tags separate instructions from data"
   → confirmed the tutorial's Chapter 4 guidance (XML tags recommended;
   Claude trained to recognize them; no magic tag names; consistency).
2. "OWASP top 10 LLM prompt injection number one risk"
   → confirmed prompt injection holds LLM01 in the 2025 edition and the
   August 2026 refresh.

## Handoff prompt (B09 — for the viewer, typed into Claude)
> Rewrite this prompt with XML tags — put my instruction in <instructions>
> and this pasted text in <document> — then show me where an injection
> could have hidden before.

## Build-time prompts
- None sent to any external model for scriptwriting. Narration was authored
  directly from the refactor source and the verified claims above.
