#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for the-long-game.

SHOW-TELL (Bear, 2026-09-26): one drawn illustration per body beat, minimal
labels, Liam's narration carries the explanation. NEW film (no mirror
source): the long-document habit — outline first, then sections one at a
time, then stitching — dramatized with a twenty-page grant proposal.
Companion to small-steps-big-jobs (film 11): that film breaks a big job
into steps; this one keeps a long document from falling apart.

Spine: BIDEA (hesitant writer) + BDEFS (terms card) bookends, 9 drawn body
beats (B00–B08), the Claude.ai composer Your Turn, and the spoken outro.
No cold open, no verdict card (bookend_exempt). No cards in the body: every
beat is a thing, a part, or a flow, so each passes the card test toward
"draw it" (reasons in SHOTLIST.md).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "the-long-game"
TITLE = "The long game"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00",
      "Start with the goal. A twenty-page grant proposal: the need, the plan, the budget, the team \u2014 one document that reads like one person wrote it. That is the long game.",
      "B00_Stack",
      "A tall stack of pages drops onto the stage and settles; a title line draws on the top page; the label 'the goal' sits beside it.",
      [{"at": 0.1, "event": "stack drops in"}, {"at": 0.4, "event": "label"}, {"at": 0.7, "event": "title line draws"}]),
 beat("B01",
      "So she asked for the whole thing in one prompt. Out came twenty pages in thirty seconds \u2014 and the middle repeated the beginning, page twelve contradicted page three, and the tone wandered off. Written all at once, a long document drifts.",
      "B01_AllAtOnce",
      "The neat stack bursts into five scattered pages; the label 'all at once' lands; terracotta dots flag the repeated pair and the contradicted page.",
      [{"at": 0.1, "event": "stack bursts into scattered pages"}, {"at": 0.35, "event": "label"}, {"at": 0.55, "event": "repeat dots"}, {"at": 0.7, "event": "contradiction dot"}]),
 beat("B02",
      "Here\u2019s why. Nobody can keep twenty pages straight in one pass \u2014 not even an AI. By page fourteen it has forgotten page three. Facts drift, sections repeat, the tone wobbles. A long document is really five short ones stapled together. So write it that way.",
      "B02_Drift",
      "Three pages in a row, numbered 3, 9, 14; the label 'it drifts'; repeat dots on page 9, a changed-fact dot on page 14; a staple draws across them.",
      [{"at": 0.1, "event": "three pages land"}, {"at": 0.25, "event": "numbers and label"}, {"at": 0.55, "event": "drift dots"}, {"at": 0.8, "event": "staple draws"}]),
 beat("B03",
      "Move one: the outline. Before any prose, ask the AI for a section-by-section skeleton \u2014 every part, in order. Then you do the most important job in this film: read it, fix it, approve it. The outline is the contract.",
      "B03_Outline",
      "The drift pages fade; the outline card lands; its four section rows draw in; a terracotta check stamps your approval; the label 'move one: outline'.",
      [{"at": 0.1, "event": "outline card lands"}, {"at": 0.35, "event": "section rows draw"}, {"at": 0.8, "event": "approval check"}, {"at": 0.9, "event": "label"}]),
 beat("B04",
      "Move two: one section at a time. The AI writes section one \u2014 only section one \u2014 with the outline beside it. Small enough to check in one sitting, because you read it before the next one starts.",
      "B04_SectionOne",
      "The outline card slides left; the section-one page drops in; an arrow draws card to page; the label 'move two: sections'; a check lands on the page.",
      [{"at": 0.1, "event": "card slides left, page drops"}, {"at": 0.3, "event": "arrow draws, label"}, {"at": 0.7, "event": "check lands"}]),
 beat("B05",
      "Move three is the handoff. Section two gets the outline plus section one, so the facts stay consistent. Each section carries what the last one said. That is what keeps page fourteen agreeing with page three.",
      "B05_Handoff",
      "Section two drops below section one; one arrow draws outline to section two, another section one to section two; a check and the label 'move three: the handoff'.",
      [{"at": 0.1, "event": "section two drops"}, {"at": 0.25, "event": "outline arrow"}, {"at": 0.35, "event": "handoff arrow"}, {"at": 0.8, "event": "check and label"}]),
 beat("B06",
      "Then the stitching. Read the whole thing end to end \u2014 out loud if you can \u2014 and fix only the seams: the transitions, a repeated sentence, a tone that shifts. You are not rewriting. You are making five sections read like one document.",
      "B06_Stitching",
      "Three numbered sections line up; a terracotta scan line sweeps down them; the repeated line lifts out and fades; the label 'the stitching'.",
      [{"at": 0.1, "event": "sections line up"}, {"at": 0.25, "event": "scan line sweeps"}, {"at": 0.45, "event": "repeated line lifts out"}, {"at": 0.75, "event": "label"}]),
 beat("B07",
      "Same proposal, same AI. On the left: the one-prompt version \u2014 twenty pages that fall apart. On the right: outline first, sections one at a time, stitched at the end. A document that holds together.",
      "B07_SideBySide",
      "Left: the scattered pages return with the label 'one giant prompt'. Right: a neat checked stack with the label 'the long game'.",
      [{"at": 0.1, "event": "jumble left"}, {"at": 0.25, "event": "left label"}, {"at": 0.55, "event": "neat stack right"}, {"at": 0.9, "event": "right label"}]),
 beat("B08",
      "Make it a habit. Outline first. One section per prompt. Stitch at the end. Anything longer than you can check in one sitting is a long game \u2014 play it in three moves.",
      "B08_Habit",
      "One big card lands: 'outline first' / 'one section per prompt' / 'stitch at the end'; a check drops on it.",
      [{"at": 0.15, "event": "rule card lands"}, {"at": 0.3, "event": "row one"}, {"at": 0.45, "event": "row two"}, {"at": 0.6, "event": "row three"}, {"at": 0.9, "event": "check"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. A colleague of mine asked an AI to write her whole twenty-page grant proposal in one prompt. What came back looked finished \u2014 and fell apart the moment she read it. Here\u2019s the three-part method that holds a long document together.",
    "BrutalistHesitantWriter",
    {"text": "Write our twenty-page grant proposal.", "triggerWords": "Write our twenty-page grant proposal",
     "replacementWords": "Help me outline our grant proposal first",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Write our twenty-page grant proposal.'"},
     {"at": 0.6, "event": "backspaces the trigger and types 'Help me outline our grant proposal first.' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive write-it-all-at-once question and corrects it into the film's method: outline first.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. An outline: the skeleton of the document, every part in order. A section: one chapter\u2019s worth. And a stitch: reading it as one piece and fixing the seams. That\u2019s all you need for this film.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "outline", "meaning": "the skeleton of the document, every part in order"},
               {"term": "section", "meaning": "one chapter\u2019s worth of the document"},
               {"term": "stitch", "meaning": "reading it as one piece, fixing the seams"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'outline' lands"}, {"at": 0.5, "event": "'section' lands"}, {"at": 0.78, "event": "'stitch' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]
YT_PROMPT = ("I\u2019m writing a twenty-page grant proposal for a community food bank. Don\u2019t write any of it yet. "
             "First, draft a detailed section-by-section outline, then wait for my approval.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Does the AI give you an outline instead of prose? And is every part of the proposal on it \u2014 "
    "nothing missing, nothing extra?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN", "segment": "Your First Outline", "command": YT_PROMPT,
     "runningText": "paste this into Claude\u2026",
     "output": ["Check: the AI gives you an outline, not prose.", "Check: every part is on it \u2014 nothing missing, nothing extra."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Sonnet", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, with the voice carrying the explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 5.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE \u00b7 HOW TO AI", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "English-adjacent (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience, not AI experts",
    "source_doc": "NEW \u2014 built from scratch from the series brief (2026-10-04); no mirror source",
    "playlist": "How to AI",
    "companion_to": "small-steps-big-jobs",
    "tags": ["AI", "prompts", "how to AI", "long documents", "outlining", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

n_beats = len(B)
n_body = sum(1 for b in B if b["lane"] == "manim")
total = round(sum(b["estimated_duration_s"] for b in B))
assert n_beats == 13, f"expected 13 beats, got {n_beats}"
assert n_body == 9, f"expected 9 body beats, got {n_body}"
assert 150 <= total <= 360, f"total {total}s outside the 2.5\u20136 min band"
manim_beats = [b["beat_id"] for b in B if b["lane"] == "manim"]
assert manim_beats == [f"B0{i}" for i in range(9)], f"body beat ids off: {manim_beats}"
print(n_beats, "beats;", n_body, "body;", "est", total, "s")
