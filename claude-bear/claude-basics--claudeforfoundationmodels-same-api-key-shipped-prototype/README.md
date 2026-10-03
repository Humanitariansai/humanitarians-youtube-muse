# Why the same API key that shipped your prototype becomes a critical bug in production

A bundled API key works perfectly in development — and is a shipping-app
vulnerability the moment you release, because a compiled binary can always
be decompiled and every string inside it read straight out, no matter how it
was obfuscated. The instinct is to hide the key harder; that never works.
The threat model is what changed, not the key: production forces the
credential behind a backend relay that injects the real key server-side,
which changes how every request is constructed
(`.apiKey("sk-ant-...")` in source → `.proxied(headers:[...])` against a
relay) — and that boundary is only needed once a user can hold the binary,
not on a server you fully control.

**Topic:** CLAUDE BASICS · WHERE A SECRET LIVES
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--claudeforfoundationmodels-same-api-key-shipped-prototype

---

## Chapters

0:00 How do I hide my API key better?
0:10 Same key, flipped risk
0:25 The anchor: dev code vs. release code
0:41 Why: same lock, different holder
0:54 The anchor returns: one boundary, not everywhere
1:13 Carry-out
1:22 Your turn
1:44 Outro

---

## YOUR TURN

I'm building an app that calls the Claude API directly with a bundled key,
and I need to ship it. Walk me through the backend relay pattern I need:
what my app should send instead of the key, what the minimum relay server
needs to do, and how it keeps the real key safe even if someone decompiles
my app.

Run that today, against your own app.

---

## Deliberately not claimed

No specific obfuscation technique is named as broken — the point is that
obfuscation as a category doesn't change what's extractable from a shipped
binary. Not OAuth, token refresh, or App Attest attestation mode. No verdict
on whether the relay pattern is the "right" architecture — that's a design
judgment this video doesn't make.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicAPI #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
