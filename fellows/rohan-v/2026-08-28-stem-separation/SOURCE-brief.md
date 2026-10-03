# SOURCE-brief — "Stem Separation: Estimation, Not Extraction"

What was asked for, and what the source material was.

## The request

Build a 2:30–3:00 explainer on stem separation — how models pull vocals from
a mix. Target: a smart non-technical viewer. Go easy on graphics. Both this
video and the first video in the series should be the same length.

A viewer should leave knowing four things:

1. What the model actually receives (one flat mixed file; originals are gone).
2. Why separation is estimation, not reversal.
3. What bleed, leftovers, and metallic smear are and why they happen.
4. How to tell when a stem is usable and when it is not.

## Source material

No external documents were supplied for this video. The topic is audio signal
processing; the claims are verifiable from first principles and from the
literature on mask-based source separation (Demucs, Spleeter, Open-Unmix).

## Decisions taken during the build

| Question | Decision | Why |
|---|---|---|
| New Remotion components or library-only? | Library-only (`ClaudeWindow`, `ClaudeVerdictArtifact`, `ClaudeComposerAsk`, `OutroCTA`) | User asked to go easy on graphics and get it done quickly — no new component builds |
| Act structure? | ASK → BLUF → FRAMEWORK → MECHANICS → LIMIT → APPLY → OUTRO | Standard HAI pragmatist ladder; each beat answers one question before moving on |
| Analogy? | Cake-baking (B03) | The most compact way to separate "additive and irreversible" from "reversible"; no physics background required |
| How to frame bleed? | As a cost of estimation, not a failure | Calibrates trust correctly; telling a viewer "this is a bug" leads to wrong conclusions |
| 9:16 version? | Built with all 7 beats, same narration | User specified both videos the same length; 2:21 is under the 3:00 Shorts cap |

## Status

Built, compiled, and QC'd. **Not published** — the toolkit has no publishing
machinery by design. Awaiting review.
