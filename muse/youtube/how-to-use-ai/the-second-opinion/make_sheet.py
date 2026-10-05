#!/usr/bin/env python3
"""make_sheet.py — "The Second Opinion" (show-tell, general audience).

Source: NEW — built from scratch for the humanitarians AI YouTube channel
"How to AI" series. Skill: show-tell (switched from the assigned ai-explainer
for series consistency — see BUILD-LOG.md).

The argument: for a big decision, never stop at the first answer. Get a
second opinion — ask a second AI, or make one AI argue against itself
(steel-manning: the strongest version of the other side, stated fairly).
The second opinion doesn't hand you the answer; it hands you the whole
picture. You decide. Companion to make-it-check-its-own-work.

Run: python3 make_sheet.py   -> writes beat_sheet.json (13 beats).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "the-second-opinion"
TITLE = "The Second Opinion"

WPS = 2.5  # words per second (~150 wpm)


def est(narration):
    return round(len(narration.split()) / WPS, 1)


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim",
            "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": est(narration),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image,
                     "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


EM = "\u2014"  # em dash


B = [
 remotion("BIDEA", "the question",
  "Merhaba. This is Liam, in for Bear. For a small question, one answer from "
  "the AI is plenty. But for a big decision, one answer is never the whole "
  "story. Big decisions deserve a second opinion.",
  "BrutalistHesitantWriter",
  {"text": "One good answer\nneeds no second opinion.",
   "triggerWords": "needs no second opinion",
   "replacementWords": "deserves a second opinion",
   "fontSize": 70, "charSize": 22, "charMs": 22,
   "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2,
   "jitter": 20, "seed": "the-second-opinion", "banner": ""},
  [{"at": 0.0, "event": "types 'One good answer needs no second opinion.'"},
   {"at": 0.55, "event": "backspaces 'needs no second opinion' -> 'deserves a second opinion'"}],
  lead_silence_s=0.8,
  motion_claim="The writer types the naive take and corrects it to the film's claim: a good answer deserves a second opinion.",
  qc={"sparse_by_design": True,
      "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),

 remotion("BDEFS", "terms",
  "Three terms for this film. A second opinion: a fresh, independent take on "
  "the same question. Steel-manning: arguing the other side's case at its "
  "strongest, fairly stated. Devil's advocate: someone whose job is to argue "
  "against the plan " + EM + " once an actual Church office, and still a good job to "
  "give an AI.",
  "ClaudeDefinitions",
  {"title": "Terms In This Film",
   "terms": [
    {"term": "Second opinion",
     "def": "a fresh, independent take on the same question"},
    {"term": "Steel-manning",
     "def": "arguing the other side's case at its strongest, fairly"},
    {"term": "Devil's advocate",
     "def": "someone whose job is to argue against the plan"}],
   "durationSeconds": 21.2},
  [{"at": 0.0, "event": "title lands"},
   {"at": 0.2, "event": "term 1 lands"},
   {"at": 0.45, "event": "term 2 lands"},
   {"at": 0.7, "event": "term 3 lands"}]),

 beat("B00",
  "The move is simple. For a big decision, don't stop at the first answer "
  + EM + " get a second opinion. There are two ways to get one. Ask a second AI. "
  "Or make the first AI argue against itself. Either way, you end up holding "
  "both sides of the decision.",
  "B00_TheMove",
  "A question pill; the first answer card lands; the second answer card lands beside it; two route pills land beneath.",
  [{"at": 0.05, "event": "question pill 'A big decision?' lands"},
   {"at": 0.3, "event": "first answer card lands"},
   {"at": 0.55, "event": "second answer card lands beside it"},
   {"at": 0.8, "event": "route pills 'ask a second AI' / 'argue against itself' land"}]),

 beat("B01",
  "Route one: a second AI. A fresh brain that never saw the first answer "
  + EM + " it can't just agree politely, because it doesn't know what it's agreeing "
  "with. Route two: the steelman. One AI, told to build the strongest case "
  "against its own answer. Two routes, same payoff: both sides on the table.",
  "B01_TwoRoutes",
  "Two route cards land, one per spoken route; a 'both sides on the table' pill lands.",
  [{"at": 0.08, "event": "route card 'a second AI' lands on 'Route one'"},
   {"at": 0.45, "event": "route card 'the steelman' lands on 'Route two'"},
   {"at": 0.85, "event": "'both sides on the table' pill lands"}]),

 beat("B02",
  "Watch it on a real decision. The question: should I take the night-shift "
  "job? It pays more, but the hours are brutal. AI number one says: take it. "
  "The extra pay is real, and the overtime adds up. Confident. Done. And "
  "maybe it's right.",
  "B02_FirstAnswer",
  "The decision pill lands; the confident answer card lands; the check lands.",
  [{"at": 0.05, "event": "decision pill 'Night-shift job — take it?' lands"},
   {"at": 0.4, "event": "answer card 'Take it — the pay is real.' lands"},
   {"at": 0.85, "event": "check lands on 'Confident. Done.'"}]),

 beat("B03",
  "Now the second opinion. You write back: argue the other side at its "
  "strongest. And the AI builds the steelman " + EM + " the case against its own answer. "
  "Broken sleep. Health costs that don't show up in the paycheck. The long "
  "drive home half awake. Not a weak straw version " + EM + " the strongest version. "
  "That is what steel-manning means.",
  "B03_TheSteelman",
  "The first answer card returns; the critique prompt lands; the steelman card grows a terracotta rim; three cost pills pop, one per spoken cost.",
  [{"at": 0.05, "event": "the first answer card returns"},
   {"at": 0.25, "event": "prompt pill 'argue the other side at its strongest' lands"},
   {"at": 0.45, "event": "the steelman card grows with a terracotta rim"},
   {"at": 0.65, "event": "'broken sleep' pill pops"},
   {"at": 0.75, "event": "'health costs' pill pops"},
   {"at": 0.85, "event": "'the drive home' pill pops"}]),

 beat("B04",
  "Now hold both. The pay is real " + EM + " and so are the costs. The second opinion "
  "doesn't hand you the answer " + EM + " it hands you the whole picture. The AI can't "
  "live your life for you. You decide.",
  "B04_BothSides",
  "Two cards side by side — 'the pay is real' vs 'the costs are real'; the YOU pill lands beneath.",
  [{"at": 0.05, "event": "both cards land, 'vs' between them"},
   {"at": 0.7, "event": "the YOU pill lands on 'You decide'"}]),

 beat("B05",
  "Spend the second opinion where being wrong is expensive and hard to undo. "
  "A lease you sign. A job you leave for. A big purchase. A medical question "
  + EM + " which you still take to a real doctor. Dinner plans? One answer is plenty. "
  "Spend it where it costs.",
  "B05_WhereItPays",
  "Four icon cards — lease, job move, big purchase, medical — each stamped with a check as named; a 'dinner plans' pill gets the single-answer tag.",
  [{"at": 0.08, "event": "four icon cards land"},
   {"at": 0.35, "event": "check stamps lease"},
   {"at": 0.5, "event": "check stamps job move"},
   {"at": 0.65, "event": "check stamps big purchase"},
   {"at": 0.78, "event": "check stamps medical"},
   {"at": 0.9, "event": "'dinner plans — one answer is plenty' pill lands"}]),

 beat("B06",
  "The honest part. Two AIs can share the same blind spots " + EM + " same training, "
  "same gaps. And one AI arguing against itself still runs on the same brain. "
  "A second opinion widens the view. It is not the truth. And one rule: never "
  "shop around until some AI tells you what you wanted to hear. That's not a "
  "second opinion. That's a cheerleader.",
  "B06_TheLimit",
  "Two chat windows land; one shared 'same training' band links them; an opinion-shopping row lands and the glowing card takes a terracotta X.",
  [{"at": 0.05, "event": "two chat windows land"},
   {"at": 0.3, "event": "the 'same training' band links them"},
   {"at": 0.6, "event": "opinion-shopping row lands; one card glows"},
   {"at": 0.88, "event": "the glow dies; the terracotta X lands on 'cheerleader'"}]),

 beat("B07",
  "One upgrade. Never ask the second AI: do you agree? That only ever gets a "
  "nod. Give it a real job: steelman the opposite case. Or ask: what would "
  "change your answer? And keep the second take independent " + EM + " don't show it "
  "the first answer first, or it will just agree politely.",
  "B07_ProMove",
  "'Do you agree?' earns a dim nod; 'Steelman the opposite case.' pops three strong-argument flags; 'What would change your answer?' lands; a covered card is tagged 'keep it hidden'.",
  [{"at": 0.08, "event": "prompt pill 'Do you agree?' lands"},
   {"at": 0.3, "event": "the dim nod lands"},
   {"at": 0.5, "event": "prompt pill 'Steelman the opposite case.' lands"},
   {"at": 0.68, "event": "three strong-argument flags pop"},
   {"at": 0.82, "event": "prompt pill 'What would change your answer?' lands"},
   {"at": 0.92, "event": "the covered 'keep it hidden' card lands"}]),

 beat("B08",
  "So make it a reflex. A big decision comes up: get the first answer, get a "
  "second opinion, then decide yourself. Three steps instead of one. That is "
  "the whole habit.",
  "B08_TheHabit",
  "A chain draws: 'first answer' card, arrow, 'second opinion' card, arrow, YOU pill.",
  [{"at": 0.05, "event": "'first answer' card lands"},
   {"at": 0.35, "event": "arrow draws; 'second opinion' card lands"},
   {"at": 0.65, "event": "arrow draws; the YOU pill lands"},
   {"at": 0.9, "event": "the chain holds"}]),

 remotion("BHTF", "your turn",
  "Your turn. Paste this into Claude: Steelman the case against my plan: "
  "describe your decision. Give me the strongest argument for the other side, "
  "fairly stated. Then tell me what evidence would change your answer. Read "
  "the other side's case out loud to yourself " + EM + " if you can't state it fairly, "
  "you haven't understood it yet. Then you make the call, not the AI.",
  "ClaudeComposerAsk",
  {"greeting": "Your turn.",
   "topic": "HOW TO AI " + EM + " YOUR TURN",
   "segment": "The Second Opinion",
   "command": "Steelman the case against my plan: describe your decision. "
              "Give me the strongest argument for the other side, fairly "
              "stated. Then tell me what evidence would change your answer.",
   "runningText": "paste this into Claude" + EM,
   "output": ["you can state the other side's case fairly",
              "you make the final call, not the AI"]},
  [{"at": 0.0, "event": "Composer opens " + EM + " 'Your turn.'"},
   {"at": 0.1, "event": "the prompt types in full"},
   {"at": 0.8, "event": "two check lines land"}]),

 remotion("BOUT", "outro",
  "The Second Opinion. At Nik Bear Brown.",
  "ClaudeTitleOutro",
  {"title": "The Second Opinion", "slug": "the-second-opinion",
   "handle": "@NikBearBrown", "subline": ""},
  [{"at": 0.0, "event": "title restates; handle; mascot"}],
  kind="outro_voice", tail_silence_s=1.0),
]

SHEET = {
 "metadata": {
  "slug": SLUG, "title": TITLE, "topic": "HOW TO AI \u00b7 SECOND OPINIONS",
  "skill": "show-tell", "style_preset": "show-tell",
  "channel": "claude-liam", "persona": "Liam (in for Bear)",
  "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
  "clock": "narration", "palette": "claude", "register": "Teardown",
  "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
  "caption_policy": "none", "greeting_language": "Merhaba (Turkish)",
  "bookend_exempt": ["cold-open", "bvdt"],
  "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the "
   "hesitant writer + terms card, no verdict card; Your Turn is the Claude.ai "
   "composer; spoken outro stays.",
 },
 "beats": B,
}

# ═══════════════════════ self-assertions (the gate) ═══════════════════════
_body_ids = [f"B{i:02d}" for i in range(9)]
_scene_classes = ["B00_TheMove", "B01_TwoRoutes", "B02_FirstAnswer",
                  "B03_TheSteelman", "B04_BothSides", "B05_WhereItPays",
                  "B06_TheLimit", "B07_ProMove", "B08_TheHabit"]

assert len(B) == 13, f"expected 13 beats, got {len(B)}"
assert [b["beat_id"] for b in B] == ["BIDEA", "BDEFS"] + _body_ids + ["BHTF", "BOUT"]
assert len({b["beat_id"] for b in B}) == 13, "beat ids must be unique"

for b in B:
    assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    assert b["estimated_duration_s"] > 0, f"{b['beat_id']}: non-positive duration"
    assert b["voice"] == "am_onyx", f"{b['beat_id']}: voice must be am_onyx"
    assert b["engine"] == "kokoro", f"{b['beat_id']}: engine must be kokoro"
    assert b["shot"]["show"], f"{b['beat_id']}: missing show block"

for bid, cls in zip(_body_ids, _scene_classes):
    b = next(x for x in B if x["beat_id"] == bid)
    assert b["shot"]["manim"]["class"] == cls, f"{bid}: class mismatch"
    assert b["lane"] == "manim", f"{bid}: lane must be manim"

bidea = B[0]
assert bidea["lead_silence_s"] == 0.8, "BIDEA needs lead_silence_s 0.8"
assert bidea["shot"]["remotion"]["props"]["triggerWords"] in \
    bidea["shot"]["remotion"]["props"]["text"], "triggerWords must appear in text"

bdefs = next(x for x in B if x["beat_id"] == "BDEFS")
assert bdefs["shot"]["remotion"]["props"]["durationSeconds"] == \
    bdefs["estimated_duration_s"], "BDEFS durationSeconds must match narration"

bhtf = next(x for x in B if x["beat_id"] == "BHTF")
assert "YOUR TURN" in bhtf["shot"]["remotion"]["props"]["topic"], "BHTF topic needs YOUR TURN"
cmd = bhtf["shot"]["remotion"]["props"]["command"]
assert cmd in bhtf["narration_text"], "BHTF prompt must be read verbatim in narration"

bout = B[-1]
assert bout["kind"] == "outro_voice" and bout["tail_silence_s"] == 1.0

total = round(sum(b["estimated_duration_s"] for b in B), 1)
assert 150 <= total <= 240, f"total {total}s outside the 150-240 s band"

(HERE / "beat_sheet.json").write_text(json.dumps(SHEET, indent=1, ensure_ascii=False) + "\n")
print(f"wrote beat_sheet.json: 13 beats, {total} s")
