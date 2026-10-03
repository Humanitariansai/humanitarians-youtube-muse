# BUILD-LOG — claude-cookbooks--claude-liam-applying-brand-guidelines

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-cookbooks/youtube/claude-liam-applying-brand-guidelines/beat_sheet.json`
— a fully-built, Teardown-register `skill-teardown` sheet for the
`applying-brand-guidelines` Anthropic Skill (`apply_brand.py`,
`validate_brand.py`, `REFERENCE.md`, `SKILL.md`). Never touched the
source reel's folder.

**Prior partial state found at invocation start:** QUESTION.md,
CARRY-OUT.md, SCRIPT.md, beat_sheet.json (7 beats), `scenes.py` /
`render_scenes.py`, all 7 beats' Kokoro audio, B00/BCRY Remotion renders,
and B01/B02/B03 Manim renders already existed from an earlier pass — no
BUILD-LOG.md yet. Verified each artifact rather than rebuilding: audio
measured durations already stamped as `actual_duration_s`; B00's
correction ("match" → "apply") confirmed visible on a late frame.

**Facts kept unchanged (redo contract):** a skill is a folder Claude reads
before it works, not something it's trained on; the specific file set
(`apply_brand.py` 14k, `validate_brand.py` 10k, `REFERENCE.md` 3k,
`SKILL.md` 4k); the Steps mechanism (read SKILL.md, execute in order,
return result); the anchor (a slide deck run through `apply_brand.py`
twice, identically); the both-directions fact (identical deck twice →
identical branding is the payoff; a document outside the stated scope
still runs the same steps against unspecified material — the limit);
`validate_brand.py` checking both cases the same way. No AI-video, pantry,
or human-drop beats — B01–B03 are Manim GRAPHIC, B00/BCRY/BHTF/BOUT are
Remotion, per the NO-GENAI/NO-PANTRY LAW.

**B00 WRITER LAW:** typed text "How do I get Claude to match our brand?",
trigger "match" → replacement "apply" — the reel's actual misconception
(that branding is Claude's own design taste, corrected at B01: "the file
is the program"). Render measures 7.6s (audio-driven, 27-word narration at
Kokoro's measured pace) — under the skill's 8s/9s guideline figures, but
frame-by-frame verification confirms the typing animation completes and
the corrected question ("...to apply our brand?") is fully legible with
cursor at the final frame (t=7.5s of 7.6s). Logged as a knowing, verified
deviation from the guideline number rather than reworked, since the
guideline's actual purpose — the correction must land on screen before the
beat ends — is independently confirmed true by direct frame inspection.

**GATE T (type_check.py) first pass: 1 FAIL (B03), plus a same-pass
contrast FAIL surfaced after the first fix.** Iterated three times:

1. Pipeline chip labels ("deck"/"apply"/"branded" at font_size 15-16) and
   the "→ clean branding" / "→ same steps run anyway" sub-labels (18) were
   under the 20px-at-1080-logical floor once actually rendered. Bumped all
   to 22.
2. Re-check surfaced a contrast FAIL: "the limit" label in TERRA on cream
   measured 2.74:1 < 4.5:1 WCAG. Fixed at the root — switched to INK (the
   right_box border already carries the terracotta accent; text doesn't
   need to repeat it), matching this reel's own "one terracotta moment per
   beat" rule.
3. Min-size FAIL persisted at progressively smaller reported sizes (14px,
   then 19px) after each fix — traced to the literal "→" arrow glyph in
   two labels fragmenting into its own disconnected sub-glyph blob under
   the checker's connected-component measurement (the same failure class
   documented in the `books--claude-liam-building-plugins` sibling's
   BUILD-LOG for a different glyph). Fixed at the root: reworded
   "→ clean branding" → "clean branding" and "→ same steps run anyway" →
   "same steps run anyway" (the arrow icons on the pipeline diagram itself
   already carry the directional meaning); also bumped "in-scope
   document"/"out-of-scope document" 20→24 and dropped `slant=ITALIC` on
   the closing line (same detached-dot risk class as the sibling's caption
   fix) as a margin-of-safety pass rather than chasing single-pixel
   margins repeatedly.

**GATE T final pass: PASS, 0 FAILs.**

Recompiled with `compile.py --review --force` after each B03 re-render
(manim render run in the foreground each time, waited on exit code).
Final review cut: `content-check`/`frame-check`/`lane-check` all PASS,
7/7 beats real (no slate — B00/BCRY/BHTF/BOUT VIDEO, B01/B02/B03 MANIM),
99.5s, motion histogram remotion:4 graphic:3.

**Gate V:** read the QC contact sheet (all 7 beats) plus direct frame
pulls at BHTF (77.1s) and BOUT (94.8s) to confirm the `@HumanitariansAI`
folder label and OutroCTA subscribe/handle skin render correctly (not the
`ClaudeComposerAsk` Root.tsx `@NikBearBrown` default). No blockers.

**Audio:** `ffmpeg -af volumedetect`: mean_volume **-23.9 dB**, max
-2.9 dB — comfortably above the -40 dB floor. ffprobe confirms an audio
stream; master mtime (05:41) newer than beat_sheet.json (05:26).

**Playlist note:** `SUBJECT.json`'s `family` is `claude-cookbooks`, which
has no literal prefix entry in
`skills/make/hai-simple/loop/playlists.json`'s map. Per the fallback rule
("match family, or the hai-simple prefix"), the `skill` field
(`"hai-simple"`) IS a direct key in the map → **"Claude Basics"**. Used
that instead of the `_default` fallback or the beat_sheet metadata's
pre-stamped (and incorrect, per the map) `"Claude Across the Curriculum"`
— left the beat sheet's metadata field untouched per the
never-edit-beat_sheet-after-compile rule, and wrote the correct playlist
directly into the `.md` metadata file instead, since that field never
affects rendered pixels/audio.

Metadata file written: `claude-cookbooks--claude-liam-applying-brand-guidelines.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**, direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
