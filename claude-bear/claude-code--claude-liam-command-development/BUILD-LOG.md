# BUILD-LOG — claude-code--claude-liam-command-development

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-code/youtube/claude-liam-command-development/beat_sheet.json`
— a fully-built Teardown reel (7 beats, the Claude Code plugin-dev
`command-development` skill, `claude-liam` / @NikBearBrown). `source_dir` in
SUBJECT.json pointed at a `/Users/bear/...` path that doesn't exist on this
machine; found two local copies of the content
(`anthropics/claude-code/youtube/claude-liam-command-development/` — the
newer, VOICE-LOCK-audited rebuild dated 2026-08-25 with an `AUDIT.md` and
`beat_sheet.pre-rebuild.json` — and an older `cut: master` copy under
`anthropics/youtube/claude-code/`); used the newer audited one as the source
of record and read it plus its AUDIT.md in full before writing anything.
Never touched the source reel's folder.

**Facts kept unchanged:** a command is one markdown file with optional YAML
frontmatter; three locations (project `.claude/commands/`, personal
`~/.claude/commands/`, plugin `plugin-name/commands/`), each with its own
`/help` label and use case; five frontmatter fields (description,
allowed-tools, model, argument-hint, disable-model-invocation); the critical
design rule — the command body is instructions FOR Claude, never a message
TO the person running it, illustrated with the source's own correct/
incorrect review-command pair; dynamic argument syntax ($ARGUMENTS, $1/$2/
$3 positional, @file, `!`bash``` inline); the file format's own honesty
about its limits (bash execution syntax lives in a separate reference page,
not reproduced in the skill; no built-in validation tooling for a command
file's structure).

**Beat-count note (redo):** source is 7 beats (B00 cold open, B01 anatomy —
locations + frontmatter fields + dynamic arguments, B02 design — the
instructions rule + four command patterns + CLAUDE_PLUGIN_ROOT, B05
Teardown gets-right/bites, BVDT verdict, BHTF handoff, BOUT outro — B03/B04
unused in the source). Kept the same count (7) with a 1:1 remap: B00 →
BrutalistHesitantWriter; B01 kept as the file-and-locations mechanism beat;
B02 recentred on the instructions-rule correct/incorrect example and
promoted to the reel's anchor (dropped the four-pattern catalogue and
`${CLAUDE_PLUGIN_ROOT}` detail — true and useful, but wouldn't fit one beat
under the redo's fixed beat count; not contradicted, just not carried into
this cut); B05's "gets right / where it bites" Teardown framing recast as
B03, a neutral both-directions beat (spelled out precisely vs. pushed to an
external reference / not built) — same underlying facts, no design verdict,
which is the correct Plain-register home; BVDT (verdict) became BCRY
(carry-out). No beat in the source was AI-VIDEO, pantry, or a human-drop
slot, so NO-GENAI/NO-PANTRY LAW required no beat substitution.

WRONG-GUESS LAW note: with only 7 beats locked by the redo contract, there
was no beat to spare for a dedicated wrong-guess beat separate from B00. The
hesitation IS the wrong guess (WRITER LAW); the correction is picked back up
explicitly at the carry-out (BCRY) instead of in its own body beat.

**B00 WRITER LAW:** misconception — a newcomer drafting a command's body
assumes it should describe what's about to happen to the person running it
("talks to the user"); the correction is the source's own "critical rule"
(commands are instructions FOR Claude, not messages TO the user). Typed
text: "I want a slash command / whose body talks to / the user. / How do I
write it?", trigger "user" → replacement "Claude" (reused the sibling
`claude-code--claude-liam-agent-development` reel's tuned timing values:
charMs 42, hesitateBetween 8, mistakeRate 3, jitter 22 — already
root-cause-fixed there for the "window too short" failure class). Measured
`actual_duration_s` came back 10.88s (≥ 8s floor); B00 read directly at
Gate V shows the full corrected question "...talks to Claude. How do I
write it?" complete on screen.

**Body beats:** all 3 (B01–B03) built as Manim GRAPHIC scenes, reusing
verbatim the shared "chip row" renderer from the sibling hai-simple reel
`claude-code--claude-liam-agent-development/scenes.py` (title + up to 5
labeled chips, optional arrows, optional accent/strike, caption), driven by
a per-beat content dict. Anchor: B02 plants the correct/incorrect
review-command pair ("THE COMMAND BODY" → "READ BY CLAUDE" (accented) →
"NOT SHOWN TO YOU"), paid off at BHTF where the viewer builds exactly that
kind of command and checks it against a body-reads-like-a-direction
criterion. B03 uses `strike` (dimmed MUTE text, the sibling's documented
fix for the literal-strikethrough-bisects-glyphs GATE T class) to mark
"BASH SYNTAX DETAIL" and "VALIDATION TOOL" as pushed elsewhere/not built,
against three precisely-specified chips. Close: BCRY `WantQuote`
(carry-out), BHTF `ClaudeComposerAsk` (the source's verbatim PR-review
Your-Turn prompt, explicit `folderLabel: "@HumanitariansAI"`), BOUT
`OutroCTA` (@HumanitariansAI).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (7 beats), `scenes.py` (chip-row Manim generator ported
from the sibling reel + 3-beat content table), `render_scenes.py`. Ran
`generate_audio_kokoro.py` (7/7 beats, am_onyx, $0.00) — measured durations
became the clock. Rendered 3 Manim beats and 4 Remotion beats
(`remotion_scenes.py`, foreground; the harness auto-moved the >120s
invocation to background mid-run, blocked on `TaskOutput` until it returned
exit code 0 before proceeding — no render step was left running
unsupervised).

**GATE T (type_check.py) — run BEFORE compile.py, incorrectly:** first
invocation (before `compile.py` had stamped `build.status` into
beat_sheet.json) reported GATE T FAIL, but this was a tooling-order mistake
on this invocation's part, not a real defect — `type_check.py`'s Manim
pattern-name resolution requires `beat.build.status == "MANIM"`, which only
`compile.py` writes back into the sheet. Re-ran `compile.py` first (7/7
beats real, master born natively 4K, `GATE AUDIO: PASS -23.9 dB`), then
re-ran `type_check.py` against the compiled/stamped sheet — this is the
correct order and matches the sibling reels' documented timestamps.

**GATE T real findings, in order:**
1. B03 bbox-overlap §8.6b: chip border blob bbox enclosing a sub-glyph
   fragment near the "ARGUMENT SYNTAX" word boundary — same
   box+interior-label false-positive class as `BPB10Scene`/`BPB21Scene`/
   `BPB12Scene`/`BPB01Scene` already in `type_check.py`'s
   `BBOX_OVERLAP_EXEMPT_PATTERNS`. Verified via frame pull + 3× pixel crop:
   "ARGUMENT SYNTAX" renders as one cleanly kerned, fully legible label with
   visible margin inside its chip border. Added `BPB03Scene` to that list
   with the verification recorded inline (note: this reel's scene also
   happens to share the bare name `BPB03Scene` with the sibling
   `claude-code--claude-liam-agent-development`'s `KERNING_EXEMPT_PATTERNS`
   entry — a different list, different check, no conflict).
2. B03 min-size §8.1: the SAME fragment (17px < 20px floor). No exemption
   mechanism exists for min-size the way it does for bbox-overlap/kerning,
   so this one was fixed at the root instead of exempted: the 5-chip row's
   `chip_w` (~2.16 units) forces `set_width()` downscaling on any label
   that doesn't fit at its assigned font size, and "ARGUMENT SYNTAX" (16
   chars) needed enough shrink to fragment at the pixel level. Renamed the
   chip to "ARGUMENTS" (9 chars, still an accurate label for the beat's
   content — dynamic-argument syntax) — short enough to render at full,
   unscaled size. Re-rendered B03 only, re-compiled, re-ran GATE T.

**GATE T final pass: PASS, 0 FAILs** (7 beats checked; min-size 7/7 PASS,
bbox-overlap 7/7 PASS, kerning 3/3 PASS, contrast/overflow/card-clip all
PASS).

Compiled with `compile.py .`: 7/7 beats real (no slate), master born
natively 4K (3840×2160, `compile.py`'s 4K LAW), 131.5s runtime, tail
silence +1.0s on BOUT applied. `content-check`/`frame-check`/`lane-check`
all PASS. `GATE AUDIO: PASS mean_volume -23.9 dB`.

**Gate V:** pulled 16 frames at 8s spacing across the full 131.5s runtime
plus one targeted frame at t=129.5s for BOUT, and read every one directly.
B00's correction and full final question land inside the beat (confirmed
above). B02's anchor (THE COMMAND BODY → READ BY CLAUDE (terracotta) → NOT
SHOWN TO YOU, with the correct-example caption) reads cleanly. B03's fixed
"ARGUMENTS" chip renders at full size alongside the other four. BCRY carry-
out card, BHTF (`ClaudeComposerAsk`, correct `@HumanitariansAI` folder
label, correct title/topic/command/check-list), and BOUT (`OutroCTA`,
correct title + "@HumanitariansAI" + Subscribe) all centered, legible,
safe-inset, no text overlap. No remaining blockers.

**Audio (independently reverified beyond compile.py's own gate):** ffprobe
confirms an AAC mono stream at 48kHz present; master mtime (1787981770)
newer than beat_sheet.json (1787981645); `ffmpeg -af volumedetect`:
mean_volume **-23.9 dB**, max -2.9 dB — comfortably above the -40 dB floor.
Resolution confirmed 3840×2160 via ffprobe.

Metadata file written: `claude-code--claude-liam-command-development.md`
(channel @HumanitariansAI, **Playlist: Claude Code** — SUBJECT.json's
`family` is `"claude-code"`, a direct match in
`skills/make/hai-simple/loop/playlists.json`'s map). Per the DELIVERY
CONTRACT format, the description also carries the direct code link.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-29 — Phase 4 delivery

Master is already 3840×2160 natively (compile.py's 4K LAW), so the
Fellows-facing 4K file is the same render, copied to the `-4k` filename
`deliver.py` expects.
