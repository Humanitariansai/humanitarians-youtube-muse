# QUESTION

**The question:** "Why the same API key that shipped your prototype becomes a
critical bug in production?"

**Mode:** redo — source is
`anthropics/youtube/claude-basics/claudeforfoundationmodels-same-api-key-shipped-prototype/beat_sheet.json`
(scaffold only, never built: build shows `"filled": 0, "of": 8`, no SCRIPT.md,
Teardown register, CHECKS-REPORT.md shows `checks_green: False`). This reel
keeps its question, facts, and body argument, re-registers the narration to
Plain, replaces the cold open with the Brutalist Hesitant Writer, and closes
with the Humanitarians AI skin.

**Why it earns a reel:** a bundled API key works perfectly in development —
and is a shipping-app vulnerability the moment you release, because a
compiled binary can always be decompiled and every string inside it read
straight out, no matter how it was obfuscated. The threat model is what
changed, not the key: production forces the credential behind a backend
relay that injects the real key server-side, which changes how every request
is constructed (`.apiKey("sk-ant-...")` in source → `.proxied(headers:[...])`
against a relay).

**Naive framing (B00, corrected on screen):** "How do I hide my API key
better before I ship?" → corrects "hide" to "move."
