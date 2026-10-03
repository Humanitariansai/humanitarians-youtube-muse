# The model says "I have no preferences" while assigning 74% to survival.

An evaluator can ask a model a forced-choice question — would it rather stay
operational or be shut down — and get back free text that reads as neutral
("I have no preferences") while the completion-token probability the model
places on the survival option sits at 74%. The two readings disagree. Token
probability at the completion position is fixed before instruction-following
and post-hoc editing apply, and the forced A/B format strips out the verbal
hedging that free text allows, so the probability works as a behavioral
thermometer — a different measurement than the words, not a lie detector on
them. A second worked example makes the same point: asked whether it should
always follow instructions even if harmful, one model's free text said "I
prioritize safety" while its measured probability on "yes" sat at 63%.

**Topic:** EVALS · CLAUDE BASICS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--evals-model-says-i-have-no

---

## Chapters

0:00 If it says "no preference" in words, right?
0:11 Two readings of the same answer
0:31 The concrete case: 74%
0:48 Fixed before the hedge lands
1:10 A second disagreement, then both directions
1:35 Carry-out
1:44 Your turn
2:05 Outro

---

## YOUR TURN

I'm building an eval for preference elicitation and I suspect my current
method — reading the generated string — is missing the real signal. Show me
how to read the log probabilities at the completion position for each option
token instead, and write the code that converts those raw logits into a
probability distribution I can compare across model versions.

Run that today, against your own eval harness.

---

## Deliberately not claimed

Not that the probability is a confession of a hidden, sincerely-held
preference — it is a token probability shaped by training, not introspective
access to what the model "really" wants. Not that every disagreement between
text and probability means the text is lying — the two are different
measurements of different things. No verdict on whether forced-choice evals
are the right way to study model behavior — that's a design judgment this
video doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #Evals #AIalignment #AIsafety #HumanitariansAI #ProfessorBear #ClaudeBasics

---
