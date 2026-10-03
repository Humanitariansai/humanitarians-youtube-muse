# Research Map — *Branding and AI* (re-architected 19 + S4 blueprint)

How the existing manuscript feeds the new blueprint, and where new research is needed. Pairs with
`TIKTOC.md` (the blueprint) and `madison/README.md` (chapter → recipe map).

## Existing chapters → new slots (the research base)

The 14 existing chapters are **research sources**, not final chapters. Each maps to a new slot;
some need reframing before they become the new chapter.

| New slot | Existing chapter = research base | Reframe needed |
|---|---|---|
| Ch 1 — The Creative Engineer | old Ch 1 (as-is) | none — already on-thesis |
| Ch 3 — AI Toolchain: Cowork, Codex & Madison | old Ch 2 (The Madison Framework) | **EXPAND**: teach the CLI agents (Cowork/Codex/Claude Code), not just read Madison |
| Ch 5 — Brand Archetypes as a System | old Ch 3 | none |
| Ch 6 — Brand Strategy & Positioning | old Ch 8a + 8b (merge) | **MERGE** personal + startup into one chapter; the two paths become the running-project fork, not two chapters |
| Ch 9 — Visual Identity Systems | old Ch 9 | none |
| Ch 10 — Brand Voice & Storytelling | old Ch 10 | add explicit **voice** section (currently storytelling-only) |
| Ch 18 — Portfolio as Product | old Ch 11 | none |
| Ch 19 — Professional Presence & Launch | old Ch 12 | none |
| **S1** — Product Requirements & Scope | old Ch 4 | move to end-of-book Ship It appendix |
| **S2** — Pipelines & Workflow (on Madison) | old Ch 5 | **reframe**: operate Madison, drop hand-built n8n |
| **S3** — AI Intelligence & Multi-Agent | old Ch 6 | move to appendix |
| **S4** — Interface & Deployment | old Ch 7 | move to appendix |
| (Ch 8 — Naming, Trademark & Protection) | naming sub-section inside old Ch 8a/8b | extract naming material as seed; expand with trademark/IP |

**Source text in pantry:** `132516973-The-Fundamentals-of-Branding.txt` (Davis, AVA 2009) — a
canon checklist, dated (pre-AI, Twitter-era). Use for canon coverage, not current facts.

## New chapters needing a research pass (11)

All have a per-chapter research note in this directory. Canon is stable (foundational sources
named); time-sensitive facts are flagged `[verify]` for the Phase-4 fact-check.

| New chapter | Research note | Primary canon sources | Madison hands-on |
|---|---|---|---|
| 2 — What a Brand Is: Equity & Assets | `new-ch02-brand-equity.md` | Keller (CBBE), Aaker (brand equity), Interbrand/Brand Finance/Kantar valuation | `intelligence-agent`, `madison-brand-sentiment-monitor` |
| 4 — The Brand Audience | `new-ch04-audience.md` | Kotler STP, Christensen JTBD, Holt cultural branding, VALS | `madison-audience-definition`, `madison-persona-generation`, `survey-analysis` |
| 7 — Brand Architecture & Portfolio | `new-ch07-architecture-portfolio.md` | Aaker & Joachimsthaler (Brand Relationship Spectrum), Kapferer | `madison-brand-portfolio-dashboard` |
| 8 — Naming, Trademark & Brand Protection | `new-ch08-naming-trademark.md` | Lanham Act / trademark-strength spectrum, USPTO/TESS, INTA | AI name-gen + clearance (ad-hoc; gap recipe) |
| 11 — Brand Experience & Touchpoints | `new-ch11-experience-touchpoints.md` | Pine & Gilmore (Experience Economy), journey mapping, ZMOT/moments of truth | `ai-concierge` |
| 12 — Content, Media & Campaigns | `new-ch12-content-media-campaigns.md` | IMC (Schultz), PESO model (Dietrich) | `madison-campaign-construction`, `…copy-content-generation`, `content-agent` |
| 13 — Measuring Brand Equity & Impact | `new-ch13-measurement.md` | Reichheld (NPS), Keller measurement, Farris (Marketing Metrics) | `madison-performance-reporting`, `…category-sentiment-dashboard` |
| 14 — Brand Management, Governance & Rebranding | `new-ch14-management-rebranding.md` | Wheeler (Designing Brand Identity), rebrand case studies | `madison-brand-consistency-contradiction-checker` |
| 15 — Brand Ethics, Purpose & Sustainability | `new-ch15-ethics-sustainability.md` | Holt (brand activism), Edelman Trust Barometer; **regulation: EU ECGT, FTC Green Guides** | claims/proof + `madison-consumer-trust-anxiety-index` |
| 16 — Crisis & Reputation Management | `new-ch16-crisis-reputation.md` | Coombs (SCCT), Tylenol case | `madison-brand-news-reputation-monitor` |
| 17 — Global & Cross-Cultural Branding | `new-ch17-global-cross-cultural.md` | Hofstede, De Mooij, standardization vs adaptation | localization + `content-agent` |

## Method

1. Existing chapters: lift the durable content into the new slot; apply the reframe; re-run the
   AI+1 generator in FRAMEWORK MODE so exercises operate Madison recipes.
2. New chapters: draft from the research note's canon + sources, ground every claim, run the
   `[verify]` items through the fact-check pass before publishing.
3. Running project (personal / company[real|fictional|startup]) threads every chapter; Madison
   recipe per chapter per `madison/README.md`.
