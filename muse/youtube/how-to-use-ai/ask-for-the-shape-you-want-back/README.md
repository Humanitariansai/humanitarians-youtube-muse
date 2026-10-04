# Ask for the Shape You Want Back

**How to AI #4** · show-tell · Teardown register · Liam ("Liam, in for Bear")
· Kokoro `am_onyx` · channel `claude-liam` · watermark `@NikBearBrown`

**Pitch:** Formatting output: tables, bullets, length, tone.

Ask Claude a vague question and you get a vague answer back. This film shows the
fix: name the shape (a table with columns), give the answer a size (under 100
words), pick the tone (friendly email, not a formal letter), match the format to
where the answer is going — and, for developers, the strongest version of the
trick: prefilling, where you write the first character of Claude's answer yourself
and it has to continue your shape. Plus two warnings: a tidy table can still be
wrong, and don't over-engineer the ask.

- 13 beats (2 bookends, 9 isometric Manim drawings, Your Turn composer, spoken outro)
- 9 Manim scenes · est. 246 s (~4.1 min)
- Refactor of `claude/claude-for-education/claude-liam-prompt-tutorial-lesson-05-formatting-output`
  (Anthropic Prompt Engineering Tutorial, Lesson 05: Formatting Output)

**Status:** pre-render package complete (script, drawings, docs). Static QC:
9 scenes clean, 0 warnings, 0 errors. Render + narration on Bear's Mac —
see `CLAUDE-CODE-RENDER.md`. Layout audit (`--curve-strict`) deferred to the
render pass (no Manim in the build VM).
