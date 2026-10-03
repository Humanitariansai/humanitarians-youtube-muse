# SCRIPT.md — It's an Agent, Not a Command. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-agent-development` (Teardown, the Claude Code
plugin-dev `agent-development` skill) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Extending a Claude Code plugin, you reach for "command" first. A command
only runs when typed. What you want here keeps going on its own, through
several steps. That's an agent — the file that builds it.

## B01 — the file, in two parts
An agent is one markdown file, in two parts. On top: YAML frontmatter — a
name in lowercase with hyphens, a description that tells Claude when to
fire the agent, a model (usually set to "inherit"), a color from a small
set tied to the kind of work, and an optional list of tools. Leave tools
out, and the agent gets every tool there is. Below the frontmatter, the
rest of the file is markdown, written straight to the agent — "you are,"
"you do" — and that text becomes its system prompt.

## B02 — the trigger (ANCHOR PLANTED)
The description field decides when the agent runs. Say you want one that
reviews Python code for security issues. The pattern is fixed: "Use this
agent when," followed by two to four examples, each with four parts — the
setup, the user's request, what the agent would say back, and a note on
why it fits. Skip the examples, and Claude has nothing to match the
trigger against.

## B03 — precise here, open there (BOTH DIRECTIONS)
The file format itself is precise: names are lowercase with hyphens,
examples are required in a fixed shape, and the body follows a five-part
structure — responsibilities, process, standards, output, edge cases. What
the format doesn't decide for you: which model tier to pick, whether a
task is really agent-shaped or just a command, and how one agent hands off
to another. Those calls happen in the body text you write, not in the
frontmatter.

## Close

**BCRY — carry-out**
A Claude Code agent is one file: a description with examples that decides
when it runs, and a body that decides what it does once it's running.

**BHTF — your turn (ANCHOR PAYOFF — returns to B02)**
Your turn. Open a Claude Code session and paste this: Create an agent for
my plugin that reviews Python code for security vulnerabilities. Then
check four things — does the description start with "Use this agent when"
and include at least two examples? Is the model set to inherit, rather
than a specific model hardcoded in? Does the tools list include only what
a reviewer actually needs — reading and searching code, say — instead of
leaving tools out entirely? And does the body address the agent directly,
in second person? Those four checks are your gate.

**BOUT — outro**
It's an Agent, Not a Command. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | you're extending a plugin, need something that runs on its own |
| Wrong guess | B00 → BCRY | "command" corrected to "agent," resolved in the carry-out |
| Mechanism | B01–B02 | file anatomy; the description field as the trigger |
| Anchor | B02 → BHTF | the Python security-review agent, planted then built in Your Turn |
| Both directions | B03 | precise in the file format, open in the judgment calls |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats: B00 (cold open), B01 (frontmatter + system-prompt
anatomy), B02 (description field + creation paths), B05 (Teardown
gets-right/bites), BVDT (verdict), BHTF (handoff), BOUT (outro) — B03/B04
were never used in the source sheet. hai-simple's spine has no verdict
beat, so this redo keeps the SAME beat count (7) with a 1:1 remap: B00 to
the hesitant writer; B01 and B02 kept as the two mechanism beats (judgment
language dropped, facts kept); B05's Teardown "gets right / where it
bites" framing is recast as B03, a neutral both-directions beat — what the
file format specifies exactly, versus what it leaves to the builder's
judgment — because a beat built to critique the skill's design has no home
in Plain register, but the underlying facts (validation rules are
concrete; there's no agent-vs-command decision tree, no model-selection
heuristic, no multi-agent handoff guidance) are true either way, and
"precise here, open there" is exactly the BOTH-DIRECTIONS move Plain
register asks for. BVDT (verdict) becomes BCRY (carry-out) — the reel's
one closing sentence instead of a scored recap. BHTF and BOUT are kept as
Your Turn and outro, with the outro re-skinned to Humanitarians AI. No
beat in the source was AI-VIDEO, pantry, or a human-drop slot, so
NO-GENAI/NO-PANTRY LAW required no beat replacement — all beats render as
REMOTION or GRAPHIC either way.

WRONG-GUESS LAW note: with only 7 beats total (locked by the redo
contract) there is no beat to spare for a dedicated wrong-guess beat
separate from B00. The hesitation IS the wrong guess here (WRITER LAW), and
the correction is picked back up explicitly at the carry-out (BCRY) rather
than in its own body beat — a deliberate compression under the beat-count
constraint, not an oversight.
