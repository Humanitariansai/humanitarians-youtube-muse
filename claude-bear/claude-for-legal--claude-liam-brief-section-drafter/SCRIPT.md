# Claude, Brief Section Drafter. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-brief-section-drafter`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wondered: can Claude write your whole legal brief? Not quite — the skill drafts one section, in your case's own theory, with every fact and citation still needing your check. Here's what it actually does." | writer types "Can Claude WRITE your legal brief?", hesitates on WRITE, corrects to "draft" — lands "Can Claude draft your legal brief?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is brief-section-drafter. The SKILL.md file holds the full instruction set in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | folder tree reveal: one file, SKILL.md, 15k |
| B02 | pipeline | The pipeline sits in the Steps section. Claude reads each step in order, then runs it. Linear — no branching unless a step says so. | YOUR REQUEST → Read SKILL.md → Execute → DRAFT SECTION |
| B03 | 3 mechanism | The constraint is specific. Draft one section, in house style, consistent with the case theory — every fact cited, every case checked, every argument tied back to that theory. Stay inside that scope, and the draft holds its shape every time. | heading card: "The interesting constraint." + full scope statement |
| **BCRY** | **6 carry-out** | Same spec in, same section out, every time. Checking the facts, the cases, and anything outside that spec is still your job. | the sentence, alone, serif, large — WantQuote |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. I'm drafting the argument section of a brief, and I have my case theory and every source ready. Read the brief-section-drafter skill, tell me exactly what facts and cases you need from me before you draft a single sentence, then draft the section in house style — citing every fact and every case as you go. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro series | Claude, Brief Section Drafter. | OutroSeries — title restate |
| BCTA | outro cta | …Liam, in for Bear. | OutroCTA — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the constraint (house style, case theory, cited facts/cases) and stops; the source's "Teardown moment" framing and "what it bites" verdict language are both dropped |
| Stakes → mechanism | B00 states the misconception; B01–B02 explain the file and pipeline before B03's constraint |
| Carry-out | BCRY compresses the distinction (repeatable inside spec vs. verification stays human), not the topic |
| Host handoff | B00 hands off narration duties to Liam implicitly via "here's what it actually does"; no puppet host in hai-simple |
| Hedge words | none used outside any flag — every claim is a confirmed, present-tense description of the skill's own spec |

## Deliberately not claimed

- **Not "Claude writes the whole brief."** The naive framing in B00 ("write your whole
  legal brief") is stated and corrected within the same beat — the skill drafts ONE
  section, never a complete brief.
- **Not "the draft is finished."** B03 and BCRY both stay inside what the source's own
  SKILL.md specifies: house style, case theory, cited facts and cases. Neither beat
  claims the citations or facts are verified by Claude — that check is stated as the
  reader's job, not implied to be handled.
- **No verdict on the skill's design.** The source's Teardown register judged the skill
  ("what it gets right," "what it bites"); this Plain redo describes the same constraint
  without ruling on whether it was well designed.

## Handoff prompt (BHTF, read aloud)

> "I'm drafting the argument section of a brief. I have my case theory and every source
> ready. Read the brief-section-drafter skill, tell me exactly what facts and cases you
> need from me before drafting a single sentence, then draft the section in house style —
> citing every fact and every case as you go."

Why it's worth running: it forces Claude to name its own input requirements before it
drafts anything — the same "explain first" clause the source reel's own handoff used to
surface the skill's real constraint logic.

---
**GATE P — signed:** ______________________  (human)
