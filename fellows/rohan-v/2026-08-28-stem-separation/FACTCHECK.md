# FACTCHECK — "Stem Separation: Estimation, Not Extraction"

Every factual claim the narration makes, with its source and verdict.
Verified 2026-08-28.

| # | Beat | Claim | Verdict | Source / Rationale |
|---|---|---|---|---|
| 1 | B00 | "A pop song is not one sound — it's thirty separate recordings collapsed into a single file" | TRUE (scoped) | Professional multitrack sessions routinely exceed 30 tracks. The figure is a representative example, not a minimum or maximum. "Collapsed into a single file" accurately describes the mastering step. |
| 2 | B01 | "A recording session produces separate tracks: vocals, drums, bass, keys" | TRUE | Standard multitrack production. These four are among the most common stem types across commercial stem separators (Demucs, Spleeter, Open-Unmix). |
| 3 | B01 | "Mastering sums them into a single stereo file" | TRUE (simplified) | Mixing (not mastering) performs the summation. Mastering processes the mix output. The reel uses "mastering" as a lay shorthand for the terminal production step that produces a distribution file; technically imprecise but not misleading to the target audience. |
| 4 | B01 | "The original tracks are not on disk. The model has no memory of the session." | TRUE | A distributed audio file (MP3, WAV, AAC) contains no reference to the multitrack session. The model receives only the rendered mix. |
| 5 | B02 | Stems are described as "frequency regions most likely to be human voice" / "transient-heavy broadband bursts" / "everything the first two masks did not claim" | TRUE | Accurately characterizes how mask-based source separation (the dominant modern approach) generates outputs: learned spectral masks applied to a time-frequency representation of the input. The "other" stem is residual by construction. |
| 6 | B02 | "None are the original tracks. All are probability estimates." | TRUE | Outputs are the result of mask application to the mixed signal; they are not extracted from stored originals. The mask is learned from training data as a statistical approximation. |
| 7 | B03 | "Mixing is additive: signal A + signal B = signal C." | TRUE | Digital audio mixing is linear summation in the time domain. |
| 8 | B03 | "Signal C contains no record of A or B separately." | TRUE | After summation, A and B are not stored as separate representations in C. Recovery would require solving an underdetermined system (two unknowns, one equation) without additional constraints. |
| 9 | B03 | "The model learned statistical patterns from multitrack sessions." | TRUE | Supervised source separation models are trained on paired multitrack / mix datasets (MUSDB18, MoisesDB, etc.). |
| 10 | B03 | "It predicts what A and B probably were — it does not compute them." | TRUE | The model's output is a maximum-likelihood estimate conditioned on the mix; it is not an algebraic inversion. |
| 11 | B04 | "Bleed: a ghost of the drums in the vocal stem" | TRUE | Bleed is a well-documented artifact in stem separation. When the drum mask overlaps with vocal-frequency regions, drum energy leaks into the vocal output. |
| 12 | B04 | "Leftovers: bass split across two output files" | TRUE | Low-frequency content that spans the model's source categories (e.g., bass guitar with kick drum) may be split unevenly. This is an artifact of the finite number of output classes. |
| 13 | B04 | "Metallic smear: aggressive masking artifacts on consonants" | TRUE | Hard masking (thresholded spectral masks) introduces ringing and smearing artifacts, particularly on transients and sibilants. The perceptual descriptor "metallic" is widely used in audio production forums for this artifact class. |
| 14 | B05 | "When it fails, the model sounds confident anyway." | TRUE | Source separation models produce an output for every input regardless of confidence. There is no refusal mode; a degraded output is still produced. |
| 15 | B05 | "Rhythm ghost above −10 dB" as a fail threshold | SCOPED | −10 dB relative to the vocal peak is a reasonable calibration anchor for detecting audible bleed, but is not a universal standard. Stated in the reel as an example criterion for the trust test, not a specification. The claim is scoped: the reel says "calibrate your trust", not "−10 dB is always the line." |

## Deliberate omissions

- **No model names.** Demucs, Spleeter, HTDemucs, Open-Unmix, and others are
  not named. The concept is model-independent and the roster changes quickly.
- **No training data citations.** MUSDB18 and similar datasets are not named —
  the viewer does not need provenance to understand the estimation framing.
- **No third-party personal names.** No individual other than the presenter
  appears in narration or on-screen copy.
