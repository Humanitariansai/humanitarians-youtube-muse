# Why the server hands back an encrypted context you're only going to echo

When a long conversation triggers compaction, the response carries back TWO
fields — a human-readable `content` summary and an opaque `encrypted_content`
blob. The natural assumption is that the readable summary, being the part you
can actually understand, is what "remembers" the conversation, so passing it
back should be enough. It isn't: the readable text is display/debug only,
while the encrypted blob is a server-verifiable token that reconstructs the
full compressed context — turn boundaries, roles, metadata — that plain prose
throws away. This video walks through a twenty-turn compaction case where
threading the summary back breaks context, and threading the blob back holds.

**Topic:** CLAUDE BASICS · CONTEXT COMPACTION
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--anthropic-sdk-php-server-hands-back-encrypted-context

---

## Chapters

0:00 Is the summary what Claude remembers?
0:11 Two things come back: summary and blob
0:26 The anchor: a twenty-turn conversation
0:45 Why: display text vs. server-verifiable token
1:00 The anchor returns: one token, not a replay
1:17 Carry-out
1:24 Your turn
1:43 Outro

---

## YOUR TURN

You're building a multi-turn PHP app with the Anthropic SDK. Show me how to
detect a compaction block in the response, and write the code that threads
the `encrypted_content` blob — not the human-readable summary — back into
the next `messages` array. Explain what breaks if you send the summary text
instead.

Run that today, against your own PHP integration.

---

## Deliberately not claimed

Not how the token is encrypted, or what algorithm is used. Not when
compaction triggers or how to configure it manually. Not a verdict on
whether this is the "right" way to handle context overflow — that's a
design judgment this video doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicSDK #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
