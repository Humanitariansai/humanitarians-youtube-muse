Why splitting a chunk from its document makes it retrieve for the wrong question

A chunk pulled out of a document for search keeps its own words but loses its place in the document — and that's enough to make it retrieve for the wrong question. A medical-paper chunk that reads "This treatment reduced mortality by 12%," with no disease named, gets handed to any mortality query, right disease or not. The fix: generate a short summary of the whole document and prepend it to the chunk before embedding, so the vector carries the chunk's content *and* its context. Across ten test queries on that same chunk, precision moved from 33% to 90% — but only because the chunk was ambiguous to begin with. A chunk that already names its subject gains nothing, and this doesn't repair a bad summary or a broken chunking strategy — it fixes one specific failure, not retrieval in general.

Claude Basics — the questions a general audience actually asks about Claude and AI, answered simply. Liam, in for Bear.

0:00 The question
0:10 The stakes — a medical chunk, no disease named
0:20 The wrong guess — word match should be enough
0:28 Why it breaks — handed to the wrong query
0:38 The fix — prepend context before embedding
0:51 The payoff — precision 33% → 90%
1:04 Both directions — when it doesn't help
1:12 One failure, not all of retrieval
1:22 Carry-out
1:30 Your turn
1:51 Outro

Your turn: paste this into Claude —
"I have a research paper being split into chunks for RAG. A chunk says 'This treatment reduced mortality by 12%' with no disease name in context. Show me how to prepend a context header to each chunk before embedding, what fields should be in that header, and how I'd verify the fix is actually preventing false matches on unrelated queries."

This video was scripted and narrated with AI assistance (Kokoro text-to-speech, voice: Liam) and produced with Claude Code; every technical claim was checked against the source material before rendering.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--claude-cookbooks-splitting-chunk-from-document-makes

Playlist: Claude Basics

#Claude #RAG #ContextualRetrieval #AI

youtube.com/@HumanitariansAI
