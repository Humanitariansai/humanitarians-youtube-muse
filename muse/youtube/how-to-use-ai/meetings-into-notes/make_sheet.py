#!/usr/bin/env python3
"""make_sheet.py — Meetings into Notes (show-tell, Liam, Teardown).

Built from scratch 2026-10-03 for the humanitarians AI YouTube channel, general
audience (smart, pragmatic, not AI experts). Thesis: paste the mess (a meeting
transcript or rough notes) and get back the meaning — a 3-bullet summary, the
decisions with owners, and what was left unresolved. Three exact prompts, one
fictional example (Maya / Sam), one follow-up beat, one privacy line
(film #20 covers privacy in depth).

Spine (show-tell): BIDEA hesitant writer -> BDEFS terms -> B00 the pain
(rambling meeting) -> B01 paste it -> B02 rough notes are fine -> B03 prompt 1
(3 bullets) -> B04 prompt 2 (decisions + owners) -> B05 prompt 3 (unresolved)
-> B06 the fictional example end-to-end -> B07 keep asking -> B08 the privacy
line -> BHTF your-turn composer -> BOUT spoken outro.

Run: python3 make_sheet.py  (writes beat_sheet.json)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "meetings-into-notes"
TITLE = "Meetings into Notes"
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
         "Meetings are where decisions go to hide. Ninety minutes, eight people, four tangents "
         "about the coffee machine \u2014 and somewhere in there, a real decision about the launch "
         "date. Nobody writes it down. By Friday, three people remember three different versions.",
         "B00_RamblingMeeting",
         "A long messy transcript page drops onto the stage, lines tangled; three small bubbles land "
         "above it, each remembering a different date. Label 'the meeting' beside the page.",
         [{"at": 0.1, "event": "transcript page drops in"}, {"at": 0.3, "event": "tangled lines draw"},
          {"at": 0.75, "event": "three date bubbles land"}]),
    beat("B01",
         "The fix is simple. Paste the transcript \u2014 or your rough notes \u2014 into Claude. "
         "You hand it the mess; it hands back the meaning. No formatting, no clean-up needed first.",
         "B01_PasteIt",
         "The transcript page slides into the chat window's composer; a reply card grows beside it "
         "with a terracotta check. Labels 'mess in' and 'notes out'.",
         [{"at": 0.1, "event": "page slides into the composer"}, {"at": 0.7, "event": "reply card grows + check"}]),
    beat("B02",
         "And you do not need a perfect transcript. Your video-call app probably transcribes for you "
         "already. Your own rough notes work too \u2014 paste the fragments as they are. "
         "Claude reads the sense, not the formatting.",
         "B02_RoughNotes",
         "Three fragment cards ('launch??', 'Sam \u2014 paymt', 'release notes?') drop into the composer "
         "as-is; a check lands on the composer. Label 'rough notes' beside them.",
         [{"at": 0.15, "event": "fragment cards drop in"}, {"at": 0.8, "event": "check lands on the composer"}]),
    beat("B03",
         "The first prompt is: summarize this meeting in 3 bullets. Three, not ten \u2014 the limit "
         "forces it to pick what mattered. What you get is the whole meeting in about thirty seconds.",
         "B03_ThreeBullets",
         "The exact prompt sits in the composer; a reply grows with three bullet lines and terracotta "
         "dots. Label 'summarize' beside the reply.",
         [{"at": 0.1, "event": "prompt in the composer"}, {"at": 0.35, "event": "three-bullet reply grows"}]),
    beat("B04",
         "The second prompt is: list every decision and who owns the next step. This is the one that "
         "matters most. Meetings feel productive because people talked. This prompt asks the "
         "uncomfortable question: who actually does what.",
         "B04_DecisionsOwners",
         "The exact prompt lands in the composer in two lines; a reply card grows with two decision rows, "
         "each with an owner pill ('Maya', 'Sam'). Label 'owners' beside the reply.",
         [{"at": 0.1, "event": "prompt in two lines"}, {"at": 0.75, "event": "decision rows + owner pills"}]),
    beat("B05",
         "The third prompt is the one most people skip: what was left unresolved? Every meeting leaves "
         "loose ends \u2014 the question nobody answered, the thing everyone nodded at but nobody owns. "
         "This prompt hunts them down.",
         "B05_Unresolved",
         "Two loose-end cards drop in; ink '?' marks land on them. Label 'unresolved' beside the cards.",
         [{"at": 0.15, "event": "loose-end cards drop"}, {"at": 0.35, "event": "'?' marks land"}]),
    beat("B06",
         "Watch it work. Maya moves the launch to Friday, Sam owns the payment fix, and nobody decides "
         "who writes the release notes. Transcript in \u2014 summary, decisions, three action items out. "
         "And one unresolved question: who writes the release notes?",
         "B06_Example",
         "The transcript page lands; three output cards spring out of the window beside it: summary, "
         "decisions, action items. Label 'example' beside the window.",
         [{"at": 0.1, "event": "transcript page lands"}, {"at": 0.7, "event": "three output cards spring out"}]),
    beat("B07",
         "The notes are not the end. Keep asking. Draft the follow-up email to the team. Or: what should "
         "I prepare before next week's check-in? The transcript is now a document you can question.",
         "B07_KeepAsking",
         "The chat window; a follow-up question lands in the composer; an email card grows beside the "
         "window. Label 'keep asking'.",
         [{"at": 0.1, "event": "follow-up question in the composer"}, {"at": 0.75, "event": "email card grows"}]),
    beat("B08",
         "One line of caution. Check your workplace rules before pasting an internal meeting into a "
         "public AI. If the rules say no, use your rough notes instead of the transcript.",
         "B08_CheckRules",
         "The transcript page drops; an ink lock lands over it. Label 'check your rules' beside the page.",
         [{"at": 0.1, "event": "transcript page drops"}, {"at": 0.8, "event": "lock lands over it"}]),
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
             "Hallo. This is Liam, in for Bear. You leave a meeting with a notebook full of half-sentences, "
             "and three days later you cannot tell what anyone agreed to. The naive fix is to take better "
             "notes. But the better question is the one on screen.",
             "BrutalistHesitantWriter",
             {"text": "How do I take better meeting notes",
              "triggerWords": "take better meeting notes",
              "replacementWords": "get Claude to turn the meeting into notes",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
              "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'How do I take better meeting notes'"},
              {"at": 0.6, "event": "backspaces 'take better meeting notes' -> 'get Claude to turn the meeting into notes'"}],
             lead_silence_s=0.8,
             motion_claim="The writer types the naive notes question and corrects it to the film's thesis: Claude turns the meeting into notes.",
             qc={"sparse_by_design": True,
                 "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms. A transcript: the written record of what was said. A summary: the short version "
             "\u2014 what mattered. An action item: one task, one owner, one deadline.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "transcript", "meaning": "the written record of what was said"},
                        {"term": "summary", "meaning": "the short version \u2014 what mattered"},
                        {"term": "action item", "meaning": "one task, one owner, one deadline"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'transcript' lands"}, {"at": 0.5, "event": "'summary' lands"},
              {"at": 0.78, "event": "'action item' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is the meeting transcript, pasted below. Give me three things: "
             "1. a three-bullet summary. 2. every decision and who owns the next step. "
             "3. what was left unresolved.")
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT +
    " Then check two things yourself. One: does every action item have a named owner? "
    "If one just says the team, ask Claude: who? Two: does the summary stay short? "
    "If it wanders, say: shorter.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN", "segment": "Meetings into Notes",
     "command": YT_PROMPT, "runningText": "paste this into Claude\u2026",
     "output": ["Check: does every action item have a named owner? If one just says the team, ask Claude: who?",
                "Check: does the summary stay short? If it wanders, say: shorter."],
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
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card "
                              "(Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like "
                              "tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; "
                              "spoken outro stays."),
    "audience": ("general audience \u2014 smart and pragmatic, not necessarily AI experts; "
                 "may never have pasted anything into an AI chat tool"),
    "source_doc": ("built from scratch 2026-10-03; no mirror source. Fictional example "
                   "(Maya / Sam); no real people's names, no real company internals."),
    "playlist": "Getting started with Claude", "chapter_number": 0,
    "tags": ["meetings", "meeting notes", "Claude", "AI assistant", "productivity",
             "action items", "Nik Bear Brown"]},
    "beats": B}

if __name__ == "__main__":
    beats = sheet["beats"]
    # --- identity & count ---
    assert len(beats) == 13, f"expected 13 beats, got {len(beats)}"
    ids = [b["beat_id"] for b in beats]
    assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05", "B06", "B07",
                   "B08", "BHTF", "BOUT"], ids
    # --- duration band (~3:00-3:30, brief allows 3-6 min) ---
    total = sum(b["estimated_duration_s"] for b in beats)
    assert 165 <= total <= 210, f"total {total}s outside 2:45-3:30 band"
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
