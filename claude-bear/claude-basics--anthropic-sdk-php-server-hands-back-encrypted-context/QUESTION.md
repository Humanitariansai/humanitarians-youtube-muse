# QUESTION

**The question:** "Why does the server hand back an encrypted context you're only going to echo?"

**Mode:** redo — source is
`anthropics/youtube/claude-basics/anthropic-sdk-php-server-hands-back-encrypted-context/beat_sheet.json`
(scaffold only, never built: 0/8 beats filled, no SCRIPT.md, Teardown register).
This reel keeps its question, facts, and body argument, re-registers the
narration to Plain, replaces the cold open with the Brutalist Hesitant Writer,
and closes with the Humanitarians AI skin.

**Why it earns a reel:** when a long conversation triggers compaction, the
response carries back TWO fields — a human-readable `content` summary and an
opaque `encrypted_content` blob. The natural assumption is that the readable
summary, being the part you can actually understand, is what "remembers" the
conversation, so passing it back should be enough. It isn't: the readable
text is display/debug only, while the encrypted blob is a server-verifiable
token that reconstructs the full compressed context — turn boundaries, roles,
metadata — that plain prose throws away.

**Naive framing (B00, corrected on screen):** "The summary is what Claude
remembers, right?" → corrects "remembers" to "shows you."
