# Storyboard — How Do You Know an AI Is Right?

_Fellow: Asavari (Ash) Shejwal · AI / STEM · 2026-08-14 · 16:9 + 9:16_

Brutalist explainer, framework-first (PROOF standard). One visual per beat; automated narration.

## Beat 1 — AI ACCOUNTABILITY

**On screen:** How Do You Know an AI Is Right?

**Narration:** Every AI demo looks impressive. That is exactly the problem. Looking good and being right are different things, and telling them apart is called evaluation. Here's the core move. You cannot know a model is right by admiring its output. You need something to compare it against, an answer key, and crucially, you have to write that key before you see the model's answer. Otherwise you'll just rationalize whatever it gave you.

## Beat 2 — THE PROBLEM

**On screen:** Grading by vibes rewards confidence, not correctness.

**Narration:** Here's why vibes fail. When you judge an answer by reading it, you reward the things that are easy to fake. Fluency, confidence, official sounding citations. None of those are correctness. A model that has learned to sound thorough will pass your gut check while being wrong, and you'll approve it, because it pattern matches to good. Confidence is cheap to manufacture. Correctness is not.

## Beat 3 — THE MECHANISM

**On screen:** Write the key first. Let something independent grade.

**Narration:** So here's the mechanism. First, write the answer key, the ground truth, before the model runs, so it can't be contaminated by what the model happens to say. Second, let something independent do the grading. The thing being tested cannot also be its own judge, or it will share its own blind spots. If a model checks its own work, it grades against its own assumptions and passes. An independent key, written first, catches the errors the model can't see in itself.

## Beat 4 — THE LIMIT

**On screen:** A metric you can game is a metric you will game.

**Narration:** One important limit. An evaluation is only as good as its answer key. If the key is easy, or if you keep tuning the model against the same test until it passes, you get a great looking score that means nothing in the real world. The test set has to be honest. Held out, representative, and hard enough to actually distinguish right from wrong. A number you optimized directly against is not evidence. It's a mirror.

## Beat 5 — THE TAKEAWAY

**On screen:** Trust the score, not the show.

**Narration:** So the takeaway. Before you trust an AI system, look past the demo and ask for the evaluation. Is there an answer key, written before the model's output? Is the grader independent of the model? Could the test have been gamed? And would the result survive on data the model has never seen? A convincing demo is a show. A real evaluation is evidence. Ask for the evidence.
