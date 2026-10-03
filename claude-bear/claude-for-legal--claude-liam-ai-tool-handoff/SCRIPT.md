# When Does an AI Handoff Actually Finish? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone hands Claude a contract redline and figures the job is finished the moment it comes back. Wrong word — it isn't finished, it's just started. Liam, take them through it." | BrutalistHesitantWriter — types "Can I just have Claude finish this contract redline?", corrects "finish" → "start" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's tempting to treat "Claude delivered it" as "the job is done." But say the instruction itself was wrong — redline every use of the word "Vendor," when only one specific vendor's name should change. Claude will redline every one, correctly, exactly as asked. The output is flawless, and the contract is now wrong, because nothing paused to check the instruction before it shipped. | a contract page; every instance of one word gets marked, cleanly and correctly; a caption reveals the instruction itself was the error |
| B02 | 3 mechanism / **4 anchor planted** | A handoff that actually works has three parts: a scope — exactly what's being asked — a boundary — the point where a human has to confirm before anything counts as final — and a record of what changed. Watch the anchor: that same contract redline comes back from Claude with every changed clause marked in the margin. Not accepted. Marked. | three labeled parts lighting in turn (scope / boundary / record); THE ANCHOR — a redlined contract page, clauses marked, stamped "MARKED — NOT ACCEPTED" |
| B03 | **4 anchor payoff / 5 both directions** | The lawyer opens that same redline, checks every marked clause against the record instead of rereading the whole contract cold, and only then does it become final. But a redline nobody commented on isn't automatically approved — silence isn't a signature, somebody still has to say yes. And a redline that gets heavily rewritten isn't a failure either — a clean first pass and a rewritten one can both be the handoff working exactly as intended. | THE ANCHOR RETURNS — the marked page gets a human signature stamp and becomes "FINAL"; then splits into "silence ≠ approval" and "rewritten ≠ failure" |
| **BCRY** | **6 carry-out** | The handoff isn't done when Claude finishes — it's done when a person signs off on what comes back. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Take one document you're reviewing right now. Ask Claude to make exactly one change — a single clause, a single term. When it comes back, check the marked change against your instruction line by line before you accept anything. That's the whole handoff: one scope, one boundary, one signature. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | When Does an AI Handoff Actually Finish? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the delivery-vs-completion gap; the three-part mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (finished the moment it's returned); B01 falsifies it with a concrete case — a wrong instruction executed perfectly still ships the mistake |
| Exactly one inference flag | none needed — the account describes the generic shape of a working handoff (scope / boundary / record), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the marked-not-accepted redline becomes the signed-final redline) |
| Both directions | B03 — no comments doesn't prove approval (silence isn't a signature); heavy rewriting doesn't prove failure (a clean pass and a rewritten one are both the handoff working) |
| No design judgment | B01–B03 state what a handoff needs and why, never a verdict on whether any specific skill or tool was well designed |

## Deliberately not claimed

- **Not that Claude made an error.** B01's case is an instruction error, executed
  correctly — the reel never claims the tool did anything wrong.
- **Not a specific Claude product feature.** Because the source sheet's actual facts
  were never written (see QUESTION.md), this script describes the generic mechanics of
  an AI-tool handoff (scope, boundary, record) rather than citing any particular skill's
  steps or output format.
- **No accusation that anyone was negligent.** The unchecked instruction in B01 is
  presented as an ordinary risk of any handoff, not a failure by a named person or team.

## Handoff prompt (BHTF, read aloud)

> "Take one document you're reviewing right now. Ask Claude to make exactly one change —
> a single clause, a single term. When it comes back, check the marked change against
> your instruction line by line before you accept anything."

Why it's worth running: it forces the scope down to one checkable thing, so the review
step (the boundary the reel is built around) takes minutes instead of a full re-read.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
