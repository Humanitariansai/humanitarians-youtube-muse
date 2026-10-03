# Why web search never runs your code but your own tool always does — with identical syntax

`.webSearch(maxUses: 5)` in `serverTools` and a Swift `lookupFavorites()` in
`tools` are declared the same way, in the same file — yet web search's
result lands inside the same turn, while `lookupFavorites()` forces the
model to stop and wait for a second request. The split isn't about how the
tool is declared, it's about who can execute it. Web search runs on
infrastructure Anthropic already owns (a web index, a sandbox), so Anthropic
finishes the call itself, in-turn. A client-side tool is arbitrary code on
the caller's device — only the caller can run it, which forces an
exit-and-return, no matter how trivial the function is or how often the
server-side tool fires.

**Topic:** CLAUDE BASICS · WHO HOLDS EXECUTION
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--claudeforfoundationmodels-web-search-never-runs-code

---

## Chapters

0:00 A tool call should always round-trip through my code?
0:10 Same declaration, different behavior
0:25 The anchor: serverTools vs. tools
0:43 Why: who can execute
1:01 The anchor returns: tested both ways
1:23 Carry-out
1:34 Your turn
1:55 Outro

---

## YOUR TURN

In my Claude app, I have one tool declared as a server-side tool, like web
search, and one declared as a client-side tool that calls my own code. Walk
me through what happens at the network level for each — how many
round-trips, who executes the tool, and where the result enters the
conversation — so I can reason about latency budgets in my app.

Run that today, against your own tool mix.

---

## Deliberately not claimed

No claim about domain filtering, `maxUses` rate limiting, or the tool-result
schema — the source excludes these explicitly as follow-on questions. No
verdict on which pattern is "better" — explaining why the round-trip split
exists is not the same as ruling on whether you should prefer server-side or
client-side tools. Not the only kind of split — the `.webSearch`/
`lookupFavorites` pair is one concrete instance of the general rule, not an
exhaustive list.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicAPI #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
