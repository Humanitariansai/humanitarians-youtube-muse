# GATE P — narration sign-off

**Reel:** `fast-radio-bursts` — *Twenty Seconds to Decide.*
**Skill:** `ai-explainer`, channel `claude-hai` (@HumanitariansAI) · **Ep. 05**
**Register:** Pragmatist · **Voice:** Kokoro `af_bella` (Bella), free
**Beats:** 14 · **Runtime:** 3:59 · **Audio cost:** $0.00

**VERDICT: PASS**

---

## Why this topic gets this treatment

`ideas.md` calls topic 05 "Finding 'the needle' — AI flagging rare fast radio
bursts in radio telescope data." The needle-in-a-haystack framing is true and,
on its own, is the same film as Ep. 01: there is a lot of data, AI sifts it.

The thing that makes FRB detection genuinely different from every other episode
in this series is that **the haystack is destroyed as you search it.** Raw
voltages sit in a ring buffer of about thirty-five seconds. If the classifier
does not trigger, they are overwritten. So the decision is not just fast, it is
irreversible — and that changes what the model is *for*. It is not a labeller,
it is a shutter.

That is the episode.

## What the viewer should be able to do afterwards

1. **Say why a burst is searchable at all.** Dispersion gives it a shape: low
   frequencies arrive last, so a real burst is a curve and terrestrial
   interference is not.
2. **Reproduce the loop.** Ring buffer → dedisperse over a bank of trial DMs →
   candidate → two images (frequency-time and DM-time) → CNN → trigger a 100 ms
   dump, or let the buffer overwrite.
3. **Explain the training-set trick.** There are not enough real bursts, so the
   positives are simulated and injected into real noise while the negatives are
   real recorded interference.
4. **Name the two limits, and tell them apart.** The pipeline is sharpest on
   bursts resembling what was simulated; and its rejections are unrecoverable,
   so a miss can never be audited.
5. **Transfer it.** Set a threshold when misses are unrecoverable, audit what a
   detector discarded, and keep a random control sample — which is what the
   handoff asks for.

## Teaching-arc check (nopunt whole-sheet checklist)

| Item | Beat | Status |
|---|---|---|
| FRAMEWORK before examples | B06 (five stations + the clock) precedes B07 | ✓ |
| WORKED EXAMPLE using the framework visibly | B07 — one candidate and one impostor walk the same rail, both pairs of images shown | ✓ |
| FALSIFIABILITY / failure-mode beat | B10 — two limits, each with its own panel | ✓ |
| SCAFFOLDED viewer task (prompt **and** rubric) | B12 — prompt read verbatim, then a three-item rubric | ✓ |
| Four bookends | B00 · B11 · B12 · B13 | ✓ |
| No source, no verdict | B04, B05, B08, B09, B10 each carry an on-screen citation; B10's marks which half is inference | ✓ |

## Cognitive-load / pacing notes

- **B03 before B04 on purpose.** The viewer needs the *shape* before the volume,
  or the haystack beat is just a big number with nothing to look for.
- **B05 is concrete-before-abstract for the negatives.** Three interference
  classes are shown as plots before any talk of training data, so B08's "real
  negatives" has a referent.
- **B06 carries the clock deliberately.** The ring buffer is introduced as part
  of the mechanism rather than saved for the failure beat, so B10 can land as a
  consequence the viewer already has the pieces for.
- **B07 shows the impostor's two images alongside the burst's.** The comparison
  is the teaching moment: the DM-time plane is where the two look least alike.
- **Consolidation floors** (duration-planner): the `mechanism` beats B03, B06,
  B07, B08, B10 are the longest by design.

## Register check (Pragmatist)

- Leads with **method** (B06), gives a **worked example** (B07), names the
  **design decision and why** (B08), and spends a full beat on **where it fails**
  (B10). Required Pragmatist move, present.
- The Irreducibly-Human moment is B10's right panel, and it is a *cost* claim,
  not a flattering one: somebody has to choose the threshold, and that choice
  destroys evidence. That is a harder and more useful point than "humans stay in
  the loop."
- No hedging. Every number stated once, on screen, cited.

## Honesty notes for the reviewer

- **No invented numbers.** Unlike Ep. 04, this cut carries no illustrative
  figure — every quantity is published and cited in `FACTCHECK.md`.
- **Two claims are the reel's own inference**, not citations, and are labelled as
  such on screen: that a simulator's assumptions bound the learned signal model
  (B10 left), and that overwritten rejections cannot be audited (B10 right).
- **All dynamic spectra are synthetic**, drawn from the dispersion relation by
  `assets/gen_frb.py`. Scenes caption them. This was deliberate over real
  archival data: no permissions, no network, and full control over the one clean
  burst, one of each interference class, and the two DM-time planes the beats need.
- **"About twenty seconds"** is the usable buffer after pipeline latency; the
  35.5 s ring is on screen in B06 so the relationship is visible.

## Things to listen for on review

1. B06 is the longest body beat (22.1 s) and carries five stations plus the
   clock. If it feels crowded, splitting the clock into its own beat is the fix.
2. B12 reads a long prompt verbatim (28.7 s). Confirm it does not tip into tedious.
3. "Ninety nine and a half percent" and "five hundred and thirty six" are spoken
   as words. Confirm Kokoro lands them cleanly.
