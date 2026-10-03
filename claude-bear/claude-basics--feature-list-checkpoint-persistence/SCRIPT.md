# Persisting Progress Across Context Windows — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`claude-basics/feature-list-checkpoint-persistence`, Teardown register,
unbuilt scaffold — 0/8 beats filled). Register: **Plain**. 8 beats, matching
the source's beat count exactly. Carry-out derived from the source's verdict
beat (CARRY-OUT.md, GATE C) — already a factual recap, not a design
judgment, so it needed only a register label, not a rewrite.*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Act | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer cold open | "People assume an agent remembers where it left off. It doesn't — context resets each session. It checks a file instead. How does it know to resume at feature 51, not feature 1?" | Writer types "An agent with 200 features just remembers where it left off. How does it resume at feature 51, not feature 1?"; "remembers" hesitates and corrects to "checks" |
| B01 | 1 the problem | A context window has a limit. When it fills, the session ends. The next session starts blank — no memory of what passed or failed. The agent has two options: re-read everything, which burns half the new context, or guess. Neither works. | Manim: a filled "Session 1" bar next to an empty "Session 2" bar, two dim arrows branching to "re-read everything" and "guess", both struck |
| B02 | **4 ANCHOR PLANTED** | The fix is one file: feature_list.json, 200 entries, each with an id and a status — incomplete or passing. Git commits one per feature, an immutable ledger. Say session one finishes features 1 through 50 — each flips to passing, each committed. Feature 51 is the first one still marked incomplete. | THE ANCHOR — a vertical list of 200 rows; rows 1–50 flip from incomplete to passing as session 1 runs; row 51 stays lit as "first incomplete" |
| B03 | 3 mechanism | Every new session does the same three things: open feature_list.json, find the first entry still marked incomplete, and start there. Implement it, run the tests, commit, mark it passing. Then repeat — read, find the gap, fill it. | A four-step loop diagram: OPEN FILE → FIND FIRST INCOMPLETE → IMPLEMENT + TEST + COMMIT → MARK PASSING, looping back |
| B04 | **4 ANCHOR PAYOFF** | Session two opens the same file. It finds feature 51 marked incomplete — the same one session one left behind — and starts exactly there. No re-reading the first fifty, no guessing. By the end of session two, features 51 through 100 are passing too. | THE ANCHOR RETURNS — same 200-row list as B02; row 51 highlighted as where session 2 opens the file and resumes; rows 51–100 flip to passing as session 2 runs |
| **BCRY** | **6 carry-out** | An agent's context window isn't its memory — it's a workspace. Externalize the state to a file plus git, and each new session just reads it, finds the first gap, and fills it. | the sentence, alone, serif, large |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Externalize my agent's progress to a feature_list.json plus git, so it can resume across sessions — then prove it picks up exactly where it left off, without replaying finished work. Liam, in for Bear. | `ClaudeComposerAsk` — "Your turn." |
| BOUT | outro | Persisting Progress Across Context Windows. Liam, in for Bear. | `OutroCTA` — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-basics`, Teardown, never built) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "An agent with 200 features to implement... how does it know to begin at feature 51 without replaying the first 50?" | unchanged |
| Facts | feature_list.json (200 entries, id + status incomplete/passing); git commit per feature; session 1 does 1–50, session 2 resumes at 51 and finishes 51–100; read → find first incomplete → implement/test/commit → repeat | unchanged |
| Beat count | 8 (B00–B05, YOURTURN, B07) — never built (0/8 filled) | 8 (B00–B04, BCRY, BHTF, BOUT) |
| B00 | `ClaudeComposerAsk` text-card cold open, itself stating the whole scenario | `BrutalistHesitantWriter` (WRITER LAW) — "remembers" → "checks"; the worked (feature 51) case moved to B02/B04 as the anchor pair |
| Register | Teardown (metadata; narration itself was already close to pure mechanism, minimal judgment language) | Plain — no design-judgment clauses survive; framing reshaped into the anchor-pair spine |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | source's YOURTURN/B07 used `ClaudeComposerAsk` / `ClaudeTitleOutro`, `@NikBearBrown` | `ClaudeComposerAsk` (unchanged pattern) / `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| Body B01–B04 | source's B01 (the problem) / B02 (the fix — the file) / B03 (centerpiece — the file mutating, the concrete 1–50 / 51–100 example) / B04 (honesty — scope exclusions) / B05 (verdict recap) | rebuilt as Manim GRAPHIC scenes (`scenes.py`); B02's worked example folded forward into the anchor plant, B03's mechanism kept as its own beat, B04's concrete payoff kept as the anchor payoff, B05's recap promoted to BCRY as the carry-out |

**Component note:** the source's beats used `ClaudeComposerAsk` as a
text-card body pattern (not the cold open it's meant for). Per hai-simple's
spine, `ClaudeComposerAsk` is reserved for the writer handoff / Your Turn
beat only, so B01–B04 were rebuilt as custom Manim scenes carrying the
identical facts and sequence, per the standard GRAPHIC beat pipeline
(`scenes.py` + `render_scenes.py`). This is not a NO-GENAI/NO-PANTRY
substitution — no source beat was `ai-video-prompt`, pantry, or a
human-drop slot.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; the read/find/implement mechanism waits until B03 |
| Wrong guess surfaced and falsified by a case | B00 states it directly ("just remembers") and B01's two dead-end options; B02–B04's concrete feature-51 case falsifies it — it isn't memory, it's a file lookup |
| No design judgment | source narration was already close to pure mechanism; no verdict language on the design itself survives |
| One running anchor, planted and paid off | B02 plants feature 51 as the first incomplete entry after session 1; B04 pays it off — session 2 opens the same file, finds the same entry, resumes there |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not how the initial feature list is generated.** The source attributes
  that to a separate initializer session; this reel doesn't invent a
  mechanism for it.
- **Not the detailed test framework.** The source scopes out how "passing"
  gets decided; so does this reel.
- **No verdict on the design.** Explaining how the checkpoint mechanism
  works is not the same as ruling on whether `feature_list.json` + git is
  the right way to build one — that's Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "Externalize my agent's progress to a feature_list.json plus git, so it
> can resume across sessions — then prove it picks up exactly where it left
> off, without replaying finished work."

Why it's worth running: it forces the viewer to build and verify the actual
resume mechanism, not just read about it — the "prove it" clause means the
prompt isn't done until a second session visibly picks up mid-list.

---
**GATE P — signed:** ______________________  (human)
