# QUESTION.md

**Question:** Claude picked up a new "skill" called client-letter — did it
actually learn how to write client letters, or is that not what's going on?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-client-letter`, a Teardown skill-explainer
under `anthropics/claude-for-legal/`). Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>` is
still present in four places (B00, B03, BVDT, BHTF), and the SKILL.md it was
meant to describe (`/Users/bear/Documents/CoWork/bear-textbooks/books/
anthropics/claude-for-legal/legal-clinic/skills/client-letter/SKILL.md`) does
not exist on this machine (confirmed: only `youtube/` exists locally under
`anthropics/claude-for-legal/`; no `legal-clinic/` directory). This is the
identical gap already documented on the `claude-for-legal--claude-liam-
case-brief` and `claude-for-legal--claude-liam-build-guide` sibling redos.
See BUILD-LOG.md for how this redo handled it: the source's true, generic
argument (what a skill is, how it executes, why it's a specification with a
limit) is preserved and expanded to meet hai-simple's six-move spine. The
one piece of real, generic, non-invented domain knowledge used as the
anchor's flavor is the well-known shape of a legal client letter itself
(what happened, what it means, what happens next) — not anything about how
this particular unread SKILL.md implements it.
