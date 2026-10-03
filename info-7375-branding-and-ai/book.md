# Branding and AI: Building the Creative Engineer

## Meta

- **Slug:** `branding-and-ai`
- **Working title:** Branding and AI: Building the Creative Engineer
- **Subtitle alternative (catalog):** Brand Strategy, Visual Identity, and Storytelling for Technical Practitioners
- **Status:** intake — TOC handoff received
- **Intake date:** 2026-05-02
- **Editor:** Nik Bear Brown
- **Creative domain co-author / reviewer:** Nina Harris
- **Publisher:** Bear Brown LLC
- **Primary deployment:** INFO 7375, Northeastern University (14-week graduate course)
- **Total chapters:** 12 across 4 parts (theory spine + case layer)

## Audience

Graduate students in technical programs — computer science, data science, AI/ML, engineering, information systems — who can build but cannot yet position. The student walks in believing their GitHub is their portfolio. They walk out able to:

- Scope, build, and deploy an AI-powered tool from PRD through public URL.
- Develop a complete brand strategy (mission, vision, values, UVP, archetype, voice) for either a personal professional brand or a startup concept.
- Design a cohesive visual identity system (logo, palette, typography, imagery) governed by brand strategy and archetype.
- Write a brand narrative using the Hero's Journey or The Quest framework through their selected archetype.
- Build a portfolio that integrates the AI tool as a case study and demonstrates both technical and creative capability in one artifact.
- Deliver an investor-ready presentation in the Guy Kawasaki 10/20/30 format.

Adjacent texts — *Designing Brand Identity* (Wheeler), *Building a StoryBrand* (Miller), *Hello, My Name Is Awesome* (Watkins), *AI Product Management* (Druce/Kinnear) — each cover a slice. None occupy the gap this book occupies: AI systems design + brand strategy for a technical graduate audience.

## Scope

**In scope:**

- The "Creative Engineer" / Full Stack Creative concept: why technical credentials alone fail to differentiate.
- The Madison framework as a reference architecture for AI-powered products, including its agent-based design patterns.
- The 12 Jungian brand archetypes as a strategic system (not a personality quiz).
- Build sequence for an AI tool: PRD and gap analysis, n8n data pipelines and API integration, multi-agent AI intelligence, Streamlit/Gradio interface, public deployment.
- Brand strategy: mission, vision, values, UVP, archetype application, naming methodology, positioning.
- Visual identity systems: logo, color (with WCAG compliance), typography, imagery direction, mood boards, creative briefs, website wireframes.
- Brand storytelling: Hero's Journey, The Quest, content strategy, LinkedIn articles, blog posts, case study writing.
- Portfolio as product: AI-powered portfolio tools (v0.dev, Framer AI), AI image generation for branding, LinkedIn optimization.
- Professional presence: ATS-optimized and designer resumes, social media strategy, presentation frameworks.

**Out of scope (explicit):**

- Pure marketing-discipline brand theory beyond what an archetype-driven strategy needs.
- Deep dives into specific ML model architectures (referenced as instruments, not taught as subject).
- Trademark, IP, and corporate-formation legal work (named in Chapter 8 naming, deeper coverage belongs in a business-formation text).
- Full-stack web development (the portfolio is built using AI-powered design tools, not hand-coded from scratch).
- Cryptocurrency, NFT, and Web3 brand strategy (out of scope for this edition).

## Prerequisites

- Comfort with at least one programming language and ability to read documentation.
- Working knowledge of git, the command line, and APIs.
- No prior coursework in marketing, branding, or design is assumed. The book teaches these as technical disciplines from first principles.
- Recommended but not required: prior exposure to product management, UX research, or any course where students have shipped a working prototype.

## Voice adjustments

Defer to root `style/` and `plugins/feynman/VOICE.md`. No book-specific overrides at intake; voice samples will accumulate in `books/branding-and-ai/style/` as chapters draft.

Two book-level notes for chapter authors:

1. The reader is technical. They will distrust hand-waving about "branding as art." The Feynman move — strip the jargon, show the machinery, run the calculation on the page — is especially load-bearing here. Brand strategy is taught as a system of decisions with assessable outcomes, not as taste.
2. Archetype work is the highest-risk material in the book for sliding into pop-psychology cadence. Treat archetypes as a *strategic anchor* — a selection mechanism that produces consistency across touchpoints — not as personality types or identity claims. When a chapter cites an archetype, the chapter must show it doing work (a messaging decision, a visual decision, a story-structure decision). Reference-only invocations are not doing the method.

## Authoring instructions for chapter writers

These are book-wide instructions to apply when drafting any chapter:

### Two-layer architecture: theory spine + case layer

Every chapter is paired with a real-world case. Cases alternate by chapter:

- **Brand deployment cases** (positive examples) pair with chapters where the foundation needs a working illustration: 1, 2, 4, 6, 8 (one per path), 11, 12.
- **Brand failure mode cases** pair with chapters where the lesson lands hardest through a worked failure: 3, 5, 7, 9, 10.

Each case carries a citable primary source (filing, paper, model card, blog post, interview, public statement). Cases that pass the editorial gate ship under student bylines. The case-pairing summary is in `outline.md`.

### Path fork at Chapter 8

Chapters 1–7 are unified. Chapter 8 introduces a structural fork: students choose **personal professional brand** or **startup brand concept**. The underlying theory is identical for both paths. Exercises, examples, and case pairings diverge. The fork is marked explicitly in Chapters 8–12 with labeled exercise variants. Chapter authors for these chapters write *one* theory section and *two* exercise sets.

### The archetype thread

The archetype is the connective thread across all four parts. Authors must respect the load curve:

- **Chapter 1** introduces archetypes as a system, students identify their personal archetype.
- **Chapter 2** uses the archetype as the *selection mechanism* for which Madison tool the student studies as their build reference.
- **Chapter 3** covers all 12 archetypes as a system.
- **Chapters 4–7 (Build):** archetypes go dormant. Building the tool consumes all bandwidth. The archetype quietly shaped the build — it chose the reference architecture — but the chapter prose does not foreground it.
- **Chapter 8** archetypes re-activate with full strategic depth as the governing lens for brand strategy.
- **Chapters 9–12** carry the archetype through visual identity, storytelling, portfolio voice, and professional presence.

A chapter that invokes the archetype out of phase (e.g., a Build chapter that pauses to discuss archetype theory) is not doing the method.

### Madison framework treatment

Chapter 2 is the framework's home. Chapters 4–7 reference it as a running worked example — students return to it but are not re-taught it. Authors of Chapters 4–7 must not re-explain the framework's architecture; they reference patterns by name and assume the reader has Chapter 2 in working memory.

### Show the build

Build chapters (4–7) follow the workshop's "show the work" rule with no exceptions. Code on the page. Pipeline diagrams on the page. API call structure on the page. A build chapter that says "you connect the API" without showing the connection is not doing the method.

### Book vs. course sequencing

The book and the course do not run in the same order. Chapters 10 (Storytelling) and 11 (Portfolio) can be taught in either course order; the book teaches storytelling first because the portfolio chapter references narrative frameworks that are taught there. **Slides and course materials never reference chapter numbers.** They reference topics. Chapter numbers are book artifacts; topics are stable across semesters and across the book/course divide.

### Pantry — legacy course as reference, not source of truth

`books/branding-and-ai/pantry/` holds two unzipped Canvas Common Cartridge exports of the legacy INFO 7375 course (Spring 2026 and Summer 2026 sections). Chapter authors mine the pantry during the research protocol — after gathering primary sources from the open literature, before drafting — to see how a topic was previously taught, what assignments were given, what examples the prior instructor used, and what changed between iterations.

Three rules govern pantry use:

1. **Pantry is reference, not citation.** Chapter claims cite primary sources (papers, model cards, blog posts, filings). A pantry page is not a citable source for the textbook. It is a framing aid and a continuity check for students who took the prior version.
2. **Pantry surfaces examples; chapters re-verify them.** If the pantry uses a particular tool, brand, or case study to illustrate a concept, the chapter author may use the same one if it still serves — but must re-fetch the primary source and confirm the example still holds. Stale benchmarks, deprecated tools, and rebranded companies are pantry hazards.
3. **Pantry shape ≠ book shape.** The legacy course has 4 modules; the new book has 12 chapters. Pantry content does not map cleanly to chapters. Authors search by concept (`grep -rli '<concept>' pantry/`) and pull what serves, not by looking up "the chapter 6 module."

Pantry navigation starts at `pantry/INDEX.md`, which lists modules, wiki pages, assignments, and binary assets with file paths.

**One pantry entry has elevated status: `pantry/madison/`.** This is the full Madison framework source repo. It is the reference architecture Chapter 2 *teaches* and Chapters 4–7 *build against*. Authors of those chapters read code, agent definitions, and n8n workflows here when explaining how a Madison tool is structured. Unlike Canvas pantry content, Madison source is citable — chapters can reference Madison's README, agent definitions, and workflow JSON as primary material because Madison is itself the subject of those chapters.

The Madison/Canvas distinction in one sentence: **Canvas pantry shows how the topic was previously taught; Madison pantry is the topic.**

## Resolved intake decisions

Five open questions from the TOC handoff have been resolved:

1. **Working title.** Retained: *Branding and AI: Building the Creative Engineer*. Library-discoverable primary term plus thesis-statement subtitle. Subtitle alternative reserved for publisher proposal stress-test.
2. **Theory spine chapter count.** 12 chapters confirmed. Maps to a 14-week syllabus with two assessment weeks (midterm presentations, final presentations) functioning as gates, not content chapters.
3. **Madison framework depth.** Hybrid: Chapter 2 is the dedicated architecture chapter; Chapters 4–7 thread Madison as the running worked example. Framework has a home address without being isolated from the build sequence.
4. **Comparable texts.** No direct competitor identified. Adjacent texts named in this `book.md` for publisher proposal differentiation. Differentiation statement: no current textbook combines AI systems design with brand strategy for a technical graduate audience.
5. **Personal vs. startup brand.** Unified theory spine with path-specific exercises. Structural fork at Chapter 8.

## Open questions (still unresolved)

1. **Madison framework public availability.** The book treats Madison as the reference architecture. If Madison is not publicly available at publication, Chapter 2 needs an "armchair version" — a synthesized reference architecture that captures the agent-based pattern without depending on a specific tool. Author to decide before drafting Chapter 2.
2. **Case pool for student bylines.** The case-layer model assumes a cohort produces all 12 case pairings per semester. Decide editorial gate before first deployment: who reviews student case drafts, what threshold passes, how attribution is handled when a case is jointly authored.
3. **AI tool currency.** v0.dev, Framer AI, n8n, Streamlit, Gradio — the tooling layer in Chapters 5, 7, and 11 is the chapter content most likely to date. Decide whether tool-specific instructions live in the chapter prose or in a refreshable companion (online supplement, GitHub repo). Default is companion; authors flag at draft time if a chapter cannot be written without committing to a specific tool.
4. **Archetype sourcing.** Pearson and Mark's *The Hero and the Outlaw* is the closest scholarly reference for the 12-archetype system. Decide whether the book cites it as canonical, treats it as one of several formulations, or reframes the archetypes from primary sources (Jung, Campbell). Recommended: cite Pearson/Mark as the working reference and name the simplification at the chapter level.

## Connections

- Pairs naturally with INFO 7375 (Northeastern) and any graduate AI/CS program that wants to add a positioning or capstone-presentation component.
- Could feed forward into a more specialized text on AI product management or design systems for AI products.
- Backstops: a marketing-discipline brand text (*Designing Brand Identity*, Wheeler) for readers who want deeper marketing context, and an AI engineering text for readers who want deeper systems context.

## Tags

`branding` `AI` `creative-engineer` `archetypes` `madison-framework` `portfolio` `brand-strategy` `visual-identity` `storytelling` `INFO-7375` `northeastern` `graduate` `textbook`
