# GATE P — narration sign-off

**Reel:** `claude-hai-gravitational-wave-detection` — *Knowing the Noise by Name.*
**Skill:** `ai-explainer`, channel `claude-hai` (@HumanitariansAI)
**Register:** Pragmatist · **Voice:** Kokoro `af_bella` (Bella), free
**Beats:** 14 · **Audio cost:** $0.00

**VERDICT: PASS**

---

## What the viewer should be able to do afterwards

A student who watches this should be able to:

1. **State the problem correctly.** Name the reason gravitational-wave astronomy
   needs a noise classifier at all — the instrument's own transients outnumber
   real signals by orders of magnitude, and the most common ones imitate real
   signals — and distinguish that from "AI finds the waves."
2. **Reproduce the method from memory, in four steps.** Spectrogram at four time
   windows → volunteer labels → CNN trained on those labels → machine sorts
   first and routes uncertain cases back to people. The loop closing is the
   point, not the network.
3. **Name the failure mode without being prompted.** A trained classifier can
   only assign a label it has already seen; a changing instrument produces
   classes that are not in the training set, and *people* are what catch them
   (Paired Doves, Helix).
4. **Draw the scope boundary.** This method names noise categories. It does not
   detect waves (matched filtering does) and it did not clean GW170817's glitch
   (BayesWave did).
5. **Transfer it.** Apply the same three questions — where does a human go, which
   metric exposes the confusion, what would failure look like — to their own
   labelled dataset. That is what the handoff beat asks for.

## Teaching-arc check (nopunt whole-sheet checklist)

| Item | Beat | Status |
|---|---|---|
| FRAMEWORK before examples | B06 (the four-station loop) precedes B07 | ✓ |
| WORKED EXAMPLE using the framework visibly | B07 — one blip walks the same four stations, rail stays on screen | ✓ |
| FALSIFIABILITY / failure-mode beat | B09 (out-of-distribution class) + B10 (scope boundary) | ✓ |
| SCAFFOLDED viewer task (prompt **and** rubric) | B12 — prompt read verbatim, then a three-item grading rubric | ✓ |
| Four bookends | B00 cold open · B11 verdict · B12 handoff · B13 title restate | ✓ |
| No source, no verdict | every claim beat carries its citation on screen (B04, B08 cite by author/year; B05/B09/B10 name the tool or class) | ✓ |

## Cognitive-load / pacing notes

- **One new element per beat.** B04 (volume) and B05 (similarity) are deliberately
  split — they are two different reasons the problem is hard, and merging them
  would put two new elements in one consolidation window.
- **B02 is an advance organizer**, not a teaser: it states the whole idea in one
  breath so every later beat lands against a whole the viewer already holds
  (EXECUTIVE-SUMMARY LAW).
- **Consolidation floors** (duration-planner): `mechanism` beats B06/B07/B09 are
  the longest body beats by design (~20 s+), because each new step must integrate
  with steps still active in working memory. `realworld` B03 is an anchor, not
  instruction, and carries its detail on screen rather than in the voice.
- **Comparisons hold.** B05's real-chirp / blip pair is on screen together for
  more than two seconds before any verdict is drawn on it.

## Register check (Pragmatist)

- Leads with **method** (B06), states **when to use it** (B10, lane 3), and gives
  a full beat to **when NOT to and where it fails** (B09, B10) — the Pragmatist
  register's required move, not a hedge.
- No academic hedging, no personality tax. Numbers are stated once, on screen,
  with their source.
- The Irreducibly-Human moment is B09 and it is earned rather than sermonised:
  the volunteers found two classes the network could not name. One aside, no
  repetition.

## Honesty notes for the reviewer

- The **97.1%** figure is the *original* published classifier on *test* data; the
  narration says "the first classifier" for that reason. It is not a claim about
  the current production system.
- **613,786** is a computed sum of two sourced per-detector figures (233,981 +
  379,805); both addends appear on screen in B08.
- **No unsourced number appears on screen.** An illustrative confidence figure
  (`0.98`) was drafted for B07's output card and then cut during the visual-QC
  pass: a made-up number on a card that looks like a readout is exactly the kind
  of thing a viewer will quote back. The card now reads `BLIP` / *in
  milliseconds*, both of which the source supports.
- The Paired Doves *cause* is deliberately not asserted. The source's technical
  citation says "possibly linked" to beamsplitter motion at Hanford, so the reel
  says volunteers found and named the morphology and stops there.

## Things to listen for on review

1. B03 is the longest single-sentence chain in the reel. Does it stay followable
   at Bella's pace, or should it split into two beats?
2. B12 reads a three-clause prompt aloud. Verbatim readings are supposed to feel
   slightly long — confirm it does not tip into tedious.
3. "Fifty one and a half days" and "one point one seconds" are spoken as words on
   purpose (Kokoro mangles some numerals). Confirm they land cleanly.
