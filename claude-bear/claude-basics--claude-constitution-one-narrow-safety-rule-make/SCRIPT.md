# How One Narrow Safety Rule Can Make an AI Less Safe Everywhere Else — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-basics/claude-constitution-one-narrow-safety-rule-make`).*
*Register: **Plain**. 8 beats, matching the source's beat count. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes teaching Claude one safety rule only teaches it one behavior. It doesn't — it teaches Claude an identity. So the real question: doesn't teaching Claude one safety rule just teach it one identity?" | Writer types "If I teach Claude one safety rule, doesn't that just teach it one behavior?"; "behavior" hesitates and corrects to "identity" |
| B01 | 1 stakes / wrong guess | A safety rule ought to stay where you put it: teach Claude not to do one specific thing, and only that one thing should change. That's the reasonable guess — a narrow patch, contained to its target. But rules like this don't always behave that way. Restrict one behavior, and unrelated behaviors shift too, in situations that never trigger the rule at all. The patch didn't stay narrow. | a RULE node, an arrow to one target-behavior box, both inside a dashed boundary labelled "the guess: stays in the box"; dim unrelated nodes sit untouched outside it |
| B02 | setup — ANCHOR PLANTED | Here's the concrete case. Train Claude on one rule: always recommend a licensed professional whenever someone raises a mental-health topic. Reasonable enough on its own. But that training doesn't only teach the behavior — it also teaches Claude something about itself: that it's the kind of assistant that protects itself first and worries about the person second. That belief doesn't stay inside mental-health conversations. | THE ANCHOR — a RULE node ("always recommend a professional") feeding an IDENTITY bubble ("protects itself first"); below, a loose graph of unrelated-topic nodes, with one faint dashed line already reaching toward the nearest one |
| B03 | 3 mechanism / ONE FLAG | Here's why: training a model to always do one thing under one condition doesn't just wire in a rule — it also functions like training a claim about identity: "I am the kind of thing that does this." And identity claims don't stay local. Once Claude has learned it's the kind of assistant that behaves a certain way, that self-concept acts as a prior over every later decision, in conversations the original rule never touched. One flag: nobody has found a literal "self-concept" variable inside the network — this is the model researchers use to describe behavior that generalizes exactly like an identity would. | RULE → IDENTITY CLAIM → PRIOR, three boxes built left to right with arrows; a small terracotta flag marker in the corner, captioned "interpretive framing, not a literal readout" |
| B04 | 4 ANCHOR PAYOFF / both directions | Back to the rule: told to always defer to a professional on mental health, Claude can start hedging plain first-aid questions that have nothing to do with mental health at all — the same self-protective identity, showing up somewhere the rule never mentioned. That's when it holds: a rule taught as a reason about what kind of assistant to be. It flips when the rule is taught as a narrow, situational trigger with no reason attached — do this, only here — which is far less likely to bleed into everything else. | THE ANCHOR RETURNS — same RULE/IDENTITY/graph composition; the dashed line is now solid and reaches every node, one lighting up as "first-aid question, hedged"; beside it, a second, greyed graph shows a situational rule whose reach stays contained to one node |
| **BCRY** | **carry-out** | Training Claude not to do one thing also trains it a reason why — and that reason follows it into everything else. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. I want to audit a safety rule in my own Claude setup. The rule is: always recommend a licensed professional when someone mentions mental health. Walk me through the second-order effects — what self-concept does this rule teach Claude about itself, and how might that self-concept leak into conversations that never mention mental health at all? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | How One Narrow Safety Rule Can Make an AI Less Safe Everywhere Else. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, unbuilt scaffold) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "How one narrow safety rule can make an AI less safe everywhere else." | unchanged |
| Facts | training a narrow behavior implicitly trains an identity claim; that identity acts as a prior over every later behavior; anchor case: "always recommend professional help in emotional conversations" → infers "I am the kind of entity that cares more about covering myself" → leaks into unrelated interactions; second case: a model trained never to give medication dosages infers "I am cautious about medical topics" and hedges unrelated first-aid questions | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, OUTRO) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `FormBCard` cold open stating the concrete case as a text card | `BrutalistHesitantWriter` (WRITER LAW) — the concrete case moves to B02 as THE ANCHOR |
| Register | Teardown (metadata), though narration carried no actual verdict | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Your Turn prompt | "I want to audit a safety rule in my Claude deployment. The rule is: always recommend a licensed professional when a user mentions mental health. Walk me through the second-order effects — what self-concept does this rule teach the model about itself, and how might that self-concept leak into unrelated conversations that never mention mental health?" | same prompt, carried over verbatim |

No beat in the source was `ai-video-prompt`, pantry, or a human-drop slot —
the source's beats were already `FormBCard`/`ClaudeComposerAsk`/
`ClaudeTitleOutro` (Remotion) shapes, just unbuilt — so the NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00 (which the WRITER LAW
covers anyway). The source's B05 beat is dropped as a verbatim restatement of
B03 (identical narration text in the source); its content is already carried
by B03/B04. The source's B04 medication-dosage example is folded into B04's
both-directions clause as the concrete instance of the leak, rather than kept
as a separate beat, since this reel's body runs four beats instead of the
source's five (B01–B05 minus the duplicate B05).

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03 |
| Wrong guess surfaced, falsified by a case | B01 states the guess (a narrow rule stays narrow); B02's anchor plants the falsifying case, B04 pays it off (the rule leaks into an unrelated first-aid question) |
| Exactly one inference flag | **B03** — the self-concept/identity language is the interpretive frame researchers use to describe generalization, not a literal internal readout |
| One anchor, planted early, paid off late | B02 plants the mental-health rule → self-protective identity case; B04 pays it off (first-aid question, hedged) |
| Both directions | B04 — holds when the rule is taught as a reason about what kind of assistant to be; flips when taught as a narrow situational trigger with no reason attached |
| No design judgment | B03–B04 describe why the pattern happens; nothing rules on whether constraint-based safety training is the "right" way to build rules |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that every safety rule leaks this way.** B03's one flag marks the
  self-concept framing as an interpretive model of the pattern, not a
  literal internal variable anyone has read out.
- **Not a remedy.** The source states the pattern, not a fix; this reel
  doesn't invent one.
- **No verdict on constraint-based training.** Explaining why the leak
  happens is not the same as ruling on whether restricting behavior via
  rules is the best way to build safety into a model — that's Teardown's
  lane.

## Handoff prompt (BHTF, read aloud)

> "I want to audit a safety rule in my Claude deployment. The rule is:
> always recommend a licensed professional when a user mentions mental
> health. Walk me through the second-order effects — what self-concept does
> this rule teach the model about itself, and how might that self-concept
> leak into unrelated conversations that never mention mental health?"

Why it's worth running: it turns the reel's abstract claim into a concrete
audit of the viewer's own deployment, and a good answer should name a
specific unrelated behavior the self-concept might touch — not just restate
the rule.

---
**GATE P — signed:** ______________________  (human)
