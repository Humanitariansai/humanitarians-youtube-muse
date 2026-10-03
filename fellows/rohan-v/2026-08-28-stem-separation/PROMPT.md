# PROMPT — "Stem Separation: Estimation, Not Extraction"

## The brief

Build a 2:30–3:00 explainer on stem separation for a smart non-technical
viewer. The viewer should leave knowing: what the model receives, why it
cannot reverse a mix, what the artifacts mean, and how to calibrate trust.
Go easy on graphics; get it done quickly.

## Constraints given

| Constraint | Resolution |
|---|---|
| Target 2:30–3:00 | Measured **2 min 21 s** |
| Light on graphics | All seven beats use existing library components — no new Remotion builds |
| Same length as first video | Both built at ~141s; 9:16 uses all 7 beats, no beats dropped |
| Non-technical viewer | No signal-processing jargon; cake-baking analogy introduced at B03; bleed explained by example, not math |
| Voice `af_bella` | `metadata.voice_kokoro`; all 7 beats generated locally |
| Opens "Hi, I'm Rohan" | B00, first line of narration |

## Structure

```
B00  ASK          composer cold open — the question the model is being asked
B01  BLUF         one file in; originals gone; model guesses
B02  FRAMEWORK    what "stems" actually means — probability, not recovery
B03  MECHANICS    why mixing is irreversible — the cake analogy
B04  LIMIT        bleed, leftovers, smear — cost of estimation, not failure
B05  APPLY        the trust test — three things to check before using a stem
B06  OUTRO        one-sentence restate + @HumanitariansAI
```

## Build order used

1. Beat sheet authored with narration and library component assignments.
2. `generate_audio_kokoro.py` — 7 beats, `af_bella`, 141s total.
3. `remotion_scenes.py` — all 7 library components rendered and extended to
   audio durations.
4. `compile.py --height 2160` — 16:9 4K master compiled.
5. FFmpeg letterbox pass — 9:16 4K built from all 7 beats.

## No toolkit changes

All components used in this reel (`ClaudeComposerAsk`, `ClaudeWindow`,
`ClaudeVerdictArtifact`, `OutroCTA`) were already in the shared scene
library. No new components were registered.

## What this reel deliberately does not do

- **It does not publish.** No YouTube machinery is invoked.
- **It does not define the model architecture.** Mask-based source separation
  is named as a pattern but the internals are not explained — the viewer
  needs the concept, not the implementation.
- **It does not claim a quality threshold in dB.** The "above −10 dB" figure
  in B05 is a calibration anchor, not a universal standard — FACTCHECK.md
  notes the scope.
