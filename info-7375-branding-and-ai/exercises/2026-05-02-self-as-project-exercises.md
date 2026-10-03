# Self-as-Project — End-of-Chapter LLM Exercises

**Project:** Self-as-Project — *the learner is the running project*
**Audience:** graduate students of INFO 7375 currently looking for jobs
**Premise:** getting a job is self-branding executed under deadline. Every chapter produces a personal-brand artifact you'll actually use this year.

---

## Setup — Before Chapter 1

Before the first exercise, do this once. **It's the single most important setup decision in the semester.**

1. Go to `claude.ai`.
2. Click **Projects** in the left sidebar. Click **New Project**.
3. Name it: **My Personal Brand — [Your Name]**.
4. In the project's **Custom Instructions** field, paste this:

```
You are helping me build my personal brand as a graduating Creative Engineer looking for jobs in AI / technical product / brand-AI roles. Across the semester I will return to you with a chapter-by-chapter exercise from my INFO 7375 textbook. Each exercise builds on the previous one. Treat my prior outputs as canonical and reference them by filename when I add new ones.

When I write or revise something, push back on vague language ("innovative," "passionate," "skilled in") and force specificity. Quote the actual evidence I should be using. If I say something I cannot defend with a primary source or a real artifact I produced, flag it.

Do not be sycophantic. If a sentence is weak, say so. If my archetype claim does not match my actual work, say so. I am being graded by recruiters and hiring managers, not by my self-image.
```

5. Save. Return to this Project for every exercise below.

For exercises that produce files (resumes, wireframes, portfolio code), drop them into the Project's file space using the paperclip icon. Future prompts will reference them.

If you don't use Claude Projects, every exercise still works in plain Claude chat — you'll just paste your previous outputs into the message context manually each time. This is more friction. The Project is worth setting up.

---

### LLM Exercise — Chapter 1: The Creative Engineer

**Project:** Self-as-Project
**What you're building this chapter:** A baseline snapshot of your current professional state — what a recruiter sees today, what you'd want them to see, and a provisional archetype hypothesis.
**Tool:** Claude Project (the one you just set up).

---

**The Prompt:**

```
This is the first exercise in my personal-brand build. I want a baseline snapshot — what a recruiter currently sees when they search for me, and where the gaps are.

Step 1 — Audit my current public footprint. I'll paste below my:
- LinkedIn URL (or the contents of my LinkedIn About + Headline + most recent role description)
- GitHub username (or my pinned repos and profile bio)
- Personal website URL if I have one (or "none yet")
- Any other public profile that comes up when someone googles my name

Read all of it. Then write me a one-paragraph "what a recruiter sees" summary, in plain language, as if you were a hiring manager scanning me for 90 seconds.

Step 2 — Apply the four-verb framework from Chapter 1: Ideate, Build, Brand, Ship. Score me 1-5 on each verb based on the evidence visible in my public artifacts. Justify each score with the specific evidence (or absence of evidence) you found. Be honest. A score of 5 on Build with no shipped product visible is a lie.

Step 3 — Propose a provisional Jungian archetype for me from the 12 (Hero, Sage, Explorer, Innocent, Creator, Ruler, Caregiver, Magician, Lover, Jester, Everyman, Rebel). Base it on:
- The kind of work I describe wanting in my public bio
- The voice I use in my own writing
- The negative space — what I do NOT describe or showcase

Justify the archetype pick with three specific pieces of evidence. Then name the SHADOW of that archetype — the failure mode I'm most likely to produce — and what early warning signs would tell me I'm slipping into it.

Output a single Markdown document called "Personal Brand Baseline — [my name] — [today's date]" with three sections: Recruiter Snapshot, Four-Verb Scorecard, Provisional Archetype + Shadow.

Here is what's currently public about me:
[PASTE LINKEDIN, GITHUB, ANY OTHER PROFILES]
```

---

**What this produces:** A baseline document you'll return to every chapter. The starting line. By Chapter 12 you'll re-run a version of this prompt and the difference will be the artifact of your work.

**How to adapt this prompt:**
- *For your own context:* If your "public footprint" is sparse, paste a summary of your resume instead. The exercise still works — the four-verb scorecard and archetype hypothesis are the load-bearing parts.
- *For ChatGPT / Gemini:* Works as-is. Drop the "Project" reference; paste your public material directly.
- *For Claude Code:* Not the right tool here — this is a reflection-first exercise, not a code task.

**Connection to previous chapters:** None — this is the first.

**Preview of next chapter:** Chapter 2 takes your archetype and uses it to choose which Madison agent layer (Intelligence, Content, Research, Experience, Performance) maps to your career strategy.

---

### LLM Exercise — Chapter 2: The Madison Framework

**Project:** Self-as-Project
**What you're building this chapter:** A "Personal Career Architecture" doc that treats your job search as a multi-agent system you orchestrate.
**Tool:** Claude Project.

---

**The Prompt:**

```
Use my Personal Brand Baseline (already in this project's files / context) as the starting point.

Chapter 2 teaches the Madison framework: a five-layer agent architecture (Intelligence, Content, Research, Experience, Performance) plus an orchestration layer. Each layer is a specialized role.

I want to apply that pattern to my own job search. Treat me as the orchestration layer. Treat the work my career requires as a set of specialized roles I either staff with my own time or delegate to AI tools.

For each of the five Madison layers, write:

1. Intelligence — what I need to know about the AI / tech / brand-AI job market. What signals matter (job posting trends, companies hiring, recent funding, recent layoffs, technology shifts). What sources feed this. How often I should refresh.

2. Content — what I need to publish to be visible. What kinds of artifacts (blog posts, GitHub commits, LinkedIn updates, portfolio pieces, comments on others' work). What cadence is sustainable for me.

3. Research — what I need to learn about specific employers I'm targeting. How I research a company before applying or before an interview. What I should know that most candidates won't bother to find.

4. Experience — what the people-facing work looks like. Networking conversations, informational interviews, follow-ups, recruiter relationships. Who I should talk to. How often.

5. Performance — what I measure. Application count is wrong; outcomes per application is closer. Networking conversations per week. Response rate on outreach. What metrics actually predict offers.

For each layer, give me:
- One concrete weekly action I commit to
- One AI tool that could augment that layer (Claude, Cursor, an n8n workflow, a custom GPT, etc.) — name it specifically
- One failure mode I should watch for in that layer

Then — based on my archetype from Chapter 1 — tell me which layer is most load-bearing for my brand. A Sage gets traction through Intelligence + Content. A Hero through Performance + Experience. A Magician through Content + Experience. A Caregiver through Experience + Research. Pick mine and justify.

Output a Markdown document called "Personal Career Architecture — [my name]" with the five layer plans + the load-bearing-layer call.
```

---

**What this produces:** A career-systems document. Five named layers, weekly commitments, tool suggestions, failure-mode watch list, and a clear answer to "where should I put the most energy."

**How to adapt this prompt:**
- *For your own project:* If you're not job-searching at all (e.g., you're applying to PhD programs or starting a company), reframe the layers — Intelligence becomes program/market research; Performance becomes publication count or revenue.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not yet — Chapter 5 turns one of these layers into actual automation.

**Connection to previous chapters:** Builds directly on the archetype from Chapter 1 — the load-bearing-layer call depends on knowing your archetype.

**Preview of next chapter:** Chapter 3 stress-tests your provisional archetype against richer evidence and forces you to commit (or revise).

---

### LLM Exercise — Chapter 3: Jungian Brand Archetypes as a System

**Project:** Self-as-Project
**What you're building this chapter:** An "Archetype Commitment" — your final archetype call after stress-testing against your actual work, plus a documented shadow watchlist.
**Tool:** Claude Project.

---

**The Prompt:**

```
In Chapter 1 I committed provisionally to an archetype based on my public footprint. Now I want to stress-test that pick.

Step 1 — I'll paste 3–5 samples of my actual writing below. Could be email drafts, code comments, project READMEs, social media posts, anything I wrote without trying to perform an archetype. Read them. Tell me what archetype the writing actually expresses, and how confident you are.

Step 2 — Compare your reading of my actual writing to the provisional archetype I committed to in Chapter 1. If they match, tell me. If they don't, tell me which one wins and why. ("Wins" means: which archetype is more honest? Which one can I sustain over years?)

Step 3 — For my final archetype pick (whether it's the same as Chapter 1 or revised), write me a Shadow Watchlist. Include:
- The shadow's name (e.g., the Sage's shadow is dogmatism; the Hero's is bullying; the Caregiver's is martyrdom)
- Three specific behaviors that would be early warning signs I'm slipping into the shadow
- One ritual or habit I can install to catch the shadow before it lands

Step 4 — Write a one-paragraph "Archetype Manifesto" — first person, my voice, naming my archetype and what it means I commit to. Should be specific enough that someone reading it could predict three things I would say no to. No "passionate" or "innovative." No marketing-speak.

Output a Markdown document called "Archetype Commitment — [my name]" with:
- The committed archetype + confidence level + reasoning
- The Shadow Watchlist
- The Archetype Manifesto

Here are my writing samples:
[PASTE 3–5 SAMPLES]
```

---

**What this produces:** A locked archetype with a falsifiable test (the manifesto's "predict three nos" check) plus a shadow watchlist you'll reference all year.

**How to adapt this prompt:**
- *For your own project:* If you don't have writing samples, paste the longest piece of professional communication you've sent in the last month — even an email to a professor.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not the right tool.

**Connection to previous chapters:** Validates or revises the Chapter 1 provisional archetype. The Career Architecture from Chapter 2 may need a re-pass if your archetype shifted.

**Preview of next chapter:** Chapter 4 turns your job search into a one-page PRD with a "$100,000 no" clause.

---

### LLM Exercise — Chapter 4: Product Requirements and Scope

**Project:** Self-as-Project
**What you're building this chapter:** A one-page **Career PRD** treating your job search as a product launch.
**Tool:** Claude Project.

---

**The Prompt:**

```
Apply Chapter 4's PRD framework to my job search. Treat ME as the product, the job market as the launch target, and the next 6 months as the MVP window.

A PRD has four sections:
1. Problem
2. Gap analysis
3. Tool (the product)
4. MVP boundary (in-scope vs. explicitly out-of-scope)

Write my Career PRD with these constraints:

PROBLEM. The user is a hiring manager, not me. What problem do they have that hiring me would solve? Be specific. "Companies need AI engineers" is not a PRD; it's a wish. Frame the problem at the level of "Series-B fintech startups need engineers who can ship a multi-agent pipeline in 90 days and also explain to a non-technical CEO why the architecture choices matter." If I don't know enough to specify this, list the three things I need to research before I can.

GAP ANALYSIS. Who else fits this problem? Name 3–5 candidate-archetypes I'm competing against (e.g., the senior engineer with five years in multi-agent systems but no design sense; the design-school graduate with brand instincts but no shipped code). Where do they fall short of what hiring managers want? Where do I exceed them? Where do I fall short of them?

TOOL. One sentence describing what I, the product, deliver. NOT a list of skills. A specific value claim. *"A creative engineer who ships multi-agent AI pipelines and writes the brand strategy that makes them sellable."* — that level of specificity. Not "AI engineer with strong communication skills."

MVP BOUNDARY. Two columns.
- IN SCOPE for the next 6 months: roles I will pursue, salary floor I will accept, locations I will consider, technologies I will deepen.
- OUT OF SCOPE: roles I will decline even if offered, comp I won't accept, locations I won't move to, technologies I won't pretend to be expert in.

The OUT column should have at least 5 items. The exercise from Chapter 4 is the "$100,000 no" — what's the role I would decline at $X compensation because it would damage my brand? Name it specifically.

Output a Markdown document called "Career PRD — [my name] — [date]". Single page. No marketing language. If a sentence could appear in a corporate LinkedIn post, rewrite it.
```

---

**What this produces:** A one-page Career PRD that doubles as your decision filter for the next six months. Every job posting can be checked against it.

**How to adapt this prompt:**
- *For your own project:* The MVP window can shorten (3 months for an aggressive search) or lengthen (12 months for a more strategic move).
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not yet — Chapter 5 turns your search into a tracked workflow.

**Connection to previous chapters:** Uses the archetype from Chapter 3 to filter the IN/OUT columns. A Sage's "out" list looks different from a Hero's.

**Preview of next chapter:** Chapter 5 turns your application and networking activity into a documented workflow with explicit contracts.

---

### LLM Exercise — Chapter 5: Data Pipelines and Workflow Automation

**Project:** Self-as-Project
**What you're building this chapter:** A **Career Pipeline** spec — the workflow that takes you from "discovers an opportunity" to "signs an offer," with documented contracts and degraded modes.
**Tool:** Claude Project for the design pass; Cowork for actually setting up the tracking spreadsheet/database.

---

**The Prompt:**

```
Design my job-search pipeline using the Chapter 5 framework: every external dependency is a contract; every contract can break; every break has a degraded mode.

The pipeline has stages. For each stage, document: what enters, what exits, what external contract it depends on, what failure mode would break it, and what my degraded mode is.

Stages to map:

1. DISCOVERY. How job opportunities reach me. Sources: job boards, LinkedIn alerts, referrals, recruiter cold-outreach, my own published work.
2. QUALIFICATION. The PRD-filter pass. Does this role fit my Career PRD's IN list? Yes/no decision.
3. APPLICATION. The actual application work — resume tailoring, cover note, portfolio link, network warm-up.
4. NETWORK ACTIVATION. Reaching out to anyone I know at the company before or during the application.
5. INTERVIEW PREPARATION. Research, talking points, technical practice.
6. INTERVIEW EXECUTION. The conversation itself, follow-up notes.
7. NEGOTIATION. Offer, counter, accept/decline.
8. ONBOARDING / TRANSITION. The first 30 days at the new role, or the post-decline cleanup.

For each stage:
- What's the input?
- What's the output?
- What external contract does it depend on? (E.g., "LinkedIn's recruiter messaging works"; "the company's ATS parses my PDF correctly"; "my reference at Company X is reachable.")
- What's the most likely failure mode? (E.g., "LinkedIn's algorithm deprioritizes my posts"; "the recruiter goes cold for two weeks"; "the take-home assignment requires a tech stack I haven't touched in a year.")
- What's my degraded mode? (E.g., "If LinkedIn dies, I shift to direct email outreach"; "If a recruiter goes cold for two weeks, I one-time follow up and then move on without grudge"; "If the take-home is in unfamiliar tech, I cite my closest analogous work transparently and learn the gaps in 48 hours.")

Then — recommend 3 tools or systems that would automate or augment this pipeline. Could be a Notion database, an Airtable tracker, a Cowork-managed spreadsheet, an n8n workflow, or a custom Claude Project. For each, name the specific stage(s) it would help and what the setup cost is.

Output a Markdown document called "Career Pipeline — [my name]" with the eight stages mapped, plus the tool recommendations.
```

---

**What this produces:** A documented pipeline you can build a tracking system around. Many students stall in Stage 5 (interview prep) without realizing it; the pipeline view exposes where the bottleneck is.

**How to adapt this prompt:**
- *For your own project:* If you're not job-searching, replace the stages with the equivalent for your goal (PhD application: discovery → qualification → personal-statement drafting → recommender activation → submission → interview → decision).
- *For ChatGPT / Gemini:* Works as-is.
- *For Cowork:* After getting the design back, ask Cowork to set up the actual tracking spreadsheet. Sample follow-up: *"Create a Google Sheet (or local CSV) with one row per opportunity and columns matching the eight stages above. For each, include status, last-action-date, next-action-date, contract-status, and notes."*

**Connection to previous chapters:** Uses the Career PRD from Chapter 4 as the qualification filter (Stage 2).

**Preview of next chapter:** Chapter 6 builds an AI-powered career-search assistant on top of this pipeline.

---

### LLM Exercise — Chapter 6: AI Intelligence and Multi-Agent Systems

**Project:** Self-as-Project (will spawn one or more sub-Projects)
**What you're building this chapter:** A working **Career Search Assistant** — a Claude Project (or set of Projects) with custom instructions that automate the most repetitive parts of your search.
**Tool:** Claude Project (a NEW one for the Assistant, in addition to the main Personal Brand project) + Claude chat for testing.

---

**The Prompt:**

```
Design an AI assistant system to support my job search. Use Chapter 6's autonomy/orchestration framework.

I want THREE specialized assistants, not one mega-assistant. Each is a Claude Project with its own custom instructions. The orchestration is me — I send the right work to the right Project.

For each of the three, write:
1. The Project name
2. The Custom Instructions (system prompt) — paste-ready, ready to drop into Claude's "Custom Instructions" field
3. The kind of work I send it
4. Three example messages I might send it
5. The anti-hallucination guards built into its instructions

The three assistants:

ASSISTANT 1 — Application Drafter. Takes a job description + my Career PRD + the role description and produces a tailored resume bullet rewrite, a cover note, and a LinkedIn outreach message to anyone I know at the company.

ASSISTANT 2 — Interview Researcher. Takes a company name and produces: their recent funding/news, their published technical posts, their CEO's last 3 interviews, the team I'd join, intelligent questions I should ask. Forces "I cannot verify" labels on anything not in its training data and not provided by me.

ASSISTANT 3 — Reflection Coach. After every interview or networking conversation, I drop in my notes. The Coach asks me 3 sharp questions about what happened, what I noticed, what I would change next time. Forces specificity. No "great job!" affirmations.

For each assistant, the custom instructions should:
- Reference my archetype (so the voice stays consistent)
- Use my Career PRD as the filter for in-scope/out-of-scope work
- Include explicit instructions about NOT inventing things
- Include explicit instructions about pushing back on weak input

Output a Markdown document called "Career Search Assistants — [my name]" containing all three Project names, their full custom instructions ready to paste, the example messages, and a one-paragraph "how I orchestrate them" section explaining the workflow between them.
```

---

**What this produces:** Three deployed Claude Projects (after you paste the custom instructions in) plus the orchestration logic. This is the most immediately useful artifact of the semester for an active job search.

**How to adapt this prompt:**
- *For your own project:* Add or remove assistants based on your specific career stage. A senior engineer might want a Negotiation Assistant. A career-changer might want a Translation Assistant (translating their old field's accomplishments into the new field's vocabulary).
- *For ChatGPT / Gemini:* Replace "Claude Project" with "Custom GPT" (ChatGPT) or "Gem" (Gemini). The custom-instructions concept transfers.
- *For Claude Code:* Optional extension — turn the Application Drafter into a script that takes a job-posting URL and outputs the tailored materials as files.

**Connection to previous chapters:** The custom instructions for all three assistants reference your archetype (Ch 3) and Career PRD (Ch 4). The Reflection Coach connects to the pipeline stages from Chapter 5.

**Preview of next chapter:** Chapter 7 audits all the *interfaces* between you and the world — LinkedIn, GitHub, email signature, resume PDF — for alignment with what you're actually offering.

---

### LLM Exercise — Chapter 7: Interface Design and Deployment

**Project:** Self-as-Project
**What you're building this chapter:** A **Surface Alignment Audit** of every public interface a recruiter or hiring manager touches, plus one immediate fix to your most-used surface (typically LinkedIn).
**Tool:** Claude Project for the audit; Cowork or your browser for the actual LinkedIn updates.

---

**The Prompt:**

```
Run a Surface Alignment Audit on every interface between me and the people who decide whether to hire me. Use Chapter 7's framework: an interface promises something; the underlying system has to keep the promise; misalignment is brand damage compounding at session frequency.

The surfaces to audit:

1. LinkedIn — headline, photo, banner, About section, Featured section, current role description, skills, recommendations.
2. Resume — both versions if I have them (ATS + designer).
3. GitHub — profile README, pinned repos, contribution graph, organization memberships, starred repos.
4. Personal website — if it exists; if not, note "absent" as a separate finding.
5. Email signature — what an interviewer sees in our scheduling thread.
6. Twitter/X or other social — only if I'm active there professionally.
7. Any portfolio I've shared in the last 12 months.

For each surface, produce:
- What does it currently PROMISE? (the implicit claim a viewer reads from it)
- What does my underlying reality DELIVER? (the work, archetype, and capability behind the claim)
- ALIGNMENT VERDICT: aligned / overpromise / underpromise / misaligned-archetype
- ONE SPECIFIC FIX I can make today

Apply my Chapter 3 archetype as the alignment standard. A Sage's interfaces should not promise Hero outcomes. A Magician's interfaces should not read like a Caregiver's.

Then — pick the surface with the worst alignment score and write me the EXACT REPLACEMENT TEXT for it. Don't suggest "rewrite the headline to emphasize X." Write the new headline. Don't suggest "improve the About section." Write the new About section, in my voice, archetype-aligned, ready to paste in.

The replacement should be production-ready. I should be able to copy it into the surface and ship it before I sleep tonight.

Output a Markdown document called "Surface Alignment Audit — [my name] — [date]" with the audit table, the chosen surface, and the production-ready replacement text.
```

---

**What this produces:** An audit + one shipped fix the same day. The audit becomes a checklist you re-run quarterly.

**How to adapt this prompt:**
- *For your own project:* If certain surfaces don't apply (no Twitter, no website yet), mark them as "future work" and audit only what exists. The audit's value scales with what you have.
- *For ChatGPT / Gemini:* Works as-is.
- *For Cowork:* After getting the replacement text, ask Cowork to actually save it as a `.md` file with the exact text you'll paste into LinkedIn. Mini-discipline: name the file `2026-XX-XX-linkedin-headline-v[N].md` so you have a version history of how your surfaces have evolved.

**Connection to previous chapters:** Tests the archetype (Ch 3) and Career PRD (Ch 4) against actual public artifacts. Uses the Application Drafter from Chapter 6 if you want to A/B test different versions.

**Preview of next chapter:** Chapter 8 writes the master one-page Personal Brand Strategy — the document that all surfaces from now on will answer to.

---

### LLM Exercise — Chapter 8: Brand Strategy

**Project:** Self-as-Project
**What you're building this chapter:** Your one-page **Personal Brand Strategy** — the master document everything else (visual identity, storytelling, portfolio, presentation) will derive from.
**Tool:** Claude Project.

---

**The Prompt:**

```
Write my one-page Personal Brand Strategy. This is the master document for the rest of the semester. Every later artifact has to be consistent with what we lock here.

The eight required sections:

1. MISSION (one sentence). The work I exist to do. NOT my job description. The actual aim.
2. VISION (1–2 sentences). The world I'm working toward.
3. VALUES (3–5 commitments). Each value must imply at least two specific decisions I would make differently from someone with different values. "Integrity" is not a value; it's a wish. "I will not work for companies whose product I cannot defend at a dinner party" is a value.
4. UVP — Unique Value Proposition (one sentence). What I specifically offer that another engineer at my level does not.
5. ARCHETYPE (named, with two sentences of expression). My Chapter 3 archetype, applied with strategic depth. Plus one sentence on the shadow as a known failure mode I'm watching.
6. VOICE (notes). Sentence rhythm, vocabulary preferences, formats I favor and reject.
7. POSITIONING (one paragraph). Who I compete with, who I complement, where in the field I sit.
8. NEGATIVE SPACE — the no-list. At least 5 specific things I will not do that another engineer at my level might. The negative space is the brand. This section does most of the work.

Plus:
- A one-sentence TAGLINE I could put under my name on a resume or portfolio.
- A DOMAIN decision: what URL my personal site will live at, with one-sentence reasoning.

Use my full prior context — Personal Brand Baseline (Ch 1), Career Architecture (Ch 2), Archetype Commitment (Ch 3), Career PRD (Ch 4), Career Pipeline (Ch 5), Search Assistants config (Ch 6), Surface Audit (Ch 7) — as the source material.

Two non-negotiable tests when you write the doc:
1. The negative-space section must let a reader predict three specific things I would say no to. If the reader can't predict, the section is decoration.
2. Every value must imply at least two concrete decisions. If the value is unactionable, replace it.

Output a Markdown document called "Personal Brand Strategy v1 — [my name]". One page. If it goes to two pages, you have not yet specified enough — you are listing instead of deciding.
```

---

**What this produces:** A one-page master document. Every chapter from here forward references it. Recruiters who ask "tell me about yourself" get a version of this read aloud.

**How to adapt this prompt:**
- *For your own project:* Run this prompt twice — once "honest" (what is true now), once "aspirational" (what you're building toward over 18 months). Compare. The gap is the work plan.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not the right tool.

**Connection to previous chapters:** This document synthesizes everything from Chapters 1–7. It is the chapter where the personal-brand build crystallizes.

**Preview of next chapter:** Chapter 9 turns the strategy into a visual identity system — palette, type, mood, wireframe for your personal site.

---

### LLM Exercise — Chapter 9: Visual Identity Systems

**Project:** Self-as-Project
**What you're building this chapter:** A **Personal Visual System** — palette, typography, mood board, and wireframe for your personal website.
**Tool:** Claude Project for the system; Figma (or Excalidraw / Whimsical / pen and paper) for the wireframe.

---

**The Prompt:**

```
Build a Personal Visual System for me, derived from my Personal Brand Strategy v1. The deliverables here will feed the portfolio site I build in Chapter 11.

Five components, each constrained by my archetype:

1. CREATIVE BRIEF (1 page). The strategy-to-design translation. Sections:
 - Brand strategy summary (pulled from Chapter 8 doc — 3–4 sentences)
 - Project scope (what I'm designing: personal site + LinkedIn banner + resume header)
 - Audience (named — who is reading my materials)
 - Tone words (3–5 archetype-aligned adjectives — "innovative" and "modern" forbidden; force specificity)
 - 3 references (link or describe — work I want my materials to feel like, with one-line notes on what specifically about each one works)
 - 3 anti-references (work I want my materials to NOT feel like, with one-line notes on why each one fails the brief)

2. COLOR PALETTE. Primary, two accents, neutrals (near-black, near-white, two grays). Specify each color as both a name (e.g., "Forest Slate") and a hex code. Test every text-on-background combination against WCAG AA minimum (4.5:1 for normal text, 3:1 for large text and UI). Document the contrast ratios. If a combination fails, propose an adjusted hex that passes.

3. TYPOGRAPHY PAIR. One display face for headlines, one body face for running text. Both should be free or have a free option (Google Fonts, open-source releases). Justify each choice against my archetype. Specify weights: at minimum a heavy display weight, a regular body weight, and one alternate (italic or medium) for emphasis. Specify sizes for h1, h2, h3, body, caption, UI.

4. MOOD BOARD INSTRUCTIONS. Tell me to pull together 6–10 images that capture the visual feel. List specifically what to look for (e.g., "find 2 examples of personal sites by Sage-archetype practitioners that use serif typography for body text and a single accent color"). Caption requirements for each image: what about it works for me.

5. WIREFRAME for my personal site. Low fidelity. Pages: home, about, projects/case studies, writing/thought leadership, contact. For each page: section blocks in order, layout grid (column count, max content width), visual hierarchy, components reused across pages. Format the wireframe as either ASCII boxes or a structured Markdown description detailed enough that I could build it in v0 from your description alone.

Apply my archetype as the constraint throughout. A Sage palette is restrained and high-contrast. A Hero palette is saturated with strong primaries. A Magician palette uses jewel tones with intentional gradient affordances. Match.

Output a Markdown document called "Personal Visual System v1 — [my name]" with all five components.
```

---

**What this produces:** A complete visual identity spec ready to be implemented in v0 (Chapter 11).

**How to adapt this prompt:**
- *For your own project:* If you already have visual brand work (a logo, a chosen typeface), provide it as input and ask for an audit + alignment fix instead of a from-scratch design.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Once you have the spec, you can ask Claude Code to generate a Tailwind config (`tailwind.config.js`) that encodes the palette and typography as design tokens. Useful for Chapter 11.

**Connection to previous chapters:** Brand Strategy (Ch 8) is the source. Surface Audit (Ch 7) tells you which existing surfaces need refresh first.

**Preview of next chapter:** Chapter 10 writes your origin story, one customer-as-hero case study, and your first published thought-leadership piece.

---

### LLM Exercise — Chapter 10: Brand Storytelling

**Project:** Self-as-Project
**What you're building this chapter:** Three stories — your **origin story**, one **case study** (in customer-as-hero format), and one **published thought-leadership piece**.
**Tool:** Claude Project for drafting; LinkedIn / Substack / your blog for publishing.

---

**The Prompt:**

```
Write three pieces of brand storytelling for me. All three must be archetype-aligned per my Personal Brand Strategy v1.

PIECE 1 — ORIGIN STORY (300–500 words).
How I became the engineer/designer/practitioner I am. Use the Hero's Journey simplified arc: ordinary world (where I started), call (the moment something pulled me toward this work), threshold crossing (the first real commitment), tests and allies (the work that shaped me), the boon I bring back (what I now offer).

The story must be true. No invented turning points. If I don't have a clear "call" moment, write the version that's closest to true and flag the synthetic compression.

The story must NOT be a resume in prose. A resume lists. A story shows. The reader should feel one specific scene clearly enough to picture it.

PIECE 2 — CASE STUDY (800–1,200 words).
Pick ONE project from my history (could be a class project, an internship project, my AI tool from this course, an open-source contribution, anything I've shipped). Write it as a customer-as-hero case study.

Format:
- Customer (the team / user / class / community I served — they are the protagonist)
- Problem they had (specific, recognizable, with stakes)
- What they tried before that didn't work
- Approach I brought (the work I did — but framed as serving the customer, not showcasing me)
- Transformation (what changed because of the work — specific outcomes, numbers if I have them)
- What I learned (the meta-lesson the project produced)

I am the GUIDE in this story, not the hero. Yoda, not Luke. Most engineers get this backwards. Hold the line.

PIECE 3 — THOUGHT-LEADERSHIP PIECE (800–1,500 words).
Write one substantive piece of public-facing writing. Topic must be archetype-aligned and connected to the kind of work I want to be hired for. Sage-archetype Substack post — explain a mechanism. Hero-archetype LinkedIn article — make a case for a position the field hasn't fully accepted. Magician-archetype blog post — show a transformation that surprised me.

The piece is not allowed to be:
- A "lessons learned from my AI tool project" post (lazy, every student writes this)
- A summary of a paper I read (no original work)
- An "I'm excited to announce" post (announcement, not thinking)

The piece should advance one specific idea I have about my field that not everyone holds. It should be defensible — a hostile reader could push back, but I have the evidence.

Output three Markdown documents:
1. "Origin Story — [my name]"
2. "Case Study — [project name] — [my name]"
3. "[Piece title] — [my name]"

For each, suggest the publication channel (LinkedIn article / Substack / personal blog / Medium) and the optimal day-of-week and time-of-day to publish it for my archetype's typical audience.
```

---

**What this produces:** Three pieces of finished writing. One published before Chapter 11. The other two slot directly into your portfolio's About and Case Studies sections.

**How to adapt this prompt:**
- *For your own project:* Iterate on each piece separately. Run Piece 3 multiple times with different topics until one feels right.
- *For ChatGPT / Gemini:* Works as-is.
- *For Claude Code:* Not relevant here — pure writing.

**Connection to previous chapters:** Pulls voice from Chapter 8 strategy. Will populate the portfolio in Chapter 11.

**Preview of next chapter:** Chapter 11 deploys your portfolio site using v0 or Framer, with these stories as content.

---

### LLM Exercise — Chapter 11: Portfolio as Product

**Project:** Self-as-Project
**What you're building this chapter:** A **deployed portfolio at a public URL**, archetype-aligned, with the AI tool you built (the book's main thread) integrated as a centerpiece case study.
**Tool:** Claude Code OR v0.app (recommend v0 for most learners; Claude Code if you want to fully own the codebase).

---

**The Prompt:**

```
[FOR v0.app: paste this into v0 directly, in the "Generate" prompt field]
[FOR Claude Code: open Claude Code in your portfolio directory and paste this]
[FOR Claude Project: this generates the prompt + content; you'll use v0 separately]

Generate a personal portfolio site for me using React + Tailwind + shadcn/ui. The site should match the Personal Visual System v1 I produced in Chapter 9 (palette, typography, layout grid, archetype) and use the content I produced in Chapter 10 (origin story, case study, thought-leadership piece).

Pages required:
1. HOME. Above the fold: my name, my one-sentence positioning (from Brand Strategy Ch 8), a clear primary CTA. Below: a "Selected Work" section with 3 project cards (use placeholders if I haven't filled them in yet). A "Writing" section with at least one published piece.
2. ABOUT. My origin story (from Chapter 10). Photo placeholder. Optional values list (drawn from Brand Strategy values). Contact-me CTA.
3. WORK / CASE STUDIES. List of all case studies as cards. One detail page per case study (use my Chapter 10 case study as the template).
4. WRITING. Index of published pieces. Each piece links out to its actual published location (LinkedIn, Substack, etc.) — do not republish in full on the portfolio.
5. CONTACT. Email, LinkedIn, GitHub, optionally Twitter/X. No contact form unless I want one (most don't get used).

Visual constraints:
- PALETTE: [paste your Chapter 9 palette hex codes]
- TYPOGRAPHY: [paste your Chapter 9 type pair, with sizes]
- ARCHETYPE: [paste your archetype name]
- TONE: [paste 3 tone words from Ch 9 brief]

Behavior constraints:
- Mobile-responsive at 375px, 768px, 1280px.
- WCAG AA contrast across all text.
- All images have alt text.
- The site is keyboard-navigable end-to-end.
- Lighthouse performance score 90+ on the deployed version (no full-bleed video, no auto-playing media).

Generate the React components for all five pages plus a shared header/footer. Use shadcn/ui components where appropriate. Use Tailwind utility classes. No CSS-in-JS.

After generating: deploy to Vercel (v0 makes this one click), or output the file structure for me to deploy via Claude Code. Give me the public URL when it's live.

Then audit your own output: name three things you'd change before sending recruiters there. I want self-criticism, not affirmation.
```

---

**What this produces:** A live, deployed portfolio at a public URL. The most important single artifact you'll produce in the semester for the job search.

**How to adapt this prompt:**
- *For your own project:* If you already own a `.dev` or `.com` domain, point it at the v0 deployment. If you don't, register one this week — your name, your name + your role, or an archetype-aligned word.
- *For ChatGPT / Gemini:* These tools cannot directly generate deployable React the way v0 can. Use them to draft the content; use v0 or Claude Code for the implementation.
- *For Claude Code:* Better than v0 if you want a portfolio you can keep customizing in code. v0 is faster to a deployed result. Pick based on your tradeoff between speed and ownership.
- *For Cowork:* Use Cowork after deployment to add new case studies, update copy, manage the source files locally.

**Connection to previous chapters:** Implements the Visual System (Ch 9), populates with Stories (Ch 10), structured by the wireframe (Ch 9 again). The whole semester compounds here.

**Preview of next chapter:** Chapter 12 builds your two-version resume, finalizes LinkedIn, and produces your 10/20/30 final pitch deck — all consistent with the deployed portfolio.

---

### LLM Exercise — Chapter 12: Professional Presence and Launch

**Project:** Self-as-Project
**What you're building this chapter:** The launch package — **two-version resume**, **finalized LinkedIn**, **10/20/30 pitch deck of yourself**, and a **launch announcement post**.
**Tool:** Claude Project for drafting; Google Docs / Word for the resume PDF; Pitch / Beautiful.ai / Google Slides for the deck; Cowork for assembling final files.

---

**The Prompt:**

```
Build my complete launch package. This is the final integration. Every artifact must be consistent with the Personal Brand Strategy v1 (Ch 8), the Visual System (Ch 9), and the deployed portfolio (Ch 11).

DELIVERABLE 1 — RESUME, ATS-OPTIMIZED VERSION.
Single column. Standard section headers (Experience, Education, Skills, Projects). No graphics, no two-column layouts. Plain text saved as both .docx and .pdf. Keyword-rich for the kind of role described in my Career PRD (Ch 4).
For each role, write 3–5 outcome-oriented bullets, not responsibility-oriented bullets. Outcome example: "Built data pipeline ingesting 870 articles per day with 90% deduplication rate." Responsibility example: "Worked on data engineering tasks." First is hireable; second is not.
If I don't have specific numbers for a bullet, leave a [verify with X] tag rather than inventing a number.

DELIVERABLE 2 — RESUME, DESIGNER VERSION.
Same content, visually distinctive. Uses my palette (from Ch 9) and type pair. Uses my tagline from the Brand Strategy. Saved as PDF only. Should signal craft within 5 seconds of opening.

DELIVERABLE 3 — LINKEDIN FINALIZATION.
Paste-ready text for: headline (under 220 characters), about section (under 2,000 characters), the "Featured" section's three pinned items (portfolio URL, AI-tool URL, published thought-leadership piece). Plus rewrites of my current role description and one prior role description. All archetype-aligned.

DELIVERABLE 4 — 10/20/30 PITCH DECK OF MYSELF.
Ten slides. 20 minutes spoken. 30-point font minimum.
Slide structure for a "pitch yourself" deck:
1. Title — name, role-claim, one-sentence positioning
2. Problem — what hiring teams in my target market struggle with
3. Solution — me as the answer, expressed in one specific value claim
4. How it works — my methodology (the Madison-pattern reference if relevant; the four-verb framework from Ch 1)
5. Demo / proof — my AI tool URL, screenshot, one-line outcome
6. Brand position — archetype, voice, what I refuse to do
7. Track record — work history compressed to its three most relevant accomplishments
8. Roadmap — what I want to be doing 12 months from now
9. Team / collaborators — one slide on who I work well with and why
10. Ask — what I want from the audience (interview, referral, advisor relationship, partnership)

For each slide, give me the headline (large, 30+ pt), the body content (3 bullets max OR a single image / chart description), and the speaker note (what I'd say while the slide is on screen — should fit in 1.5–2 minutes).

DELIVERABLE 5 — LAUNCH POST.
A single LinkedIn post (or Substack post if my archetype is Sage-publication-leaning) announcing the portfolio + AI tool + intent. Opens in a scene, not in a "I'm excited to announce." 200–400 words. Includes the portfolio URL and the AI tool URL. Ends with a specific ask.

Output five Markdown files, one per deliverable, ready to paste or convert. After all five, write me a one-paragraph "How to use this package over the next 30 days" — what I do with it, in what order.
```

---

**What this produces:** Five finished artifacts. Combined, they are the launch.

**How to adapt this prompt:**
- *For your own project:* If you're applying to fewer than 10 roles, drop Deliverable 1 (ATS version) and lean on Deliverable 2 alone. ATS resume-tailoring matters at scale, not at single-digit application counts.
- *For ChatGPT / Gemini:* Works as-is.
- *For Cowork:* After getting the five Markdown files, ask Cowork to compile them into a single zipped "launch package" folder with consistent filenames. Drop the deck content into Pitch or Google Slides separately for the visual layout.
- *For Claude Code:* Not the right tool — text and structured docs.

**Connection to previous chapters:** Synthesizes everything. The deck slide 5 ("demo / proof") needs the AI tool URL from Chapter 7. The portfolio link comes from Chapter 11. The voice is locked from Chapter 8. The visual choices are locked from Chapter 9. The case-study content from Chapter 10 feeds into the deck's track-record slide.

**Preview of next chapter:** None — this is the last. The next exercise is real life. Send the launch post. Go to interviews. Iterate.

---

## Closing note for the learner

You started the semester with a baseline (Chapter 1). You now have:

- A documented archetype with a shadow watchlist
- A career architecture mapping the work onto five layers
- A one-page Career PRD as a decision filter
- A pipeline with documented contracts and degraded modes
- Three working AI assistants tailored to your search
- A surface alignment audit with at least one shipped fix
- A one-page Personal Brand Strategy locking everything together
- A complete visual identity system with WCAG-tested palette
- An origin story, a case study, a published thought-leadership piece
- A deployed portfolio at a public URL
- A two-version resume, finalized LinkedIn, a 10/20/30 self-pitch deck, and a launch post

The compounding starts now. The semester gave you the artifact. The next twelve months are about whether you keep the discipline going.

Run the Surface Alignment Audit (Ch 7) once a quarter. Add one case study to your portfolio per quarter (Ch 11 framework). Publish on the cadence you committed to in Ch 10. Re-run the Personal Brand Strategy v1 against your reality every six months — version it forward (v2, v3) so you can see the drift.

The Creative Engineer is not a credential. It is a practice. You're now practicing.

Go ship.

---

## Adaptation notes for instructors

- These exercises assume the learner has access to **Claude Pro / Team** for Projects. If a cohort uses ChatGPT instead, swap "Claude Project" → "Custom GPT" in the setup and Chapter 6 exercises. Other prompts work as-is.
- The exercises **build dependencies** chapter-to-chapter. A student who skips Ch 4 will struggle with Ch 5–8. Either enforce sequence or build a "catch-up" mini-prompt for any skipped chapter.
- Ch 6 (three Claude Projects) and Ch 11 (deployed portfolio) are the **highest-leverage** exercises. A cohort short on time should not skip these.
- For **non-job-searching cohorts** (PhD applicants, founders, career-changers), reframe the Career PRD's "audience" from hiring manager to admissions committee / investor / hiring committee in your specific market.
- The exercises are written assuming **archetype is committed by Ch 3**. If a cohort hasn't committed by then, either pause and recommit, or run Ch 3 twice (once provisional, once final) before proceeding.

---

*Generated from the Self-as-Project running track for INFO 7375 — Branding and AI: Building the Creative Engineer.*
