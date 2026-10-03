# CAJAL Figure Report — 03 The AI Toolchain: Cowork, Codex & Madison

Source chapter: chapters/03-the-ai-toolchain-cowork-codex-madison.md
Chapter slug: 03-the-ai-toolchain-cowork-codex-madison

---

## FIGURE 1 · The four meanings of "agent" · Critical · matrix
The word "agent" carries four meanings in 2026. Rows: Meaning 1 (function + prompt, e.g. email summarizer), Meaning 2 (LLM + tools + loop, ReAct), Meaning 3 (autonomous over a horizon, Devin 2.0), Meaning 4 (specialized role in a system, Madison). Columns: informal label · example product · architectural implication · dominant failure mode.
- Spatial: 4-row × 4-column table, meaning number + label as row headers.
- RED: none — a neutral disambiguation reference; four peers.
- EXCLUSIONS: no ReAct trace detail, no orchestration patterns, no Madison layer list.

## FIGURE 2 · Madison's five roles plus orchestration · Critical · systems diagram
The five specialized layers — Intelligence, Content, Research, Experience, Performance — each a named role with input/output, coordinated through a central Orchestration layer. Each role box carries its one-line job. Performance feeds back as the closing loop.
- Spatial: five role boxes arranged around a central Orchestration node with labeled input/output arrows; a feedback arrow from Performance back into orchestration.
- RED: none — five peer roles; the architecture is the point, not one role.
- EXCLUSIONS: no mega-agent comparison (Fig 3), no ReAct internals, no tech-stack names.

## FIGURE 3 · Five roles vs. one mega-agent · Critical · comparison panels
The most consequential architectural choice. Left: five labeled, inspectable, named layers through an orchestration node — fault-locatable and saleable. Right: one opaque mega-agent box annotated with the three failures it produces — token costs balloon, failure modes blur, no product surfaces.
- Spatial: two panels divided by a hairline; left = small multi-box layered system; right = single dark opaque box with three failure annotations.
- RED: the opaque mega-agent box on the right — the architecture to avoid, the single focal contrast.
- EXCLUSIONS: no ReAct loop, no orchestration-pattern table, no archetype mapping.

## FIGURE 4 · Cursor vs. Devin: the control–delegation spectrum · Important · timeline / spectrum
A horizontal spectrum from "user in full control / augmentation" (left) to "system autonomous / delegation" (right). Cursor at left, Devin at right, Madison placed left-of-center and highlighted. Each endpoint annotated with brand position and recovery model. The architecture encodes a theory of risk.
- Spatial: horizontal axis with three positioned markers; brand-position labels above, recovery-model labels below.
- RED: the Madison marker (left-of-center) — where the chapter's framework lands, the thing to look at first.
- EXCLUSIONS: no capability benchmarks, no logos, no five-layer detail.

## FIGURE 5 · The ReAct loop (Intelligence Agent morning run) · Critical · cycle diagram
One complete think–act–observe cycle: THOUGHT → ACTION → OBSERVATION → back to THOUGHT, populated with the chapter's news-scoring trace (pull 870 articles → dedupe to 87 → score sentiment → write to sheet + fire dashboard). The feedback arrow from OBSERVATION back to THOUGHT highlighted.
- Spatial: four nodes in a loop with curved arrows; the return arrow OBSERVATION→THOUGHT emphasized; trace content annotated on each node.
- RED: the OBSERVATION→THOUGHT feedback arrow — the move that distinguishes a true agent loop from a plain prompt, the focal element.
- EXCLUSIONS: no failure-mode taxonomy here (covered in Fig 6), no other layers, no code.

## FIGURE 6 · Three ReAct failure modes and their fixes · Important · matrix
The loop's three distinct failures, each with a different design response: reasoning failure (does the wrong thing — add a guard, recoverable), action failure (tool errors or silently hallucinates a result — make it loud), observation failure (plausible-but-wrong result propagates — most dangerous; the Performance layer catches it). Columns: failure · what happens · design response.
- Spatial: 3-row matrix, failure name as row header, two description columns; severity rising top to bottom noted in a left margin tick.
- RED: the observation-failure row — the most dangerous category, the thing to look at first.
- EXCLUSIONS: no full ReAct trace, no orchestration patterns. Red here is emphasis (most dangerous to reason about), never a danger-color encoding on data.

## FIGURE 7 · Graph-based vs. conversation-based orchestration · Important · comparison panels
Two orchestration patterns. Left: graph-based (n8n / LangGraph) — predictable, every path defined, failures locatable, auditable. Right: conversation-based (AutoGen) — flexible, agents self-organize, but failures hard to isolate, huge debugging surface. Rows: failure locatability, novel-task handling, auditability, debugging surface, best fit.
- Spatial: two columns, five aligned property rows, divided by a hairline; a footer noting Madison chose graph (predictability).
- RED: none — a genuine trade-off between two peers; no single winner to spotlight.
- EXCLUSIONS: no ReAct internals, no tech-stack listing beyond the named tools.

## FIGURE 8 · Human-in-the-loop: place the gate where errors are expensive · Important · process flowchart
Risk-engineering placement of humans. A pipeline flow where most steps auto-execute, but consequential decisions (publish content, allocate budget, deploy a persona) pass through a human-gate before execution. Rule annotated: gate where a wrong answer is expensive and hard to reverse; automate the rest.
- Spatial: left-to-right pipeline with several auto steps and one human-gate bar on the high-cost branch before "execute."
- RED: the human-gate bar — the single non-delegable checkpoint, the focal element.
- EXCLUSIONS: no archetype-to-layer mapping, no orchestration table, no ReAct trace.

---

## Video candidates

FIGURE the-four-meanings-of-"agent" — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE madison's-five-roles-plus-orchestration — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE five-roles-vs.-one-mega-agent — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE cursor-vs.-devin:-the-control–delegation-spectrum — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE the-react-loop-(intelligence-agent-morning-run) — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE three-react-failure-modes-and-their-fixes — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE graph-based-vs.-conversation-based-orchestration — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE human-in-the-loop:-place-the-gate-where-errors-are-expensive — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
