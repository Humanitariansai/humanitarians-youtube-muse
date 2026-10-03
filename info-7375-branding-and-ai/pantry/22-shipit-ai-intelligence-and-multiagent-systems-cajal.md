# CAJAL Figure Report — Appendix S3: AI Intelligence and Multi-Agent Systems
*Chapter slug: 22-shipit-ai-intelligence-and-multiagent-systems*
*Hands-on multiagent / AI-intelligence build chapter. Favor systems diagrams, agent-orchestration graphs, sequence/workflow diagrams.*

---

## FIGURE 1 — The four patterns of AI intelligence · Critical · comparison matrix
A four-row reference matrix laying out the chapter's spine: Single LLM call, Chained calls, Tool-using agent (ReAct), and Multi-agent system. Columns: who controls the next step, representative tools/products, best used when, primary failure mode. The matrix establishes that "adding AI" is not one thing — each pattern has a distinct risk profile. Fully greyscale; this is a neutral reference table where all four patterns are peers.
EXCLUSIONS: no red, no autonomy-axis grid (that is Figure 2), no n8n node icons, no decorative color coding of rows, no archetype content.

## FIGURE 2 — The autonomy / orchestration grid · Critical · conceptual map (two-axis quadrant)
A two-axis scatter grid: x-axis "Agent decision autonomy (low → high)", y-axis "Orchestrator control (low → high)". Place autonomous agents (high autonomy / low orchestrator), orchestrated multi-agent (low autonomy / high orchestrator), conversational multi-agent (middle), and a label noting single-call / chained patterns sit outside the grid. Madison is marked in the orchestrated quadrant. RED ELEMENT: the Madison/orchestrated marker — the single point the reader must locate, the chapter's recommended position.
EXCLUSIONS: no second red mark, no AutoGPT cost figures, no four-pattern columns (that is Figure 1), no failure-mode text inside cells.

## FIGURE 3 — Architecture A vs Architecture B as a brand experience · Important · comparison panels
Two side-by-side panels for identical capability: Architecture A (autonomous, transparent — user watches the reasoning trace) vs Architecture B (orchestrated, competent — structured brief in, finished report out). Each panel shows the user-facing flow and a "when it works / when it fails" line, surfacing that A's brand is transparency and B's brand is competence. Fully greyscale; the two architectures are genuine peers, neither universally correct.
EXCLUSIONS: no red, no archetype-mapping rows (that is Figure 4), no underlying-model detail, no quadrant axes.

## FIGURE 4 — Archetype-to-architecture mapping · Important · comparison matrix
A mapping table: rows Sage, Creator, Explorer, Hero, Caregiver. Columns: recommended architecture tendency, the shadow expressed as an AI failure mode, what to watch for in production. Shows that the architectural choice expresses the archetype or its shadow. Fully greyscale.
EXCLUSIONS: no red, no Madison agent code, no autonomy grid, no decorative archetype icons.

## FIGURE 5 — Compounding error: probability of an error-free chain · Critical · line chart
A line chart, x-axis agent steps 0–40, y-axis probability of error-free output (0–100%). Two decay curves: a 10%-per-step error line (0.9^n) and a 5%-per-step error line (0.95^n). Annotate at steps 10, 20, 40 to show geometric collapse (≈35%, ≈12%, ≈1.5% for the 10% line). RED ELEMENT: the 10%-per-step curve — the line the reader must read first, the canonical AutoGPT-range collapse the section warns about. The 5% line stays grey.
EXCLUSIONS: no second red, no cost-runaway data, no bars (line chart only), y-axis must start at zero.

## FIGURE 6 — Three autonomous-agent failure modes · Important · conceptual map
Three labeled blocks — Compounding error, Cost runaway, Trust collapse on visible failure — each with its mechanism in one line (step N built on a wrong step N-1; arbitrarily many paid calls with no ceiling; visible failure damages trust more than opaque failure). A footer band names the three production controls that prevent cost runaway: max step count, per-execution cost ceiling, repeated-call circuit breaker. Fully greyscale.
EXCLUSIONS: no red, no probability curve (that is Figure 5), no orchestration trade-off rows (that is Figure 8), no emoji.

## FIGURE 7 — Anatomy of the competitor_analyst agent · Important · annotated example
An annotated CrewAI Agent specification (the competitor_analyst). Central code block with leader lines to four callouts: role activates training-data associations; goal carries a discipline ("set it null and explain limitations"); backstory is personality + brand commitment; allow_delegation=False is the orchestration commitment in code. A closing note: when it fails, it fails locally. Fully greyscale.
EXCLUSIONS: no red, no full Climate-analyst spec, no anti-hallucination pattern ladder (that is Figure 9), no autonomy grid.

## FIGURE 8 — Orchestrated vs autonomous vs chained: the trade-off · Important · comparison matrix
A trade-off matrix. Columns: autonomous agents, orchestrated multi-agent, chained calls. Rows: predictability, debugging surface, specification cost, failure visibility, cost control. Shows no architecture wins on every dimension — the engineer chooses where to sit. Fully greyscale; the three columns are peers in a deliberate trade-off.
EXCLUSIONS: no red, no autonomy grid, no Madison code, no four-pattern overlap with Figure 1 (this is trade-offs, not definitions).

## FIGURE 9 — Three anti-hallucination patterns · Supplementary · comparison panels
Three stacked panels showing the same agent handling an unavailable data point three ways, weakest to strongest: Pattern 1 permission to abstain ("I cannot verify this"); Pattern 2 structured null fields with a note; Pattern 3 confidence labeling (verified | inferred | unverifiable). A note that Pattern 2 is the recommended starting point. Fully greyscale.
EXCLUSIONS: no red, no agent-anatomy leader lines (that is Figure 7), no full code spec, no decorative color per pattern.

## FIGURE 10 — The AI layer inside a deterministic pipeline · Critical · process flowchart
A horizontal left-to-right flow: Fetch (prepare input) → AI step (process) → Format (normalize output) → Validate (schema check) → Write (store). A branch off Validate routes to an error handler when the schema is invalid (error surfaced, not propagated). Shows the two minimum-viable disciplines: AI wrapped in deterministic neighbors, and output validated before downstream use. RED ELEMENT: the Validate → error-handler branch — the single mechanism the reader must notice, the thing that separates production discipline from a floating AI node.
EXCLUSIONS: no second red, no four-pattern table, no autonomy grid, no n8n-specific UI chrome.

---

## Video candidates

FIGURE the-four-patterns-of-ai-intelligence — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE the-autonomy--orchestration-grid — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE architecture-a-vs-architecture-b-as-a-brand-experience — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE archetype-to-architecture-mapping — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE compounding-error-probability-of-an-error-free-chain — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE three-autonomous-agent-failure-modes — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE anatomy-of-the-competitoranalyst-agent — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE orchestrated-vs-autonomous-vs-chained-the-trade-off — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE three-anti-hallucination-patterns — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE the-ai-layer-inside-a-deterministic-pipeline — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.

**Chapter recommendation:** **the-ai-layer-inside-a-deterministic-pipeline** — the sole video candidate; a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
