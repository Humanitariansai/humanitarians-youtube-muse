#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Show It an Example" (film 3 of 24, How to AI).

SHOW-TELL (Bear, 2026-09-26): one drawn isometric illustration per body beat,
minimal on-screen labels, Liam's narration (Kokoro am_onyx) carries the
explanation. Source argument refactored from Anthropic's Prompt Engineering
Interactive Tutorial, Lesson 07 (few-shot prompting) — the source supplies the
argument and facts; the script is rewritten for a smart, pragmatic general
audience (Bear, 2026-10-03: explain every term, show rather than tell).

The technique's jargon name ("few-shot") is never used before BDEFS explains
it in plain words: teaching the AI by example instead of by instruction.

Cast of objects (law: SAME OBJECTS, WHOLE FILM): the prompt box (your prompt),
example pages (finished samples), the rule stack (written instructions), and
the output page (your draft).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "show-it-an-example"
TITLE = "Show It an Example"

NARR = {
    "BIDEA": ("Hallo. This is Liam, in for Bear. You want Claude to write the "
              "way you write. So you sit down and carefully describe your style, "
              "in three long paragraphs. And Claude still gets it wrong. "
              "What if you stopped explaining, and started showing?"),
    "BDEFS": ("Three terms. A prompt: the text you type into an AI. "
              "An example: a finished sample of the exact thing you want it to make. "
              "And few-shot: the jargon name for a simple idea — teaching the AI "
              "by showing it a few examples instead of writing instructions."),
    "B00": ("Here is the whole trick, on one box. Your prompt is a box, and you "
            "have two ways to fill it. You can describe what you want in words — "
            "or you can show it. This film is about the showing way."),
    "B01": ("First, the describe way. You write the rules out: warm tone, short "
            "sentences, plain words, always end with a question. The stack grows — "
            "a paragraph for tone, a paragraph for length, a paragraph for words. "
            "Five rules, all in words. Claude reads every one of them... and still "
            "has to guess what warm actually sounds like."),
    "B02": ("Now the show way. Same box, but instead of the rule stack, three "
            "examples drop in. Three finished notes, written exactly the way you "
            "want them. No rules, no describing, no guessing. Just three samples "
            "that say: like this."),
    "B03": ("Why do three examples beat the whole rule stack? Because each example "
            "quietly carries five things at once: the length, the tone, the shape "
            "of the text, the words you actually use, and how tricky cases get "
            "handled. You typed none of that. Three small samples showed all of it "
            "— and Claude copied the lot."),
    "B04": ("One warning, because the same power cuts the other way. Claude copies "
            "the pattern — whatever the pattern is. Drop in one sloppy example "
            "and the result comes out sloppy too. The examples teach; you choose "
            "what they teach. One bad example teaches the wrong lesson, fast."),
    "B05": ("So pick good examples. Three quick checks before you paste. Are they "
            "real, typical ones — not weird edge cases? Do they all agree with "
            "each other, or are they pulling in different directions? And do they "
            "look like the thing you are about to ask for? Yes, yes, yes — paste."),
    "B06": ("And there is a bonus. Three examples are almost always shorter than "
            "the five paragraphs they would replace. Fewer words in, same five "
            "specs carried. Less typing for you, a shorter prompt to send, and "
            "Claude still gets the full picture."),
    "BHTF": ("Your turn. Paste this into Claude: Pick something you write often — "
             "weekly updates, captions, meeting notes. Find three real ones you are "
             "proud of and paste them into Claude as examples. Then add your new "
             "note at the end and tell Claude to continue the pattern. Run it once "
             "more with only a written style description and no examples. Then "
             "check two things yourself. Which version sounds more like you? And "
             "did the example version get the length right, without you saying a "
             "word about it?"),
    "BOUT": f"{TITLE}. At Nik Bear Brown.",
}


def dur(text):
    return round(len(text.split()) / 2.5, 1)


def manim_beat(bid, cls, image, show, **extra):
    b = {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
         "narration_text": NARR[bid], "estimated_duration_s": dur(NARR[bid]),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image,
                  "show": show, "manim": {"class": cls}, "motion_claim": image}}
    b.update(extra)
    return b


def remotion(bid, act, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": NARR[bid], "estimated_duration_s": dur(NARR[bid]),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a "
                 "cream stage per beat, minimal labels, with the voice carrying the "
                 "explanation. The negative space is the style, so only underfill and "
                 "clustered are waived; edge-bleed, empty-frame and contrast still apply.")

OPEN = [
    remotion(
        "BIDEA", "the question", "BrutalistHesitantWriter",
        {"text": "How do I describe my style\nso Claude gets it right?",
         "triggerWords": "describe my style", "replacementWords": "show it an example",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
         "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'How do I describe my style'"},
         {"at": 0.6, "event": "backspaces 'describe my style' → 'show it an example' on the spoken correction"}],
        lead_silence_s=0.8,
        motion_claim="The writer types the naive describe question and corrects it to the real one: show it an example.",
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion(
        "BDEFS", "terms", "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [
             {"term": "prompt", "meaning": "the text you type into an AI"},
             {"term": "example", "meaning": "a finished sample of exactly what you want it to make"},
             {"term": "few-shot", "meaning": "teaching the AI by example instead of by instruction"}],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'prompt' lands"},
         {"at": 0.5, "event": "'example' lands"},
         {"at": 0.78, "event": "'few-shot' lands"}],
        gate="CARD",
        qc={"sparse_by_design": True,
            "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

B = [
    manim_beat(
        "B00", "B00_TheBox",
        "An empty open kraft box drops onto the stage and settles; the words 'your prompt' beside it.",
        [{"at": 0.1, "event": "box drops in"}, {"at": 0.7, "event": "label"}]),
    manim_beat(
        "B01", "B01_RuleStack",
        "The box waits at left while a stack of instruction pages piles up beside it, labelled 'rules'.",
        [{"at": 0.1, "event": "pages pile one by one"}, {"at": 0.6, "event": "label"}]),
    manim_beat(
        "B02", "B02_ExamplesIn",
        "The rule stack slides away; three finished example pages drop into the box one by one.",
        [{"at": 0.1, "event": "rules slide off"}, {"at": 0.35, "event": "examples drop in"}]),
    manim_beat(
        "B03", "B03_FiveThings",
        "The three example pages fan out in a row; five small tags rise off them: length, tone, shape, words, tricky bits.",
        [{"at": 0.1, "event": "examples fan out"}, {"at": 0.4, "event": "five tags rise"}]),
    manim_beat(
        "B04", "B04_BadCard",
        "A fourth, sloppy example card drops in at the end of the row; an output page slides out of the box, crooked, labelled 'your draft'.",
        [{"at": 0.15, "event": "bad card drops"}, {"at": 0.5, "event": "crooked output"}]),
    manim_beat(
        "B05", "B05_ThreeChecks",
        "The three good examples pass through a check gate one by one; a check pops over each.",
        [{"at": 0.15, "event": "gate rises"}, {"at": 0.4, "event": "cards pass, checks pop"}]),
    manim_beat(
        "B06", "B06_ShortVsTall",
        "The three examples stand beside the tall rule stack: a short pile against a tall one, 'examples' vs 'rules'.",
        [{"at": 0.15, "event": "tall stack grows"}, {"at": 0.5, "event": "labels"}]),
]

YT_PROMPT = ("Pick something you write often — weekly updates, captions, meeting "
             "notes. Find three real ones you are proud of and paste them into "
             "Claude as examples. Then add your new note at the end and tell Claude "
             "to continue the pattern. Run it once more with only a written style "
             "description and no examples.")
YOURTURN = remotion(
    "BHTF", "your turn", "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "HOW TO AI · YOUR TURN",
     "segment": "Teach by Example", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: which version sounds more like you?",
                "Check: did the example version get the length right, unasked?"],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

BEATS = OPEN + B + [YOURTURN]
BEATS.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
              "narration_text": NARR["BOUT"], "estimated_duration_s": dur(NARR["BOUT"]),
              "voice": "am_onyx", "engine": "kokoro",
              "shot": {"type": "REMOTION", "source": "own",
                       "show": [{"at": 0.0, "event": "title restates; handle"}],
                       "remotion": {"pattern": "ClaudeTitleOutro",
                                    "props": {"title": TITLE, "slug": SLUG,
                                              "handle": "@NikBearBrown", "subline": ""}}},
              "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · TEACHING WITH EXAMPLES",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant "
                              "writer + terms card, no verdict card; Your Turn is the "
                              "Claude.ai composer; spoken outro stays."),
    "audience": "smart, pragmatic general audience — not AI experts",
    "source_doc": ("Refactor of nikbearbrown/humanitarians-youtube-muse:"
                   "claude/claude-for-education/claude-liam-prompt-tutorial-lesson-07-"
                   "few-shot-prompting (after Anthropic Prompt Engineering Interactive "
                   "Tutorial, Lesson 07: Few-Shot Prompting); argument and facts kept, "
                   "script rewritten for a general audience, 2026-10-03"),
    "playlist": "How to AI", "chapter_number": 3,
    "tags": ["few-shot prompting", "examples beat instructions", "prompting basics",
             "Claude", "How to AI", "Nik Bear Brown"]},
    "beats": BEATS}

# ── assertions: beat counts and duration ──────────────────────────────
assert len(BEATS) == 11, f"expected 11 beats, got {len(BEATS)}"
ids = [b["beat_id"] for b in BEATS]
assert ids[:2] == ["BIDEA", "BDEFS"] and ids[-2:] == ["BHTF", "BOUT"], ids
assert len([b for b in BEATS if b["lane"] == "manim"]) == 7, "expected 7 manim body beats"
for b in BEATS:
    assert b["narration_text"].strip(), f"{b['beat_id']} has no narration"
    assert b["voice"] == "am_onyx" and b["engine"] == "kokoro", b["beat_id"]
    assert "few-shot" not in b["narration_text"].lower() or b["beat_id"] != "BIDEA", \
        "few-shot must be explained in BDEFS before first use"
total = sum(b["estimated_duration_s"] for b in BEATS) + 1.0  # + BOUT tail
assert 180 <= total <= 360, f"total {total}s outside 3–6 min band"
classes = [b["shot"]["manim"]["class"] for b in B]
assert all(c.startswith(bid) for bid, c in zip([b["beat_id"] for b in B], classes))
assert len(set(classes)) == 7, "scene classes must be unique"

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(BEATS)} beats; est {round(total)} s ({round(total/60, 1)} min)")
