# Edit video with words

Show-tell film (How to AI, Wave 7 #45) for the Humanitarians AI YouTube
channel. Liam, in for Bear (Kokoro `am_onyx`, Teardown register,
@NikBearBrown).

**Premise:** YouTube is adding a chat-based editing assistant to Shorts
and the YouTube Create app — type "match the cuts to the beat" instead
of working the timeline. The film walks through the announcement (Made
on YouTube, Sept 2026), the Happy Kelli demo, what the assistant does,
why you stay in charge, and the reported early-2027 window — then notes
Meta's already-shipped Edits Assistant and what you can use today.

**Reframe note:** the feature is a preview, not a product — the film
says "the reported window" and carries a "reported window" caption on
the timing beat. Re-verify the launch status before the final publish
render; availability churns.

| File | What it is |
|------|------------|
| ACTS.md | Act structure, coverage map, cast per act, BIDEA/BDEFS notes |
| SHOTLIST.md | Per-beat lane auditions with runner-ups |
| FACTCHECK.md | 17 claim rows, all PASS / CORRECTED / EXEMPT, with sources |
| SOURCES.md | Fact → source table |
| PROMPTS.md | "No generation prompts" |
| make_sheet.py | Generates `beat_sheet.json`; asserts 14 beats / 10 Manim |
| beat_sheet.json | The sheet: 14 beats with narration and shot notes |
| scenes.py | 10 Manim scene classes (B00–B09) + helpers |
| BUILD-LOG.md | Dated build steps, including QC fixes |
| CHECKS-REPORT.md | Static gate: 10 clean · 0 warnings · 0 errors; PROOF GATE |
| CLAUDE-CODE-RENDER.md | Render instructions for Bear's Mac |
| README.md | This file |

## Status

Pre-render package + VM slate cut. The 4 Remotion bookends are labeled
slates in the slate cut (Remotion can't render in the build VM); Bear's
Mac renders the real ones per CLAUDE-CODE-RENDER.md. Never render,
publish, upload, or stage anything for publication without Bear's
explicit instruction. No audio, video, or cache files are committed.
