# Claude Code, Skill Development. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a Teardown-form sheet). Register: **Plain**.
7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks Claude to just remember their PDF workflow. But conversations end and reminders fade. The real fix is a skill — a packaged capability Claude can find on its own. What's inside one?" | BrutalistHesitantWriter — types "How do I add a reminder so Claude always follows my PDF workflow?", corrects "reminder" → "skill" |
| B01 | 1 stakes / 2 wrong guess, falsified | A reminder lives inside this conversation — once it scrolls away or a session ends, it's gone. A skill lives in a file Claude reads before you even ask. Its name and description sit in front of every conversation, always visible; the rest — the instructions, and any scripts, references, or output files — loads only once Claude decides the skill applies. | a reminder bubble scattering as conversation text scrolls past; a SKILL.md file staying fixed; three tiers lighting in turn — name+description, body, resources |
| B02 | 3 mechanism / **4 anchor planted** | Picture a skill called pdf-editor, for rotating PDFs and converting pages to images. Its description has to name the trigger directly — "used when the user asks to rotate a PDF or convert PDF pages" — because that's the only sentence Claude sees before it decides. The instructions inside are written as direct steps, not advice, and the actual rotation code lives in its own script file, referenced by name. | THE ANCHOR — pdf-editor's SKILL.md card: description naming the trigger phrase, body as numbered steps, `scripts/rotate_pdf.py` lighting up beside it |
| B03 | **4 anchor payoff / 5 both directions** | Get the description right and pdf-editor fires exactly when someone asks to rotate a PDF — every time, because Claude is matching a specific phrase, not guessing. But swap that for a vague line like "use this skill for PDF tasks," and it won't fire reliably at all. And paste the rotation script directly into the body instead of its own file, and the whole skill loads in full on every single trigger — the lean file you wrote becomes the thing progressive disclosure was built to avoid. | THE ANCHOR RETURNS — pdf-editor firing three times reliably; then the description card going vague and dark ("never fires"); then the script folded into the body, the file swelling heavy |
| **BCRY** | **6 carry-out** | A skill isn't something you ask Claude to remember — it's a file whose description has to do the finding, and everything inside it only loads once that description matches. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Create a skill for my plugin called pdf-editor that handles rotating PDFs and converting pages to images. Watch three things when Claude answers: does the description read in third person with a specific trigger phrase — this skill should be used when the user asks to rotate a PDF or convert pages — instead of something vague like use this for PDF tasks? Is the body written as direct steps, not advice? And does the actual rotation code live in its own script file, referenced by name, instead of pasted into the body? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Code, Skill Development. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the file/visibility fact; the pdf-editor mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (tell Claude to remember); B01 falsifies it with a case — a reminder scrolls out of context, a skill's name and description sit visible in every conversation regardless |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documentation of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the pdf-editor skill — trigger phrase vs. vague description; referenced script vs. inline script) |
| Both directions | B03 — the skill fires reliably with a specific trigger phrase (holds); the same skill goes silent with a vague description, and swells past its own lean design with an inlined script (flips) |
| No design judgment | B03 states the two failure modes as facts about how the description match and the resource-loading model work, never a verdict on whether the skill's documentation should have led with the warning |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the progressive
  disclosure explanation, the description-quality criteria, and the
  imperative-form rule as "what it gets right," and the undocumented
  trigger mechanism, the soft word-count ceiling, and the vague
  skill-reviewer-agent mention as "where it bites" — Teardown language,
  including a judgment that the skill's own documentation leaves the
  trigger mechanism unexplained. Plain keeps the same underlying facts
  (a vague description doesn't fire reliably; an inlined script breaks the
  loading model) but states them as mechanism boundaries, not a critique of
  the skill file.
- **Not that pattern-matching vs. language-model judgment is settled.** The
  source itself flags that the trigger mechanism — how Claude actually
  decides a description matches — is never explained by the skill being
  taught; this reel doesn't invent an answer it doesn't have.
- **No claim that every skill needs scripts, references, and assets.** All
  three resource folders are optional; the reel states that directly in
  B01 and never implies a skill is incomplete without them.

## Handoff prompt (BHTF, read aloud)

> "Create a skill for my plugin called pdf-editor that handles rotating
> PDFs and converting pages to images."

Why it's worth running: watching whether Claude writes a third-person
description naming the trigger phrase (not a vague summary), keeps the body
in imperative form, and references `scripts/rotate_pdf.py` by name instead
of pasting the script inline — three checks straight from the source's own
worked example — surfaces whether the description-and-loading distinction
from B03 actually lands.

---
**GATE P — signed:** ______________________  (human)
