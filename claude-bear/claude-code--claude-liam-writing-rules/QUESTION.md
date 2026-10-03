# QUESTION

**The question:** "Writing Hookify Rules." — if you want Claude to catch a
dangerous command or warn on a risky edit automatically, do you need to write
code, or is there something simpler? Answered using the `writing-rules`
skill's own worked example — a rule that blocks `rm -rf` — as the concrete
case.

**Mode:** redo — source is
`anthropics/claude-code/youtube/claude-liam-writing-rules/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`anthropics/claude-code/plugins/hookify/skills/writing-rules/SKILL.md`.
7 beats — B00 cold open, B01 anatomy, B02 design, B05 teardown, BVDT verdict,
BHTF handoff, BOUT outro — B00 was already `ClaudeComposerAsk` REMOTION, not
AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no substitution beyond
the WRITER LAW swap). This reel keeps the question and the source's body
facts, re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, restates the source's B05 "gets right / bites" as a
both-directions mechanism fact instead of a design judgment, and closes with
the Humanitarians AI skin.

**Why it earns a reel:** A hookify rule is a markdown file with YAML
frontmatter, saved at `.claude/hookify.{name}.local.md`, read dynamically on
every tool use — no compiling, no restarting. Five frontmatter fields: name
(kebab-case, verb-first), enabled (bool), event (bash / file / stop / prompt
/ all), pattern (a regex, the simple form) or conditions (an array of
field + operator + pattern, the advanced form — ALL must match), and action
(warn by default, or block). The markdown body after the frontmatter is the
message Claude sees when the rule fires — what was detected, why it matters,
what to do instead. Two pitfalls sit on opposite sides of pattern precision:
too broad (`log` also matches `catalog` and `login`) fires on things nobody
meant to catch; too specific (`rm -rf /tmp` only) misses the identical danger
typed against a different path.

**Naive framing (B00, corrected on screen):** "How do I write a script to
stop Claude from running rm -rf?" → corrects "script" to "rule" (no code is
involved; a hookify rule is a markdown file Claude reads before every tool
call, not a program you write and run).

**Body facts carried from source (unchanged):**
- a hookify rule is a markdown file with YAML frontmatter, at
  `.claude/hookify.{name}.local.md`, read dynamically on every tool use
- five frontmatter fields: name (kebab-case, verb-first), enabled (bool),
  event (bash / file / stop / prompt / all), pattern or conditions, action
  (warn default, or block)
- simple format: one `pattern` field (regex); advanced format: a
  `conditions` array — each entry is field + operator + pattern, ALL must
  match; six operators: regex_match, contains, equals, not_contains,
  starts_with, ends_with
- four content event types: bash (Bash tool command strings), file
  (Edit/Write/MultiEdit — matches `new_text` by default, or `file_path` /
  `old_text` / `content` via the advanced format), stop (catch-all pattern
  with a checklist body), prompt (user input) — plus `all`
- message body: explain what was detected, why it's a problem, what to do
  instead
- pitfalls: too-broad pattern (`log` matches `catalog`/`login`), too-specific
  pattern (`rm -rf /tmp` catches only that one path), YAML escaping
  (unquoted patterns recommended — quoted strings need doubled backslashes)
- source's Your Turn worked example: a rule blocking `rm -rf`, and a
  separate rule warning on `.env` edits
