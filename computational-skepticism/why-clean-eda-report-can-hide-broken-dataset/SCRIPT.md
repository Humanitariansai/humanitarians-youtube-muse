# Script: Why a Clean EDA Report Can Hide a Broken Dataset

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "is the dataset complete?", corrects to "can it still destroy your model?".
**Narration**:
"An exploratory data analysis report comes back spotless: zero missing values, clean distributions, no outliers. You assume the dataset is complete. It might not be. In fact, it could destroy your deployment. Let's see why."

## B01 — stakes (The Spotless Report)
**Visual**: Manim `B01Scene`. Clean dataset dashboard: 79,400 rows, 0% missingness badge, tidy bell curve histogram in ink, "REPORT: CLEAN" badge.
**Narration**:
"Picture a dataset assembled for machine learning: seventy-nine thousand four hundred rows, tidy formats, and zero obvious garbage. The exploratory analysis runs clean. Missingness is near zero, distributions are well-behaved, and every summary check reports success."

## B02 — stakes (The Production Breakdown)
**Visual**: Manim `B02Scene`. Deployment breakdown: clean validation curve -> production failure on subpopulation -> retraining and hyperparameter tuning yields 0% improvement.
**Narration**:
"The model trains cleanly and passes validation. But deployed in production, it repeatedly fails on a specific group of users. Retraining, tuning hyperparameters, and changing architectures change nothing. The dataset, looked at in isolation, still appears flawless."

## B03 — anchor planted (The Three Source Tables Funnel)
**Visual**: Manim `B03Scene`. THE ANCHOR: Three distinct source tables (Ticketing, Profiles, Transactions) funneling through a join into one combined table.
**Narration**:
"To see why, let's look at how the data was created. The final table was assembled by taking three separate source systems and joining them on a shared customer identifier into a single combined table."

## B04 — wrong guess (Zero Missingness = Full Coverage)
**Visual**: Manim `B04Scene`. Naive assumption card: 0% missing values in EDA directly equated to 100% population coverage.
**Narration**:
"Intuition assumes that because the missing-value check found zero empty cells in the table, the dataset captured everyone who was supposed to be there."

## B05 — break it (The Silent Join Drop)
**Visual**: Manim `B05Scene`. Falsification: 4% join drop rate highlighted in terracotta at the join funnel; unjoined rows fall out into the void.
**Narration**:
"That assumption collapses the moment you examine the join. Four percent of the records failed to match across all three source systems and were silently dropped before the table was ever created."

## B06 — mechanism (Inconsistent Identifiers & Selective Drop)
**Visual**: Manim `B06Scene`. Identifier format mismatch: Standard IDs vs Legacy IDs. The legacy subpopulation suffers 100% join failure.
**Narration**:
"A four percent loss sounds minor if spread evenly. But it was not even. One specific subpopulation had inconsistent identifier formatting in an older source system. Nearly all of their records failed the join and were erased."

## B07 — mechanism: collapse (The Funnel Collapse)
**Visual**: Manim `B07Scene`. MANIM MOVE `collapse`: Three incoming streams collapse into one output table; unmatched records from the legacy stream collapse outward and vanish into empty space.
**Narration**:
"When the join collapses multiple tables into one, unmatched rows do not leave behind blank entries. They vanish completely. The training set never saw them, so the model never learned how to serve them."

## B08 — anchor payoff (Survivors Call Themselves the World)
**Visual**: Manim `B08Scene`. THE ANCHOR PAYOFF: EDA diagnostic lens scans only the interior of the surviving table; reports "0.0% Missing", oblivious to the dropped rows outside.
**Narration**:
"Now bring back the exploratory data report. The histograms, summary statistics, and missing-value checks only examine the surviving rows inside the table. They cannot detect missingness in records that do not exist."

## B09 — anchor payoff (Residue vs Population)
**Visual**: Manim `B09Scene`. 79,400 rows labeled as "Residue of a Pipeline Filter", contrasted with "The Real Population".
**Narration**:
"Seventy-nine thousand four hundred rows was never a census of the real world. It was simply the residue of an upstream filtering process that nobody audited."

## B10 — one flag (Composite Illustration / Internal Pipeline Scope)
**Visual**: Manim `B10Scene`. THE ONE FLAG banner: "FLAG: COMPOSITE MECHANISM". Unmonitored pipeline joins vs end-to-end row count tracking.
**Narration**:
"One flag — this example is a composite illustration of silent join failure. When pipelines track and log raw source row counts end-to-end, join drop rates become immediately visible before model training begins."

## B11 — direction A (Clean EDA ≠ Complete Dataset)
**Visual**: Manim `B11Scene`. SPOTLESS EDA REPORT -> COMPLETE DATASET struck through with a heavy terracotta bar.
**Narration**:
"So a spotless exploratory report does not prove your dataset is complete. Standard summary statistics can only tell you about consistency within the rows that survived the pipeline."

## B12 — direction B (EDA is Still Essential)
**Visual**: Manim `B12Scene`. EDA Scope Card: Catches corrupt types, invalid values, and internal distribution skew, but bounded strictly by table boundaries.
**Narration**:
"And yet exploratory analysis is not useless. It catches corrupt types, impossible values, and extreme outliers. But its vision stops at the table's edge — it cannot see what was never recorded."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"You cannot compute the missingness of rows that never made it into the dataset — every diagnostic reads only the survivors and calls them the world."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take an assembled dataset in your current pipeline. Before running any summary statistics, trace its row count back to the original source tables. Calculate the exact drop rate at every join, and check if dropped records cluster in a specific subpopulation. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Why a Clean EDA Report Can Hide a Broken Dataset. Liam, in for Bear."
