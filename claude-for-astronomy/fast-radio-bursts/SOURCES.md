# SOURCES — *Twenty Seconds to Decide.*

Ep. 05 · AI in Astronomy & Space Science

## Primary literature

| Short cite | Full source |
|---|---|
| CHIME/FRB RFI (2023) | *Mitigating radio frequency interference in CHIME/FRB real-time intensity data* — [arXiv:2206.07292](https://arxiv.org/pdf/2206.07292) · [IOPscience, ApJS](https://iopscience.iop.org/article/10.3847/1538-4365/acc252). Source of the 1.5 PB/day input rate, the 10^11 S/N values per second, and the ~10^5-to-a-few-per-day false-positive reduction. |
| CHIME/FRB baseband (2021) | *An analysis pipeline for CHIME/FRB full-array baseband data* — [arXiv:2010.06748](https://arxiv.org/pdf/2010.06748) · [IOPscience, ApJ](https://iopscience.iop.org/article/10.3847/1538-4357/abe626). Source of the 35.5 s ring buffer, the ~14 s pipeline latency, the ~100 ms dump on trigger, and the high-S/N-only retention. |
| Agarwal et al. 2020 (FETCH) | *FETCH: A deep-learning based classifier for fast transient classification*, MNRAS 497, 1661 — [arXiv:1902.06343](https://arxiv.org/abs/1902.06343) · [Oxford Academic](https://academic.oup.com/mnras/article/497/2/1661/5863960) · [code](https://github.com/devanshkv/fetch). Source of the two-image (frequency-time + DM-time) input design, the simulated-positives / real-negatives training set, and the >99.5% accuracy and recall figures. |
| Petroff et al. 2015 | *Identifying the source of perytons at the Parkes radio telescope* — [arXiv:1504.02165](https://arxiv.org/abs/1504.02165). Source of the microwave-oven identification. |
| CHIME/FRB Catalog 1 | *The First CHIME/FRB Fast Radio Burst Catalog* — [arXiv:2106.04352](https://arxiv.org/abs/2106.04352) · [IOPscience](https://iopscience.iop.org/article/10.3847/1538-4365/ac33ab). Source of the 536 bursts, 62 repeat bursts from 18 sources, 400–800 MHz, 2018-07-25 to 2019-07-01. |
| CHIME/FRB system overview | *The CHIME Fast Radio Burst Project: System Overview* — [IOPscience, ApJ](https://iopscience.iop.org/article/10.3847/1538-4357/aad188) |
| Verifying FRBs | *Verifying and Reporting Fast Radio Bursts* — [arXiv:1808.07809](https://arxiv.org/pdf/1808.07809) (RFI morphology classes) |

Verified but deliberately unused: the Lorimer burst discovery, and FRB 20200428
from the magnetar SGR 1935+2154. See `FACTCHECK.md` § "Verified, then
deliberately NOT used".

## Reel provenance

| Item | Value |
|---|---|
| Brief | `E:/NEU/Jobs/Humanitarians_AI/weekly_stem_videos/ideas.md` → Astronomy, topic **05** ("Finding 'the needle'") |
| Series | AI in Astronomy & Space Science, **Ep. 05** |
| Sibling episodes | `ai-vs-the-data-deluge` (01) · `exoplanet-hunting` (02) · `gravitational-wave-detection` (03) · `galaxy-classification` (04) |
| Fact-check date | 2026-08-16, from primary sources, during this build |
| Toolkit | `brutalist.art` · skill `ai-explainer` · channel `claude-hai` |
| Slug | `fast-radio-bursts` — matches the folder, following the naming the human applied to Ep. 04 |

## Generated imagery — provenance and seeds

Every dynamic spectrum is **synthetic**, produced by `assets/gen_frb.py` from the
dispersion relation. Nothing was downloaded, licensed, or lifted. Re-running the
script reproduces every PNG byte-for-byte.

    dt = k * DM * (nu^-2 - nu_ref^-2),   k = 4.148808 ms GHz^2 (pc cm^-3)^-1
    band: 400-800 MHz (CHIME's, and Catalog 1's)

| Asset | Recipe | Seed |
|---|---|---|
| `burst_dm500.png`, `burst_dm500_big.png` | dispersed sweep, own time axis | 11 |
| `burst_dedispersed.png` | the same pulse, sweep removed | 11 |
| `burst_scattered.png` | scattering broadened as nu^-4 | 12 |
| `burst_dm200.png`, `burst_dm500_trio.png`, `burst_dm900.png` | three DMs on ONE shared axis, sized for DM 900 | 13, 11, 14 |
| `rfi_zero_dm.png`, `rfi_zero_dm_big.png` | broadband, no sweep | 21 |
| `rfi_narrowband.png` | fixed channels, always on | 22 |
| `rfi_patch.png` | bursty band-limited blobs | 23 |
| `dmtime_burst.png` | bowtie closing at a real DM | 11 |
| `dmtime_rfi.png` | window's lower edge at DM 0, so the apex sits on the bottom and never closes | 31 |
| `sheet_10x6.png` | 60 candidates, burst at index 37 | 9101 |
| `sheet_24x14.png` | 336 candidates, burst at index 201 | 9102 |

Display: one fixed asinh-free linear paint with gamma 0.85 onto ink-on-white.
Noise is deliberately faint — see `BUILD-LOG.md` for why that is a GATE V
constraint and not just an aesthetic one.

## DOUBLE-CHECK LAW — editorial decisions

1. **The needle-in-a-haystack film was rejected as the spine.** It is Ep. 01's
   framing, and `ideas.md` says Ep. 01 exists so later episodes need not repeat
   it. The volume beat survives only to set up the thing that is new.
2. **The spine is irreversibility.** Every other episode's method can be re-run
   on stored data; this one cannot, because the buffer overwrites. That is the
   distinct idea and the distinct limit.
3. **The simulated-positives point is framed as a design tell, not the failure**,
   so it does not become Ep. 03's out-of-distribution punchline a second time.
4. **Two claims are labelled as inference on screen** (B10, both panels), and the
   citation line says so explicitly.
5. **No invented numbers.** Every quantity is published and cited.
6. **The 20 s figure is derived and shown as such** — the 35.5 s ring is on
   screen in B06 next to it, so the viewer can see where 20 comes from.
7. **A wrong derived figure was dropped rather than corrected.** An early draft
   carried a bits-per-second rate taken from a search summary; the arithmetic did
   not check out against the paper's 1.5 PB/day, so the derived number came out
   entirely rather than being patched.

## Not used

- No archival or licensed data. No AI-generated stills. No stock. No screen
  recordings. No published FRB figures reproduced or redrawn.
