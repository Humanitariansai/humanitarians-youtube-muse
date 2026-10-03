# Cowork Prompt — Glossary Builder

Build a quality `key-terms/Glossary.md` for a book: aggregate the terms the chapters
already declare, define each in the book's voice, attach a sourced citation wherever the
project's `facts/<topic>/` knowledge slice has one, and assemble an A–Z glossary with
chapter tags. Deterministic where possible, AI only for the definitions.

This is the reusable method. It was first validated on `branding-and-ai` (209 terms).
Later passes can reuse the same `Glossary.md` to (a) drop a per-chapter glossary appendix
into chapters, or (b) export Anki cards — both read the same entry structure.

---

## Inputs

- `chapters/*.md` — each may contain a `## Key Terms` section: a line of terms separated by ` · ` (middot).
- `facts/<topic>/` (sibling of `books/`, at `../../facts/<topic>/`): `terms.json`, `facts.json`, `graph.json`.
  Optional — if absent, the glossary still builds, just without citations or the gaps appendix.
- The book's voice and the actual chapter text (the definitions must reflect how *this book* uses each term).

## Output

- `key-terms/Glossary.md` — A–Z, chapter-tagged, book-voice definitions, citations where sourced,
  plus an appendix of foundational concepts the book doesn't yet name.
- Intermediates (regenerable, safe to delete): `key-terms/_glossary-candidates.json`, `key-terms/_parts/*.md`.

---

## Pipeline (3 stages)

### Stage 1 — Extract (deterministic, no AI)

Run: `node SCRIPTS/glossary-extract.mjs --topic <topic>`

Pulls every chapter's `## Key Terms` list, dedupes, and matches each term against the
`facts/<topic>` definitions (exact + normalized + loose-contains). Writes
`key-terms/_glossary-candidates.json`: `{ term, key, chapters[], source:{def,url}|null }`.
Reports match rate so you know how much sourcing to expect (branding was ~6% — most book
terms are bespoke coinages with no Wikipedia equivalent).

### Stage 2 — Author definitions (AI, parallelizable by chapter batch)

Split the chapters into batches (≈5 each) and run one agent per batch. Each agent:

1. Reads its chapters in full.
2. Term list per chapter:
   - Has a `## Key Terms` section → use those terms (split a compound entry only if each part is independently glossary-worthy).
   - No `## Key Terms` section → **propose 6–9** of the most teachable terms/concepts the chapter introduces (frameworks, coinages, mechanisms — never company/brand names, never generic words).
3. Citations — sourced, never invented: open `_glossary-candidates.json`; if a term has a non-null `source`, use that URL and keep the definition consistent with it; otherwise the citation is `-`. **Never invent a URL.** Citations come only from the facts slice.
4. Writes entries to `key-terms/_parts/batch<X>.md` in the exact contract below.

**Entry contract (two lines, blank line between entries):**

```
- **<term>** :: ch <comma-separated 2-digit chapter numbers> :: src <url-or-->
  <One or two sentence definition in the book's voice — how THIS book uses the term. Plain, precise, teachable. No "refers to"/"is defined as" filler. Do not start with the term itself.>
```

### Stage 3 — Merge (deterministic, no AI)

Run: `node SCRIPTS/glossary-merge.mjs --topic <topic>`

Parses all `_parts/*.md`, dedupes by normalized term (a term used in several chapters becomes
one entry with a union of chapter tags), keeps the fuller definition and any citation, sorts
A–Z (numerics/symbols under `#`), and appends "Foundational concepts not yet named in the book"
computed from `graph.json` (concepts linked by ≥2 other pages that no glossary term covers).
Writes `key-terms/Glossary.md`.

---

## Design rules

- **Book-voice definitions, facts-sourced citations.** The definition teaches the term as the book uses it; the citation (when present) points to an external sourced reference. Don't paste Wikipedia verbatim as the definition.
- **Citations only from `facts/`.** No invented or guessed URLs, ever. A term with no facts match simply has no citation.
- **Terms, not brands.** Company/product names (7 Up, Mountain Dew) are not glossary terms. Concepts, frameworks, and coinages are.
- **One entry per concept.** Multi-chapter terms merge; the chapter tag lists every chapter that uses it.
- **The gaps appendix is candidates, not errors.** It flags foundational concepts the glossary doesn't name; some may already be covered under different wording, and some entries are Wikipedia noise (specific brands). Treat as a review list, not a to-do.

## Run order (copy/paste)

```
node SCRIPTS/glossary-extract.mjs --topic <topic>
# then run Stage-2 authoring agents over chapter batches, writing key-terms/_parts/batch*.md
node SCRIPTS/glossary-merge.mjs --topic <topic>
```

## Future passes (not done here)

- **Chapter appendix:** for each chapter, emit the subset of glossary terms tagged to it as a `## Glossary` block at the chapter's end (read `Glossary.md`, filter by chapter tag).
- **Anki:** export `term<TAB>definition<TAB>chapter` TSV from `Glossary.md` for spaced-repetition import.
