# Script: Why a 99%-accurate test is wrong about almost everyone it flags

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "99% likely", corrects to "almost certainly healthy".
**Narration**:
"Someone gets a positive result from a ninety-nine percent accurate test. Naturally, they assume they are ninety-nine percent likely to be sick. They're not. They are almost certainly healthy. Let's see why."

## B01 — stakes (The Harvard Problem)
**Visual**: Manim `B01Scene`. Test tube / screening icon, "99% accurate", Harvard study 95% guess in terracotta.
**Narration**:
"Imagine a screening test for a rare disease that affects one person in ten thousand. The test is ninety-nine percent accurate. You test positive. When doctors at Harvard were asked your chance of being sick, most guessed ninety-five percent."

## B02 — stakes (The Real Number)
**Visual**: Manim `B02Scene`. Bold typographic reveal: "≈ 1%". The 95-point gap between intuition and reality.
**Narration**:
"The actual answer is about one percent. Your intuition was off by two orders of magnitude, even though the test did exactly what the box promised."

## B03 — anchor planted (10,000 People)
**Visual**: Manim `B03Scene`. THE ANCHOR: 10,000-person dot grid on cream. 1 single terracotta dot (sick), 9,999 ink dots (healthy).
**Narration**:
"To see why, let's count people instead of probabilities. Picture ten thousand people arriving at a clinic. In that entire crowd, exactly one person actually has the disease. Nine thousand nine hundred and ninety-nine are completely healthy."

## B04 — wrong guess (Equal Weight Intuition)
**Visual**: Manim `B04Scene`. Naive mental model: 99% accuracy mapped straight to 99% true positives.
**Narration**:
"Intuition assumes that because the test is ninety-nine percent accurate, ninety-nine percent of the positive flags must belong to sick people."

## B05 — break it (Two Unequal Pools)
**Visual**: Manim `B05Scene`. Falsification: splitting the population into two starkly unequal pools (1 vs 9,999).
**Narration**:
"That breaks the moment you split the crowd into its two real pools: the one person who is sick, and the huge crowd that isn't."

## B06 — mechanism (The Sick Pool)
**Visual**: Manim `B06Scene`. The 1 sick person tested: 99% accuracy catches them → 1 True Positive.
**Narration**:
"Start with the sick pool. There is only one sick person. The ninety-nine percent accurate test catches them. That gives us exactly one true positive."

## B07 — mechanism: accumulate (The Healthy Pool)
**Visual**: Manim `B07Scene`. MANIM MOVE `accumulate`: Across the 9,999 healthy grid, 1% errors accumulate dot by dot into ~100 False Positives.
**Narration**:
"Now look at the healthy pool. Nine thousand nine hundred and ninety-nine people. The test gets ninety-nine percent of them right, but it fails on one percent. One percent of nearly ten thousand people is roughly one hundred false positives."

## B08 — anchor payoff (The Pool of Flags)
**Visual**: Manim `B08Scene`. Gathering all flags: 1 True Positive + 100 False Positives = 101 Total Positives.
**Narration**:
"Now gather every positive result in the clinic. You have one true positive from the sick person, and one hundred false alarms from the healthy crowd. That's one hundred and one positive flags in total."

## B09 — anchor payoff (1 in 101)
**Visual**: Manim `B09Scene`. Random draw from the positive pool: 1 / 101 ≈ 0.99% (< 1%).
**Narration**:
"If you hold a positive test slip, you are simply one person in that pool of one hundred and one. The chance you are the single sick individual is one out of one hundred and one — less than one percent."

## B10 — one flag (Screening vs Clinical Context)
**Visual**: Manim `B10Scene`. THE ONE FLAG: Broad population screening vs symptomatic patient referral.
**Narration**:
"One flag — this arithmetic applies to general screening across the whole population. If a patient comes in already exhibiting classic symptoms, their prior odds are much higher, and the positive test carries far more weight."

## B11 — direction A (Positive ≠ Proof)
**Visual**: Manim `B11Scene`. POSITIVE TEST → HAS DISEASE struck through with terracotta.
**Narration**:
"So a positive flag from an accurate model does not prove the condition is present. When base rates are tiny, sheer population size overwhelms classifier accuracy."

## B12 — direction B (Positive ≠ Useless)
**Visual**: Manim `B12Scene`. 1 in 10,000 → 1 in 100 (100× probability update arrow).
**Narration**:
"And yet a positive test is not useless either. It raised that patient's probability of disease a hundred-fold, from one in ten thousand up to one in a hundred."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"When what you're looking for is rare, the healthy population manufactures more false positives than the sick population can manufacture true ones."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take an AI detection system in your domain — a fraud detector, a spam filter, or a security scanner. Look up its claimed accuracy, and then find the true background rate of incidents in production. Calculate the ratio of true alerts to false alarms. Run that calculation before your next deployment review. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Why a 99%-accurate test is wrong about almost everyone it flags. Liam, in for Bear."
