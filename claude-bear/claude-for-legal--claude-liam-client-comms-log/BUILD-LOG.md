# BUILD-LOG — claude-for-legal--claude-liam-client-comms-log

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-client-comms-log/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-clinic skill `client-comms-log`.

**Source-fidelity blocker, and how it was handled (read before touching this
reel again):** the source's beat_sheet.json never received its
skill-specific "Claude's job: ___" fill — the literal placeholder `>`
survives verbatim in four beats (B00, B03, BVDT, BHTF), the identical
unfilled-`>` bug already documented on the `claude-for-legal--claude-liam-
case-brief` sibling redo (and, per that reel's own log, on `claude-for-
legal--claude-liam-build-guide` before it — this is a batch-build defect
that runs across the whole `claude-for-legal` family, not a one-off). The
SKILL.md client-comms-log was meant to describe
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/client-comms-log/SKILL.md`)
does not exist on this machine — confirmed by `find` across the whole
`anthropics/claude-for-legal/` tree (only `youtube/` exists locally; no
`legal-clinic/` directory). This is NOT a "genuine blocker that halts the
build" per the completion law, because the source DOES establish real,
generic, true facts about how a Claude skill works (a folder Claude reads
before it acts, one file — SKILL.md — read top to bottom and executed step
by step, and the specification semantics: repeatable results in exchange
for a hard limit at the file's edge) — those facts are what carried over.
What did NOT carry over, because it was never actually present in the
source: any specific claim about what client-comms-log's particular
legal-clinic procedure does. This redo treats "client-comms-log" literally
and generically — the named example of a skill-shaped folder, using only
the well-known, generic shape of a client-communications log entry (date,
contact, channel, summary, follow-up — the same kind of record any
practice-management tool or CRM keeps) as anchor flavor — and never
asserts an invented procedure from the unread SKILL.md. Logged in
QUESTION.md and SCRIPT.md as well.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads it and executes the file's steps in order, with no
branching unless the file itself branches; a skill is a specification, not
a capability — its payoff is repeatable results, its limit is anything the
file never covers.

**New content added to meet hai-simple's spine (not in the source, but not
invented legal-specific fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat (WRONG-GUESS LAW / ANCHOR LAW /
BOTH-DIRECTIONS LAW all require their own beat). Added: B01 (stakes —
"a client-comms-log skill" sounds like a relationship upgrade), B02 (wrong
guess broken with a falsifying case — delete the skill's folder, no client
history is forgotten, because nothing was stored between runs), B06 (anchor
payoff — restates the design tell against the named anchor), B07 (both
directions — a clean entry proves nothing about understanding; a messy one
proves nothing about breakage). B03/B04/B05 carry the source's anatomy/
pipeline/design-tell facts forward, with B03 now also serving as the anchor
plant (client-comms-log's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro). Result here: B00 +
7 body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — a small, proportionate
expansion to satisfy hai-simple's mandatory six-move spine, identical in
shape to the `claude-for-legal--claude-liam-case-brief` sibling redo, which
hit the same source-fidelity gap.

**B00 WRITER LAW:** wrong guess — a newcomer assumes "Claude has a
client-comms-log skill" means the model itself now keeps a persistent
memory of clients across conversations. Typed text: "Claude remembers
every / client call with the / client-comms-log skill. / What is a
skill?", trigger "remembers" → replacement "logs", ending on the real
question. Audio 12.5s — clears the ≥8s WRITER LAW floor with wide margin;
verified on a late frame (t=11.0s) that the correction resolves to "logs"
and the typing has progressed to "What" (cursor mid-word) before the beat
ends, confirming the correction lands on screen well before cutoff.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer pattern verbatim from the
`claude-for-legal--claude-liam-case-brief` sibling redo, adapted in this
reel's own `scenes.py` with client-comms-log-specific chip labels and
narration. Anchor pair: B03 plants `client-comms-log/` + `SKILL.md` as two
plain chips; B06 returns the identical composition with `SKILL.md`
accented. Close: BCRY `WantQuote` (carry-out), BHTF `ClaudeComposerAsk`
(explicit `folderLabel: "@HumanitariansAI"` — the known
ClaudeComposerAsk-defaults-to-@NikBearBrown bug, worked around per
precedent — confirmed correct on the rendered frame), BOUT `OutroCTA`
(@HumanitariansAI). All four Remotion + WantQuote component prop schemas
verified renderable via `./art scenes --check` before authoring the sheet
(GATE L).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats (foreground,
`render_scenes.py`, exit 0) and 4 Remotion beats via `remotion_scenes.py`
(the call auto-backgrounded past the tool's 120s timeout; blocked on it
explicitly with TaskOutput rather than ending the turn, per the COMPLETION
LAW and the one-shot-invocation rule — exit 0, all 4 beats confirmed
rendered before moving on).

**GATE T (type_check.py): PASS** (0 FAILs across all 11 beats) — the
chip-row/chip-stack renderer's known kerning/bbox-overlap fixes (upright
serif captions, MUTE-not-strikethrough for rejected chips,
`render_chip_stack`'s one-phrase-per-row layout for B07) were reused
directly from the case-brief sibling, so no new type-check defect
surfaced.

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media).
`claude-for-legal--claude-liam-client-comms-log.mp4`, 119.4s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11 (63%),
over the toolkit's ~40% "pantry cap" motion-diversity guidance
(MOTION.md) — noted, not treated as a gate; this reel is legitimately
diagram-heavy (a skill's anatomy/mechanism/spec argument reads naturally
as labeled-chip diagrams) and every GRAPHIC beat is original,
locally-rendered Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled frames at 1/3 fps across the full runtime
and read one representative frame per beat by hand — all legible, correct
chip content, safe insets, no overlapping text, the B03→B06 anchor pair
visually identical as intended (only the accent shifts to `SKILL.md`),
B07's vertical-stack layout reads cleanly, BHTF/BOUT both carry
@HumanitariansAI correctly. B00's correction frame confirmed at t=11.0s
(mid-beat): text reads "Claude logs every client call with the
client-comms-log skill. What|" — the "remembers"→"logs" correction has
already resolved and typing is continuing toward the final question.

**Audio presence:** `ffmpeg -af volumedetect` (via compile.py's own GATE
AUDIO check) on the compiled master: mean_volume **−24.0 dB** — comfortably
clears the −40 dB floor.

**Master vs. beat_sheet.json:** master mtime is newer than beat_sheet.json's
last content edit; beat_sheet.json was NOT touched after compile, per the
"never touch beat_sheet.json after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Status: DONE — review cut passes every gate** (content-check, frame-check,
lane-check, GATE AUDIO, GATE T, Gate V by eye). Source-fidelity gap logged
above and in QUESTION.md/SCRIPT.md/the description's "Deliberately not
claimed" section — nothing about the actual legal-clinic client-comms-log
procedure is asserted anywhere in this reel.

## 2026-08-29 — Phase 4 delivery
