# QUESTION

**The question:** "Claude Code, Plugin Structure." — if you're building a
Claude Code plugin, does everything — commands, agents, skills — live inside
the `.claude-plugin` folder alongside the manifest, or somewhere else?
Answered using the `plugin-structure` skill's own naming rule for skills (the
file must be named exactly `SKILL.md`) as the concrete case.

**Mode:** redo — source is
`anthropics/claude-code/youtube/claude-liam-plugin-structure/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`claude-code/plugins/plugin-dev/skills/plugin-structure/SKILL.md`. 7 beats —
B00 cold open, B01 anatomy, B02 design, B05 teardown, BVDT verdict, BHTF
handoff, BOUT outro — B00 was already `ClaudeComposerAsk` REMOTION, not
AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no substitution beyond
the WRITER LAW swap). This reel keeps the question and the source's body
facts, re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, restates the source's B05 "gets right / bites" as an
anchor-and-both-directions mechanism fact instead of a design judgment, and
closes with the Humanitarians AI skin.

**Why it earns a reel:** A plugin's manifest, `plugin.json`, lives inside the
`.claude-plugin/` directory and needs exactly one required field: `name`, in
kebab-case (version, description, author, homepage, repository, license, and
keywords are optional metadata). Every component directory — `commands/`,
`agents/`, `skills/`, `hooks/`, `.mcp.json`, `scripts/` — lives at the
plugin's ROOT, one level up from `.claude-plugin/`, not inside it. The
source's own Critical Rules section names this split as the single most
common mistake, and it is silent when gotten wrong: misplaced components
just don't load, no error. Auto-discovery covers commands (any `.md` in
`commands/`) and agents (any `.md` in `agents/`) — drop the file in the
right place and it works. Skills are pickier: each lives in its own
subdirectory under `skills/`, and inside that subdirectory the file must be
named exactly `SKILL.md` — not `README.md`, not lowercase `skill.md`. Get
the filename wrong and the skill doesn't error, it silently fails to appear.
Custom paths in the manifest supplement auto-discovery rather than replacing
it — setting a custom path does not stop the default directory from also
being scanned. `${CLAUDE_PLUGIN_ROOT}` is the required path form for hook
commands, MCP server arguments, and script references, because plugins
install to different locations depending on how a user installed them.

**Naive framing (B00, corrected on screen):** "My commands folder — does it
go inside .claude-plugin?" → corrects "inside" to "outside" (the newcomer's
default read of a folder literally named `.claude-plugin` is that everything
plugin-related belongs inside it; the manifest does, the components don't).

**Body facts carried from source (unchanged):**
- manifest `plugin.json` lives inside `.claude-plugin/`; one required field,
  `name`, kebab-case; everything else in the manifest is optional metadata
- component directories (`commands/`, `agents/`, `skills/`, `hooks/`,
  `.mcp.json`, `scripts/`) live at the plugin ROOT, not inside
  `.claude-plugin/` — the source's own "most common mistake," silent when
  wrong
- commands and agents: any `.md` file in the right directory auto-loads, no
  registration step
- skills: each gets its own subdirectory under `skills/`; the file inside
  must be named exactly `SKILL.md` for auto-discovery — a misnamed file
  produces silent failure, not an error
- custom paths in the manifest supplement auto-discovery, they do not
  replace it — the default directory is still scanned even when a custom
  path is set
- `${CLAUDE_PLUGIN_ROOT}` is required for every path reference in hooks and
  MCP config, because install location varies by how the user installed the
  plugin
- source's Your Turn worked example: a plugin with a command, an agent, and
  a skill, checked for correct manifest placement, correct component
  placement, and the exact `SKILL.md` filename
