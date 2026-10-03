# ACTS.md — "Claude making a film about Muse" (general-audience redo)

Redo of `muse/youtube/claude-liam-lecture-claude-making-a-film-about-muse/`
for the humanitarians AI YouTube channel. Same film, new audience:
smart and pragmatic, not necessarily AI experts. Every term is explained
in plain words; the security critique is shown, not told.

Deep-explainer shape (this is an argument: a read, a critique, a
resolution) built with the lecture skill's whole-source discipline.
Channel: claude-liam (Liam, in for Bear · Kokoro am_onyx · Teardown
register · @NikBearBrown).

**Exact title:** Claude making a film about Muse

**Framing (read first):** This film presents **Bear and Claude's opinion**
— their analysis of Meta Muse as of October 3, 2026: what it does, what
it costs, how Meta makes money on it, and a twelve-point security
critique plus how Bear resolved it for himself. "Claude" is the AI
assistant Bear worked with on the analysis — BIDEA says so plainly.
Liam narrates as Bear's stand-in; contested and third-party claims stay
attributed on screen and in voice ("researchers report", "their read",
"in Nik's experience", "the document reports") — the film never presents
the document's opinions as the narrator's own verified facts.

**Core promise:** By the end, a non-expert viewer understands what Muse
is, how Meta plans to make money on it, what the real security concerns
are (in plain language, with pictures), and what a careful user actually
does about them.

**What changed from the original (redo notes):**
- 6 acts kept, but 23 body beats compressed to 16; the two money beats
  merged; the open-questions act cut (too technical for this audience —
  its spirit survives in BHTF).
- The security critique is the main translation job: "fail-safe defaults
  (Saltzer and Schroeder, 1975)" becomes the two-bouncers visual;
  "prompt injection" becomes a concrete hidden-text demo; "policy, not
  crypto" becomes "a promise, not a wall".
- BDEFS cut from 5 terms to 4 (agent, connector, allow-list, prompt
  injection); "intent layer" is introduced where it's used (Act III).
- Token allowances (100M/500M/3B) cut as inside baseball; tier names and
  prices kept, attributed to the document.
- BHTF kept from the original — auditing your own AI apps' disk access
  is the perfect general-audience action.

**Structure:** Five acts.

- Act I — What it is (2 beats): a consumer agent that acts, not just
  chats; launch, downloads, Nik's capability take (attributed).
- Act II — What it does (3 beats): your own computer in Meta's cloud;
  errands; connectors (commerce-first; Amazon blocked, attributed).
- Act III — Money (2 beats): pricing tiers (attributed); the real bet —
  merchant-paid transaction fees and owning the intent layer, with the
  skepticism kept.
- Act IV — The security critique (6 beats): full disk access; deny-list
  vs allow-list (the bouncers); researcher findings (attributed, with
  qualifiers); your data in Meta's cloud; prompt injection demo;
  approval fatigue + trust shortcuts.
- Act V — How Bear resolved it (3 beats): Mac app removed, web-only, no
  phone; the sandbox setup; the general rules (caps outside the agent,
  human for irreversible actions, guard the short list).

**Tone:** honest, plain, pragmatic. Teardown register. The critique is
firm but fair — every sharp claim carries its attribution, and Bear's
own setup shows the concerns are manageable, not apocalyptic.

**What this film is not:** not a product tutorial (see the companion
films); not a prediction of what Meta will do (expectations are voiced
as the document's, never as fact); not a call to avoid AI agents.

**Source facts:**
- The document Bear pasted on 2026-10-03 ("Meta Muse: What It Does,
  Security Concerns, and Business Model"), via the original film's
  ACTS.md + FACTCHECK.md (attribution map) + SOURCES.md. The full
  document text was not re-read for this redo; the original package is
  the source of record. [record]
- Cross-checked product facts (Sept 8 2026 launch, US/Canada, Muse
  Spark, surfaces): docs/muse.md. [record]
- Pricing tiers (Free $0 / Power $20/mo / Maximum $100/mo; card required
  even for free): the document reports; not independently verified.
  Voiced as such. [record]
- 2.5M downloads in ~2 weeks; $1.25/$4.25 API pricing; 6.8 GB runtime
  export; Malwarebytes zero-day; 11-of-47 analysis: third-party/document
  reporting; voiced with attribution, never as established fact. [record]
- Bear's setup (Mac app removed and verified; web-only; sandbox repos
  via bot account; PRs + reviews; caps outside the agent): Bear's
  reported actions, via the original package. [record]
