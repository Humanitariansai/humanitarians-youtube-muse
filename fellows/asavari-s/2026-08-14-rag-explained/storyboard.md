# Storyboard — RAG, Explained

_Fellow: Asavari (Ash) Shejwal · AI / STEM · 2026-08-14 · 16:9 + 9:16_

Brutalist explainer, framework-first (PROOF standard). One visual per beat; automated narration.

## Beat 1 — AI ENGINEERING

**On screen:** RAG, Explained

**Narration:** Here's a question that trips people up. How can an AI answer questions about your company's documents, when it was never trained on them? The answer is a pattern called RAG, retrieval augmented generation. And the key idea is simple. The model doesn't memorize your files. It looks them up at the moment you ask, pulls the relevant passages, and then answers using them. Retrieve first, generate second.

## Beat 2 — THE PROBLEM

**On screen:** A model only knows what it was trained on.

**Narration:** Start with the problem RAG solves. A language model only knows what it saw during training. Ask it about your internal document, last week's filing, anything private or recent, and it has two options. Admit it doesn't know, or, far more often, invent something that sounds right. That confident invention is the hallucination everyone worries about. The model isn't lying. It simply has no source.

## Beat 3 — THE MECHANISM

**On screen:** Retrieve the right passages, then generate.

**Narration:** Here's how RAG works, step by step. Your documents are split into chunks and indexed, so they can be searched by meaning, not just keywords. When a question comes in, the system finds the handful of passages most relevant to it. Those passages get handed to the model along with the question, and the model is told, answer using this. So the answer is grounded in retrieved text, with citations you can check, not pulled from the model's fuzzy memory.

## Beat 4 — THE LIMIT

**On screen:** RAG is only as good as what it retrieves.

**Narration:** But here's the catch, and it's the part people skip. RAG doesn't fix hallucination. It moves the risk. If the retrieval step pulls the wrong passages, the model will write a fluent, confident answer on top of the wrong evidence, and it will look just as trustworthy as a correct one. So the hard problem in RAG isn't the generation. It's retrieval. Chunking, search quality, and knowing when nothing relevant was found. Garbage in, confident garbage out.

## Beat 5 — THE TAKEAWAY

**On screen:** Judge a RAG system by its retrieval, not its prose.

**Narration:** So how do you judge a RAG system? Not by how good the answer sounds, that's the easy part to fake. Ask whether it cites the passages it used, and whether you can open them and check. Ask what it does when nothing relevant exists. Does it say so, or answer anyway? And ask whether anyone is actually measuring retrieval quality, or just eyeballing the output. A RAG answer you can trace beats a polished one you can't. Same lesson as always: no source, no verdict.
