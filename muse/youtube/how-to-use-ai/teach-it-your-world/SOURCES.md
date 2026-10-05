# SOURCES.md — "Teach it your world"

Primary sources checked 2026-10-04. Secondary press corroboration for the
file-attachment claim. No statistics quoted in the film, so no datasets.

## Anchor source (read live 2026-10-04)

1. **Anthropic Help Center — "Retrieval augmented generation (RAG) for
   projects"** — https://support.anthropic.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
   - Used for: the RAG definition (BDEFS), the librarian mechanism (B04),
     the "name the document" best practice (B07 habit 2), and the project
     knowledge behaviors. Key lines: "RAG or retrieval augmented generation
     is a technology that allows your projects to store and access
     significantly more knowledge than before"; "Claude uses a project
     knowledge search tool to retrieve relevant information from your
     uploaded documents"; "Instead of loading all project content into
     memory at once, Claude intelligently searches and retrieves only the
     most relevant information needed to answer your questions";
     "Reference specific documents — When asking questions, you can
     reference specific documents by name to help Claude focus its search."

## Product behavior

2. **Anthropic Help Center — "How can I create and manage projects?"**
   (retrieved via search-result mirror at
   https://github.com/harishpiyer/claude-code-docs/blob/HEAD/content/support/9519177-how-can-i-create-and-manage-projects.md
   — a mirror of the Anthropic support document; quoted text is the
   support article's own wording)
   - Used for B03: "You'll find the project knowledge base on the right side
     of your project's main page. Anything you upload to this space will be
     used across all of your chats within that project." Also notes the RAG
     mode link for large project knowledge.

3. **File attachments in Claude conversations** (press corroboration;
   claim kept generic in the film):
   - PCWorld, 2025-09-11, "Anthropic's Claude AI chatbot can now create and
     edit Office files" —
     https://www.pcworld.com/article/2906610/anthropics-claude-ai-chatbot-can-now-create-and-edit-office-files.html
   - PPC Land, "Claude launches file creation for professional documents" —
     https://ppc.land/claude-launches-file-creation-for-professional-documents/
     (notes uploads up to 30MB; CSV/XLSX analysis workflows)
   - webpronews.com, "Anthropic's Claude AI Adds In-Chat Excel Editing" —
     documents uploading datasets into chats for analysis.

## Technique lineage

4. **Anthropic Prompt Engineering Tutorial, Lesson 8 ("Avoiding
   Hallucinations")** — the grounding pattern (source in prompt, "answer
   only based on the context", "I don't know" permitted) that BDEFS's
   "grounding" and B07's pin-and-quote habits descend from. Same lineage the
   sibling film "Don't get fooled" cites (mirror repo PEDAGOGY.md verdict +
   Lesson-08 sheet).

## Corrections applied (DOUBLE-CHECK LAW)

- The B01 hesitant-writer text was drafted as "AI is smart because it knows
  everything" → corrected to the film's claim, matching the writer's
  contract (the correction IS the pedagogy).
- An early draft said "Claude reads every document before answering"; fixed
  to the article's actual mechanism (search + retrieve only the relevant
  parts) — B04.
- Model names, plan names, and file-type lists were stripped from the
  narration during drafting as datable/churn-prone.
