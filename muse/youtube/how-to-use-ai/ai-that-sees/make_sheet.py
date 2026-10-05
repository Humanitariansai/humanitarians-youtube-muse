#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "AI that sees" (How-to-AI extra film).

SHOW-TELL (Bear, 2026-09-26): one drawn illustration per beat, minimal labels,
Liam's narration (Kokoro am_onyx) carries the explanation. No composer cold
open, no verdict card (bookend_exempt); spoken @NikBearBrown outro stays.

Premise: you can show the AI things — screenshots, photos, forms — and a
photo often says in a second what five minutes of typing cannot. Companion to
film 18 ("Just talk to it", voice mode). Source: built from scratch (NEW).
Facts verified 2026-10-04 (see FACTCHECK.md).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "ai-that-sees"
TITLE = "AI that sees"

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

B = [
 beat("B00", "Start with the move itself. You attach a photo to your message, the way you would send a picture to a friend. Same paperclip, same plus button. The AI looks at it, reads it, and answers in words.",
      "B00_PhotoHero", "A message composer holds a plus button; a kraft photo card grows out of it; the label 'photo' sits beside it.",
      [{"at": 0.1, "event": "composer + plus button land"}, {"at": 0.35, "event": "photo card grows from the button"}, {"at": 0.6, "event": "label 'photo' with leader"}]),
 beat("B01", "Here is what happens in between. Your photo travels to the AI. The AI scans it the way you would — top to bottom, looking for the parts that matter. Then it answers in words, as if you had described the photo perfectly.",
      "B01_HowVision", "A photo card on the left, the AI eye on the right; a terracotta scan line sweeps the photo top to bottom, then an answer page grows.",
      [{"at": 0.1, "event": "photo + eye land, 'scan' label"}, {"at": 0.4, "event": "scan line sweeps top to bottom"}, {"at": 0.65, "event": "answer page grows"}]),
 beat("B02", "The classic is the error message. That dialog box full of codes you cannot read. Screenshot it, attach it, and ask what it means. The AI reads the whole box and tells you in plain language what went wrong.",
      "B02_ErrorShot", "A dim error dialog with an ink X; the eye scans it with a terracotta line, and an answer page grows.",
      [{"at": 0.1, "event": "dialog + 'error' label land"}, {"at": 0.35, "event": "the eye lands"}, {"at": 0.55, "event": "scan line sweeps"}, {"at": 0.75, "event": "answer page grows"}]),
 beat("B03", "Receipts are next. A long faded slip you would never retype. Photograph it and ask for the total, the date, the three biggest lines. The AI reads the slip and hands you the numbers, in text.",
      "B03_Receipt", "A tall kraft receipt with faint lines; a terracotta scan line sweeps it, and a tidy answer page grows.",
      [{"at": 0.1, "event": "receipt + label land"}, {"at": 0.4, "event": "scan line sweeps"}, {"at": 0.65, "event": "answer page grows"}]),
 beat("B04", "A sick plant is a photo problem. Is this one dying of thirst, or drowning? Photograph the leaves, attach it, and ask. The AI names the plant, reads the spots and droop, and tells you what it needs.",
      "B04_Plant", "A photo card with a spotted leaf; the eye scans it and an answer page grows.",
      [{"at": 0.1, "event": "leaf card + eye + 'plant' label land"}, {"at": 0.4, "event": "scan line sweeps"}, {"at": 0.65, "event": "answer page grows"}]),
 beat("B05", "Forms, too. A paper form full of small boxes, or a screen you cannot copy from. Photograph it and ask which box is which, or what this field wants. The AI reads the layout and explains it, row by row.",
      "B05_Form", "A white form with ink boxes and ghost lines; a ghost highlight band steps down the rows, and an answer page grows.",
      [{"at": 0.1, "event": "form + 'form' label land"}, {"at": 0.35, "event": "highlight band appears, steps down two rows"}, {"at": 0.6, "event": "answer page grows"}]),
 beat("B06", "Photos settle arguments of the eye. Two paint swatches, two shirts, two sofas. Which one goes with the room? Send both photos and ask. The AI looks at both and picks one, and says why.",
      "B06_WhichOne", "Two swatch cards under the AI eye; a terracotta check lands on one of them.",
      [{"at": 0.1, "event": "two swatches + eye land, 'which one' label"}, {"at": 0.5, "event": "terracotta check lands on one swatch"}]),
 beat("B07", "Handwriting counts as a photo, too. A whiteboard after the meeting, a notebook page, a recipe card. Photograph it and say transcribe this. The AI reads the scrawl and gives you back clean text.",
      "B07_Handwriting", "A whiteboard with wavy ink scribbles; an arrow runs to a clean answer page with straight lines.",
      [{"at": 0.1, "event": "whiteboard + 'notes' label land"}, {"at": 0.35, "event": "scribbles draw"}, {"at": 0.6, "event": "arrow draws, answer page grows"}]),
 beat("B08", "One rule makes every photo work better. Take it like evidence: light on, held still, the thing big in the frame. A blurry dark photo is a blurry dark question. The AI can only read what the camera caught.",
      "B08_ClearPhoto", "A dim 'blurry' card with soft blobs beside a crisp kraft 'clear' card; a terracotta check lands on the clear one.",
      [{"at": 0.1, "event": "both cards land, labelled"}, {"at": 0.5, "event": "terracotta check lands on 'clear'"}]),
 beat("B09", "If the photo is busy, point. Crop in on the part that matters, or say it: the cracked tile, top left. You are aiming the AI's eyes at the same spot yours would go to.",
      "B09_PointIt", "A busy kraft card full of small shapes; a crop frame closes in on one ink tile, with a 'this one' label and leader.",
      [{"at": 0.1, "event": "busy card lands"}, {"at": 0.35, "event": "crop frame appears around the whole card"}, {"at": 0.55, "event": "frame shrinks onto the tile"}, {"at": 0.7, "event": "'this one' label with leader"}]),
 beat("B10", "And always add a few words. A photo never replaces the question. Say transcribe this, explain this error, or which of these two is cheaper. The photo is the evidence; your words are the question.",
      "B10_SayWhat", "A photo card and a small question page with lines drawing in; an arrow runs from the question to the photo.",
      [{"at": 0.1, "event": "photo lands"}, {"at": 0.3, "event": "question page lands"}, {"at": 0.5, "event": "question lines draw"}, {"at": 0.7, "event": "arrow points at the photo"}]),
 beat("B11", "Last: the AI reads everything you show it, including what you did not mean to share. Photograph the receipt, not the bank statement. The label, not your ID. If you would not pin it to a wall, do not attach it.",
      "B11_KeepItPrivate", "A receipt card gets a terracotta check; an ID card gets an ink X.",
      [{"at": 0.1, "event": "receipt + ID land, labelled"}, {"at": 0.45, "event": "terracotta check lands on the receipt"}, {"at": 0.6, "event": "ink X lands on the ID"}]),
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
    "Ciao. This is Liam, in for Bear. You can talk to the AI — and you can show it things. A screenshot, a receipt, a plant. A photo can say in a second what takes five minutes to type. The question is not what multimodal means. It is when a picture beats a paragraph.",
    "BrutalistHesitantWriter",
    {"text": "What does multimodal mean\nin an AI app?", "triggerWords": "What does multimodal mean", "replacementWords": "when should I show the AI a photo instead of typing",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'What does multimodal mean'"}, {"at": 0.6, "event": "backspaces the definition into 'when should I show the AI a photo instead of typing' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive definition question and corrects it to the real one: when a photo beats typing.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Multimodal: an AI that takes more than one kind of input — words, photos, even speech. Vision: the AI's ability to read a photo or screenshot. Attach: adding a photo to your message, usually with a paperclip or plus button.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "multimodal", "meaning": "an AI that takes more than words: photos, speech, files"},
               {"term": "vision", "meaning": "the AI's ability to read a photo or screenshot"},
               {"term": "attach", "meaning": "adding a photo to your message, like to a friend"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'multimodal' lands"}, {"at": 0.5, "event": "'vision' lands"}, {"at": 0.78, "event": "'attach' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Take a photo of something you would normally retype: a receipt, an error message, a plant. "
             "Attach it and write: what is this, and what should I do about it?")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Did the AI read the photo correctly? And would you trust the answer enough to act on it?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Show It Once",
     "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: did the AI read the photo correctly?", "Check: would you trust the answer enough to act on it?"],
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
assert len(B) == 16, f"expected 16 beats, got {len(B)}"
body = [b for b in B if b.get("lane") == "manim"]
assert len(body) == 12, f"expected 12 manim body beats, got {len(body)}"
assert [b["beat_id"] for b in body] == [f"B{i:02d}" for i in range(12)], "body beat ids out of order"
for b in body:
    assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), f"{b['beat_id']}: class name must start with beat id"
    assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    assert 6 <= b["estimated_duration_s"] <= 20, f"{b['beat_id']}: duration {b['estimated_duration_s']}s out of band"
total = sum(b["estimated_duration_s"] for b in B)
assert 170 <= total <= 280, f"total {total}s outside 170–280s band"
# hesitant-writer trigger contract
hw = OPEN[0]["shot"]["remotion"]["props"]
assert hw["triggerWords"] in hw["text"], "trigger must appear verbatim in text"
assert not hw["triggerWords"].endswith(("?", ".", "!")), "trigger must not end in punctuation"
assert not hw["replacementWords"].endswith(("?", ".", "!")), "replacement must not end in punctuation"
# definitions term-length contract (ClaudeDefinitions truncates > ~17 chars)
for t in OPEN[1]["shot"]["remotion"]["props"]["terms"]:
    assert len(t["term"]) <= 17, f"BDEFS term too long: {t['term']!r}"
# bookend contract
assert B[0]["beat_id"] == "BIDEA" and B[1]["beat_id"] == "BDEFS"
assert B[-2]["beat_id"] == "BHTF" and B[-1]["beat_id"] == "BOUT"
assert B[-1]["kind"] == "outro_voice" and B[-1]["tail_silence_s"] == 1.0
for b in B:
    assert b.get("voice") == "am_onyx", f"{b['beat_id']}: voice must be am_onyx"
    assert b.get("estimated_duration_s") or b.get("actual_duration_s"), f"{b['beat_id']}: no duration"

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · MULTIMODAL", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Italian (Ciao)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
    "source_doc": "Built from scratch (NEW). Image-attachment support verified against mirrored Anthropic developer docs, 2026-10-04 (see FACTCHECK.md).",
    "playlist": "how-to-use-ai",
    "series_note": "Extra film beyond the 24-film How-to-AI queue (all 24 Done); companion to #18 'Just talk to it'.",
    "tags": ["multimodal", "vision", "show-tell", "how-to-ai", "Claude", "general-audience", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats;", len(body), "manim;", "est", round(total), "s")
