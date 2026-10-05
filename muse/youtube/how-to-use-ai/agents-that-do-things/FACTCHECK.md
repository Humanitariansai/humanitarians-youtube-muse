# FACTCHECK.md — Agents: AI that does things.

Every claim in the script was checked before writing. The film names NO
products, quotes NO prices, and asserts NO version-specific features — a
deliberate design decision so the film cannot go stale. Unverifiable claims
were cut; hedges are kept where the source is a pattern rather than a
universal fact.

## Verified (record)

1. An AI agent / agentic AI is a program that can pursue goals, use software
   or other tools, and take actions with some level of autonomy — contrasting
   with chatbots that answer questions. → [record] (Wikipedia, "Agentic AI":
   "an artificial intelligence program that can pursue goals, use software or
   other tools, and take actions with some level of autonomy";
   https://en.wikipedia.org/wiki/Agentic_AI, crawled 2026-10-04)
2. Agent anatomy: an LLM reasoning engine paired with tools, APIs and memory
   that allow it to act in the world rather than just describe it; the core
   loop is perceive, reason, act, observe, repeat. → [record]
   (loanpro.io glossary: "The core loop: perceive, reason, act, observe,
   repeat"; "Generative AI creates content, agentic AI creates outcomes";
   https://loanpro.io/glossary/agentic-ai, crawled 2026-10-04)
3. Anthropic's "Building effective agents" (Dec 2024) distinguishes agents —
   systems where LLMs dynamically direct their own processes and tool usage —
   from workflows with predefined code paths; recommends finding the simplest
   solution possible and only increasing complexity when needed, because
   agentic systems trade latency and cost for better task performance. →
   [record] (anthropic.com/engineering/building-effective-agents, via mirrors
   crawled 2026-10-04)
4. The same guide's risk list: errors compound over many steps; higher cost
   and latency; unpredictable behavior. Mitigations: sandboxed environments,
   human oversight checkpoints, guardrails; limiting scope, read-only access,
   or human-in-the-loop where errors are high-stakes and hard to discover. →
   [record] (same source)
5. LLMs cannot reliably distinguish instructions from data — both arrive as
   natural-language text — which is the structural basis of prompt injection.
   → [record] (topgallant-partners.com, "Prompt Injection: The Security Flaw
   Living Inside Every AI Agent", crawled 2026-10-04)
6. Indirect prompt injection: malicious instructions hidden in emails,
   webpages or files are read by the AI and interpreted as directives — e.g.
   an email containing a hidden instruction the agent follows, or a fake
   system warning in a dataset tricking the model into deleting reports.
   OpenAI published research on self-replicating prompt injection in
   September 2026. → [record] (theregister.com, 2026-09-29,
   https://www.theregister.com/security/2026/09/29/; economy.ac summary of the
   OpenAI research, crawled 2026-10-04)

## Corrected / hedged (judgment)

7. B06 says the agent "might just do it" — deliberately hedged. Models are
   increasingly trained to resist injection, and behavior varies; the film
   presents it as a failure mode to supervise, not a certainty. [judgment]
8. B08's "retry a dead end forty times" is an illustrative round number,
   phrased as a possibility ("will retry"), not a measured finding. [judgment]
9. B05's Saturday-evening example is a worked illustration of the supervision
   pattern, not a claim about any real product's behavior. [judgment]

## Exempt (no external claim)

- The three-rule supervision framework (delegate only what you can check;
  approve the irreversible; start on low stakes) and the 10-minute budget are
  the film's own teaching devices, derived from the verified risk list —
  not factual claims. [record]
- "A chatbot with hands", "librarian versus assistant", "new hire after
  probation" are metaphors, labeled as such in narration. [record]
