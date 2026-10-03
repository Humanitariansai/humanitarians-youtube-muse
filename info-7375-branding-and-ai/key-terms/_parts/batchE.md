- **PRD (product requirements document)** :: ch 20 :: src -
  A one-page document that forces a team to decide what a product will and will not do before any code is written; it is a decision record and a contract with future-you, not an administrative wish list.

- **what vs. how** :: ch 20 :: src -
  The core rule of a PRD: the product team specifies what the product must do, while the engineering team owns how it is implemented. Smuggling implementation choices (a specific model, vendor, or template) into the PRD turns them into false constraints.

- **problem statement** :: ch 20 :: src -
  The PRD section naming a specific user, a specific task, its frequency, and what it costs them; a good one is testable against real users, while a vague or symptom-level version names no user, task, or consequence.

- **gap analysis** :: ch 20 :: src -
  The PRD section that names actual existing products and explains exactly what each one gets wrong for your specific user, revealing the unserved space the new tool will occupy.

- **MVP (minimum viable product)** :: ch 20 :: src -
  The smallest real version of a product that produces validated learning about customers with the least effort; "minimum" means smallest thing that tests the core bet, not least possible, and it must be a real product rather than a mock.

- **Build-Measure-Learn loop** :: ch 20 :: src -
  The cycle in which a team states a hypothesis, builds the smallest tool that tests it, measures actual user behavior, and learns whether the hypothesis held — only working when you decide in advance which assumption you are testing.

- **validated learning** :: ch 20 :: src -
  Knowledge that comes from what users actually did, not what they said they would do; usage data answers the question that survey-style questions cannot, because users reliably claim they will do things they will not.

- **MVP boundary** :: ch 20 :: src -
  The PRD section that lists both what is in scope for v1 and, explicitly, what is out; the "out" list is the disciplined part, since each item is something a reasonable person wanted and the boundary keeps the Build-Measure-Learn loop fast.

- **scope discipline** :: ch 20 :: src -
  The practice of refusing features that would compromise a product's core; it compounds, because each refusal preserves the coherence of the experience, and over time that coherence becomes the product's identity and brand (as in the Linear case).

- **$100,000 no** :: ch 20 :: src -
  The feature a real user will ask for, with a real argument and real money behind it, that you decline anyway because building it would damage the product's coherence; it is written first in the out-of-scope column and acknowledges a genuine cost.

- **scope creep** :: ch 20 :: src -
  The gradual accumulation of features added in the moment, each individually reasonable, that erodes a product's coherence; the PRD's out list with the $100,000 no at its head is the document you return to when someone proposes a new feature.

- **pipeline as a chain of contracts** :: ch 21 :: src -
  The reframing that a data pipeline is not primarily code but a chain of agreements — about data shape, cost, rate limits, and terms of service — each owned by someone else and subject to change without your consent; the pipeline survives only while every agreement holds.

- **four kinds of data pipeline** :: ch 21 :: src -
  The taxonomy of ETL (batch extract-transform-load), stream-processing (continuous near-real-time events), workflow-automation (visual node graphs gluing services), and inference (LLM-plus-retrieval); each differs in tooling, failure modes, and design discipline.

- **degraded mode** :: ch 21 :: src -
  The designed answer to what a product does when an external contract fails, in four levels of increasing robustness: informative failure, partial degradation, fallback source, and graceful staleness. Stale-but-labeled data usually beats no data.

- **damage flows downhill** :: ch 21 :: src -
  The asymmetry in a contract chain whereby an upstream platform's unilateral change spreads diffuse reputational damage across itself but inflicts concentrated, product-killing damage on the smallest, most dependent downstream tool — and users blame the tool, not the platform.

- **monitor the contracts** :: ch 21 :: src -
  The discipline of watching for contract-level events (rate-limit creep, pricing shifts, deprecated schema fields, updated terms) rather than only execution failures, since a workflow can run successfully while the underlying agreement silently degrades.

- **independently replaceable node** :: ch 21 :: src -
  The property a visual workflow tool like n8n gives a pipeline: each dependency is a node with defined input and output, so a broken or repriced service can be swapped without touching neighboring steps, making contracts explicit and isolable.

- **monopsony** :: ch 21 :: src -
  A market with one buyer facing many sellers who have no realistic alternative, giving the buyer power to set terms unilaterally; the structure of the Apollo-Reddit relationship, and one no amount of error handling can fully solve — only choosing contracts with genuine alternatives can.

- **four patterns of AI intelligence** :: ch 22 :: src -
  The four distinct ways AI sits in a workflow — single LLM call, chained calls, tool-using agent (ReAct), and multi-agent system — each with a different risk profile, maintenance cost, and user experience; treating them as interchangeable is the most common mistake.

- **autonomy/orchestration spectrum** :: ch 22 :: src -
  The internal spectrum of multi-agent systems from autonomous agents (each decides its own next step, maximally flexible and unpredictable) through conversational to orchestrated (a workflow decides which agent runs when, trading upfront design for debuggability and cost-predictability).

- **architecture as brand decision** :: ch 22 :: src -
  The claim that where AI decides versus where a human decides is not purely technical but determines what the product feels like — a transparent autonomous flow versus a competent orchestrated one — so the architectural choice must express the archetype, not its shadow.

- **compounding error** :: ch 22 :: src -
  The failure mode in which an autonomous agent's each step is conditioned on the last, so an early mistake propagates; errors compound geometrically, and a 10%-per-step error rate leaves a forty-step chain roughly 1.5% likely to be fully correct.

- **cost runaway** :: ch 22 :: src -
  The failure mode in which an autonomous agent without a hard step ceiling makes arbitrarily many paid model calls chasing a goal it cannot reach; prevented by a max step count, a per-execution cost ceiling, and a repeated-call circuit breaker.

- **anti-hallucination layer** :: ch 22 :: src -
  The constraints written into an agent's specification to surface uncertainty rather than fabricate, in three patterns from weakest to strongest: permission to abstain, structured output with null fields and notes, and per-claim confidence labeling; guards inside the prompt beat guards in a later validation step.

- **agent specification** :: ch 22 :: src -
  The contract between designer and LLM, defining an agent's role (which activates training-data associations), goal (the task plus constraints), backstory (the tie-breaker for edge cases), and tools (its boundary); an incomplete spec behaves well on easy inputs and strangely on hard ones.

- **local failure** :: ch 22 :: src -
  The architectural reward of orchestration: when a specialized agent that cannot delegate produces a wrong output, the failure traces to a specific agent, tool call, and input, rather than diffusing across an autonomous agent's entire execution trace.

- **interface layers (visual surface / interaction model / deployment surface / brand surface)** :: ch 23 :: src -
  The four distinct things "interface" refers to — the visual surface, the interaction model that sets the user's mental model, the deployment surface encountered before the UI loads, and the brand surface of error messages, empty states, and confidence — all of which must cohere with each other and the system.

- **confidence misalignment** :: ch 23 :: src -
  When an interface presents output as more certain than the system actually is, with no hedging or source attribution; the most common AI-interface failure, fixed not by making the system more accurate but by making the interface honest about its accuracy.

- **capability misalignment** :: ch 23 :: src -
  When an interface implies the tool can do things it cannot reliably do — a chat box implying general competence, a button implying it handles any document; a narrower capability claim is almost always more trustworthy than a broader one.

- **tone misalignment** :: ch 23 :: src -
  When an interface speaks in a voice the underlying system cannot maintain, such as a warm conversational UI paired with clipped templated outputs; the subtlest misalignment because it operates below explicit claims, fixed by matching interface copy to the system's actual output register.

- **alignment audit** :: ch 23 :: src -
  A two-column pre-deploy exercise listing every implicit promise the interface makes against whether the system can keep it reliably for real users; for every no or sometimes, you fix the interface — narrow the claim or add a qualifier — not the system.

- **minimum viable interface** :: ch 23 :: src -
  The smallest interface that accurately represents what the tool does and makes the right commitments without the wrong ones; it requires an input affordance matching the system's inputs, a visible processing state, and an output surface that represents confidence honestly.

- **Streamlit** :: ch 23 :: src -
  A Python-first web app framework that re-renders on each interaction, suited to tools where the user's job is to do work — configure inputs, run a process, inspect results; the right fit for orchestrated, structured pipelines.

- **Gradio** :: ch 23 :: src -
  A component-based Python library (part of Hugging Face) for interactive model demos where the user's job is to try the model — submit an input, see an output; deployed via Hugging Face Spaces and a mismatch for orchestrated systems that imply structured behavior.

- **empty state** :: ch 23 :: src -
  What the interface shows before the user has done anything; part of the brand surface, it should hold the archetype's voice rather than display a blank screen or generic placeholder.

- **error state** :: ch 23 :: src -
  What the interface says when something goes wrong; a brand-surface element that should be tested with actual failing inputs and should keep the archetype's voice rather than defaulting to generic or technical messages.

- **README as interface** :: ch 23 :: src -
  The last interface layer — the document a user reads to understand what they used or to decide whether to use it — with six elements in reading order: deployed URL first, then what it does, how to use it, its limits, an architecture diagram, and the tech stack.

- **cognitive friction** :: ch 97 :: src -
  The productive struggle of encountering something you cannot yet do or understand; it triggers the prediction error that fires dopamine and strengthens synapses, so the struggle is not the price of learning but its biological mechanism. Remove it and you remove the trigger.

- **phase gate** :: ch 97 :: src -
  The explicit, specified point at which AI processing stops and irreplaceable human work begins (or vice versa); not a vague commitment to use AI responsibly but a specification — AI handles X, human handles Y, the gate is at Z — sitting at the boundary between Tier 1 pattern work and Tiers 4-7 judgment.

- **Irreducibly Human taxonomy** :: ch 97 :: src -
  The seven-tier ladder of cognitive capacities ranking where machines win and where they cannot reliably operate: Tier 1 pattern and association (machines win) up through metacognitive, causal, collective, and existential tiers (Tiers 4-7) where human cognition is required.

- **extraneous vs. germane load** :: ch 97 :: src -
  The distinction between cognitive work that merely impedes learning without constituting it (extraneous — formatting, organizing, templating, safely delegable to AI) and the work that is the learning itself (germane — synthesizing evidence, constructing an argument, forming a judgment).

- **capability-building vs. capability-borrowing** :: ch 97 :: src -
  The difference between AI uses that develop a student's own Tier 4-7 capacity and uses that merely borrow the machine's capability; borrowing produces the fluent feeling of mastery without the neural events that constitute it (as in the Bastani and Kosmyna findings).

- **plausibility auditing** :: ch 97 :: src -
  The Tier 4 capacity to ask whether an output makes sense given what you actually know about how a domain works; AI generates confident nonsense, and only a human with genuine domain knowledge — which AI cannot shortcut — reliably catches it.

- **the identification layer** :: ch 97 :: src -
  The irreducibly human part of causal analysis — variable selection, edge orientation, and conditioning decisions — that must be performed before AI is used for estimation, because data and pattern-matching cannot choose among causal structures that fit the same statistics (Markov equivalence).

- **AI+1** :: ch 97 :: src -
  The argument and curriculum that the wage premium goes to AI-fluent domain experts who stay in their domain and add AI superpowers, rather than career-switchers who become generic technologists; it teaches both the domain-specific Tier 4-7 work AI cannot do and the Tier 1 workflows that boost productivity.

- **the fluency trap** :: ch 97 :: src -
  The illusion that fluent AI output is finished and authored work; the smoothness is real but the craft (or learning, or judgment) is not, and the absence of human cognitive engagement is invisible on the surface — which is why systems like Brutalist and Boondoggling make it visible.

- **boondoggling** :: ch 97 :: src -
  The practice of conducting Claude through a build — assigning each task to the right labor, sequencing by dependency, and writing explicit handoff conditions between steps; programming as conducting, where the human's job is not to type less but to decide more precisely.

- **Boondoggle Score** :: ch 97 :: src -
  A conductor's score with two parallel parts: the Minion Part (exact copy-pasteable prompts for Claude in dependency order) and the Gru Part (the human's supervisory actions, each labeled with a capacity like plausibility auditing or problem formulation), joined by testable handoff conditions.
