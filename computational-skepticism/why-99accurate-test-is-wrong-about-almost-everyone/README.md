# Why a 99%-accurate test is wrong about almost everyone it flags

A screening test or AI classifier is 99% accurate and returns positive — yet the flagged person almost certainly does not have the condition. 

When a condition is rare (such as 1 in 10,000), the massive healthy population manufactures far more false alarms than the tiny sick population can manufacture true positives. Even with 99% accuracy, 99 out of 100 positive flags are false alarms.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam break down the base-rate mechanism by counting people rather than manipulating formulas.

---

### Key Takeaways & Carry-Out
- **The Core Mechanism**: In 10,000 people with 1 sick individual, a 99% accurate test catches the 1 sick person (1 True Positive) and misflags 1% of the 9,999 healthy people (~100 False Positives).
- **The Posterior Odds**: Handed a positive slip, the odds of being the sick person are 1 in 101 (less than 1%).
- **Carry-Out Law**: When what you're looking for is rare, the healthy population manufactures more false positives than the sick population can manufacture true ones.
- **Direction A**: A positive result from a high-accuracy classifier is NOT proof of the condition when the base rate is low.
- **Direction B**: A positive result is NOT useless — it updated the prior probability a hundred-fold (from 1:10,000 to 1:100).

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take an AI detection system in your domain — a fraud detector, a spam filter, or a security scanner. Look up its claimed accuracy, and then find the true background rate of incidents in production. Calculate the ratio of true alerts to false alarms. Run that calculation before your next deployment review.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Uncertainty & Probability
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 2: Probability, Uncertainty, and the Confidence Illusion)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/why-99accurate-test-is-wrong-about-almost-everyone
