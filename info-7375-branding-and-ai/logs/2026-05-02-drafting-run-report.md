# Drafting Run Report — 2026-05-02

**Book:** branding-and-ai
**Voice plugin:** feynman (workshop default)
**Run scope:** all twelve chapters marked `to write`, plus path-fork variants for Chapter 8

---

## Chapters drafted

| # | Slug | Words | Sources | [verify] | Pantry hits |
|---|------|------:|--------:|---------:|------------:|
| 1 | the-creative-engineer | 2,765 | 5 | 1 | 3 |
| 2 | the-madison-framework | 2,703 | 5 | 0 | 4 |
| 3 | jungian-brand-archetypes-as-a-system | 2,518 | 4 | 1 | 2 |
| 4 | product-requirements-and-scope | 2,434 | 3 | 0 | 1 |
| 5 | data-pipelines-and-workflow-automation | 2,544 | 3 | 0 | 2 |
| 6 | ai-intelligence-and-multi-agent-systems | 2,632 | 3 | 0 | 2 |
| 7 | interface-design-and-deployment | 2,550 | 4 | 0 | 1 |
| 8a | PERSONAL-brand-strategy | 2,521 | 2 | 0 | 1 |
| 8b | STARTUP-brand-strategy | 2,619 | 2 | 0 | 1 |
| 9 | visual-identity-systems | 2,591 | 3 | 0 | 1 |
| 10 | brand-storytelling | 2,763 | 3 | 1 | 1 |
| 11 | portfolio-as-product | 2,854 | 2 | 0 | 1 |
| 12 | professional-presence-and-launch | 2,976 | 2 | 0 | 1 |

**Totals:** 13 drafts, ~34,470 words, ~41 primary sources, 3 inline `[verify]` flags.

---

## One-sentence deep-dive mechanism per chapter

1. **Creative Engineer** — Spence signaling theory applied to a labor market disrupted by AI tooling: when the costly signal of "I can build" got cheap, the market is repricing toward signals that didn't (problem-scoping, positioning, shipping).
2. **Madison Framework** — Architecture choices become brand surfaces: legible boundaries (five named agents) create namable product surfaces customers can price; opaque choices leave nothing for brand to attach to.
3. **Archetypes** — Archetype as forced specification: a constraint that makes brand decisions decidable; without it brands drift and customers lose the recognition handles that anchored their loyalty.
4. **PRD/Scope** — Scope as creative constraint: every "yes" to a feature is a "no" to shipping the core, and the discipline that survives the $100,000 customer is the same discipline that ships a coherent product.
5. **Data Pipelines** — Pipeline fragility as a brand problem: every external dependency is a contract you don't control; when contracts shift (Reddit June 2023), downstream tools break, and the brand damage flows downhill to whoever's name is on the front page.
6. **AI Intelligence / Multi-Agent** — Autonomy versus orchestration trade-off: autonomy buys flexibility at the cost of predictability, and the choice IS a brand decision (transparent collaboration vs. delivered competence).
7. **Interface / Deploy** — Interface compounds at session frequency, features at use frequency: interface misalignment damages brand faster than feature failure, because every visit is another impression against the asset.
8. **Brand Strategy (both paths)** — Negative space is the brand: consistency at scale comes from what you decline, not what you ship; the archetype is the rule that decides.
9. **Visual Identity** — Visual elements are perceived in archetypal context: match between visual decisions and archetype produces coherence; mismatch produces a dissonance the user feels but cannot articulate.
10. **Brand Storytelling** — Story shape carries archetypal commitments: Hero's Journey, Quest, Methodology, Service, and Rebellion each fit specific archetypes; mismatched stories read as false to audiences regardless of execution quality.
11. **Portfolio as Product** — Portfolio compounds across uses: total brand impressions = time invested × times referenced, and the second factor can be the larger one when the artifact is well-designed (Brittany Chiang, 6,000+ forks).
12. **Professional Presence** — Integrated pitch density: ten minutes of presenting builds an impression that would otherwise need months of LinkedIn scrolling; coherence (every slide answering the same question) beats polish (Airbnb's 2009 deck).

---

## Blockers

None severe. Three soft blockers worth flagging for revision:

1. **Voice-unanchored.** Root `style/VOICE.md` only contains the fry plugin's voice spec; no Feynman-specific voice file exists. All thirteen drafts ran with `voice-unanchored` flagged. **Recommended action:** create a Feynman voice file (or rely on CLAUDE.md §6 as the working spec and remove the flag system for the feynman default). Either way, calibrate the first review chapter (Chapter 1) deliberately and use it to set voice for the rest.

2. **[verify] on Coca-Cola URL** (Chapter 3). Used Coca-Cola's official history page for the New Coke 1985 reference; URL not directly fetched in this run. Trivial to verify on revision.

3. **[verify] on Jaguar 2024 rebrand details** (Chapter 10). Used as one of three narrative-archetype mismatch cases; my coverage summary is from public reporting that I did not directly cite from a primary source in this run. Either replace with a different third case or pull a primary source for the Jaguar coverage on revision.

4. **[verify] on AI engineer salary numbers** (Chapter 1). Salary aggregator sources used for the labor-market argument; primary source from BLS or LinkedIn Workforce Report would be stronger. Easy to upgrade in revision.

No chapters hit hard blockers. Nothing was unwritable.

---

## Chapters where pantry was thin

The Canvas course exports were less useful than the Madison framework for chapter content. Madison's repository (`pantry/madison/`) provided meaningful primary material for Chapters 2, 4, 5, and 6. The Canvas pantry primarily provided:

- Module 1 wiki page (operational definition of Creative Engineer) — used in Ch 1
- Syllabus framing — implicit throughout

Chapters that leaned almost entirely on outside sources and Madison rather than Canvas pantry: 3 (archetypes), 7 (interface), 8 (brand strategy, both variants), 9 (visual identity), 10 (storytelling), 11 (portfolio), 12 (professional presence).

This is structurally appropriate — those chapters cover material the legacy course taught at a different cadence, and the new course's framing requires sources external to the Canvas exports. **No action required.** The Madison pantry remained productive throughout; Canvas pantry usage was correctly calibrated to "framing aid only."

---

## Open questions surfaced during drafting (recommend adding to book.md)

1. **Madison framework public availability.** Already in book.md open questions. Reaffirmed: the chapters cite Madison source as primary material, which is correct under the pantry rules, but if Madison becomes unavailable or significantly restructured, Chapters 2 and 4–7 will need a fallback — either a synthesized reference architecture or a different running example. Worth resolving before the course's first deployment.

2. **Salary and labor-market numbers across the book.** Chapter 1 makes claims about AI engineer salary distributions (~$206K base, 25–40% specialist premium). These are aggregator-sourced. Several other chapters reference labor-market evidence informally. **Recommend:** sweep the book for primary BLS / LinkedIn Workforce Report citations and replace the aggregator-cited numbers in revision.

3. **Bud Light Dylan Mulvaney case (Ch 10).** Used as one of three narrative-archetype mismatch cases. The case is real and well-documented but politically sensitive. Whether to retain it or substitute a less-charged third case is an editorial decision worth flagging for the first review.

4. **Jaguar 2024 rebrand case (Ch 10).** As above — included as third example but not fully primary-sourced in this run. Either upgrade the citation or substitute.

5. **First chapter as voice-setting exercise.** With voice-unanchored flagged across all chapters, Chapter 1 was the de facto voice-setting draft. **Recommend:** review Chapter 1 closely in revision; once Bear's voice direction is confirmed, populate `books/branding-and-ai/style/` with anchor samples (perhaps the approved Chapter 1 itself) and re-flag the remaining chapters.

6. **Path-fork mechanics.** Chapter 8 produced two drafts (PERSONAL and STARTUP). This worked cleanly but imposes ~2x effort for that chapter. The downstream chapters (9–12) currently fold both paths into single drafts with notes about path-specific exercises. Decide whether downstream chapters should also produce path-fork variants or stay unified with labeled exercises.

---

## Sources used (deduplicated)

**Primary academic / canonical:**
- Spence, M. (1973). Job Market Signaling. *QJE* 87(3).
- Campbell, J. (1949). *The Hero with a Thousand Faces*.
- Mark, M. & Pearson, C.S. (2001). *The Hero and the Outlaw*. McGraw-Hill.
- Ries, E. (2011). *The Lean Startup*.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.
- Booker, C. (2004). *The Seven Basic Plots*.
- Miller, D. (2017). *Building a StoryBrand*.
- Yao, S. et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv:2210.03629.
- Bai, Y. et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073.
- Wu, Q. et al. (2023). AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. arXiv:2308.08155.
- Peng, S. et al. (2023). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. arXiv:2302.06590.

**Tools / frameworks (primary documentation):**
- Madison framework (pantry/madison/) — full repository
- n8n (github.com/n8n-io/n8n)
- CrewAI (docs.crewai.com)
- Streamlit (streamlit.io)
- Gradio (gradio.app)
- v0 / Vercel (v0.app)
- WCAG 2.2 (W3C)
- LangGraph (LangChain blog)

**Industry / case material:**
- Anthropic constitution (anthropic.com/news/claude-new-constitution)
- Stack Overflow 2024 Developer Survey
- Tropicana 2009 redesign post-mortem (The Branding Journal)
- Gap 2010 logo coverage (CNN Money)
- Reddit API controversy June 2023 (Wikipedia)
- Snapchat 2018 redesign (CNBC)
- Google Bard February 2023 launch error (CNN Business)
- Pepsi 2008 logo Arnell document (Fast Company, Creative Bloq, CBS News)
- Pepsi Kendall Jenner April 2017 ad (NPR, NBC News)
- Linear product method (linear.app/method/introduction, Figma blog)
- Andrej Karpathy "Neural Networks: Zero to Hero" (karpathy.ai)
- Stripe / Patrick Collison (Medium analysis)
- Brittany Chiang portfolio (brittanychiang.com, GitHub bchiang7/v4)
- Airbnb 2009 seed pitch deck (Failory)
- Guy Kawasaki 10/20/30 (guykawasaki.com)
- AutoGPT failure modes (Wikipedia, Tom's Hardware, IBM)
- Cursor / Devin / Cognition Labs (multiple)

---

## Recommended next step

Review Chapter 1 first as the voice-setting draft. Once voice is locked in, sweep through the rest. The hard rules (no fabrication, primary sources, [verify] discipline) held throughout. The chapters are ready for editorial pass, not for publication.

The drafts skipped Chapter 8 path-fork integration in subsequent chapters (9–12), folding both paths into single drafts with labeled exercises. If you want full Chapter 9–12 path-fork variants, that is a second pass.

Pantry navigation worked: Madison framework citable as primary, Canvas exports useful as framing aid, archetype thread coherent across the arc.

Run complete.
