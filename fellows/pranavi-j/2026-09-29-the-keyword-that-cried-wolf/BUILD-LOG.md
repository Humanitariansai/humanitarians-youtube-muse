# BUILD-LOG — The Keyword That Cried Wolf

## 2026-09-29/2026-10-02 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-09-29. **FACTCHECK:** resolved same day — B06 gets a "not
reviewed — below alert threshold" label on the SEC case row (never actively reviewed-and-approved,
since its `urgency_score` never crosses the alert gate), B07's honest-limits beat kept at full
weight, no softening.

**Audio:** Kokoro `af_bella`, all 9 beats, B00 a real silent mp3 (`ffmpeg anullsrc`) with
`audio_policy: "silence"` set explicitly per `build_safety.py`'s silent-required-audio gate.

**`scenes.py` (landscape):** authored with a `T()` safe-text helper (creates `Text()` at
`font_size=48`, then scales geometrically to the intended size) used for every on-screen string —
avoids a confirmed Manim/Pango small-font-size rendering artifact (phantom gaps inside words, e.g.
"video" -> "v ideo") that bit two sibling projects earlier this cycle. B03 quotes the real scoring
rule verbatim; B04 shows both real trigger-word titles in their actual context; B05 explicitly
shows the fail-open third branch (model-fails -> goes through anyway), not just the happy path;
B06 shows all 3 test cases together with the SEC case correctly labeled "not sent to model."

**Landscape final:** 3840x2160, 135.54s. GATE V: 0 BLOCKER, 0 MAJOR.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(1080x1920-native, rendered 2160x3840), same `T()` helper plus the portrait `config.frame_width`
patch (Manim's CLI `-r` flag doesn't recompute `frame_width` for portrait otherwise — documented
fix, copied from the `2026-09-14` sibling projects). B05's 3-branch flow diagram and B06's 3-row
table both needed real redesign (not just narrowing) to stay legible in the narrow canvas —
confirmed by direct frame inspection, not assumed.

**Vertical final:** 2160x3840, 135.42s. GATE V: 0 BLOCKER, 2 MAJOR (both on B08, brand/sign-off
card, borderline underfill exactly at the 55% floor — personally confirmed via direct frame
extraction that the card is fully legible and well-composed; same accepted minor-cosmetic category
as the brand cards in every sibling video this cycle).

**Real bugs hit and fixed during this build (both previously known, both handled per established
playbook):**
- **Stale render cache:** `run.sh` does not detect `scenes.py` source changes and silently reuses
  old `manim/*.mp4`/`clips/*.mp4`/Manim's own `media/` cache. Deleted and re-rendered clean
  whenever a scene edit followed a prior render, and verified every clip's mtime postdates
  `scenes.py`'s mtime before trusting any render as current.
- **Manim Text() small-font-size artifact:** avoided from the start in this project by using the
  `T()` helper for every beat in both `scenes.py` files, rather than discovering and retrofitting
  it after the fact (as happened on the `2026-09-14` sibling projects).

**Process note:** this build spanned several agent sessions due to repeated transient network
disconnects (API `ECONNRESET`), not logic failures — each resumption re-verified actual on-disk
state (file mtimes, process list, deliverable hashes) before continuing, rather than trusting the
prior session's self-report. The final landscape and vertical masters were personally
re-inspected frame-by-frame (B05, B06, B08) directly from the shipped deliverables as a final
check before considering this project done.

**Deliverables confirmed, both renamed and verified:**
- `deliverables/landscape/KeywordReScoring_SaiPranaviJeedigunta.mp4` (+ `.verified.json`)
- `deliverables/vertical/KeywordReScoring_SaiPranaviJeedigunta.mp4` (+ `.verified.json`, input
  hashes confirmed matching the final clips on disk)

Publishing not authorized. Nothing inside `brutalist/` was modified.
