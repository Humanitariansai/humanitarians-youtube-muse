# QUESTION

**The question:** "Claude, Creating Financial Models." — when Claude builds a
DCF, runs a sensitivity table, or stress-tests a scenario, is that Claude
exercising general financial judgment, or is something more specific going
on? Answered using the `creating-financial-models` skill's own description
as the concrete case.

**Mode:** redo — source is
`anthropics/claude-cookbooks/youtube/claude-liam-creating-financial-models/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`.../claude-cookbooks/skills/custom_skills/creating-financial-models/SKILL.md`.
6 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BHTF
handoff, BOUT outro — the source's BVDT verdict beat had already been
stripped during an earlier rebuild pass, logged in the source's own
REBUILD-LOG.md as "a placeholder verdict is worse than no verdict"; B00 was
already `ClaudeComposerAsk` REMOTION, not AI-video/pantry, so NO-GENAI/
NO-PANTRY LAW required no substitution beyond the WRITER LAW swap). This
reel keeps the question and the source's body facts, re-registers the
narration to Plain, replaces the cold open with the Brutalist Hesitant
Writer, adds a dedicated carry-out beat (the source had none to fold in —
its BVDT was already stripped), restates the source's B03 "gets right /
bites" framing as a both-directions mechanism fact instead of a design
judgment, and closes with the Humanitarians AI skin.

**Why it earns a reel:** `creating-financial-models` is a skill folder
Claude reads before it works, not something Claude is separately trained
on. Three files total: `dcf_model.py` (16k), `sensitivity_analysis.py`
(11k), and a 4k `SKILL.md` holding the full instruction set in plain
language, no hidden logic — "the file is the program." The instructions
sit in a Steps section: Claude reads each step in order and executes it,
linear, no branching unless a step says so — read `SKILL.md`, execute,
return the result. The skill provides DCF analysis, sensitivity testing,
Monte Carlo simulations, and scenario planning for investment decisions.
Give it a revenue projection and it runs the same suite the same way every
run: same input, same output. The limit is the spec — only what
`SKILL.md` names.

**Naive framing (B00, corrected on screen):** "How do I teach Claude to
build financial models?" → corrects "teach" to "point" (Claude isn't
trained for this specifically; it's pointed at a skill — a folder it reads
before acting).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works; this one is
  `creating-financial-models`
- three files total: `dcf_model.py` (16k), `sensitivity_analysis.py`
  (11k), `SKILL.md` (4k) — the `SKILL.md` is the full instruction set,
  plain language, no hidden logic
- the pipeline lives in a Steps section: read `SKILL.md`, execute each
  step in order, return the result — linear execution, no branching unless
  a step says so
- the skill provides DCF analysis, sensitivity testing, Monte Carlo
  simulations, and scenario planning for investment decisions
- same input, same output, every run — hand it the identical projection
  twice, get the identical valuation both times
- the limit is the spec: only what `SKILL.md` specifies — DCF analysis,
  sensitivity testing, Monte Carlo, scenario planning, and nothing outside
  that suite
- source's rebuilt Your Turn worked example: "I want to stress-test a
  five-year revenue projection. Read the creating-financial-models skill
  and walk me through what you will build before you touch a number."

**Deliberately not claimed:** no specific formulas, discount-rate
conventions, or Monte Carlo parameters beyond what the source's own
narration states — the source `SKILL.md` itself is not available on this
machine, so nothing beyond its already-narrated description is invented.
