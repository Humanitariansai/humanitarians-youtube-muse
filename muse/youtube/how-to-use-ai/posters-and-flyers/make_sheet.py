#!/usr/bin/env python3
"""make_sheet.py — Posters and Flyers (Humanitarians AI YouTube film)

Film #38, Wave 6 "Making things". Builds beat_sheet.json: 13 beats, show-tell
spine (hesitant writer -> terms -> the job -> companion pointer -> three
steps -> the split -> print checklist -> AI label -> recap -> your turn ->
outro). Skill: show-tell. Persona: Liam, in for Bear. TTS: Kokoro am_onyx.
Register: Teardown. Channel: claude-liam. Watermark: @NikBearBrown.

Companion: pictures-from-words (film 19) taught the image-generation ladder
and the five-slot recipe; this film references it and does not re-teach it.
No pricing tiers quoted anywhere (standing preference).

Run: python3 make_sheet.py   (writes beat_sheet.json in cwd)
Durations: narration at ~150 wpm => words/2.5 + 1.0 s pause, rounded to 0.1.
"""
import json

VOICE = "am_onyx"
ENGINE = "kokoro"

SPARSE = {
    "sparse_by_design": True,
    "sparse_reason": (
        "show-tell style (Bear, 2026-09-26): one drawn object or scene on a "
        "cream stage per beat, minimal labels, with the voice carrying the "
        "explanation. The negative space is the style, so only underfill and "
        "clustered are waived; edge-bleed, empty-frame and contrast still "
        "apply."
    ),
}


def _dur(line):
    return round(len(line.split()) / 2.5 + 1.0, 1)


def remotion(beat_id, act, narration, pattern, props, show_events,
             lead_silence_s=None, qc=None, extra=None):
    beat = {
        "beat_id": beat_id,
        "act": act,
        "lane": "bookend",
        "proof_gate": "SHOW",
        "narration_text": narration,
        "estimated_duration_s": _dur(narration),
        "voice": VOICE,
        "engine": ENGINE,
        "shot": {
            "type": "REMOTION",
            "source": "own",
            "show": [{"at": t, "event": e} for t, e in show_events],
            "remotion": {"pattern": pattern, "props": props},
        },
    }
    if lead_silence_s is not None:
        beat["lead_silence_s"] = lead_silence_s
    if qc is not None:
        beat["qc"] = qc
    if extra:
        beat.update(extra)
    return beat


def graphic(beat_id, act, narration, manim_class, visual_intent, show_events,
            motion_claim=None):
    return {
        "beat_id": beat_id,
        "act": act,
        "lane": "manim",
        "proof_gate": "SHOW",
        "narration_text": narration,
        "estimated_duration_s": _dur(narration),
        "voice": VOICE,
        "engine": ENGINE,
        "shot": {
            "type": "GRAPHIC",
            "source": "own",
            "visual_intent": visual_intent,
            "show": [{"at": t, "event": e} for t, e in show_events],
            "manim": {"class": manim_class},
            "motion_claim": motion_claim or visual_intent,
        },
        "qc": SPARSE,
    }


BEATS = [
    remotion(
        "BIDEA", "the question",
        ("Hallo. This is Liam, in for Bear. You need a poster \u2014 a garage "
         "sale, a bake sale, your side business. The AI can't design it. But "
         "it can do the next best thing: draw the art. You do the words."),
        "BrutalistHesitantWriter",
        {
            "text": "Can AI design\nmy poster",
            "triggerWords": "design",
            "replacementWords": "draw the art for",
            "fontSize": 70, "charMs": 22,
            "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2,
            "jitter": 20, "seed": "posters-and-flyers", "banner": "",
        },
        [(0.0, "types 'Can AI design my poster'"),
         (0.6, "backspaces 'design' -> 'draw the art for' on the spoken correction")],
        lead_silence_s=0.8,
        qc={"sparse_by_design": True,
            "sparse_reason": "Hesitant-writer bookend: the correction is the motion."},
    ),
    remotion(
        "BDEFS", "terms",
        ("Four terms. Image generator: an app that turns your words into "
         "pictures. Prompt: the sentence you type. Printable: a file sharp "
         "enough to print. Aspect ratio: the picture's shape \u2014 tall, "
         "wide, or square. That's the vocabulary."),
        "ClaudeDefinitions",
        {
            "title": "Terms In This Film",
            "terms": [
                {"term": "image generator",
                 "meaning": "an app that turns words into pictures"},
                {"term": "prompt", "meaning": "the sentence you type"},
                {"term": "printable",
                 "meaning": "a file sharp enough to print"},
                {"term": "aspect ratio",
                 "meaning": "the picture's shape \u2014 tall, wide, square"},
            ],
            "folderLabel": "@NikBearBrown",
        },
        [(0.05, "card 1 'image generator' lands"),
         (0.30, "card 2 'prompt' lands"),
         (0.55, "card 3 'printable' lands"),
         (0.78, "card 4 'aspect ratio' lands, terracotta edge")],
    ),
    graphic(
        "B00", "show-tell",
        ("Here's the job. A poster is just a big piece of paper with three "
         "jobs: a headline people read across the room, the details they "
         "read up close, and a picture that makes them look. You bring the "
         "first two. The AI does the third."),
        "B00_Hero",
        "A kraft portrait poster sheet drops onto the stage; a headline band "
        "and detail lines draw in; a small sun-and-hill doodle draws in the "
        "art zone; the label 'poster' lands beside it.",
        [(0.05, "poster drops in"),
         (0.30, "headline band and detail lines draw in"),
         (0.60, "sun-and-hill doodle draws in the art zone"),
         (0.80, "'poster' label lands with leader line")],
    ),
    graphic(
        "B01", "show-tell",
        ("The picture part is our sister film's job. Pictures from words "
         "taught the ladder: start vague, add subject plus style plus mood, "
         "then iterate \u2014 like texting a friend. And the five-slot "
         "recipe: subject, setting, style, lighting, mood. Go watch it if "
         "you missed it. Here, we just use it."),
        "B01_Companion",
        "A picture frame on the left; five chips \u2014 subject, setting, "
        "style, lighting, mood \u2014 land one by one on the right; an arrow "
        "feeds them into the frame, whose doodle grows warmer with each chip.",
        [(0.05, "picture frame fades in"),
         (0.15, "chip 1 'subject' lands; doodle gains a sun"),
         (0.30, "chip 2 'setting' lands; hills appear"),
         (0.45, "chip 3 'style' lands; warm wash spreads"),
         (0.60, "chips 4-5 'lighting', 'mood' land; arrow feeds frame"),
         (0.85, "'the recipe' label lands beside the chips")],
    ),
    graphic(
        "B02", "show-tell",
        ("Step one: tell it the real job first. Before any picture, write "
         "down three facts: what \u2014 a garage sale; when \u2014 Saturday, "
         "nine in the morning; where \u2014 twelve Maple Street. The AI "
         "needs these because the poster needs these. No facts, no poster."),
        "B02_Facts",
        "The poster returns; three fact chips \u2014 'garage sale', "
        "'Saturday, 9 a.m.', '12 Maple Street' \u2014 fly in one by one and "
        "settle as the poster's detail lines.",
        [(0.05, "poster fades back in"),
         (0.15, "chip 'garage sale' lands; becomes headline line"),
         (0.45, "chip 'Saturday, 9 a.m.' lands; becomes detail line"),
         (0.70, "chip '12 Maple Street' lands; becomes detail line"),
         (0.90, "'three facts' label lands with leader line")],
    ),
    graphic(
        "B03", "show-tell",
        ("Step two: make the words exact. Type the exact headline you want, "
         "in quotes: 'GARAGE SALE'. The generator draws letters as shapes "
         "\u2014 it doesn't type them \u2014 so it misspells. Check every "
         "letter. Your headline is your shop sign; a misspelled sign costs "
         "you customers."),
        "B03_ExactWords",
        "The poster shows a wobbly misspelled 'GARAG SALE'; a quote chip "
        "'GARAGE SALE' pins above it; a terracotta X stamps the wrong "
        "headline; the correct headline fades in.",
        [(0.05, "poster with wobbly 'GARAG SALE'"),
         (0.20, "quote chip '\"GARAGE SALE\"' pins above"),
         (0.45, "terracotta X stamps the wrong headline"),
         (0.65, "correct 'GARAGE SALE' fades in, ink, bold"),
         (0.85, "'exact words' label lands with leader line")],
    ),
    graphic(
        "B04", "show-tell",
        ("Step three: ask for the layout. Big headline on top, details "
         "below, and leave the bottom half empty \u2014 that's where your "
         "facts go. If you let the picture fill the whole page, there's "
         "nowhere left for the words, and a poster without words is just "
         "wallpaper."),
        "B04_Layout",
        "A fresh poster; three zones draw in: a big headline band (1), a "
        "details band (2), an empty bottom zone in ghost fill (3); numbered "
        "labels name them.",
        [(0.05, "empty poster fades in"),
         (0.15, "zone 1 'headline' band draws across the top"),
         (0.40, "zone 2 'details' band draws in the middle"),
         (0.60, "zone 3 empty zone fills ghost at the bottom"),
         (0.85, "'room for facts' label lands with leader line")],
    ),
    graphic(
        "B05", "show-tell",
        ("And here's the pro move: split the job. Have the AI draw a picture "
         "with no words in it at all \u2014 a warm morning garage scene, no "
         "text. Then you add the headline and details yourself, in any "
         "simple poster tool. AI pictures, your words. The letters are "
         "always spelled right, because a human typed them."),
        "B05_Split",
        "A picture frame on the left labeled 'AI draws'; a word poster on "
        "the right labeled 'you write'; an arrow draws from frame to "
        "poster.",
        [(0.05, "picture frame lands, labeled 'AI draws'"),
         (0.25, "word poster lands, labeled 'you write'"),
         (0.50, "arrow draws from the picture into the poster"),
         (0.80, "'split the job' label lands above")],
    ),
    graphic(
        "B06", "show-tell",
        ("Then the print checklist \u2014 three checks before you print a "
         "hundred. One: tall shape, the way paper is. Two: dark words on "
         "light paper \u2014 it reads from across the room. Three: the "
         "three-second test. Hold it at arm's length. Headline, when, where "
         "\u2014 can a stranger get all three in three seconds? If not, "
         "make the headline bigger."),
        "B06_PrintCheck",
        "The poster stands center; three terracotta checks land one by one "
        "with short labels: 'tall shape', 'dark on light', '3-second test'.",
        [(0.05, "finished poster fades in"),
         (0.15, "check 1 lands: 'tall shape'"),
         (0.45, "check 2 lands: 'dark on light'"),
         (0.70, "check 3 lands: '3-second test'"),
         (0.90, "headline pulses once, bigger")],
    ),
    graphic(
        "B07", "show-tell",
        ("One last rule: say it's AI-made. Most apps that make pictures "
         "offer an AI label \u2014 use it. The label matters most when the "
         "picture could pass for a real photo, and on a flyer for your "
         "business, honesty is the whole brand."),
        "B07_Label",
        "An 'AI-made' tag stamps onto the poster's corner with a terracotta "
        "border and a stamp ring; the label 'say it' lands beside it.",
        [(0.05, "poster fades in"),
         (0.25, "stamp ring grows on the poster corner"),
         (0.45, "'AI-made' tag stamps down, terracotta border"),
         (0.75, "'say it' label lands with leader line")],
    ),
    graphic(
        "BVDT", "recap",
        ("The recap. One: say the real job \u2014 what, when, where. Two: "
         "make the words exact, in quotes. Three: AI draws the picture, you "
         "add the words. Four: run the three checks and label it AI-made. "
         "That is a poster in an afternoon."),
        "BVDT_Recap",
        "The poster shrinks left; four numbered chips land one by one: 'say "
        "the job', 'exact words', 'AI draws, you write', 'label AI-made'.",
        [(0.05, "poster settles left"),
         (0.15, "chip 1 'say the job' lands"),
         (0.35, "chip 2 'exact words' lands"),
         (0.55, "chip 3 'AI draws, you write' lands"),
         (0.75, "chip 4 'label AI-made' lands, terracotta edge")],
    ),
    remotion(
        "BHTF", "your turn",
        ("Your turn. Paste this into Claude: I'm making a flyer for [your "
         "event \u2014 what, when, where]. Give me the five-slot picture "
         "recipe \u2014 subject, setting, style, lighting, mood \u2014 for "
         "a background with no text in the image, plus one short headline I "
         "can add myself. Then two checks yourself. One: does the picture "
         "contain any words at all? If it does, ask again for no text. Two: "
         "read your poster from across the room \u2014 headline, when, "
         "where, three seconds."),
        "ClaudeComposerAsk",
        {
            "greeting": "Your turn.",
            "topic": "CLAUDE \u00b7 YOUR TURN",
            "segment": "How to AI",
            "command": ("I'm making a flyer for [your event \u2014 what, when, "
                        "where]. Give me the five-slot picture recipe \u2014 "
                        "subject, setting, style, lighting, mood \u2014 for a "
                        "background with no text in the image, plus one short "
                        "headline I can add myself."),
            "runningText": "paste this into Claude\u2026",
            "output": [
                "Check: does the picture contain any words at all? If it "
                "does, ask again for no text.",
                "Check: read your poster from across the room \u2014 "
                "headline, when, where, three seconds.",
            ],
            "folderLabel": "@NikBearBrown",
        },
        [(0.0, "Composer opens \u2014 'Your turn.'"),
         (0.1, "the prompt types in full"),
         (0.8, "two check lines land")],
    ),
    remotion(
        "BOUT", "outro",
        "Posters and flyers. At Nik Bear Brown.",
        "ClaudeTitleOutro",
        {"title": "Posters and flyers.",
         "slug": "posters-and-flyers",
         "handle": "@NikBearBrown",
         "subline": ""},
        [(0.0, "title restates; handle")],
        extra={"kind": "outro_voice", "tail_silence_s": 1.0},
    ),
]

METADATA = {
    "title": "Posters and flyers",
    "slug": "posters-and-flyers",
    "film": 38,
    "wave": "Wave 6 \u2014 Making things",
    "series": "Humanitarians AI \u2014 how to use AI",
    "series_note": ("Wave 6 film #38; companion to film 19 'Pictures from "
                    "words', which taught the image-generation ladder and the "
                    "five-slot recipe \u2014 this film uses them without "
                    "re-teaching."),
    "skill": "show-tell",
    "style_preset": "show-tell",
    "channel": "claude-liam",
    "persona": "Liam (in for Bear)",
    "voice_kokoro": "am_onyx",
    "engine": "kokoro",
    "register": "Teardown",
    "watermark": "@NikBearBrown",
    "greeting": "Hallo",
    "palette": {"stage": "#F2F0E9", "ink": "#3D3929", "accent": "#D97757",
                "dim": "#8B8F96", "ghost": "#D9D4C7", "card": "#FAF9F5"},
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell drops the composer cold open; the "
                              "verdict card is dropped and the recap is "
                              "drawn as a BVDT beat instead of a card."),
    "playlist": "how-to-use-ai",
    "tags": ["image-generation", "posters", "flyers", "printables",
             "companion-pictures-from-words", "general-audience"],
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
}

if __name__ == "__main__":
    ids = [b["beat_id"] for b in BEATS]
    assert len(BEATS) == 13, len(BEATS)
    assert ids == ["BIDEA", "BDEFS", "B00", "B01", "B02", "B03", "B04",
                   "B05", "B06", "B07", "BVDT", "BHTF", "BOUT"], ids
    body = [b for b in BEATS if b["lane"] == "manim"]
    bookends = [b for b in BEATS if b["lane"] == "bookend"]
    assert len(body) == 9 and len(bookends) == 4, (len(body), len(bookends))
    for b in BEATS:
        assert b["voice"] == "am_onyx", b["beat_id"]  # Kokoro code, not persona
        assert b["engine"] == "kokoro", b["beat_id"]
        assert b["estimated_duration_s"] > 0, b["beat_id"]
        assert b["narration_text"].strip(), b["beat_id"]
    assert {b["shot"]["type"] for b in bookends} == {"REMOTION"}
    assert {b["shot"]["type"] for b in body} == {"GRAPHIC"}
    for b in body:
        cls = b["shot"]["manim"]["class"]
        assert cls.startswith(b["beat_id"].replace("BVDT", "BVDT")), b
        assert cls.startswith(b["beat_id"]), b["beat_id"]
    assert "Liam, in for Bear" in BEATS[0]["narration_text"], "IN-FOR-BEAR LAW"
    # hesitant-writer contract
    hw = bookends[0]["shot"]["remotion"]["props"]
    assert hw["triggerWords"] in hw["text"], "trigger must appear verbatim"
    for k in ("triggerWords", "replacementWords"):
        assert not hw[k].endswith(("?", "!", ".")), k
    # terms short enough for ClaudeDefinitions
    for t in bookends[1]["shot"]["remotion"]["props"]["terms"]:
        assert len(t["term"]) <= 17, t["term"]
    # your-turn contract
    htf = bookends[2]["shot"]["remotion"]["props"]
    assert "Paste this into Claude" in bookends[2]["narration_text"]
    assert htf["greeting"] == "Your turn." and len(htf["output"]) == 2
    assert bookends[3].get("kind") == "outro_voice"
    assert bookends[3].get("tail_silence_s") == 1.0
    # recap names the spine
    recap = next(b for b in BEATS if b["beat_id"] == "BVDT")["narration_text"].lower()
    for kw in ["what, when, where", "exact", "ai draws", "label"]:
        assert kw in recap, kw
    total = sum(b["estimated_duration_s"] for b in BEATS)
    assert 200 <= total <= 360, total
    BS = {"metadata": METADATA, "beats": BEATS}
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print(f"beats={len(BEATS)} body={len(body)} bookends={len(bookends)} "
          f"total={total:.1f}s (~{int(total//60)}m{int(total%60):02d}s)")
