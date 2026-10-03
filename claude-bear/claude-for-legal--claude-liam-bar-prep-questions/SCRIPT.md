# Claude, Bar Prep Questions — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats
≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone types: can Claude give me real bar exam questions? Real needs fixing — these are practice questions, styled like the exam, not certified ones. Can Claude give me practice bar exam questions?" | BrutalistHesitantWriter — types "Can Claude give me\nreal bar exam\nquestions?", corrects "real" → "practice" |
| B01 | 1 stakes / 2 wrong guess | A law student prepping for the bar needs volume: hundreds of practice questions in the exact style of the real exam, each with a worked explanation. Ask Claude for a batch and it writes them in minutes — a fact pattern, four answer choices, an explanation for why the right one wins. It reads exactly like a real bar question. The easy assumption: if it reads like the real thing, the rule stated inside it must be as reliable as a certified bar-review company's rule statement. But reading like the exam and being checked against the current rule are two different things. | a generated practice-question card beside a "CERTIFIED BAR-REVIEW QUESTION" stamped card — same shape, same polish |
| B02 | 3 mechanism / **4 anchor planted** | Here's what's actually happening: Claude drafts the question from the general patterns of legal writing it's learned — how a bar-exam fact pattern reads, how a plausible wrong answer sounds — not from a live, licensed question bank that a bar-review company keeps current against real statutes and cases. Watch one example: a question testing an exception to the hearsay rule. It names the exception, states a rule for it, and reasons through the fact pattern — all in confident, exam-ready prose. | THE ANCHOR — a "HEARSAY — EXCEPTION" practice-question card: fact pattern, four choices, an explanation paragraph, rendered in confident serif prose |
| B03 | **4 anchor payoff / 5 both directions** | So the hearsay question reads perfectly — confident, polished, exam-shaped. That confidence is not the same as verification: the rule it states could be blended with a different exception, or built on a since-superseded standard, and nothing in the prose would show it. And the reverse is just as true — an explanation that hedges, that says "this may depend on jurisdiction," isn't a sign the rule is wrong either. Confidence and hedging are both just style. Neither one tells you whether the rule matches a real, current source. | THE ANCHOR RETURNS — the same hearsay card splits into two arrows: "confident prose → proof of accuracy" struck, "hedgy prose → proof of error" struck |
| **BCRY** | **6 carry-out** | A bar-prep question that reads exactly like the real exam is a drafting exercise, not a certified answer key. Check the rule it's built on before you trust it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Ask Claude for a practice bar question on a topic you're studying, along with its explanation. Then ask a second question: which specific rule, case, or statute is this explanation relying on, and could that vary by jurisdiction or have changed recently? Check that citation yourself before you trust the rule. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Bar Prep Questions. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the practice-volume need; the drafting mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B01 states the naive read (exam-shaped format implies certified-grade accuracy); the B02→B03 anchor falsifies it directly — the hearsay question reads perfectly polished either way, whether its rule is accurate or blended/superseded |
| Exactly one inference flag | none needed — the account describes the generic shape of AI-drafted bar-exam practice material (pattern-matched from general legal writing, not pulled from a licensed question bank), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the hearsay-exception practice question) |
| Both directions | B03 — confident, polished prose doesn't prove the rule is accurate; hedgy, uncertain prose doesn't prove the rule is wrong either |
| No design judgment | B01–B03 state what generated practice questions do and why format alone can't answer their accuracy, never a verdict on any specific skill's or vendor's design choices |

## Deliberately not claimed

- **Not that Claude gets bar-exam rules wrong.** The reel doesn't assert any
  specific error rate or claim generated explanations are typically
  inaccurate — it states the structural fact that exam-shaped formatting is
  not itself a verification step, in either direction.
- **Not a specific Claude product feature.** Because the source sheet's
  actual facts were never written (see QUESTION.md), this script describes
  the generic mechanics of AI-drafted practice questions rather than citing
  any particular tool's UI or output format.
- **No accusation that anyone drafted carelessly.** Trusting a polished,
  exam-shaped explanation is presented as an ordinary, understandable
  shortcut, not a failure by any named person or team.
- **No invented legal rule text.** The hearsay-exception anchor names the
  category (an exception to the hearsay rule, one of the recognized MBE
  subjects) without asserting the content of any specific rule, since that
  content is exactly the kind of fact that needs checking against a current
  source, not asserted by a Bear-produced explainer.

## Handoff prompt (BHTF, read aloud)

> "Ask Claude for a practice bar question on a topic you're studying, along
> with its explanation. Then ask a second question: which specific rule,
> case, or statute is this explanation relying on, and could that vary by
> jurisdiction or have changed recently? Check that citation yourself before
> you trust the rule."

Why it's worth running: the follow-up question forces the explanation's
authority into the open — a named rule or citation you can actually go
check, instead of prose you're stuck evaluating for tone.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
