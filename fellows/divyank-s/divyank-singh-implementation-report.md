# Implementation Report: Building Three Brutalist Explainer Reels

**Author:** Divyank Singh
**Email:** singh.divya@northeastern.edu
**Date:** July 24–25, 2026
**Scope:** End-to-end implementation of one reel in each of the `brutalist.art`
toolkit's three video-explainer skills (`ai-explainer`, `cli-explainer`,
`deep-explainer`), including all environment debugging required to get the
toolkit rendering on this machine. Total cost: **$0.00** (Kokoro TTS is
local; Remotion rendering is local; no API keys used anywhere).

This report is a specific technical account of what was actually done —
exact commands, exact version numbers, exact bugs and their fixes — not a
summary of the toolkit's documentation.

---

## 1. Environment: what had to be fixed before anything would render

The toolkit's own docs (`HOW-TO.md`) claim the Kokoro voice model "ships
inside this toolkit" and imply the render pipeline works out of the box.
Neither was true on this machine (macOS 13.4, Darwin 22.5.0, Apple Silicon).
Three separate, unrelated bugs had to be diagnosed and fixed, in this order:

### 1.1 No audio engine installed

- System Python was 3.14.6 (via Homebrew), too new for several of the
  toolkit's pinned dependencies (`Pillow>=10.2,<11` fails to build its C
  extension against 3.14; `manim>=0.18,<0.19` has no wheel for 3.14 at all).
- Fix: installed Python 3.11.15 via Homebrew (`/opt/homebrew/bin/python3.11`),
  created a dedicated virtualenv at `brutalist.art/.venv/` (added to
  `.gitignore`), and installed only the audio-critical packages directly —
  `kokoro-onnx>=0.4`, `mutagen>=1.47,<1.48`, `Pillow>=10.2,<11` — without the
  Manim/faster-whisper packages, which still fail on this machine (see 1.4).
- Ran `./setup --install`, which downloaded the two Kokoro model files
  (`kokoro-v1.0.onnx`, ~325MB; `voices-v1.0.bin`, ~28MB) from
  `github.com/thewh1teagle/kokoro-onnx` releases into
  `brutalist.art/runtime/models/kokoro/` — these are git-ignored
  (`runtime/models/kokoro/*.onnx`, `*.bin`), so every machine needs this
  step once.

### 1.2 Remotion required macOS 15; this machine runs macOS 13.4

This was the single largest bug and is the actual subject of the
`cli-explainer-demo` build (Section 3, below).

- Every Remotion render aborted with:
  ```
  dyld[<pid>]: Symbol not found: _AVCaptureDeviceTypeContinuityCamera
    Referenced from: .../compositor-darwin-arm64/libavdevice.dylib
    (built for macOS 15.0 which is newer than running OS)
    Expected in: /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
  ```
  followed by `Error: Command was killed with SIGABRT`.
- Confirmed the installed Remotion version was `4.0.486` (resolved from
  `"remotion": "^4.0.0"` in `runtime/remotion/package.json`), and confirmed
  the exact minimum-OS requirement baked into the binary itself with:
  ```
  otool -l node_modules/@remotion/compositor-darwin-arm64/libavdevice.dylib \
    | grep -A3 LC_BUILD_VERSION
  #       cmd LC_BUILD_VERSION
  #  platform 1
  #     minos 15.0
  ```
- Located the exact version boundary by pulling individual
  `@remotion/compositor-darwin-arm64` releases with `npm pack` and probing
  each one's `libavdevice.dylib` the same way, across a coarse sweep
  (versions 320/350/380/400/420/430/440/445/448) then a fine sweep
  (431/433/435/436/437/438/439):
  | Version | `minos` |
  |---|---|
  | 4.0.320 – 4.0.438 | **13.0** |
  | 4.0.439 – 4.0.486 (and later) | **15.0** |
  - Cross-referenced this against the actual Remotion GitHub history:
    PR #7028 (merged 2026-04-09) documented macOS 13 as the minimum and
    added a friendlier runtime error message; PR #7067 (merged 2026-04-14)
    raised the *compiled binary's* minimum further, to macOS 15. Release
    `4.0.438` (2026-04-10) is the last one built before that second bump;
    `4.0.439` (first seen 2026-04-20 in the registry) is the first with the
    macOS-15 binary.
- Fix: pinned exact versions in `runtime/remotion/package.json`:
  ```json
  "@remotion/cli": "4.0.438",
  "@remotion/paths": "4.0.438",
  "remotion": "4.0.438"
  ```
  then `rm -rf node_modules package-lock.json && npm install`. Verified with
  a direct test render (`npx remotion render src/index.ts ClaudeComposerAsk
  /tmp/test-B00.mp4 ...`) before touching any real reel.

### 1.3 37 dead cross-machine symlinks broke the Remotion asset bundler

- Once the version pin fixed the compositor, a *different* error appeared on
  the very first real render:
  ```
  Error: ENOENT: no such file or directory, realpath
    '.../runtime/remotion/public/adaptive-therapy-mp3'
  ```
- `runtime/remotion/public/` contained 47 entries; 37 were symlinks pointing
  at `/Users/bear/Documents/CoWork/bear-textbooks/books/.../mp3` — the
  original toolkit author's machine, a path that doesn't exist here.
  Remotion's bundler `realpath`s every file under `public/` on every render,
  regardless of which composition is being built, so this broke *all*
  rendering, not just the reels that would have used those assets.
- Fix (confirmed with the user before acting, since it touched tracked
  files across the whole toolkit): removed the 37 broken symlinks with a
  loop testing `[ -L "$f" ] && [ ! -e "$f" ]`, keeping the 10 real assets
  (`bear-brown-logo-mp3`, `hai-wordmark-mp3`/`.svg`, `musinique-logo*`,
  `h-logo-mp3`, `logo-outro`, `bear-brown-initials-showcase-mp3`) intact.

### 1.4 Manim is not installed and cannot be, on this machine, without more setup

- `manim>=0.18,<0.19` has no wheel for Python 3.14 in the `requirements.txt`
  install path; even after switching to Python 3.11, building `manimpango`
  failed:
  ```
  Package pangocairo was not found in the pkg-config search path.
  RequiredDependencyException: pangocairo >= 1.30.0 is required
  ```
- No fix applied — this machine has no system `pangocairo`/`pkg-config`.
  Both `cli-explainer` and `deep-explainer` nominally expect a Manim lane;
  both substitute Remotion patterns instead (documented per-build below and
  in each reel's own `BUILD-LOG.md`), rather than silently dropping the
  requirement.

### 1.5 `run.sh`'s per-reel `scenes.py` guard

- `runtime/scripts/run.sh` refuses to render into any reel folder that
  lacks its own `scenes.py`, *even with zero Manim beats*, to prevent the
  shared `manim/animated_graphics.py` (which only contains fixture scenes
  for a different reel, `vox-electoral-college`) from leaking into an
  unrelated reel:
  ```
  [run] REFUSED: <reel> has no scenes.py. The shared animated_graphics.py
  [run] holds only the electoral-college fixture scenes...
  ```
- Fix: added a minimal `scenes.py` (docstring only, no `Scene` classes) to
  each of the three reel folders — satisfies the guard; `run.sh`'s own
  regex scan for Manim `Scene` classes then correctly finds zero and skips
  the Manim stage entirely.

### 1.6 A hardcoded branding lint blocked the `claude-liam` channel for any topic but one

- `runtime/qc/beat_lint.py` (GATE L) enforces a fixed "kicker" (topic
  string) per channel, read from `runtime/qc/brand_labels.json`:
  ```json
  "claude-liam": { "kicker": "Computational Skepticism", "chip": "@NikBearBrown" }
  ```
  This is left over from a different, pre-existing series in the full
  toolkit. Any `claude-liam` reel on a different topic (all three built
  here) fails this lint by design.
- Resolved per explicit user decision each time: ran with `ART_QC=0`,
  which disables GATE L along with the other automated QC gates (A, W, V)
  for these one-off demo builds, rather than editing the shared
  `brand_labels.json` (which would change the fixed kicker for every future
  `claude-liam` reel in the toolkit) or mislabeling the topic to match.
  **Consequence:** none of the three final builds has had a frame-level
  Visual QC pass (`_qc/REPORT.md`, `qc-sheet.png` contact sheet review) —
  they compiled and played back correctly, but weren't inspected
  frame-by-frame against the toolkit's 9-point QC rubric.

### 1.7 Two Remotion components referenced by name didn't exist as registered compositions

- The beat sheets initially referenced Remotion patterns `"LayerStack"` and
  `"ChipGrid"` directly (the names of the underlying React components in
  `runtime/remotion/src/illustrations/structural.tsx`). Rendering failed
  with a "composition not found" style error listing dozens of unrelated
  registered IDs — because `LayerStack`/`ChipGrid` are only registered as
  fixed-sample-prop *preview* compositions (`Illu-LayerStack`,
  `Illu-ChipGrid`, 150 frames, hardcoded example data), not as
  general-purpose, prop-driven compositions.
- Root cause found by grepping `runtime/remotion/src/Root.tsx` for existing
  parameterized wrappers: `ClaudeScienceLayerStack` / `ClaudeScienceSourceFlow`
  / `ClaudeScienceChipGrid` (defined in `runtime/remotion/src/ClaudeScienceIllu.tsx`)
  are fully generic passthrough wrappers — despite the reel-specific name,
  their zod schemas accept arbitrary `layers[]` / `items[]` / `caption` /
  `sparkLine` props. Fix: used these registered wrapper names in place of
  the bare component names; no new Remotion code was written.
- Separately, `DivergentFates` (a `deckPatterns.tsx` rhetorical pattern) *is*
  registered directly under that name, but expects its props nested one
  level deeper than the other components — `{"data": {"slideMeta": ...,
  "tracks": [...]}}`, not a flat object — found by reading its
  `Composition` registration's `defaultProps` in `Root.tsx`.

### 1.8 A background render silently overwrote an in-progress edit

- While `run.sh`'s Remotion render was still running in the background for
  `ai-explainer-demo`, a new beat (`BINV`, the archival-image beat) was
  added to `beat_sheet.json` on disk. The in-progress `remotion_scenes.py` /
  `compile.py` processes had already loaded the *old* version of the file
  into memory at start; both scripts write the full sheet back out at the
  end, so the running process's stale copy overwrote the edit, silently
  dropping the new beat from the file (though the beat's already-generated
  audio and image files were untouched on disk).
- Fix: no special tooling — just re-applied the same edit once the render
  had finished, then re-ran. Lesson recorded here since it isn't a toolkit
  bug so much as a race condition in editing a beat sheet while a build is
  in flight.

---

## 2. Build 1 — `ai-explainer`: *"Claude, Gated."*

- **Final path:** `ai-explainer-demo/mp4/claude-liam-blueprint-before-draft.mp4`
  — **145.69 seconds** (2:25.7), 27,296,915 bytes, 3840×2160.
- **Channel:** `claude-liam` (Kokoro `am_onyx`, "Onyx" — the toolkit's only
  male voice; already the channel default, no override needed).
- **Topic selection, corrected mid-build:** the reel was first drafted
  around a generic LLM-tokenization concept, built into a nonexistent
  `Northeastern/Humanitarians/book/` path invented for the purpose. This
  was wrong on two counts — no such book existed, and the content had no
  connection to any real source. Corrected after the user pointed to the
  real book, `ai1-cli`: found `ai1-cli/vids/video-ideas.md`, a real,
  pre-scored scout file (9 candidate topics, each with a hook, core idea,
  and a 1-10 score). Selected **Candidate 01**, *"Why the Blueprint Comes
  Before the Draft"* (score 9/10, tied with Candidate 04, the CAJAL
  figure-detection appendix) — chosen over the tie because its four-gate
  structure mapped directly onto an already-registered Remotion component
  (`ClaudeScienceLayerStack`) with no new code needed, and because it
  represents the book's foundational chapter rather than an appendix tool.
- **Source:** `ai1-cli/chapters/01-inventory-research-blueprint-signoff.md`,
  read in full.
- **Structure:** 9 beats (`B00`–`B07` plus `BINV`, inserted between `B01`
  and `B02`). Cold open → four-gates overview (`ClaudeScienceLayerStack`) →
  **archival beat** (`BINV`) → ask/result pair on the chapter-17
  misclassification catch (`DivergentFates`) → the rejected-prompt beat
  (`ClaudeScienceChipGrid`) → verdict (`ClaudeVerdictArtifact`) → handoff →
  title outro.
- **The archival beat (`BINV`):** added after the initial 8-beat cut, at
  the user's request to add "character" via a real historical image. Found
  via the Wikimedia Commons API (`commons.wikimedia.org/w/api.php`, since
  Smithsonian's own search page at `si.edu/search/collection-images`
  returns `HTTP 403 Forbidden` to non-browser fetches): a 1983–84
  photograph of a library card catalog, credited to the Mennonite Church
  USA Archives (Goshen College Library, Goshen, Indiana), licensed "No
  known copyright restrictions" (Flickr Commons). Downloaded directly to
  `media/BINV.png` (bypassing the toolkit's `pantry.py` intake script,
  whose beat-ID regex `^([A-Z]{1,3}\d{2})` — 1-3 letters then exactly 2
  digits — doesn't match the ID `BINV` and would have collided with the
  unrelated real beat `B01` if forced).
- **Every on-screen quote checked verbatim against the source chapter** —
  e.g. "the agent prepares; the human signs" (line 15), "the inventory is
  a claim, and you just checked it" (lines 23 & 119), the chapter-17
  correction (line 119), "I don't understand that prompt at all" (line
  131) — logged claim-by-claim in that folder's `SOURCES.md`.
- **Gates:** `PEDAGOGY.md` signed `VERDICT: PASS` twice by the user in
  chat — once for the original 8-beat cut, once as a separate addendum
  after the `BINV` beat was added (narration budget re-verified
  programmatically at that point: B01 62 words, B03 66, B04 61, all inside
  the 45–70-word bookend-adjacent band).

---

## 3. Build 2 — `cli-explainer`: *"Claude, Patched."*

- **Final path:** `cli-explainer-demo/mp4/cli-liam-remotion-macos-fix.mp4`
  — **152.20 seconds** (2:32.2), 7,593,236 bytes.
- **Topic:** there was no `cli-ideas.md`/`simulation-ideas.md` scout card in
  `ai1-cli` (the routing convention this skill otherwise expects), so the
  skill's own alternate trigger — "the source is a thing you built" — was
  applied directly to Section 1.2's real debugging session from earlier
  the same day: the Remotion macOS-13-vs-15 compositor fix.
- **A documentation/reality mismatch found while reading the skill:**
  `skills/make/cli-explainer/SKILL.md` repeatedly references
  `vox_run.sh`/`vox_compile.py` as the render pipeline; neither file exists
  anywhere under `runtime/scripts/`. The actual scripts are `run.sh` and
  `compile.py` — confirmed by cross-checking `compile.py`'s documented slot
  precedence (`media/[BID].mp4 > manim/[BID].(mp4|mov) > media/[BID].png >
  slate`) against the skill doc's near-identical description of
  `vox_compile.py`'s behavior. Used `run.sh`/`compile.py` throughout; the
  `vox_*` names appear to be stale documentation from an earlier rename.
- **Structure:** 11 beats, the full required spine — `B00` INTRO,
  `B01` PROBLEM, `B02` ASK → `B03` CODE → `B04` OUTPUT (discovery cycle),
  `B05` CHANGE → `B06` CODE → `B07` OUTPUT (the mandatory revision cycle),
  `B08` SUMMARY, `B09` NEXT STEPS, `B10` OUTRO.
- **Real code shown on screen** (per the skill's ACTUAL-CODE LAW — no
  pseudocode): the exact `otool -l ... | grep -A3 LC_BUILD_VERSION`
  diagnostic command and its real output (`B03`), and the exact
  `for v in 431 433 435 436 437 438 439; do npm pack ...; done` version-sweep
  script and its real per-version results (`B06`) — both are verbatim
  transcripts of commands actually run in Section 1.2, not reconstructions.
- **Output beats without Manim:** `B04` uses `BinaryBranch` (a registered
  Remotion rhetorical pattern, `deckPatterns.tsx`) to show the "our code vs.
  the binary" diagnosis resolving to "it's the binary"; `B07` reuses
  `DivergentFates` to show the real 4.0.438-vs-4.0.439 outcome split.
- **A specific defect found and fixed after the first full render:** beats
  `B01` (PROBLEM) and `B08` (SUMMARY) were authored as `{"type": "GRAPHIC",
  "source": null}` silent title cards, mirroring the skill's own shipped
  reference example (`reference/example-cli-beat_sheet.json`). This left
  both as unfilled `SLATE`s after rendering, and `compile.py` correctly
  refused to produce a clean master with 2 slates remaining. On review, the
  skill's own SHOW-DON'T-TELL law text explicitly contradicts its own
  reference example here: *"extend it to EVERY beat: if a PROBLEM or
  SUMMARY line describes something that can move, show it moving... not a
  static card."* Fixed by giving `B01` a real `ClaudeScienceSourceFlow`
  illustration (three reel types converging on one shared render step) and
  `B08` a real `ClaudeVerdictArtifact` recap card — both using already
  measured audio durations, no re-recording needed. Third render produced
  an 11/11 clean master.

---

## 4. Build 3 — `deep-explainer`: *"Claude, Constitutional."*

- **Final path:** `deep-explainer-demo/claude-liam-ai1-four-gates.mp4` —
  **339.22 seconds (5:39.2)**, 126,756,487 bytes, 3840×2160. (This build's
  root-level copy has not been moved/removed, unlike builds 1 and 2, whose
  root copies were separately deleted after completion — the matching
  slate cut, `claude-liam-ai1-four-gates-slate.mp4`, 129,046,554 bytes, is
  also still present at the same location.)
- **Constraint stated by the user beforehand:** the video "must not be
  shorter than the mentioned time limit" — the skill's own documented band
  is 5–10 minutes, so the floor was 300 seconds. Measured result: 339.22s,
  39 seconds over the floor, safely inside the band. (The planning-time
  estimate, using the skill's own ~2.9 words/second rule of thumb, had
  projected 438s/7.3 min; real Kokoro pacing came in faster than that
  estimate.)
- **Topic scope decision:** rather than spanning several `ai1-cli`
  chapters (which would have required new, unverified reading under time
  pressure), the entire episode was built from the single chapter already
  used in Build 1 (`chapters/01-inventory-research-blueprint-signoff.md`),
  treated as its own real 4-part framework — this chapter's four gates
  (inventory, research, blueprint, sign-off) directly satisfy the skill's
  "multi-act, 4+ parts" trigger condition on its own.
- **Structure:** 32 beats — `B00` cold open, four acts (`A1C`–`A4C` segment
  cards + six content beats each = 28 body beats), `BVDT` verdict, `BHTF`
  handoff, `BOUT` outro.
  - **Act I — Read Before You Trust** (inventory): the chapter-17 catch
    (`DivergentFates`, reused legitimately as this episode's own worked
    example), the real scale numbers (24 chapters, ≈117,000 words, median
    ≈5,000 words/chapter — chapter line 117), a 3-row real inventory-table
    sample, the author's own real margin note ("It's long. I like it...",
    line 123).
  - **Act II — Believe Nothing Once** (research): the rejected elaborate
    prompt vs. the plain 4-question replacement (`BinaryBranch`), the
    real ✓✓/⚡/⚠ triangulation-reconciliation marks (line 151), the real
    "twenty-four for twenty-four 'highly relevant' should make you
    suspicious" quote (line 157), "the disagreements are the decision"
    (line 158).
  - **Act III — A Few Hundred Decisions** (blueprint): the four real named
    readers (line 165), the real 21/2/1/0-chapter disposition
    (`ClaudeScienceLayerStack`, line 167), "audience-conditional relevance,
    not thin evidence" (line 178), "verify before drafting, or the chapter
    reframes around what verifies" (line 169).
  - **Act IV — The Signature That Counts** (sign-off/GATE 0): the five
    real discipline notes the signature warrants (lines 175–181), the real
    three-word approval quote "That looks great." (line 175), approve-vs-
    refuse (`BinaryBranch`, line 58), the spine quote "the agent prepares;
    the human signs" reprised, and the real closing bridge line "you now
    own a signed plan for a book that doesn't build under your name yet"
    (line 78).
- **VOX quota — 6 real archival photographs, all sourced by hand via the
  Wikimedia Commons API** (not AI-generated, not stock), one to two per
  act: Library of Congress reading room (1897, public domain), Uris
  Library Stacks at Cornell (CC BY 2.0), a museum surveying-chain object
  photo illustrating triangulation (public domain), an antique writing
  desk at Casa Loma (CC BY 2.0), *"Architect and engineer"* (1947, no
  known copyright restrictions), and a document-signing-ceremony photo
  between Azerbaijan and the EU (CC BY 4.0). Measured lane share: 6 of 28
  body beats = **21.4%**, inside the skill's target 20–25% band (and the
  15–30% no-warning band). A named-individual signing photo (Reagan and
  Gorbachev, 1987, also public domain and higher resolution) was found in
  the same search but deliberately **not used**, to avoid the skill's
  Tier-3 rule that using a specific named real person as a beat's subject
  requires an explicit human rights-escalation decision every time — the
  nameless Azerbaijan–EU photo served the same illustrative purpose
  (ratification/sign-off) without that escalation.
- **Manim substitution:** no Manim on this machine (Section 1.4); its
  documented ~25–40% share was absorbed into the REMOTION lane across all
  four acts, using only already-registered components
  (`ClaudeScienceChipGrid`, `ClaudeScienceLayerStack`, `BinaryBranch`,
  `DivergentFates`, and `FluencySegmentCard` — reused from a different,
  pre-existing reel, `claude-liam-fluency-trap`, for the act-title cards,
  since it's a generic `{title, index}` component already tokenized to the
  Claude palette, `#F2F0E9`/`#3D3929`).
- **Ad hoc "quote card" pattern:** no dedicated quote/citation component
  was found registered in `Root.tsx`; single-item `ClaudeScienceChipGrid`
  (`cols: 1`) was reused as a one-card verbatim-quote reveal in place of
  building a new component mid-build.
- **Gate D2 (`SHOPPING.md`), written after audio lock as the skill
  requires:** closed with **zero open entries** — all 6 VOX stills were
  sourced and placed before the previz/render step, rather than left as
  asks for a human.
- **Render outcome:** this was the only one of the three builds to compile
  cleanly — 32/32 beats filled — on the **first real render attempt**,
  because every failure mode found in Builds 1–2 (the `scenes.py` guard,
  the `LayerStack`/`ChipGrid` naming issue, `DivergentFates`'s nested
  `data` prop shape, and the null-source PROBLEM/SUMMARY-style slate
  defect) was corrected in the beat sheet before the first `./art run`
  call.

---

## 5. Deliverables

| Build | Final master | Duration | Size | Beats | Gates signed |
|---|---|---|---|---|---|
| `ai-explainer` — "Claude, Gated." | `ai-explainer-demo/mp4/claude-liam-blueprint-before-draft.mp4` | 145.69s (2:25.7) | 27.3 MB | 9 | `PEDAGOGY.md` PASS ×2 |
| `cli-explainer` — "Claude, Patched." | `cli-explainer-demo/mp4/cli-liam-remotion-macos-fix.mp4` | 152.20s (2:32.2) | 7.6 MB | 11 | `PEDAGOGY.md` PASS |
| `deep-explainer` — "Claude, Constitutional." | `deep-explainer-demo/claude-liam-ai1-four-gates.mp4` | 339.22s (5:39.2) | 126.8 MB | 32 | `PEDAGOGY.md` PASS, Gate D2 (`SHOPPING.md`) clear |

Every build also has, in its own folder: `beat_sheet.json` (with
`actual_duration_s` stamped per beat from real Kokoro output),
`SOURCES.md` and/or `FACTCHECK.md` (claim-by-claim verification against the
named source), `PEDAGOGY.md` (the signed GATE P record), and
`BUILD-LOG.md` (build 2 and 3) documenting the decisions logged in
Sections 2–4 above in that build's own words.

## 6. What was not done

- **Frame-level Visual QC** (`_qc/REPORT.md`, the 9-point rubric, the
  `qc-sheet.png` contact sheet review) was not run on any of the three
  builds — `ART_QC=0` was used throughout specifically to bypass the
  hardcoded branding-kicker lint (Section 1.6), which also disables this
  pass. All three compile and play back correctly, but none has had a
  human or automated frame-by-frame inspection.
- **No video is published or authorized for publication.** All three
  remain in their build folders.
- **Manim is still not installed** on this machine; the substitution
  described in Sections 3 and 4 is a logged workaround, not a permanent
  fix. Installing it would need a system `pangocairo` (e.g. via Homebrew)
  in addition to the Python package.
- **`runtime/qc/brand_labels.json` was left unedited** — the
  `claude-liam` → "Computational Skepticism" kicker mismatch (Section 1.6)
  still applies to any future `claude-liam` reel on a different topic.
