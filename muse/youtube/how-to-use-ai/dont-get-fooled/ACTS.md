# ACTS.md — Don't get fooled.

An ai-explainer concept film for the humanitarians AI YouTube channel: why
AI sounds sure when it's wrong, and the three habits that keep you safe —
grounding, citing, and cross-checking.

**Exact title:** Don't get fooled.

**Core promise:** By the end, the viewer can say what a hallucination is in
plain words (the AI making things up confidently), knows that a confident
tone is never proof, and walks away with three concrete habits: feed the AI
the source and make it answer only from it; give it permission to say "I
don't know"; make it quote the passage and check the quote; cross-check
anything that matters.

**Structure:** Cold open → hesitant-writer BLUF → three acts → verdict
recap → your-turn handoff → title-restate outro.

- Cold open (B00): the composer asks the film's question — "Why does the
  AI sound so sure when it's wrong?" — and answers it in two lines.
- BLUF (B01): the hesitant writer corrects "AI lies to you because it's
  badly trained" → "AI guesses the most likely words, not the truth", plus
  the stakes: three small habits keep you safe.
- Act 1 — why it lies to you (B02–B04): the next-word-prediction mechanism;
  habit zero (the confident tone tells you nothing); the true story of the
  lawyer who filed six invented court cases (Mata v. Avianca, 2023).
- Act 2 — the three-sentence fix (B05–B06): grounding — paste the source,
  answer only from it; the "I don't know" permission.
- Act 3 — the audit habits (B07–B09): quote the exact sentence and check it
  (hallucinated citations are catchable); cross-check anything that
  matters; the three-sentence card to keep.
- BVDT — verdict recap (the mechanism / the fix / the audit).
- BHTF — your turn: paste the grounding prompt into Claude with a
  Wikipedia article; ask what it covers and what it doesn't.
- BOUT — title restate, spoken sign-off.

**Tone:** Teardown at its plainest — short sentences, every term defined in
the same breath it appears, no jargon left standing. Liam's voice, warm and
direct. The film judges a design (the next-token predictor's indifference
to truth) and hands the viewer a working practice.

**What this film is not:** not a lecture on how language models are
trained — the mechanism is one beat, in plain words. Not a legal analysis
of Mata v. Avianca — the case is a one-beat cautionary example, reported
facts only. Not a product demo — no real AI interface is shown; the
composer is a drawn Claude-style card.

**Source facts:**
- Anthropic Prompt Engineering Tutorial · Lesson 8 ("Avoiding
  Hallucinations"): hallucination is a structural property of an
  ungrounded next-token predictor; confidence and correctness are
  uncorrelated; the three-part grounding pattern (source in prompt,
  answer only from it, "I don't know" permitted); citations extend
  grounding to the output side. (mirror repo PEDAGOGY.md verdict +
  Lesson-08 sheet; see SOURCES.md) [record]
- Mata v. Avianca (S.D.N.Y., 2023): attorney Steven Schwartz used ChatGPT
  for legal research; the brief cited six fictitious cases (e.g.
  "Varghese v. China Southern Airlines, 925 F.3d 1339 (11th Cir. 2019)");
  Judge P. Kevin Castel sanctioned Schwartz, LoDuca, and the firm $5,000.
  (Reuters, 2023-06-22; corroborating coverage) [record]

**Skill:** ai-explainer. One drawing per beat; the Claude-style composer
card is the cast object at the bookends (cold open, handoff) and the
verdict card recaps the three habits. Kept (not switched): the film is a
concept walkthrough — the ai-explainer lane.
