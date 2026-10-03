# SOURCES — "Stem Separation: Estimation, Not Extraction"

Every claim in this reel traces to established signal-processing principles,
widely published literature on learned source separation, or the build session
that produced this file.

## Primary sources

| # | Source | What it establishes |
|---|---|---|
| S1 | Digital audio mixing — first principles | Mixing is linear summation in the time domain; the operation is additive and the intermediate states are not stored in the output |
| S2 | Mask-based source separation literature (Demucs, Open-Unmix, Spleeter, and the MUSDB18 benchmark) | Model outputs are learned spectral masks applied to the mix; they are statistical estimates trained on multitrack/mix pairs, not algebraic inversions |
| S3 | Audio production practice and tooling forums | Bleed, leftovers, and metallic smear as named artifact classes; the perceptual description of masking artifacts on transients and sibilants |
| S4 | This build session — 2026-08-28 | The pipeline was run end to end; every build step the reel references was actually executed |

## Toolkit files cited (S4)

| File | What it supports |
|---|---|
| `runtime/scripts/generate_audio_kokoro.py` | "Kokoro-82M, Apache-2.0, local, no API"; measured durations are ground truth |
| `CLAUDE.md` rule 2 | Audio-first; durations are the master clock |

## Verification performed in this session

| Claim | How it was verified |
|---|---|
| 7 beats synthesized offline at $0.00 | Kokoro ran locally; total cost $0.00 per generate_audio_kokoro.py output |
| Audio durations drive the visuals | Composition durations set from measured mp3 lengths; every rendered beat matches to within 0.03s |
| Both 16:9 and 9:16 use all 7 beats | concat.txt in the 9:16 build pass contains all B00–B06; final duration 140.9s vs. 141.3s (rounding only) |

## Not sourced, and therefore not claimed

- Any specific dB threshold as a universal pass/fail criterion for stem quality.
- Any comparison between named stem separation tools.
- Any statement about review turnaround or merge timing for pull requests.
