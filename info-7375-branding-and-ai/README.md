# Branding and AI

## NEU INFO 7375 — Fall 2026 course

**Predict → Build It → Use It → Ship It → Verify**

Start with the [fifteen-lesson course](COURSE.md), [syllabus](SYLLABUS.md), and [ten-day Assignments](assignments/fall-2026/README.md). Required course work uses Claude Code and Python, with one running brand project. [NEU prerequisites](prerequisites/README.md) explain access, policy, and 60/10/10/20 grading. Lesson Assessments are ungraded; video, public launch, and paid production are optional. The original book and its broader toolchain are preserved below.

AI+1, Hands on. Domain specific. No generic prompts.

**Author:** Nik Bear Brown & Nina Harris
**Publisher:** Humanitarians AI Incorporated
**Copyright:** Copyright © 2026 Nik Bear Brown & Nina Harris. All rights reserved.
**Edition:** 2026

## Summary

*Branding and AI* is a graduate-level, hands-on branding course for technical practitioners
whose credentials no longer separate them. When AI collapses the cost of *building*, the
scarce skill becomes knowing **what** to build and making it **legible** to the audience it
is for. The book reads that shift through Spence's signaling mechanism, names the four verbs
that now carry career value — **Ideate, Build, Brand, Ship** — and walks the disciplines that
make a *Creative Engineer* recognizable: the Madison reference architecture, the twelve
Jungian brand archetypes as a system, product scope, data pipelines, interface and
deployment, brand strategy on two paths (personal and startup), visual identity, storytelling,
portfolio-as-product, and launch.

Every chapter opens on a brand decision and uses AI to execute it. The book ships the AI it
teaches: `madison/` is a self-contained copy of the **Madison** framework, so a download is
runnable. Each chapter closes with a five-part **AI+1** block — *When to Use AI / When NOT /
Recipe / CLI / Validation* — that advances one running brand (the **Self-as-Project** thread)
by running the mapped Madison recipe. The agent drafts; you own the decision.

## Table of Contents

**The running project** (personal brand, or a company brand — real, fictional, or your startup) threads every chapter; each closes with a framework-mode AI+1 block that advances it by running a Madison recipe.

- **Chapter 1 — The Creative Engineer.** *When the cost of building collapses, the value of knowing what to build rises.*
- **Chapter 2 — What a Brand Is: Equity & Assets.** *A logo is the cheapest part of a brand.*
- **Chapter 3 — The AI Toolchain: Cowork, Codex & Madison.** *Architecture is a brand decision — learn the tools that build it.*
- **Chapter 4 — The Brand Audience.** *"Everyone" is not an audience.*
- **Chapter 5 — Brand Archetypes as a System.** *The constraint that makes every downstream decision decidable.*
- **Chapter 6 — Brand Strategy & Positioning.** *What you decline to build defines the brand — personal and startup paths.*
- **Chapter 7 — Brand Architecture & Portfolio.** *Every brand is a system of brands.*
- **Chapter 8 — Naming, Trademark & Brand Protection.** *A great name you cannot own is a liability.*
- **Chapter 9 — Visual Identity Systems.** *Strategy and design together — the system, not the Pepsi document.*
- **Chapter 10 — Brand Voice & Storytelling.** *A brand telling the wrong story burns faster than none.*
- **Chapter 11 — Brand Experience & Touchpoints.** *For most customers, the experience is the brand.*
- **Chapter 12 — Content, Media & Campaigns.** *AI made content free; that is why most of it is worthless.*
- **Chapter 13 — Measuring Brand Equity & Impact.** *A number that moved is a question, not a verdict.*
- **Chapter 14 — Brand Management, Governance & Rebranding.** *Keeping a brand coherent, and knowing when to change it.*
- **Chapter 15 — Brand Ethics, Purpose & Sustainability.** *A green claim you cannot prove is now a fine.*
- **Chapter 16 — Crisis & Reputation Management.** *Reputation is built in years and lost in hours.*
- **Chapter 17 — Global & Cross-Cultural Branding.** *Localization is re-creation, not translation.*
- **Chapter 18 — Portfolio as Product.** *The artifact you build once whose returns compound.*
- **Chapter 19 — Professional Presence and Launch.** *The final deliverable is you.*

**Appendix — Ship It track** (optional, for a company/startup brand with a product or tool):
- **S1 — Product Requirements & Scope** · **S2 — Pipelines & Workflow (on Madison)** · **S3 — AI Intelligence & Multi-Agent Systems** · **S4 — Interface & Deployment**

## The bundled Madison framework

`madison/` is a vendored, self-contained copy of the AI tool the exercises run on:

- `madison/recipes/` — 22 curated brand-relevant recipes (the five agent roles + orchestration + brand tasks)
- `madison/wrap-your-tool/` — a Next.js scaffold for shipping a recipe as a deployable tool
- `madison/prompts/plus-one.md` — the AI+1 operator prompt (human-gated agent runs)
- `madison/README.md` — the five roles and the chapter → recipe map

You do not need the companion volume *The Madison CLI Framework* to use these; it documents
the architecture, this book applies it.

## Files

- `chapters/` — the manuscript: front matter, introduction, Chapters 1–19, Appendix S1–S4 (Ship It), fundamental themes, back matter
- `madison/` — the bundled Madison framework (recipes, template, prompt)
- `exercises/branding-ai1-running-project-spec.md` — the AI+1 running-project + recipe-map spec
- `TIKTOC.md` — the book's compact architecture (spine, chapter map, Madison boundary)
- `images/` — figures (SVG + PNG)
- `metadata.yaml`, `build.sh`, `styles/` — build inputs (pandoc → EPUB/HTML)
- `LICENSE.md` — rights and reuse terms

## Medhavy

This book is prepared for Kindle, online publication, and integration with Medhavy: https://www.medhavy.com/
