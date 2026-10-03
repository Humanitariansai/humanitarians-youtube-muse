# QUESTION

**The question:** "Claude Code, Plugin Settings." — if you want a plugin's
configuration (a validation level, an on/off switch, per-project state) to
survive between sessions, is that a thing you ask Claude to remember, or a
thing you write down? Answered using the `plugin-settings` skill's own
pattern — one file, `.claude/plugin-name.local.md`, read by hooks, commands,
and agents alike — as the concrete case.

**Mode:** redo — source is
`anthropics/claude-code/youtube/claude-liam-plugin-settings/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`claude-code/plugins/plugin-dev/skills/plugin-settings/SKILL.md`. 7 beats —
B00 cold open, B01 anatomy, B02 design, B05 teardown, BVDT verdict, BHTF
handoff, BOUT outro — B00 was already `ClaudeComposerAsk` REMOTION, not
AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no substitution beyond
the WRITER LAW swap). This reel keeps the question and the source's body
facts, re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, restates the source's B05 "gets right / bites" as a
both-directions mechanism fact instead of a design judgment, and closes with
the Humanitarians AI skin.

**Why it earns a reel:** A plugin settings file is `.claude/plugin-name.local.md`
— always in the `.claude` directory, always ending `.local.md`, always
named to match the plugin. YAML frontmatter on top holds structured fields
(`enabled`, `mode`, retry counts, lists); a markdown body below holds
free-form text — prompts, instructions, documentation. Three consumers read
the same file: hooks are bash scripts that parse the frontmatter with `sed`;
commands use the Read tool and parse it in Claude's own context; agents
reference it directly in their instructions. The quick-exit pattern —
check the file exists, check `enabled`, exit 0 for a no-op — is how a hook
skips cleanly without touching `hooks.json`. Three usage patterns in the
source: a hook toggle (flip `enabled` without editing `hooks.json`, though
a restart is still needed to re-read it), agent state management (the
`multi-agent-swarm` plugin stores `agent_name`/`task_number`/`pr_number` in
frontmatter, a prompt in the body fed back to the agent each iteration),
and config-driven branching (a `validation_level` field driving a bash
`case` statement). The file is user-managed, not git-committed — the
source recommends `.claude/*.local.md` in `.gitignore`, unenforced. Changes
require a Claude Code restart; they are not hot-swapped. The `sed`
frontmatter parser is fragile: multiline values, quoted colons, or indented
blocks can silently corrupt what's extracted, with no error.

**Naive framing (B00, corrected on screen):** "How do I get Claude Code to
remember my plugin's settings between sessions?" → corrects "remember" to
"read" (asking Claude to remember something in conversation does not
survive a new session; a settings file is written once and read back every
time, by three different consumers, regardless of what the conversation
still holds).

**Body facts carried from source (unchanged):**
- the file is `.claude/plugin-name.local.md` — directory, naming, `.local.md`
  suffix all fixed
- YAML frontmatter (structured fields) above a markdown body (free-form
  context/prompts) in one file
- three consumers: hooks (bash `sed` parsing), commands (Read tool), agents
  (referenced in instructions)
- quick-exit pattern: check file exists, check `enabled`, exit 0 for no-op
- three patterns: hook toggle, agent state management (frontmatter fields +
  body-as-prompt, per `multi-agent-swarm`), config-driven behavior
  (`validation_level` branching a `case` statement)
- lifecycle: user-managed, not git-committed (`.claude/*.local.md` should be
  gitignored — unenforced); restart required, not hot-swapped
- the `sed`-based frontmatter parser is fragile on multiline YAML, quoted
  colons, or indented blocks — corrupts silently, no error
- source's gaps: restart requirement buried under "Best Practices" rather
  than stated in the overview; gitignore recommendation has no enforcement
  step; body-as-prompt pattern (`ralph-wiggum`) shown but not explained
