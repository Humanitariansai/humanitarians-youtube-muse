#!/usr/bin/env python3
"""make_sheet.py — Edit video with words. (Humanitarians AI YouTube film)

Builds beat_sheet.json: 14 beats, show-tell spine (hesitant writer ->
definitions -> 10 body beats -> your turn -> outro). Skill: show-tell.
Persona: Liam, in for Bear. TTS: Kokoro am_onyx. Register: Teardown.
Channel: claude-liam. Watermark: @NikBearBrown.

Source: NEW — built from scratch for the how-to-AI queue (Wave 7, #45).
Claims grounded in current reporting, verified 2026-10-07:
- YouTube conversational editing announced at Made on YouTube 2026-09-23;
  reported window early 2027 for Shorts + YouTube Create app (TechCrunch;
  YouTube's own posts give no date — attributed as "reported").
- Happy Kelli onstage demo: dance footage, best take per outfit, music +
  transitions; "a one-hour shoot can be 10 hours or more in the edit";
  "edits with you, not for you" (TechCrunch 2026-09-23).
- Capabilities: text overlays, pause removal, suggestions from conversation;
  jump back to timeline for manual control (chronicle.ng 2026-09-24).
- Meta Edits Assistant announced 2026-09-30, rolling out US on Edits app;
  reads follows/views/retention/likes/shares/comments/trends/interests;
  suggests hooks, captions, scripts, trending audio; free with daily prompt
  limit; "does the digging, creative calls are yours" — Brett Westervelt
  (industrywired / realhacker.news / webpronews / techmymoney, Oct 2026).
- YouTube Create AI first draft: auto-trim + arrange into first draft;
  auto captions, noise removal (exemplary.ai summary of YouTube statements).

Run: python3 make_sheet.py   (writes beat_sheet.json in cwd)
Durations: ~2.4 words/sec narration => words/2.4 + 1.5s pause, rounded.
"""
import json
import re

WORD = re.compile(r"[A-Za-z0-9'\u00c0-\u024f]+(?:[-'][A-Za-z0-9'\u00c0-\u024f]+)*")


def est_dur(text):
    return round(len(WORD.findall(text)) / 2.4 + 1.5, 1)


def graphic(beat_id, act, cls, narration, visual_intent, show):
    return {
        "beat_id": beat_id, "act": act, "lane": "manim",
        "narration_text": narration,
        "estimated_duration_s": est_dur(narration),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "GRAPHIC", "source": "own",
                 "visual_intent": visual_intent,
                 "show": show,
                 "manim": {"class": cls}},
        "qc": {"sparse_by_design": True,
               "sparse_reason": f"show-tell body beat {beat_id}: one drawing, minimal labels"},
    }


def remotion(beat_id, act, narration, pattern, props, show):
    return {
        "beat_id": beat_id, "act": act, "lane": "bookend",
        "narration_text": narration,
        "estimated_duration_s": est_dur(narration),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "REMOTION", "source": "own",
                 "show": show,
                 "remotion": {"pattern": pattern, "props": props}},
        "qc": {"sparse_by_design": True,
               "sparse_reason": f"show-tell bookend beat {beat_id}: Claude bookend pattern"},
    }


BEATS = [
    remotion(
        "BIDEA", "the question",
        ("Hallo. This is Liam, in for Bear. Editing a video means learning "
         "the timeline \u2014 the cuts, the tracks, the little keyframe "
         "diamonds. Or it did. Because the next version of the editor doesn't "
         "ask you to learn anything. It asks you to just say what you want."),
        "BrutalistHesitantWriter",
        {"text": ("Editing video means learning the timeline \u2014 if I want "
                  "a better edit, I have to learn the timeline\n"
                  "Editing video means learning the timeline \u2014 if I want "
                  "a better edit, I just say what I want changed"),
         "triggerWords": "I have to learn the timeline",
         "replacementWords": "I just say what I want changed",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6,
         "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
         "seed": "edit-video-with-words", "banner": ""},
        [{"at": 0.05, "event": "the naive line types in: 'I have to learn the timeline'"},
         {"at": 0.45, "event": "hesitation; terracotta strike crosses 'I have to learn the timeline'"},
         {"at": 0.70, "event": "correction writes in: 'I just say what I want changed'"}],
    ),
    remotion(
        "BDEFS", "terms",
        ("Four terms, before we start. Shorts: YouTube's short, vertical "
         "videos. YouTube Create: YouTube's free editing app for your phone. "
         "Chat editing: an AI editor you instruct in plain language, inside "
         "a chat window. Edits: Meta's own video-editing app."),
        "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [
             {"term": "Shorts",
              "meaning": "YouTube's short, vertical videos"},
             {"term": "YouTube Create",
              "meaning": "YouTube's free editing app for phones"},
             {"term": "chat editing",
              "meaning": "an AI editor you instruct in plain language"},
             {"term": "Edits",
              "meaning": "Meta's own video-editing app"}],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.05, "event": "'Shorts' lands with its meaning"},
         {"at": 0.30, "event": "'YouTube Create' lands with its meaning"},
         {"at": 0.55, "event": "'chat editing' lands with its meaning"},
         {"at": 0.78, "event": "'Edits' lands with its meaning"}],
    ),
    graphic(
        "B00", "the idea", "B00_HeroChat",
        ("Picture a chat window sitting inside your editing app. You type: "
         "match the cuts to the beat. And the clips rearrange themselves "
         "\u2014 no timeline, no dragging, no keyframes. That is the whole "
         "idea: an editor that takes instructions in plain language."),
        "A phone; its chat window; your instruction 'match the cuts to the "
        "beat' lands as a bubble; the film strip below shuffles its clips "
        "into a new order on its own.",
        [{"at": 0.08, "event": "phone + chat window fade in"},
         {"at": 0.25, "event": "user bubble 'match the cuts to the beat' lands"},
         {"at": 0.55, "event": "film-strip clips shuffle into a new order"},
         {"at": 0.80, "event": "'plain language' tag lands"}],
    ),
    graphic(
        "B01", "why it matters", "B01_TenHours",
        ("Why does this matter? Because editing eats time. The creator who "
         "demoed this for YouTube put it this way: a one-hour shoot can be "
         "ten hours or more in the edit. Ten hours of trimming, cutting, "
         "and nudging clips into place."),
        "A timeline crowded with tiny clips; a '1 hour shoot' card becomes "
        "a '10+ hours edit' card as a clock hand spins.",
        [{"at": 0.08, "event": "crowded timeline draws in"},
         {"at": 0.30, "event": "'1 hour shoot' card lands"},
         {"at": 0.55, "event": "clock spins; '10+ hours edit' card lands"},
         {"at": 0.80, "event": "terracotta ring on '10+ hours'"}],
    ),
    graphic(
        "B02", "the announcement", "B02_Announced",
        ("So here is what YouTube announced at its Made on YouTube event "
         "this September: a conversational editing assistant, coming to "
         "Shorts and to the YouTube Create app. You start from a suggested "
         "prompt, or type your own \u2014 then keep refining the cut by "
         "continuing the conversation."),
        "A 'Made on YouTube \u00b7 Sept 2026' card; a phone slides in "
        "carrying a chat window; 'Shorts' and 'YouTube Create' labels dock "
        "beneath it.",
        [{"at": 0.08, "event": "'Made on YouTube' card lands"},
         {"at": 0.35, "event": "phone with chat window slides in"},
         {"at": 0.60, "event": "'Shorts' + 'YouTube Create' labels dock"},
         {"at": 0.82, "event": "a suggested-prompt chip types itself"}],
    ),
    graphic(
        "B03", "the demo", "B03_Demo",
        ("In YouTube's demo, the creator Happy Kelli hands over dance "
         "footage \u2014 herself dancing, in different outfits. She asks "
         "the assistant to pick the best take of each outfit. Then she "
         "says: add music, add transitions. And the assistant assembles "
         "the cut."),
        "Three 'take' cards (outfit A, B, C); the chat picks the best of "
        "each; a music note and transition arrows land on the assembled cut.",
        [{"at": 0.08, "event": "three take cards land: outfits A, B, C"},
         {"at": 0.35, "event": "chat bubble 'best take of each outfit' lands"},
         {"at": 0.55, "event": "best takes lift out; also-rans dim"},
         {"at": 0.75, "event": "music note + transition arrows land on the cut"}],
    ),
    graphic(
        "B04", "the fiddly work", "B04_Fiddly",
        ("It handles the fiddly work too. Text overlays, on command. Pauses "
         "in speech, removed. And it makes suggestions from the "
         "conversation itself \u2014 it reads what you are going for, and "
         "proposes the next move."),
        "A chat bubble; a text-overlay chip stamps onto a clip; pause gaps "
        "shrink on a waveform; suggestion chips fan out below.",
        [{"at": 0.08, "event": "chat bubble lands"},
         {"at": 0.30, "event": "text overlay stamps onto a clip"},
         {"at": 0.52, "event": "pause gaps shrink on the waveform"},
         {"at": 0.75, "event": "suggestion chips fan out"}],
    ),
    graphic(
        "B05", "you stay in charge", "B05_YourHands",
        ("And here is the part that matters most: at any point, you can "
         "jump back into the regular timeline and adjust everything by "
         "hand. The AI drafts; you direct. As the demo put it: it edits "
         "with you, not for you."),
        "The chat window slides aside; the real timeline appears; a cursor "
        "drags a clip edge by hand; the tag 'edits with you, not for you' "
        "lands.",
        [{"at": 0.08, "event": "chat window slides aside"},
         {"at": 0.30, "event": "timeline draws in"},
         {"at": 0.55, "event": "cursor drags a clip edge by hand"},
         {"at": 0.80, "event": "'edits with you, not for you' tag lands"}],
    ),
    graphic(
        "B06", "when", "B06_Early2027",
        ("When can you try it? The reported window is early twenty "
         "twenty-seven \u2014 for Shorts and the Create app. It is a "
         "preview today, not a product. But the direction is set: the "
         "timeline stops being the price of admission."),
        "A calendar page turns to a hero tag reading 'early 2027'; 'Shorts' "
        "and 'Create app' labels dock beneath; a timeline icon fades behind "
        "a 'no longer required' ring.",
        [{"at": 0.08, "event": "calendar page lands"},
         {"at": 0.35, "event": "'early 2027' hero tag grows"},
         {"at": 0.60, "event": "'Shorts' + 'Create app' labels dock"},
         {"at": 0.82, "event": "'reported window' caption lands"}],
    ),
    graphic(
        "B07", "meanwhile, meta", "B07_MetaShips",
        ("Meanwhile, Meta has already shipped its version of the idea, "
         "inside the Edits app. Announced September thirtieth and rolling "
         "out in the US: an assistant that reads your Reels numbers \u2014 "
         "views, watch time, likes \u2014 and suggests what to make next."),
        "An 'Edits' phone; dashboard bars for views, watch time, likes "
        "grow; a chat bubble assembles from the bars carrying 'what to make "
        "next'.",
        [{"at": 0.08, "event": "'Edits' phone lands"},
         {"at": 0.30, "event": "dashboard bars grow: views, watch time, likes"},
         {"at": 0.58, "event": "bars feed a chat bubble"},
         {"at": 0.80, "event": "'what to make next' lands in the bubble"}],
    ),
    graphic(
        "B08", "the line", "B08_TheLine",
        ("Hooks, captions, scripts \u2014 it can even suggest trending "
         "audio. But Meta draws a clear line: the assistant does the "
         "digging, it says. The creative calls stay yours."),
        "Suggestion chips (hooks, captions, scripts, audio) fan out; a "
        "divider line draws; below it the tag 'the creative calls stay "
        "yours' lands with a terracotta check.",
        [{"at": 0.08, "event": "suggestion chips fan out"},
         {"at": 0.40, "event": "divider line draws"},
         {"at": 0.60, "event": "'the creative calls stay yours' lands"},
         {"at": 0.80, "event": "terracotta check stamps it"}],
    ),
    graphic(
        "B09", "start today", "B09_Today",
        ("And you do not have to wait to start. The YouTube Create app "
         "already ships an AI first draft: it trims your clips and arranges "
         "them into a starting cut, all by itself. Same app \u2014 just no "
         "chat window yet. The conversation is the part that arrives in "
         "twenty twenty-seven."),
        "A 'YouTube Create' phone; loose clips auto-arrange into a first "
        "draft; a 'no chat yet' note appears, then a small 'chat: 2027' "
        "chip docks beside it.",
        [{"at": 0.08, "event": "'YouTube Create' phone lands"},
         {"at": 0.35, "event": "loose clips auto-arrange into a first draft"},
         {"at": 0.62, "event": "'no chat yet' note lands"},
         {"at": 0.82, "event": "'chat: 2027' chip docks"}],
    ),
    remotion(
        "BHTF", "your turn",
        ("Your turn. Paste this into Claude: Act as my video editor. I will "
         "describe my footage. Reply with plain-language edit instructions, "
         "one per line: which parts to cut, where the music should shift, "
         "and what text to put on screen. My footage \u2014 then describe "
         "your clips. Check the result two ways. One: every instruction "
         "names exactly one thing to change. Two: a human editor could "
         "follow your list and ask no questions."),
        "ClaudeComposerAsk",
        {"greeting": "Your turn.",
         "topic": "HOW TO AI \u00b7 YOUR TURN",
         "segment": "Edit video with words",
         "command": ("Act as my video editor. I will describe my footage. "
                     "Reply with plain-language edit instructions, one per "
                     "line: which parts to cut, where the music should "
                     "shift, and what text to put on screen. My footage: "
                     "[describe your clips here]"),
         "runningText": "paste this into Claude\u2026",
         "output": ["Check: every instruction names exactly one thing to change.",
                    "Check: a human editor could follow the list and ask no questions."],
         "folderLabel": "@NikBearBrown",
         "modelLabel": "Opus 5.5",
         "effortLabel": "High"},
        [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.8, "event": "the two check lines land"}],
    ),
    remotion(
        "BOUT", "outro",
        ("Edit video with words. At Nik Bear Brown."),
        "ClaudeTitleOutro",
        {"title": "Edit Video With Words",
         "slug": "edit-video-with-words",
         "handle": "@NikBearBrown",
         "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; mascot"}],
    ),
]

METADATA = {
    "title": "Edit video with words.",
    "slug": "edit-video-with-words",
    "series": "Humanitarians AI \u2014 how to use AI",
    "skill": "show-tell",
    "style_preset": "show-tell",
    "channel": "claude-liam",
    "persona": "Liam (in for Bear)",
    "voice": "am_onyx",
    "voice_kokoro": "am_onyx",
    "engine": "kokoro",
    "clock": "narration",
    "register": "Teardown",
    "watermark": "@NikBearBrown",
    "greeting": "Hallo",
    "greeting_language": "German/Dutch (Hallo)",
    "palette": {"stage": "#F2F0E9", "ink": "#3D3929", "accent": "#D97757",
                "dim": "#8B8F96", "ghost": "#D9D4C7", "card": "#FAF9F5",
                "kraft": "#DCC9AA"},
    "playlist": "how-to-use-ai",
    "tags": ["show-tell", "youtube-shorts", "youtube-create", "video-editing",
             "conversational-editing", "meta-edits", "general-audience"],
    "derived_from": "NEW \u2014 built from scratch for the how-to-AI queue (Wave 7, #45)",
    "audience": "smart, pragmatic general audience \u2014 NOT AI experts; "
                "every term explained in plain language, shown rather than told",
    "bookend_exempt": ["cold-open", "verdict"],
    "bookend_exempt_reason": "show-tell spine (skill law): opens on the "
                             "hesitant writer + terms card; no verdict card; "
                             "Your Turn is the Claude.ai composer; spoken "
                             "outro stays.",
    "caption_policy": "none",
}

if __name__ == "__main__":
    ids = [b["beat_id"] for b in BEATS]
    assert len(BEATS) == 14, len(BEATS)
    assert 13 <= len(BEATS) <= 22, "beat count outside 13-22 band"
    assert ids[0] == "BIDEA" and ids[1] == "BDEFS", ids[:2]
    assert ids[-2:] == ["BHTF", "BOUT"], ids[-2:]
    body = [b for b in BEATS if b["shot"]["type"] == "GRAPHIC"]
    book = [b for b in BEATS if b["shot"]["type"] == "REMOTION"]
    assert len(body) == 10, len(body)
    assert len(book) == 4, len(book)
    assert [b["beat_id"] for b in body] == \
        [f"B0{i}" for i in range(10)], "body ids must be B00..B09"
    classes = [b["shot"]["manim"]["class"] for b in body]
    assert all(c.startswith(b + "_") for b, c in
               zip([x["beat_id"] for x in body], classes)), "class naming <BID>_<Name>"
    assert len(set(classes)) == 10, "class names must be unique"
    idea = BEATS[0]["narration_text"]
    assert "Liam, in for Bear" in idea, "IN-FOR-BEAR LAW: name the voice"
    htf = next(b for b in BEATS if b["beat_id"] == "BHTF")
    assert htf["shot"]["remotion"]["props"]["greeting"] == "Your turn."
    assert "Paste this into Claude" in htf["narration_text"], \
        "handoff must name the prompt"
    bout = next(b for b in BEATS if b["beat_id"] == "BOUT")
    assert "At Nik Bear Brown" in bout["narration_text"]
    total = round(sum(b["estimated_duration_s"] for b in BEATS), 1)
    for b in BEATS:
        assert b["narration_text"] and b["estimated_duration_s"] > 0
        assert b["shot"]["type"] in ("GRAPHIC", "REMOTION")
    BS = {"metadata": METADATA, "beats": BEATS}
    print(f"beats={len(BEATS)} body={len(body)} bookends={len(book)} "
          f"total={total}s (~{int(total//60)}m{int(total%60):02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
