# BUILD-LOG — claude-code--claude-liam-skill-development

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-code/youtube/claude-liam-skill-development/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-form sheet (metadata `brand:
"claude-liam"`, `source_skill` pointing at
`claude-code/plugins/plugin-dev/skills/skill-development/SKILL.md`). 7
beats: B00 cold open (`ClaudeComposerAsk`, REMOTION — not AI-video/pantry,
so NO-GENAI/NO-PANTRY LAW required no substitution beyond the WRITER LAW
swap), B01 anatomy, B02 design, B05 teardown ("gets right"/"bites"), BVDT
verdict recap, BHTF handoff, BOUT outro.

Facts carried over unchanged: a skill = `SKILL.md` (YAML frontmatter —
`name` + `description`, required — plus an imperative markdown body) +
three optional resource folders — `scripts/` (code, never read into
context), `references/` (docs loaded while working), `assets/` (output
files, never loaded into context); progressive disclosure in three levels
— metadata always in context (~100 words), body loads only on trigger match
(target 1,500–2,000 words, hard ceiling 5,000 with no documented warning
path above 3,000), resources load only as needed (no word limit); the
description must be third person naming a specific trigger phrase, not a
vague summary; the body must be imperative form, not advisory; six-step
build process (understand → plan resources → create structure → edit,
resources first SKILL.md last → validate → iterate); always reference
created resources by name; source's worked example — a `pdf-editor` skill
(rotate PDFs, convert pages to images) checked for a third-person
trigger-phrase description, imperative body, a lean body under 2,000 words
that references `scripts/rotate_pdf.py` by name rather than embedding it,
and explicit references to every resource file it creates. Source's own
flagged gaps carried as fact, not verdict: the trigger-match mechanism
(pattern-match vs. LLM judgment) is never explained by the skill itself;
the word-count target is a recommendation with no hard-limit enforcement;
the skill-reviewer agent's invocation and checks are vague.

B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "reminder" → "skill" — the naive
assumption that telling Claude to remember a workflow in conversation is
equivalent to building a findable package, corrected to the fact that a
skill's name and description sit visible in every conversation regardless
of what's been said before). Register re-registered Teardown-form → Plain:
the source's B05 "gets right"/"bites" framing (including a judgment that
the skill's own docs leave the trigger mechanism unexplained) restated here
as a mechanism/failure-mode fact (B03) with no verdict on the skill's
documentation. Source's BVDT verdict recap folded into a dedicated BCRY
carry-out beat per CARRY-OUT LAW (same disposition as the `hook-development`
redo precedent in this family — `anthropics/youtube/hai-simple/claude-code--claude-liam-hook-development`,
used directly as the structural template for this build). Close re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Anchor (B02 → B03:
the `pdf-editor` skill — trigger phrase vs. vague description; referenced
script vs. inline script) and a both-directions beat (B03) added per this
factory's PHASE 1 structure requirement — the source didn't carry these as
distinct beats. 7 beats total, matching the source's beat count.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.52s, B01 19.50s, B02 22.42s, B03 26.45s, BCRY 9.69s, BHTF 31.10s,
   BOUT 3.63s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `SKDB01Scene` /
   `SKDB02Scene` / `SKDB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (this step exceeded the harness's 120s inline timeout and was moved to
   background by the tool automatically — since this invocation is
   one-shot with no next turn to receive a wake-up notification, actively
   polled for the background process to exit before proceeding, per the
   COMPLETION LAW's render-in-foreground rule).
4. B00 verified directly: `media/B00.mp4` = 11.53s (meets the ≥8s TIMING
   LAW floor). Pulled a frame at t≈9s: the correction ("reminder"→"skill")
   is complete and visible, no accent-colored "reminder" remaining onscreen.
5. `compile.py` → `claude-code--claude-liam-skill-development.mp4`, 7/7
   real (no slate), 3840×2160 (4K LAW). B01/B02/B03 were slowed 1.72×/2.54×/
   2.98× to fill their audio durations (Manim scene `wait()` calls were
   shorter than the Kokoro narration) — visually confirmed at Gate V that
   the slower pacing reads cleanly, no dead air or stutter.

**GATE T (type_check.py) — two real defects found and fixed, confirmed by
direct frame inspection and by replicating the checker's own pixel-gap
algorithm in a standalone script to pinpoint the exact failing frame:**

- First pass: FAIL (1 pixel beat, B02, kerning §8.4). Traced to the
  anchor card's caption `"used when: rotate a PDF, convert PDF pages"` and
  the "specific" card's `"...when asked to rotate a PDF"` — both set in
  `SANS` (Montserrat) at small sizes with a `"to rotate"` word-boundary
  glitch causing Pango to collapse the inter-word space. Fixed by
  switching those captions to `SERIF` (EB Garamond) and rewording
  `"...when asked to rotate a PDF"` → `"...when asked: rotate a PDF"` to
  remove the exact `"to "` + word-initial-consonant adjacency that
  triggered the collapse.
- Second pass: FAIL (same numbers, same beat). Wrote a standalone script
  replicating `type_check.py`'s `check_kerning_sanity` pixel-gap algorithm
  frame-by-frame against `manim/B02.mp4` to find the exact failing frame
  rather than guessing — found it was the *title* text `"BUILT TO BE
  FOUND"`, not the card captions: two consecutive short words ("TO", "BE")
  depress the row's mean-letter-width while the real inter-word gap stays
  fixed, so the ratio crosses the checker's kerning threshold as a false
  positive. Retitled the beat `"MADE FINDABLE"` (no adjacent short words).
- Third pass: **PASS (0 FAILs)** — confirmed both by the standalone
  frame-scan script (no frames flagged across the full clip) and by
  `type_check.py` itself.
- **Gate V caught a defect GATE T doesn't check (pixel-level layout, not
  typography):** pulling frames across the compiled master showed B01's
  three progressive-disclosure tier cards ("name + description" / "body" /
  "scripts / references / assets") completely overlapping — their two-line
  text (title + caption, `arrange(DOWN, buff=0.55)`) was taller than the
  0.85-unit card height, and the cards were only spaced 1.2 units apart,
  so overflowing text from each card bled into its neighbors. Fixed by
  enlarging the cards to 4.4×1.3, tightening the label buff to 0.35, and
  respacing the three tiers to 1.5 units apart (0.35 unit gap between card
  edges) — re-rendered, re-inspected the frame directly: three clean,
  separated cards with no overlap.

**Gate V (visual):** pulled frames every 6–8s across the full 125.3s
runtime and read them directly. B00's correction, B01's file/tier diagram
(post-fix), B02's anchor card, B03's anchor-return and two failure modes,
BCRY's carry-out card, BHTF's Your Turn composer card, and BOUT's outro/
subscribe card all read legibly with safe inset respected and no text
overlap. **Noted, not a defect introduced here:** `OutroCTA` renders on
flat white rather than the humanitarians cream ground — same shared-
component behavior already logged unremarked in sibling reels in this
family (`hook-development`, `action-creator`, `screenshot-prompt-caching`).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the two fixes above
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: duration 125.317s; mp4 mtime (1787991785) newer than
  beat_sheet.json mtime (1787990521)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family.

Metadata file written: `claude-code--claude-liam-skill-development.md`
(channel @HumanitariansAI, Playlist: **Claude Code** — resolved from
`skills/make/hai-simple/loop/playlists.json`: the reel's own family
`claude-code` matches the map's `claude-code` prefix directly — plus the
direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
