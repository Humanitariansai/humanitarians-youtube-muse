# Claude, Auto Updater. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude's auto-updater logic is baked into the model itself — some hidden capability. It isn't. It's baked into a file: SKILL.md. So — is the logic baked into the file?" | BrutalistHesitantWriter — types "Claude's auto-updater — is the logic baked into the model?", corrects "model" → "file" |
| B01 | 1 stakes / **4 anchor planted** | A Claude Skill is just a folder Claude reads before it acts. This one is named auto-updater, and everything it knows lives in one file: SKILL.md — plain sentences, not code. Open it, and you'd see something like five numbered steps, top to bottom. Claude reads that file, then follows it. The file is the whole program. | THE ANCHOR — a SKILL.md card opening, five numbered steps typing themselves in top to bottom |
| B02 | 2 wrong guess, falsified / 3 mechanism | It can look like Claude is reasoning out what to do on its own — that's the guess most people make. It isn't, here. Claude works straight down the Steps section, one step after another, and only branches where a step actually says to. Delete step three from that file, and step three simply doesn't happen. Nothing hidden fills the gap. | a linear pipeline of boxes, step 1 → step 2 → step 3 → done; step 3 struck out and skipped over, nothing filling the space |
| B03 | **4 anchor payoff** / 5 both directions | Go back to that same SKILL.md, the one with its steps listed top to bottom. Run auto-updater on the same input twice, and you get the same steps and the same result both times — that holds for as long as the input stays inside what the file describes. Step outside it, into a case the file never anticipated, and Claude has nothing written there to fall back on. | THE ANCHOR RETURNS — the same SKILL.md card, run twice side by side, identical checkmarks; then a case outside the file — a blank, nothing to match |
| **BCRY** | **6 carry-out** | A Skill's SKILL.md is the whole program. Claude follows it exactly — reliable inside what's written, blind past its edge. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: write me a SKILL.md with five short numbered steps for a repeatable task I do often. Then read it back to me, step by step, before you run anything — and follow only what's written, nothing else. Watch whether every action Claude takes matches a line in that file, and whether it stops the moment the steps run out. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Auto Updater. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder/file split; the step-by-step mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (logic baked into the model); B02 falsifies it with a case — delete step three from the file, and step three doesn't happen, nothing hidden fills in |
| Exactly one inference flag | none needed — every claim describes the general, publicly documented mechanism of a Claude Skill (a folder, a `SKILL.md`, steps read in order); no claim is made about what `auto-updater` specifically automates, since the source never says and the real file is unreachable (see QUESTION.md) |
| One anchor, planted early, paid off late | B01 → B03 (the SKILL.md card with its five numbered steps) |
| Both directions | B03 — repeatable when the input stays inside what the file describes (holds); nothing to fall back on when the input falls outside it (flips) |
| No design judgment | B02/B03 state the step-by-step mechanism and its edge as facts about how a Skill runs, never a verdict on whether `auto-updater`'s SKILL.md was written well |

## Deliberately not claimed

- **Not what `auto-updater` specifically updates.** The source's own
  narration never says — three of its seven beats carry a literal unfilled
  `>` template placeholder exactly where that content should be (see
  QUESTION.md). This reel states only what's generically true of any
  Claude Skill's mechanism, with `auto-updater` as the example's name, not
  as a source of invented specifics.
- **Not a verdict on the design.** The source's B03 called this "the
  Teardown moment" — Teardown language. Plain keeps the same underlying
  mechanism (repeatable inside the spec, unsupported outside it) but states
  it as a boundary, not a critique of the file.
- **No claim that Claude never reasons.** B02 states plainly that *this*
  mechanism — a Skill's Steps section — is followed linearly, not that
  Claude never reasons about anything anywhere.

## Handoff prompt (BHTF, read aloud)

> "Write me a SKILL.md with five short numbered steps for a repeatable task
> I do often. Then read it back to me, step by step, before you run
> anything — and follow only what's written, nothing else."

Why it's worth running: watching whether every action Claude takes matches
a line in the file, and whether it stops cleanly the moment the steps run
out, surfaces whether the file-is-the-program claim from B01–B03 actually
holds for a Skill you wrote yourself.

---
**GATE P — signed:** ______________________  (human)
