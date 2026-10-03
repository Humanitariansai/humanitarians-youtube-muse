# SCRIPT.md — It Talks to Claude, Not You. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-command-development` (Teardown, the Claude Code
plugin-dev `command-development` skill) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Writing a command, you picture its body speaking to the user. It doesn't —
it speaks to Claude. The body is instructions Claude executes, not a
message for the user. Here's how command files work.

## B01 — the file, in one part with three homes
A command is one markdown file, with an optional settings block on top.
Three places it can live: project commands, visible only inside that one
project; personal commands, in your own home folder, visible across every
project on your machine; and plugin commands, bundled inside a plugin and
available the moment it's installed. The settings block can carry five
fields: a description for the help menu, a list of tools the command is
allowed to use, which model runs it, a hint describing its expected
arguments, and a switch that turns off automatic triggering.

## B02 — who it's for (ANCHOR PLANTED)
Here's the anchor. A command's body is read by Claude, not shown to the
person who typed it. Correct: "review this code for security issues and
list each one with a line number." That's a direction Claude can act on.
Incorrect: "this command will review your code and give you a report."
That sentence describes what happens to the user — Claude has nothing to
actually do with it. Every command body should read like the first one: a
direction, never a description of an outcome.

## B03 — precise here, left elsewhere (BOTH DIRECTIONS)
Some of this is spelled out completely. The three locations, the five
fields, and the argument syntax — a single dollar sign and number for a
positional value, an at-sign for a file, an exclamation mark and backticks
to run a shell command inline — all fully specified. Some of it isn't: the
exact syntax for that inline shell command lives in a separate reference
page, not in the skill itself, and there's no built-in way to check
whether a command file is well-formed before you run it.

## Close

**BCRY — carry-out**
A Claude Code command is a markdown file: frontmatter tells Claude when
and how to run it, and the body is instructions Claude reads — never a
message meant for the person running it.

**BHTF — your turn (ANCHOR PAYOFF — returns to B02)**
Your turn. Open a Claude Code session and paste this: create a slash
command for my plugin that reviews a pull request and posts a summary.
Then check four things — does the body read like a direction to Claude,
not a description of what you'll see happen? Does allowed-tools name
specific commands, like git or gh, rather than every tool? Is there an
argument-hint, so autocomplete shows what the command expects? And does
any shell command run inline, with an exclamation mark and backticks,
instead of being left as a placeholder you'd fill in by hand? Those four
checks are your gate.

**BOUT — outro**
It Talks to Claude, Not You. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | you're writing a command, assume its body addresses the person running it |
| Wrong guess | B00 → BCRY | "user" corrected to "Claude," resolved in the carry-out |
| Mechanism | B01–B02 | file anatomy and locations; who the body is written for |
| Anchor | B02 → BHTF | the correct/incorrect review-command example, planted then built in Your Turn |
| Both directions | B03 | precise in the file format, pushed to an external reference for the rest |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats: B00 (cold open), B01 (locations + frontmatter fields +
dynamic arguments), B02 (the instructions rule + four command patterns),
B05 (Teardown gets-right/bites), BVDT (verdict), BHTF (handoff), BOUT
(outro) — B03/B04 were never used in the source sheet. hai-simple's spine
has no verdict beat, so this redo keeps the SAME beat count (7) with a 1:1
remap: B00 to the hesitant writer; B01 kept as the file-and-locations
mechanism beat; B02 recentred on the instructions-rule example (dropped
the four-pattern catalogue and CLAUDE_PLUGIN_ROOT detail to fit one beat,
since the redo contract adds no beats) and promoted to the reel's anchor,
because the correct/incorrect pair is the single clearest illustration of
the critical rule and pays off cleanly at Your Turn; B05's Teardown "gets
right / where it bites" framing is recast as B03, a neutral
both-directions beat — what's fully specified in the file format versus
what's pushed to an external reference or simply not built — because a
beat built to critique the skill's design has no home in Plain register,
but the underlying facts (bash execution syntax lives in a separate
reference file; there's no validation tooling for command files) are true
either way, and "precise here, left elsewhere" is exactly the
BOTH-DIRECTIONS move Plain register asks for. BVDT (verdict) becomes BCRY
(carry-out) — the reel's one closing sentence instead of a scored recap.
BHTF and BOUT are kept as Your Turn and outro, with the outro re-skinned
to Humanitarians AI. No beat in the source was AI-VIDEO, pantry, or a
human-drop slot, so NO-GENAI/NO-PANTRY LAW required no beat replacement —
all beats render as REMOTION or GRAPHIC either way.

**Dropped from the source, and why:** the four command patterns (Review,
Testing, Documentation, Workflow) and `${CLAUDE_PLUGIN_ROOT}` path
resolution are true and useful but do not fit a 7-beat redo without
crowding the anchor beat; they are not contradicted, just not carried
into this cut. Dynamic-argument syntax ($ARGUMENTS, $1/$2/$3, @file,
!`bash`) survives as one clause in B03 rather than its own beat.

WRONG-GUESS LAW note: with only 7 beats total (locked by the redo
contract) there is no beat to spare for a dedicated wrong-guess beat
separate from B00. The hesitation IS the wrong guess here (WRITER LAW),
and the correction is picked back up explicitly at the carry-out (BCRY)
rather than in its own body beat — a deliberate compression under the
beat-count constraint, not an oversight.
