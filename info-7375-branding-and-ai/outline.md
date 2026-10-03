# Branding and AI — Outline

Status legend: `to write` · `drafting` · `drafted` · `revising` · `done`

Total: 12 chapters across 4 parts. All at intake are `to write`.

Per `book.md` authoring instructions: every chapter pairs with a real-world case (deployment or failure-mode), the archetype thread runs across all four parts, the Madison framework lives in Chapter 2 and threads through Chapters 4–7, and Chapters 8–12 carry a path fork (personal brand / startup brand) with labeled exercise variants.

---

## Part I — Foundation
*Act 1: "You need more than code."*

### Chapter 1. The Creative Engineer
- **Status:** drafted (2026-05-02, voice-unanchored flag, [verify] on salary numbers)
- **Position in arc:** Act 1, Scene 1 — the inciting incident.
- **Argument:** AI tooling has democratized building. What distinguishes practitioners now is positioning, brand, and communication. Graduate programs that teach only technical skills produce graduates who ship invisible work.
- **Scope:** The Creative Engineer / Full Stack Creative concept. Three career-limiting beliefs ("branding is decoration," "AI does the creative work," "my GitHub is my portfolio"). The 80/20 philosophy. Course roadmap (build, brand, launch). Introduction to the 12 archetypes as a brand strategy system; student identifies a personal archetype and prepares to use it as the selection mechanism in Chapter 2.
- **Case pairing:** Brand deployment — a named AI tool or product launch where brand strategy materially affected market reception.
- **Learning outcomes:** LO 1.1 (define Creative Engineer), LO 1.2 (analyze the three misconceptions), LO 1.3 (describe the AI/brand intersection as a discipline).

### Chapter 2. The Madison Framework
- **Status:** drafted (2026-05-02, voice-unanchored flag)
- **Position in arc:** Act 1, Scene 2 — the mentor's gift.
- **Argument:** Before building your own AI tool, you study a reference architecture. Madison is that reference. Studying it is not copying it; it is learning to read system design.
- **Scope:** Agent-based architecture (what agents are, how they coordinate, why this pattern matters). Madison's specific design patterns — agent roles, data flows, decision logic. Reading the framework as a design reference. Selecting a Madison tool that fits the archetype identified in Chapter 1; the archetype is the selection mechanism. Adapting reference patterns to an original tool. The difference between studying an architecture and copying it.
- **Madison home address:** This is the framework's dedicated chapter. Subsequent build chapters reference it but do not re-teach it.
- **Case pairing:** Brand deployment — a named AI system where architecture decisions had downstream brand or UX consequences.
- **Learning outcomes:** LO 2.1 (analyze Madison's architecture, CLO 1), LO 2.2 (evaluate architecture's impact on tool design, CLO 1), LO 2.3 (select a Madison tool aligned with archetype, CLO 1 and CLO 3).

### Chapter 3. Jungian Brand Archetypes as a System
- **Status:** drafted (2026-05-02, voice-unanchored, [verify] on Coca-Cola URL)
- **Position in arc:** Act 1, Scene 3 — the lens is ground.
- **Argument:** Brand archetypes are not a personality quiz. They are a strategic system with assessable outcomes. Selecting an archetype gives every downstream brand decision a coherent anchor.
- **Scope:** The 12 archetypes (Hero, Sage, Explorer, Innocent, Creator, Ruler, Caregiver, Magician, Lover, Jester, Everyman, Rebel). Core motivation, shadow, and communication style for each. Identifying an archetype in an existing brand (analysis). Selecting an archetype for a new brand (strategy). Archetype as identity vs. archetype as costume. Why consistency across touchpoints matters more than cleverness.
- **Archetype thread:** This chapter covers the full system. The archetype goes dormant during the build (Chapters 4–7) and reactivates with depth in Chapter 8.
- **Case pairing:** Brand failure mode — archetype drift across touchpoints. Three or more incidents where a brand selected an archetype but failed to apply it consistently.
- **Learning outcomes:** LO 3.1 (identify the 12 archetypes, CLO 3), LO 3.2 (analyze brands through archetype identification, CLO 3), LO 3.3 (select a primary archetype with rationale, CLO 3).

---

## Part II — Build
*Act 2, Movement 1: "Build it."*

### Chapter 4. Product Requirements and Scope
- **Status:** drafted (2026-05-02)
- **Position in arc:** Act 2, Movement 1, Scene 1 — the quest begins.
- **Argument:** A good AI tool starts with a good PRD, not with code. Scope discipline is a professional skill. Gap analysis is how you find the space your tool should occupy.
- **Scope:** PRD structure and purpose. Gap analysis (what exists, what is missing, where the tool fits). Job market positioning. MVP boundaries. Scope as a creative constraint. Students use their archetype-selected Madison tool from Chapter 2 as a design reference for their own PRD.
- **Madison reference:** Students map their tool's architecture against the reference tool's patterns.
- **Case pairing:** Brand deployment — a named product where PRD discipline (or its absence) determined whether the tool shipped coherently.
- **Learning outcomes:** LO 4.1 (write a PRD, CLO 2), LO 4.2 (conduct gap analysis, CLO 2), LO 4.3 (defend scope decisions, CLO 2).

### Chapter 5. Data Pipelines and Workflow Automation
- **Status:** drafted (2026-05-02)
- **Position in arc:** Act 2, Movement 1, Scene 2 — the first build.
- **Argument:** Data is the fuel. A reproducible pipeline is the engine. n8n gives you the workflow automation layer between raw data and AI intelligence.
- **Scope:** n8n nodes, triggers, connections. Pipeline architecture (collection, transformation, storage). API integration (connecting external data sources). Reproducible workflows (documentation and portability). Demo pipeline vs. production pipeline.
- **Madison reference:** Pipeline patterns modeled on Madison's data flow architecture.
- **Case pairing:** Brand failure mode — pipeline fragility damaging user trust. Three or more incidents where data infrastructure failures damaged brand credibility.
- **Learning outcomes:** LO 5.1 (design and implement an n8n workflow, CLO 2), LO 5.2 (integrate at least one external API, CLO 2), LO 5.3 (document pipeline architecture for reproducibility, CLO 2).

### Chapter 6. AI Intelligence and Multi-Agent Systems
- **Status:** drafted (2026-05-02)
- **Position in arc:** Act 2, Movement 1, Scene 3 — the tool comes alive.
- **Argument:** Adding AI intelligence to a workflow is not the same as letting AI run the workflow. Multi-agent design patterns govern where AI decides and where humans do.
- **Scope:** Adding AI to existing n8n workflows. Multi-agent systems (agent roles, coordination, handoff). AI-generated output vs. creative direction. Scalability and stress testing. Production readiness (error handling, edge cases, graceful failure).
- **Madison reference:** Multi-agent patterns drawn directly from Madison's agent coordination model.
- **Case pairing:** Brand deployment — a named AI tool where multi-agent architecture was visible in the user experience, connecting system design to brand perception.
- **Learning outcomes:** LO 6.1 (add AI intelligence using multi-agent patterns, CLO 1 and CLO 2), LO 6.2 (evaluate production readiness, CLO 2), LO 6.3 (distinguish AI output from creative direction, CLO 2).

### Chapter 7. Interface Design and Deployment
- **Status:** drafted (2026-05-02)
- **Position in arc:** Act 2, Movement 1, Scene 4 — the tool meets the world.
- **Argument:** A tool that is not deployed is a homework assignment. The interface is the first brand touchpoint most users encounter.
- **Scope:** UI design for AI tools (what is different about AI UIs). Streamlit and Gradio implementation. Public deployment (working prototype to URL). Portfolio integration (deployed tool as case study asset). Documentation as professional artifact (README, architecture overview, setup).
- **Case pairing:** Brand failure mode — interface-brand misalignment. Three or more incidents where a technically sound tool failed because the interface contradicted the brand strategy.
- **Midterm gate:** After this chapter, students present their AI tool in a Guy Kawasaki 10/20/30 pitch. The midterm is the Act 2 midpoint.
- **Learning outcomes:** LO 7.1 (build a functional UI in Streamlit/Gradio, CLO 2), LO 7.2 (deploy a working prototype with documentation, CLO 2 and CLO 6), LO 7.3 (evaluate interface decisions against UX principles, CLO 2).

---

## Part III — Brand
*Act 2, Movement 2: "Make it mean something."*

> **Path fork begins here.** Theory sections are unified. Exercises and case pairings are labeled by path: **Personal Brand** or **Startup Brand**.

### Chapter 8. Brand Strategy
- **Status:** drafted (2026-05-02, both path-fork variants — PERSONAL and STARTUP)
- **Position in arc:** Act 2, Movement 2, Scene 1 — the tool gets an identity.
- **Argument:** Brand strategy is not decoration applied after the build. It is a system of decisions (mission, vision, values, UVP, archetype, voice, positioning) that determines how every audience encounter lands.
- **Scope:** Brand foundation elements (mission, vision, values, UVP). Two paths (personal professional brand vs. startup concept). Deep application of the selected archetype to messaging and voice. Archetype-driven positioning and differentiation. Tool naming and validation (naming methodologies, testing, trademark basics). Professional positioning (what makes you hireable / fundable).
- **Path fork:** Theory unified. Exercise sets labeled **Personal Brand** and **Startup Brand**. Reader commits to a lane.
- **Archetype thread:** Reactivates with full strategic depth. Students may revise their Chapter 1 selection based on the completed tool and strategic analysis.
- **Case pairing:** Two brand deployment cases — one personal brand, one startup — where archetype-driven strategy produced measurable differentiation.
- **Learning outcomes:** LO 8.1 (develop complete brand strategy document, CLO 4), LO 8.2 (apply selected archetype consistently, CLO 3 and CLO 4), LO 8.3 (name and validate using methodology, CLO 4), LO 8.4 (defend strategy decisions, CLO 4).

### Chapter 9. Visual Identity Systems
- **Status:** drafted (2026-05-02)
- **Position in arc:** Act 2, Movement 2, Scene 2 — the brand becomes visible.
- **Argument:** Visual identity is not a logo. It is a system (logo, palette, typography, imagery direction) governed by the brand strategy and archetype decisions made in Chapter 8. The creative brief is the strategy-to-design translation layer. The wireframe is the structural plan for the portfolio.
- **Scope:** Creative brief development. Visual identity components (logo, color, typography, imagery). Archetype-aligned visual decisions (palettes by archetype, typography personality, imagery direction). Mood boards as a communication tool. Website wireframing and UX fundamentals. Color accessibility and WCAG compliance.
- **Wireframes as bridge:** Wireframes here are the structural plan for the portfolio in Chapter 11. In the book, storytelling (Chapter 10) sits between to give the reader narrative content for the wireframe. In the course, instructors may swap the order.
- **Case pairing:** Brand failure mode — visual identity without strategy. Three or more incidents where visual investment without strategic foundation produced aesthetic work that failed to communicate positioning.
- **Learning outcomes:** LO 9.1 (design cohesive visual identity system, CLO 5), LO 9.2 (develop creative brief, CLO 5), LO 9.3 (evaluate WCAG compliance, CLO 5), LO 9.4 (create mood board, CLO 5), LO 9.5 (produce website wireframe, CLO 5 and CLO 6).

---

## Part IV — Launch
*Act 3: "Tell the story. Own the room."*

### Chapter 10. Brand Storytelling
- **Status:** drafted (2026-05-02, [verify] on Jaguar 2024 case detail)
- **Position in arc:** Act 3, Scene 1 — the narrative lands.
- **Argument:** A brand without a story is a logo on a business card. Storytelling frameworks (Hero's Journey, The Quest) give the reader a repeatable method for turning brand strategy into narrative content through the archetype lens.
- **Scope:** Narrative frameworks (Hero's Journey, The Quest). Storytelling through the archetype lens (a Hero archetype tells a different story than a Sage archetype). Content strategy and publication (what, where, how often). LinkedIn articles and blog posts as thought leadership. Authentic voice (writing in a voice vs. performing one). Case study writing as storytelling.
- **Role in the launch sequence:** For LinkedIn articles, case studies, and blog posts, storytelling is the foundation. For the portfolio website, storytelling functions as refinement — strengthens about-page copy, sharpens project descriptions, turns feature lists into narratives.
- **Archetype thread:** Governs narrative voice, story structure, content positioning.
- **Case pairing:** Brand failure mode — narrative-archetype mismatch. Three or more incidents where a brand's storytelling contradicted its archetype.
- **Learning outcomes:** LO 10.1 (write brand narrative through archetype lens, CLO 7), LO 10.2 (develop content strategy and publish, CLO 8), LO 10.3 (analyze archetype/framework/voice relationship, CLO 7).

### Chapter 11. Portfolio as Product
- **Status:** drafted (2026-05-02)
- **Position in arc:** Act 3, Scene 2 — assembly.
- **Argument:** A portfolio is not a collection of screenshots. It is a product with an audience, a structure, and a strategic purpose. AI-powered design tools (v0.dev, Framer AI) make it possible to demonstrate technical and creative capability in one artifact.
- **Scope:** AI-powered portfolio development (v0.dev, Framer AI). AI image generation for branding assets. Portfolio structure (case study format, project narratives, visual hierarchy). LinkedIn optimization as a brand touchpoint. The AI tool as a portfolio case study (documentation, demonstration, positioning). Applying narrative frameworks from Chapter 10 to portfolio content. Accessibility (WCAG compliance in portfolio design).
- **Integration point:** Most integrative chapter in the book. Draws on wireframes (Ch. 9), storytelling (Ch. 10), visual identity (Ch. 9), and the deployed tool (Ch. 7).
- **Case pairing:** Brand deployment — a named practitioner or graduate whose portfolio strategy produced a measurable career outcome.
- **Learning outcomes:** LO 11.1 (build portfolio with AI-powered design tools integrating the AI tool as case study, CLO 6), LO 11.2 (generate AI images for branding and evaluate alignment, CLO 6), LO 11.3 (optimize LinkedIn profile, CLO 8), LO 11.4 (apply narrative frameworks to portfolio content, CLO 6 and CLO 7).

### Chapter 12. Professional Presence and Launch
- **Status:** drafted (2026-05-02)
- **Position in arc:** Act 3, Scene 3 — the curtain call.
- **Argument:** The final deliverable is not the portfolio. It is you, presenting a coherent professional identity that integrates everything you have built, branded, and written.
- **Scope:** Resume as brand artifact (ATS-optimized version that gets past the filter, designer version that gets remembered). Social media presence (LinkedIn article publishing, social strategy). Promotion strategy (how to get portfolio and tool seen). Final presentation (Guy Kawasaki 10/20/30 framework). Complete brand portfolio presentation as competency. What happens after the course (continuing to build, iterate, position).
- **Case pairing:** Brand deployment — a named professional presentation or pitch where integration of technical demonstration and brand narrative produced a distinct outcome (hire, funding, partnership).
- **Learning outcomes:** LO 12.1 (build two resume versions for creative tech roles, CLO 9), LO 12.2 (produce and publish social content with brand consistency, CLO 8), LO 12.3 (present complete brand portfolio in 10/20/30 format, CLO 10).

---

## Dependency Map

```
Ch 1 (Creative Engineer) → Ch 2 (Madison) → Ch 3 (Archetypes)
                                  ↓
                                  Ch 4 (PRD/Scope) → Ch 5 (Pipelines) → Ch 6 (AI/Agents) → Ch 7 (UI/Deploy)
                                                                                                        ↓
                                                                                         [MIDTERM PITCH]
                                                                                                        ↓
                                  Ch 3 (Archetypes) → Ch 8 (Brand Strategy) → Ch 9 (Visual Identity)
                                                                                                        ↓
                                                            Ch 10 (Storytelling) → Ch 11 (Portfolio) → Ch 12 (Presence/Launch)
                                                                                                        ↓
                                                                                       [FINAL PRESENTATIONS]
```

Four hard dependencies:

1. **Build before brand.** Chapter 8 cannot begin until Chapters 4–7 are complete. The midterm pitch is the gate.
2. **Archetypes seed the build, then go dormant.** Chapter 1 introduces the system, Chapter 2 uses the archetype to select the Madison reference tool, Chapter 3 covers the full framework. Chapters 4–7 do not foreground the archetype. Chapter 8 reactivates it.
3. **Storytelling before portfolio (in the book).** Chapter 11 references narrative frameworks taught in Chapter 10. Course deployments may swap the order.
4. **Portfolio integrates everything.** Chapter 11 requires the tool (Part II), brand strategy and visual identity (Part III), wireframes (Ch. 9), and storytelling (Ch. 10).

---

## Case Pairing Summary

| Theory Chapter | Case Type | Case Focus |
| --- | --- | --- |
| Ch 1: Creative Engineer | Brand deployment | Brand strategy's material impact on market reception |
| Ch 2: Madison Framework | Brand deployment | Architecture decisions affecting brand/UX |
| Ch 3: Archetypes | Brand failure mode | Archetype drift across touchpoints |
| Ch 4: PRD/Scope | Brand deployment | PRD discipline determining coherent ship |
| Ch 5: Data Pipelines | Brand failure mode | Pipeline fragility damaging user trust |
| Ch 6: AI Intelligence | Brand deployment | Multi-agent architecture visible in UX |
| Ch 7: Interface/Deploy | Brand failure mode | Interface-brand misalignment |
| Ch 8: Brand Strategy | Brand deployment (×2) | Archetype-driven differentiation (one per path) |
| Ch 9: Visual Identity | Brand failure mode | Visual design without strategic foundation |
| Ch 10: Storytelling | Brand failure mode | Narrative-archetype mismatch |
| Ch 11: Portfolio | Brand deployment | Portfolio strategy producing career outcomes |
| Ch 12: Presence/Launch | Brand deployment | Integrated presentation producing distinct outcome |

Cases that pass the editorial gate ship under student bylines.

---

## Course-to-Book Mapping (representative 14-week semester)

This mapping is a reference, not a binding sequence. Per `book.md` authoring instructions, course materials never reference chapter numbers — they reference topics. Instructors build a semester-specific mapping for each deployment.

| Week | Topic | Book Chapter(s) |
| ---: | --- | --- |
| 1 | Introduction, archetypes overview, positioning | Ch 1 + Ch 3 (introduction) |
| 2 | Madison framework, PRD, scope planning | Ch 2 + Ch 4 |
| 3 | n8n, data pipelines, API integration | Ch 5 |
| 4 | AI intelligence, multi-agent systems | Ch 6 |
| 5 | UI design, deployment | Ch 7 |
| 6 | Brand strategy, archetypes deep dive, naming | Ch 3 (deep dive) + Ch 8 |
| 7 | Visual identity, creative brief, wireframes | Ch 9 |
| 8 | Midterm presentations | — |
| — | Break | — |
| 9 | Portfolio build *or* storytelling (instructor choice) | Ch 10 *or* Ch 11 |
| 10 | Storytelling *or* portfolio build (instructor choice) | Ch 11 *or* Ch 10 |
| 11 | Portfolio refinement | Ch 11 (continued) |
| 12 | Resume, social media, launch | Ch 12 |
| 13 | Final presentations (Group 1) | — |
| 14 | Final presentations (Group 2) | — |

---

## Suggested structure

| Part | Focus | Chapters |
| --- | ---: | ---: |
| Part I | Foundation (Setup) | 1–3 |
| Part II | Build (Confrontation, Movement 1) | 4–7 |
| — | Midterm pitch (Act 2 midpoint) | — |
| Part III | Brand (Confrontation, Movement 2) | 8–9 |
| Part IV | Launch (Resolution) | 10–12 |
| — | Final presentations (Act 3 climax) | — |
