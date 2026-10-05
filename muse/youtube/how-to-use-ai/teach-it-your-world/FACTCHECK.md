# FACTCHECK.md — "Teach it your world"

Verified 2026-10-04. Claims are labeled [record] (checked against a source),
[reasoning] (derived, no external claim needed), or [common knowledge].
Sources live in SOURCES.md. No invented statistics anywhere in the film.

## Factual claims in the narration, beat by beat

**B00.** "It knows the world. It does not know my world." — [reasoning]:
illustrative cold open. The composer output (a generic packing list) is an
illustrative example, not a recorded session; the beat is framed as a
demonstration ("Watch:"), not a transcript. No factual claim about any
product's actual output.

**B01.** "Upload your own documents … and it stops answering from the
internet and starts answering from your world." — [reasoning] from the two
product facts below (attachments; project knowledge). Framed as the film's
thesis, demonstrated in the body.

**BDEFS.**
- "knowledge base: your own documents, gathered in one place for the AI" —
  [record]: Anthropic's help center calls the Projects upload space a
  "project knowledge base" ("Add content to project knowledge"; "project
  knowledge search tool"). Genericized for the audience.
- "upload: copying a file into the chat so the AI can read it" —
  [common knowledge], corroborated by press coverage of in-chat file upload
  support (see SOURCES.md).
- "grounding: answering only from the material you handed it" — [record]:
  the standard "answer only based on the context" instruction from
  Anthropic's prompt-engineering guidance (same lineage the sibling film
  "Don't get fooled" cites from the Prompt Engineering Tutorial, Lesson 8).
- "RAG: the AI searches your documents, then answers from what it finds" —
  [record]: Anthropic help, "Retrieval augmented generation (RAG) for
  projects": "Claude uses a project knowledge search tool to retrieve
  relevant information from your uploaded documents. Instead of loading all
  project content into memory at once, Claude intelligently searches and
  retrieves only the most relevant information needed to answer your
  questions."

**B02.** "The AI trained on the internet — it knows everyone's everything,
and nobody's specifics." — [reasoning]: a plain-words gloss of training on
public data; the beat's worked claim (no rota → a guessed answer) is the
film's running illustration, consistent with the hallucination mechanism the
sibling film "Don't get fooled" documents. No product behavior asserted.

**B03.** "Most AI apps let you attach files to a conversation, including
Claude's." — [record]: file upload into Claude conversations is documented
in press coverage of the feature (PCWorld 2025-09-11; PPC Land notes uploads
up to 30MB; webpronews on uploading datasets for analysis). "Claude's
projects keep your documents on hand, so every chat in that project starts
already knowing them." — [record]: Anthropic help, "How can I create and
manage projects?": "You'll find the project knowledge base on the right side
of your project's main page. Anything you upload to this space will be used
across all of your chats within that project."

**B04.** "Anthropic's own help pages describe exactly this: a search tool
that retrieves only the most relevant information from your uploaded
documents." — [record]: near-verbatim paraphrase of the RAG-for-projects
help article quoted under BDEFS; the article was opened and read live on
2026-10-04. "It does not read all your documents — that would take
forever." — [reasoning]: the article's stated rationale ("Instead of
loading all project content into memory at once").

**B05.** "Every word becomes a point on a map … Points for similar meanings
sit near each other." — [reasoning]: the standard embeddings intuition,
taught as a metaphor ("the 'embeddings' idea, in plain words"). No
implementation claim about any product's retrieval stack. The
invoice/receipt/bill vs elephant example is illustrative, not measured.

**B06.** "If you would attach it to an email to brief a new colleague, it
belongs in the AI's world too." — [judgment]: the film's own heuristic,
framed as a rule of thumb, not a sourced fact.

**B07.** Habit 1 ("attach the file, or keep it on the project's shelf") —
[record]: attachments (B03) + project knowledge (B03). Habit 2 ("say 'answer
only from these files,' and name the document") — [reasoning] from
Anthropic's RAG best practices: "Reference specific documents — When asking
questions, you can reference specific documents by name to help Claude focus
its search" (RAG-for-projects article). Habit 3 ("make it quote … check
the quote") — [reasoning]: citation-as-verification, the output-side
companion of grounding (same lineage as BDEFS grounding).

**B08.** "The AI never warns you about what's missing" — [reasoning]: a
retrieval system answers from retrieved content; absence of retrieval is not
surfaced as a warning. Framed as the film's teardown judgment, not a product
claim. "Stale documents give stale answers" — [reasoning]: uncontroversial;
the narration presents it as housekeeping advice. "It trusts your uploads
completely. A wrong document does not get flagged; it gets quoted." —
[reasoning]: the known failure mode of grounded generation (the retriever
retrieves, the model answers from what it retrieves); presented as the
teardown judgment, consistent with "garbage in, garbage out."

**BVDT.** The falsifiable line ("ask about something only your docs know. A
generic answer means it never read them.") — [reasoning]: an operational
test the viewer can run; falsifiability is the skill's requirement, not a
factual claim.

**BHTF.** The viewer prompt is an original composition; its check lines are
the film's own self-checks. No factual claims.

## Deliberately excluded / hedged

- No model names or version numbers (DOUBLE-CHECK LAW: datable).
- No pricing or plan names ("including Claude's" is the only product
  reference; plan-dependent details like per-project limits are omitted).
- No file-type lists (they churn; the film says "the rota, the manual, the
  notes").
- The B00 composer exchange is a drawn illustration, not a recorded session;
  CHECKS-REPORT.md notes this.
