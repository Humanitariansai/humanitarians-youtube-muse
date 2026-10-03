#!/usr/bin/env python3
"""make_sheet.py — Claude, Allowed. (show-tell film, claude-allowed)

Rewrites hai-claude-allowed ("Claude, Allowed.", Claude, For Students H1) for the
Humanitarians AI channel general audience: smart, pragmatic, NOT AI experts.
The source's argument survives; the student framing generalizes to anyone living
under an AI-use policy (school, work, publishing).

Spine (show-tell): BIDEA (hesitant writer) -> BDEFS (terms) -> B00 hero (the
policy doc) -> B01 scope -> B02 the exception trap -> B03 what's still open ->
B04 predict -> B05 reveal -> BHTF (composer) -> BOUT (spoken outro).
No cold-open, no verdict card (bookend_exempt). Body is all isometric Manim
drawings on the Claude palette; the voice explains. No body cards: every body
beat is a thing, a part, or a flow — nothing that passes the card test.

Run: python3 make_sheet.py   (writes beat_sheet.json next to it)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "claude-allowed"
TITLE = "Claude, Allowed."


def beat(bid, narration, cls, image, show):
    return {
        "beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
        "narration_text": narration,
        "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {
            "type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
            "manim": {"class": cls}, "motion_claim": image,
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
    beat(
        "B00",
        "Meet the hero object: the AI-use policy. Schools have one. Employers have one. A few paragraphs — and nearly all the confusion hides inside a single exception.",
        "B00_PolicyPage",
        "An AI policy document drops in; a terracotta highlighter sweeps to one line — 'the exception'.",
        [
            {"at": 0.1, "event": "policy doc drops in"},
            {"at": 0.55, "event": "highlighter lands on the exception line"},
            {"at": 0.8, "event": "'the exception' label"},
        ],
    ),
    beat(
        "B01",
        "Most bans say roughly the same thing: don't use AI to do work you're supposed to do yourself, and submit it without saying so. That's the scope — evaluated work, submitted as yours, undisclosed. Not: never use AI. Not: never get good at it. Not: never practice on your own time.",
        "B01_Scope",
        "Six policy slips sort into two rows: 'banned' (graded work / as your own / undisclosed) and 'open' (practice / get fluent / own time); a check lands on the open row.",
        [
            {"at": 0.1, "event": "two rows appear: banned, open"},
            {"at": 0.35, "event": "banned slips drop: graded work, as your own, undisclosed"},
            {"at": 0.65, "event": "open slips drop: practice, get fluent, own time"},
            {"at": 0.9, "event": "check on the open row"},
        ],
    ),
    beat(
        "B02",
        "Here's the trap. Nearly every policy has an exception — something like 'except for educational purposes.' One teacher reads that as any use with permission. Another reads it as nothing AI, full stop. You don't want to learn which one is yours after you submit. So ask first, and get the answer in writing — even an email reply counts. Assumptions here are expensive.",
        "B02_Trap",
        "The exception phrase sits on a plate and splits into three readings (permissive / middle / strict); a check lands on an envelope — 'ask · in writing'.",
        [
            {"at": 0.1, "event": "exception plate lands"},
            {"at": 0.35, "event": "three reading cards drop in"},
            {"at": 0.7, "event": "envelope arrives"},
            {"at": 0.85, "event": "check on the envelope: ask, get it in writing"},
        ],
    ),
    beat(
        "B03",
        "What's yours, no matter the policy: fluency. Practice prompting on your own time. Quiz yourself on your own material. Get explanations when you're confused — as long as you don't submit AI output as your own work. Anthropic's AI Fluency course is free and openly licensed, so anyone can take it. A ban on graded homework is not a ban on getting capable.",
        "B03_Fluency",
        "A workbench pad; three items drop in one by one — a prompt page, a quiz card, a course book tagged 'free'.",
        [
            {"at": 0.1, "event": "workbench pad"},
            {"at": 0.3, "event": "prompt page drops in"},
            {"at": 0.55, "event": "quiz card drops in"},
            {"at": 0.8, "event": "course book with 'free' tag"},
        ],
    ),
    beat(
        "B04",
        "One question before the reveal — commit to it. What actually gets people caught? Using AI — or something else? Think before the next beat.",
        "B04_Predict",
        "A sparse beat: a big '?' on the stage, the question caption under it, a terracotta dot — hold.",
        [
            {"at": 0.1, "event": "'?' lands"},
            {"at": 0.4, "event": "question caption"},
            {"at": 0.65, "event": "terracotta dot"},
        ],
    ),
    beat(
        "B05",
        "It's not the use. It's the undisclosed use. People aren't punished for being AI-fluent — they're punished for submitting AI-assisted work without saying so. Same output, different path. Disclosure doesn't make everything automatically fine. But it puts you in the conversation instead of outside it.",
        "B05_Reveal",
        "Two identical pages: the left gets a check ('disclosed — the conversation'), the right a cross ('undisclosed — the violation').",
        [
            {"at": 0.1, "event": "two identical pages"},
            {"at": 0.4, "event": "check lands left: disclosed"},
            {"at": 0.6, "event": "cross lands right: undisclosed"},
            {"at": 0.85, "event": "captions: the conversation / the violation"},
        ],
    ),
]

OPEN = [
    remotion(
        "BIDEA", "the question",
        "Hallo. This is Liam, in for Bear. Everyone says AI is banned — at school, at work. But a ban is a rule, and rules have edges. Let's read the sentence, not the story around it.",
        "BrutalistHesitantWriter",
        {
            "text": "Everyone says AI is banned at school, so is AI banned everywhere",
            "triggerWords": "is AI banned everywhere",
            "replacementWords": "what does the ban actually cover",
            "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
            "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": "",
        },
        [
            {"at": 0.0, "event": "types the naive question"},
            {"at": 0.6, "event": "backspaces 'is AI banned everywhere' → 'what does the ban actually cover' on the spoken correction"},
        ],
        lead_silence_s=0.8,
        motion_claim="The writer types the naive ban question and corrects it to the real one: what the ban actually covers.",
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."},
    ),
    remotion(
        "BDEFS", "terms",
        "Three terms. Policy: the written AI rules where you study or work. Disclosure: saying openly that AI helped. AI fluency: being good at using AI — like being good with a spreadsheet.",
        "ClaudeDefinitions",
        {
            "title": "Terms In This Film",
            "terms": [
                {"term": "policy", "meaning": "the written AI rules where you study or work"},
                {"term": "disclosure", "meaning": "saying openly that AI helped"},
                {"term": "AI fluency", "meaning": "being good at using AI — like being good with a spreadsheet"},
            ],
            "folderLabel": "@NikBearBrown",
        },
        [
            {"at": 0.12, "event": "'policy' lands"},
            {"at": 0.5, "event": "'disclosure' lands"},
            {"at": 0.78, "event": "'AI fluency' lands"},
        ],
        gate="CARD",
        qc={"sparse_by_design": True,
            "sparse_reason": "TERMS card: three prerequisites, one line each."},
    ),
]

YT_PROMPT = ("Draft me a short, honest email to my teacher asking whether I can use Claude for "
             "[describe your assignment or subject]. I want to start the right conversation — keep it to one paragraph.")
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then two checks yourself. "
    "Does the email name the exact assignment? And do you have the teacher's reply in writing before you use AI on it? "
    "At work, swap in your manager.",
    "ClaudeComposerAsk",
    {
        "greeting": "Your turn.",
        "topic": "CLAUDE · YOUR TURN",
        "segment": "Ask Before You Use",
        "command": YT_PROMPT,
        "runningText": "paste this into Claude…",
        "output": [
            "Check: the email names the exact assignment.",
            "Check: you have the reply in writing before using AI on it.",
        ],
        "folderLabel": "@NikBearBrown",
    },
    [
        {"at": 0.0, "event": "Composer opens — 'Your turn.'"},
        {"at": 0.1, "event": "the prompt types in full"},
        {"at": 0.8, "event": "two check lines land"},
    ],
)

SPARSE_REASON = (
    "show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
    "minimal labels, with the voice carrying the explanation. The negative space is the style, so only "
    "underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply."
)
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({
    "beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
    "narration_text": f"{TITLE} At Nik Bear Brown.",
    "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
    "shot": {"type": "REMOTION", "source": "own",
             "show": [{"at": 0.0, "event": "title restates; handle"}],
             "remotion": {"pattern": "ClaudeTitleOutro",
                         "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
    "kind": "outro_voice", "tail_silence_s": 1.0,
})

sheet = {
    "metadata": {
        "slug": SLUG,
        "title": TITLE,
        "topic": "CLAUDE · AI USE POLICIES",
        "skill": "show-tell",
        "style_preset": "show-tell",
        "channel": "claude-liam",
        "persona": "Liam (in for Bear)",
        "voice": "am_onyx",
        "voice_kokoro": "am_onyx",
        "engine": "kokoro",
        "clock": "narration",
        "palette": "claude",
        "register": "Teardown",
        "fps": 24,
        "aspect_ratio": "16:9",
        "width": 3840,
        "height": 2160,
        "caption_policy": "none",
        "greeting_language": "German/Dutch (Hallo)",
        "bookend_exempt": ["cold-open", "bvdt"],
        "bookend_exempt_reason": (
            "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card, no verdict card; "
            "Your Turn is the Claude.ai composer; spoken @NikBearBrown outro stays."
        ),
        "audience": "smart, pragmatic general audience — not necessarily AI experts",
        "source_doc": (
            "nikbearbrown/humanitarians-youtube-muse: claude-for-artificial-intelligence/hai-claude-allowed "
            "(beat_sheet.json, PEDAGOGY.md, NARRATION-GATE-P.md); rewritten for the humanitarians AI channel"
        ),
        "playlist": "How to use AI",
        "chapter_number": 0,
        "tags": ["Claude", "AI policy", "AI at school", "AI at work", "disclosure", "academic integrity",
                 "AI fluency", "Anthropic", "Nik Bear Brown"],
    },
    "beats": B,
}

if __name__ == "__main__":
    ids = [b["beat_id"] for b in sheet["beats"]]
    assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05", "BHTF", "BOUT"], ids
    manim_beats = [b for b in sheet["beats"] if b["lane"] == "manim"]
    assert len(manim_beats) == 6, len(manim_beats)
    for b in manim_beats:
        assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), b["beat_id"]
    total = sum(b["estimated_duration_s"] for b in sheet["beats"])
    assert 120 <= total <= 240, f"total {total}s outside 2-4 min band"
    assert sheet["metadata"]["bookend_exempt"] == ["cold-open", "bvdt"]
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
    print(f"beats={len(ids)} body={len(manim_beats)} total={round(total, 1)}s (~{int(total//60)}m{int(total%60):02d}s)")
    print("beat_sheet.json written")
