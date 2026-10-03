# Claude, Applying Brand Guidelines

Does branding a document with Claude mean it's exercising some general
design taste? No — the applying-brand-guidelines skill is a folder Claude
reads before it works: `apply_brand.py`, `validate_brand.py`,
`REFERENCE.md`, and a `SKILL.md` holding the full instruction set in plain
language. Claude reads the steps, executes them in order, then
`validate_brand.py` checks the result — the same way, every time, even
against a document outside the skill's stated scope.

**Topic:** APPLYING-BRAND-GUIDELINES · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-cookbooks--claude-liam-applying-brand-guidelines

---

## Chapters

0:00 The naive framing: "match our brand"
0:08 A skill is a folder Claude reads — not trained on it
0:26 The anchor: three steps, a slide deck through apply_brand.py
0:42 The anchor returns: same input twice, then the scope limit
1:06 Carry-out
1:17 Your turn
1:35 Outro

---

## YOUR TURN

I want to apply brand guidelines to my team's documents. Read the
applying-brand-guidelines skill and walk me through what you will do before
you do it.

Watch for that walk-through — explaining first is what surfaces which steps
`SKILL.md` actually specifies, and where the stated scope stops, rather
than only seeing the finished, rebranded document.

---

## Deliberately not claimed

- Not a verdict on whether the source skill's `SKILL.md` should have
  covered more document types or brand elements — that's Teardown
  territory; this reel states the mechanism and the limit, then stops.
- No specific color codes, font names, or layout rules beyond what the
  source's own narrated description already names — the source `SKILL.md`
  isn't available on this machine, so nothing beyond that is invented.
- Not a claim that the skill decides what counts as "on brand" — only that
  it runs the same steps and the same check regardless of whether the
  document fits the stated scope.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear
