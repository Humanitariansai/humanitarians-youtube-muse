# Branding and AI — Glossary

> 209 terms, A–Z. Definitions are in the book's voice; citations link a sourced reference where one exists in the project's facts slice. Chapter tags show where each term is used.
> Generated from chapters' `## Key Terms` sections plus proposed terms for chapters without one. Regenerate via `SCRIPTS/glossary-extract.mjs` → batch authoring → `SCRIPTS/glossary-merge.mjs`.

---

## #

**$100,000 no** *(ch 20)*  
The feature a real user will ask for, with a real argument and real money behind it, that you decline anyway because building it would damage the product's coherence; it is written first in the out-of-scope column and acknowledges a genuine cost.

**10/20/30 rule** *(ch 19)*  
Guy Kawasaki's pitch constraint of ten slides, twenty minutes, and a thirty-point font minimum; the font floor is the underestimated part, because it forces editing — content that won't fit at 30-point belongs in the speaking script, not on the slide.

## A

**Aaker dimensions** *(ch 2)*  
David Aaker's four levers of brand equity — awareness, perceived quality, associations, and loyalty — that a manager can actually pull; the diagnostic move is to map a brand on all four and intervene on the weakest, where the lift is greatest.

**agent specification** *(ch 22)*  
The contract between designer and LLM, defining an agent's role (which activates training-data associations), goal (the task plus constraints), backstory (the tie-breaker for edge cases), and tools (its boundary); an incomplete spec behaves well on easy inputs and strangely on hard ones.

**AI ethics claims** *(ch 15)*  
Product-marketing assertions like "responsible," "explainable," or "bias-free" AI that are appealing but almost always unsubstantiated; the chapter requires each to be backed by product-specific evidence (an explanation mechanism, a published bias audit with named methodology, a documented human-in-the-loop architecture) rather than fluent language.

**AI+1** *(ch 0, 1, 2, 3, 4, 97)*  
The division of labor the whole book runs on: the AI agent drafts (reformatting, drafting, pattern-spotting) while you — the +1 — own the accountable judgment, accepting, rejecting, or revising every draft and treating any generated persona, metric, or citation as something that still needs an evidence check.

**aided/unaided awareness** *(ch 13)*  
Two measures of whether an audience knows a brand exists: unaided ("what brands can you name?") is the demanding test of mental salience, while aided ("have you heard of X?") is softer and hits a ceiling, making unaided the more meaningful competitive measure.

**alignment audit** *(ch 23)*  
A two-column pre-deploy exercise listing every implicit promise the interface makes against whether the system can keep it reliably for real users; for every no or sometimes, you fix the interface — narrow the claim or add a qualifier — not the system.

**anti-hallucination layer** *(ch 22)*  
The constraints written into an agent's specification to surface uncertainty rather than fabricate, in three patterns from weakest to strongest: permission to abstain, structured output with null fields and notes, and per-claim confidence labeling; guards inside the prompt beat guards in a later validation step.

**anti-references** *(ch 9)*  
Two to four examples of visual work to avoid, each annotated with why it fails the brief; often more useful than positive references because they make the negative space of the design explicit.

**archetypal foundation** *(ch 9)*  
The principle that visual choices must follow from the brand's archetype rather than personal taste, so the components converge on one impression automatically; its absence produces the Pepsi outcome, where designers reach for borrowed authority because nothing strategic anchors the work.

**archetype shadow** *(ch 1, 5)*  
The failure mode built into each archetype — the archetype's own strength taken too far, like the Creator's perfectionism that never ships or the Sage's analysis without action; once you name your archetype, the shadow tells you which failure to watch for.

**archetype–narrative match** *(ch 10)*  
The requirement that a brand's story shape carry the same commitments as its archetype; each archetype has story shapes native to it and shapes that read as imposture when borrowed.

**archetype–narrative mismatch** *(ch 10)*  
The failure that occurs when a brand tells a story shape that belongs to a different archetype, which audiences feel as falseness through one of three pathways: wrong emotional register, an archetype-inconsistent role for the brand, or borrowed cultural content the brand has no claim to.

**architecture as a brand decision** *(ch 3)*  
The chapter's integrating thesis, after McLuhan: how you decompose an AI product into parts quietly decides what customers can see, name, trust, and buy — so engineering seams create brand positions long before any marketing copy is written.

**architecture as brand decision** *(ch 22)*  
The claim that where AI decides versus where a human decides is not purely technical but determines what the product feels like — a transparent autonomous flow versus a competent orchestrated one — so the architectural choice must express the archetype, not its shadow.

**autonomy/orchestration spectrum** *(ch 22)*  
The internal spectrum of multi-agent systems from autonomous agents (each decides its own next step, maximally flexible and unpredictable) through conversational to orchestrated (a workflow decides which agent runs when, trading upfront design for debuggability and cost-predictability).

## B

**backlash asymmetry** *(ch 15)*  
The dynamic by which a values claim creates a behavioral expectation, so that later inconsistent behavior is judged as hypocrisy against the standard the brand set — making the trust damage greater than if no claim had been made. Purpose-washing therefore erodes trust faster than silence.

**bases of segmentation** *(ch 4)*  
The five different cuts you can take through one population — demographic, geographic, behavioral, psychographic, and needs-based — where demographics is where most people wrongly stop and a shared need is what actually defines a true segment.

**Boondoggle Score** *(ch 97)*  
A conductor's score with two parallel parts: the Minion Part (exact copy-pasteable prompts for Claude in dependency order) and the Gru Part (the human's supervisory actions, each labeled with a capacity like plausibility auditing or problem formulation), joined by testable handoff conditions.

**boondoggling** *(ch 97)*  
The practice of conducting Claude through a build — assigning each task to the right labor, sequencing by dependency, and writing explicit handoff conditions between steps; programming as conducting, where the human's job is not to type less but to decide more precisely.

**brand archetype** *(ch 5)*  
One of twelve recurring brand identities, formalized by Mark and Pearson, that organizes who a brand is and lets customers recognize it below the level of conscious articulation; committing to one turns vague brand questions into decidable ones.

**brand architecture** *(ch 7)*  
The system specifying how a company's brands relate to each other, how equity flows among them, what names appear on what offerings, and how risk is contained when something goes wrong — designed deliberately or inherited by accident.  
  *Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/Brand_architecture)*

**brand constants vs. variables** *(ch 11)*  
The distinction that enables consistency without uniformity: constants (archetype, voice, visual identity) hold across every channel, while variables (length, formality, personality density) flex to fit the medium.

**brand equity** *(ch 2)*  
The worth of a brand in and of itself — the accumulated set of expectations living in customers' minds that changes their behavior and can be measured in money, producing future value through price premium, retention, and forgiveness.  
  *Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/Brand_equity)*

**brand experience** *(ch 11)*  
The sum of every contact a customer has with a brand across touchpoints; because customers never read the strategy, the experience effectively is the brand, and a brilliant positioning that contradicts the support experience loses to the support experience.

**brand extension (line / category)** *(ch 7)*  
Deploying existing brand equity to enter new territory — a line extension adds a variant within the same category (Tide Pods), a category extension crosses into a new one (Apple into phones); the leverage is real and so is the dilution risk.  
  *Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/Brand_extension)*

**brand governance** *(ch 14)*  
The daily operational discipline of keeping a brand coherent as it scales and deciding when to deliberately change it; a brand book on a shelf is not governance — governance is what happens when someone needs an on-brand decision in the moment.

**brand identity vs. image** *(ch 2)*  
Identity is what the company projects (the sender's side); image is what actually lands in the receiver's mind; brand work is the management of the gap between them, and equity leaks wherever the two diverge.

**brand metrics vs. performance metrics** *(ch 13)*  
The split between measures of the asset itself (awareness, consideration, preference, association, price premium), which move slowly, and measures of business outcomes (conversion, CAC, ROAS, retention, LTV), which move fast; the error that kills measurement programs is treating them as interchangeable.

**Brand Relationship Spectrum** *(ch 7)*  
Aaker and Joachimsthaler's map of architectural options running from one master brand to many independent brands, with shared equity and efficiency rising toward one pole and risk containment rising toward the other.  
  *Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/Brand_relationship)*

**brand stewardship** *(ch 14)*  
The function of owning the brand system: at small scale, ensuring decisions reference the system rather than being made in isolation; at large scale, shifting from reviewing every artifact to designing the system so the common case is easy and the wrong case requires effort.

**brand tracking study** *(ch 13)*  
A repeated survey — same questions, same representative population, regular intervals — designed to show how equity accumulates or leaks over time; its value is the trend line, not any single data point.

**brand-lift study** *(ch 13)*  
The cleanest design for measuring campaign effect: split the audience into a matched exposed group and control group, show the campaign only to the exposed group, and compare brand metrics — a randomized-controlled-trial logic applied to brand measurement.

**branded house** *(ch 7)*  
An architecture where one master brand stretches across every offering, so marketing in one product builds equity for all (Apple, FedEx); the trade-off is shared exposure, since any crisis propagates through the whole portfolio.

**Build-Measure-Learn loop** *(ch 20)*  
The cycle in which a team states a hypothesis, builds the smallest tool that tests it, measures actual user behavior, and learns whether the hypothesis held — only working when you decide in advance which assumption you are testing.

**building for after** *(ch 19)*  
The post-launch discipline of installing compounding habits while momentum is live: refreshing the portfolio quarterly, publishing on a sustainable cadence, and building a few real relationships rather than a large network. Cadence beats quality at the margin — consistent monthly output compounds more than brilliant output published once.

## C

**cadence over volume** *(ch 10)*  
The content-production principle that a sustainable publishing rhythm beats high output; a few well-told pieces compound into an audience's model of who you are, while an unsustainable volume burns out and abandons the strategy.

**campaign brief** *(ch 12)*  
A one-page document that turns strategy into a coordinated campaign by answering six questions in sequence — objective, audience, message, channel mix, budget, measurement — each constraining the next; a brief that runs to three pages has not yet made its decisions.

**cannibalization** *(ch 7)*  
When offerings in a portfolio compete for the same audience and dilute one another's equity; redundancy is expensive even when each individual offering is good, which is why every brand must carry distinct, non-duplicated associations.

**capability misalignment** *(ch 23)*  
When an interface implies the tool can do things it cannot reliably do — a chat box implying general competence, a button implying it handles any document; a narrower capability claim is almost always more trustworthy than a broader one.

**capability-building vs. capability-borrowing** *(ch 97)*  
The difference between AI uses that develop a student's own Tier 4-7 capacity and uses that merely borrow the machine's capability; borrowing produces the fluent feeling of mastery without the neural events that constitute it (as in the Bastani and Kosmyna findings).

**Caregiver** *(ch 5)*  
The archetype organized around service, compassion, and protection — here to nurture those who cannot protect themselves; its shadow is martyrdom, the tone of "we sacrifice for you, and you should notice."

**category-error drift** *(ch 5)*  
When a brand abandons its archetype to become a different one entirely, erasing the recognition cues its audience depended on; Tropicana's 2009 repackaging is the canonical case.

**CBBE pyramid** *(ch 2)*  
Keller's customer-based brand equity model as a theory of accumulation across four levels — salience, then performance and imagery, then judgments and feelings, then resonance at the apex — where awareness is the floor, not the goal, and compound equity is built only by climbing to resonance.

**centerpiece case study (four functions)** *(ch 18)*  
A case study that performs four jobs at once — frame the problem specifically, show the technical work with verifiable metrics, connect the work to brand and archetype, and be honest about limits. Specific numbers and admitted limitations are Feynman moves: they build trust in the claims you do make.

**claim-proof map** *(ch 15)*  
An operational table that pairs every ethics or sustainability claim with the specific evidence required, the evidence actually held, and a status of HAVE, NEED, or CANNOT SUBSTANTIATE. It functions as both a brand-integrity tool and a greenwashing-compliance record; "cannot substantiate" signals that the claim should be cut, not that the proof should be manufactured.

**clearance search** *(ch 8)*  
The cost-ordered pre-screening sequence run before committing to a name — register search with phonetic and visual variants, domain check, common-law web search, and the non-optional step of consulting counsel; literacy in it is not the same as clearance.

**co-branding** *(ch 7)*  
Pairing two independent consumer brands so the combination signals a joint value proposition neither could communicate alone (Nike and Apple); the symmetric risk is that you inherit the partner's reputation and crises.  
  *Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/Co-branding)*

**cognitive friction** *(ch 97)*  
The productive struggle of encountering something you cannot yet do or understand; it triggers the prediction error that fires dopamine and strengthens synapses, so the struggle is not the price of learning but its biological mechanism. Remove it and you remove the trigger.

**coherence audit** *(ch 18)*  
The pre-launch check of sending portfolio, LinkedIn, and résumé to someone who hasn't seen them and asking whether they feel like the same person from three angles. The goal is not identical surfaces but three angles on one person — matching positioning sentence, legible archetype, same featured projects, consistent voice.

**coherence check** *(ch 6)*  
Examining every adjacent pair of brand components for contradiction before finalizing a strategy; an internally inconsistent document does not constrain decisions, it merely defers the conflict to a worse moment under pressure.

**coherence principle** *(ch 19)*  
The standard, drawn from the Airbnb pitch deck, that a professional presentation must make one argument well rather than ten separate pleas — every surface answering the same question, carried by specific load-bearing numbers and weight on the people involved. It applies beyond the deck to the LinkedIn headline, résumé bullets, case studies, and follow-up email.

**company registration** *(ch 8)*  
An entity name filed with a state, meaning only that the state did not already have it on file; it is not a trademark and protects the name neither federally nor against a same-state company in a different category.

**compounding error** *(ch 22)*  
The failure mode in which an autonomous agent's each step is conditioned on the last, so an early mistake propagates; errors compound geometrically, and a 10%-per-step error rate leaves a forty-step chain roughly 1.5% likely to be fully correct.

**confidence misalignment** *(ch 23)*  
When an interface presents output as more certain than the system actually is, with no hedging or source attribution; the most common AI-interface failure, fixed not by making the system more accurate but by making the interface honest about its accuracy.

**consideration** *(ch 13)*  
A purchase-funnel metric measuring openness — "would you try this brand?" — a lower bar than preference; high consideration with low preference reveals that something in the evaluation process is failing.

**core vs. expression** *(ch 17)*  
The glocalization rule for what is fixed and what flexes: the core (purpose, archetype, fundamental promise) stays global, the expression (language, imagery, claims, tone, channels) localizes. Holding the expression too rigidly reads as tone-deaf; flexing the core makes the brand incoherent — a different brand in every market.

**cost runaway** *(ch 22)*  
The failure mode in which an autonomous agent without a hard step ceiling makes arbitrarily many paid model calls chasing a goal it cannot reach; prevented by a max step count, a per-execution cost ceiling, and a repeated-call circuit breaker.

**creative brief** *(ch 9)*  
The dense one-to-two-page artifact that translates brand strategy into design constraints before any visual work begins, in eight sections from strategy summary to deliverables; once written, every later design decision can be checked against it.

**Creative Engineer** *(ch 0, 1)*  
An engineer who has noticed that the old costly signals have shifted and invested accordingly — investing in Ideate, Brand, and Ship on top of a necessary Build foundation rather than treating a working repository as proof enough.

**Creator** *(ch 5)*  
The archetype organized around imagination, expression, and originality — making something that was not there before; its shadow is perfectionism, becoming so invested in craft that it forgets the audience.

**crisis types (victim / accidental / preventable)** *(ch 16)*  
SCCT's three clusters by responsibility attribution: victim crises (external harm, low attribution, deny/bolster), accidental crises (unintended harm, moderate attribution, diminish), and preventable crises (known-and-ignored risk, high attribution, rebuild). The triage decision about which type applies determines every subsequent response choice.

**cross-cultural verification** *(ch 17)*  
The non-optional step of testing brand elements — name, tagline, colors, imagery, humor — with embedded native speakers of the target market rather than dictionaries, multilingual colleagues, or a confident model. A model can produce a culturally plausible transcreation but cannot feel whether it lands; that judgment lives in communities.

**CSR, ESG, and B Corp** *(ch 15)*  
Three instruments for making purpose legible to outsiders, ordered by increasing third-party rigor: voluntary unverified CSR programs, standardized but unharmonized ESG disclosure, and B Lab's audited B Corp certification. Each is a signal that invites scrutiny rather than a credential that resolves it — reporting a metric is not the same as performing well on it.

**cultural tension** *(ch 4)*  
Douglas Holt's added layer: the strongest brands resolve a contradiction or anxiety in the broader culture that a group feels but no brand is addressing, turning positioning from "we do X" into "we do X for people who feel Y about the world."

**customer journey map** *(ch 11)*  
A tool that lays out every contact from awareness through advocacy, asking at each stage what the touchpoint is, the brand's job there, the customer's emotional state, and whether the touchpoint delivers — making seams between adjacent touchpoints visible.

**customer-as-hero (StoryBrand)** *(ch 10)*  
Donald Miller's framing in which the customer is always the hero of a brand story and the brand is the guide — Yoda to the customer's Luke — providing a plan and tools while the customer faces the problem and is transformed.

## D

**DAM (digital asset management)** *(ch 14)*  
A single searchable source of truth for brand assets, organized so anyone can find the current logo, color codes, and voice examples in under a minute; if assets are not findable that fast, the guidelines system will not be used.

**damage flows downhill** *(ch 21)*  
The asymmetry in a contract chain whereby an upstream platform's unilateral change spreads diffuse reputational damage across itself but inflicts concentrated, product-killing damage on the smallest, most dependent downstream tool — and users blame the tool, not the platform.

**decision record** *(ch 14)*  
Documented resolutions of edge cases so that when the same governance question recurs there is an answer rather than another discussion, preventing the same conversation from happening twelve times.

**degraded mode** *(ch 21)*  
The designed answer to what a product does when an external contract fails, in four levels of increasing robustness: informative failure, partial degradation, fallback source, and graceful staleness. Stale-but-labeled data usually beats no data.

**design system** *(ch 14)*  
The component libraries, templates, and documented patterns that make it easier to stay on-brand than to go off-brand, and the layer that lets consistency scale past the point where any individual can review every artifact.

**domain** *(ch 8)*  
A rented web address that grants no trademark rights whatsoever; the domain and trademark systems are legally separate, so owning one says nothing about the other — "I bought the domain, so I own the name" is the most dangerous version of this error.

**drift vs. intentional variation** *(ch 14)*  
Two departures from the documented system that look identical but differ in meaning: intentional variation is an authorized flex, drift is an unauthorized erosion; distinguishing them requires knowing who authorized the departure and whether it appears once or as a repeated pattern.

## E

**empty state** *(ch 23)*  
What the interface shows before the user has done anything; part of the brand surface, it should hold the archetype's voice rather than display a blank screen or generic placeholder.

**endorsed brand** *(ch 7)*  
The reverse orientation, where the child brand leads with its own identity and the parent appears as a small credibility signal in a "by" or "from" construction (Courtyard by Marriott); useful when the offering must differ from the parent yet still borrow its trust.

**equity migration** *(ch 14)*  
The set of practices that carry equity across a brand change rather than abandoning it — a transition period with both marks, an endorsed "formerly X" model, clear communication, and deliberate preservation of the recognition cues carrying the most equity.

**equity stranding** *(ch 14)*  
The central migration risk: because equity lives in customers' mental models, a change that abandons recognition cues leaves customers nothing to anchor to, so some fraction will not rebuild their model and will stop looking.

**error state** *(ch 23)*  
What the interface says when something goes wrong; a brand-surface element that should be tested with actual failing inputs and should keep the archetype's voice rather than defaulting to generic or technical messages.

**escalation path** *(ch 16)*  
The pre-defined chain naming who decides, who speaks, and who must approve a public statement before it goes out — including whether legal review is required — so the live moment under pressure becomes execution rather than improvisation.

**Everyman** *(ch 5)*  
The archetype organized around belonging and equality, telling the customer they fit here exactly as they are; its shadow is conformity, becoming so broad it stands for nothing.

**experience economy** *(ch 11)*  
Pine and Gilmore's argument that market value progresses from commodities to goods to services to experiences, with the differentiated premium layer shifting to the experience staged around an otherwise identical product.

**Explorer** *(ch 5)*  
The archetype organized around freedom, discovery, and autonomy, saying the world is worth seeking out; its shadow is aimlessness, losing coherence and standing for nothing in particular.

**extraneous vs. germane load** *(ch 97)*  
The distinction between cognitive work that merely impedes learning without constituting it (extraneous — formatting, organizing, templating, safely delegable to AI) and the work that is the learning itself (germane — synthesizing evidence, constructing an argument, forming a judgment).

## F

**Farris test** *(ch 13)*  
Paul Farris's screen for any proposed metric: if this number changed tomorrow, would you do anything differently? If the answer is no, the metric is vanity and should be cut from the plan.

**flood and filter** *(ch 12)*  
The chapter's framing that as AI drives the cost of competent content toward zero, the scarce and rising-value capability becomes editorial judgment — deciding what is worth saying, verifying it is true, and making it sound like you rather than brand-speak.

**forcing function** *(ch 5)*  
A committed archetype acting as a constraint that makes every downstream brand decision — copy, color, sponsorship, tone — checkable and decidable rather than arbitrary; not an asset like a logo but the thing that makes all the other assets cohere.

**four kinds of data pipeline** *(ch 21)*  
The taxonomy of ETL (batch extract-transform-load), stream-processing (continuous near-real-time events), workflow-automation (visual node graphs gluing services), and inference (LLM-plus-retrieval); each differs in tooling, failure modes, and design discipline.

**four meanings of "agent"** *(ch 3)*  
The four distinct things the word "agent" means in 2026 — a function with a prompt, an LLM with tools and a loop (ReAct), an autonomous system over a sustained horizon (Devin), and a specialized role in a larger pipeline (Madison) — each implying a different architecture, failure mode, and human relationship.

**four patterns of AI intelligence** *(ch 22)*  
The four distinct ways AI sits in a workflow — single LLM call, chained calls, tool-using agent (ReAct), and multi-agent system — each with a different risk profile, maintenance cost, and user experience; treating them as interchangeable is the most common mistake.

**four-verb framework (Ideate / Build / Brand / Ship)** *(ch 19)*  
The book's organizing loop applied to the learner's own work: Ideate (problem and audience), Build (pipeline, AI layer, interface), Brand (strategy, identity, content), and Ship (portfolio, tool, presentation, launch). The final presentation is the first Ship of the rest of a career — the costly separating signals AI tooling did not make cheap.

**frequency** *(ch 12)*  
The number of times each person sees a message; the right optimization when the goal is to make people act on something they have probably already heard of, since a single impression rarely changes behavior.

## G

**gap analysis** *(ch 20)*  
The PRD section that names actual existing products and explains exactly what each one gets wrong for your specific user, revealing the unserved space the new tool will occupy.

**glocalization** *(ch 17)*  
A global strategy with local execution: the brand's core — purpose, archetype, fundamental promise — holds everywhere while the expression (language, imagery, claims, channels, cultural references) adapts per market. McDonald's is the worked case — the Golden Arches are global, the local menu is not.

**goodwill** *(ch 2)*  
The accountant's name for the slice of an acquisition price that buys no physical asset — in the Cadbury deal, the value of the word itself and what it does inside millions of buyers' heads at the moment of purchase.

**Gradio** *(ch 23)*  
A component-based Python library (part of Hugging Face) for interactive model demos where the user's job is to try the model — submit an input, see an output; deployed via Hugging Face Spaces and a mismatch for orchestrated systems that imply structured behavior.

**graph-based vs. conversation-based orchestration** *(ch 3)*  
The two dominant ways to wire agents together: graph-based (n8n, LangGraph) defines every path in advance for predictability and locatable failures, while conversation-based (AutoGen) lets agents self-organize for flexibility at the cost of harder debugging; Madison chose graph for trustworthy daily execution.

**greenwashing regulation (EU ECGT / FTC Green Guides)** *(ch 15)*  
The 2026 legal regime turning loose environmental claims into legal exposure: the EU's Empowering Consumers for the Green Transition Directive bans generic green claims without substantiation and offset-based "climate neutral" claims, while the US FTC Green Guides treat claims made contrary to them as presumptively deceptive under Section 5.

## H

**Hero** *(ch 5)*  
The archetype organized around courage and mastery, built on the idea that the customer can become more through effort and the brand is the instrument of that becoming; its shadow is arrogance and contempt for those who struggle.

**Hero's Journey (monomyth)** *(ch 10)*  
Joseph Campbell's recurring story architecture in which a hero leaves an ordinary world, crosses a threshold, survives an ordeal, and returns transformed with a boon; the simplified three-act Departure–Initiation–Return shape supplies the deep structure beneath a brand story.

**Hofstede cultural dimensions** *(ch 17)*  
Geert Hofstede's framework describing national cultures along dimensions such as power distance and individualism vs. collectivism, used as a lens for why the same brand message reads differently across cultures. The crucial caveat: these are population-level tendencies, not scripts for individuals — using them to stereotype produces the very error they should help avoid.

**holding statement** *(ch 16)*  
A brief, pre-drafted message that signals the organization is aware of an emerging situation and taking it seriously without committing to an account of cause, responsibility, or resolution. It resolves the speed-versus-accuracy tension by being fast to post yet committing to nothing that cannot be sustained.

**house of brands** *(ch 7)*  
An architecture where a portfolio of independent brands each carry their own identity and the parent stays invisible (P&G, Unilever), isolating risk and enabling precise targeting at the cost of building every brand essentially from scratch.

**human-in-the-loop** *(ch 3)*  
Placing a human gate not as a philosophical stance on autonomy but as risk engineering: find the decisions where a wrong answer is expensive and hard to reverse — publishing content, allocating budget, deploying a persona — gate those, and automate everything else.

## I

**Image Repair Theory** *(ch 16)*  
William Benoit's mapping of the full palette of crisis responses — denial, evasion of responsibility, reducing offensiveness, corrective action, and mortification — none of which is equally available in every situation; in a preventable crisis, denial only compounds the damage.

**independently replaceable node** *(ch 21)*  
The property a visual workflow tool like n8n gives a pipeline: each dependency is a node with defined input and output, so a broken or repriced service can be swapped without touching neighboring steps, making contracts explicit and isolable.

**individualism vs. collectivism** *(ch 17)*  
The Hofstede dimension with the most direct messaging implications: campaigns built on personal achievement and self-expression resonate in high-individualism markets, while messaging built on belonging, family, and shared identity does more work in high-collectivism markets.

**ingredient branding** *(ch 7)*  
Making a component brand visible inside a finished product (Intel Inside, Gore-Tex); it works when the component carries associations the finished-product maker cannot independently claim and buyers know what the component does.

**Innocent** *(ch 5)*  
The archetype organized around simplicity, purity, and optimism, promising that the world is good and the product reflects it; its shadow is denial — refusing to acknowledge bad news and sounding out of touch.

**intangible asset** *(ch 2)*  
What a brand is in accounting and strategic terms — a thing that produces future cash flow without physical form; on a large acquisition it routinely dwarfs the factories and machinery on the balance sheet.

**integrated marketing communications (IMC)** *(ch 12)*  
Don Schultz's discipline of saying one synchronized thing across every channel: the specific expression adapts to the medium, but the underlying claim, archetype, and voice stay identical, with the campaign as the unit that enforces it.

**interface layers (visual surface / interaction model / deployment surface / brand surface)** *(ch 23)*  
The four distinct things "interface" refers to — the visual surface, the interaction model that sets the user's mental model, the deployment surface encountered before the UI loads, and the brand surface of error messages, empty states, and confidence — all of which must cohere with each other and the system.

**Irreducibly Human taxonomy** *(ch 97)*  
The seven-tier ladder of cognitive capacities ranking where machines win and where they cannot reliably operate: Tier 1 pattern and association (machines win) up through metacognitive, causal, collective, and existential tiers (Tiers 4-7) where human cognition is required.

**ISO 10668** *(ch 2)*  
The formal standard for brand valuation that Interbrand, Kantar, and Brand Finance all reference; it exists precisely because the competing valuation methods disagree by design and need an arbitration standard.

## J

**Jester** *(ch 5)*  
The archetype organized around fun, lightness, and irreverence, insisting this is supposed to be enjoyable; its shadow is cruelty, making jokes at the wrong person's expense.

**jobs-to-be-done** *(ch 4)*  
Christensen's reframing that customers do not buy products, they hire them to do a job; the milkshake bought to make a commute tolerable shows that the real job cuts across demographics and predicts purchase better than who the buyer is on paper.

## L

**likelihood of confusion** *(ch 8)*  
The core infringement test — whether a reasonable consumer would be confused about the source of goods when encountering two marks — weighing similarity, relatedness, channels, buyer sophistication, and mark strength, so an exact-match search is never the same as being cleared.

**living guidelines** *(ch 14)*  
A system rather than a document — a set of tools and practices (DAM, design system, decision record) available in the form people need at the moment they decide, so that staying on-brand is easier than going off-brand.

**local failure** *(ch 22)*  
The architectural reward of orchestration: when a specialized agent that cannot delegate produces a wrong output, the failure traces to a specific agent, tool call, and input, rather than diffusing across an autonomous agent's entire execution trace.

**Lover** *(ch 5)*  
The archetype organized around intimacy, beauty, and connection, saying life is better when it is felt; its shadow is obsession — becoming suffocating or merely superficial.

## M

**Madison framework** *(ch 0, 3)*  
The open-source, agent-based marketing-intelligence system the book ships and teaches with: five specialized agent roles (Intelligence, Content, Research, Experience, Performance) plus an orchestration layer, used as the worked example for reading AI architecture as a brand decision.

**Magician** *(ch 5)*  
The archetype organized around transformation and vision — promising to change what you thought was fixed; its shadow is manipulation, overpromising while hiding the mechanism.

**Mark/Pearson system** *(ch 1, 5)*  
The twelve-archetype framework set out in *The Hero and the Outlaw*, borrowing Jung's archetype names to build a brand-strategy taxonomy; it is concrete enough to teach and general enough to apply across industries, but it is a taxonomy, not the only one.

**marketing-mix modeling** *(ch 13)*  
An attribution approach using aggregate time-series data (sales against media spend, pricing, promotions, economic and competitor signals) to estimate each input's contribution; it captures unobserved brand touchpoints that multi-touch misses, at the cost of granularity.

**mega-agent** *(ch 3)*  
The single do-everything model offered as the alternative to a layered architecture; in production it breaks three ways — token costs balloon from re-reading context, failure modes blur so faults can't be located, and the product has no nameable surfaces to sell, version, or trust.

**minimum viable interface** *(ch 23)*  
The smallest interface that accurately represents what the tool does and makes the right commitments without the wrong ones; it requires an input affordance matching the system's inputs, a visible processing state, and an output surface that represents confidence honestly.

**moments of truth (ZMOT / FMOT / SMOT)** *(ch 11)*  
The high-weight touchpoints that disproportionately shape a customer's model of the brand: the Zero Moment (pre-purchase research), First Moment (the shelf decision), and Second Moment (whether use delivers on the promise) — plus software equivalents like first run and renewal.

**monitor the contracts** *(ch 21)*  
The discipline of watching for contract-level events (rate-limit creep, pricing shifts, deprecated schema fields, updated terms) rather than only execution failures, since a workflow can run successfully while the underlying agreement silently degrades.

**monopsony** *(ch 21)*  
A market with one buyer facing many sellers who have no realistic alternative, giving the buyer power to set terms unilaterally; the structure of the Apollo-Reddit relationship, and one no amount of error handling can fully solve — only choosing contracts with genuine alternatives can.

**mortification** *(ch 16)*  
The crisis response of full acknowledgment of responsibility plus sincere apology, which — combined with genuine corrective action — is the only path that gives a brand a reasonable chance of recovery from a high-responsibility, preventable crisis.

**multi-touch attribution** *(ch 13)*  
A family of models (last-click, first-click, linear, time-decay, data-driven) that distribute conversion credit across tracked touchpoints; structurally limited because it can only credit what was tracked, leaving the most significant brand-building activities invisible.

**MVP (minimum viable product)** *(ch 20)*  
The smallest real version of a product that produces validated learning about customers with the least effort; "minimum" means smallest thing that tests the core bet, not least possible, and it must be a real product rather than a mock.

**MVP boundary** *(ch 20)*  
The PRD section that lists both what is in scope for v1 and, explicitly, what is out; the "out" list is the disciplined part, since each item is something a reasonable person wanted and the boundary keeps the Build-Measure-Learn loop fast.

## N

**negative space** *(ch 6)*  
The set of things a company consistently declines to build or do; sustained over years, these refusals make a brand recognizable more than its features do, because the pattern of constraint is the brand.

**negative-space rule** *(ch 18)*  
The curation discipline that what a portfolio excludes defines its point of view as clearly as what it includes; three to six archetype-aligned projects beat ten. The operational test: for every project featured, name one you left out and write one sentence explaining the exclusion — if you can't, the portfolio has no point of view.

**Net Promoter Score (and its limits)** *(ch 13)*  
Fred Reichheld's single-question loyalty metric (promoters minus detractors on a 0–10 recommend scale); useful as one lagging sentiment signal but undermined as a unique growth predictor by replication studies, and limited by single-item, cultural-calibration, information-compression, and correlation problems.

**Nice Classification** *(ch 8)*  
The international system of goods-and-services classes used to scope a trademark search, where software products typically live in Class 9 or Class 42; a mark's strength and conflicts are always assessed within a class, not in the abstract.

## O

**omnichannel consistency** *(ch 11)*  
An equity-protection strategy of holding the brand's core across every surface a customer meets; each time the experience contradicts the stated identity, the gap between identity and image widens and built equity erodes.

**outcome vs. responsibility statement** *(ch 19)*  
The résumé-bullet discipline of showing what you built and what happened because of it — with a number, a quality metric, and a business impact — rather than naming a duty. A missing number gets a [verify] placeholder; a missing number is honest, a wrong number is disqualifying.

**Outlaw** *(ch 5)*  
The archetype organized around disruption and rebellion, saying the system is broken and need not stay that way; its shadow is nihilism and harm, and it draws its energy from being the challenger.

## P

**persona as research artifact** *(ch 4)*  
A concrete portrait of a target segment member grounded in evidence, not a plausible invention; what separates a real persona is at least one verifiable behavioral claim, with every non-trivial claim tagged Confirmed, Needs Evidence, or Inferred.

**PESO model** *(ch 12)*  
Gini Dietrich's framework naming four media types with distinct economics — paid (advertising you buy), earned (coverage others give unpaid), shared (social channels the audience spreads), and owned (surfaces you fully control) — whose power lies in integration, not any single channel.

**phase gate** *(ch 97)*  
The explicit, specified point at which AI processing stops and irreplaceable human work begins (or vice versa); not a vague commitment to use AI responsibly but a specification — AI handles X, human handles Y, the gate is at Z — sitting at the boundary between Tier 1 pattern work and Tiers 4-7 judgment.

**pipeline as a chain of contracts** *(ch 21)*  
The reframing that a data pipeline is not primarily code but a chain of agreements — about data shape, cost, rate limits, and terms of service — each owned by someone else and subject to change without your consent; the pipeline survives only while every agreement holds.

**plausibility auditing** *(ch 97)*  
The Tier 4 capacity to ask whether an output makes sense given what you actually know about how a domain works; AI generates confident nonsense, and only a human with genuine domain knowledge — which AI cannot shortcut — reliably catches it.

**pooling equilibrium** *(ch 1)*  
The collapsed state where a signal gets cheap enough that everyone can produce it, so it stops distinguishing anyone; the GitHub repository did not vanish as a signal, it pooled once most developers shipped code with AI assistance.

**portfolio as compounding asset** *(ch 18)*  
The chapter's thesis that a portfolio is a product built once whose returns accrue for years — brand impressions, name recognition, implicit credibility — rather than a one-time hiring artifact. The gap between an adequate portfolio that merely clears a hiring funnel and a designed one that compounds is roughly twenty hours of deliberate work for a decade of return.

**portfolio pruning** *(ch 7)*  
Deliberately cutting brands from a portfolio, on the counterintuitive logic that more brands usually means less total value; the survivors concentrate equity, budget, and attention, as when Unilever cut from roughly 1,600 brands to 400.

**positioning against the actual alternative** *(ch 6)*  
Locating a company relative to what the customer genuinely considers — including building it themselves or not solving the problem at all — rather than against a named competitor, which produces a different and usually truer strategy.

**power distance** *(ch 17)*  
A Hofstede dimension measuring how far less powerful members of a society accept and expect unequal distribution of power; high-power-distance cultures respond to brand authority and expert endorsement differently than low-power-distance cultures, where skepticism of authority is more normative.

**PRD (product requirements document)** *(ch 20)*  
A one-page document that forces a team to decide what a product will and will not do before any code is written; it is a decision record and a contract with future-you, not an administrative wish list.

**preference** *(ch 13)*  
Which brand a customer would choose over alternatives under equal price and availability — the higher funnel bar that measures actual competitive standing rather than mere openness.  
  *Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/Brand_preference)*

**price premium** *(ch 2)*  
The measurable extra that buyers will pay for a branded product over a chemically identical generic; the delta is brand equity made visible, reflecting reduced risk and a bundle of associations the generic cannot provide.

**problem statement** *(ch 20)*  
The PRD section naming a specific user, a specific task, its frequency, and what it costs them; a good one is testable against real users, while a vague or symptom-level version names no user, task, or consequence.

**psychographics (VALS)** *(ch 4)*  
Segmentation by values, lifestyle, and personality type rather than by age or income — one of the five bases, offering a cut through a population that demographic data alone cannot reach.

**purpose-washing** *(ch 15)*  
The performance of a values commitment without bearing its cost — a brand signals concern (a "sustainability collection," an ethics statement) while its core behavior and decisions stay unchanged. The behavioral test exposes it: a real purpose is a commitment you maintain when maintaining it costs you something.

## R

**reach** *(ch 12)*  
The number of distinct people who see a message at least once; the right optimization when the goal is awareness — announcing that something exists.

**ReAct loop** *(ch 3)*  
The small think–act–observe cycle (Thought, Action, Observation, repeat) from Yao et al.'s 2023 paper that runs inside each Madison layer, interleaving reasoning with tool use; its three failure points are reasoning, action, and observation failures.

**README as interface** *(ch 23)*  
The last interface layer — the document a user reads to understand what they used or to decide whether to use it — with six elements in reading order: deployed URL first, then what it does, how to use it, its limits, an architecture diagram, and the tech stack.

**recognition asset** *(ch 5)*  
The accumulated pattern of consistent touchpoints that lets a customer's eye snap to a brand without conscious thought; invisible until destroyed, and built only when the hundredth touchpoint stays consistent with the first.

**refresh vs. rebrand** *(ch 14)*  
A spectrum from evolution to revolution: a refresh updates the expression while the core identity stays legible, a rebrand changes name, identity, and positioning so the old brand is no longer legible; the most damaging illegitimate trigger is a new executive wanting a mark of their own.

**reputation management** *(ch 16)*  
The brand discipline of protecting accumulated equity, which builds slowly over years but can collapse in hours — made more acute by social media compressing the response window. It treats crisis response as a brand competence, not just a communications task.

**route-to-counsel** *(ch 8)*  
The discipline of routing every legal-availability question to a trademark attorney, since AI can generate and classify names but cannot run a live register or assess likelihood of confusion; AI owns the generation, humans own the decision, counsel owns the clearance.

**royalty-relief valuation** *(ch 2)*  
Brand Finance's method for putting a number on a brand: estimate the royalty rate you would have to pay to license the brand from someone else, then capitalize that royalty stream at an appropriate rate.

**Ruler** *(ch 5)*  
The archetype organized around control, leadership, and prosperity, claiming to be the standard; its shadow is tyranny, becoming rigid and punishing deviation.

## S

**Sage** *(ch 5)*  
The archetype organized around wisdom, truth, and expertise — the trusted source that knows; its shadow is dogmatism, becoming preachy and unable to update when the evidence changes.

**scene opening** *(ch 19)*  
Opening a pitch in a specific moment — one person, one morning, one pain — rather than in self-introduction, because the first sixty seconds decide whether the audience pays attention and an introduction wastes them.

**scope creep** *(ch 20)*  
The gradual accumulation of features added in the moment, each individually reasonable, that erodes a product's coherence; the PRD's out list with the $100,000 no at its head is the document you return to when someone proposes a new feature.

**scope discipline** *(ch 20)*  
The practice of refusing features that would compromise a product's core; it compounds, because each refusal preserves the coherence of the experience, and over time that coherence becomes the product's identity and brand (as in the Linear case).

**secondary meaning** *(ch 8)*  
The association the public builds, over years and at expense, between a descriptive phrase and one specific source rather than the general description; it is the only way a descriptive mark can become protectable.

**segment vs. demographic** *(ch 4)*  
A demographic descriptor like "women 25–34" is a description, not a segment; what makes a group a segment is a shared need, so two people with nothing demographically in common belong to the same segment if they are solving the same problem.

**Self-as-Project** *(ch 0)*  
The book-long thread in which you build one brand end to end — your own — running a real branding task through Madison at each chapter so that every chapter's artifact feeds the next, from signal baseline to launch.

**separating equilibrium** *(ch 1)*  
The good state in Spence's model, where the signal's cost-structure successfully separates high-productivity candidates from lower-productivity ones — what "a working app on GitHub" did for engineers for roughly twenty years.

**service blueprint (front-stage / back-stage)** *(ch 11)*  
George Lynn Shostack's method that pairs each front-stage touchpoint the customer experiences with the back-stage operations that must execute for it to work, exposing where a front-stage promise outruns the operation behind it.

**Seven Basic Plots** *(ch 10)*  
Christopher Booker's taxonomy of seven fundamental Western plot shapes (Overcoming the Monster, Rags to Riches, the Quest, Voyage and Return, Comedy, Tragedy, Rebirth); for brands the Quest is most invoked, making a claim about why the destination matters rather than only who travels toward it.

**severity triage** *(ch 16)*  
The first step when a monitoring alert fires: classifying the incident by SCCT crisis type before any response is written, because who speaks, what they say, and how fast all follow from that single classification.

**shadow drift** *(ch 5)*  
When a brand's own archetypal commitments curdle into their shadow — the Innocent sliding into denial, for instance — rather than swapping to a different archetype; a degradation from within rather than a category swap.

**Situational Crisis Communication Theory (SCCT)** *(ch 16)*  
W. Timothy Coombs's framework holding that the right crisis response depends on how much responsibility the public assigns the organization; applying a low-responsibility strategy to a high-responsibility crisis actively deepens the damage.

**Spence signaling mechanism** *(ch 1)*  
Michael Spence's idea that employers infer unobservable productivity from costly signals like a degree, which work only as long as their cost-structure holds; when a signal gets cheap to produce, it stops sorting candidates and the market is back to guessing.

**stakes (real and specific)** *(ch 10)*  
The element that makes a transformation believable: a specific user, problem, and measurable change, observed by someone. Abstract stakes ("saves time") signal the writer does not actually know what changed for the customer.

**standardization vs. adaptation** *(ch 17)*  
The core global-branding trade-off between running one identical brand everywhere (efficiency, consistent global recognition, lower cost) and changing the brand's expression to fit each market (local resonance at higher coordination cost). The decision is made per element, not once for the whole brand.

**story shape** *(ch 10)*  
The structural form a brand story takes — Hero's Journey, Quest, Transformation, Rebellion, Service/Methodology, Inversion — which carries the brand's promises and must be named explicitly and checked against the archetype before publishing.

**STP (segmentation / targeting / positioning)** *(ch 4)*  
The canonical three-step sequence that turns a market into a chosen audience: segment by genuinely different needs, target the segment that fits what you do well and is winnable, then position a specific claim in that target's mind — and the order matters.

**Streamlit** *(ch 23)*  
A Python-first web app framework that re-renders on each interaction, suited to tools where the user's job is to do work — configure inputs, run a process, inspect results; the right fit for orchestrated, structured pipelines.

**sub-brand** *(ch 7)*  
A structure attaching a qualifier to a leading master brand (Apple to iPhone), so the new offering inherits almost all the parent's equity at launch; the trade-off is dependency — it is only as strong as the master.

## T

**the fluency trap** *(ch 97)*  
The illusion that fluent AI output is finished and authored work; the smoothness is real but the craft (or learning, or judgment) is not, and the absence of human cognitive engagement is invisible on the surface — which is why systems like Brutalist and Boondoggling make it visible.

**the four verbs (Ideate, Build, Brand, Ship)** *(ch 0, 1)*  
The four kinds of work that now carry career value once building gets cheap; Build is the verb AI cheapened, while Ideate (finding a problem worth solving), Brand (making the work legible to an audience), and Ship (real users, real feedback) are the remaining costly signals.

**the identification layer** *(ch 97)*  
The irreducibly human part of causal analysis — variable selection, edge orientation, and conditioning decisions — that must be performed before AI is used for estimation, because data and pattern-matching cannot choose among causal structures that fit the same statistics (Markov equivalence).

**the no-list** *(ch 6)*  
An explicit, maintained list of specific things the company will not do that a competitor at its stage might; each item must be specific, archetype-consistent, costly to refuse, and testable over time, and the list converts product decisions into a recognizable brand.

**the seven brand components** *(ch 6)*  
Mission, vision, values, UVP, archetype, voice, and positioning — each doing a job the other six cannot, and each constraining the others so the whole stays coherent; if they fit on one page, enough decisions have been made.

**three compounding channels** *(ch 18)*  
The three paths a portfolio pays off through: direct hiring (a recruiter finds and advances you), indirect reference (someone remembers and mentions you later through an invisible chain), and template effects (others clone or fork your design, carrying your name in their commit histories and footer credits). Most graduates design only for the first and leave the compounding of the second and third on the table.

**tone misalignment** *(ch 23)*  
When an interface speaks in a voice the underlying system cannot maintain, such as a warm conversational UI paired with clipped templated outputs; the subtlest misalignment because it operates below explicit claims, fixed by matching interface copy to the system's actual output register.

**tone words** *(ch 9)*  
The three to five adjectives in a brief describing how the design should feel, where vague anti-words like *innovative*, *modern*, and *clean* are forbidden because they constrain nothing; each working word narrows the design space in a direction the archetype implies.

**touchpoint** *(ch 11)*  
Any specific point of contact between a customer and the brand — an ad, an onboarding email, a support chat, an error message — where the brand's promise is either expressed or contradicted; equity is usually lost in the touchpoints nobody designed.

**trade dress** *(ch 8)*  
Protectable visual appearance of a product or its packaging that functions, like a name, to identify its commercial source.

**trademark** *(ch 8)*  
The legal right to use a name or mark for specific goods or services, enforceable against confusingly similar uses in the same category; it is the right that matters most, the hardest to acquire, and the only one of a name's three rights that needs a lawyer to clear.  
  *Source: [en.wikipedia.org](https://en.wikipedia.org/wiki/Category:Sound_trademarks)*

**trademark-strength spectrum (generic / descriptive / suggestive / arbitrary / fanciful)** *(ch 8)*  
The *Abercrombie* scale on which the same property that makes a name immediately understandable makes it hardest to protect; generic marks are never protectable, descriptive ones need secondary meaning, and protection without it begins at suggestive and rises to fanciful.

**translation vs. localization vs. transcreation** *(ch 17)*  
Three escalating levels of language adaptation: translation converts words, localization adds context (units, formats, references), and transcreation re-creates the emotional effect — asking "what would produce this feeling in this culture?" rather than "what do these words mean?" Brand work happens at the transcreation level, where the result may share no words with the original yet remain faithful to it.

**twelve archetypes** *(ch 1)*  
The twelve Jungian character patterns — Hero, Sage, Explorer, Innocent, Creator, Ruler, Caregiver, Magician, Lover, Jester, Everyman, Rebel — used as a strategic positioning system that answers not "what can I do" but "what role do I occupy in my audience's story."

**two-version résumé (ATS / designer)** *(ch 19)*  
The practice of maintaining one résumé in two formats with identical content: an ATS-optimized version (single column, standard headers, plain fonts, keyword-aligned) built to survive automated parsing, and a designer version using the brand's visual system to signal craft to a human reader.

**type specification** *(ch 9)*  
The exact assignment of face, weight, size, line height, and tracking to every text role from H1 to UI label; without it, every new page becomes a fresh typographic decision and accumulated inconsistency destroys system coherence over time.

## U

**UVP (unique value proposition)** *(ch 6)*  
What a product offers that competitors do not, stated in one sentence specific enough that a customer could verify or falsify it; aspiration alone does not qualify.

## V

**validated learning** *(ch 20)*  
Knowledge that comes from what users actually did, not what they said they would do; usage data answers the question that survey-style questions cannot, because users reliably claim they will do things they will not.

**vanity vs. value metric** *(ch 13)*  
The distinction enforced by the Farris test: a vanity metric flatters the team but informs no decision (raw impressions, follower counts), while a value metric connects to a decision or a dollar (qualified conversion, retention, price premium, referral rate).

**visual identity system** *(ch 9)*  
The rulebook of six interacting components — logo, color, typography, imagery, layout, and motion — that together let a stranger read a set of surfaces as one brand; it is a system because each component is perceived in context with the others, not a stack of independent choices.

## W

**WCAG AA contrast** *(ch 9)*  
The accessibility standard requiring a 4.5:1 contrast ratio for normal text and 3:1 for large text and graphical objects, tested on every text-on-background combination; it is a legal requirement in many jurisdictions, not a best-practice suggestion, and failures are fixed by small hex adjustments that preserve the palette's character.

**what vs. how** *(ch 20)*  
The core rule of a PRD: the product team specifies what the product must do, while the engineering team owns how it is implemented. Smuggling implementation choices (a specific model, vendor, or template) into the PRD turns them into false constraints.

**wrong-fast** *(ch 16)*  
Responding quickly with the wrong message — a defensive, minimizing, or unsupportable statement issued before the facts are known — which is worse than silence because it gets falsified when the facts emerge, layering a second crisis on the first.

---

## Appendix — Foundational concepts not yet named in the book

> Concepts the branding knowledge graph treats as foundational (linked by ≥2 other branding pages) that the book's glossary does not currently define. Candidates for future coverage — not gaps in the existing text.

- **Brand management** — linked by 19 pages · https://en.wikipedia.org/wiki/Brand_management
- **Brand implementation** — linked by 6 pages · https://en.wikipedia.org/wiki/Brand_implementation
- **Mountain Dew** — linked by 5 pages · https://en.wikipedia.org/wiki/Mountain_Dew
- **Brand loyalty** — linked by 4 pages · https://en.wikipedia.org/wiki/Brand_loyalty
- **Visual brand language** — linked by 4 pages · https://en.wikipedia.org/wiki/Visual_brand_language
- **Brand valuation** — linked by 3 pages · https://en.wikipedia.org/wiki/Brand_valuation
- **Nation branding** — linked by 3 pages · https://en.wikipedia.org/wiki/Nation_branding
- **Corporate branding** — linked by 3 pages · https://en.wikipedia.org/wiki/Corporate_branding
- **Branding agency** — linked by 3 pages · https://en.wikipedia.org/wiki/Branding_agency
- **Rebranding** — linked by 3 pages · https://en.wikipedia.org/wiki/Rebranding
- **Product naming** — linked by 3 pages · https://en.wikipedia.org/wiki/Product_naming
- **Brand language** — linked by 3 pages · https://en.wikipedia.org/wiki/Brand_language
- **Personal branding** — linked by 2 pages · https://en.wikipedia.org/wiki/Personal_branding
- **Brand engagement** — linked by 2 pages · https://en.wikipedia.org/wiki/Brand_engagement
- **Saffron Brand Consultants** — linked by 2 pages · https://en.wikipedia.org/wiki/Saffron_Brand_Consultants
- **Celebrity branding** — linked by 2 pages · https://en.wikipedia.org/wiki/Celebrity_branding
- **Place branding** — linked by 2 pages · https://en.wikipedia.org/wiki/Place_branding
- **Customer experience** — linked by 2 pages · https://en.wikipedia.org/wiki/Customer_experience
- **Rebadging** — linked by 2 pages · https://en.wikipedia.org/wiki/Rebadging
- **Service mark** — linked by 2 pages · https://en.wikipedia.org/wiki/Service_mark
- **Altagamma** — linked by 2 pages · https://en.wikipedia.org/wiki/Altagamma
- **Teem** — linked by 2 pages · https://en.wikipedia.org/wiki/Teem
- **Diet Pepsi** — linked by 2 pages · https://en.wikipedia.org/wiki/Diet_Pepsi
- **Employer branding** — linked by 2 pages · https://en.wikipedia.org/wiki/Employer_branding
- **Umbrella brand** — linked by 2 pages · https://en.wikipedia.org/wiki/Umbrella_brand

