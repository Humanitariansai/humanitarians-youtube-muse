# Claude, Cookbook Audit — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone wonders if Claude will judge their notebook by feel. But this skill runs a written rubric — it audits, it doesn't judge. So: how does that work?" | BrutalistHesitantWriter — types "How do I get Claude to judge my notebook?", corrects "judge" → "audit" |
| B01 | 1 stakes / 2 wrong guess, falsified | A skill is a folder Claude reads before it works — not something it's trained on. This one is cookbook-audit: SKILL.md, style_guide.md, and validate_notebook.py holding a twelve-kilobyte instruction set, plain language, no hidden logic. Claude reads the file, then acts. The file is the program. | a folder opens into three files; SKILL.md highlighted; "not trained on it" callout crosses a brain glyph; "the file is the program" closer |
| B02 | 3 mechanism / **4 anchor planted** | The instructions sit in a Steps section: read SKILL.md, execute each step in order, return the result — linear, no branching unless a step says so. Watch the anchor. Hand the skill a notebook: it reads the rubric, checks the notebook against it, and returns a score. Same three steps, every time. | three phase cards (read SKILL.md / execute / return result); THE ANCHOR — notebook → validate_notebook.py → rubric score |
| B03 | **4 anchor payoff / 5 both directions** | Same notebook, same score, every run — hand cookbook-audit the identical notebook twice and it returns the identical rubric score both times. That's the payoff of a file being the program. But the reverse holds too: hand it a notebook with something outside the stated rubric, and it still runs the same steps, checking only what SKILL.md names. validate_notebook.py is the check: right structure, right rubric items, right scope, all caught the same way. | THE ANCHOR RETURNS — the same pipeline firing identically twice, then split: in-scope notebook → clean score (the payoff); out-of-scope issue → same steps run anyway (the limit), with validate_notebook.py's check named on both sides |
| **BCRY** | **6 carry-out** | Auditing a cookbook notebook isn't Claude forming its own opinion of quality — it's SKILL.md, a rubric Claude reads, applies, and checks the same way against whatever notebook you hand it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. I want to audit an Anthropic Cookbook notebook against a rubric. Read the cookbook-audit skill and walk me through what you will do before you do it. Watch for that walk-through — explaining first is what surfaces which rubric items SKILL.md actually checks, and where the scope stops. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Cookbook Audit. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the folder-not-training fact; the Steps/anchor mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (judge by feel); B01 falsifies it with a case — a skill is a folder Claude reads, not something it's trained on, and the file is the program |
| Exactly one inference flag | none needed — every claim is read directly off the source's own narrated description of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (hand the skill a notebook; validate_notebook.py runs the same three steps) |
| Both directions | B03 — the same notebook twice returns the identical score (the payoff); a notebook issue outside the stated rubric still runs the same steps (the limit) |
| No design judgment | B03 states scope precision as a property of running a fixed, checked set of steps, never a verdict on whether the skill's SKILL.md should have covered more |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed the scope
  constraint and `validate_notebook.py`'s falsifying role as
  Teardown-flavoured "design tell" language ("what it gets right… what it
  bites"). Plain keeps the underlying fact — reliable inside the rubric,
  checked the same way regardless of what's outside it — but states it as a
  property of running fixed, validated steps, not a critique of the skill's
  documentation.
- **No specific rubric line items or scoring weights.** The source
  `SKILL.md` itself isn't available on this machine; this reel states only
  what the source's own narration already names (a rubric, a score,
  structure and scope checks — kept at that level of generality).
- **Not a claim that the skill decides what counts as "good."** Only that it
  runs the same steps and the same check regardless of whether the notebook
  fits the stated rubric.

## Handoff prompt (BHTF, read aloud)

> "I want to audit an anthropic cookbook notebook based on a rubric. Use
> whenever a notebook review or audit is requested. Read the cookbook-audit
> skill and walk me through what you will do before you do it."

Why it's worth running: this is the source's own worked example. Asking
Claude to explain first — before running the skill — is what surfaces which
rubric items its `SKILL.md` actually checks, and where the stated scope
stops, rather than only seeing the finished score.

---
**GATE P — signed:** ______________________  (human)
