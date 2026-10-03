# BUILD-PROMPT — claude-liam-madison-brand-guidebook

Paste into a local Claude Code session at `books/` (the toolkit needs the Mac:
Kokoro, Manim, Remotion, ffmpeg).

```
Read books/CLAUDE.md, then build the deep-explainer reel at
branding-and-ai/youtube/claude-liam-madison-brand-guidebook/.

State: PLAN.md is Gate-1 APPROVED (2026-08-11, Bear). beat_sheet.json is
authored (B00 + 36 body beats + your-turn closing block, Kokoro am_onyx,
claude palette). SOURCES.md and BUILD-LOG.md are in the folder.

Do, in order, honoring every gate:
1. Validate beat_sheet.json against runtime/schema/beat_sheet.schema.json;
   fix Remotion pattern names/props against the actual component zod schemas
   (SegmentCard/ClaudeVerdictArtifact prop names were authored from memory in
   a cloud session — check them).
2. factcheck → FACTCHECK.md. Claims are mostly self-referential to the
   template (32 pages, 8 sections, tint ladders, the spacing note, the
   #FF7929→#8B3A0F remap, the 3:1 rule from bearbrown_co/CLAUDE.md). Verify
   against brand-guidebook-000-nbb.idml and the site page
   madison.humanitarians.ai/app/brand-guidebook/page.tsx (the YOUR TURN beat
   must match the published prompt).
3. GATE P: render the narration slate for Bear's review. STOP for sign-off.
4. After sign-off: Kokoro audio (free), align, write durations back.
5. Gate D2: SHOPPING.md from locked durations. All 9 vox stills are one
   InDesign action — export pages 1, 3, 4, 7, 11, 16, 18, 20, 25, 29, 31 of
   brand-guidebook-000-nbb (2x PNG) into pantry/ named by beat
   (B02, B08, B04, B09, B15, B19, B21, B23, B25, B31, B32; B10 reuses B09's
   still, B26 reuses B25's — vox runs R1/R2, one camera move each).
6. Gate D1: ./brutalist-art/art run branding-and-ai/youtube/claude-liam-madison-brand-guidebook
   (full previz, slates where pantry is empty). Bear watches it.
7. Pantry intake → recompile changed slots → review cut → TYPECHECK.md +
   FACTCHECK.md clean → ./brutalist-art/art final.
Never publish; master stays in the folder.
```
