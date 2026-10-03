# PROMPTS — *Knowing the Noise by Name.*

GATE F expects beat-prefixed prompts for every open slot. **This reel has no open
slots** — every beat is rendered by the pipeline (Manim or a registered Remotion
composition), so there is nothing here to hand to a generation service and no
money to spend.

What follows is therefore not a shopping list. It is the two prompt-shaped
artifacts the reel actually contains — the on-screen asks — plus the scene briefs
that stand in for generation prompts, so that if any slot is ever re-cut the
intent is recorded.

---

## The two on-screen prompts (these are content, not requests)

**B00 — the cold-open ask** (typed into `ClaudeComposerAsk`, must stay verbatim
in sync with the beat sheet):

> LIGO logged about a million instrument glitches in one 51-day observing run,
> and some of them look like real black-hole mergers. What is the actual method
> for sorting them, how accurate is it, and where does it fail?

**B12 — the handoff prompt** (typed into `ClaudeComposerAsk`, read aloud verbatim
by the narrator per HANDOFF LAW):

> I have a labelled dataset where two classes look nearly identical and one is
> rare. Walk me through (1) the human-in-the-loop step that catches a class my
> model has no label for, (2) the metric that exposes the confusion between the
> two look-alikes, and (3) the test that would prove the pipeline failed.

Grading rubric shown as the beat's output lines, and spoken:

1. a **named** metric, not accuracy
2. a human placed exactly where **new** classes appear
3. a stated **failure condition**

---

## Scene briefs (in place of generation prompts)

| Beat | Scene class | Brief |
|---|---|---|
| B01 | `B01_Presenter` | Name card. `OM MALI` large centre-left with a terracotta hairline sweeping under it; role line beneath; the beat's claim set right — "the hard part is not the physics" / "trusting the instrument" with the second phrase in terracotta. Kicker top-left, wordmark bug bottom-right. |
| B02 | `B02_OneBreath` | Kinetic type in three sets. A dense field of small ink glitch ticks behind set 1 with exactly one terracotta tick; three ticks resolve to framed tiles at set 2; name chips attach at set 3; closing rule lands full width. |
| B03 | `B03_NearMiss` | One shared time axis, `t=0 MERGER`. Two lanes (HANFORD, LIVINGSTON) with schematic strain traces. Terracotta glitch spike at −1.1 s on Livingston; that lane greys downstream and its path to the joint-search node is crossed out; the node stamps `SINGLE DETECTOR` and `first public alert`. Second marker at +1.7 s: `FERMI · GRB 170817A`. Closing line: *One glitch, and the alert went out on one detector.* (The 70-observatory follow-up was cut with the narration trim — it is in `FACTCHECK.md` row 4, not on screen.) |
| B04 | `B04_MillionGlitches` | 51-cell day bar filling left to right while a counter climbs to `1,000,000` (terracotta on landing). Citation line under the counter. Right side: a tall stack of glitch tiles against a handful of reviewer marks. Closing stamp `HAND SORTING DOES NOT SCALE`. |
| B05 | `B05_Impostor` | Two identical spectrogram frames, level, side by side. **Both features are drawn from the same envelope function** — the merger's bands drift right as frequency rises, the blip's do not. Drawing them as obviously different shapes would be a prettier picture and a false one; the whole beat is that a simple check cannot separate them. Both hold together ≥2 s. A consistency-check bracket spans both and returns the same verdict twice; the second flips terracotta to `MISREAD`. |
| B06 | `B06_Framework` | Four numbered stations left to right: `RENDER` (glitch → four stacked tiles), `LABEL` (volunteer marks drop named chips), `TRAIN` (labelled tiles feed a layered network glyph), `SORT` (flood fans into named bins). A terracotta arc returns from station 4 to station 2, captioned `unsure cases route to people`. |
| B07 | `B07_WorkedExample` | The same four stations reduced to a thin rail across the top so the framework stays visible; a terracotta marker walks it. Four labelled windows `0.25 s · 0.5 s · 1.0 s · 2.0 s` show the SAME event — the feature narrows as the window widens. Right column splits into *the human call* (volunteer marks + a `BLIP` chip) and *the machine call* (network glyph + an output card reading `BLIP` / `in milliseconds`). The illustrative confidence figure was dropped: nothing unsourced now appears on screen. |
| B08 | `B08_Result` | Left: accuracy arc filling to `97.1%`, figure in terracotta, cited. Beneath it a 20-cell class strip with four cells labelled. Right: two bars growing to `233,981` (Hanford) and `379,805` (Livingston), each figure landing with its bar, totalling `613,786` through O3, cited. |
| B09 | `B09_UnseenClass` | An incoming row of glitch tiles above five labelled bins (`Blip · Koi Fish · Whistle · Scattered Light · +16 more`). Five tiles drop INTO their bins; the stream keeps arriving. Two terracotta tiles match nothing and hold a `?`. The network returns its only possible answer, `nearest known class`, struck through and captioned *confidently wrong*. A volunteer mark reaches past the bins, two new terracotta bins are drawn — `Paired Doves`, `Helix` — and the stalled tiles land in them. Closing rule across the frame. |
| B10 | `B10_Scope` | Three columns: `DETECT` (template bank, owner chip `MATCHED FILTERING (classical)`), `CLEAN ONE EVENT` (single glitch subtracted, owner chip `BAYESWAVE (one event)`), `NAME THE CATEGORY` (continuous stream into named bins). The first two are struck through; the third stays live and turns terracotta. Closing line: `use it for the category, not the catch`. |
