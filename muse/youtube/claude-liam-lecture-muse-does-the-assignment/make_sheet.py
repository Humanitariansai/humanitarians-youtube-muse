#!/usr/bin/env python3
"""make_sheet.py — Muse Does the Assignment (lecture, INFO 6205 algorithms).

LECTURE (Bear, 2026-10-02): one film for the whole source, primarily visual,
every body beat auditioning the playset and taking the best visual. Fixed
bookends: hesitant writer -> key terms -> acts -> recap -> Your Turn -> outro.

Source: the Week 1 INFO 6205 assignment "Help Beary Navigate the Forest to
Collect Honey", Muse's three-approach reference solution
(~/workspace/algo-wk1/wk1-beary-pathfinding/solution.py), its 25-test suite,
and the independent assignment audit (ASSIGNMENT-REVIEW.md). All numbers on
screen are computed values from real runs, never invented (see FACTCHECK.md).

The film's spine: Muse is handed the assignment with the instruction "do your
best work, and check the assignment itself for errors." It solves the
pathfinding problem three ways (bitmask DP, state-space BFS, greedy), the
film teaches when to pick which — and closes on the twist: Muse found four
defects in the assignment, including a wrong example answer.

Channel: claude-liam (Liam, in for Bear; Kokoro am_onyx; Teardown register;
@NikBearBrown). Course credit: INFO 6205 Program Structure and Algorithms,
named in BIDEA per the lecture skill's course rule; the outro stays locked.

Kokoro-safety: "BFS" is spoken as letters (whisper-check); "NP-hard" is on
the known-clean list; "INFO 6205" reads as "info sixty-two oh five" (checked).
No acronyms beyond BFS/NP; no version numbers; no pricing tiers.

Lane choices: Manim wins nearly every body beat because the subject IS a
mechanism on a grid — an animated grid walkthrough is the best visual by the
BEST-BEAT LAW. B08 uses a Manim terminal card typing the VERBATIM output of
the real test run (the "real code, run" lane; Remotion can't render in the
build VM, so the capture plays as a Manim card and FACTCHECK.md attests the
text is verbatim). Runner-ups per beat are logged in SHOTLIST.md.

Run: python3 make_sheet.py
Durations: narration at ~150 wpm (words / 2.5), matching the reel clock.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "muse-does-the-assignment"
TITLE = "Muse Does the Assignment"
COURSE = "INFO 6205 Program Structure and Algorithms"


def beat(bid, act, narration, cls, image, show):
    return {"beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}


B = [
    # ── ACT I: the assignment ──────────────────────────────────────────
    beat("B01", "act i · the assignment",
         "Meet Beary. He lives on a grid. Cells marked H hold honey pots. Cells marked O are "
         "obstacles — he cannot cross them. He starts at B. His job: collect every honey pot "
         "and come home, in the fewest steps.",
         "B01_Grid",
         "A 3x3 grid draws itself on the cream stage: B top-left, three H cells, two O cells. "
         "Labels land beside each mark: 'start', 'honey', 'blocked'.",
         [{"at": 0.1, "event": "grid lines draw in"},
          {"at": 0.35, "event": "B, H, O marks pop into their cells; labels land"},
          {"at": 0.7, "event": "a small path dot pulses on B"}]),
    beat("B02", "act i · the assignment",
         "Four rules. One: he moves one cell at a time — up, down, left, right. No diagonals. "
         "Two: every honey pot gets collected. Three: he returns to where he started. "
         "Four: fewest steps wins. And if no route exists at all, the answer is minus one.",
         "B02_Rules",
         "A Beary dot walks the example grid, collecting each H with a terracotta check, then "
         "walks home; a step counter ticks up beside the grid and the 'return to B' leg glows.",
         [{"at": 0.15, "event": "dot starts walking; first H collected, check lands"},
          {"at": 0.45, "event": "all honey collected; counter running"},
          {"at": 0.75, "event": "return leg glows; dot arrives home"}]),
    beat("B03", "act i · the assignment",
         "The assignment gives an example grid and says the answer is six. Hold that number. "
         "We will come back to it at the end — because Muse found something wrong with it, "
         "and it is the best part of the story.",
         "B03_Example",
         "The example grid with a 'says: 6' tag; the six-step tour draws without returning, "
         "then the return leg draws on and the tag flips to a question mark.",
         [{"at": 0.2, "event": "'says: 6' tag lands on the grid"},
          {"at": 0.45, "event": "six-step tour draws, stopping at the last honey"},
          {"at": 0.7, "event": "return leg draws; tag flips to '?', held"}]),
    # ── ACT II: bitmask DP ─────────────────────────────────────────────
    beat("B04", "act ii · first approach: bitmask DP",
         "Muse's first approach starts with a simple observation. Between any two interesting "
         "points — Beary and each honey pot — the shortest walk is just BFS, spreading outward "
         "until it arrives. Run it from every key point, and you get a small table: every leg, "
         "at its shortest.",
         "B04_Legs",
         "A terracotta BFS wave spreads from B across the grid, cell by cell; reached H cells "
         "light up with their distances, and a small distance table fills beside the grid.",
         [{"at": 0.15, "event": "BFS wave starts spreading from B"},
          {"at": 0.45, "event": "honey cells light up with distances 2, 4, 6"},
          {"at": 0.75, "event": "distance table completes beside the grid"}]),
    beat("B05", "act ii · first approach: bitmask DP",
         "Now the grid disappears. What remains is a pure ordering puzzle: visit every honey "
         "pot and come home, cheapest order first. That is the traveling salesperson problem. "
         "Muse solves it exactly — trying every subset of honey pots, remembering each subset's "
         "cheapest finish in a handful of bits.",
         "B05_Order",
         "The grid fades; a subset lattice grows — subsets of honey pots as nodes, terracotta "
         "edges keeping each subset's cheapest cost; the winning order path glows through it.",
         [{"at": 0.15, "event": "grid fades, subset lattice grows"},
          {"at": 0.5, "event": "edges fill with cheapest costs, subset by subset"},
          {"at": 0.8, "event": "winning order path glows through the lattice"}]),
    beat("B06", "act ii · first approach: bitmask DP",
         "The answer: twelve steps, and provably the best — no shorter tour exists. On this "
         "grid it took a fraction of a second. But note the fine print: every subset means the "
         "work doubles with each honey pot you add.",
         "B06_Twelve",
         "The optimal twelve-step tour draws on the grid; a hero '12' lands beside it with "
         "'provably optimal' beneath; a small doubling curve starts rising at the edge.",
         [{"at": 0.2, "event": "optimal tour draws; step counter runs to 12"},
          {"at": 0.55, "event": "hero '12' lands with 'provably optimal'"},
          {"at": 0.8, "event": "doubling curve starts rising beside it"}]),
    # ── ACT III: state-space BFS ───────────────────────────────────────
    beat("B07", "act iii · second approach: state-space BFS",
         "The second approach is simpler to trust. Forget clever ordering. Instead, expand what "
         "a position means: not just the cell, but the cell plus which honey pots you have "
         "already collected. Run one plain BFS over that bigger world. The first time you stand "
         "on the start cell holding everything — that walk is shortest. BFS guarantees it.",
         "B07_States",
         "The grid duplicates into stacked layers, one per collected-set; the BFS frontier "
         "climbs from layer to layer as honey is collected, landing home on the full layer.",
         [{"at": 0.15, "event": "grid stacks into collected-set layers"},
          {"at": 0.45, "event": "frontier climbs layers as honey is collected"},
          {"at": 0.8, "event": "frontier lands on B in the full layer; 'shortest' tag"}]),
    beat("B08", "act iii · second approach: state-space BFS",
         "Two completely different methods should never disagree. So Muse tested them against "
         "each other: three hundred random grids, obstacles and honey scattered everywhere. "
         "They agreed on every single one. Twenty-five tests, all passing.",
         "B08_Crosscheck",
         "A terminal card on the stage types the verbatim output of the real test run: "
         "'25 passed, 0 failed' then 'ALL TESTS PASSED', each line landing with a terracotta check.",
         [{"at": 0.2, "event": "terminal card opens; first lines type"},
          {"at": 0.55, "event": "'25 passed, 0 failed' lands with a check"},
          {"at": 0.8, "event": "'ALL TESTS PASSED' lands with a check"}]),
    # ── ACT IV: greedy ─────────────────────────────────────────────────
    beat("B09", "act iv · third approach: greedy",
         "The third approach is the tempting one. Always walk to the nearest uncollected honey "
         "pot. No subsets, no giant state space — just short BFS hops, one after another. "
         "Fast, simple, and — in general — wrong.",
         "B09_Greedy",
         "On a 4x4 grid the dot hops to the nearest honey, then the next nearest; each hop "
         "draws fast and cheap-looking while a 'feels right' tag fades in and out.",
         [{"at": 0.15, "event": "dot hops to nearest honey"},
          {"at": 0.45, "event": "second nearest-first hop draws"},
          {"at": 0.7, "event": "'feels right' tag fades in, then out"}]),
    beat("B10", "act iv · third approach: greedy",
         "Here is the trap, on a real grid. Nearest-first grabs the close honey and pays ten "
         "steps for the tour. The best order pays eight. Greedy feels right. That feeling is "
         "exactly what this assignment is teaching you to distrust.",
         "B10_Trap",
         "Split stage: greedy's tour draws left in dim grey totaling 10; the optimal tour draws "
         "right in terracotta totaling 8; the two extra steps pulse.",
         [{"at": 0.2, "event": "greedy tour draws left, totaling 10"},
          {"at": 0.55, "event": "optimal tour draws right in terracotta, totaling 8"},
          {"at": 0.85, "event": "the two wasted steps pulse"}]),
    # ── ACT V: which one, when ─────────────────────────────────────────
    beat("B11", "act v · which one, when",
         "So why three answers to one problem? Because this problem is NP-hard — no known "
         "method escapes the exponential. The only question is where you can afford to pay it. "
         "Eight honey pots means 256 subsets: nothing. Thirty honey pots means over a billion: "
         "impossible.",
         "B11_Wall",
         "A 2-to-the-K curve climbs gently then explodes off the top of the frame; markers land "
         "at K=8 ('256, nothing') and K=30 ('over a billion, impossible').",
         [{"at": 0.2, "event": "curve climbs gently"},
          {"at": 0.5, "event": "curve explodes upward; K=8 marker lands"},
          {"at": 0.8, "event": "K=30 marker lands off the top"}]),
    beat("B12", "act v · which one, when",
         "Muse's rule of thumb. Few honey pots: use the bitmask DP — exact and clean. Want the "
         "obviously correct code: the state-space BFS. Dozens of honey pots: admit that exactness "
         "is unaffordable, and go greedy — or approximate. The number of targets decides. Not "
         "your cleverness.",
         "B12_Rule",
         "A three-branch decision card grows: 'few targets -> bitmask DP', 'want obvious "
         "correctness -> state BFS', 'many targets -> greedy / approximate'; the K dial turns.",
         [{"at": 0.2, "event": "decision card grows; first branch lands"},
          {"at": 0.5, "event": "second and third branches land"},
          {"at": 0.8, "event": "K dial turns; 'targets decide' tag lands"}]),
    # ── ACT VI: grading the grader ─────────────────────────────────────
    beat("B13", "act vi · grading the grader",
         "Then Muse did the second half of its instructions: it checked the assignment itself. "
         "Remember the six? Six is the shortest tour that never comes home. The assignment's own "
         "rules demand the return trip — and with it, the answer is twelve. The example was "
         "worked without the walk home.",
         "B13_SixVsTwelve",
         "Split stage: the six-step tour draws left, stopping at the last honey, tagged 'never "
         "comes home'; the twelve-step tour draws right, returning to B, tagged 'the real answer'.",
         [{"at": 0.2, "event": "six-step tour draws left, stops at last honey"},
          {"at": 0.5, "event": "'never comes home' tag lands"},
          {"at": 0.7, "event": "twelve-step tour draws right, returns to B; 'the real answer'"}]),
    beat("B14", "act vi · grading the grader",
         "Three more findings. The assignment says a valid path always exists, and also says "
         "return minus one if impossible — both cannot be true at once. It never rules out "
         "diagonal moves. And it says 'at least one' start cell, leaving two starts undefined. "
         "All four now fixed, in a corrected notebook.",
         "B14_Fixes",
         "A four-item checklist card: 'example answer 6 -> 12', 'minus-one contradiction resolved', "
         "'no diagonals stated', 'exactly one start'; terracotta checks land one by one.",
         [{"at": 0.2, "event": "checklist card grows"},
          {"at": 0.4, "event": "first two checks land"},
          {"at": 0.65, "event": "last two checks land"},
          {"at": 0.85, "event": "'corrected notebook' tag lands"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


BIDEA_NARR = (
    "Hallo. This is Liam, in for Bear. I handed Muse a real homework assignment from an "
    "algorithms course — INFO 6205 — and told it: do your best work, and check the assignment "
    "itself for errors. So the question isn't: can an AI solve a pathfinding puzzle. "
    "The question is: what happens when Muse does the whole assignment — and then grades the grader."
)
BDEFS_NARR = (
    "Five terms, plainly. BFS: a search that spreads outward one step at a time, so the first "
    "time it reaches a cell, that is the shortest path. Shortest path: the fewest steps between "
    "two cells, dodging obstacles. Heuristic: a fast rule of thumb, not guaranteed perfect. "
    "Bitmask DP: an exact method that tries every subset of targets, tracking visited ones as bits. "
    "And NP-hard: problems with no known fast exact solution — the work grows exponentially."
)

OPEN = [
    remotion("BIDEA", "the question", BIDEA_NARR,
             "BrutalistHesitantWriter",
             {"text": "Can an AI\nsolve a pathfinding puzzle?", "triggerWords": "can an AI solve a pathfinding puzzle",
              "replacementWords": "what happens when Muse does the whole assignment",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2,
              "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'Can an AI'"},
              {"at": 0.6, "event": "backspaces 'can an AI solve a pathfinding puzzle' -> 'what happens when Muse does the whole assignment' on the spoken correction"}],
             lead_silence_s=0.8,
             motion_claim="The writer types the naive question and corrects it to the real one: Muse doing the whole assignment.",
             qc={"sparse_by_design": True,
                 "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms", BDEFS_NARR,
             "ClaudeDefinitions",
             {"title": "Terms In This Lecture",
              "terms": [{"term": "BFS",
                         "meaning": "search spreading outward one step at a time; first arrival is the shortest path"},
                        {"term": "shortest path",
                         "meaning": "the fewest steps between two cells, dodging obstacles"},
                        {"term": "heuristic",
                         "meaning": "a fast rule of thumb, not guaranteed perfect"},
                        {"term": "bitmask DP",
                         "meaning": "exact method trying every subset of targets, visited ones tracked as bits"},
                        {"term": "NP-hard",
                         "meaning": "no known fast exact solution; the work grows exponentially"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'BFS' lands"},
              {"at": 0.32, "event": "'shortest path' lands"},
              {"at": 0.52, "event": "'heuristic' lands"},
              {"at": 0.68, "event": "'bitmask DP' lands"},
              {"at": 0.84, "event": "'NP-hard' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True,
                 "sparse_reason": "TERMS card: five prerequisites, one line each."}),
]

YT_PROMPT = (
    "Here is a four-by-four grid. Row one: B, dot, dot, dot. "
    "Row two: dot, H, dot, dot. Row three: H, dot, dot, dot. Row four: dot, H, dot, dot. "
    "Solve it three ways: bitmask DP, state-space BFS, and greedy nearest-honey. "
    "Report each method's step count, say which are optimal, and point to the exact greedy move that costs extra."
)
YT_NARRATION = ("Your turn. Paste this into the AI: " + YT_PROMPT +
                " Then check two things yourself. Did it report all three step counts, with the "
                "two exact methods agreeing? And can you name the greedy move that costs extra? "
                "If yes twice, you have understood the assignment better than its example did.")
YOURTURN = remotion("BHTF", "your turn", YT_NARRATION,
                    "ClaudeComposerAsk",
                    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN",
                     "segment": "Muse Does the Assignment", "command": YT_PROMPT,
                     "runningText": "paste this into the AI…",
                     "output": ["Check: all three step counts are reported, and the two exact methods agree.",
                                "Check: you can name the greedy move that costs extra."],
                     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
                    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
                     {"at": 0.1, "event": "the prompt types in full"},
                     {"at": 0.8, "event": "two check lines land"}])

BVDT_LINES = [
    "Beary's errand is a traveling-salesperson tour on a grid: collect everything, come home, fewest steps.",
    "Bitmask DP earns the exact answer by separating shortest legs from cheapest order.",
    "State-space BFS earns the same answer with one obviously correct search.",
    "Greedy nearest-first is fast and sometimes wrong: ten steps where eight exist.",
    "The number of honey pots picks the method, because the subsets double every time.",
    "And the assignment itself needed grading: its example answer forgot the walk home.",
]
BVDT = remotion("BVDT", "recap",
                "Let's recap with Claude. " + " ".join(BVDT_LINES),
                "ClaudeVerdictArtifact",
                {"lines": BVDT_LINES, "folderLabel": "@NikBearBrown"},
                [{"at": 0.1 + 0.14 * i, "event": f"line {i+1} lands"} for i in range(6)],
                gate="CARD",
                qc={"sparse_by_design": True,
                    "sparse_reason": "Verdict card: six recap lines, one per act."})

SPARSE_REASON = ("lecture style: Manim carries each mechanism beat on the cream stage; "
                 "the negative space is the style, so only underfill and clustered are waived; "
                 "edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

ALL = OPEN + B + [BVDT, YOURTURN]
ALL.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
            "narration_text": f"{TITLE}. Liam, in for Bear. At Nik Bear Brown.",
            "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "REMOTION", "source": "own",
                     "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                     "remotion": {"pattern": "ClaudeTitleOutro",
                                  "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
            "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 6205 · ALGORITHMS · LECTURE", "skill": "lecture",
    "style_preset": "lecture", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "course": COURSE,
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9",
    "width": 3840, "height": 2160, "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "audience": "INFO 6205 students and smart general viewers; every term explained in-line",
    "source_doc": ("Week 1 INFO 6205 assignment 'Help Beary Navigate the Forest to Collect Honey' "
                   "(uploaded notebook) + Muse's reference solution (3 approaches, 25 tests) + "
                   "independent assignment audit; see SOURCES.md and FACTCHECK.md"),
    "series_note": "Standalone lecture film for INFO 6205; companion work lives in the "
                   "'Coursera Info 6205 Algorithms' folder of the same repo",
    "playlist": "INFO 6205 Algorithms",
    "tags": ["algorithms", "pathfinding", "BFS", "dynamic programming", "traveling salesperson",
             "INFO 6205", "Nik Bear Brown"]},
    "beats": ALL}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

# ── assertions: the sheet must be render-ready ─────────────────────────────
n_body = sum(1 for b in ALL if b["lane"] == "manim")
n_book = sum(1 for b in ALL if b["lane"] == "bookend")
total = sum(b["estimated_duration_s"] for b in ALL)
assert len(ALL) == 19, f"expected 19 beats, got {len(ALL)}"
assert n_body == 14, f"expected 14 manim body beats, got {n_body}"
assert n_book == 5, f"expected 5 bookends, got {n_book}"
assert ALL[0]["beat_id"] == "BIDEA" and ALL[-1]["beat_id"] == "BOUT"
assert ALL[-2]["beat_id"] == "BHTF" and ALL[-3]["beat_id"] == "BVDT"
assert YT_PROMPT in YT_NARRATION, "BHTF must read the prompt in full"
assert YOURTURN["shot"]["remotion"]["props"]["command"] == YT_PROMPT
print(f"sheet ok: 19 beats, 14 manim, ~{total:.0f}s estimated")
