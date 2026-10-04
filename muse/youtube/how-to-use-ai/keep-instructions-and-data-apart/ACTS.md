# ACTS.md — Keep instructions and data apart

Film #5 of the "How to AI" series (24 films). Persona: Liam ("Liam, in for Bear").
Kokoro voice `am_onyx`. Teardown register. Channel `claude-liam`. Watermark `@NikBearBrown`.
Skill: `ai-explainer` (concept explainer; the source supplies the argument, this film
supplies a general-audience rewrite).

## Act 1 — The mix-up (B00–B03, ~103s)
The cold open poses the puzzle: Claude obeyed a line nobody wrote. The hesitant-writer
overview states the whole idea in one breath: pasted text is never just data — it can
sound like orders. Then the film SHOWS it: a pasted email whose buried line orders
Claude to forward the email, and Claude obeys. The mechanism beat explains why: the
prompt is one flat stream, no labels between "mine" and "theirs" — that border is the
attack surface.

## Act 2 — The fence (B04–B06, ~70s)
The fix, demonstrated visually: wrap the instruction in `<instructions>` tags and the
pasted text in `<document>` tags; the sneaky line is trapped inside the document fence
and becomes data, not a command. Multiple documents get numbered fences
(`<document index="1">`). The "why tags" beat explains Claude's familiarity with XML
structure and the key teaching point: tag names don't matter, consistency does.

## Act 3 — Honesty and the takeaway (B07–B10, ~101s)
A fence is not a vault: tags are a convention Claude respects, not a lock — prompt
injection remains the top-ranked AI security risk (OWASP LLM Top 10), so real secrets
stay out of the AI. The verdict lands three lines. The handoff gives the viewer a
paste-ready prompt that fences their own prompts and flags where injections could
have hidden. The outro restates the title; Liam signs off.
