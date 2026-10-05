# SOURCES.md — Agents: AI that does things.

Fact → source table. Accessed 2026-10-04. All sources are encyclopedic,
vendor-engineering, or trade-press; the film makes no vendor-specific
product claims, so this is sufficient. If a future cut names a product or
quotes a price, re-check against the vendor's own pricing page.

| # | Fact used in the film | Source |
|---|----------------------|--------|
| 1 | Agent / agentic AI definition: pursues goals, uses software/tools, acts with some autonomy; contrasts with chatbots answering questions | Wikipedia, "Agentic AI" (https://en.wikipedia.org/wiki/Agentic_AI) |
| 2 | Agent anatomy: LLM reasoning engine + tools/APIs/memory; "Generative AI creates content, agentic AI creates outcomes" | loanpro.io glossary, "What is Agentic AI?" (https://loanpro.io/glossary/agentic-ai) |
| 3 | Perceive → reason → act → observe → repeat: the core agent loop | loanpro.io glossary (same page) |
| 4 | Anthropic's "Building effective agents": agents vs workflows (LLMs dynamically directing their own processes and tool usage); find the simplest solution first; agentic systems trade latency and cost for better task performance | Anthropic Engineering, "Building effective agents" (Dec 2024; https://www.anthropic.com/engineering/building-effective-agents) — verified via mirrors crawled 2026-10-04 |
| 5 | Agent risks: error compounding over many steps, higher cost/latency, unpredictable behavior; mitigations: sandboxes, human oversight checkpoints, guardrails, limited scope, human-in-the-loop | same Anthropic source |
| 6 | LLMs cannot reliably distinguish instructions from data (both arrive as plain text) — the structural basis of prompt injection | topgallant-partners.com, "Prompt Injection: The Security Flaw Living Inside Every AI Agent" (crawled 2026-10-04) |
| 7 | Indirect prompt injection: hidden instructions in emails/webpages/files read as directives; OpenAI's September 2026 research on self-replicating prompt injection | theregister.com, 2026-09-29 (https://www.theregister.com/security/2026/09/29/); economy.ac research summary (crawled 2026-10-04) |

No statistics are asserted in the film. The Gartner-style forecasts and
adoption figures found during research were deliberately left out — they
churn fast and the film doesn't need them.
