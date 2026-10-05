# ACTS.md — "Teach it your world" (slug `teach-it-your-world`)

ai-explainer concept film for the humanitarians AI YouTube channel: upload
your documents so the AI answers from YOUR material — personal knowledge
bases, explained non-technically. Persona: Liam ("Liam, in for Bear,");
Kokoro voice `am_onyx`; Teardown register; channel `claude-liam`;
watermark `@NikBearBrown`.

**Skill:** ai-explainer — SWITCHED from the assigned cc-explainer (see
BUILD-LOG.md: cc-explainer's REAL-SESSION LAW needs an actually-run `claude`
CLI session, which cannot exist in this VM — no CLI, no credentials; inventing
one would be a DOUBLE-CHECK LAW violation. The pitch is a concept explainer
for a non-technical audience, which is ai-explainer's lane: "a Claude-branded
concept walkthrough").

## The argument (one paragraph)

The AI knows the world's knowledge — it does not know your world. Ask it about
your trek, your team's rota, your policies, and it answers with everyone's
generic version, or invents one. Hand it your own documents and it stops
answering from the internet and starts answering from your material: it
searches your documents like a librarian, pulls only the matching pages (this
is RAG — retrieval augmented generation), and reads those before it answers.
It finds the right pages because words with similar meanings sit near each
other on a map (embeddings, in plain words). Three habits make it stick: give
it the source, pin it down ("answer only from these files"), and make it quote
the exact line it used. And the teardown: it never warns you about what's
missing, stale documents give stale answers, and it trusts your uploads
completely — garbage in, confident garbage out.

## Acts

| Act | Beats | Job |
|---|---|---|
| the question | B00 | Cold open: composer asks a personal question, gets the internet's generic answer |
| the idea | B01 | Hesitant-writer BLUF: "AI is smart because it knows everything" → "when you give it your material" |
| terms | BDEFS | 4 terms: knowledge base, upload, grounding, RAG — one plain line each |
| the gap | B02 | The problem: your question goes to the internet's knowledge, comes back a guess |
| the fix | B03 | Pages drop into the box; the guess straightens into an answer with a check |
| the librarian | B04 | RAG performed: searches the shelf, pulls only the matching pages |
| meaning map | B05 | Embeddings in plain words: similar meanings cluster; "not the elephant" |
| what to upload | B06 | Three boxes fill: your notes, work docs, only-you-know |
| three habits | B07 | Three stamped cards: give it the source · pin it · make it quote |
| where it bites | B08 | Teardown: blind spots, stale in/stale out, wrong doc = confident quote |
| verdict | BVDT | Artifact card: mechanism, practice, falsifiable test |
| your turn | BHTF | Composer: paste a rota, pin it, quote it — read aloud, two self-checks |
| outro | BOUT | Spoken title + "At Nik Bear Brown" + "Liam, in for Bear" |

## Deliberate anti-rot choices

- Product surface described generically ("most AI apps let you attach files
  to a conversation, including Claude's") with the one worked example
  (Claude projects' knowledge shelf) kept to behavior, never to button
  positions or plan names.
- No model names, no version numbers, no pricing, no file-type lists — the
  film teaches the pattern (source → search → pin → quote), not the release
  notes.
- The RAG definition follows Anthropic's own help article verbatim in spirit
  ("retrieves only the most relevant information from your uploaded
  documents"); the librarian and meaning-map are metaphors the narration
  flags as explanations, not product claims.

## What this film is not

- Not a RAG engineering tutorial — no vectors, no chunking, no indexes named.
- Not a product demo — no real interface is shown; the composer is a drawn
  Claude-style card (ILLUSTRATE LAW: the UI is the subject only at the
  bookends).
- Not the secrets film (`what-never-to-paste-into-ai`) — B08 covers
  misplaced trust and staleness, not PII handling.
