# Claude, Amendment History — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats
≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone reads a contract and assumes the original signed document still governs. It doesn't — every amendment since has changed what's actually in force. The real question: what does the contract say, now?" | BrutalistHesitantWriter — types "What does\nthe original\ncontract say?", corrects "original" → "current" |
| B01 | 1 stakes / 2 wrong guess, falsified | A contract gets signed, then amended twice over the next two years — a notice period changed once, a renewal date changed again. Ask what it says today, and the easy move is to pull up the original signed document. But the original only ever says what it said on day one. It has no way of knowing anything came after it. | an original-contract card stamped "DAY ONE"; two amendment chips slide past it, dim and disconnected, never touching it |
| B02 | 3 mechanism / **4 anchor planted** | Amendment history walks that chain in order, and for any one clause, only the most recent edit counts — not the sum of every edit, just the last one. Watch one clause: a lease's notice period. The original contract set it at thirty days. The first amendment stretched it to sixty. The second amendment cut it back to forty-five. | THE ANCHOR — three cards in a row (original / amendment 1 / amendment 2), each overwriting the same "NOTICE:" field: 30 → 60 → 45 |
| B03 | **4 anchor payoff / 5 both directions** | So today, notice is forty-five days — not thirty, not sixty, whichever edit landed last, and only for that one clause. A clause no amendment ever touched isn't missing from this picture — the original wording is still what's in force. And an amendment existing somewhere in the file doesn't mean it touched the clause you're asking about. You still have to follow that clause's own chain, not just the contract's. | THE ANCHOR RETURNS — the 45 card locks in and highlights; then splits into two: "untouched clause → original still governs" and "amendment exists ≠ this clause changed" |
| **BCRY** | **6 carry-out** | The contract in force today isn't the original, and it isn't the amendments — it's the original with each clause replaced by its most recent edit. Check clause by clause, not document by document. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Paste in a contract along with every amendment to it. Then ask: go through this clause by clause. For each one, tell me whether an amendment changed it, and if so, give me only the most recent version — not the original. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Amendment History. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the amended-contract fact; the clause-chain mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (the original document still governs); the B02→B03 anchor falsifies it directly — reading the original alone gives 30 days, but what's in force is 45 |
| Exactly one inference flag | none needed — the account describes the generic shape of tracking a document through a chain of amendments (clause-level supersession), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the lease's notice-period clause: 30 → 60 → 45) |
| Both directions | B03 — an untouched clause isn't missing, the original still governs it; an amendment existing elsewhere in the file doesn't prove it touched the clause in question |
| No design judgment | B01–B03 state what amendment tracking does and why the original alone can't answer it, never a verdict on any specific skill's or drafter's design choices |

## Deliberately not claimed

- **Not that amendments always supersede cleanly.** The reel doesn't claim
  every amendment is unambiguous or that conflicts between amendments never
  happen — it states the ordinary case: the most recent edit to a clause is
  what's in force for that clause.
- **Not a specific Claude product feature.** Because the source sheet's
  actual facts were never written (see QUESTION.md), this script describes
  the generic mechanics of amendment tracking in legal documents rather than
  citing any particular tool's UI or output format.
- **No accusation that anyone drafted carelessly.** Reading only the
  original document is presented as an ordinary, understandable shortcut,
  not a failure by any named person or team.

## Handoff prompt (BHTF, read aloud)

> "Paste in a contract along with every amendment to it. Go through this
> clause by clause. For each one, tell me whether an amendment changed it,
> and if so, give me only the most recent version — not the original."

Why it's worth running: the exercise surfaces the same distinction the reel
is built around — a clause-by-clause read catches every place the original
document alone would have given the wrong answer.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
