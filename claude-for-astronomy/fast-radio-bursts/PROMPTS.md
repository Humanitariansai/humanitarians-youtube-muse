# PROMPTS — *Twenty Seconds to Decide.*

GATE F expects beat-prefixed prompts for every open slot. **This reel has no open
slots** — every beat is rendered by the pipeline, and the data-looking plots are
generated in-repo. Nothing to hand to a generation service, nothing to spend.

What follows is the two prompt-shaped artifacts the reel *contains*, the plot
recipe, and the scene briefs that stand in for generation prompts.

---

## The two on-screen prompts (content, not requests)

**B00 — the cold-open ask** (verbatim in `ClaudeComposerAsk`):

> Fast radio bursts last milliseconds and the raw data is too big to store. What
> is the actual method for catching one in real time, how good is it, and what
> happens to everything it rejects?

**B12 — the handoff prompt** (read aloud verbatim, per HANDOFF LAW):

> I have a real-time detector that must discard most of its input unmodified,
> because storing everything is impossible. Help me (1) choose an operating
> threshold when false negatives are unrecoverable and false positives are merely
> expensive, (2) design a way to audit what the detector threw away, and (3)
> decide what small fraction of raw input to keep at random as a control.

Rubric, on screen and spoken: a named **cost** for a miss · a way to **measure**
what you lost · a **random** sample kept.

That third item is the real engineering answer to unrecoverable rejection, and it
is the transferable lesson of the episode.

---

## The plot generation (in place of a stock/gen-AI request)

`assets/gen_frb.py` — run `python assets/gen_frb.py`. Deterministic; seeds listed
in `SOURCES.md`. Every panel is drawn from the dispersion relation

    dt = k * DM * (nu^-2 - nu_ref^-2),   k = 4.148808 ms GHz^2 (pc cm^-3)^-1

over CHIME's 400-800 MHz band, then rendered ink-on-white.

| Recipe | How |
|---|---|
| `burst` | a dispersed sweep: per-frequency arrival time from the relation above, Gaussian pulse, patchy band structure. The time axis is **derived from the sweep**, because at 400-800 MHz a DM of 500 sweeps ~9.7 **seconds** — a fixed 100 ms window puts the burst off-panel entirely |
| `dedispersed` | the same pulse with the sweep removed: it stands vertical, which is what the correct trial DM produces |
| `rfi_zero_dm` | one broadband spike, no sweep — microwave oven, power line, lightning |
| `rfi_narrowband` | a few channels, on the whole time — a transmitter |
| `rfi_patch` | bursty, band-limited blobs; margins scale with tile size so the 40 px contact-sheet tiles still work |
| `dm_time` | S/N against trial DM and time. A DM error of 1 pc cm^-3 already smears the pulse by ~19 ms across this band, so the bowtie spans only a couple of DM units — the window is derived, not hard-coded |
| `sheet` | a contact sheet of candidates; all interference except one burst, drawn in terracotta so a beat can point at it |

Three tuning passes were needed before these read (logged in `BUILD-LOG.md`):
the sweeps ran off-window, the noise floor buried them, and the DM trio looked
identical until the three panels were put on one shared time axis.

---

## Scene briefs (in place of generation prompts)

| Beat | Scene class | Brief |
|---|---|---|
| B01 | `B01_Presenter` | Name card. `OM MALI` large centre-left, terracotta hairline under it, role line beneath. Right panel, two rows: "every other method: re-run it" with a loop glyph, the loop then **struck**; and "this one: decide now" with a one-way arrow in the accented token. |
| B02 | `B02_OneBreath` | Kinetic type in three sets against one waterfall. Set 1: space gives it a shape. Set 2: the candidate sheet arrives, one tile terracotta. Set 3: a thin gate slides across the sheet. Closer: what it rejects is deleted. |
| B03 | `B03_Signature` | An empty frequency-time axis. At the source, a vertical line — every frequency at once. A plasma band sweeps across and shears it into a curve. The schematic is replaced by the real synthetic waterfall. Then the DM 200 / 500 / 900 trio on one shared axis, slopes visibly steepening. |
| B04 | `B04_Haystack` | The 336-tile candidate sheet left. Right column, three figures in narration order: 1.5 PB/day, then 10^11 S/N per second, then ~100,000 candidates a day in the accented token. Then exactly one tile on the sheet is ringed terracotta. Closer: one of these is from space. |
| B05 | `B05_Impostors` | Three framed impostor plots: ZERO DISPERSION, NARROWBAND, PATCHY, each with a one-line sub. A terracotta reference curve is overlaid on the first — the shape the search wants and this candidate lacks. Then a callout card: Parkes, the peryton was the staff microwave oven, opened before the timer finished. |
| B06 | `B06_Framework` | A ring buffer circle at the left, marked 35.5 s, with an advancing write head. Five stations: BUFFER, DEDISPERSE (a fan of trial curves), CANDIDATE (two small pictures), CLASSIFY (network glyph), KEEP (a 100 ms slice written, in terracotta). A grey return arc from KEEP back to the ring, labelled "on a no, the buffer overwrites". |
| B07 | `B07_TwoPictures` | The five stations reduce to a rail across the top. Top row: the burst's waterfall and its DM-time bowtie closing to a point, verdict BURST in terracotta. Bottom row: the impostor's waterfall and its bowtie pinned to the bottom edge, never closing, verdict REJECT. Both pairs feed one network glyph. |
| B08 | `B08_FakeReal` | Two columns. Left, SIMULATED: a synthetic curve generated and injected into a panel of real noise; label "the positives". Right, RECORDED: three real interference plots stacked; label "the negatives". Both feed one training block, ringed terracotta. Two lines beneath: the fakes teach it what to want / the real ones teach it what to refuse. |
| B09 | `B09_Result` | Left: recall arc past 99.5%, cited, with the "on test data" condition spelled out. Centre: a funnel from ~100,000 candidates a day down to a handful, survivors in terracotta. Right: counters to 536 bursts, with 62 repeats from 18 sources called out beneath. |
| B10 | `B10_TwoLimits` | Two panels. Left: a cloud of simulated burst shapes with a boundary drawn around them, and one scattered burst sitting outside it, unflagged; boundary labelled "what somebody thought to simulate". Right: the ring buffer again, its write head passing a rejected candidate which greys out and is struck; a one-way NO RE-RUN arrow in terracotta over a struck loop glyph. |
