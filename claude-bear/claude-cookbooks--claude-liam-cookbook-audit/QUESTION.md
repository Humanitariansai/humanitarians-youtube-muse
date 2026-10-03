# QUESTION

**The question:** "Claude, Cookbook Audit." — when Claude reviews an Anthropic
Cookbook notebook, is that Claude forming its own opinion of quality, or is
something more specific going on? Answered using the `cookbook-audit` skill's
own description as the concrete case.

**Mode:** redo — source is
`anthropics/claude-cookbooks/youtube/claude-liam-cookbook-audit/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`.claude/skills/cookbook-audit/SKILL.md`, not available on this machine.
6 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BHTF
handoff, BOUT outro; the source's own rebuild log (`AUDIT.md`) already
stripped a verdict beat as too short to earn one. B00 was already
`ClaudeComposerAsk` REMOTION, not AI-video/pantry, so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap). This reel keeps the
question and the source's body facts, re-registers the narration to Plain,
replaces the cold open with the Brutalist Hesitant Writer, adds a dedicated
carry-out beat (the source had none to fold in), and closes with the
Humanitarians AI skin.

**Why it earns a reel:** `cookbook-audit` is a skill folder Claude reads
before it works, not something Claude is separately trained on. Three files:
`SKILL.md` (12k), `style_guide.md` (5k), `validate_notebook.py` (17k) — the
`SKILL.md` holds the full instruction set in plain language, no hidden logic.
The instructions sit in a Steps section: Claude reads each step in order and
executes it, linear, no branching unless a step says so — read `SKILL.md`,
execute, return the result. The skill's job: audit an Anthropic Cookbook
notebook against a rubric, used whenever a notebook review or audit is
requested. Give it the identical notebook twice and it returns the identical
rubric score both times; give it a notebook with something outside the
stated rubric and it still runs the same steps, checking only what
`SKILL.md` names — `validate_notebook.py` is the check that runs regardless.

**Naive framing (B00, corrected on screen):** "How do I get Claude to judge
my notebook?" → corrects "judge" to "audit" (Claude isn't forming a
by-feel impression; it's auditing against a written rubric it reads before
acting).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works; this one is
  `cookbook-audit`
- three files: `SKILL.md` (12k), `style_guide.md` (5k),
  `validate_notebook.py` (17k) — the `SKILL.md` is the full instruction set,
  plain language, no hidden logic
- the pipeline lives in a Steps section: read `SKILL.md`, execute each step
  in order, return the result — linear execution, no branching unless a
  step says so
- the skill's job: audit an Anthropic Cookbook notebook based on a rubric,
  used whenever a notebook review or audit is requested
- `validate_notebook.py` is the falsifier: it checks the notebook against
  the rubric the same way regardless of what's in the notebook
- source's Your Turn worked example: "I want to audit an anthropic cookbook
  notebook based on a rubric. Use whenever a notebook review or audit is
  requested. Read the cookbook-audit skill and walk me through what you
  will do before you do it."

**Deliberately not claimed:** no specific rubric line items or scoring
weights beyond what the source's own narration states — the source
`SKILL.md` itself is not available on this machine, so nothing beyond its
already-narrated description is invented.
