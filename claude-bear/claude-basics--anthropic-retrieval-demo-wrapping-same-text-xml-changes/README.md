# Why wrapping the same text in XML changes the answer Claude gives

Paste a paragraph in as plain text and ask Claude for a summary — it comes
back generic. Paste the identical words again, this time wrapped in XML tags,
and the summary gets sharp. Nothing about the content changed, only its shape.
This video explains why: Claude was trained on enormous amounts of
consistently tagged, structured text, and inputs that match that shape get
processed more coherently than inputs that don't. Wrapping text in XML isn't
a trick — it's speaking the shape Claude was trained to expect.

**Topic:** CLAUDE BASICS · INPUT STRUCTURE
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-basics--anthropic-retrieval-demo-wrapping-same-text-xml-changes

---

## Chapters

0:00 Is XML just decoration?
0:11 The puzzle: same words, different answer
0:20 The anchor: one product description
0:33 Why: trained on the shape
0:51 The anchor returns: Robot Building Kit
1:08 Carry-out
1:16 Your turn
1:35 Outro

---

## YOUR TURN

Open a Claude conversation. Paste in any short paragraph of product or
document text, once as plain text, and ask for a summary. Then paste the
identical text again, wrapped in XML tags — title, content, category,
whatever fields fit — and ask for the same summary. Compare the two answers.

Run that today — on your own text, not the video's example.

---

## Deliberately not claimed

Not that XML is the only structure that works, and not a claim about
tokenization or attention internals — the video stays at the level of
training-distribution expectation, and does not rule on whether you should
always tag your prompts.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #PromptEngineering #LLM #HumanitariansAI #ProfessorBear #ClaudeBasics

---
