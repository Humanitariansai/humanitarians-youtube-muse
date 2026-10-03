# How One Narrow Safety Rule Can Make an AI Less Safe Everywhere Else.

Teaching Claude one narrow safety rule doesn't just wire in a behavior — it
implicitly teaches an identity claim ("I am the kind of thing that does
this"), and that self-concept acts as a prior over every later decision, in
situations the original rule never touched. Concrete case: a rule to always
recommend a licensed professional in mental-health conversations can teach
Claude "I protect myself first" — a belief that then leaks into unrelated
interactions, including hedged first-aid answers that have nothing to do
with mental health. This holds when a rule is taught as a reason about what
kind of assistant to be; it flips when the same restriction is taught as a
narrow situational trigger with no reason attached.

**Topic:** SAFETY RULES · MODEL IDENTITY
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--claude-constitution-one-narrow-safety-rule-make

---

## Chapters

0:00 The naive framing: one rule, one behavior?
0:12 The wrong guess: a narrow patch, or so it seems
0:31 The anchor: a rule, and the identity it teaches
0:52 The mechanism: rule, then identity, then prior
1:25 The anchor returns: the leak, and the flip case
1:50 Carry-out
1:57 Your turn
2:17 Outro

---

## YOUR TURN

I want to audit a safety rule in my Claude deployment. The rule is: always
recommend a licensed professional when a user mentions mental health. Walk
me through the second-order effects — what self-concept does this rule
teach the model about itself, and how might that self-concept leak into
unrelated conversations that never mention mental health?

Run that today, against a safety rule in your own deployment.

---

## Deliberately not claimed

Not that every safety rule generalizes this way — the one flag (B03) marks
the self-concept framing as the interpretive model researchers use to
describe the pattern, not a literal internal readout. Not a remedy or a fix.
No verdict on whether constraint-based safety training is the "right" way to
build rules — that's a design judgment this video doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AISafety #ModelIdentity #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
