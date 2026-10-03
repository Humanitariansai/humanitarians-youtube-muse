# It's an Agent, Not a Command.

Extending a Claude Code plugin and want it to handle a task on its own? That's
not a command — it's an agent. An agent is one markdown file in two parts: YAML
frontmatter (name, description, model, color, optional tools) and a body that
becomes its system prompt. The description field is the trigger — "Use this
agent when," plus two to four worked examples — and it's what decides whether
the agent fires reliably. The file format is precise about structure; it's
silent on judgment calls like model choice or agent-vs-command scoping, which
live in what you write, not in the frontmatter.

**Topic:** CLAUDE CODE · AGENT DEVELOPMENT
**Playlist:** Claude Code
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-code--claude-liam-agent-development

---

## Chapters

0:00 The naive framing: "I need a command"
0:10 The file, in two parts — frontmatter and body
0:34 The anchor: the description field is the trigger
1:03 Precise here, open there
1:30 Carry-out
1:39 Your turn
2:07 Outro

---

## YOUR TURN

Open a Claude Code session and paste this: Create an agent for my plugin that
reviews Python code for security vulnerabilities. Then check four things —
does the description start with "Use this agent when" and include at least
two examples? Is the model set to inherit, rather than a specific model
hardcoded in? Does the tools list include only what a reviewer actually
needs — reading and searching code, say — instead of leaving tools out
entirely? And does the body address the agent directly, in second person?
Those four checks are your gate.

Run that today, against a task you'd actually want an agent for.

---

## Deliberately not claimed

No specific model names or version numbers — "inherit," "a model tier" stand
in for whatever the current lineup is, since that changes. No claim about how
many colors or tools exist beyond what the file format itself specifies. The
Python security-review example is illustrative, not a claim that this is the
only or best use of an agent.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #AgentDevelopment #ClaudeAgents #LLM #HumanitariansAI #ProfessorBear

---
