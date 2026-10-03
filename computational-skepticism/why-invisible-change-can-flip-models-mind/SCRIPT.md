# Script: Why an Invisible Change Can Flip a Model's Mind

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "random noise", corrects to "accumulated linear math".
**Narration**:
"Someone sees an image flipped by an invisible perturbation and assumes the model is hallucinating on random noise. It isn't. The math is completely systematic. Let's see why."

## B01 — stakes (The Clean Panda)
**Visual**: Manim `B01Scene`. Clean image of panda, classifier prediction "Panda" (57.7% confidence), noise pattern overlay ($\epsilon = 0.007$).
**Narration**:
"In 2014, researchers showed an image classifier a photo of a panda. It predicted panda with fifty-eight percent confidence. Then they added a faint pattern of noise — so subtle that to human eyes, the picture was identical."

## B02 — stakes (The Gibbon Flip)
**Visual**: Manim `B02Scene`. Perturbed image, classifier prediction flipped to "Gibbon" (99.3% confidence). The 57.7% -> 99.3% flip badge.
**Narration**:
"To a person, the panda hasn't moved a millimeter. But the model looked at the perturbed image and predicted gibbon — with over ninety-nine percent confidence. An invisible change flipped the model's entire classification."

## B03 — wrong guess (The Random Noise Fallacy)
**Visual**: Manim `B03Scene`. Random noise vectors canceling out ($\sum \delta_i \approx 0$) vs aligned perturbation.
**Narration**:
"The natural reaction is to assume the model is fragile or broke on random glitching. But if the noise were truly random, the pushes would cancel each other out. Something far more structured is happening."

## B04 — mechanism (Linear Scoring)
**Visual**: Manim `B04Scene`. $f(x) = w^T x = \sum w_i x_i$. Inputs $x$, weights $w$, dot product score relative to decision threshold.
**Narration**:
"Consider how a linear layer scores an input. It takes every input feature, multiplies it by a learned weight, and sums them up. If the total score exceeds a threshold, the model predicts one class over another."

## B05 — mechanism (The Perturbation Budget)
**Visual**: Manim `B05Scene`. Input perturbation $x_{new} = x + \delta$. Max coordinate constraint $\|\delta\|_\infty \le \epsilon$ (e.g. $\epsilon = 0.007$).
**Narration**:
"Now introduce a tiny change, delta. To keep the change invisible to human vision, no single pixel value is allowed to change by more than a tiny budget, epsilon — say, less than one percent brightness."

## B06 — mechanism (Sign Alignment)
**Visual**: Manim `B06Scene`. Attacker sets $\delta = \epsilon \cdot \text{sign}(w)$. Every coordinate aligns with weight sign ($+w \to +\epsilon$, $-w \to -\epsilon$).
**Narration**:
"Instead of choosing random noise, the attacker aligns every single coordinate with the model's weights. If a weight is positive, add epsilon. If a weight is negative, subtract epsilon. Every single coordinate is pushed in the exact direction that increases the activation."

## B07 — anchor / manim move: accumulate (The L1 Accumulation)
**Visual**: Manim `B07Scene`. MANIM MOVE `accumulate`: Running-sum bar growing as thousands of tiny per-coordinate pushes are added one by one.
**Narration**:
"Look at the mathematics of that sum. The change in the model's score is epsilon times the sum of the absolute weights. In a single coordinate, the push is imperceptible. But across a million pixels, those tiny pushes do not cancel — they accumulate."

## B08 — anchor payoff (Crossing the Decision Threshold)
**Visual**: Manim `B08Scene`. The running-sum bar sweeps across the decision threshold into the Gibbon classification region ($+ \epsilon \|w\|_1 \gg \text{threshold}$).
**Narration**:
"In a high-dimensional image with a million numbers, a nudge of less than one percent per pixel adds up to a massive shift of thousands of units in total score. The running sum blasts past the decision threshold."

## B09 — one flag (Piecewise Linearity & Deep Networks)
**Visual**: Manim `B09Scene`. THE ONE FLAG: Piecewise linear activations (ReLU) mean deep networks behave like high-dimensional linear planes locally.
**Narration**:
"One flag — neural networks are non-linear, but modern architectures rely on piecewise linear units like ReLU. Locally, their loss surfaces behave like high-dimensional linear planes, leaving them exposed to the exact same linear accumulation."

## B10 — direction A (Invisible to Eyes)
**Visual**: Manim `B10Scene`. Direction A: $\|\delta\|_\infty \le \epsilon$ (tiny per pixel, human retina cannot detect).
**Narration**:
"So in one direction, the perturbation is genuinely invisible. No individual pixel shifts enough for human biology to register any change."

## B11 — direction B (Decisive to Model)
**Visual**: Manim `B11Scene`. Direction B: $\Delta f = \epsilon \|w\|_1$ (massive total activation shift, completely flips classifier).
**Narration**:
"Yet in the other direction, the mathematical shift is overwhelming. High dimensions turn millions of unnoticeable nudges into an irresistible force."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"In a million-dimensional space, an invisible nudge on every coordinate accumulates into a decisive shift across the whole model."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take an image classifier or embedding model in your stack. Calculate the L-one norm of its first layer weights across input dimensions. Multiply by an epsilon of one two-hundred-and-fifty-fifth. See how large an activation shift an aligned adversary can generate without changing a single visible pixel. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Why an Invisible Change Can Flip a Model's Mind. Liam, in for Bear."
