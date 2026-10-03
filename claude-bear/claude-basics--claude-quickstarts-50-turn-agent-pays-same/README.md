Why a 50-turn agent pays for the same screenshot 35 times unless it caches the pixels

A 50-turn computer-use agent that only ever sees 5 unique desktop states still burns 50 × 2,000 = 100,000 image tokens if every screenshot gets reprocessed from scratch — naive math for a task with 5 actual pictures. The natural assumption is that if the model already saw a screenshot once, showing it again should be nearly free. It isn't: an API call carries no memory between requests, so every turn resends the entire conversation, images included, and the model reprocesses all of it from scratch, every single time. The fix is to hash the screenshot and mark it cached the first time it's sent — the next turn that sends the identical hash hits the cache instead of paying to reprocess it. Back to the 50-turn task: only 5 states ever get tokenized in full, 10,000 tokens instead of 100,000. It only pays off when a screen repeats byte-for-byte; a moved cursor or a genuinely new page is a different state, billed like anything else.

Claude Basics — the questions a general audience actually asks about Claude and AI, answered simply. Liam, in for Bear.

0:00 The question
0:11 The stakes — a 50-turn task, 5 unique states
0:25 The wrong guess — "the model already saw it, so it's free"
0:34 Why it breaks — no memory between API calls
0:46 The fix — hash it, mark it cached
0:58 The payoff — 10,000 tokens instead of 100,000
1:13 Both directions — only when the screen repeats exactly
1:25 Both directions — not when the screen actually changes
1:37 Carry-out
1:47 Your turn
2:07 Outro

Your turn: paste this into Claude —
"I'm building a 50-turn computer-use agent that revisits the same 5 desktop states repeatedly. Show me exactly where to place `cache_control` on the screenshot messages so each unique state is only billed once, and write the code that detects a repeated state and routes to the cached version instead of sending the raw image again."

This video was scripted and narrated with AI assistance (Kokoro text-to-speech, voice: Liam) and produced with Claude Code; every technical claim was checked against the source material before rendering.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--claude-quickstarts-50-turn-agent-pays-same

Playlist: Claude Basics

#Claude #PromptCaching #ComputerUse #AI

youtube.com/@HumanitariansAI
