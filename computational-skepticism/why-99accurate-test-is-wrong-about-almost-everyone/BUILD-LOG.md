# BUILD-LOG — Why a 99%-accurate test is wrong about almost everyone it flags

## Metadata
- **Candidate**: Candidate 01 — Why a 99%-accurate test is wrong about almost everyone it flags
- **Source**: `computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- **Slug**: `why-99accurate-test-is-wrong-about-almost-everyone`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (math & population accumulation) + Remotion (hesitant writer open, quote, your turn, outro)

## Six-Move Audit
1. **Stakes First**: B01, B02 (1 in 10,000 disease prevalence, Harvard physicians' survey guessing 95% vs actual 1%)
2. **Wrong Guess & Falsification**: B04, B05 (intuition equates 99% accuracy to 99% sick probability; falsified by partitioning the population into two starkly unequal pools: 1 sick vs 9,999 healthy)
3. **Epistemic Mechanism**: B06, B07 (Sick pool of 1 person yields 1 True Positive; Healthy pool of 9,999 with 1% error rate yields ~100 False Positives accumulating across grid)
4. **Anchor Planted & Payoff**: B03 (10,000-person dot grid planted) -> B08, B09 (101 positive test slips collected in total: 1 True Positive / 101 Total Flags ≈ 0.99% < 1%)
5. **Both Directions**: B11 (Direction A: Positive flag does not prove condition), B12 (Direction B: Positive flag does massive work, 100× update from 1:10,000 to 1:100)
6. **Carry-Out**: BCRY ("When what you're looking for is rare, the healthy population manufactures more false positives than the sick population can manufacture true ones.")
7. **One Flag**: B10 (Population screening vs symptomatic clinical prior)
8. **Your Turn**: BHTF (Prompt to audit production AI detection accuracy vs base rate)
9. **Outro**: BOUT (Title restatement + @HumanitariansAI skin)

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats checked against type specifications.
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); all durations measured and synchronized in `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 24fps (B01–B12) implementing the `accumulate` move across the 10,000-person dot grid.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to 4K (`3840×2160`), 24 fps, total runtime 173.58s.
- **Gate Audio**: PASS — `mean_volume: -23.9 dB`, `max_volume: -2.9 dB` (audible threshold > -40 dB verified).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography, color palette (`#FAF9F5`, `#3D3929`, `#D97757`), margins, safe-insets, and readability.
- **Delivery**: Ready for two-target delivery packaging via `deliver.py`.
