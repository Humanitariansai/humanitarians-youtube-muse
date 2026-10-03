#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Muse builds the opportunity matcher".

LECTURE, channel claude-liam (Liam, in for Bear · Kokoro am_onyx · @NikBearBrown).
Assignment 4, Part 1 film: the opportunity-matcher build story — design,
two implementations, new coverage, what went wrong, results, error handling,
and the honest evaluation of Muse doing the work.
Source: assignment-4/FRICTIONAL.md and the files it cites.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "claude-liam-lecture-a4-part1-opportunity-matcher"
TITLE = "Muse builds the opportunity matcher"


def beat(bid, act, narration, cls, image, show, claim=None):
    return {
        "beat_id": bid, "act": act, "lane": "manim", "proof_gate": "SHOW",
        "narration_text": narration,
        "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "GRAPHIC", "source": "own",
            "visual_intent": image, "show": show,
            "manim": {"class": cls},
            "motion_claim": claim or image,
        },
        "qc": {
            "sparse_by_design": True,
            "sparse_reason": "lecture style: one drawn scene on a cream stage per beat, minimal labels, voice carries the explanation.",
        },
    }


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {
        "beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
        "narration_text": narration,
        "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "REMOTION", "source": "own", "show": show,
                 "remotion": {"pattern": pattern, "props": props}},
    }
    b.update(extra)
    return b


B = [
    # ── ACT I — the problem ───────────────────────────────────────────────
    beat("B01", "the problem",
         "Assignment 3 collected: three thousand four hundred forty-six postings across eighteen boards. Ninety-seven kept. But collecting isn't judging — of those ninety-seven, which ones actually matter?",
         "M01_WhichMatter",
         "A big pile of posting marks shrinks to 97; a question mark rises over them.",
         [{"at": 0.15, "event": "pile shrinks to 97"},
          {"at": 0.55, "event": "question mark rises"}],
         claim="The shrinking pile is the funnel; the '?' is the unanswered question."),
    beat("B02", "the problem",
         "Assignment 4, Part 1 demands real intelligence. Not more storage — decisions. The machine must go from 'here are the postings' to 'here is what to do about them.' Collect, then judge.",
         "M02_CollectJudge",
         "A box labeled 'collect' hands a posting to a box labeled 'judge'; a verdict stamp lands.",
         [{"at": 0.15, "event": "handoff from collect to judge"},
          {"at": 0.6, "event": "verdict stamp lands"}],
         claim="The handoff plus the stamp is the assignment's demand in motion."),
    # ── ACT II — the design ───────────────────────────────────────────────
    beat("B03", "the design",
         "The design: five dimensions, one fit score. The title's role words count most — thirty percent. A named audience and a materials signal, twenty each. Whether it rewards a gap in the CV, fifteen. And the company's education demand, fifteen. The weights are judgment — labeled in the code, not hidden.",
         "M03_FiveDimensions",
         "Five bars labeled with weights 0.30/0.20/0.20/0.15/0.15 merge into one number.",
         [{"at": 0.15, "event": "five weighted bars"},
          {"at": 0.55, "event": "bars merge into one number"}],
         claim="Bars merging into one number IS the fit score."),
    beat("B04", "the design",
         "And routing, not just scoring. Zero point six five or higher: PURSUE — draft the application. Zero point four five: NETWORK — find the human first. Zero point two five: WATCH. Below that: SKIP. Decisions a person can act on.",
         "M04_Routing",
         "A vertical gauge; lines draw at 0.65, 0.45, 0.25; zones label PURSUE, NETWORK, WATCH, SKIP.",
         [{"at": 0.15, "event": "gauge"},
          {"at": 0.4, "event": "threshold lines draw"},
          {"at": 0.7, "event": "zones label"}],
         claim="The gauge with zones is the decision, not just the number."),
    beat("B05", "the design",
         "Every score carries its evidence. The rationale quotes what fired: 'title matches developer education,' 'rewards CV gap: certification.' A number you can't audit is a rumor.",
         "M05_Rationale",
         "A score card; evidence lines type in beneath it, each quoted.",
         [{"at": 0.15, "event": "score card"},
          {"at": 0.45, "event": "evidence lines type in"}],
         claim="The typing evidence lines are the 'why'."),
    # ── ACT III — two implementations, new coverage ───────────────────────
    beat("B06", "two implementations, new coverage",
         "Implementation one: matcher.py. Plain Python, runs anywhere. Seven hundred fourteen postings scored in three point one seconds.",
         "M06_MatcherPy",
         "A script mark; posting marks fly through it; a stopwatch spins to 3.1s.",
         [{"at": 0.15, "event": "postings fly through the script"},
          {"at": 0.55, "event": "stopwatch spins to 3.1s"}],
         claim="Speed in motion; the stopwatch is the scale claim."),
    beat("B07", "two implementations, new coverage",
         "Implementation two: the n8n equivalent. Schedule, fetch the boards, normalize, score, route, write the briefs, email the digest. Same weights, same thresholds, same decisions — eleven nodes, validated. Two implementations, one spec.",
         "M07_N8n",
         "Node boxes link left to right: schedule, fetch, normalize, score, route, briefs, email.",
         [{"at": 0.15, "event": "nodes appear"},
          {"at": 0.45, "event": "links draw left to right"}],
         claim="The linked chain is the workflow."),
    beat("B08", "two implementations, new coverage",
         "New coverage: Anthropic's board is live. Six hundred forty postings pulled today. The equivalents are real — Developer Education Lead for the Claude Platform, fit zero point nine one. The direct equivalent of the Figma target.",
         "M08_AnthropicLive",
         "A board fills with posting marks; one rises to the top labeled 0.91.",
         [{"at": 0.15, "event": "board fills"},
          {"at": 0.55, "event": "one posting rises, labeled 0.91"}],
         claim="The rising posting is the equivalent found."),
    beat("B09", "two implementations, new coverage",
         "Meta's board is unreadable — a JavaScript shell on private GraphQL, no public feed. Recorded honestly, the way Google was. And a hand search found no 'Muse for education' role. Absence is a measurement gap, not evidence of no demand.",
         "M09_MetaUnreadable",
         "A browser window; the page renders as an empty shell; a 'no feed' mark.",
         [{"at": 0.2, "event": "browser window"},
          {"at": 0.5, "event": "empty shell, no-feed mark"}],
         claim="The empty shell is the honest finding."),
    # ── ACT IV — what went wrong ──────────────────────────────────────────
    beat("B10", "what went wrong",
         "What went wrong, first: the first run put six hundred thirty-three of seven hundred fourteen postings in WATCH. Noise — generic business words like 'partner' and 'customer' counted as audience.",
         "M10_WatchFlood",
         "Postings pour into four buckets; the WATCH bucket overflows.",
         [{"at": 0.15, "event": "postings pour"},
          {"at": 0.5, "event": "WATCH bucket overflows"}],
         claim="The overflowing bucket is the failure, shown."),
    beat("B11", "what went wrong",
         "The fix: the pairing rule. Discounted title words — training, enablement, education — only count when the text confirms them with a named audience or a materials phrase. It operationalizes Bear's own reversal: training your own people counts; pure process doesn't.",
         "M11_PairingRule",
         "A weak word mark ('training') alone fades; paired with an audience mark it lights up.",
         [{"at": 0.2, "event": "weak word alone fades"},
          {"at": 0.55, "event": "paired, it lights up"}],
         claim="Fading versus lighting IS the rule."),
    beat("B12", "what went wrong",
         "Then the bullseye failed. The Claude Docs role — the perfect materials-maker job — scored zero point four six. The materials vocabulary had no phrase for 'own the documentation.' Measured across seven hundred thirty-seven postings: two hits, both right. Added. Now zero point six six — PURSUE. And 'documentation for' measured eight hits, mostly boilerplate — rejected.",
         "M12_Bullseye",
         "A gauge needle sits at 0.46; the phrase 'own the documentation' drops in; the needle swings to 0.66, past the PURSUE line.",
         [{"at": 0.15, "event": "needle at 0.46"},
          {"at": 0.45, "event": "phrase drops in"},
          {"at": 0.7, "event": "needle swings past PURSUE"}],
         claim="The swinging needle is the fix, measured."),
    # ── ACT V — results, and when things break ────────────────────────────
    beat("B13", "results, and when things break",
         "Final: twenty-two PURSUE, thirty-seven NETWORK, three hundred twenty-five WATCH, three hundred thirty SKIP. Zero quarantined. Top of the list: the Anthropic education lead, Figma's Designer Advocate for Partnerships, Webflow's Senior Developer Educator.",
         "M13_Final",
         "Four buckets fill to proportion: 22, 37, 325, 330.",
         [{"at": 0.15, "event": "buckets fill to proportion"}],
         claim="Proportions shown honestly — most of the board is not actionable."),
    beat("B14", "results, and when things break",
         "And outputs a human can open: the digest as markdown and HTML, fifteen per-role briefs, the run report with timings. Not JSON — files.",
         "M14_Outputs",
         "Files land in a row: digest.md, digest.html, fifteen briefs, run report.",
         [{"at": 0.2, "event": "files land one by one"}],
         claim="The landing files are the deliverable."),
    beat("B15", "results, and when things break",
         "When things break: fetches retry with backoff, then fall back to cached data — the digest still ships, flagged. Malformed records go to quarantine, counted and named. The run never dies silently.",
         "M15_Errors",
         "A fetch fails (X mark), retries loop, then falls back to a cached file; a malformed record drops into quarantine.",
         [{"at": 0.15, "event": "fetch fails, retries loop"},
          {"at": 0.5, "event": "fallback to cached"},
          {"at": 0.75, "event": "bad record quarantined"}],
         claim="The loop and the fallback are the promise."),
    # ── ACT VI — the evaluation ───────────────────────────────────────────
    beat("B16", "the evaluation",
         "Now the evaluation. This film is also a test of Muse doing agentic work: it wrote the scripts, pulled the boards, ran the analysis, tuned from measured evidence, and pushed everything to the repo where Bear can see it.",
         "M16_Evaluation",
         "A checklist ticks: wrote scripts, ran analysis, tuned from evidence, pushed to repo.",
         [{"at": 0.15, "event": "checklist ticks through"}],
         claim="The ticking checklist is the evaluation so far."),
    beat("B17", "the evaluation",
         "What failed: my own push script had a scoping bug. Twenty-five files failed; zero went up. Fixed it, re-ran, all twenty-five landed. Logged, not hidden. That is the standard being demonstrated.",
         "M17_PushBug",
         "Twenty-five file marks try to rise to a cloud; all fall back; a wrench turns; all twenty-five rise.",
         [{"at": 0.15, "event": "files fall back"},
          {"at": 0.5, "event": "wrench turns"},
          {"at": 0.7, "event": "all twenty-five rise"}],
         claim="Falling then rising is the honest failure and fix."),
]

OPEN = [
    remotion(
        "BIDEA", "the question",
        "Hallo. This is Liam, in for Bear. Assignment 3 built a machine that collects jobs — a job scraper. Assignment 4 asked it to judge them — a job judge. This is the film of that build. And it's also, on purpose, an evaluation of Muse doing this kind of work.",
        "BrutalistHesitantWriter",
        {"text": "I built\na job scraper",
         "triggerWords": "a job scraper",
         "replacementWords": "a job judge",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6,
         "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
         "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'I built'"},
         {"at": 0.5, "event": "backspaces 'a job scraper' → 'a job judge' on the spoken correction"}],
        lead_silence_s=0.8,
        motion_claim="The writer types the collector framing and corrects it to the judge framing.",
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."},
    ),
    remotion(
        "BDEFS", "terms",
        "Five terms. Matcher: the program that scores postings. Fit score: one number from five dimensions. PURSUE: the top routing decision — draft the application. Pairing rule: weak title words need confirmation. Quarantine: where malformed records go, never crashing the run.",
        "ClaudeDefinitions",
        {"title": "Terms In This Lecture",
         "terms": [
             {"term": "matcher", "meaning": "the program that scores postings"},
             {"term": "fit score", "meaning": "one number from five dimensions"},
             {"term": "PURSUE", "meaning": "the top routing decision"},
             {"term": "pairing rule", "meaning": "weak words need confirmation"},
             {"term": "quarantine", "meaning": "where malformed records go"},
         ],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'matcher' lands"},
         {"at": 0.32, "event": "'fit score' lands"},
         {"at": 0.52, "event": "'PURSUE' lands"},
         {"at": 0.68, "event": "'pairing rule' lands"},
         {"at": 0.84, "event": "'quarantine' lands"}],
        gate="CARD",
        qc={"sparse_by_design": True,
            "sparse_reason": "TERMS card: five prerequisites, one line each."},
    ),
]

B = OPEN + B + [
    remotion(
        "BVDT", "recap",
        "Let's recap. "
        "Assignment 3 collected 3,446 postings; Part 1 judges them — five dimensions, one fit score, four decisions. "
        "Two implementations, one spec: matcher.py and the n8n workflow. "
        "Anthropic's board is live with real equivalents; Meta's is unreadable, honestly recorded. "
        "What went wrong got measured and fixed: the pairing rule, the bullseye at 0.66. "
        "Twenty-two PURSUE, zero quarantined — everything pushed to GitHub, failures included.",
        "ClaudeVerdictArtifact",
        {"artifactTitle": "The Opportunity Matcher",
         "artifactHeading": "Recap",
         "brandLabel": "@NikBearBrown",
         "artifactLines": [
             "3,446 postings collected; Part 1 judges them — five dimensions, one score.",
             "Routing, not just scoring: PURSUE, NETWORK, WATCH, SKIP.",
             "Two implementations, one spec: matcher.py and the n8n workflow.",
             "Anthropic live with real equivalents; Meta unreadable, honestly recorded.",
             "Measured fixes: the pairing rule, the bullseye at 0.66.",
             "22 PURSUE, 0 quarantined — everything on GitHub, failures included.",
         ]},
        [{"at": 0.1, "event": "line 1 lands"},
         {"at": 0.28, "event": "line 2 lands"},
         {"at": 0.46, "event": "line 3 lands"},
         {"at": 0.62, "event": "line 4 lands"},
         {"at": 0.78, "event": "line 5 lands"},
         {"at": 0.9, "event": "line 6 lands"}],
    ),
    remotion(
        "BHTF", "your turn",
        "Your turn. Pick one kept posting and score it by hand on the five dimensions — role, audience, materials, gap, company. Then compare with the machine's routing. Check two things yourself. Is your score within zero point one of the machine's? And can you name the single signal that decided it?",
        "ClaudeComposerAsk",
        {"greeting": "Your turn.", "topic": "MATCHER · YOUR TURN",
         "segment": "Score One By Hand", "command": "Pick a kept posting; score role/audience/materials/gap/company",
         "runningText": "scoring by hand…",
         "output": ["Check: your score is within 0.1 of the machine's.",
                    "Check: you can name the deciding signal."],
         "folderLabel": "@NikBearBrown", "modelLabel": "Muse Spark", "effortLabel": "Low"},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.8, "event": "two check lines land"}],
    ),
    {
        "beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
        "narration_text": f"{TITLE}. At Nik Bear Brown.",
        "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "REMOTION", "source": "own",
            "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
            "remotion": {
                "pattern": "ClaudeTitleOutro",
                "props": {"title": TITLE, "slug": SLUG,
                          "handle": "@NikBearBrown", "subline": ""},
            },
        },
        "kind": "outro_voice", "tail_silence_s": 1.0,
    },
]

sheet = {
    "metadata": {
        "slug": SLUG, "title": TITLE, "topic": "A4 · PART 1",
        "skill": "lecture", "style_preset": "lecture",
        "channel": "claude-liam", "persona": "Liam (in for Bear)",
        "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
        "clock": "narration", "palette": "claude", "register": "Teardown",
        "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
        "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
        "audience": "anyone evaluating the Assignment 4 Part 1 build — and Muse doing it",
        "source_doc": "assignment-4/FRICTIONAL.md and the files it cites",
        "playlist": "INFO 7375", "chapter_number": 0,
        "tags": ["INFO 7375", "opportunity matcher", "n8n", "Muse", "Nik Bear Brown"],
    },
    "beats": B,
}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b["estimated_duration_s"] for b in B)), "s")
