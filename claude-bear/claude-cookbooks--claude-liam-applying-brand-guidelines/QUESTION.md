# QUESTION

**The question:** "Claude, Applying Brand Guidelines." — when Claude puts a
document in your company's brand, is that Claude exercising a general sense
of taste, or is something more specific going on? Answered using the
`applying-brand-guidelines` skill's own description as the concrete case.

**Mode:** redo — source is
`anthropics/claude-cookbooks/youtube/claude-liam-applying-brand-guidelines/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`.../claude-cookbooks/skills/custom_skills/applying-brand-guidelines/SKILL.md`,
not available on this machine. 6 beats — B00 cold open, B01 anatomy, B02
pipeline, B03 design tell, BHTF handoff, BOUT outro; the source's own
rebuild log (`AUDIT.md`) already stripped a verdict beat as too short to earn
one — B00 was already `ClaudeComposerAsk` REMOTION, not AI-video/pantry, so
NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW swap).
This reel keeps the question and the source's body facts, re-registers the
narration to Plain, replaces the cold open with the Brutalist Hesitant
Writer, adds a dedicated carry-out beat (the source had none to fold in),
and closes with the Humanitarians AI skin.

**Why it earns a reel:** `applying-brand-guidelines` is a skill folder Claude
reads before it works, not something Claude is separately trained on. Four
files: `apply_brand.py` (14k), `validate_brand.py` (10k), `REFERENCE.md`
(3k), and a 4k `SKILL.md` holding the full instruction set in plain
language, no hidden logic — "the file is the program." The instructions sit
in a Steps section: Claude reads each step in order and executes it,
linear, no branching unless a step says so — read `SKILL.md`, execute,
return the result. The skill applies consistent corporate branding —
colors, fonts, layouts, messaging — to generated documents. Scope is
external communications only, and `validate_brand.py` is the falsifier:
wrong colors, wrong fonts, wrong scope, all caught the same way. Give it the
identical document twice and it returns identical branding both times; give
it a document outside the stated scope and it still runs the same steps,
against material `SKILL.md` never specified.

**Naive framing (B00, corrected on screen):** "How do I get Claude to match
our brand?" → corrects "match" to "apply" (Claude isn't developing a feel
for the brand by osmosis; it's applying a written spec it reads before
acting).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works; this one is
  `applying-brand-guidelines`
- four files: `apply_brand.py` (14k), `validate_brand.py` (10k),
  `REFERENCE.md` (3k), `SKILL.md` (4k) — the `SKILL.md` is the full
  instruction set, plain language, no hidden logic
- the pipeline lives in a Steps section: read `SKILL.md`, execute each step
  in order, return the result — linear execution, no branching unless a
  step says so
- the skill applies consistent corporate branding — colors, fonts, layouts,
  messaging — to generated documents
- scope is external communications only — the stated constraint
- `validate_brand.py` is the falsifier: wrong colors, wrong fonts, wrong
  scope
- source's Your Turn worked example: "I want to apply brand guidelines to
  my team's documents. Read the applying-brand-guidelines skill and walk me
  through what you will do before you do it."

**Deliberately not claimed:** no specific color codes, font names, or
layout rules beyond what the source's own narration states — the source
`SKILL.md` itself is not available on this machine, so nothing beyond its
already-narrated description is invented.
