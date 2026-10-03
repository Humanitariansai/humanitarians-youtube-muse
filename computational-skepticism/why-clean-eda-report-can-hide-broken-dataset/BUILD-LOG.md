# BUILD-LOG — Why a clean EDA report can hide a broken dataset

## Metadata
- **Candidate**: Candidate 03 — Why a clean EDA report can hide a broken dataset
- **Source**: `computational-skepticism-for-ai/chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md`
- **Slug**: `why-clean-eda-report-can-hide-broken-dataset`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (funnel & table join math moves) + Remotion (hesitant writer open, quote, your turn, outro)

## Six-Move Audit
1. **Stakes First**: B01, B02 (Spotless EDA report with zero missing values, perfect distributions, no outliers vs. catastrophic subpopulation failure in production deployment).
2. **Wrong Guess & Falsification**: B04, B05 (The intuitive belief that zero missing cells in a merged table implies complete data coverage; falsified by realizing that dropped entities produce zero missing cells because they never entered the table).
3. **Epistemic Mechanism**: B06, B07 (Three source tables joining on an unstandardized key drop unmatched rows silently into the void — the `collapse` Manim move demonstrates row attrition before EDA begins).
4. **Anchor Planted & Payoff**: B03 (Three upstream source tables funneled into merged dataset) -> B08, B09 (EDA calculates summary statistics solely over the survivors, mistaking surviving records for the complete population).
5. **Both Directions**: B11 (Direction A: A clean EDA report is not proof of dataset integrity), B12 (Direction B: EDA is still an essential diagnostic for what survived; it just cannot audit its own boundary).
6. **Carry-Out**: BCRY ("You cannot compute the missingness of rows that never made it into the dataset — every diagnostic reads only the survivors and calls them the world.")
7. **One Flag**: B10 (Flagged explicitly as a composite illustration rather than an individual historical incident; emphasizes the structural risk inherent in unmonitored joins).
8. **Your Turn**: BHTF (Prompt for students/practitioners to audit join drop rates and upstream row lineages before trusting summary statistics).
9. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats conform to strict course skepticism type specifications.
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); all durations measured and synchronized in `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 24fps (B01–B12) implementing the `collapse` move across upstream sources, join stages, survivor tables, and lineage audit frames.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to 4K (`3840×2160`), 24 fps, total runtime 189.5s.
- **Gate Audio**: PASS — `mean_volume: -23.9 dB`, `max_volume: -2.9 dB` (audible threshold > -40 dB verified).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography (EB Garamond / Helvetica), color palette (`#FAF9F5`, `#3D3929`, `#D97757`), margins, safe-insets, and readability.
- **Delivery**: Ready for two-target delivery packaging via `deliver.py`.
