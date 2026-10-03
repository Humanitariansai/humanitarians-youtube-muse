# Claude, Closing Checklist. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:35.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude just knows how to build a legal closing checklist, straight from its own judgment. It doesn't — it reads one written file, step by step. So does Claude just read how to build it?" | BrutalistHesitantWriter — types "Does Claude just know how to build a closing checklist?", corrects "know" → "read" |
| B01 | 1 stakes / anatomy | A skill is a folder Claude reads before it works. This one is closing-checklist, and it holds a single file: SKILL.md — the whole instruction set, in plain language, no hidden logic. Claude reads the file, then acts. The file is the program. | a folder icon labelled "closing-checklist/"; one file card, "SKILL.md", inside it |
| B02 | 3 mechanism / **4 anchor planted** | The pipeline lives in the file's Steps section. Claude reads each step in order, and runs it — linear, no branching unless a step says so. If a step is written there, it runs. If it isn't, it doesn't exist. | three step cards lighting up left to right in the Steps box; THE ANCHOR — a dashed "?" card sitting outside the box, unconnected |
| B03 | **4 anchor payoff / 5 both directions** | Ask for a step that's written in the file, and it runs the same way every time — reliable, because it's spec, not judgment. Ask for something the file never mentions, and nothing fills the gap: that step just isn't part of the run. | the three step cards run again, same order, highlighted; THE ANCHOR RETURNS — the same dashed "?" card, an arrow labelled "ask" pointing at it, staying dark: "not written here. doesn't run." |
| **BCRY** | **6 carry-out** | closing-checklist runs the steps written in its SKILL.md, the same way every time — not legal judgment, and nothing the file doesn't say. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I'm closing a transaction and want to use the closing-checklist skill. Read the SKILL.md and walk me through each step you'll run, in order, before you run any of them. That order matters — it's the whole spec, laid out before a single step executes. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Closing Checklist. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder/file split; the Steps-section mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude just knows); B01 falsifies it directly — it reads one file, the file is the program |
| Exactly one inference flag | none needed — every claim is read directly off the source's own narration, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the dashed "unwritten step" card: planted sitting outside the Steps box, paid off when an "ask" arrow points at it and it stays dark) |
| Both directions | B03 — spec-bound execution holds exactly as advertised when the step is written (reliable, repeatable); the same mechanism draws a flat line when a step is not written (nothing fills the gap) |
| No design judgment | B03 states the boundary as a fact about how the skill executes, never a verdict on whether closing-checklist should have been built differently |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03/BVDT framed the spec
  boundary as "the interesting constraint" / "what it gets right, where it
  bites" — Teardown language. Plain keeps the same underlying facts
  (spec-bound execution; repeatable results; a hard edge at what the file
  says) but states them as mechanism, not a critique of the skill file.
- **Not a claim about what specific legal task closing-checklist performs**
  beyond building and tracking a transaction's closing checklist. The
  source's own B03 and BHTF beats left their most specific clauses as
  unfilled `>` placeholders — the actual legal task was never recorded on
  this machine, and this reel does not invent one.
- **No claim that Claude goes silent outside the spec.** B03 states only
  that an unwritten step isn't part of the run — not that Claude has nothing
  to say about a request that falls outside it.

## Handoff prompt (BHTF, read aloud)

> "I'm closing a transaction and want to use the closing-checklist skill.
> Read the SKILL.md and walk me through each step you'll run, in order,
> before you run any of them."

Why it's worth running: watching Claude name its steps before running any of
them, in the order the file specifies, surfaces the same B01–B03 fact
directly — the file is the program, and the order is the whole spec.

---
**GATE P — signed:** ______________________  (human)
