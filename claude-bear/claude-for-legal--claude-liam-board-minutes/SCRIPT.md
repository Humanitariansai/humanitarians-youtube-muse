# When Are Board Minutes Actually "Official"? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes board minutes means a full transcript of everything that was said. Wrong word — minutes are the record of what was decided, not what was said. Liam, take them through it." | BrutalistHesitantWriter — types "Can Claude turn my notes into a full TRANSCRIPT of the meeting?", corrects "TRANSCRIPT" → "MINUTES" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's tempting to think a fuller draft is a better draft — every comment, every aside, captured. But say the notes include a director's offhand doubt about a deal, later dropped without a vote. Minutes that recorded it would preserve a private hesitation as a permanent record, attached to a decision that was never actually made. Real board minutes leave it out on purpose — they record decisions and actions, not discussion. | a notes page full of dense commentary; one line — the offhand doubt — gets circled in accent, then struck, with a caption revealing why |
| B02 | 3 mechanism / **4 anchor planted** | A minutes handoff that actually works has three parts: raw notes in, a draft limited to decisions, motions, and actions out, and a required approval step before any of it counts as official. Watch the anchor: those same meeting notes come back from Claude as a clean draft, stamped in the corner. Not official. Draft. | three labeled parts lighting in turn (notes / draft / approval); THE ANCHOR — a clean minutes draft, stamped "DRAFT — PENDING APPROVAL" |
| B03 | **4 anchor payoff / 5 both directions** | That same draft comes back to the board at the next meeting, gets checked line by line against what was actually decided, and only once the board votes to approve it does it become the official minutes. But a draft nobody marked up isn't automatically approved — silence isn't a vote, the board still has to say yes. And a draft that gets heavily corrected at approval isn't a failure either — catching an error at that stage is the approval step doing exactly its job. | THE ANCHOR RETURNS — the draft-stamped page gets a board vote and becomes "APPROVED — OFFICIAL MINUTES"; then splits into "silence ≠ approval" and "corrected ≠ failure" |
| **BCRY** | **6 carry-out** | Board minutes aren't official the moment they're drafted — they're official once the board approves them. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Take your rough notes from a real meeting. Ask Claude to draft board-minutes-style minutes — decisions, motions, and next steps only, not the play-by-play discussion. Then check that draft against your notes, line by line, before anyone treats it as the record. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | When Are Board Minutes Actually Official? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the fuller-isn't-better-draft gap; the three-part mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (minutes = transcript); B01 falsifies it with a concrete case — a dropped, never-voted-on doubt that a transcript would wrongly preserve as part of the record |
| Exactly one inference flag | none needed — the account describes the generic shape of a minutes handoff (draft, review, approve) and ordinary corporate-governance practice (decisions not discussion; approval at a later meeting), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the draft-stamped minutes page becomes the approved-official page) |
| Both directions | B03 — no markup doesn't prove approval (silence isn't a vote); heavy correction doesn't prove failure (catching an error at approval is the step working) |
| No design judgment | B01–B03 state what a minutes handoff needs and why, never a verdict on whether any specific skill or tool was well designed |

## Deliberately not claimed

- **Not that Claude made an error.** B01's case is about what belongs in the record at
  all — a decision never made — not a mistake in what Claude drafted.
- **Not a specific Claude product feature.** Because the source sheet's actual facts
  were never written (see QUESTION.md), this script describes the generic mechanics of
  a board-minutes drafting handoff (notes in, decisions-only draft out, board approval)
  rather than citing any particular skill's steps or output format.
- **No accusation that anyone was negligent.** The offhand doubt in B01 is presented as
  an ordinary judgment call about what belongs in a record, not a failure by a named
  person or team.

## Handoff prompt (BHTF, read aloud)

> "Take your rough notes from a real meeting. Ask Claude to draft board-minutes-style
> minutes — decisions, motions, and next steps only, not the play-by-play discussion.
> Then check that draft against your notes, line by line, before anyone treats it as
> the record."

Why it's worth running: it forces the draft down to the one thing minutes are actually
for — the decisions — so the approval step (the boundary the reel is built around)
is a quick check against a short list, not a re-read of everything anyone said.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
