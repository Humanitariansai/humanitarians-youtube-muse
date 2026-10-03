# BUILD LOG — hai-simple/books--claude-liam-combining-plugins

Redo of `anthropics/books/claude-cowork-plugins/youtube/claude-liam-combining-plugins`
(Teardown register, 39 beats) as `hai-simple` (Plain register, Humanitarians AI skin).
Source folder untouched.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. No verdict recap (source's `V01` dropped); every hand-off
  beat states what happens and what breaks without it, never a design judgment on Anthropic's
  plugin architecture.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer types
  the newcomer's wrong-guess word "CHOOSE" (implying manual routing), hesitates, corrects to
  "tell Claude" → lands the source's real question verbatim: *"If I install several plugins,
  do I have to tell Claude which one to use?"*
- **Close:** source's 6-beat close (`V01, H01, O01, BVDT, BHTF, BOUT`) → 4-beat close
  (`BCRY, BHTF, BOUT, BCTA`). `BVDT`/bookend `BHTF`/`BOUT` in the source had **empty
  narration_text** — dead scaffold, dropped, not compressed. `V01`'s verdict-recap content is
  redundant with the body under Plain register. `O01`'s title narration is preserved, split
  across the new two-part Humanitarians AI outro (`OutroSeries` + `OutroCTA`).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** unchanged. Every hand-off, mechanism, and example is the source's,
  reworded only for register, not substance. Beat-count delta (39 → 36) is entirely inside
  the close restructuring above; the body (B00→B25) is a 1:1 carry of the source's B00–B26
  substance (B26's line became the new global carry-out, BCRY, instead of an Act VI card).

## NO-GENAI / NO-PANTRY LAW

Source's `pantry_note` fields (Tier-1 illustrative photography briefs on B04, B08, B10, B11,
B16, B21, B25) were never actually filled with pantry stills in the source's own review cut —
it fell back to bespoke Manim "Doodle" scenes (`scenes_std.py`, documentary-duotone
approximations). This build keeps that resolution: all of B04/B08/B10/B11/B16/B21/B25 are
GRAPHIC/Manim here too, retinted, not sourced from any pantry/human-drop asset. No beat in
this reel is AI-VIDEO, pantry, or a human-drop slot.

## Two defects found and fixed during Gate V (frame QC)

1. **Wrong channel handle on BHTF.** `ClaudeComposerAsk`'s Root.tsx `<Composition>`
   `defaultProps` hardcodes `folderLabel: '@NikBearBrown'` (confirmed by reading
   `runtime/remotion/src/Root.tsx`); the beat sheet didn't set the prop, so the rendered
   frame showed `@NikBearBrown` on a Humanitarians AI video. Fixed by adding an explicit
   `"folderLabel": "@HumanitariansAI"` to BHTF's props and re-rendering. Verified in a
   full-resolution frame grab post-fix.
2. **Overlapping layer boxes in the anchor composition.** `_stack_group()` (scenes.py)
   shifted each of the four layer cards by `i * 0.42` design units while each card's height
   was `0.85` — half of every card overlapped the next, garbling "Marketing/Sales/Research/
   Data" text at B01 and BCRY (the ANCHOR LAW pair). Fixed by shifting by `box_h + gap`
   (1.03 units) instead; re-rendered B01 and BCRY, recompiled, verified clean in full-res
   frame grabs.

## Component choices, logged

- **Outro: `OutroSeries` + `OutroCTA`, not `ClaudeTitleOutro`.** `ClaudeTitleOutro`'s own
  docstring (`ClaudeTitleOutro.tsx`) hardcodes `handle: '@NikBearBrown'` with **no prop, no
  override** and explicitly states "Other channels (HAI, Medhavy, Musinique) use their own
  outro components — never this one." The one prior hai-simple pilot
  (`hai-simple-what-is-claude-actually`) used `ClaudeTitleOutro` anyway with a `handle` prop
  that the component silently ignores — a real bug in that pilot, not repeated here. Content:
  `OutroSeries` (eyebrow "CLAUDE BASICS · HUMANITARIANS AI", line "Claude, In Concert.") →
  `OutroCTA` (line "…Liam, in for Bear.", handle "@HumanitariansAI"). No book `AUTHOR.MD`
  exists for this source book, so outro copy was authored directly from the HAI channel
  identity rather than lifted from a file that doesn't exist.
- **Body beats: pure Manim, not the `VR*` Remotion card family.** The source's own
  `BUILD-LOG.md` records that `VRSegmentCard`/`VRLayerStack`/`VRChipGrid`/`VRSourceFlow`
  (from `VercelRefactorIllu.tsx`) import `CLAUDE` tokens directly with no retint path —
  confirmed by reading `Root.tsx`. Using them here would have put Claude-branded cream/
  terracotta on a Humanitarians AI video. All 32 GRAPHIC beats (6 act cards + 25 body beats +
  the anchor payoff) are bespoke Manim in the humanitarians palette (`#F3EBDD`/`#2F2A26`/
  `#E4572E`/`#1F4E5F`) instead — reusing/retinting the source's own bespoke scene geometry
  (`scenes_std.py`) where a beat mapped 1:1, writing new scenes where it didn't.
- **Known visual seam, accepted:** `OutroSeries`/`OutroCTA` (`tokens/vox.ts`) render on flat
  white (`#FFFFFF`) with near-black ink (`#2A1A0E`), not the humanitarians cream/ink used
  everywhere else in this reel — those two components have no palette prop. A one-beat seam
  at the very end, not a legibility or safety defect; not worth blocking the review cut over,
  and not fixable without editing a shared component outside this build's scope.
- **`art` motion-histogram WARNING (88% graphic vs. the ~40% pantry-language cap):** expected
  and accepted. NO-GENAI/NO-PANTRY LAW forces every body beat to GRAPHIC or REMOTION, and the
  only Remotion body-card family available (`VR*`) is palette-locked to Claude (above) — so
  the humanitarians-palette body is necessarily Manim-heavy. Not a pantry violation.

## Gates

- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.41s**, clears the ≥8s floor (the 2026-08-27 pilot's 8-word
  narration produced a 2.86s open that never showed its own correction).
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (well above the -40 dB floor).
- **Gate V (frame QC):** full contact sheet (`qc-sheet.png`) reviewed beat-by-beat, plus
  full-resolution frame grabs of B00, B01, B02, B10, B19, BCRY, BHTF, BOUT. Two defects found
  and fixed (above); nothing else flagged — no text overflow, no unsafe inset, no overlap
  remaining after the fix.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (36/36
  beats, no violations).

## Output

`books--claude-liam-combining-plugins-slate.mp4` — 314.0s, 36/36 beats real (no slates),
audible narration throughout. This is the review cut (COMPLETION LAW satisfied: newer than
`beat_sheet.json`, audible audio verified via ffprobe/compile GATE AUDIO).

**Playlist:** Claude Basics (`SUBJECT.json` → `"skill": "hai-simple"` matched against
`skills/make/hai-simple/loop/playlists.json`'s `"hai-simple"` key).

## Phase 4 (4K + delivery)

- **4K master:** `compile.py` without `--review` enforces its 4K LAW automatically —
  wrote `books--claude-liam-combining-plugins.mp4` natively at 3840×2160, 314.0s,
  36/36 beats real, mean_volume -23.8 dB. Copied to `books--claude-liam-combining-plugins-4k.mp4`
  so `deliver.py`'s `newest_master()` picks it as the explicit 4K variant.
- **Playlist correction, logged:** initially matched `SUBJECT.json`'s `"skill": "hai-simple"`
  literally against `playlists.json`'s `"hai-simple"` key → "Claude Basics". Caught before
  final delivery by checking `HAILOOP-LOG.md`: the immediately-preceding sibling reel
  (`books--claude-liam-building-plugins`, same source book, Ch.12 "Building Your Own
  Plugins") explicitly reasoned that neither `family: "books"` nor a `"books--"` slug
  prefix has a literal entry in the map, and content-matched to **"Extending Claude —
  Skills, Plugins & Connectors"** instead of falling to `_default` — logging that
  reasoning rather than mechanically using a skill-name match. This reel is the same
  book, same topic family (combining/using plugins); for consistency with that
  established precedent, the playlist here is also **Extending Claude — Skills, Plugins
  & Connectors**, not "Claude Basics" and not `_default`. Fixed in `books--claude-
  liam-combining-plugins.md` (title/description also de-branded from "Claude Basics")
  before delivery; the repo README was corrected in a follow-up commit after the first
  `deliver.py --push` had already gone out with the wrong playlist line.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/books--claude-liam-combining-plugins/` (4K master + description, syncs to
  Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/books--claude-liam-combining-plugins/` (README.md +
  beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md +
  QUESTION.md — no media). Commits `bcc071e4` (initial) and `720ca52a` (playlist fix).

**Status: DELIVERED.**
