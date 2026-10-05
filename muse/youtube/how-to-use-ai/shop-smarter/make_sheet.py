#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Shop smarter" (film 43 of the How-to-AI series).

SHOW-TELL (Bear, 2026-09-26): one drawn illustration per beat, minimal labels,
Liam's narration (Kokoro am_onyx) carries the explanation. No composer cold
open, no verdict card (bookend_exempt); spoken @NikBearBrown outro stays.

Premise: AI as buying co-pilot. The film teaches the comparison METHOD, not
brand picks: start with your own priorities, ask for a side-by-side table,
ask the trade-off question (what would I give up), summarize review patterns
instead of trusting star averages, and paste the fine print to hunt money
traps. One honest limit: the AI doesn't know today's price — always check the
live price yourself. No specific product endorsements; no pricing tiers quoted.
Source: built from scratch (NEW). Facts verified 2026-10-05 (see FACTCHECK.md).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "shop-smarter"
TITLE = "Shop smarter"

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

B = [
 beat("B00", "Shopping is comparing. Three options on the table — same job, different strengths, different weaknesses. The question is never which is the best one. The question is: best for what?",
      "B00_ThreeOptions", "Three kraft option boxes in a row on the table, labelled A, B, C; the same cast of boxes the film keeps throughout.",
      [{"at": 0.1, "event": "boxes land left to right"}, {"at": 0.5, "event": "labels 'A', 'B', 'C' land beneath with leader lines"}]),
 beat("B01", "So start with yourself, not the products. Tell the AI what matters: who it's for, how you'll use it, what would make you regret the buy. The AI doesn't know your life. Your priorities are the ruler everything else gets measured against.",
      "B01_Priorities", "A 'you' head on the left hands a priority card to the AI panel on the right; the card slides across and a terracotta dot lands on it.",
      [{"at": 0.1, "event": "head + panel + card land, 'you' and 'AI' labels"}, {"at": 0.5, "event": "card slides to the panel; terracotta dot lands"}]),
 beat("B02", "Now ask for a table. Name the options and your criteria, and say: lay these out side by side, one row per criterion. A table turns a fog of opinions into something your eyes can actually compare.",
      "B02_TheTable", "An ink comparison grid draws: three columns headed A, B, C; row guides; the label 'side by side' sits beneath.",
      [{"at": 0.1, "event": "grid lines draw"}, {"at": 0.5, "event": "column headers A, B, C land; label lands"}]),
 beat("B03", "Then ask the question most shoppers skip: for each option, what would I be giving up? Don't ask which is best — ask what each one costs you. The right choice is usually the one whose downside you mind the least.",
      "B03_Tradeoffs", "The same table stays on stage; a terracotta ellipse rings the trade-off row and an ink check lands on the least-bad cell.",
      [{"at": 0.1, "event": "table fades in (continuity from B02)"}, {"at": 0.4, "event": "terracotta ellipse rings the trade-off row"}, {"at": 0.65, "event": "ink check lands; label 'trade-off'"}]),
 beat("B04", "Next, the reviews. Nobody can read four thousand of them, and the star average lies — some reviews are bought, some are written by people who never bought the thing. Ask the AI: read the reviews and tell me what the unhappy buyers agree on. Patterns, not stars.",
      "B04_ReviewFunnel", "Five small review pages above funnel down to one summary page; a terracotta check lands on the summary.",
      [{"at": 0.1, "event": "five review pages land"}, {"at": 0.4, "event": "funnel lines draw; summary page grows"}, {"at": 0.7, "event": "check lands; label 'patterns'"}]),
 beat("B05", "Then the fine print — the trap-hunting step. Paste the return policy, the warranty, the subscription terms into the chat and ask: what's the catch here? A ten-thousand-word contract becomes three warnings you can actually act on.",
      "B05_FinePrint", "A tall contract page of tiny ghost lines; a magnifier lands on one clause and a terracotta ellipse rings it; label 'the catch'.",
      [{"at": 0.1, "event": "contract page lands"}, {"at": 0.45, "event": "magnifier lands"}, {"at": 0.65, "event": "terracotta ellipse rings the clause"}]),
 beat("B06", "Ask about the money traps by name. Does the warranty cover what actually breaks? Can you return it, and who pays the shipping? Does anything auto-renew after a trial? The traps are never in the headline. They're in paragraph nine.",
      "B06_MoneyTraps", "Three mini trap cards — 'warranty', 'returns', 'renew' — each stamped with a terracotta X; the label 'paragraph nine' sits below.",
      [{"at": 0.1, "event": "three trap cards land"}, {"at": 0.5, "event": "terracotta X stamps each card"}, {"at": 0.7, "event": "label 'paragraph nine' lands"}]),
 beat("B07", "One honest limit: the AI doesn't know today's price. Prices move, sales end, stock runs out — and the AI's memory of prices can be months old. Treat its numbers as stale by default. Click through and check the live price yourself, every time.",
      "B07_StalePrices", "A price tag stamped with an ink X; a cursor draws a cable to a fresh 'live' card with an ink check; label 'check live'.",
      [{"at": 0.1, "event": "price tag lands"}, {"at": 0.4, "event": "ink X stamps the tag"}, {"at": 0.6, "event": "cable draws to the live card; check lands"}]),
 beat("B08", "So the method. Your priorities first. A side-by-side table. The trade-off question. The review patterns. The fine print, asked about directly. You stay the decider. The AI does the reading. That's the whole co-pilot.",
      "B08_TheMethod", "Three numbered plates stack — 'priorities', 'table', 'fine print' — with checks; a 'you decide' head crowns them.",
      [{"at": 0.1, "event": "plates land with numbers and labels"}, {"at": 0.5, "event": "checks land on each plate"}, {"at": 0.7, "event": "head lands; label 'you decide'"}]),
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
    "Hallo. This is Liam, in for Bear. You could spend three evenings reading reviews. Or let the AI do the reading, and spend your evenings on the deciding. Today: how to shop with an AI co-pilot — one that helps you choose without choosing for you.",
    "BrutalistHesitantWriter",
    {"text": "Which vacuum should I buy", "triggerWords": "Which vacuum should I buy", "replacementWords": "how do I compare options and spot the trap",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Which vacuum should I buy'"}, {"at": 0.6, "event": "backspaces it into 'how do I compare options and spot the trap' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive pick-for-me question and corrects it to the method question: compare options, spot the trap.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Co-pilot: the AI helping you decide, not deciding for you. A review summary: what hundreds of reviews boil down to. Fine print: the small contract text nobody reads — which is exactly where the traps live.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "co-pilot", "meaning": "the AI helping you decide, not deciding for you"},
               {"term": "review summary", "meaning": "what hundreds of reviews boil down to"},
               {"term": "fine print", "meaning": "the small contract text nobody reads — home of the traps"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'co-pilot' lands"}, {"at": 0.5, "event": "'review summary' lands"}, {"at": 0.78, "event": "'fine print' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("I'm choosing between two options: [A] and [B]. My priorities are: [X, Y, Z]. "
             "Lay them out side by side, one row per priority, then tell me what I'd be giving up with each.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Did the table change what you are leaning toward? And did it name a trade-off you had not thought of?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Shop Smarter Once",
     "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: did the table change what you are leaning toward?", "Check: did it name a trade-off you had not thought of?"],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, with the voice carrying the explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

# ── assertions ──────────────────────────────────────────────────────────────
assert len(B) == 13, f"expected 13 beats, got {len(B)}"
body = [b for b in B if b.get("lane") == "manim"]
assert len(body) == 9, f"expected 9 manim body beats, got {len(body)}"
assert [b["beat_id"] for b in body] == [f"B{i:02d}" for i in range(9)], "body beat ids out of order"
for b in body:
    assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class name must start with beat id"
    assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    assert 6 <= b["estimated_duration_s"] <= 25, f"{b['beat_id']}: duration {b['estimated_duration_s']}s out of band"
total = sum(b["estimated_duration_s"] for b in B)
assert 180 <= total <= 360, f"total {total}s outside 3-6 min band"
# hesitant-writer trigger contract
hw = OPEN[0]["shot"]["remotion"]["props"]
assert hw["triggerWords"] in hw["text"], "trigger must appear verbatim in text"
assert not hw["triggerWords"].endswith(("?", ".", "!")), "trigger must not end in punctuation"
assert not hw["replacementWords"].endswith(("?", ".", "!")), "replacement must not end in punctuation"
# terms length contract (ClaudeDefinitions truncates past ~17 chars)
for t in OPEN[1]["shot"]["remotion"]["props"]["terms"]:
    assert len(t["term"]) <= 17, f"term too long: {t['term']!r}"
# bookend contract
assert B[0]["beat_id"] == "BIDEA" and B[1]["beat_id"] == "BDEFS"
assert B[-2]["beat_id"] == "BHTF" and B[-1]["beat_id"] == "BOUT"
assert B[-1]["kind"] == "outro_voice" and B[-1]["tail_silence_s"] == 1.0
for b in B:
    assert b.get("voice") == "am_onyx", f"{b['beat_id']}: voice must be am_onyx"

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · SHOPPING", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
    "source_doc": "Built from scratch (NEW). Review-manipulation facts verified against the FTC Consumer Review Rule, 2026-10-05 (see FACTCHECK.md).",
    "playlist": "how-to-use-ai", "film_number": 43, "series": "How to AI", "wave": "Wave 6 — Making things",
    "tags": ["shopping", "show-tell", "how-to-ai", "Claude", "general-audience", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats;", len(body), "manim;", "est", round(total), "s")
