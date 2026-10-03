# FACTCHECK — *Knowing the Noise by Name.*

**Reel:** `claude-hai-gravitational-wave-detection` (ai-explainer, claude-hai)

## Provenance of this verification — read first

This reel is a **re-authored rebuild** of
`claude-for-astronomy/gravitational-wave-detection/`. Every factual claim below
was verified in that reel's own `FACTCHECK.md` against primary sources
(verification pass dated **2026-08-08**, quoted source text recorded per claim).

**What this pass did:** each surviving claim was re-read against the quoted
source text recorded in that file, re-mapped to its new beat, and re-checked for
whether the *rewritten* Pragmatist narration still says only what the source
supports. Claims the rebuild dropped were dropped, not softened; two claims are
**new to this cut** and are marked `NEW` below.

**What this pass did NOT do:** it did not re-fetch the primary sources over the
network. Verification is inherited, with the source URLs carried verbatim so any
claim can be re-opened in one click. If you want a live re-verification pass
before publishing, that is a separate step and worth doing for the two `NEW`
rows in particular.

**Money status:** $0.00. No paid API was called for any part of this reel —
Kokoro (local) for voice, Manim and Remotion (local) for every visual. Zero
archival stills are used, so there is nothing to license.

---

## Claims, by beat

| # | Claim as used in this cut | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | On 17 August 2017 LIGO recorded a real binary neutron star merger (GW170817), and a short instrumental transient hit the Livingston detector ~1.1 s before the coalescence time — a brief saturation in a digital-to-analog converter | B03 | ✅ | [LIGO-T1700406-v3, BayesWave Glitch Subtraction for GW170817](https://dcc.ligo.org/LIGO-T1700406/public); [GW170817 discovery paper](https://arxiv.org/pdf/1710.05832) |
| 2 | That saturation prevented the automated low-latency search from registering a simultaneous two-detector event; the first public alert was a single-detector Hanford candidate — a type never disseminated in low latency before | B03 | ✅ | [Low-Latency GW Alerts for Multi-Messenger Astronomy During O2](https://arxiv.org/pdf/1901.03310); [Modeling compact binary signals and instrumental glitches](https://arxiv.org/pdf/2101.01200) |
| 3 | Fermi-GBM detected short gamma-ray burst GRB 170817A ~1.7 s after the merger time | B03 | ✅ | [Fermi-GBM Detection of GRB 170817A](https://arxiv.org/abs/1710.05446) |
| 4 | ~70 observatories on seven continents and in space took part in the electromagnetic follow-up | **not used in this cut** (dropped with the B03 narration trim) | ✅ verified, unused | [LIGO Caltech GW170817 press release](https://www.ligo.caltech.edu/page/press-release-gw170817) |
| 5 | In O1 — 51.5 days — roughly 10⁶ glitches above an SNR-6 threshold were recorded | B04 | ✅ | [Zevin et al. 2017, *Gravity Spy*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5927381/) |
| 6 | LIGO's detector-characterisation effort is far too small to classify that volume by hand — the project's own stated motivation | B04 | ✅ | [Zevin et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5927381/) |
| 7 | A blip glitch is a very short (~10 ms) wide-band transient that resembles the time-frequency signature of a massive binary black hole merger closely enough that standard signal-consistency checks cannot separate the two | B05 | ✅ | [Blip glitches in Advanced LIGO data](https://arxiv.org/abs/1901.05093) |
| 8 | Blip glitches occur at roughly two per hour of data | B05 | ✅ | [Blip glitches in Advanced LIGO data](https://arxiv.org/abs/1901.05093) |
| 9 | Each glitch is visualised as a spectrogram at four time windows at once (±0.25, 0.5, 1.0, 2.0 s), and all four are shown to both volunteers and the algorithm | B06, B07 | ✅ | [Zevin et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5927381/) |
| 10 | Volunteers sort the images into named morphological classes (Blip, Koi Fish, Whistle, Scattered Light among them); the project launched with 20 classes | B06, B08, B09 | ✅ | [Zevin et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5927381/) (20 classes); [Glanzer et al. 2022, data quality up to O3](https://arxiv.org/pdf/2208.12849) (class list) |
| 11 | A convolutional neural network trains on the human-labelled images and classifies new glitches on its own | B06, B07 | ✅ | [Zevin et al. 2017 (abstract)](https://arxiv.org/abs/1611.04596) |
| 12 | Machine and volunteer classification are **coupled**: the network gives a fast first-pass sort and enables tiered volunteer routing, while volunteers verify/correct machine labels and supply new training data | B06 | ✅ | [Glanzer et al. 2022](https://arxiv.org/pdf/2208.12849) |
| 13 | The original CNN classifier achieved 97.1% average accuracy on test data | B08 | ✅ | [Zevin et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5927381/) |
| 14 | By the end of O3, Gravity Spy classifications covered 233,981 Hanford glitches and 379,805 Livingston glitches | B08 | ✅ (addends sourced) | [Glanzer et al. 2022](https://arxiv.org/pdf/2208.12849) |
| 15 | 613,786 combined ("more than six hundred thousand") | B08, B11 | ✅ computed | sum of row 14; both addends shown on screen |
| 16 | In beta testing, volunteers identified two previously unknown morphologies — Paired Doves and Helix — that were not in the machine's training set | B09 | ✅ | [Zevin et al. 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5927381/) |
| 17 | Gravity Spy's classifier is a different tool from BayesWave, the Bayesian method actually used to model and subtract GW170817's own Livingston glitch | B10 | ✅ | [LIGO-T1700406-v3](https://dcc.ligo.org/LIGO-T1700406/public) |
| 18 | `NEW` LIGO's real-time detection pipelines (PyCBC Live, GstLAL, MBTA) are matched-filtering searches against a bank of precomputed waveform templates — classical signal processing, not a trained model making the primary detection call | B10 | ✅ as framing | carried from the source reel's `SCRIPT.md` §"Why Gravity Spy, not the low-latency search pipeline itself"; the characterisation of matched filtering as template-bank signal processing is standard and uncontested in the GW literature. **Flagged for live re-verification before publishing.** |
| 19 | `NEW` A trained classifier can only assign a class present in its training set, so a novel morphology on a changing instrument is out of its reach — which is why the volunteer layer is load-bearing rather than decorative | B09, B11 | ✅ as reasoning | This is an inference the reel makes, not a quoted claim. It follows directly from rows 10, 11 and 16: the class set is fixed at training time, and the two new classes in row 16 were found by people. Stated on screen as a rule ("a classifier cannot name what it has never seen"), not attributed to a source. |

## Claims present in the source reel but DROPPED from this cut

Dropped for length and focus, not because they failed:

- The whole electromagnetic follow-up campaign — the AT 2017gfo kilonova
  counterpart (source beat 5) and the 70-observatory figure (source beat 5,
  row 4 above). B03 was cut back to the near miss itself: the glitch, the
  single-detector alert, and the independent Fermi confirmation. The follow-up
  is a second story and it was making the beat run 29 s.
- Gravity Spy's Zooniverse partnership and 12 October 2016 full public launch
  date (source beats 10) — the date is not load-bearing for the method.
- "Thousands of volunteers" as a headline figure (source beat 10).
- The Paired Doves *physical cause* (beamsplitter motion at Hanford, source beats
  16–17). Deliberately dropped: the technical source frames it as "possibly
  linked", and the rebuild's B09 only needs the discovery, not the diagnosis.
- GW150914 and the GWTC-5.0 event total — background in the source, never scripted.

## Rounding and wording decisions (DOUBLE-CHECK LAW)

1. **"about ninety seven percent"** for 97.1% in the voice; the exact figure
   **97.1%** appears on screen in B08 with its citation. Same treatment as the
   source reel.
2. **"fifty one and a half days"** — spoken in full rather than rounded to 51, a
   change from the source reel, which rounded down. The exact figure reads
   cleanly at Bella's pace and rounding was never necessary.
3. **"more than six hundred thousand"** in the voice; the two exact per-detector
   figures and their sum are on screen.
4. **"a converter saturates"** compresses "a very brief (<5 ms) saturation in a
   digital-to-analog converter". The mechanism is named; the 5 ms detail is
   dropped as load the beat does not need.
5. **No hyphens, dashes or colons in narration**, carried over from the source
   reel's build requirement — it measurably improves Kokoro's delivery.
6. **Every number on screen is sourced.** An illustrative confidence figure
   (`0.98`) was drafted for B07's output card and cut during visual QC — a
   fabricated number sitting on a card that reads like a model readout is a
   DOUBLE-CHECK LAW hazard even when captioned. The card now carries only what
   the source supports: the class name and the fact that the call is made in
   milliseconds.
