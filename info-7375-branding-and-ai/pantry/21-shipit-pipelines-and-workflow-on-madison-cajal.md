# CAJAL Figure Report — 21 ShipIt: Pipelines and Workflow on Madison

Source chapter: chapters/21-shipit-pipelines-and-workflow-on-madison.md
Chapter slug: 21-shipit-pipelines-and-workflow-on-madison

---

## FIGURE 1 · A pipeline is a chain of contracts · Critical · systems diagram
The chapter's reframing thesis made literal: a left-to-right chain of nodes (source → API → transform → store) where every connecting edge is labeled as a contract — shape, cost, rate limit, terms of service — and stamped "owned by someone else, subject to change". Replaces the "pipeline as code" mental model with "pipeline as agreements". The single idea everything else serves.
- Spatial: horizontal node chain, four boxes connected by arrows; each arrow carries a small contract tag beneath it; a banner above reads "the pipeline runs while every agreement holds".
- RED: none — the contracts are peers; the figure establishes a frame, not a focal point.
- EXCLUSIONS: no Apollo numbers, no n8n node names, no degraded-mode taxonomy, no pipeline-type table.

## FIGURE 2 · Four kinds of data pipeline · Important · comparison table
The taxonomy that gives the chapter its vocabulary: ETL, Stream-processing, Workflow-automation, Inference — rows; columns for tools, throughput/frequency, typical use, and "used in Madison?". Locates the reader: workflow-automation + inference is what they will build. A reference figure, neutral by design.
- Spatial: four-row table, columns Type | Tools | Throughput | Typical use | In Madison?; the Workflow-automation and Inference rows marked as the two the reader uses.
- RED: none — four peer categories; comparison reference, fully greyscale.
- EXCLUSIONS: no Apollo case content, no contract-chain diagram, no n8n setup commands.

## FIGURE 3 · Apollo and the damage asymmetry · Critical · comparison panels
The brand lesson sharpened: damage flows downhill in a contract chain. Three actors — Reddit (upstream, diffuse spread across hundreds of millions), Apollo (downstream, concentrated, product-killing), Christian Selig (personal reputation, strengthened) — each a panel showing damage type and duration. The asymmetry is the point.
- Spatial: three vertical panels, large/medium/small or aligned equal, each with actor, damage type, and duration; a downward gradient/arrow motif suggesting damage flowing to the smallest party.
- RED: the Apollo (downstream) panel — the party that absorbs everything; the one the reader must register, since it is the reader's position. (Single red mark only.)
- EXCLUSIONS: no API pricing math beyond a single headline figure, no Twitter/Heroku detail (those are supporting text), no monopsony economics, no n8n content.

## FIGURE 4 · Three survival disciplines · Critical · structural schematic
The actionable core: document the contract, design a degraded mode, monitor the contract — three discipline cards, each with what it catches and how to implement it in n8n. The tooling is implementation; these three are the point. The reader's checklist.
- Spatial: three equal cards across, each headed by the discipline, a "catches:" line and an "in n8n:" line; a footer rule "tooling is implementation — these three are the point".
- RED: none — three peer disciplines applied together; neutral.
- EXCLUSIONS: no degraded-mode four-level taxonomy (that is Fig 5), no Apollo case, no specific code.

## FIGURE 5 · Degraded mode taxonomy — four levels · Important · hierarchy / progression
The four degraded modes in increasing order of robustness: informative failure → partial degradation → fallback source → graceful staleness. A ladder where each rung adds robustness, annotated with minimum implementation and when to use it. Answers "what does my product do when a contract fails?"
- Spatial: a vertical or stepped ladder, four rungs ascending by robustness; each rung labeled with mode name, one-line behavior, and "use when"; an axis cue showing increasing robustness upward.
- RED: none — four peer modes on a robustness scale; the ordering is the encoding, not emphasis.
- EXCLUSIONS: no three-disciplines duplication, no Apollo, no n8n node diagram.

## FIGURE 6 · Python script vs. n8n workflow — same pipeline, two representations · Critical · comparison panels
The chapter's strongest visual argument: on the left a monolithic Python script with interwoven dependency calls (contracts hidden inside the file); on the right an n8n workflow where every contract is a separately labeled, independently replaceable node. Same pipeline — one makes the contracts visible.
- Spatial: two panels side by side; left = a single block with tangled internal call lines; right = a clean node-and-edge graph with each external dependency as its own labeled, swappable node; a divider caption "one makes the contracts visible".
- RED: none — a neutral structural contrast; the right panel's clarity is shown by layout, not color.
- EXCLUSIONS: no actual code text beyond a few illustrative call labels, no Apollo, no degraded-mode taxonomy.

## FIGURE 7 · The four-node build pipeline · Critical · process flowchart
The hands-on artifact: Schedule Trigger → HTTP Request (RSS) → Code (Transform + Deduplicate) → Google Sheets (Write Row). Each node annotated with its documented contract — the schedule's contract with time, the RSS feed's risk:low, the dedup logic, the Sheet write. The minimal pipeline that does real work.
- Spatial: four boxes left-to-right with forward arrows; each box carries node name plus a one-line contract note beneath; tally line "four nodes, three contracts, one verifiable output".
- RED: none — a neutral build diagram; the four nodes are sequential peers.
- EXCLUSIONS: no Madison 40-node architecture (that is Fig 8), no error-handling code, no contract-chain abstraction.

## FIGURE 8 · Madison Intelligence Agent architecture · Important · systems diagram
The real workflow read for design decisions, not node count: six-hour schedule trigger → parallel ingestion branches (RSS, Google News API, Reddit) → dedup node (seen-URL store) → GPT-4o-mini scoring → dual output nodes (content sheet + run log). Each choice labeled with the failure mode it addresses.
- Spatial: schedule trigger at left; three parallel ingestion branches fanning then converging at the dedup node; single scoring node; two output nodes at right; small failure-mode annotations on the parallel branches and the run-log output.
- RED: none — an architecture reference; the parallel branches and run log are design features shown by structure, not emphasis.
- EXCLUSIONS: no four-node teaching build duplication, no monopsony economics, no contract-chain abstraction, no JSON.

---

## Video candidates

FIGURE a-pipeline-is-a-chain-of-contracts — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a multi-stage cascade: the sequential firing of each stage is the mechanism, and static display of the whole chain implies false simultaneity.
FIGURE four-kinds-of-data-pipeline — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE apollo-and-the-damage-asymmetry — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE three-survival-disciplines — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE degraded-mode-taxonomy-—-four-levels — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE python-script-vs.-n8n-workflow-—-same-pipeline,-two-represen — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE the-four-node-build-pipeline — Status: VIDEO CANDIDATE · Criterion: 2 · Reason: a sequence of causal steps: the student must witness each stage causing the next to understand the mechanism, not merely see the endpoints.
FIGURE madison-intelligence-agent-architecture — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** **a-pipeline-is-a-chain-of-contracts** — highest-priority candidate (criterion 2); if produced, **the-four-node-build-pipeline**, **degraded-mode-taxonomy-—-four-levels** could fold in as supporting beats rather than separate videos.
