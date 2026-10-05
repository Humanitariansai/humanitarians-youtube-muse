#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for "Fix your photos" (How-to-AI film 39, Wave 6 "Making things").

SHOW-TELL (Bear, 2026-09-26): one drawn illustration per beat, minimal labels,
Liam's narration (Kokoro am_onyx) carries the explanation. No composer cold
open, no verdict card (bookend_exempt); spoken @NikBearBrown outro stays.

Premise: AI cleanup of your own photos — remove the photobomber, fix the
lighting, straighten and crop — before you print. The edits happen in the AI
tools of the viewer's photo app (Google Photos' Magic Eraser is the named,
verified example); Claude is used only to plan what to fix, via its verified
see-and-describe ability. Companion to the extra film `ai-that-sees`: that
film taught handing the AI a photo; this one teaches changing it. The
companion is referenced, never re-taught. No pricing tiers anywhere.
Facts verified 2026-10-05 (see FACTCHECK.md).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = "fix-your-photos"
TITLE = "Fix your photos"

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}

B = [
 beat("B00", "Start with the photo itself. You got the shot: everyone laughing, the light just right — and there's a stranger's head behind you. A few years ago this photo was dead. Today you fix it the same way you talk to the AI: in words.",
      "B00_PhotoHero", "A kraft photo card with two dark figures in front; a smaller stranger figure stands behind them, labelled 'photobomber' with a leader.",
      [{"at": 0.1, "event": "photo + figures land"}, {"at": 0.5, "event": "'photobomber' label with leader"}]),
 beat("B01", "The companion film, AI that sees, was about handing the AI a photo so it can describe it. This film is about changing the photo. For that you use the AI tools in your photo app. If you use Google Photos, it calls its eraser Magic Eraser.",
      "B01_Companion", "Two photo cards: 'see' (the companion's job) and 'change' (this film's job); a dashed terracotta eraser ring lands on 'change' and a terracotta check with it.",
      [{"at": 0.1, "event": "both cards land, labelled"}, {"at": 0.45, "event": "eraser ring appears on 'change'"}, {"at": 0.65, "event": "terracotta check"}]),
 beat("B02", "The big one: remove the photobomber. Open the edit tools, find the eraser, and tap the stranger — or circle them if the app misses. The AI erases them and paints in what should be there: grass, fence, sky.",
      "B02_Remove", "The photo with the photobomber; a dashed terracotta ring circles the stranger, who fades out as a kraft fill patch grows in, labelled 'gone'.",
      [{"at": 0.1, "event": "photo + photobomber land"}, {"at": 0.35, "event": "dashed ring circles the stranger"}, {"at": 0.6, "event": "stranger fades, fill patch grows"}]),
 beat("B03", "That painting in is called hallucination: the AI inventing a detail it can't see. It does fine on grass and sky, because grass looks like grass. But faces, hands, and words on signs — always look at those. They can come out wrong.",
      "B03_Invent", "The patched photo; a dashed terracotta outline marks the invented region, labelled 'invented' with a leader.",
      [{"at": 0.1, "event": "patched photo lands"}, {"at": 0.4, "event": "dashed outline on the invented region"}, {"at": 0.6, "event": "'invented' label with leader"}]),
 beat("B04", "Then the lighting. Skip the forest of sliders. Try the app's one-tap suggestion — in Google Photos it's called Enhance — and the AI does the slider math for you: brighter, warmer, better colors.",
      "B04_Light", "Two cards: a dim 'dark' one and a bright 'bright' one with a terracotta sun; an arrow runs dark → bright and a terracotta check lands on bright.",
      [{"at": 0.1, "event": "both cards land, labelled"}, {"at": 0.45, "event": "arrow dark → bright"}, {"at": 0.65, "event": "sun + terracotta check on bright"}]),
 beat("B05", "Before the fancy edits, straighten the horizon and tighten the frame. Open the crop tool, rotate until the horizon is level, and pull the frame in. A level horizon fixes more photos than any filter.",
      "B05_Straighten", "A photo with a tilted ink horizon; a crop frame closes in, the tilted line is replaced by a level one, labelled 'level'.",
      [{"at": 0.1, "event": "photo + tilted horizon land"}, {"at": 0.35, "event": "crop frame appears"}, {"at": 0.55, "event": "horizon goes level"}, {"at": 0.7, "event": "'level' label"}]),
 beat("B06", "One rule: edit a copy, never the original. Good apps save the edit as a separate copy. Make sure yours does — an edit saved on top of the original can't be undone, and you don't get the photo back.",
      "B06_Copy", "Two cards: 'original' untouched and 'copy' with a dashed eraser ring; a terracotta check lands on the copy.",
      [{"at": 0.1, "event": "both cards land, labelled"}, {"at": 0.45, "event": "eraser ring on the copy"}, {"at": 0.65, "event": "terracotta check on the copy"}]),
 beat("B07", "Check the spot it fixed. Zoom in where the photobomber was and look at the edges: smeared lines, a fence post that grew wrong, grass repeating like wallpaper. If it's off, undo and circle more tightly.",
      "B07_Check", "The patched photo with a magnifier grown over the fixed spot, labelled 'look' with a leader.",
      [{"at": 0.1, "event": "patched photo lands"}, {"at": 0.4, "event": "magnifier grows over the fix"}, {"at": 0.65, "event": "'look' label with leader"}]),
 beat("B08", "Last rule: an edited photo is a made thing. The family album and the print shop are fine. But never show it as what really happened — and never edit documents: receipts, IDs, anything official.",
      "B08_MadeThing", "A family photo gets a terracotta check; a document card gets an ink X, labelled 'album' and 'ID'.",
      [{"at": 0.1, "event": "both cards land, labelled"}, {"at": 0.45, "event": "terracotta check on the album photo"}, {"at": 0.6, "event": "ink X on the ID"}]),
 beat("B09", "Then print. Decide on the screen, full size, at arm's length: does it look right? Then print that one file. The print shop gets the finished photo, not your drafts.",
      "B09_Print", "A grey printer; a white print page with the fixed photo grows out of its slot, labelled 'print'.",
      [{"at": 0.1, "event": "printer + slot land"}, {"at": 0.35, "event": "page grows out of the slot"}, {"at": 0.65, "event": "'print' label"}]),
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
    "Hola. This is Liam, in for Bear. You've got a photo you love, except for one thing in it. The question isn't how do I fix this photo. It's what do I ask the AI to change in my photo.",
    "BrutalistHesitantWriter",
    {"text": "How do I fix this photo?", "triggerWords": "fix this photo", "replacementWords": "what do I ask the AI to change in my photo",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I fix this photo?'"}, {"at": 0.6, "event": "backspaces 'fix this photo' → 'what do I ask the AI to change in my photo' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive fix question and corrects it to the real one: what to ask the AI to change.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Photobomber: a stranger who wanders into your shot. Object removal: the AI erasing a thing and filling in the background. Hallucination: the AI inventing a detail it can't see.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "photobomber", "meaning": "a stranger who wanders into your shot"},
               {"term": "object removal", "meaning": "the AI erasing a thing and filling in the background"},
               {"term": "hallucination", "meaning": "the AI inventing a detail it can't see"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'photobomber' lands"}, {"at": 0.5, "event": "'object removal' lands"}, {"at": 0.78, "event": "'hallucination' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Attach a photo you want to fix and write: tell me what you would change about this photo before I print it, "
             "from most to least important. Then I will make the changes in my photo app, one at a time.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Does the background look real where the thing was removed? And do you still have the original if the edit goes wrong?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Fix One Photo",
     "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: does the background look real where the thing was removed?", "Check: do you still have the original if the edit goes wrong?"],
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
assert len(B) == 14, f"expected 14 beats, got {len(B)}"
body = [b for b in B if b.get("lane") == "manim"]
assert len(body) == 10, f"expected 10 manim body beats, got {len(body)}"
assert [b["beat_id"] for b in body] == [f"B{i:02d}" for i in range(10)], "body beat ids out of order"
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
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · PHOTO EDITING", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Spanish (Hola)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
    "source_doc": "Built from scratch (NEW). Photo-app AI editing tools verified against Google's Photos editing page, 2026-10-05 (see FACTCHECK.md); companion reference to the extra film ai-that-sees.",
    "playlist": "how-to-use-ai",
    "series_note": "Film 39 of the How-to-AI series, Wave 6 'Making things'; companion to the extra film ai-that-sees (which taught handing the AI a photo; this one teaches changing it).",
    "tags": ["photo editing", "Magic Eraser", "object removal", "hallucination", "show-tell", "how-to-ai", "Claude", "general-audience", "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats;", len(body), "manim;", "est", round(total), "s")
