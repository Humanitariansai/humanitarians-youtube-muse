# QUESTION — claude-for-legal--claude-liam-claim-chart

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-claim-chart/beat_sheet.json`.
That sheet exists and is fully built (7 beats, all marked VIDEO/filled, dated
2026-07-25, Teardown register, skill-teardown format). Unlike the sibling
`amendment-history` and `ai-inventory` redos in this family, this source's
narration text carries **real, actual content** at every skill-specific
point — no unfilled `>` template placeholders. The `source_skill` field
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/claim-chart/SKILL.md`)
does not exist on this machine, but the facts didn't need it: the source
sheet's own narration already states what the `claim-chart` Anthropic Skill
does, verbatim, across B00–BVDT.

**Facts carried over from the source (locked, unchanged):**
- The skill builds or reviews an **element chart** — a patent claim chart
  (infringement, invalidity, or review) or a civil element chart for any
  cause of action or defense.
- Every cell is **pin-cited**.
- **Gap detection is the priority output** — surfacing which elements have
  no supporting citation matters more than a chart that looks complete.
- Triggers: a claim chart, element chart, proof chart, infringement or
  invalidity contention, element-by-element mapping, or "what are we
  missing to prove [claim]."
- It is a `SKILL.md` — a folder Claude reads before acting, plain-language
  instructions, executed in order (Steps section, linear, no branching
  unless a step says so). Same input → same output, every run; the limit
  is only what the file specifies.

**Question this reel actually answers:** What does a finished claim chart
actually prove — and is a chart with every cell filled in the strong
version of it?

**Who asked, where:** nobody — this is the Anthropic-Skill-teardown format;
redone here as a general-audience Plain explainer per `hai-simple`.
**Name usable:** n/a.
