# SOURCES — *Learning What the Crowd Would Say.*

Ep. 04 · AI in Astronomy & Space Science

## Primary literature

| Short cite | Full source |
|---|---|
| Lintott et al. 2008 | *Galaxy Zoo: morphologies derived from visual inspection of galaxies from the Sloan Digital Sky Survey* — [ADS 2008MNRAS.389.1179L](https://ui.adsabs.harvard.edu/abs/2008MNRAS.389.1179L/abstract) |
| Lintott et al. 2011 | *Galaxy Zoo 1: data release of morphological classifications for nearly 900 000 galaxies*, MNRAS 410, 166 — [Oxford Academic](https://academic.oup.com/mnras/article/410/1/166/1032478) |
| Fortson et al. 2013 | *A Zoo of Galaxies* (review; launch date and launch-rate figures) — [arXiv:1303.7118](https://arxiv.org/pdf/1303.7118) |
| Willett et al. 2013 | *Galaxy Zoo 2* — decision-tree structure; class list — [GZ2 documentation / Galaxy Zoo blog](https://blog.galaxyzoo.org/2015/04/06/visualizing-the-decision-trees-for-galaxy-zoo/); [CANDELS companion, arXiv:1610.03070](https://arxiv.org/pdf/1610.03070) |
| Dieleman, Willett & Dambre 2015 | *Rotation-invariant convolutional neural networks for galaxy morphology prediction*, MNRAS 450, 1441 — [arXiv:1503.07077](https://arxiv.org/abs/1503.07077) · [author's write-up](https://sander.ai/2014/04/05/galaxy-zoo.html) |
| Walmsley et al. 2022 | *Galaxy Zoo DECaLS: Detailed visual morphology measurements from volunteers and deep learning for 314 000 galaxies*, MNRAS 509, 3966 — [Oxford Academic](https://academic.oup.com/mnras/article/509/3/3966/6378289) |
| Galaxy Zoo data releases | Vote-fraction definition, the 5–10% agreement figure, and the 8.67 M-galaxy Galaxy Zoo DESI catalogue — [data.galaxyzoo.org](https://data.galaxyzoo.org/) |
| Domain shift | *From Galaxy Zoo DECaLS to BASS/MzLS: detailed galaxy morphology classification with unsupervised domain adaption* — [arXiv:2412.15533](https://arxiv.org/abs/2412.15533) |
| Rubin / LSST | ~20 billion galaxies over the ten-year Legacy Survey of Space and Time — [KIPAC, Stanford](https://kipac.stanford.edu/news/rubin-countdown-legacy-survey) |
| Zoobot | *Zoobot: Adaptable Deep Learning Models for Galaxy Morphology* — [GitHub](https://github.com/mwalmsley/zoobot) |

Verified but deliberately unused (see `FACTCHECK.md` § "Verified, then deliberately NOT used"):
[Hanny's Voorwerp](https://en.wikipedia.org/wiki/Hanny's_Voorwerp) ·
[Lintott et al. 2009, MNRAS 399, 129](https://arxiv.org/pdf/0906.5304) ·
[*Ideas for Citizen Science in Astronomy*, arXiv:1409.4291](https://arxiv.org/pdf/1409.4291)

## Reel provenance

| Item | Value |
|---|---|
| Brief | `E:/NEU/Jobs/Humanitarians_AI/weekly_stem_videos/ideas.md` → Astronomy, topic **04** |
| Series | AI in Astronomy & Space Science, **Ep. 04** |
| Sibling episodes | `ai-vs-the-data-deluge` (01) · `exoplanet-hunting` (02) · `claude-hai-gravitational-wave-detection` (03) |
| Fact-check date | 2026-08-15, from primary sources, during this build |
| Toolkit | `brutalist.art` · skill `ai-explainer` · channel `claude-hai` |

## Generated imagery — provenance and seeds

Every galaxy in this reel is **synthetic**, produced by `assets/gen_galaxies.py`.
Nothing was downloaded, licensed, or lifted. Re-running the script reproduces
every PNG byte-for-byte.

| Asset | Recipe | Seed |
|---|---|---|
| `spiral_101…104.png` | two-arm spiral | 101, 102, 103, 104 |
| `barred_201…203.png` | barred spiral | 201, 202, 203 |
| `elliptical_301…304.png` | smooth elliptical | 301, 302, 303, 304 |
| `edgeon_401…403.png` | edge-on disc + dust lane | 401, 402, 403 |
| `merger_501…502.png` | two cores + tidal features | 501, 502 |
| `spiral3_601…602.png` | three-arm spiral | 601, 602 |
| `hero.png` | barred spiral, 512 px — the galaxy the reel votes on | 777 |
| `rot_000/045/090/135.png` | `spiral_101` rotated in-plane, canvas kept square | derived |
| `spiral_103_shallow.png` | `spiral_103` degraded to a shallower, coarser survey | derived (noise seed 4242) |
| `field_12x7.png` | 84-galaxy survey sheet | 9001 |
| `field_28x16.png` | 448-galaxy survey sheet | 9002 |

Display stretch is a single fixed asinh (`SOFT=8`, `FMAX=1100`) applied after
accumulation in linear flux, so every tile in the reel shares one scale.

## DOUBLE-CHECK LAW — editorial decisions

1. **The obvious film was rejected.** "There are too many galaxies, so AI sorts
   them" is both what `ideas.md` says Ep. 01 already covers and an episode with
   no idea in it. This cut is about what the label *is*.
2. **The punchline was chosen to not repeat Ep. 03.** The serendipity story
   (volunteers finding Hanny's Voorwerp and the Green Peas) is true, sourced and
   cut, because "people found what the machine could not name" was Ep. 03's
   closing rule one episode earlier.
3. **The accuracy claim is kept conditional.** "~99%" is stated in the voice as
   "against confident volunteer answers", which is the paper's own condition.
4. **The crowd-ceiling claim is labelled as inference.** B10's left panel is the
   reel's own reasoning from the vote-fraction target, not a citation, and both
   `FACTCHECK.md` and the on-screen citation line say so.
5. **The only invented number is marked.** B07's 63/37 split is spoken as "say
   sixty three of a hundred" and captioned ILLUSTRATIVE on screen.
6. **No image is passed off as an observation.** Every scene showing cutouts
   carries a synthetic caption; B10's two "surveys" are the same generated
   galaxy at two simulated depths, which is what makes the domain-shift point
   legible.

## Not used

- No archival or licensed imagery. No AI-generated stills. No stock. No screen
  recordings. No photographs of any named researcher.
- No published Galaxy Zoo figures were reproduced or redrawn.
