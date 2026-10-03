# QUESTION

**The question:** "Claude, Analyzing Financial Statements." — when Claude
analyzes a balance sheet or income statement, is that Claude reasoning about
finance on its own, or is something more specific going on? Answered using
the `analyzing-financial-statements` skill's own description as the concrete
case.

**Mode:** redo — source is
`anthropics/claude-cookbooks/youtube/claude-liam-analyzing-financial-statements/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`.../claude-cookbooks/skills/custom_skills/analyzing-financial-statements/SKILL.md`.
7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro — B00 was already `ClaudeComposerAsk`
REMOTION, not AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no
substitution beyond the WRITER LAW swap). This reel keeps the question and
the source's body facts, re-registers the narration to Plain, replaces the
cold open with the Brutalist Hesitant Writer, folds the source's BVDT
verdict recap into a proper carry-out beat, restates the source's B03
"gets right / bites" framing as a both-directions mechanism fact instead of
a design judgment, and closes with the Humanitarians AI skin.

**Why it earns a reel:** `analyzing-financial-statements` is a skill folder
Claude reads before it works, not something Claude is separately trained on.
Three files: `calculate_ratios.py` (12k), `interpret_ratios.py` (16k), and a
2k `SKILL.md` holding the full instruction set in plain language, no hidden
logic — "the file is the program." The instructions sit in a Steps section:
Claude reads each step in order and executes it, linear, no branching unless
a step says so — read `SKILL.md`, execute, return the result. The skill
calculates key financial ratios and metrics from financial statement data
for investment analysis. Give it a balance sheet or income statement and it
runs the ratios the same way every run: same input, same output. The limit
is the spec — only what `SKILL.md` names.

**Naive framing (B00, corrected on screen):** "How do I teach Claude to
analyze financial statements?" → corrects "teach" to "point" (Claude isn't
trained for this specifically; it's pointed at a skill — a folder it reads
before acting).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works; this one is
  `analyzing-financial-statements`
- three files: `calculate_ratios.py` (12k), `interpret_ratios.py` (16k),
  `SKILL.md` (2k) — the `SKILL.md` is the full instruction set, plain
  language, no hidden logic
- the pipeline lives in a Steps section: read `SKILL.md`, execute each step
  in order, return the result — linear execution, no branching unless a
  step says so
- the skill calculates key financial ratios and metrics from financial
  statement data for investment analysis
- same input, same output, every run — hand it the identical statement
  twice, get the identical ratios both times
- the limit is the spec: only what `SKILL.md` specifies; a statement the
  steps weren't written for still runs the same steps, against data
  outside the spec
- source's Your Turn worked example: "I want to analyze financial
  statements for investment insights. Read the analyzing-financial-statements
  skill and walk me through what you will do before you do it."

**Deliberately not claimed:** no specific ratio names, formulas, or
financial-statement line items beyond what the source's own narration
states — the source SKILL.md itself is not available on this machine, so
nothing beyond its already-narrated description is invented.
