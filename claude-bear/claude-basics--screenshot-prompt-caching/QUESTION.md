# QUESTION

**The question:** "Caching Pixels You've Already Seen." — a computer-use agent
resends the same screenshot on repeat turns; why does that cost tokens again,
and what's the one-field fix?

**Mode:** redo — source is
`anthropics/youtube/claude-basics/screenshot-prompt-caching/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, all 8 primary beats plus 3 unfilled
BOOKEND slates — BVDT/BHTF/BOUT — carrying only placeholder text, never
reconciled with the earlier beats). This reel keeps the question and the
source's body facts, re-registers the narration to Plain, replaces the cold
open with the Brutalist Hesitant Writer, folds the source's B00/B05/YOURTURN
material into a proper carry-out + Your Turn + outro closing block, and
closes with the Humanitarians AI skin.

**Why it earns a reel:** a 50-turn computer-use task takes a screenshot every
turn. 35 of those turns the desktop hasn't changed at all — the identical
image goes out again, and the API re-tokenizes it from scratch every time, at
around 2,000 tokens each. The fix is one field: `cache_control: {"type":
"ephemeral"}`. Flag a screenshot with it once; the API caches that exact
image. Send the identical screenshot again with the same flag and it's a
cache hit — next to no tokens. In the concrete case (50 turns, only 5 unique
desktop states, A through E), that's 5 misses and 45 hits: 5 × 2,000 = 10,000
tokens instead of 100,000. Ninety percent saved. This is the screenshot case
only — not the full caching protocol (minimum cacheable size, eviction
rules), and not the persistent cache tier: the ephemeral cache holds for a
session and doesn't survive an API-key switch or a long idle gap.

**Naive framing (B00, corrected on screen):** "It's the same screenshot, so
sending it again is free, right?" → corrects "free" to "billed" (resending an
identical image is NOT automatically free — it's billed again unless you flag
it as cached).

**Body facts carried from source (unchanged):**
- 50-turn computer-use task, screenshot sent every turn
- 35 of 50 turns: desktop unchanged, identical screenshot resent
- each full-resolution screenshot re-tokenizes at ~2,000 tokens, cache or no
  cache decision aside
- the fix: `cache_control: {"type": "ephemeral"}` attached to the image block
- first sighting of an image = cache miss (full tokens); repeat sighting
  under the same flag = cache hit (near-zero tokens)
- concrete case: 50 turns, 5 unique desktop states (A–E) → 5 × 2,000 = 10,000
  tokens with caching vs. 50 × 2,000 = 100,000 without → 90% savings
- exclusions (source's own honesty beat): does not cover the full caching
  protocol (token-counting rules, minimum cacheable token thresholds, cache
  eviction policy); the cache persists for a session, not across API keys or
  long idle gaps; this is ephemeral caching, not the persistent cache tier
