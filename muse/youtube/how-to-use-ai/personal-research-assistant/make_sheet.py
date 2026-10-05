#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Your personal research assistant".

SHOW-TELL (Bear, 2026-09-26): one drawn image per beat, minimal labels,
Liam's voice (Kokoro am_onyx) explains. Deep-research features for a
general audience: how to brief the AI well (decision, scope, demanded
shape), how to read its report (layers, spot-check two), and what to
distrust (hollow citations, the echo loop, stale dates, thin sources).
Companion to Film 21 "Trust, but verify".

Source: NEW — built from scratch, no mirror source. Product facts
search-grounded 2026-10-04 (see SOURCES.md); all advice original.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "personal-research-assistant"
TITLE = "Your personal research assistant"

WPS = 2.5  # estimated words per second for Kokoro am_onyx (pre-audio estimate)


def beat(bid, narration, cls, image, show):
    return {
        "beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
        "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / WPS, 1),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                 "manim": {"class": cls}, "motion_claim": image},
    }


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {
        "beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
        "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / WPS, 1),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "REMOTION", "source": "own", "show": show,
                 "remotion": {"pattern": pattern, "props": props}},
    }
    b.update(extra)
    return b


OPEN = [
    remotion(
        "BIDEA", "the question",
        "Hallo. This is Liam, in for Bear. You want the AI to do your "
        "research. So the question isn't whether it can. It's how you "
        "brief it.",
        "BrutalistHesitantWriter",
        {"text": "Can you do all my research\nfor my report?",
         "triggerWords": "do all my research",
         "replacementWords": "brief my research assistant",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
         "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Can you do all my research for my report?'"},
         {"at": 0.6, "event": "backspaces 'do all my research' → 'brief my research assistant' on the spoken correction"}],
        lead_silence_s=0.8,
        motion_claim="The writer types the naive ask and corrects it to the real one: brief my research assistant.",
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion(
        "BDEFS", "terms",
        "Four terms. Deep research: the AI's long mode — it reads many "
        "sources and reports back with citations. A brief: what you tell "
        "it first — your goal, your scope, your sources. A citation: the "
        "link from a claim to its source. A primary source: where the "
        "fact comes from first-hand.",
        "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [{"term": "deep research", "meaning": "the AI's long mode: it reads many sources and reports back"},
                   {"term": "brief", "meaning": "what you tell it first: goal, scope, sources"},
                   {"term": "citation", "meaning": "the link from a claim to its source"},
                   {"term": "primary source", "meaning": "where the fact comes from first-hand"}],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'deep research' lands"},
         {"at": 0.35, "event": "'brief' lands"},
         {"at": 0.55, "event": "'citation' lands"},
         {"at": 0.78, "event": "'primary source' lands"}],
        gate="CARD",
        qc={"sparse_by_design": True,
            "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

B = [
    beat(
        "B00",
        "This is deep research. You hand it a brief, and it goes reading "
        "— not one page, dozens — then brings back a report where each "
        "claim points to a source. A research assistant that never "
        "sleeps. But it's only as good as its instructions.",
        "B00_HeroDesk",
        "The research desk (open iso box): a brief chip drops in; iso source pages fan out around it; a report page grows with terracotta citation dots; the label 'deep research' lands beside.",
        [{"at": 0.1, "event": "the desk + brief chip drops in"},
         {"at": 0.35, "event": "source pages fan out"},
         {"at": 0.65, "event": "report page grows, citation dots land"},
         {"at": 0.85, "event": "label lands"}]),
    beat(
        "B01",
        "The brief starts with the decision, not the topic. 'Research "
        "electric bikes' gets you a wall of facts. 'I'm choosing a bike "
        "for a hilly commute' gets you an answer. Tell it what you're "
        "deciding, and the research has an aim.",
        "B01_TheDecision",
        "The brief box: a card 'your decision' drops in; a dimmed 'the topic' card slides away; a terracotta check stamps the decision card.",
        [{"at": 0.1, "event": "brief box + dimmed 'the topic' card"},
         {"at": 0.4, "event": "'your decision' card drops in"},
         {"at": 0.7, "event": "check stamps the decision card"}]),
    beat(
        "B02",
        "Then the scope: what counts, and what doesn't. Tell it where to "
        "look — university pages, official statistics — and what to "
        "skip, like opinion blogs. And set a date window. Research from "
        "last year answers a different question than research from 2019.",
        "B02_TheScope",
        "Source pages split into two piles: 'in scope' (ink checks) vs 'out of scope' (dimmed, struck); a date plate 'last 5 years' lands.",
        [{"at": 0.1, "event": "source pages on stage"},
         {"at": 0.35, "event": "pages split into two piles"},
         {"at": 0.65, "event": "checks land; out-of-scope pile dims"},
         {"at": 0.85, "event": "date plate lands"}]),
    beat(
        "B03",
        "Now tell it the shape of the answer. A citation for every claim "
        "— not a list at the end, a link on the line. And add one "
        "instruction: flag anything you could not verify. An honest 'I "
        "couldn't confirm this' beats a confident guess.",
        "B03_DemandProof",
        "The report page grows claim lines; a terracotta dot lands on each line (a citation); one line gets a '?' flag plate: 'couldn't verify'.",
        [{"at": 0.1, "event": "report page grows"},
         {"at": 0.4, "event": "citation dots land per line"},
         {"at": 0.75, "event": "'?' flag plate lands"}]),
    beat(
        "B04",
        "When the report lands, read it in layers. The summary first — "
        "that's the headline. Then the claims. Then the part most people "
        "skip: the source list. Where did it actually look? A report is "
        "only as strong as the ground it stands on.",
        "B04_ThreeLayers",
        "The report fans into three layers — 'summary', 'claims', 'sources'; the cursor taps 'sources' and it highlights; the label 'read sources first' lands.",
        [{"at": 0.1, "event": "report on stage"},
         {"at": 0.35, "event": "report fans into three layers"},
         {"at": 0.65, "event": "cursor taps 'sources'; it highlights"},
         {"at": 0.85, "event": "label lands"}]),
    beat(
        "B05",
        "Then spot-check two citations. Open them yourself. Does the "
        "source really say what the report claims? When one doesn't, "
        "you've found the weak beam. The companion film, Trust, but "
        "verify, teaches the full checking habit.",
        "B05_SpotCheck",
        "The report with citation dots; the cursor opens citation 1 → a source page lands with an ink check; opens citation 2 → a grey dead page with a terracotta X; the label 'spot-check two' lands.",
        [{"at": 0.1, "event": "report with citations"},
         {"at": 0.35, "event": "cursor opens citation 1 → check"},
         {"at": 0.65, "event": "cursor opens citation 2 → dead page, X"},
         {"at": 0.85, "event": "label lands"}]),
    beat(
        "B06",
        "Distrust the shiny report with hollow citations. It reads "
        "beautifully, the footnotes are everywhere — but open them and "
        "there's nothing behind them. Confidence is not evidence. If "
        "the citations don't hold, the report doesn't either.",
        "B06_HollowCitations",
        "A polished report: footnotes everywhere; the terracotta dots turn hollow one by one; the cursor opens one → an empty page; a terracotta X; the label 'hollow' lands.",
        [{"at": 0.1, "event": "shiny report with dots"},
         {"at": 0.4, "event": "dots turn hollow"},
         {"at": 0.65, "event": "cursor opens one → empty page"},
         {"at": 0.85, "event": "X + label land"}]),
    beat(
        "B07",
        "Distrust the echo. Sometimes a citation leads to another AI "
        "answer, which cites another AI answer back. A loop of machines "
        "agreeing with each other. Follow the chain until you reach a "
        "human source — a study, an official page, a named expert.",
        "B07_TheEcho",
        "Two report pages; curved arrows circle between them (the citation loop); the chain walks to a third, human-made page with an ink check; the label 'the echo' lands.",
        [{"at": 0.1, "event": "two report pages"},
         {"at": 0.4, "event": "arrows circle between them"},
         {"at": 0.65, "event": "the chain walks to a human-made page → check"},
         {"at": 0.85, "event": "label lands"}]),
    beat(
        "B08",
        "And check the dates. A 2019 source is fine for history and "
        "useless for rules, prices, or anything that changed since. If "
        "the citations are all old, or everything leans on one source, "
        "the research is thin — however long the report is.",
        "B08_CheckDates",
        "Date plates: '2026' (ink) vs '2019' (greyed); the old pages dim; a single source page under a tall report — a thin base; the label 'check the dates' lands.",
        [{"at": 0.1, "event": "report + source pages"},
         {"at": 0.35, "event": "date plates land; old pages dim"},
         {"at": 0.65, "event": "the report balances on one source"},
         {"at": 0.85, "event": "label lands"}]),
    beat(
        "B09",
        "Last rule: the report is a map, not the answer. A good map "
        "saves you days of walking. But you still walk the ground "
        "yourself. You are the editor; the AI is the assistant. The "
        "decision stays yours.",
        "B09_TheMap",
        "The report sits in the brief box as a map card; a pen cursor strikes one line; a plate 'you decide' lands; the label 'a map, not the answer' lands.",
        [{"at": 0.1, "event": "report as a map card"},
         {"at": 0.4, "event": "pen cursor edits one line"},
         {"at": 0.7, "event": "'you decide' plate lands"},
         {"at": 0.85, "event": "label lands"}]),
]

YT_PROMPT = (
    "I want you to research this question: [my question in one line]. "
    "This research will help me decide: [the decision]. "
    "Scope: focus on [where to look, and which dates]; ignore [what is out of scope]. "
    "Give me a report with a citation for every claim, and flag anything you could not verify. "
    "Wait for my questions before you finish."
)
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT +
    " Then check two things yourself. Open two of its citations — do they "
    "really say what the report claims? And does the report flag anything "
    "it couldn't verify, or is it confident about everything?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN",
     "segment": "Brief Your Researcher", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: open two citations — do they really say what the report claims?",
                "Check: did it flag anything it couldn't verify, or is it confident about everything?"],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = (
    "show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream "
    "stage per beat, minimal labels, with the voice carrying the explanation. "
    "The negative space is the style, so only underfill and clustered are "
    "waived; edge-bleed, empty-frame and contrast still apply."
)
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({
    "beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
    "narration_text": f"{TITLE}. At Nik Bear Brown.",
    "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
    "shot": {"type": "REMOTION", "source": "own",
             "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
             "remotion": {"pattern": "ClaudeTitleOutro",
                         "props": {"title": TITLE, "slug": SLUG,
                                   "handle": "@NikBearBrown", "subline": ""}}},
    "kind": "outro_voice", "tail_silence_s": 1.0,
})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "AI · DEEP RESEARCH",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": (
        "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + "
        "terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat "
        "and key terms like tldr uses as the second'), no verdict card; Your "
        "Turn is the Claude.ai composer; spoken outro stays."),
    "audience": "smart, pragmatic general audience — not AI experts; a viewer who has typed one-line questions into an AI chat tool",
    "source_doc": "NEW — built from scratch for the How-to-AI series (2026-10-04). No mirror source. Product facts search-grounded 2026-10-04; all advice original.",
    "playlist": "How to AI", "chapter_number": 25,
    "tags": ["Claude", "deep research", "research", "citations", "AI tips", "Nik Bear Brown"]},
    "beats": B}

# ── asserts (the film's contract) ────────────────────────────────────────────
ids = [b["beat_id"] for b in B]
assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04",
               "B05", "B06", "B07", "B08", "B09", "BHTF", "BOUT"], f"beat order wrong: {ids}"
total = sum(b["estimated_duration_s"] for b in B)
assert 200 <= total <= 280, f"total {total}s outside 200–280 s band"

for b in B:
    bid = b["beat_id"]
    if bid not in ("BIDEA", "BDEFS", "BHTF", "BOUT"):
        assert b["lane"] == "manim", bid
        cls = b["shot"]["manim"]["class"]
        assert cls == f"{bid}_{cls.split('_', 1)[1]}" and cls.startswith(bid + "_"), bid
        assert b["shot"]["manim"]["class"][0] == "B", bid

# BIDEA: hesitant-writer trigger mechanics (skill: trigger must appear verbatim
# in text; neither may end in punctuation — the component strips it).
hw = B[0]["shot"]["remotion"]["props"]
tw, rw = hw["triggerWords"], hw["replacementWords"]
assert tw in hw["text"], "triggerWords not verbatim in text"
assert not tw[-1] in ".?!,;:" and not rw[-1] in ".?!,;:", "trailing punctuation kills the trigger"
assert B[0].get("lead_silence_s") == 0.8, "BIDEA lead silence"

# BDEFS: ClaudeDefinitions truncates terms longer than ~17 chars — keep short.
for t in B[1]["shot"]["remotion"]["props"]["terms"]:
    assert len(t["term"]) <= 17, f"term too long: {t['term']}"

# BHTF: composer contract — the prompt is read in full, two self-checks.
yt = B[-2]["shot"]["remotion"]["props"]
assert "YOUR TURN" in yt["topic"], "BHTF topic must contain YOUR TURN"
assert yt["greeting"] == "Your turn.", "BHTF greeting"
assert len(yt["output"]) == 2, "BHTF needs two check lines"
assert YT_PROMPT in B[-2]["narration_text"], "BHTF prompt must be read in full"

# BOUT: spoken outro, never exempt.
bo = B[-1]
assert bo["kind"] == "outro_voice" and bo["tail_silence_s"] == 1.0, "BOUT tail"
assert bo["narration_text"].endswith("At Nik Bear Brown."), "BOUT outro line"

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(total, 1), "s (~%d:%02d)" % (int(total // 60), int(total % 60)))
