# AI+1 Running-Project Spec — *Branding and AI*

The spec the per-chapter exercise generator follows. Mirrors the AI+1 five-part block
standard used in the pharma books, adapted to branding and to **Madison as the bundled tool**.

## The running project: **Your Brand, End to End**

The reader builds **one brand** across the whole book — their own — and every chapter advances
the *same* brand by running the mapped Madison recipe (`madison/recipes/*`). The project forks
at Chapter 8 into two parallel strands the reader picks between (or runs both):

- **Path A — Personal brand** (Ch 8a): position a person (the Creative Engineer themselves).
- **Path B — Startup brand** (Ch 8b): position a venture.

By Ch 12 the reader has, for their chosen path, an archetype-anchored, evidence-checked brand
package — audience, positioning, signal pipeline, visual system, story, portfolio, and launch —
each artifact produced by running Madison with their own judgment as the accept/reject gate.

The deliverable lives in a working folder the reader creates, e.g. `your-brand/`, with one
artifact added per chapter.

## The AI+1 contract (the "+1" is the human)

Madison drafts; **the reader decides.** Every block names what AI is *for* here and where the
reader's judgment is non-delegable. In branding the non-delegable calls are: choosing the final
archetype, approving brand voice, signing off positioning, accepting a persona as real, and
clearing any market claim. Agent-generated personas, claims, and figures are drafts requiring an
evidence check.

## Per-chapter block template (five parts)

Append to each chapter, after the figures, as `## Chapter N Exercises: <title>`:

```
## Chapter N Exercises: <chapter theme>
**Project:** Your Brand, End to End
**This chapter adds:** <the one brand artifact this chapter contributes to the running project>

### Exercise 1 — When to Use AI
Three chapter tasks where Madison assistance is appropriate (reformatting / drafting /
pattern-spotting), each with "Why AI works here." Tell: you can independently evaluate the output.

### Exercise 2 — When NOT to Use AI
Three tasks here that require human judgment, each with "Why AI fails here" (calibration gap,
taste/authenticity, claim verification, archetype commitment). Tell + Series connection (T-judgment).

### Exercise 3 — LLM / Recipe Exercise
What you're building this chapter + which Madison recipe it runs (`madison/recipes/<file>.md`) +
Tool (Claude / Claude Project) + a ready-to-paste prompt block that invokes the recipe on the
reader's brand. Adapt-this-prompt + connection to prior chapter + preview of next.

### Exercise 4 — CLI Exercise
Run the recipe through the bundled tooling (`madison/templates/wrap-your-tool` or Claude Code),
producing a reproducible artifact file in your-brand/. Setup, task block, expected output,
what-to-inspect, failure mode + recovery, CLAUDE.md/AGENTS.md note.

### Exercise 5 — AI Validation Exercise
A validation checklist for the chapter's artifact — correctness, completeness, scope, two
chapter-specific checks, and a failure-mode check (fluent-but-wrong + any fabricated persona/claim).
```

## Chapter → recipe → "this chapter adds"

| Ch | Madison recipe(s) | This chapter adds to *Your Brand* |
|---|---|---|
| 1 — Creative Engineer | `intelligence-agent` | Four-verb self-audit + public-signal baseline |
| 2 — Madison Framework | `madison-marketing-intelligence-orchestrator`, `intelligence-agent` | The role map for your brand's pipeline |
| 3 — Jungian Archetypes | `madison-audience-definition`, `madison-persona-generation` | Committed archetype + audience definition |
| 4 — Requirements & Scope | `madison-branding-marketing-pipeline`, `madison-martech-product-positioning-signal-agent` | Brand/tool scope + the "$100,000 no" list |
| 5 — Data Pipelines | `madison-brand-news-reputation-monitor`, `madison-category-sentiment-dashboard` | A live signal pipeline for your brand/category |
| 6 — AI Intelligence & Multi-Agent | `madison-marketing-intelligence-orchestrator`, `intelligence-agent` | Orchestrated multi-agent intelligence run |
| 7 — Interface & Deployment | `templates/wrap-your-tool`, `ai-concierge` | Your brand tool, deployed |
| 8a — Personal Brand | `madison-competitive-positioning-agent`, `madison-audience-definition` | Personal positioning statement |
| 8b — Startup Brand | `madison-competitive-positioning-agent`, `madison-martech-product-positioning-signal-agent` | Venture positioning statement |
| 9 — Visual Identity | `madison-brand-consistency-contradiction-checker`, `madison-qa-accessibility-audit` | Visual system + coherence/accessibility QA |
| 10 — Storytelling | `madison-copy-content-generation`, `content-agent` | On-voice brand narrative + copy set |
| 11 — Portfolio as Product | `madison-brand-portfolio-dashboard`, `madison-campaign-construction` | Portfolio assembled + measured |
| 12 — Presence & Launch | `madison-pre-launch-simulation`, `madison-launch-handoff`, `madison-performance-reporting` | Launch rehearsal, handoff, and report |

**Cross-cutting threads** (cite where the chapter's ethics/trust/research beat calls for it):
`madison-consumer-trust-anxiety-index`, `madison-brand-sentiment-monitor`, `survey-analysis`.

## Rules

- Every Exercise 3/4 must point at a recipe that **exists in `madison/recipes/`** (or the
  `wrap-your-tool` template). No invented recipe names.
- The branding decision leads; Madison executes. Never open a block with the tool.
- Keep the boundary: *apply* Madison, do not re-teach the framework (that's Ch 2's one dose).
- No fabricated personas, claims, citations, or metrics — label anything unverified for the
  reader to check.
