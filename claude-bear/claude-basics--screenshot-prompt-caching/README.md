# Caching Pixels You've Already Seen.

A computer-use agent takes a screenshot on every turn, and often the desktop
hasn't changed — the exact same image goes out again. The API re-tokenizes
it from scratch every time: at roughly 2,000 tokens per screenshot, a
50-turn task with 35 repeats can burn 70,000 tokens re-reading pictures
Claude has already read. The fix is one field: `cache_control: {"type":
"ephemeral"}`. Flag a screenshot with it once and the API caches that exact
image; send the identical screenshot again with the same flag and it's a
cache hit — next to no tokens. In the worked case — 50 turns, only 5 unique
desktop states (A through E) — that's 5 misses and 45 hits: 10,000 tokens
instead of 100,000, a 90% savings. This is the screenshot case only: it
doesn't cover the full caching protocol (minimum cacheable size, eviction
rules), and the cache isn't permanent — an API-key switch or a long idle gap
empties it regardless of whether the picture changed.

**Topic:** COMPUTER USE · PROMPT CACHING
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--screenshot-prompt-caching

---

## Chapters

0:00 It's the same screenshot, so sending it again is free, right?
0:12 The naive loop, unpriced
0:38 The concrete case: 100,000 tokens uncached
0:55 One field: cache_control ephemeral
1:15 Cut down, and the scope limit
1:39 Carry-out
1:48 Your turn
2:07 Outro

---

## YOUR TURN

"My computer-use agent re-sends an identical screenshot up to 35 times in a
50-turn task — add ephemeral prompt caching and show me the token savings,
before and after."

Ask Claude to write the caching wrapper, then check: does it handle a
screenshot that changed only slightly, not identically?

---

## Deliberately not claimed

Not a savings guarantee for every deployment — the 90% figure is this reel's
worked case (5 unique states out of 50 turns), not a promise. Not the full
caching protocol — minimum cacheable token thresholds and eviction policy
aren't covered. Not permanent — the cache holds for a session; an API-key
switch or a long idle gap empties it regardless of whether the screenshot
changed.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ComputerUse #PromptCaching #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
