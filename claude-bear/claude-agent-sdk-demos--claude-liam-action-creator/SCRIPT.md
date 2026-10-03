# Claude, Action Creator. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a Skill must be code Claude runs. It isn't — a Skill is a file of instructions Claude reads before it acts. So what's actually inside one?" | BrutalistHesitantWriter — types "A Skill must be some code Claude runs automatically. Is that it?", corrects "code" → "file" |
| B01 | 1 stakes / 2 wrong guess, falsified | Open the folder and there's no program to run — just a `SKILL.md` file, plain text, and a `templates` folder beside it. Two files. This one is `action-creator`. Claude reads `SKILL.md` before it acts; the file is the instruction set, not a script running somewhere behind it. | the two-file folder, SKILL.md called out |
| B02 | 3 mechanism / **4 anchor planted** | Inside `SKILL.md` is a Steps section, and Claude works through it top to bottom — read the request, run the step, return the result. Ask for a one-click button that sends a payment reminder to a specific vendor, and `action-creator` turns that into a saved action: click it once, and the same email goes out, every time you press it. | Steps pipeline; THE ANCHOR — the payment-reminder button |
| B03 | **4 anchor payoff / 5 both directions** | That's why the button is reliable — the steps in the file don't change between clicks, so the same request produces the same email every time. But ask that same button to negotiate the invoice instead of just sending it, and nothing happens beyond what's already there — negotiating was never written into the file. The skill only does what the page in front of it says. | THE ANCHOR RETURNS — the same button, reliable click / silent edge case |
| **BCRY** | **6 carry-out** | A Skill isn't new intelligence — it's a folder of fixed steps Claude reads before acting, so a one-click button does exactly what's written, every time, and nothing that isn't. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want a one-click action that archives newsletters from a specific sender. Read the action-creator skill and walk me through what you'll do before you do it — show me each step in order, so I can see exactly what the button will run. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Action Creator. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the anatomy fact; the Steps mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Skill = code Claude runs); B01 falsifies it with a case — open the folder, there's no program, just a plain-text `SKILL.md` |
| Exactly one inference flag | none needed — every claim here is read directly off the source's own description of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the payment-reminder one-click button) |
| Both directions | B03 — the button is reliable within the file's steps (holds); asking it to do something the file never described produces nothing (flips) |
| No design judgment | B03 states the boundary as a fact about what's written in the file, never a verdict on whether that's a good or bad way to build a skill |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed this as "what it
  gets right" / "what it bites" — Teardown language. Plain keeps the same
  two facts (reliable on repeat, bounded to spec) but states them as
  mechanism, not judgment.
- **Not that all Skills share this exact shape.** `action-creator`'s
  SKILL.md + templates folder is the worked example, not a universal claim
  about every Skill's file layout.
- **No claim about extensibility.** The reel never says a Skill *can't* be
  extended — only that its current button does only what the file currently
  specifies.

## Handoff prompt (BHTF, read aloud)

> "I want a one-click action that archives newsletters from a specific
> sender. Read the action-creator skill and walk me through what you'll do
> before you do it — show me each step in order, so I can see exactly what
> the button will run."

Why it's worth running: asking Claude to narrate the steps before it builds
the action surfaces the constraint logic directly — you see the Steps
section working exactly as B02 described, on your own request.

---
**GATE P — signed:** ______________________  (human)
