#!/usr/bin/env python3
"""make_sheet.py — Tame your inbox (show-tell, Liam, Teardown).

Built from scratch 2026-10-05 for the humanitarians AI YouTube channel, general
audience (smart, pragmatic, not AI experts). Thesis: use AI as your email
first-pass — triage, summarize, draft replies — and keep two rules unbroken:
never let it auto-send, never let it auto-delete. Companion to the existing
film `talk-to-your-tools` (referenced in B00; connectors are not re-taught).

Skill: show-tell (the assigned skill). One drawn image per beat, minimal
labels, Liam's narration explains.

Spine (show-tell): BIDEA hesitant writer -> BDEFS terms -> B00 the pile
-> B01 triage (what actually needs me) -> B02 the summary -> B03 the draft
-> B04 never auto-send -> B05 never auto-delete -> BHTF your-turn composer
-> BOUT spoken outro.

Run: python3 make_sheet.py  (writes beat_sheet.json)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "tame-your-inbox"
TITLE = "Tame your inbox"
WPM = 150  # Kokoro estimate used by the sibling builds


def est(narration):
    return round(len(narration.split()) / (WPM / 60), 1)


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": est(narration),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}


B = [
    beat("B00",
         "Meet the pile. Somewhere in here are a bill, a school note, and your boss "
         "\u2014 the three that matter. The rest is noise: newsletters, receipts, promos. "
         "And the pile grows faster than you can read it. This is the companion to our "
         "film on connecting Claude to your tools. That one was about the plug. This one "
         "is about what you do once it's in.",
         "B00_ThePile",
         "An open tray; email cards drop in one by one until the pile overflows; "
         "terracotta dots land on the three that matter. Label 'the pile' beside the tray.",
         [{"at": 0.1, "event": "tray + label land"},
          {"at": 0.35, "event": "cards drop in, pile grows"},
          {"at": 0.85, "event": "three terracotta dots land on the mattering cards"}]),
    beat("B01",
         "So hand the whole pile to Claude and ask one question: what actually needs me? "
         "It reads the lot and sorts the real from the noise \u2014 the bill and the boss "
         "in one stack, newsletters and receipts in the other. You read what matters, and "
         "you skip the rest.",
         "B01_Triage",
         "The tray with the pile; a scan line sweeps the pile; it splits into two stacks: "
         "'needs you' (ink lines) and 'noise' (dim lines); a terracotta check lands on "
         "'needs you'. Label 'triage'.",
         [{"at": 0.1, "event": "tray + pile land"},
          {"at": 0.3, "event": "scan line sweeps; pile splits into two stacks"},
          {"at": 0.7, "event": "check lands on 'needs you'"}]),
    beat("B02",
         "Next, the summary. Point it at a long thread \u2014 a dozen emails back and "
         "forth \u2014 and ask for the short version. You get three lines: what was "
         "decided, what's still open, what you owe someone. You walk into the meeting "
         "already knowing the story.",
         "B02_TheSummary",
         "A tall stack of pages (the long thread); kraft lines draw to a brief card that "
         "grows with three ink lines; three terracotta dots land. Label 'the summary'.",
         [{"at": 0.1, "event": "thread stack + label land"},
          {"at": 0.35, "event": "kraft lines draw; brief card grows with three lines"},
          {"at": 0.8, "event": "three terracotta dots land"}]),
    beat("B03",
         "Then the replies. For each email that needs one, it writes you a draft "
         "\u2014 in your voice, from the thread. Read it, fix what it got wrong, and only "
         "then hit send yourself. Because a draft is the AI guessing. A sent email is "
         "you acting.",
         "B03_TheDraft",
         "One email card; a draft card grows beside it with reply lines; an ink check "
         "lands. Label 'the draft'.",
         [{"at": 0.1, "event": "email card + label land"},
          {"at": 0.35, "event": "draft card grows with reply lines"},
          {"at": 0.75, "event": "ink check lands"}]),
    beat("B04",
         "Which is the first rule of this whole film. Never let it send on its own. If it "
         "replies to the wrong person, or promises something you never said, the damage "
         "is done in one click. A draft is reversible. A sent email mostly isn't. So the "
         "send button stays yours. Always.",
         "B04_NeverAutoSend",
         "The draft card; a big ink SEND pill lands beneath it; an ink lock lands over "
         "the pill. Label 'never auto-send' beside the card.",
         [{"at": 0.1, "event": "draft card + label land"},
          {"at": 0.55, "event": "SEND pill lands"},
          {"at": 0.85, "event": "lock lands over the pill"}]),
    beat("B05",
         "And the second rule, the one nobody tells you. Never let it delete on its own. "
         "The AI can't know which old email you'll need next year \u2014 the receipt for "
         "the warranty, the landlord's promise. Deleting is forever. So tell it to archive "
         "the noise instead, and empty the trash yourself.",
         "B05_NeverAutoDelete",
         "An email card hovers over a bin; an ink X stamps the bin (not the email); the "
         "card slides into an archive tray; a terracotta check stamps the tray. "
         "Label 'never auto-delete'.",
         [{"at": 0.1, "event": "bin + email card + label land"},
          {"at": 0.25, "event": "ink X stamps the bin"},
          {"at": 0.6, "event": "card slides into the archive tray"},
          {"at": 0.85, "event": "check stamps the tray"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
    remotion("BIDEA", "the question",
             "Ciao. This is Liam, in for Bear. Your inbox has hundreds of emails, and the "
             "three that matter are buried somewhere in the middle. The naive fix is to "
             "let the AI answer them all for you. But the better question is the one on "
             "screen.",
             "BrutalistHesitantWriter",
             {"text": "How do I get Claude to answer my emails",
              "triggerWords": "get Claude to answer my emails",
              "replacementWords": "use Claude as my email first-pass, safely",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
              "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'How do I get Claude to answer my emails'"},
              {"at": 0.6, "event": "backspaces 'get Claude to answer my emails' -> 'use Claude as my email first-pass, safely'"}],
             lead_silence_s=0.8,
             motion_claim="The writer types the naive auto-reply question and corrects it to the film's thesis: first-pass, safely.",
             qc={"sparse_by_design": True,
                 "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms. Inbox triage: sorting the pile into what needs you and what "
             "doesn't. A summary: the short version of a long thread. And a draft: a "
             "reply the AI writes that you send.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "inbox triage", "meaning": "sorting the pile into what needs you and what doesn't"},
                        {"term": "summary", "meaning": "the short version of a long thread"},
                        {"term": "draft", "meaning": "a reply the AI writes that you send"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'inbox triage' lands"}, {"at": 0.5, "event": "'summary' lands"},
              {"at": 0.78, "event": "'draft' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Read my unread emails from this week. Give me a one-line summary of each, "
             "and tell me which ones need a reply. Do not send, reply to, or delete anything.")
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Point Claude at your unread email \u2014 read-only \u2014 and paste "
    "this in: " + YT_PROMPT +
    " Then check two things yourself. One: open your sent folder \u2014 it should be "
    "empty. Two: skim one original email \u2014 did the summary get it right?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN", "segment": "Tame your inbox",
     "command": YT_PROMPT, "runningText": "paste this into Claude\u2026",
     "output": ["Check: did anything leave your inbox? Open your sent folder \u2014 it should be empty.",
                "Check: skim one original email \u2014 did the summary get it right?"],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
                 "minimal labels, with the voice carrying the explanation. The negative space is the style, "
                 "so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0,
          "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE + ".", "slug": SLUG,
                                          "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE \u00b7 AT WORK",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Italian (Ciao)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card "
                              "(Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like "
                              "tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; "
                              "spoken outro stays."),
    "audience": ("general audience \u2014 smart and pragmatic, not necessarily AI experts; "
                 "may never have pointed an AI at their inbox"),
    "source_doc": ("built from scratch 2026-10-05; no mirror source. Companion to the "
                   "talk-to-your-tools film (B00 references it; connectors are not re-taught). "
                   "No real people's names, no real company internals."),
    "playlist": "Getting started with Claude", "chapter_number": 0,
    "tags": ["email", "inbox", "triage", "summary", "draft replies", "safety",
             "Claude", "AI assistant", "Nik Bear Brown"]},
    "beats": B}

if __name__ == "__main__":
    beats = sheet["beats"]
    # --- identity & count ---
    assert len(beats) == 10, f"expected 10 beats, got {len(beats)}"
    ids = [b["beat_id"] for b in beats]
    assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05",
                   "BHTF", "BOUT"], ids
    # --- duration band (~3:00-5:00; brief allows 3-6 min) ---
    total = sum(b["estimated_duration_s"] for b in beats)
    assert 180 <= total <= 300, f"total {total}s outside 3:00-5:00 band"
    # --- voice: every beat must carry a valid Kokoro voice code ---
    VALID_VOICES = {"am_onyx"}
    for b in beats:
        v = b.get("voice")
        assert v in VALID_VOICES, f"{b['beat_id']}: invalid voice {v!r}"
    # --- manim beats carry a scene class named for the beat ---
    for b in beats:
        if b["lane"] == "manim":
            cls = b["shot"]["manim"]["class"]
            assert cls.startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class {cls}"
        assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    # --- BIDEA hesitant-writer mechanics ---
    idea = next(b for b in beats if b["beat_id"] == "BIDEA")
    p = idea["shot"]["remotion"]["props"]
    assert p["triggerWords"] in p["text"], "trigger not verbatim in text"
    assert not p["triggerWords"][-1] in ".?!,;:", "trigger ends in punctuation"
    assert not p["replacementWords"][-1] in ".?!,;:", "replacement ends in punctuation"
    # --- BDEFS term length (ClaudeDefinitions truncates past ~17 chars) ---
    defs = next(b for b in beats if b["beat_id"] == "BDEFS")
    for t in defs["shot"]["remotion"]["props"]["terms"]:
        assert len(t["term"]) <= 17, f"term too long: {t['term']}"
    # --- BHTF composer contract ---
    htf = next(b for b in beats if b["beat_id"] == "BHTF")
    hp = htf["shot"]["remotion"]["props"]
    assert "YOUR TURN" in hp["topic"], "topic must contain YOUR TURN"
    assert hp["greeting"] == "Your turn."
    assert len(hp["output"]) == 2, "two viewer checks"
    assert hp["command"] in htf["narration_text"], "prompt must be read in full"
    # --- BOUT outro contract ---
    out = next(b for b in beats if b["beat_id"] == "BOUT")
    assert out["kind"] == "outro_voice" and out["tail_silence_s"] == 1.0
    assert out["narration_text"].endswith("At Nik Bear Brown.")
    # --- bookends ---
    assert sheet["metadata"]["bookend_exempt"] == ["cold-open", "bvdt"]
    (HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
    print(f"beats={len(beats)} total={total:.1f}s (~{int(total//60)}m{int(total%60):02d}s)")
