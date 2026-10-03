# Madison — bundled framework for *Branding and AI*

This directory is a **self-contained, vendored copy** of the Madison assets the book's
AI+1 exercises run on. *Branding and AI* is a branding textbook; **Madison is the AI tool
it uses**. You do not need to clone anything else — download this repository and the
end-of-chapter exercises are runnable.

Madison is an open-source, agent-based marketing-intelligence framework
([humanitarians.ai/madison](https://www.humanitarians.ai/madison)) organized into five
agent roles plus an orchestration layer. The recipes below are declarative specifications
— each carries phase gates, typed inputs, and human-in-the-loop checkpoints — that you run
to produce a brand artifact. The **AI+1** contract is the point: the agent drafts, **you**
exercise the strategic judgment to accept, reject, or revise. See `prompts/plus-one.md`.

> This is documentation-as-tooling. The companion volume *The Madison CLI Framework*
> explains the architecture in depth; you do not need it to use the recipes here.

## What's here

- `recipes/` — 22 curated brand-relevant recipes (the five roles + orchestrator + brand tasks)
- `templates/wrap-your-tool/` — Next.js scaffold for wrapping a recipe as a deployable tool
- `prompts/plus-one.md` — the AI+1 operator prompt (human-gated agent runs)

## The five roles (+ glue)

| Role | Recipe | Produces |
|---|---|---|
| Intelligence | `recipes/intelligence-agent.md` | reputation/trend/sentiment signal from live sources |
| Content | `recipes/content-agent.md`, `recipes/madison-copy-content-generation.md` | brand-voice copy, channel/A-B variants |
| Research | `recipes/madison-persona-generation.md`, `recipes/survey-analysis.md` | evidence-backed personas, segmentation |
| Experience | `recipes/ai-concierge.md` | AI concierge / customer-journey interactions |
| Performance | `recipes/madison-performance-reporting.md` | measurement, experiments, outcome reporting |
| Orchestration | `recipes/madison-marketing-intelligence-orchestrator.md` | cross-agent coordination + validation |

## Chapter → recipe map (AI+1 exercises)

| Chapter | Branding decision | Madison recipe(s) it runs on |
|---|---|---|
| 1 — The Creative Engineer | establish the four-verb baseline | `intelligence-agent` (audit your own public signal) |
| 2 — The Madison Framework | read architecture as brand surface | `madison-marketing-intelligence-orchestrator`, `intelligence-agent` |
| 3 — Jungian Brand Archetypes | fix archetype, derive audience | `madison-audience-definition`, `madison-persona-generation` |
| 4 — Product Requirements & Scope | scope the brand/tool | `madison-branding-marketing-pipeline`, `madison-martech-product-positioning-signal-agent` |
| 5 — Data Pipelines & Workflow | stand up a signal pipeline | `madison-brand-news-reputation-monitor`, `madison-category-sentiment-dashboard` |
| 6 — AI Intelligence & Multi-Agent | orchestrate the roles | `madison-marketing-intelligence-orchestrator`, `intelligence-agent` |
| 7 — Interface Design & Deployment | ship the tool | `templates/wrap-your-tool`, `ai-concierge` |
| 8a — Personal Brand Path | position a person | `madison-competitive-positioning-agent`, `madison-audience-definition` |
| 8b — Startup Brand Path | position a venture | `madison-competitive-positioning-agent`, `madison-martech-product-positioning-signal-agent` |
| 9 — Visual Identity Systems | enforce coherence | `madison-brand-consistency-contradiction-checker`, `madison-qa-accessibility-audit` |
| 10 — Brand Storytelling | generate on-voice narrative | `madison-copy-content-generation`, `content-agent` |
| 11 — Portfolio as Product | assemble + measure the portfolio | `madison-brand-portfolio-dashboard`, `madison-campaign-construction` |
| 12 — Professional Presence & Launch | rehearse and launch | `madison-pre-launch-simulation`, `madison-launch-handoff`, `madison-performance-reporting` |

**Cross-cutting** (any chapter, ethics/trust/research threads):
`madison-consumer-trust-anxiety-index`, `madison-brand-sentiment-monitor`, `survey-analysis`.

## Provenance

Vendored from the Madison framework (`humanitarians.ai/madison`). Recipes are declarative
specs; running one that makes live network calls, external writes, or model calls with
sensitive data requires the approval gate recorded in the recipe. Treat any agent-generated
persona, claim, or market figure as a draft requiring an evidence check — the human half of
AI+1.
