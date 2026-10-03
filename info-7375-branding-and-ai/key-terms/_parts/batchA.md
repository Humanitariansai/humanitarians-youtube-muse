- **AI+1** :: ch 00,01,02,03,04 :: src -
  The division of labor the whole book runs on: the AI agent drafts (reformatting, drafting, pattern-spotting) while you — the +1 — own the accountable judgment, accepting, rejecting, or revising every draft and treating any generated persona, metric, or citation as something that still needs an evidence check.

- **the four verbs (Ideate, Build, Brand, Ship)** :: ch 00,01 :: src -
  The four kinds of work that now carry career value once building gets cheap; Build is the verb AI cheapened, while Ideate (finding a problem worth solving), Brand (making the work legible to an audience), and Ship (real users, real feedback) are the remaining costly signals.

- **Creative Engineer** :: ch 00,01 :: src -
  An engineer who has noticed that the old costly signals have shifted and invested accordingly — investing in Ideate, Brand, and Ship on top of a necessary Build foundation rather than treating a working repository as proof enough.

- **Self-as-Project** :: ch 00 :: src -
  The book-long thread in which you build one brand end to end — your own — running a real branding task through Madison at each chapter so that every chapter's artifact feeds the next, from signal baseline to launch.

- **Madison framework** :: ch 00,03 :: src -
  The open-source, agent-based marketing-intelligence system the book ships and teaches with: five specialized agent roles (Intelligence, Content, Research, Experience, Performance) plus an orchestration layer, used as the worked example for reading AI architecture as a brand decision.

- **Spence signaling mechanism** :: ch 01 :: src -
  Michael Spence's idea that employers infer unobservable productivity from costly signals like a degree, which work only as long as their cost-structure holds; when a signal gets cheap to produce, it stops sorting candidates and the market is back to guessing.

- **separating equilibrium** :: ch 01 :: src -
  The good state in Spence's model, where the signal's cost-structure successfully separates high-productivity candidates from lower-productivity ones — what "a working app on GitHub" did for engineers for roughly twenty years.

- **pooling equilibrium** :: ch 01 :: src -
  The collapsed state where a signal gets cheap enough that everyone can produce it, so it stops distinguishing anyone; the GitHub repository did not vanish as a signal, it pooled once most developers shipped code with AI assistance.

- **twelve archetypes** :: ch 01 :: src -
  The twelve Jungian character patterns — Hero, Sage, Explorer, Innocent, Creator, Ruler, Caregiver, Magician, Lover, Jester, Everyman, Rebel — used as a strategic positioning system that answers not "what can I do" but "what role do I occupy in my audience's story."

- **archetype shadow** :: ch 01 :: src -
  The failure mode built into each archetype — the archetype's own strength taken too far, like the Creator's perfectionism that never ships or the Sage's analysis without action; once you name your archetype, the shadow tells you which failure to watch for.

- **Mark/Pearson system** :: ch 01 :: src -
  Margaret Mark and Carol Pearson's adaptation of Jung's archetypes into a coherent twelve-archetype branding model in *The Hero and the Outlaw* (2001), the source of the twelve identities and their paired shadows this book uses.

- **brand equity** :: ch 02 :: src https://en.wikipedia.org/wiki/Brand_equity
  The worth of a brand in and of itself — the accumulated set of expectations living in customers' minds that changes their behavior and can be measured in money, producing future value through price premium, retention, and forgiveness.

- **intangible asset** :: ch 02 :: src -
  What a brand is in accounting and strategic terms — a thing that produces future cash flow without physical form; on a large acquisition it routinely dwarfs the factories and machinery on the balance sheet.

- **goodwill** :: ch 02 :: src -
  The accountant's name for the slice of an acquisition price that buys no physical asset — in the Cadbury deal, the value of the word itself and what it does inside millions of buyers' heads at the moment of purchase.

- **price premium** :: ch 02 :: src -
  The measurable extra that buyers will pay for a branded product over a chemically identical generic; the delta is brand equity made visible, reflecting reduced risk and a bundle of associations the generic cannot provide.

- **CBBE pyramid** :: ch 02 :: src -
  Keller's customer-based brand equity model as a theory of accumulation across four levels — salience, then performance and imagery, then judgments and feelings, then resonance at the apex — where awareness is the floor, not the goal, and compound equity is built only by climbing to resonance.

- **Aaker dimensions** :: ch 02 :: src -
  David Aaker's four levers of brand equity — awareness, perceived quality, associations, and loyalty — that a manager can actually pull; the diagnostic move is to map a brand on all four and intervene on the weakest, where the lift is greatest.

- **brand identity vs. image** :: ch 02 :: src -
  Identity is what the company projects (the sender's side); image is what actually lands in the receiver's mind; brand work is the management of the gap between them, and equity leaks wherever the two diverge.

- **royalty-relief valuation** :: ch 02 :: src -
  Brand Finance's method for putting a number on a brand: estimate the royalty rate you would have to pay to license the brand from someone else, then capitalize that royalty stream at an appropriate rate.

- **ISO 10668** :: ch 02 :: src -
  The formal standard for brand valuation that Interbrand, Kantar, and Brand Finance all reference; it exists precisely because the competing valuation methods disagree by design and need an arbitration standard.

- **four meanings of "agent"** :: ch 03 :: src -
  The four distinct things the word "agent" means in 2026 — a function with a prompt, an LLM with tools and a loop (ReAct), an autonomous system over a sustained horizon (Devin), and a specialized role in a larger pipeline (Madison) — each implying a different architecture, failure mode, and human relationship.

- **ReAct loop** :: ch 03 :: src -
  The small think–act–observe cycle (Thought, Action, Observation, repeat) from Yao et al.'s 2023 paper that runs inside each Madison layer, interleaving reasoning with tool use; its three failure points are reasoning, action, and observation failures.

- **mega-agent** :: ch 03 :: src -
  The single do-everything model offered as the alternative to a layered architecture; in production it breaks three ways — token costs balloon from re-reading context, failure modes blur so faults can't be located, and the product has no nameable surfaces to sell, version, or trust.

- **graph-based vs. conversation-based orchestration** :: ch 03 :: src -
  The two dominant ways to wire agents together: graph-based (n8n, LangGraph) defines every path in advance for predictability and locatable failures, while conversation-based (AutoGen) lets agents self-organize for flexibility at the cost of harder debugging; Madison chose graph for trustworthy daily execution.

- **architecture as a brand decision** :: ch 03 :: src -
  The chapter's integrating thesis, after McLuhan: how you decompose an AI product into parts quietly decides what customers can see, name, trust, and buy — so engineering seams create brand positions long before any marketing copy is written.

- **human-in-the-loop** :: ch 03 :: src -
  Placing a human gate not as a philosophical stance on autonomy but as risk engineering: find the decisions where a wrong answer is expensive and hard to reverse — publishing content, allocating budget, deploying a persona — gate those, and automate everything else.

- **segment vs. demographic** :: ch 04 :: src -
  A demographic descriptor like "women 25–34" is a description, not a segment; what makes a group a segment is a shared need, so two people with nothing demographically in common belong to the same segment if they are solving the same problem.

- **STP (segmentation / targeting / positioning)** :: ch 04 :: src -
  The canonical three-step sequence that turns a market into a chosen audience: segment by genuinely different needs, target the segment that fits what you do well and is winnable, then position a specific claim in that target's mind — and the order matters.

- **bases of segmentation** :: ch 04 :: src -
  The five different cuts you can take through one population — demographic, geographic, behavioral, psychographic, and needs-based — where demographics is where most people wrongly stop and a shared need is what actually defines a true segment.

- **jobs-to-be-done** :: ch 04 :: src -
  Christensen's reframing that customers do not buy products, they hire them to do a job; the milkshake bought to make a commute tolerable shows that the real job cuts across demographics and predicts purchase better than who the buyer is on paper.

- **cultural tension** :: ch 04 :: src -
  Douglas Holt's added layer: the strongest brands resolve a contradiction or anxiety in the broader culture that a group feels but no brand is addressing, turning positioning from "we do X" into "we do X for people who feel Y about the world."

- **psychographics (VALS)** :: ch 04 :: src -
  Segmentation by values, lifestyle, and personality type rather than by age or income — one of the five bases, offering a cut through a population that demographic data alone cannot reach.

- **persona as research artifact** :: ch 04 :: src -
  A concrete portrait of a target segment member grounded in evidence, not a plausible invention; what separates a real persona is at least one verifiable behavioral claim, with every non-trivial claim tagged Confirmed, Needs Evidence, or Inferred.
