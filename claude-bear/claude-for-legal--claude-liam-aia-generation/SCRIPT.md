# When Is an AI Impact Assessment Actually Finished? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks if Claude can just finish their AI Impact Assessment for them. Wrong word — Claude can start it; finishing it takes someone checking it against the real system. Liam, take them through it." | BrutalistHesitantWriter — types "Can Claude just finish our AI Impact Assessment for us?", corrects "finish" → "start" |
| B01 | 1 stakes / 2 wrong guess, falsified | It's tempting to treat a polished-looking assessment as an accurate one. Say someone describes a hiring tool as "matches resumes to keywords" — when the real system also scores tone in video interviews. Claude drafts the risk section beautifully from that description. The video-scoring risk simply isn't in it, because Claude only saw the description, never the system. | a description card feeding a risk section that fills in cleanly; a caption reveals the real system also scores video-interview tone |
| B02 | 3 mechanism / **4 anchor planted** | A working impact assessment needs three things right: what the system actually does, the data feeding it, and who it affects. Claude can write all three sections fluently from whatever it's handed — it has no way to check that against the real system. Watch the anchor: that hiring tool's assessment page, System and Data sections filled in, stamped "draft — unverified," because the description behind it left out the video scoring. | three labeled parts lighting in turn (system / data / affected); THE ANCHOR — the assessment page, sections filled, stamped "DRAFT — UNVERIFIED" |
| B03 | **4 anchor payoff / 5 both directions** | The anchor returns once the missing fact gets added: the assessment's data section is rewritten to include the video scoring, and the stamp changes from "unverified" to "verified" — checked against what the system actually does. But a fluent, complete-reading assessment doesn't prove it's accurate; polish is a writing quality, not a fact-check. And a rough, half-filled first draft doesn't mean the process failed — a scaffold that flags exactly what still needs checking is doing its job. | THE ANCHOR RETURNS — the data section rewritten, stamp flips to "VERIFIED"; then splits into "polish ≠ proof" and "incomplete ≠ failure" |
| **BCRY** | **6 carry-out** | An AI Impact Assessment isn't finished when Claude writes it — it's finished when someone checks it against what the system actually does. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Describe one AI-powered feature you actually use or are building, in two or three sentences. Ask Claude to draft the System and Data sections of an AI Impact Assessment from that description alone. Then add one detail you left out on purpose — a data source, an edge case, a downstream use — and ask it to revise. Compare the two drafts side by side. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | When Is an AI Impact Assessment Actually Finished? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the fluent-vs-accurate gap; the three-part mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude can just finish it); B01 falsifies it with a concrete case — a description missing one whole risk category still produces a fluent, complete-reading draft |
| Exactly one inference flag | none needed — the account describes the generic shape of what makes an assessment accurate (system / data / affected people), not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (the same hiring-tool assessment page: unverified, then verified) |
| Both directions | B03 — a fluent, complete-reading draft doesn't prove accuracy (polish is not proof); a rough, half-filled draft doesn't mean the process failed (incomplete is not failure) |
| No design judgment | B01–B03 state what an assessment needs and why, never a verdict on whether any specific skill or tool was well designed |

## Deliberately not claimed

- **Not that Claude made an error.** B01's case is a description gap, not a mistake by
  the tool — Claude wrote exactly what it was told, correctly.
- **Not a specific Claude product feature or regulation.** Because the source sheet's
  actual facts were never written (see QUESTION.md), this script describes the generic
  mechanics of what makes an AI Impact Assessment accurate (system, data, affected
  people) rather than citing any particular skill's steps, output format, or jurisdiction's
  legal requirement.
- **No accusation that anyone was negligent.** The incomplete description in B01 is
  presented as an ordinary risk of any first draft, not a failure by a named person or team.

## Handoff prompt (BHTF, read aloud)

> "Describe one AI-powered feature you actually use or are building, in two or three
> sentences. Ask Claude to draft the System and Data sections of an AI Impact Assessment
> from that description alone. Then add one detail you left out on purpose — a data
> source, an edge case, a downstream use — and ask it to revise. Compare the two drafts
> side by side."

Why it's worth running: it makes the fluent-vs-accurate gap concrete in your own words —
the second draft is better only because you supplied a fact the first one never had.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
