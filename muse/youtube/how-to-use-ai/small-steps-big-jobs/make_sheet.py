#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for small-steps-big-jobs.

SHOW-TELL (Bear, 2026-09-26): one drawn illustration per body beat, minimal
labels, Liam's narration carries the explanation. NEW film (no mirror
source): the habit of breaking a big job into small AI steps, dramatized
with a kitchen renovation — the giant prompt's mush vs. four checked steps
(budget, layout, materials, timeline) stacked into a plan.

Spine: BIDEA (hesitant writer) + BDEFS (terms card) bookends, 8 drawn body
beats (B00–B07), the Claude.ai composer Your Turn, and the spoken outro.
No cold open, no verdict card (bookend_exempt). No cards in the body: every
beat is a thing, a part, or a flow, so each passes the card test toward
"draw it" (reasons in SHOTLIST.md).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "small-steps-big-jobs"
TITLE = "Small steps, big jobs"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00",
      "Start with the whole job. One giant box: plan my entire kitchen renovation. It feels efficient. One prompt, one answer. That's the trap.",
      "B00_GiantBox",
      "One giant sealed box with terracotta tape drops onto the stage and settles; the label 'the whole job' sits beside it.",
      [{"at": 0.1, "event": "giant box drops in"}, {"at": 0.7, "event": "label"}]),
 beat("B01",
      "You send the giant prompt. Out comes a giant answer. Long, confident — and mush. Vague on the budget. Fuzzy on the layout. Wrong about what your kitchen even looks like. The AI has to guess at everything at once, and a guess that big can't be checked.",
      "B01_MushOut",
      "The box slides left; a big page comes out; a messy scribble draws across it; the label 'mush' sits beside it.",
      [{"at": 0.15, "event": "box slides left, page arrives"}, {"at": 0.5, "event": "scribble draws"}, {"at": 0.8, "event": "label"}]),
 beat("B02",
      "Here's why. A big job is really five small jobs wearing a trench coat: budget, layout, materials, the timeline, and your taste. Ask for all five at once, and the AI guesses at each one. The guesses never check each other, so the mistakes pile up quietly.",
      "B02_WhyFails",
      "The page fades; the box opens; five labeled step cards (budget, layout, materials, timeline, your taste) tumble out in a jumble.",
      [{"at": 0.15, "event": "box opens"}, {"at": 0.4, "event": "cards tumble out"}, {"at": 0.8, "event": "jumble settles"}]),
 beat("B03",
      "So don't. Ask for one small job at a time. Start with the part everything else depends on: the budget. One card, one question: what can we spend?",
      "B03_StepOne",
      "The jumble fades; one clean step card drops onto the center of the stage; the label 'step one: budget' sits beside it.",
      [{"at": 0.2, "event": "card drops in"}, {"at": 0.6, "event": "label"}]),
 beat("B04",
      "Then step two, built on step one. The layout has to fit the budget, so you hand the AI the number you just agreed. Now it isn't guessing anymore. It's designing inside your answer.",
      "B04_StepTwo",
      "The budget card stays; the layout card drops beside it; an arrow draws from budget to layout; the label 'built on step one' sits above.",
      [{"at": 0.15, "event": "layout card drops"}, {"at": 0.5, "event": "arrow draws"}, {"at": 0.8, "event": "label"}]),
 beat("B05",
      "Then materials, designed inside the layout you just locked. You hand the AI the floor plan, and it stops suggesting stone countertops for a kitchen that can't hold them. Small enough to check in one glance.",
      "B05_Materials",
      "The materials card drops beside the layout card; an arrow draws layout to materials; a check lands on the materials card.",
      [{"at": 0.15, "event": "materials card drops"}, {"at": 0.5, "event": "arrow draws"}, {"at": 0.8, "event": "check lands"}]),
 beat("B06",
      "And the timeline comes last, because only now do you know what's actually getting done. Each checked answer feeds the next prompt: budget into layout, layout into materials, materials into timeline. That handoff is the whole trick.",
      "B06_Timeline",
      "The timeline card drops beside the materials card; the arrow chain completes; a check lands on every card.",
      [{"at": 0.15, "event": "timeline card drops"}, {"at": 0.5, "event": "chain completes"}, {"at": 0.8, "event": "checks land"}]),
 beat("B07",
      "Same kitchen, same AI. On the left: the giant prompt's answer. Everything at once, nothing you can use. On the right: four small steps, each one checked, stacked into a plan. Small steps, big jobs.",
      "B07_SideBySide",
      "Left: the mush page returns with the label 'one giant prompt'. Right: the four checked cards stack neatly with the label 'small steps'.",
      [{"at": 0.2, "event": "mush page left"}, {"at": 0.5, "event": "cards stack right"}, {"at": 0.8, "event": "labels"}]),
 beat("B08",
      "Make it a habit. One job per prompt. If you can't check the answer in a glance, the step is too big — split it in half and go again. That's the whole method.",
      "B08_OneJob",
      "One big card lands on the stack: 'one job per prompt'; a check drops on it.",
      [{"at": 0.25, "event": "rule card lands"}, {"at": 0.7, "event": "check"}]),
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
    "Hallo. This is Liam, in for Bear. A friend of mine asked an AI to plan her whole kitchen renovation in one giant prompt. What came back was long, confident — and completely unusable. Here's the small fix that changed everything.",
    "BrutalistHesitantWriter",
    {"text": "Plan my whole kitchen renovation!", "triggerWords": "Plan my whole kitchen renovation",
     "replacementWords": "Break my kitchen renovation into small steps",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Plan my whole kitchen renovation!'"},
     {"at": 0.6, "event": "backspaces the trigger and types 'Break my kitchen renovation into small steps!' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive giant-prompt question and corrects it into the film's method: small steps.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. A prompt: what you type to the AI. A step: one small job the AI does for you. And context: what the AI carries from one step into the next. That's all you need for this film.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "prompt", "meaning": "what you type to the AI"},
               {"term": "step", "meaning": "one small job the AI does for you"},
               {"term": "context", "meaning": "what the AI carries from one step into the next"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'prompt' lands"}, {"at": 0.5, "event": "'step' lands"}, {"at": 0.78, "event": "'context' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]
YT_PROMPT = ("I want to renovate my kitchen. Don't plan it all yet. First, ask me every question you need answered "
             "to set a realistic budget, then wait for my replies.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Does the AI ask questions instead of giving you an answer? And does anything about layout or materials sneak "
    "into its reply? If it does, split that off as the next step.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Your First Small Step", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: the AI asks questions instead of answering.", "Check: no layout or materials sneak in."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Sonnet", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"},
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · HOW TO AI", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "English-adjacent (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience, not AI experts",
    "source_doc": "NEW — built from scratch from the series brief (2026-10-03); no mirror source",
    "playlist": "How to AI", "chapter_number": 11,
    "tags": ["AI", "prompts", "how to AI", "task breakdown", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

n_beats = len(B)
n_body = sum(1 for b in B if b["lane"] == "manim")
total = round(sum(b["estimated_duration_s"] for b in B))
assert n_beats == 13, f"expected 13 beats, got {n_beats}"
assert n_body == 9, f"expected 9 body beats, got {n_body}"
assert 150 <= total <= 360, f"total {total}s outside the 2.5–6 min band"
manim_beats = [b["beat_id"] for b in B if b["lane"] == "manim"]
assert manim_beats == [f"B0{i}" for i in range(9)], f"body beat ids off: {manim_beats}"
print(n_beats, "beats;", n_body, "body;", "est", total, "s")
