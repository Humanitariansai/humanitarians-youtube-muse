# Claude, Listener Creator. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a Skill is a live watcher scanning your inbox in real time. It isn't — it's a template Claude fills in, a file describing conditions to match later. So what does listener-creator actually build?" | BrutalistHesitantWriter — types "A Skill must be some live watcher scanning my inbox. Is that it?", corrects "watcher" → "template" |
| B01 | 1 stakes / 2 wrong guess, falsified | Open the folder and there's no watcher running — just a `SKILL.md` file, about nine kilobytes, and a `templates` folder beside it. Two files. This one is `listener-creator`. Claude reads `SKILL.md` before it acts, then writes back a listener definition — the file is the instruction set, not a process running in the background. | the two-file folder, SKILL.md called out, "no watcher running" |
| B02 | 3 mechanism / **4 anchor planted** | Inside `SKILL.md` is a Steps section, worked top to bottom: read the request, write the condition, return the definition. Ask for a listener that flags any email from your boss marked urgent and forwards it right away, and `listener-creator` writes exactly that condition into a file. From then on, whenever a new email matches boss and urgent, the same forward fires. | Steps pipeline; THE ANCHOR — the "boss + urgent → forward" listener card, built once |
| B03 | **4 anchor payoff / 5 both directions** | That's why it's reliable — the condition in the file doesn't change, so every email from your boss marked urgent forwards the same way. But an equally urgent email from a client never fires it, because "client" was never written into the condition. The listener matches the words in the file, not how urgent the email actually is. | THE ANCHOR RETURNS — the same listener fires three times identically, then a client email goes nowhere |
| **BCRY** | **6 carry-out** | A listener isn't a watcher hovering over your inbox — it's a file naming one condition, and it fires on exactly that condition, every time, and stays silent on anything that only feels the same. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want a listener that flags any email mentioning a contract renewal and forwards it to my legal team. Read the listener-creator skill and walk me through what you'll do before you do it — show me exactly which condition you're writing into the file. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Listener Creator. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the anatomy fact; the Steps mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (listener = a live watcher, scanning now); B01 falsifies it with a case — open the folder, there's no watcher running, just a plain-text `SKILL.md` |
| Exactly one inference flag | none needed — every claim here is read directly off the source's own description of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the "boss + urgent → forward" listener) |
| Both directions | B03 — the listener fires reliably on the exact condition written (holds); an equally urgent email that doesn't match the written words never fires it (flips) |
| No design judgment | B03 states the boundary as a fact about what's written in the file, never a verdict on whether that's a good or bad way to build a listener |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed this as "what it
  gets right" / "what it bites" — Teardown language. Plain keeps the same
  two facts (reliable on the written condition, bounded to it) but states
  them as mechanism, not judgment.
- **Not that all Skills share this exact shape.** `listener-creator`'s
  SKILL.md + templates folder is the worked example, not a universal claim
  about every Skill's file layout.
- **No claim about how broad a condition can be written.** The reel never
  says a listener *can't* be written to catch more — only that its current
  definition matches only what's currently in the file.

## Handoff prompt (BHTF, read aloud)

> "I want a listener that flags any email mentioning a contract renewal
> and forwards it to my legal team. Read the listener-creator skill and
> walk me through what you'll do before you do it — show me exactly which
> condition you're writing into the file."

Why it's worth running: asking Claude to name the condition before it
writes the listener surfaces the constraint logic directly — you see the
Steps section working exactly as B02 described, on your own request.

---
**GATE P — signed:** ______________________  (human)
