# BUILD-LOG — The average that never settles

## Metadata
- **Candidate**: Candidate 02 — The average that never settles
- **Source**: `computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md` (§ "When the Central Limit Theorem politely declines to help")
- **Slug**: `average-that-never-settles`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (racing traces, distributions, formulas) + Remotion (hesitant writer open, quote, your turn, outro)

## Six-Move Audit
1. **Stakes First**: B01, B02 (Running sample mean formula $X̄_n = (1/n)\sum X_i \to \mu$; at $N = 1,000$ points, running mean appears rock-solid).
2. **Anchor Planted**: B03 (Two parallel worlds: Gaussian with finite variance $\sigma^2 < \infty$ vs Heavy-tailed Cauchy with undefined variance $\sigma^2 = \infty$).
3. **Wrong Guess & Falsification**: B04, B05 (Intuition assumes dividing by huge $N$ crushes any outlier; falsified when observation 1,001 arrives: Gaussian barely twitches by $\Delta \approx 0.001$, but Cauchy lurches violently by $\Delta = +45.2$).
4. **Epistemic Mechanism**: B06, B07 (CLT requires finite variance so exponential tail decay makes large deviations impossible; in heavy tails, power-law decay means rare massive observations dominate thousands of routine ones).
5. **Anchor Payoff (Manim Move: `trace`)**: B08, B09 (Two running-mean traces racing side-by-side from $N=1$ to $2,000$ — Gaussian settles to the center line while Cauchy keeps jumping; in production AI, 999 routine $0.01 queries plus one $1,000,000 catastrophe makes average loss evaluate a non-existent quantity).
6. **One Flag**: B10 (Physical systems with hard boundaries have finite variance where CLT holds vs Consequence systems where catastrophic unbounded outcomes break CLT).
7. **Both Directions**: B11 (Direction A: Calm historical sample is not proof of finite variance), B12 (Direction B: The tail-aware toolkit — medians, quantiles, worst-case bounds, and adversarial stress testing).
8. **Carry-Out**: BCRY ("When a system has heavy tails, averaging its history is not measuring the world; it is waiting to be surprised.")
9. **Your Turn**: BHTF (Audit your deployment loss distribution to determine if extreme tail risks exist and replace mean loss with quantile bounds).
10. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats checked against type specifications via `type_check.py`.
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); all durations measured and synchronized in `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 24fps (B01–B12) implementing the `trace` move and heavy-tailed vs Gaussian dynamics.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to native 4K (`3840×2160`), 24 fps, total runtime 181.06s.
- **Gate Audio**: PASS — `mean_volume: -24.0 dB`, `max_volume: -2.9 dB` (audible threshold > -40 dB verified).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography, color palette (`#FAF9F5`, `#3D3929`, `#D97757`), margins, safe-insets, mathematical notation, and readability.
- **Delivery**: Ready for two-target delivery packaging via `deliver.py`.
