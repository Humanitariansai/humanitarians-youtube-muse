#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Say what you want, plainly".

SHOW-TELL (Bear, 2026-09-26): one drawn isometric illustration per beat,
minimal labels, Liam's narration (Kokoro am_onyx) explaining the action.
Source: REFACTOR of the mirror-repo lesson
`claude/claude-for-education/claude-liam-prompt-tutorial-lesson-02-clear-and-direct`
(Anthropic Prompt Engineering Interactive Tutorial, Lesson 02: Being Clear
and Direct) — rewritten for a smart, pragmatic general audience, not AI experts.

The film's argument: the single highest-leverage prompting habit is to say
what you want, plainly. A vague prompt ("write a summary") leaves blank
lines the AI fills with guesses (its most common default); a brief answers
four questions (how long, what shape, who it's for, what must be in it);
the golden rule is the capable-new-employee test.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "say-what-you-want-plainly"
TITLE = "Say what you want, plainly"

NAR = {
    "BIDEA": ("Hallo. This is Liam, in for Bear. Here is the habit that matters most with AI: "
              "say what you want, plainly. Watch. \"write a summary\" is a wish. "
              "A three-sentence summary of this page, in plain words, for a teammate: that is a brief. "
              "Same request. Different answer."),
    "BDEFS": ("Three terms. A prompt: just what you type into the AI. "
              "A brief: a prompt that says exactly what you want, like a work brief for a colleague. "
              "And a default: the AI's most common guess, the one it reaches for when you leave a gap."),
    "B00": ("This is a prompt. A request, a question, a job you type into the AI. "
            "And it is the single biggest thing deciding what comes back. "
            "Not the model, not the settings. The words you put in."),
    "B01": ("But watch what a vague prompt does. \"Write a summary\" hands the AI a stack of blank lines. "
            "Every line you leave blank is a guess it has to make. "
            "And its guesses come from the default: the most common answer, not necessarily the one you needed."),
    "B02": ("The default is not wrong. It is just not yours. The AI answers the way most people want, "
            "because most people are all it knows. Your reader, your style, your situation: "
            "none of that is in the prompt, so none of it is in the answer."),
    "B03": ("The fix is almost embarrassing. Say what you want. Plainly. "
            "Out loud, in the prompt, the way you would say it to a person sitting across from you."),
    "B04": ("Every good brief answers four questions. How long. "
            "What shape: bullets, a table, plain sentences. Who it is for. And what must be in it. "
            "Answer the ones you care about. Skip the rest."),
    "B05": ("Think of the AI as a brilliant new hire on day one. "
            "Smart, eager, and with zero idea how you like things done. "
            "Your style, your reader, the edge cases: all missing. "
            "So tell it. Explicitly. The brief is the onboarding."),
    "B06": ("Here is a vague prompt becoming a brief. \"Write a summary of this document.\" "
            "Now fill the blanks. Length: three sentences. Shape: plain words. "
            "Reader: a teammate. Must-haves: the finding, the method, and the limit. "
            "Every blank you fill is a guess the AI no longer has to make."),
    "B07": ("Same job, two prompts. \"Write a summary\" gets you three pages that fit nobody. "
            "The brief — length, shape, reader, must-haves — gets you one page that fits. "
            "That is the whole habit. Say what you want, plainly."),
    "BHTF": ("Your turn. Take one prompt you actually use — something you have been running as-is. "
             "Ask it the four questions: how long, what shape, who it is for, what must be in it. "
             "Add whatever you care about but left blank. Run both versions. "
             "Then check two things yourself: does the new answer fit your reader, "
             "and did anything you left blank come back wrong?"),
    "BOUT": "Say what you want, plainly. At Nik Bear Brown.",
}

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
                 "minimal labels, with the voice carrying the explanation. The negative space is the style, "
                 "so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")


def est(narration):
    return round(len(narration.split()) / 2.5, 1)


def manim_beat(bid, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": NAR[bid], "estimated_duration_s": est(NAR[bid]),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image},
            "qc": {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}}


def remotion(bid, act, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": NAR[bid], "estimated_duration_s": est(NAR[bid]),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


B = [
    manim_beat(
        "B00", "B00_PromptSlip",
        "A plain kraft prompt slip drops onto the stage and lands; the word 'prompt' beside it. "
        "A terracotta dot pulses on the slip as the voice lands on 'the words you put in'.",
        [{"at": 0.05, "event": "slip drops in with a landing shadow"},
         {"at": 0.15, "event": "label 'prompt' lands"},
         {"at": 0.85, "event": "terracotta dot pulses on the slip"}]),
    manim_beat(
        "B01", "B01_Guesses",
        "A dark AI block; the short vague slip 'write a summary' slides into it; three mismatched "
        "pages pop out in a row beside it, labelled 'guesses'.",
        [{"at": 0.05, "event": "AI block and label"},
         {"at": 0.30, "event": "vague slip slides into the block"},
         {"at": 0.70, "event": "three mismatched pages pop out, labelled 'guesses'"}]),
    manim_beat(
        "B02", "B02_MostCommon",
        "The dark AI block with a row of small grey pages behind it ('most people'); the vague slip "
        "slides in; one grey page pops out labelled 'most common answer'. A small slip labelled 'you' "
        "sits apart, and a terracotta dot lands on it at the end.",
        [{"at": 0.05, "event": "AI block, crowd of grey pages, 'you' slip"},
         {"at": 0.35, "event": "vague slip slides in; one grey page pops out, 'most common answer'"},
         {"at": 0.88, "event": "terracotta dot lands on the 'you' slip"}]),
    manim_beat(
        "B03", "B03_TheFix",
        "The dim vague slip sits left; a new larger brief page lands right and three plain ink lines "
        "write themselves onto it as the voice says 'plainly'.",
        [{"at": 0.05, "event": "vague slip dim on the left"},
         {"at": 0.10, "event": "new brief page lands right"},
         {"at": 0.35, "event": "three ink lines write on"},
         {"at": 0.80, "event": "label 'say it plainly'"}]),
    manim_beat(
        "B04", "B04_FourQuestions",
        "The brief slip sits centre; four numbered kraft chips drop around it one by one — "
        "1 length, 2 format, 3 audience, 4 must-haves — each with its term beside it.",
        [{"at": 0.05, "event": "brief slip in place"},
         {"at": 0.20, "event": "chip 1 'length'"},
         {"at": 0.35, "event": "chip 2 'format'"},
         {"at": 0.60, "event": "chip 3 'audience'"},
         {"at": 0.78, "event": "chip 4 'must-haves'"}]),
    manim_beat(
        "B05", "B05_NewHire",
        "An open folder labelled 'day one' (the new hire); the four numbered chips drop into it; "
        "a neat page rises out with an ink check.",
        [{"at": 0.05, "event": "open folder, label 'day one'"},
         {"at": 0.28, "event": "four chips drop into the folder"},
         {"at": 0.80, "event": "a page rises out with a check"}]),
    manim_beat(
        "B06", "B06_BriefRewrite",
        "The slip sits centre with one ghost line; four numbered ink lines write on one by one "
        "(length, shape, reader, must-haves) as each is named — every blank filled.",
        [{"at": 0.05, "event": "slip with one ghost line, label 'brief'"},
         {"at": 0.30, "event": "line 1: length"},
         {"at": 0.42, "event": "line 2: shape"},
         {"at": 0.55, "event": "line 3: reader"},
         {"at": 0.68, "event": "line 4: must-haves"}]),
    manim_beat(
        "B07", "B07_Compare",
        "Split frame. Left: the vague slip returns three dim mismatched pages, labelled 'vague'. "
        "Right: the brief slip returns one neat page with an ink check, labelled 'brief'.",
        [{"at": 0.05, "event": "vague side: three mismatched pages"},
         {"at": 0.70, "event": "brief side: one neat page with a check"}]),
]

OPEN = [
    remotion(
        "BIDEA", "the question", "BrutalistHesitantWriter",
        {"text": "Write me a summary of this.\nHmm, \"write a summary\" is a wish. Say it plainly.",
         "triggerWords": "write a summary", "replacementWords": "a three-sentence summary of this page, in plain words, for a teammate",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
         "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Write me a summary of this.'"},
         {"at": 0.6, "event": "backspaces 'write a summary' → 'a three-sentence summary of this page, in plain words, for a teammate' on the spoken correction"}],
        lead_silence_s=0.8,
        motion_claim="The writer types the vague request and corrects it into the direct brief.",
        qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion(
        "BDEFS", "terms", "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [{"term": "prompt", "meaning": "just what you type into the AI"},
                   {"term": "brief", "meaning": "a prompt that says exactly what you want, like a work brief"},
                   {"term": "default", "meaning": "the AI's most common guess, reached for when you leave a gap"}],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'prompt' lands"},
         {"at": 0.5, "event": "'brief' lands"},
         {"at": 0.78, "event": "'default' lands"}],
        gate="CARD",
        qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Take one prompt you actually use — something you have been running as-is. "
             "Rewrite it as a brief: say how long the answer should be, what shape it should take, "
             "who it is for, and what must be in it. Then run the old version and the new version, and compare.")
YOURTURN = remotion(
    "BHTF", "your turn", "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "HOW TO AI · YOUR TURN", "segment": "Brief One Prompt",
     "command": YT_PROMPT, "runningText": "paste this into Claude…",
     "output": ["Check: the new answer fits your reader better.",
                "Check: every gap you filled came back wrong in the old version."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": NAR["BOUT"], "estimated_duration_s": est(NAR["BOUT"]),
          "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · PROMPTING", "skill": "show-tell",
    "style_preset": "show-tell", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24,
    "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
    "source_doc": ("REFACTOR of mirror-repo lesson "
                   "claude/claude-for-education/claude-liam-prompt-tutorial-lesson-02-clear-and-direct "
                   "(Anthropic Prompt Engineering Interactive Tutorial — Lesson 02: Being Clear and Direct), "
                   "rewritten for a general audience. General-audience prompt guidance per Anthropic's "
                   "public prompting documentation."),
    "playlist": "how-to-use-ai", "chapter_number": 0,
    "tags": ["prompting", "prompt engineering", "be clear and direct", "how to ai",
             "general audience", "Claude", "Nik Bear Brown"]},
    "beats": B}

# ── assertions: beat counts and total duration ──
assert len(B) == 12, f"expected 12 beats, got {len(B)}"
manim_beats = [b for b in B if b["lane"] == "manim"]
assert len(manim_beats) == 8, f"expected 8 manim beats, got {len(manim_beats)}"
for b in B:
    assert b["narration_text"], f"{b['beat_id']}: empty narration"
    assert b["voice"] == "am_onyx", f"{b['beat_id']}: wrong voice"
    assert b["estimated_duration_s"] > 0, f"{b['beat_id']}: bad duration"
for b in manim_beats:
    cls = b["shot"]["manim"]["class"]
    assert cls.startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class {cls} mismatches beat id"
    assert b["qc"]["sparse_by_design"], f"{b['beat_id']}: missing sparse waiver"
raw = json.dumps(sheet)
assert not any(ext in raw for ext in (".mp3", ".mp4", ".wav")), "audio/binary referenced in sheet"
total = sum(b["estimated_duration_s"] for b in B)
assert 120 <= total <= 300, f"total {total}s outside 120–300 s"
classes = [b["shot"]["manim"]["class"] for b in manim_beats]
assert len(set(classes)) == len(classes), "duplicate scene class names"

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats;", len(manim_beats), "manim;", "est", round(total, 1), "s")
