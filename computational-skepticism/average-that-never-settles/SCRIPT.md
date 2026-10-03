# Script: The average that never settles

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "always settle down", corrects to "sometimes wander forever".
**Narration**:
"If you collect enough observations, you assume the running average has to settle down. In our world, it often doesn't. Some averages wander forever. Let's see why."

## B01 — stakes (The Central Limit Promise)
**Visual**: Manim `B01Scene`. Dashboard with running sample mean formula, Gaussian silhouette, and the CLT convergence promise.
**Narration**:
"Standard statistics makes a seductive promise: add up enough independent random samples, and the average converges to a steady, predictable center. It's the foundation of benchmarks, dashboards, and error metrics."

## B02 — stakes (A Thousand Samples In)
**Visual**: Manim `B02Scene`. Running line chart showing 1,000 data points collected. The curve looks flat and stable.
**Narration**:
"You collect one thousand data points from your model's production run. The average looks rock-solid. You feel confident that you have measured the true baseline cost of an error."

## B03 — anchor planted (The Two Parallel Worlds)
**Visual**: Manim `B03Scene`. THE ANCHOR: Dual-panel arena on cream ground. Left: Gaussian World (Bell Curve). Right: Heavy-Tailed World (Cauchy).
**Narration**:
"To test that confidence, let's set up two parallel simulations: a well-behaved Gaussian world on the left, and a heavy-tailed Cauchy world on the right."

## B04 — wrong guess (The Illusion of Large N)
**Visual**: Manim `B04Scene`. Naive intuition diagram: dividing by N = 10,000 assumed to crush any single outlier into zero.
**Narration**:
"Intuition insists that no matter where data comes from, dividing by a huge number N will eventually crush any single outlier and force the running mean to freeze in place."

## B05 — break it (Point 1,001 Arrives)
**Visual**: Manim `B05Scene`. Falsification: Point 1,001 arrives. Gaussian stays flat; Cauchy jumps violently across the vertical axis in terracotta.
**Narration**:
"Now observation one thousand and one arrives in both worlds. In the Gaussian world, nothing flinches. In the heavy-tailed world, the average jumps across the screen as if you had barely started."

## B06 — mechanism (Why Gaussian Settles: Finite Variance)
**Visual**: Manim `B06Scene`. CLT condition card: Finite Variance sigma^2 < infinity. Exponential tail decay curve e^(-x^2/2).
**Narration**:
"Why did the two worlds split? The Central Limit Theorem requires two conditions: independence and finite variance. In the Gaussian world, extreme events become exponentially rare, so past points easily dilute new ones."

## B07 — mechanism (Why Cauchy Fails: Undefined Variance)
**Visual**: Manim `B07Scene`. Cauchy condition card: Variance undefined/infinite. Power-law 1/x^2 tail staying heavy. Single point outweighing 1,000 points.
**Narration**:
"In a heavy-tailed world, variance is infinite. Outliers are not rare exceptions that get diluted; they are heavy enough to overpower the entire historical sample, resetting the running average at any moment."

## B08 — anchor payoff / manim move: trace (The Two Traces Racing)
**Visual**: Manim `B08Scene`. MANIM MOVE `trace`: Side-by-side animated running mean traces racing from N=1 to N=2000. Gaussian stabilizes into a razor line; Cauchy jerks and lurches unpredictably.
**Narration**:
"Watch the two traces race side by side as sample size climbs to two thousand. The Gaussian trace settles into a razor-thin band. The Cauchy trace never settles — it wanders, lurches, and resets indefinitely."

## B09 — anchor payoff (Evaluating on a Ghost)
**Visual**: Manim `B09Scene`. AI model loss distribution card: 999 penny errors vs 1 database wipe. Average loss benchmark stamped with "ILLUSION: Mean does not converge".
**Narration**:
"This is not a mathematical curiosity. If your AI model's loss distribution is heavy-tailed — where most errors cost pennies but one in a thousand wipes a database — an average loss benchmark measures a number that does not exist."

## B10 — one flag (Physical Limits vs Consequence Tails)
**Visual**: Manim `B10Scene`. THE ONE FLAG: Physical systems (finite variance, CLT holds) vs Consequence systems (agentic actions, heavy tails, CLT fails).
**Narration**:
"One flag: physical measurements like height, weight, and sensor noise do have finite variance and settle cleanly. But systems involving catastrophic software failure, latency spikes, or real-world harm almost always live in the heavy tails."

## B11 — direction A (Stable Past ≠ Finite Variance)
**Visual**: Manim `B11Scene`. Direction A card: "STABLE HISTORICAL MEAN ≠ CONVERGED PROCESS" with a calm trace preceding an unexpected jump.
**Narration**:
"So a running average that looks stable over your historical dataset does not prove the process has finite variance. A heavy-tailed system can look placid for thousands of steps right before the next jump."

## B12 — direction B (Switch to Tail-Aware Audits)
**Visual**: Manim `B12Scene`. Direction B card: Arrow from Average Loss to Tail-Aware Toolkit: Medians, Max-Loss bounds, Adversarial Stress Testing.
**Narration**:
"And yet recognizing heavy tails does not mean you are helpless. It tells you to abandon average loss and switch to tail-aware tools: medians, worst-case stress testing, and adversarial audits."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"When variance is infinite, the sample mean never converges — so evaluating a system on average loss measures a quantity that does not exist."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take the evaluation metrics for your current AI deployment. Identify whether the loss of being wrong has a hard ceiling or if extreme tail events are possible. If extreme costs exist, replace your aggregate mean with a median and a ninety-ninth percentile worst-case audit. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"The average that never settles. Liam, in for Bear."
