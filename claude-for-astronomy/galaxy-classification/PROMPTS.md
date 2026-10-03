# PROMPTS — *Learning What the Crowd Would Say.*

GATE F expects beat-prefixed prompts for every open slot. **This reel has no open
slots** — every beat is rendered by the pipeline, and even the photographic-looking
galaxy imagery is generated in-repo. There is nothing to hand to a generation
service and no money to spend.

What follows is the two prompt-shaped artifacts the reel actually *contains* (the
on-screen asks), the image-generation recipe, and the scene briefs that stand in
for generation prompts so any slot can be re-cut with its intent intact.

---

## The two on-screen prompts (these are content, not requests)

**B00 — the cold-open ask** (typed into `ClaudeComposerAsk`; must stay verbatim
in sync with the beat sheet):

> Galaxy Zoo asked the public to sort galaxies by shape, and there are now
> catalogues of millions of them. What is the actual method, how accurate is it,
> and where does it break?

**B12 — the handoff prompt** (read aloud verbatim by the narrator, per HANDOFF LAW):

> I have a labelling task where expert annotators genuinely disagree. Show me how
> to (1) keep the disagreement as a soft label instead of forcing a majority vote,
> (2) pick a loss and a calibration check for predicting label distributions, and
> (3) design an active-learning rule that sends only the informative examples back
> to humans.

Grading rubric, shown as the beat's output lines and spoken:

1. does it **name** a loss
2. does it check **calibration**, not just accuracy
3. does it say when to **stop** asking people

---

## The image generation (in place of a stock/gen-AI request)

`assets/gen_galaxies.py` — run `python assets/gen_galaxies.py`. Deterministic:
same seeds in, byte-identical PNGs out. Every galaxy is accumulated in linear
flux and then passed through a single fixed asinh stretch (`SOFT=8, FMAX=1100`),
which is what survey pipelines use — linear near zero so faint arms survive,
logarithmic at the top so the bulge does not bloom into a white disc.

| Morphology | Recipe |
|---|---|
| `elliptical` | Four nested Gaussians (de Vaucouleurs-ish): bright core, long faint envelope, axis ratio 0.58–0.95, **no** structure |
| `spiral` | Exponential disc + two logarithmic arms drawn as ~320 overlapping knots with pitch 0.17–0.26, HII knots seeded along the arms at 5%, bulge composited last |
| `barred` | As spiral, but arms launch from the ends of a straight bar (length 0.13–0.19) rather than from the bulge |
| `edgeon` | Thin exponential disc + a dust lane applied as **absorption** (multiplies the light) bounded by the disc envelope, so it cannot run off the tile as a stray line |
| `merger` | Two cores of unequal brightness + a tidal bridge between them + two tails thrown outward |

Fixed exemplar seeds are listed in `SOURCES.md`. The hero galaxy is
`barred`/seed 777 — a barred spiral **on purpose**: "does it have a bar?" is the
GZ2 question where volunteers genuinely disagree, which is exactly what makes a
vote fraction worth predicting rather than a majority vote.

---

## Scene briefs (in place of generation prompts)

| Beat | Scene class | Brief |
|---|---|---|
| B01 | `B01_Presenter` | Name card. `OM MALI` large centre-left with a terracotta hairline under it; role line beneath. Right panel: "It does not learn what a galaxy is" **struck through**, then "It learns what people would say about it" in the accented token. Kicker top-left (Ep. 04), wordmark bug bottom-right. |
| B02 | `B02_OneBreath` | Kinetic type in three sets against one framed cutout. Set 1: "shape is a clue." Set 2: "but it is a judgement call" — tally marks fan out beside the cutout, many not one. Set 3: the tallies resolve into a proportion bar. Closing line: PREDICT THE DISAGREEMENT. |
| B03 | `B03_Shapes` | Five framed cutouts across the stage, each filling on its spoken label: SMOOTH · SPIRAL · BARRED · EDGE ON · MERGER. The bar in tile 3 is ringed in terracotta — the beat's one accent. Footer: shape encodes formation history + a synthetic-imagery caption. |
| B04 | `B04_Crowd` | Left: the 84-galaxy survey sheet. A counter climbs to 900,000 with its citation; a rate line ticks to 20,000/hr captioned "within twelve hours." Right: ONE tile lifted out of the field with a row of human marks accumulating beneath it to an average of 38, in terracotta. Closing line: the point is the repeat looks, not the crowd. |
| B05 | `B05_Tree` | The hero galaxy left. A three-level decision tree draws right: root "smooth, or features?" → "is there a bar?" → "how many arms?". The traversed path is terracotta; untaken branches stay ink at reduced weight (never below ~40%). Footer: 11 tasks, 2–7 answers each. |
| B06 | `B06_Framework` | Four numbered station cards: `ASK` (tile + tree glyph), `TALLY` (marks collapsing to a proportion bar), `TRAIN` (bar feeding a layered network), `PREDICT` (a fraction emitted for an unseen galaxy). A terracotta arc returns from station 4 to station 1, captioned "active learning: only the galaxies it is unsure about". |
| B07 | `B07_VoteFraction` | The four stations reduce to a rail across the top. Hero galaxy large left with its bar ringed. A 10×10 grid of marks fills; 63 tip to BAR, 37 to NO BAR. The grid collapses into a 0.63 / 0.37 proportion bar. A card reading "barred" is struck through — that is *not* the target — and `0.63` lands in terracotta beside it, with the network's prediction under it. Captioned as an illustrative split. |
| B08 | `B08_NoUp` | One spiral cutout, then four rotated copies (0°, 45°, 90°, 135°) whose labels stay identical. Arrows from all four converge on a single shared-weights block, ringed in terracotta and captioned "same weights, four views". Closing line: the physics tells the network what to ignore. Footer cite: Dieleman, Willett & Dambre 2015. |
| B09 | `B09_Result` | Left: accuracy arc to ~99%, cited, with the condition "against confident volunteer answers" spelled out. Centre: a predicted-vs-actual vote-fraction scatter with the points landing inside a terracotta ±5–10% band around the diagonal. Right: counter to 8,670,000, cited; a forward marker for Rubin's ~20 billion. |
| B10 | `B10_Ceilings` | Two panels. Left: a number line with CROWD and MODEL sitting together and TRUTH elsewhere; the gap bracketed in terracotta, labelled "the model cannot be more right than the crowd". Right: the same galaxy as two cutouts at different depth/pixel scale; an arrow from survey A's network to survey B's image struck through, captioned "distributional mismatch". Footer cite. |
