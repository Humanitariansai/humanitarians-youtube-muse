# The average that never settles

You have averaged a thousand data points from an AI system's production run — and the very next point moves your average as if you had barely started.

Standard statistics promises that as sample size $ grows, the sample mean converges to a stable, predictable center. But the Central Limit Theorem requires two conditions: independence and finite variance. In heavy-tailed, Cauchy-like worlds where variance is infinite, extreme outliers overpower the historical sample, and the sample mean never converges. Evaluating an AI deployment on average loss measures a quantity that does not exist.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam demonstrate why averages fail to settle by racing Gaussian and Cauchy running-mean traces side by side.

---

### Key Takeaways & Carry-Out
- **The Core Mechanism**: The Central Limit Theorem requires finite variance. When variance is infinite or undefined (heavy tails), extreme deviations do not get diluted by $ — they dominate the entire sum.
- **The Visual Demonstration**: Watching Gaussian vs. Cauchy running means up to  = 2,000$ shows the Gaussian mean razor-flat at zero, while the Cauchy mean lurches and wanders forever.
- **Carry-Out Law**: When variance is infinite, the sample mean never converges — so evaluating a system on average loss measures a quantity that does not exist.
- **Direction A**: A stable historical mean over thousands of steps does NOT prove finite variance; a heavy-tailed system can look placid right before an extreme jump.
- **Direction B**: When dealing with consequence systems and heavy tails, abandon average loss and switch to tail-aware tools: medians, max-loss bounds, and adversarial stress testing.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take the evaluation metrics for your current AI deployment. Identify whether the loss of being wrong has a hard ceiling or if extreme tail events are possible. If extreme costs exist, replace your aggregate mean with a median and a ninety-ninth percentile worst-case audit.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Uncertainty & Probability
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 2: Probability, Uncertainty, and the Confidence Illusion)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/average-that-never-settles
