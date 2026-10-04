#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Make It Interview You First".

SHOW-TELL (Bear, 2026-09-26): one drawn image per beat, minimal labels, Liam's
voice (Kokoro am_onyx) explains. Before giving the AI a task, tell it
"ask me 5 questions first": a trip-planning demo (plus a difficult-email
second demo) shows the interview surfacing the missing context, and the
tailored answer that comes back.

Source: NEW — built from scratch, no mirror source. The five interview
questions and the trip answers are an original worked example (see SOURCES.md).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "make-it-interview-you-first"
TITLE = "Make It Interview You First"

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
        "Hallo. This is Liam, in for Bear. You want Claude to plan your trip. "
        "So the question isn't how to write the perfect prompt. "
        "It's how to make Claude interview you first.",
        "BrutalistHesitantWriter",
        {"text": "How do I write the perfect prompt\nfor my trip?",
         "triggerWords": "write the perfect prompt",
         "replacementWords": "make Claude interview me first",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
         "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'How do I write the perfect prompt'"},
         {"at": 0.6, "event": "backspaces 'write the perfect prompt' → 'make Claude interview me first' on the spoken correction"}],
        lead_silence_s=0.8,
        motion_claim="The writer types the naive prompt question and corrects it to the real one: make Claude interview you first.",
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion(
        "BDEFS", "terms",
        "Three terms. A prompt: the instruction you type. An interview: Claude "
        "asks you questions before it starts. A brief: what Claude knows about "
        "your job — which is exactly what the interview builds.",
        "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [{"term": "prompt", "meaning": "the instruction you type into the chat"},
                   {"term": "interview", "meaning": "Claude asks you questions before it starts"},
                   {"term": "brief", "meaning": "what Claude knows about your job"}],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'prompt' lands"},
         {"at": 0.5, "event": "'interview' lands"},
         {"at": 0.78, "event": "'brief' lands"}],
        gate="CARD",
        qc={"sparse_by_design": True,
            "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

B = [
    beat(
        "B00",
        "Start here. You type 'plan my trip' and hit send. Claude answers "
        "straight away — and the answer is thin. A generic list that fits "
        "anyone. Nothing went in, so nothing much came out.",
        "B00_AskOnce",
        "A composer with 'plan my trip' typed; a thin page with three short lines grows above it; the label 'generic answer' lands beside it.",
        [{"at": 0.1, "event": "composer + cursor"},
         {"at": 0.3, "event": "'plan my trip' types"},
         {"at": 0.55, "event": "thin answer page grows"},
         {"at": 0.8, "event": "label lands"}]),
    beat(
        "B01",
        "Now change one line. Before the task, you add: 'Ask me five "
        "questions first.' Claude stops guessing and starts asking. Five "
        "question bubbles drop in — and that is the whole trick. The "
        "interview, not the instruction.",
        "B01_AskFirst",
        "The composer gains the line 'Ask me 5 questions first.'; five question bubbles drop in a row above it; the label 'the interview' lands beside.",
        [{"at": 0.1, "event": "composer"},
         {"at": 0.3, "event": "'Ask me 5 questions first.' types"},
         {"at": 0.6, "event": "five question bubbles drop in"},
         {"at": 0.85, "event": "label lands"}]),
    beat(
        "B02",
        "Watch what the questions do. Budget. Dates. Who is going. Fast or "
        "slow. One must-see. Each question names something Claude was about "
        "to guess — and would have guessed wrong. The interview doesn't make "
        "Claude smarter. It makes the brief complete.",
        "B02_FiveQuestions",
        "Five question cards land in a row — budget, dates, who, pace, must-see — then a terracotta scan line sweeps under them.",
        [{"at": 0.1, "event": "cards begin to land on each spoken word"},
         {"at": 0.45, "event": "all five cards down"},
         {"at": 0.75, "event": "scan line sweeps"}]),
    beat(
        "B03",
        "Now you answer — briefly. Tight budget. November. Two adults and a "
        "kid. Slow pace. The fish market at opening. Each answer lands as a "
        "chip in your brief. You skip what doesn't matter. In thirty seconds "
        "the brief holds everything the trip needs.",
        "B03_BriefBuilt",
        "An open iso brief box; five answer chips (tight, November, 2+1, slow, fish market) drop into it one by one; the label 'your brief' lands beside.",
        [{"at": 0.1, "event": "brief box opens"},
         {"at": 0.3, "event": "chips drop in on each spoken answer"},
         {"at": 0.85, "event": "label lands"}]),
    beat(
        "B04",
        "Now the plan comes back — and look at it. Not a generic list: slow "
        "mornings for the kid, free sights for the budget, the fish market "
        "on day two. Same AI, same task. The only thing that changed was "
        "the brief.",
        "B04_TailoredPlan",
        "The brief box feeds a full tailored plan page that grows line by line; the thin generic page from B00 sits dimmed beside it; a terracotta check stamps the tailored page.",
        [{"at": 0.1, "event": "brief box + thin generic page"},
         {"at": 0.35, "event": "tailored page grows"},
         {"at": 0.7, "event": "check stamps"}]),
    beat(
        "B05",
        "Second example — a difficult email. 'Help me apologise to my "
        "landlord.' Claude could draft straight away, and it would land "
        "wrong. So it asks first: who is it to? What went wrong? Firm or "
        "friendly? Three questions — and the draft lands, because it was "
        "aimed.",
        "B05_SecondDemo",
        "An envelope card labelled 'difficult email'; three question bubbles land beside it; a finished letter page fades in with an ink check.",
        [{"at": 0.1, "event": "envelope card"},
         {"at": 0.4, "event": "three question bubbles land"},
         {"at": 0.7, "event": "letter page + check"}]),
    beat(
        "B06",
        "Sharpen the move: don't just ask for questions — ask for questions "
        "that would change your answer. A lazy question, like 'favourite "
        "colour', costs you time and changes nothing. A sharp one pays you "
        "back. That is also why you skip any question that wouldn't change "
        "your result.",
        "B06_SharpQuestions",
        "Two question cards side by side: a dimmed one ('favourite colour?') with a grey strike, and a highlighted one ('changes the answer?') with a terracotta dot and check.",
        [{"at": 0.1, "event": "lazy card dims with strike"},
         {"at": 0.45, "event": "sharp card lands with dot + check"},
         {"at": 0.8, "event": "label lands"}]),
    beat(
        "B07",
        "The rule of thumb: use the interview whenever the answer depends on "
        "you. Your trip, your email, your judgment. And skip it when it "
        "doesn't — 'what time is it in Tokyo' needs no questions. Your "
        "context is the missing ingredient; the interview hands it over.",
        "B07_TheRule",
        "Two mini task cards: 'needs you' (trip, email) with question bubbles and a check, and 'plain fact' (Tokyo time) with a straight arrow and the label 'skip'.",
        [{"at": 0.1, "event": "both cards land"},
         {"at": 0.45, "event": "bubbles + check on the left card"},
         {"at": 0.7, "event": "'skip' label on the right card"}]),
]

YT_PROMPT = (
    "Here's a task I need help with: [describe it in one line]. Before you "
    "start, ask me up to five questions that would change your answer — one "
    "at a time, waiting for my reply after each one. Then do the task using "
    "my answers."
)
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT +
    " Then check two things yourself. Did every answer change something in "
    "the result? If a question changed nothing, drop it next time.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN",
     "segment": "Interview Me First", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: every answer changed something in the result.",
                "Check: questions that changed nothing get dropped next time."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
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
    "slug": SLUG, "title": TITLE, "topic": "AI · ASK FIRST",
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
    "audience": "smart, pragmatic general audience — not AI experts; a viewer who has typed one-line requests into an AI chat tool",
    "source_doc": "NEW — built from scratch for film #9 of the How-to-AI queue (2026-10-03). No mirror source.",
    "playlist": "How to AI", "chapter_number": 9,
    "tags": ["Claude", "prompting", "interview technique", "context", "AI tips", "Nik Bear Brown"]},
    "beats": B}

# ── asserts (the film's contract) ────────────────────────────────────────────
ids = [b["beat_id"] for b in B]
assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04",
               "B05", "B06", "B07", "BHTF", "BOUT"], f"beat order wrong: {ids}"
total = sum(b["estimated_duration_s"] for b in B)
assert 170 <= total <= 220, f"total {total}s outside 170–220 s band"

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
