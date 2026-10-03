# Renumber — done + remaining content TODOs

The chapter files now match the blueprint: **Ch 1–19 core + Appendix S1–S4 (Ship It) + end matter.**
File moves, slot placement, and H1 chapter numbers are done. The items below are *content* work
left for the rewrite (the +1).

## What's done (mechanical)
- All 14 old chapters moved to their new slots; 11 new drafts placed; 8a+8b merged into Ch 6.
- Ship It modules numbered 20–23 (sort after Ch 19, before end matter), titled "Appendix S1–S4".
- H1 "Chapter N — Title" lines updated to the new numbers on every moved file.

## Content TODOs (rewrite)
1. **Ch 3 — The AI Toolchain (EXPAND).** Body is still the old "Madison Framework" read. Expand it
   to actually *teach the CLI agents* (Cowork / Codex / Claude Code) — run, inspect, wire Madison —
   not just describe the architecture. H1/title already updated; subtitle still old.
2. **Ch 6 — Brand Strategy & Positioning (MERGE).** 8a is the base; 8b's body is appended under a
   `[MERGE TODO]` marker (`## Startup Brand Path (to merge)`). Fold the two into one chapter where
   personal vs. startup is the **running-project fork**, not two chapters. Reconcile the single
   TL;DR to cover both; de-duplicate the AI+1 block.
3. **Appendix S2 — Pipelines & Workflow (REFRAME).** Body still teaches hand-built n8n (old Ch 5).
   Reframe to *operate Madison* (n8n is the under-the-hood engine, not built from scratch).
4. **Cross-references (BOOK-WIDE).** Internal "Chapter N" references in the *existing* chapters now
   point at old numbers (e.g., old Ch 1 says "Chapter 4 turns your job search into a PRD" — PRD is
   now Appendix S1; archetypes moved Ch 3→5; strategy 8→6; etc.). Sweep and fix all cross-refs.
   The 11 new drafts already use the new numbers.
5. **Subtitles & TL;DR tables** on moved/merged chapters (3, 6, 10) should be re-checked against
   their new titles.

## Then (mechanical, after rewrite)
- Re-run the framework-mode **AI+1 generator** and the **TL;DR generator** across all 23 + S4 so
  every chapter is consistent.
- Run the `[verify]` items (research notes) through the fact-check pass.
- CAJAL figure pass for the new chapters.
