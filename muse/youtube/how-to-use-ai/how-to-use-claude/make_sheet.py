#!/usr/bin/env python3
"""make_sheet.py — How to Use Claude (show-tell, Liam, Teardown).

Rebuild of claude/claude-youtube/claude-liam-how-to-use-claude for the
humanitarians AI YouTube channel, general audience (may never have used an AI
chat tool). Central claim kept from the source: Claude's output quality scales
with CONTEXT, not prompt templates. The fix: Projects. The strengths:
artifacts, analysis, rewriting. The catch: check important facts.

Spine (show-tell): BIDEA hesitant writer -> BDEFS terms -> B00 hero (chat
window) -> B01 what it is (model behind) -> B02 the failure (search-engine
habit) -> B03 the mechanism (context in, better answer out) -> B04 the fix
(Projects) -> B05/B06/B07 the three strengths -> B08 the catch (check it) ->
BHTF your-turn composer -> BOUT spoken outro.

Run: python3 make_sheet.py  (writes beat_sheet.json)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "how-to-use-claude"
TITLE = "How to Use Claude"
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
         "Start with what you see. Claude is a chat window in your browser. "
         "You type at the bottom; the answer appears above \u2014 as simple as texting a friend.",
         "B00_ChatWindow",
         "A Claude chat window drops onto the stage; the word 'chat window' beside it. "
         "A cursor lands in the composer; two reply lines appear above it.",
         [{"at": 0.1, "event": "window drops in"}, {"at": 0.4, "event": "cursor in the composer"},
          {"at": 0.55, "event": "reply lines above"}]),
    beat("B01",
         "Behind that window sits a model \u2014 an AI program trained on a huge library of writing, "
         "so it can answer questions well. The window is how you talk to it. The model is what answers.",
         "B01_ModelBehind",
         "The window shifts right; a dark model block rises behind it and three lights come on. "
         "Label 'model' beside the block.",
         [{"at": 0.1, "event": "model block rises behind the window"}, {"at": 0.45, "event": "lights come on"}]),
    beat("B02",
         "Most people use it like a search engine. One question, one answer, close the tab. "
         "But Claude knows nothing about your project, your constraints, or what you already tried. "
         "So it answers a stranger \u2014 and the answer is generic.",
         "B02_Stranger",
         "A question bubble lands in the composer; a thin two-line reply appears. "
         "The window fades (tab closed); the thin reply stays, labelled 'a stranger'.",
         [{"at": 0.15, "event": "question bubble"}, {"at": 0.3, "event": "thin reply"},
          {"at": 0.45, "event": "window closes"}, {"at": 0.7, "event": "'a stranger' lands"}]),
    beat("B03",
         "Here is the one idea. Claude's answer is only as good as what it can see. "
         "Give it your project, your constraints, and an example of what good looks like \u2014 "
         "and its first draft lands close to your last draft. More context, fewer revision rounds.",
         "B03_ContextIn",
         "Three context cards (project, constraints, example) drop into the window one by one. "
         "The reply card grows from thin to full. Labels 'context' and 'answer'.",
         [{"at": 0.15, "event": "context cards drop in"}, {"at": 0.75, "event": "reply grows full"}]),
    beat("B04",
         "Projects fix this. In Claude, open a Project for the thing you are working on \u2014 "
         "a report, a garden plan, a job application. Drop in your style, your constraints, "
         "and an example you like. Do it once: every chat inside that Project starts already knowing.",
         "B04_Project",
         "An open project box; three cards labelled style, rules, example drop in. "
         "A message rides through and an informed reply comes out. Label 'project' beside the box.",
         [{"at": 0.1, "event": "project box opens"}, {"at": 0.55, "event": "style, rules, example drop in"},
          {"at": 0.85, "event": "chat rides through, informed reply out"}]),
    beat("B05",
         "First strength: artifacts. When the answer should be a finished piece \u2014 a document, "
         "a chart, a small program \u2014 Claude builds it in a panel beside the chat. "
         "Not text to copy. A thing you can use.",
         "B05_Artifact",
         "The chat window; a side panel grows beside it holding a finished document page. "
         "Label 'artifact' beside the panel.",
         [{"at": 0.2, "event": "side panel grows"}, {"at": 0.5, "event": "finished page inside"}]),
    beat("B06",
         "Second: analysis. Hand it something long \u2014 a report, a contract, a pile of notes \u2014 "
         "and it maps the structure first, before you say what to change. Your questions get sharper, "
         "because you can see the shape of the thing.",
         "B06_Analysis",
         "A stack of long pages; a scan line sweeps down them; a structure map of three section "
         "blocks appears beside. Label 'analysis'.",
         [{"at": 0.15, "event": "page stack"}, {"at": 0.3, "event": "scan sweep"},
          {"at": 0.8, "event": "structure map"}]),
    beat("B07",
         "Third: rewriting. Give it your rough draft and one example of the voice you want. "
         "It hits the tone on the first pass \u2014 and you spend your time on ideas, not phrasing.",
         "B07_Rewrite",
         "A rough-draft card and a 'your voice' example card feed in; a polished page grows with a check. "
         "Labels 'rough draft' and 'your voice'.",
         [{"at": 0.1, "event": "rough draft"}, {"at": 0.3, "event": "'your voice' example"},
          {"at": 0.75, "event": "polished page + check"}]),
    beat("B08",
         "One warning. When Claude does not know something, it can still answer confidently. "
         "So treat important facts like a first draft: check them against a source you trust.",
         "B08_CheckIt",
         "A reply bubble holds one factual claim; a large check stamps onto it. Label 'check it'.",
         [{"at": 0.15, "event": "claim bubble"}, {"at": 0.8, "event": "check stamps on"}]),
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
             "Hallo. This is Liam, in for Bear. If you have never used an AI chat tool, start here. "
             "Most advice says: write a better prompt. But the better question is the one on screen.",
             "BrutalistHesitantWriter",
             {"text": "What is the one prompt\nthat makes Claude work",
              "triggerWords": "one prompt", "replacementWords": "context",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
              "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types 'What is the one prompt'"},
              {"at": 0.6, "event": "backspaces 'one prompt' -> 'context' on the spoken correction"}],
             lead_silence_s=0.8,
             motion_claim="The writer types the naive prompt question and corrects it to the film's thesis: context.",
             qc={"sparse_by_design": True,
                 "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms. A prompt: what you type into the chat. Context: everything Claude can see "
             "about your work \u2014 your project, your constraints, your examples. And a model: "
             "the AI program behind the chat, trained to answer questions well.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [{"term": "prompt", "meaning": "what you type into the chat"},
                        {"term": "context", "meaning": "everything Claude can see about your work"},
                        {"term": "model", "meaning": "the AI program behind the chat"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'prompt' lands"}, {"at": 0.5, "event": "'context' lands"},
              {"at": 0.78, "event": "'model' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("I'm starting [describe your project in one sentence]. My main constraint is [constraint]. "
             "What is the first question you need answered before you can actually help me?")
YOURTURN = remotion(
    "BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT +
    " Then check two things yourself. One: does its question point at something you haven't told it yet? "
    "Answer it \u2014 that is the context it wanted. Two: does its next answer fit your constraint? If not, say so.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN", "segment": "How to Use Claude",
     "command": YT_PROMPT, "runningText": "paste this into Claude\u2026",
     "output": ["Check: does its question point at something you haven't told it yet? Answer it.",
                "Check: does its next answer fit your constraint? If not, say so."],
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE \u00b7 GETTING STARTED",
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
                 "may never have used an AI chat tool"),
    "source_doc": ("claude/claude-youtube/claude-liam-how-to-use-claude/beat_sheet.json "
                   "(mirror repo nikbearbrown/humanitarians-youtube-muse); rebuilt 2026-10-03 for Liam/Teardown"),
    "playlist": "Getting started with Claude", "chapter_number": 0,
    "tags": ["How to use Claude", "Claude", "AI chat", "getting started", "Claude Projects",
             "Claude artifacts", "Nik Bear Brown"]},
    "beats": B}

if __name__ == "__main__":
    beats = sheet["beats"]
    # --- identity & count ---
    assert len(beats) == 13, f"expected 13 beats, got {len(beats)}"
    ids = [b["beat_id"] for b in beats]
    assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08",
                   "BHTF", "BOUT"], ids
    # --- duration band (3:00-3:40) ---
    total = sum(b["estimated_duration_s"] for b in beats)
    assert 180 <= total <= 220, f"total {total}s outside 3:00-3:40 band"
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
