# It Talks to Claude, Not You.

Writing a custom Claude Code slash command and picturing its body as a note
to the person who runs it? That's the wrong audience. A command is one
markdown file: frontmatter on top (description, allowed-tools, model,
argument-hint, a flag to disable automatic invocation), and a body below it
that Claude reads and executes — never a message shown to you. The clearest
tell: "review this code for security issues" is a direction Claude can act
on; "this command will review your code and give you a report" describes an
outcome to a person, and Claude has nothing to do with it. The file format
is precise about locations, fields, and argument syntax; it's silent on the
exact shell-execution syntax (pushed to an external reference) and ships no
built-in way to validate a command file before you run it.

**Topic:** CLAUDE CODE · COMMAND DEVELOPMENT
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-command-development

---

## Chapters

0:00 The naive framing: "it talks to the user"
0:11 The file, in one part with three homes
0:40 The anchor: who the command body is for
1:14 Precise here, left elsewhere
1:47 Carry-out
1:58 Your turn
2:07 Outro

---

## YOUR TURN

Open a Claude Code session and paste this: create a slash command for my
plugin that reviews a pull request and posts a summary. Then check four
things — does the body read like a direction to Claude, not a description of
what you'll see happen? Does allowed-tools name specific commands, like git
or gh, rather than every tool? Is there an argument-hint, so autocomplete
shows what the command expects? And does any shell command run inline, with
an exclamation mark and backticks, instead of being left as a placeholder
you'd fill in by hand? Those four checks are your gate.

Run that today, against a command you'd actually want to build.

---

## Deliberately not claimed

No specific model names or version numbers for the `model` field — "haiku,"
"sonnet," "opus" stand in for whatever the current lineup is, since that
changes. The four command patterns (review, testing, documentation,
workflow) and `${CLAUDE_PLUGIN_ROOT}` path resolution are real and useful
but aren't covered in this cut — not contradicted, just left out to keep the
reel to one clean argument. The pull-request-review example is illustrative,
not a claim that this is the only or best use of a command.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #CommandDevelopment #ClaudeCommands #LLM #HumanitariansAI #ProfessorBear

---
