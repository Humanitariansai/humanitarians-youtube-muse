#!/usr/bin/env python3
"""make_sheet.py — Pictures from Words (How to AI, film 19).

Builds beat_sheet.json: 14 beats, three acts. Run: python3 make_sheet.py
Beat durations: speech at ~150 wpm; body beats ~18-24s.
"""
import json

BS = {
    "title": "Pictures from Words",
    "film": 19,
    "series": "Humanitarians AI — How to AI",
    "beats": [
        {
            "id": "BIDEA", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Liam",
            "line": "This is Liam, in for Bear. You need a picture — for a slide, an invitation, a mockup — and you can't draw. Good news: if you can describe a picture in words, you can make one. Describing a picture well is a learnable skill, and this film teaches you the ladder.",
            "screen": "Prompt text types in; a picture frame draws itself; a drawn placeholder scene (sun + mountains) appears inside."
        },
        {
            "id": "BDEFS", "scene": "M02", "dur_s": 22, "act": "hook",
            "voice": "Liam",
            "line": "Four terms. Image generator: an app that turns your words into pictures. Prompt: the sentence you type. Style: what the picture looks like — a photo, a watercolor, a cartoon. Iterate: ask again with tweaked words until it looks right. That's the whole vocabulary — everything else in this film is just practice.",
            "screen": "Four term cards appear: image generator / prompt / style / iterate."
        },
        {
            "id": "B01", "scene": "M03", "dur_s": 20, "act": "1",
            "voice": "Liam",
            "line": "Rung one. Start vague: type the words 'a dog'. The generator gives you a dog — the most average dog imaginable. Plain, gray, boring. That's not a failure; it's the machine doing exactly what you said. Vague words in, vague picture out. And that picture is all yours — it didn't exist before you typed.",
            "screen": "Prompt card 'a dog' → arrow → frame with a deliberately plain grey dog silhouette; caption 'vague words in → vague picture out'."
        },
        {
            "id": "B02", "scene": "M04", "dur_s": 22, "act": "1",
            "voice": "Liam",
            "line": "Rung two: add the three things that matter most — subject, style, mood. Not 'a dog', but 'a sleepy golden retriever puppy, watercolor painting, warm cozy morning light'. Same machine, much better picture. You didn't learn a new tool. You just said more — and the picture got closer to the one in your head.",
            "screen": "Richer prompt card + SUBJECT / STYLE / MOOD chips stack in; warm picture with sun, watercolor wash, warmer dog."
        },
        {
            "id": "B03", "scene": "M05", "dur_s": 20, "act": "1",
            "voice": "Liam",
            "line": "Rung three: iterate — like texting a friend. Too cold? Type 'warmer light'. Too tight? Type 'wider shot'. Each round keeps what worked and fixes one thing. Three or four rounds is completely normal. Nobody gets the picture they want on the first try — professionals don't either.",
            "screen": "The warm picture returns; 'warmer light' grows the sun deeper; 'wider shot' widens the frame; caption 'keep what works, fix one thing'."
        },
        {
            "id": "B04", "scene": "M06", "dur_s": 20, "act": "2",
            "voice": "Liam",
            "line": "The whole recipe fits on one card. Subject: what's in the picture — say, a puppy. Setting: where — a kitchen. Style: what it looks like — watercolor. Lighting: how it's lit — morning sun. Mood: how it feels — cozy. Fill all five and the generator has almost nothing left to guess.",
            "screen": "Five-row recipe card: SUBJECT → a puppy; SETTING → a kitchen; STYLE → watercolor; LIGHTING → morning sun; MOOD → cozy."
        },
        {
            "id": "B05", "scene": "M07", "dur_s": 20, "act": "2",
            "voice": "Liam",
            "line": "What happens between the words and the picture? The generator starts from visual static — like TV snow — and sharpens it, step by step, steered by your sentence, until the picture matches. You don't need the machinery. What matters is this: your words are the steering wheel, and every word steers.",
            "screen": "Prompt → arrow → three panels: 'static' dot grid → 'sharper' rough outline → 'picture' cleaner dog + sun."
        },
        {
            "id": "B06", "scene": "M08", "dur_s": 20, "act": "2",
            "voice": "Liam",
            "line": "So what do you actually use it for? Presentation slides that don't look like clip art. A birthday invitation. A mockup of the garden you want to plant. Visualizing an idea before you spend money on it. The sweet spot is drafts and placeholders — pictures that carry an idea, not pictures that pretend to be photographs.",
            "screen": "2×2 grid of use cards with mini icons: slides / invitation / garden mockup / an idea."
        },
        {
            "id": "B07", "scene": "M09", "dur_s": 22, "act": "3",
            "voice": "Liam",
            "line": "Now the honest part. First limit: words inside the picture. The generator doesn't type letters — it draws them, like shapes. So 'Happy Birthday' can come out 'Happpy Birthdaay'. Always read any text in the image before you share it. Short words survive best; a whole paragraph on a poster is asking for trouble.",
            "screen": "Birthday sign reading 'HAPPPY BIRTHDAAY'; magnifier ring lands on the garbled text; tag 'read it before you share it'."
        },
        {
            "id": "B08", "scene": "M10", "dur_s": 20, "act": "3",
            "voice": "Liam",
            "line": "Second limit: hands and faces. Fingers, teeth, eyes in a crowd — the small fiddly details go wrong more often than anything else. Zoom in before you share. If a hand looks strange, generate again or crop it out. This is getting better every year, but 'check closely' is still the rule.",
            "screen": "Frame with a simple drawn hand — six fingers; magnifier ring on the fingers; tag 'zoom in before you share'."
        },
        {
            "id": "B09", "scene": "M11", "dur_s": 22, "act": "3",
            "voice": "Liam",
            "line": "And the rule that isn't about quality: say it's AI-made. Most platforms now offer an AI label, and some places require one. A one-line caption — 'image made with AI' — keeps you honest and costs you nothing. Here's the test: if the picture could fool someone into thinking it's a real photo, that's exactly when the label matters most.",
            "screen": "Picture frame with sun + mountains; an 'AI-MADE' stamp drops on; caption 'say it's AI-made'."
        },
        {
            "id": "BVDT", "scene": "M12", "dur_s": 24, "act": "recap",
            "voice": "Liam",
            "line": "So: act one, the ladder — vague words give vague pictures; subject, style, and mood fix that; iterate like you're texting a friend. Act two, the uses — slides, invitations, mockups, and drafts. Act three, the limits — check the text, zoom in on the hands, and always say when a picture is AI-made.",
            "screen": "Three recap plates, one per act: the ladder / the uses / the limits."
        },
        {
            "id": "BHTF", "scene": "M12", "dur_s": 18, "act": "do_today",
            "voice": "Liam",
            "line": "Your turn. Today: open any image generator, type a vague prompt like 'a dog', then rewrite it with the five-slot recipe and compare the two pictures side by side. Tell me which one you'd actually use — and what one word made the difference.",
            "screen": "Do-today card: 1. type a vague prompt. 2. rewrite with the 5-slot recipe. 3. compare."
        },
        {
            "id": "BOUT", "scene": "M12", "dur_s": 14, "act": "outro",
            "voice": "Liam",
            "line": "Liam, in for Bear. Pictures from words. Thanks for watching — next film: what never to paste into AI.",
            "screen": "'Pictures from Words.' title restate with terracotta period; @NikBearBrown handle."
        }
    ]
}

if __name__ == "__main__":
    for b in BS["beats"]:
        assert b["scene"].startswith("M") and b["id"] not in ("",), b
    assert len(BS["beats"]) == 14, len(BS["beats"])
    assert 13 <= len(BS["beats"]) <= 22, "beat count outside 13-22 band"
    acts = [b["id"] for b in BS["beats"] if b["act"] in ("1", "2", "3")]
    assert len(acts) == 9, len(acts)
    recap = next(b for b in BS["beats"] if b["id"] == "BVDT")
    assert recap["line"].lower().count("act ") >= 3, "recap must cover each act"
    total = sum(b["dur_s"] for b in BS["beats"])
    assert 270 <= total <= 420, f"total {total}s outside 4.5-7 min band"
    print(f"beats={len(BS['beats'])} body={len(acts)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
