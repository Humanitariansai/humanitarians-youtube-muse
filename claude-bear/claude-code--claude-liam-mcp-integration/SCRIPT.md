# MCP Integration. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks how to add an app to their plugin so it can use Asana. But there's no app step — you configure an MCP server, choosing one of four connection types. What's in that config?" | BrutalistHesitantWriter — types "How do I add an app to my Claude plugin so it can use Asana?", corrects "app" → "MCP server" |
| B01 | 1 stakes / 2 wrong guess, falsified | To reach an external service, a plugin declares it — in a config file, as one of four connection types. If this were like installing an app, one setting would work for everything. It doesn't: a local script Claude spawns itself needs `stdio`; a hosted service authenticating with OAuth, like Asana, needs `SSE` instead. Pick the wrong type, and Claude can't reach it. | one config box branching to four labelled connection types; a mismatched type crossed out, unreachable |
| B02 | 3 mechanism / **4 anchor planted** | Two places to write that declaration. A dedicated `.mcp.json` file at the plugin's root — the usual choice with more than one server. Or an inline `mcpServers` field inside `plugin.json`, for a single simple server. Say the Asana server goes in `.mcp.json`, type `SSE`. Each tool it offers gets a fixed name: `mcp`, two underscores, `plugin`, underscore, the plugin name, underscore, the server name, two underscores, the tool name. Asana's create-task tool becomes `mcp__plugin_asana_asana__asana_create_task` — exactly that string, with two underscores between each section. | two config file shapes; THE ANCHOR — the exact tool-name string built piece by piece under a magnifier |
| B03 | **4 anchor payoff / 5 both directions** | Get that name exactly right, and Claude calls exactly that one tool — nothing more, nothing less. Get one underscore wrong, and nothing happens: no error, just silence, because a name mismatch isn't reported. Some plugins pre-allow with a wildcard instead, to dodge that risk — `asana__*` matches every tool the server offers, not just create-task. That also fires without error. But now the plugin can call anything Asana exposes, which is exactly what the specific name was there to prevent. | THE ANCHOR RETURNS — the exact string firing cleanly on one tool; then a wildcard string lighting up every tool on the same server |
| **BCRY** | **6 carry-out** | Adding an MCP server isn't an app install — it's a config entry with the right connection type and an exact tool name. Get either wrong, and it fails quietly, not loudly. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Add an MCP server to my plugin that connects to Asana for task management. Watch three things when Claude answers: does the configuration land in `.mcp.json`, not inline inside `plugin.json`? Is the type set to `SSE` — not `stdio`, not `HTTP` — since Asana is a hosted service using OAuth? And does the command's allowed-tools list the exact tool name, `mcp__plugin_asana_asana__asana_create_task`, rather than a wildcard? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | MCP Integration. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the config-declares-a-type fact; the naming/config-file mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (add an app); B01 falsifies it with a case — a local script needs `stdio`, a hosted OAuth service needs `SSE`, and the wrong type simply can't reach it |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documentation of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the exact Asana tool name, `mcp__plugin_asana_asana__asana_create_task`) |
| Both directions | B03 — the exact name works precisely and silently when right; the exact name also fails silently when one underscore is off; a wildcard also "works," at the cost of scope |
| No design judgment | B03 states the tool-name/wildcard tradeoff as a fact about what each string matches, never a verdict on whether Claude Code should report the mismatch |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the tool-naming
  precision, the no-hot-swap constraint, and the thin multi-server docs as
  "what it gets right" / "where it bites" — Teardown language. Plain keeps
  the same underlying fact (a naming mismatch is silent) but states it as a
  mechanism boundary, not a critique of the skill file.
- **Not that all three integration patterns get equal airtime.** The
  source names simple wrapper, autonomous agent, and multi-server; this
  reel compresses to the config-and-naming mechanism the anchor needs
  rather than reciting all three, for a 7-beat Plain cut.
- **No claim about lifecycle restart behavior beyond what's stated.** The
  source notes config changes need a Claude Code restart; this reel
  doesn't re-litigate whether that's a good design, only that config and
  naming have to be exact from the start.

## Handoff prompt (BHTF, read aloud)

> "Add an MCP server to my plugin that connects to Asana for task
> management."

Why it's worth running: watching whether Claude puts the config in
`.mcp.json` (not inline in `plugin.json`), picks `SSE` for a hosted OAuth
service instead of `stdio` or `HTTP`, and writes the exact tool name rather
than a wildcard — three checks straight from the source's own worked
example — surfaces whether the precision from B02/B03 actually lands.

---
**GATE P — signed:** ______________________  (human)
