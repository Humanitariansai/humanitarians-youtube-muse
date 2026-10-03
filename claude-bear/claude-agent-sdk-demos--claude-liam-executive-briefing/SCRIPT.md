# Claude, Executive Briefing. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a Skill applies its own judgment about when to help. It doesn't — it matches a fixed list of trigger words in a file. So what decides when executive-briefing actually switches on?" | BrutalistHesitantWriter — types "A Skill must be some judgment Claude applies automatically. Is that it?", corrects "judgment" → "list" |
| B01 | 1 stakes | executive-briefing is one file — SKILL.md, about four kilobytes. Open it and there's no hidden logic. Right at the top is a printed list: executive, briefing, C-suite, board, leadership, presentation. Claude checks a request against this list before it does anything else. | one-file folder, SKILL.md called out, the trigger-word list printed inside it |
| B02 | 3 mechanism / **4 anchor planted** | Say a research memo comes in with the request: "turn this into a board presentation." Two of those words are on the list — board, presentation — so the skill fires: read SKILL.md, run its steps in order, return a structured executive brief. Same memo, same words, same brief, every time. | THE ANCHOR — the memo, the matching words lighting up, the pipeline firing |
| B03 | **4 anchor payoff / 5 both directions** | Take the exact same memo and ask instead: "make this shorter for my boss." Same intent, same document — but none of those words are on the list, and the skill stays silent. You get an ordinary rewrite, not the executive-brief structure. The list decides, not the meaning behind your request. | THE ANCHOR RETURNS — same memo, second request, no words light up, skill silent |
| **BCRY** | **6 carry-out** | executive-briefing doesn't notice what you need — it matches a fixed list of trigger words, and the moment your request skips that list, the skill stays quiet, no matter what you actually meant. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want to turn my research findings into an executive-ready briefing. Read the executive-briefing skill and walk me through what you'll do before you do it — and tell me which of my words made it fire. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Executive Briefing. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the anatomy fact (one file, a printed list); the matching mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Skill = built-in judgment); B03 falsifies it with a case — the identical memo, worded without the trigger words, and the skill never fires |
| Exactly one inference flag | none needed — every claim is read directly off the source's own stated activation rule and Steps section, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the same research memo, requested two different ways) |
| Both directions | B03 — the list fires reliably when the words match (holds); the identical intent produces nothing when the words are missing (flips) |
| No design judgment | B03 states the boundary as a fact about how the file's activation rule works, never a verdict on whether keyword triggering is a good or bad way to build a skill |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed this as "what it
  gets right" / "what it bites" — Teardown language. Plain keeps the same
  underlying fact (fixed activation rule, bounded to spec) but states it as
  mechanism, not judgment.
- **Not that every Skill activates on a keyword list.** `executive-briefing`'s
  trigger words are the worked example, not a universal claim about how
  every Skill decides to switch on.
- **No claim about what happens once the skill does fire beyond the
  source's own description** — the reel states that the output is a
  structured executive brief, not what specific content or tone choices
  that structure contains.

## Handoff prompt (BHTF, read aloud)

> "I want to turn my research findings into an executive-ready briefing.
> Read the executive-briefing skill and walk me through what you'll do
> before you do it — and tell me which of my words made it fire."

Why it's worth running: asking Claude to name which words triggered the
skill surfaces the activation rule directly — you see the trigger-word
match working exactly as B02 described, on your own request.

---
**GATE P — signed:** ______________________  (human)
