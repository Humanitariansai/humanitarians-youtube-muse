# BUILD-LOG.md — "Give it a voice"

## Decisions

- **Skill: show-tell (as assigned).** The brief assigns show-tell and it
  fits exactly: one simple drawing per beat (the deck, the box, the
  track bar), the voice explains. No skill switch; nothing in the topic
  needs lecture/ai-explainer/deep-explainer machinery. cc-explainer
  excluded per the brief (no real `claude` CLI session here).
- **No ShowTellCard beats.** Every beat's idea is a thing, a part, or a
  flow — a script entering a box, a voice stream merging with a music
  stream, a typo being read aloud. The card test fails on every beat,
  so the whole body is drawings (see SHOTLIST.md, "why a card").
- **Corrected the pitch on Vids.** The pitch said "Vids has voiceovers
  coming." Research at build time shows Google Vids already ships AI
  voiceovers (30 voices / 24 languages via Gemini 3.1 Flash TTS, Apr
  2026; bracket steering tags like [excitedly], Jul 2026). What is
  coming is a Gemini 3.8 Flash-Lite TTS upgrade (Storyboard18, Sep
  2026). The film says "Vids already has AI voiceovers built in";
  the correction is recorded in FACTCHECK.md (#11) and ACTS.md redo
  notes. [judgment]
- **Suno Speech facts re-verified at build time (2026-10-05).** Launch
  announced Oct 1, 2026 by Suno CPO Jack Brody after a month of small-
  group testing; public beta on web + mobile (Create tab); two modes —
  Simple (describe it, e.g. "a pirate captain rallying his crew") and
  Advanced (your exact script; voice gender / speech style / vocal
  variety); voice + original background music generated together in
  one track with a music toggle; ~8 min max; acknowledged quirks —
  accents wander (British → Australian), dramatic pauses get very
  dramatic. All from six Oct 2, 2026 news sources (SOURCES.md).
- **Suno's "first audio model" claim left out.** Suno calls Speech "the
  first audio model that generates voice and music together as one
  cohesive track" — a marketing claim with no published benchmarks
  (TPS Report notes this). The film states only what the product does.
  [judgment]
- **No pricing anywhere.** Standing rule; Okay News notes Speech had no
  separate price announced anyway.
- **Kokoro-safe narration choices.** Bracket tags spoken as "open
  bracket, excitedly, close bracket" (the on-screen pill shows
  "[excitedly]"); no version numbers or spelled-out acronyms anywhere;
  "Hallo" greeting (known-clean per the skill).
- **Midpoint guards.** Every beat's plays are placed to land clear of
  the GATE T midpoint sample (margin ≥ ~1 s): B01's wave/trail uses
  `lead=2.0`; B05's page/script pill uses `lead=1.2`; the rest land
  early or well after the midpoint.
- **Cast continuity.** The merged track bar is the recurring motif
  (B01 → B03 → B04); the slide-deck page recurs in B02/B05/B06; the
  Suno box's open-crate form lets the script page drop inside.

## Timeline (2026-10-05)

1. Read show-tell SKILL.md; studied the-second-opinion package and the
   iso_kit template; read muse/FRICTIONAL.md format from the write repo.
2. Web research: Suno Speech launch (6 sources, Oct 2, 2026); Google
   Vids voiceover status (Workspace Updates blog + Storyboard18) —
   found the pitch's "Vids has voiceovers coming" was wrong, corrected.
3. Wrote ACTS.md, SOURCES.md, FACTCHECK.md (17 claims), SHOTLIST.md,
   PROMPTS.md.
4. Wrote make_sheet.py (11 beats, 181.6 s ≈ 3:02); first run failed a
   self-assertion — triggerWords spanned a line break in the BIDEA
   text; fixed by moving the break so the trigger appears verbatim.
5. Wrote scenes.py (iso_kit pasted at top; 7 scene classes
   B00_SilentSlides … B06_TheRule; helpers after the class lines).
6. QC gate: `py_compile` clean on both files; static_scene_check 0
   warn / 0 error on all 7 classes, both in the build dir and in a
   scratch dir holding only scenes.py (kit degrades gracefully without
   beat_sheet.json).
7. Wrote BUILD-LOG.md, CHECKS-REPORT.md, CLAUDE-CODE-RENDER.md,
   README.md; pushed all 12 files to
   `muse/youtube/how-to-use-ai/give-it-a-voice/`; verified 12/12 live
   via Contents API read.

## What I'd redo

Nothing structural. Watch at the review cut: the page must visibly
drop INTO the open Suno box in B01 (z-order: page between back and
front walls); the wandering-accent arc in B04 must not touch the
"accents wander" pill; the terracotta X must sit squarely on the
"teh" word in B06.
