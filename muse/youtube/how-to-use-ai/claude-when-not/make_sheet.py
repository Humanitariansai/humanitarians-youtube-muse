#!/usr/bin/env python3
"""make_sheet.py — "Claude, When Not." (general-audience show-tell film).

Builds beat_sheet.json: 13 beats, show-tell style, Teardown register.
Source: nikbearbrown/humanitarians-youtube-muse, Claude-for-students season
finale "Claude, When Not." (hai-when-not) — reframed from student-specific
to a smart, pragmatic general audience. Series context (H1-H5) removed; the
argument stands alone in the "How to use AI" playlist.

Beat sheet keys follow the show-tell skill: beat_id / narration_text /
estimated_duration_s / audio_file / lane / shot.manim.class / qc.
Durations: ~150 wpm speech (2.5 words/s) + 1.0 s beat pause; BOUT gets the
1.0 s spoken outro tail. Assertions: 13 beats, total duration band, the
BIDEA greeting, unique beat ids, every narration non-empty.
"""
import json

WPS = 2.5   # words per second, Kokoro am_onyx pacing
PAUSE = 1.0  # beat pause

BEATS = [
    {
        "beat_id": "BIDEA", "act": "hook", "voice": "Liam",
        "narration_text": (
            "Hallo. This is Liam, in for Bear. Here is the naive version of "
            "this film: let AI do everything for you. And here is the real one: "
            "learn when not to use it. That gap is the whole film."
        ),
        "screen": "Writer types 'let AI do everything for me', strikes it, "
                  "writes 'learn when NOT to use it'.",
        "lane": "manim", "scene_class": "BIDEA_HesitantWriter",
    },
    {
        "beat_id": "BDEFS", "act": "hook", "voice": "Liam",
        "narration_text": (
            "Four terms, in plain words. A scaffold is a support that helps you "
            "climb — you still do the climbing. A crutch is a prop that does "
            "the work instead of you. A hallucination is when an AI invents a "
            "fact and says it confidently. And disclosure just means saying "
            "plainly where the AI helped."
        ),
        "screen": "Four term cards: scaffold / crutch / hallucination / disclosure.",
        "lane": "manim", "scene_class": "BDEFS_Terms",
    },
    {
        "beat_id": "B01", "act": "1", "voice": "Liam",
        "narration_text": (
            "Here is the thesis, and it is short. The real AI skill is not "
            "using AI more. It is knowing when not to use it. Everything else "
            "in this film hangs off that one line."
        ),
        "screen": "A ladder; a figure climbs; a terracotta check lands at the top.",
        "lane": "manim", "scene_class": "B01_Thesis",
    },
    {
        "beat_id": "B02", "act": "2", "voice": "Liam",
        "narration_text": (
            "So: when to use it. Use Claude for leverage. Quiz yourself on your "
            "own material. Get feedback on a draft you wrote. Ask it to explain "
            "things that confuse you. Generate practice problems. Plan and "
            "schedule. In every one of these, you are in the driver's seat. "
            "That is a scaffold."
        ),
        "screen": "Scaffold frame draws around the ladder; five rungs light up, "
                  "one per spoken use; 'scaffold' label.",
        "lane": "manim", "scene_class": "B02_UseList",
    },
    {
        "beat_id": "B03", "act": "2", "voice": "Liam",
        "narration_text": (
            "And when not to. Do not use it for work you would hand in without "
            "saying the AI helped — skipping disclosure is the line. Not for "
            "the first draft of anything you are supposed to learn by drafting. "
            "Not for facts you will not check. And not for anything you would "
            "hide. That last one is the test."
        ),
        "screen": "The figure leans on a crutch; a page slips; 'crutch' label; "
                  "an ink cross lands on the page.",
        "lane": "manim", "scene_class": "B03_DontList",
    },
    {
        "beat_id": "B04", "act": "2", "voice": "Liam",
        "narration_text": (
            "Here is the one question that collapses all of it. Would you hide "
            "this use from your boss, your client, or your readers? If yes — "
            "do not do it. Not because you will get caught. Because the hiding "
            "means the use is taking something that was supposed to be yours: "
            "the skill, the learning, the accountability."
        ),
        "screen": "Figure holds a page openly; a second page slides behind its "
                  "back; a terracotta ring spotlights the hidden page.",
        "lane": "manim", "scene_class": "B04_HideTest",
    },
    {
        "beat_id": "B05", "act": "2", "voice": "Liam",
        "narration_text": (
            "Take drafting. If you are supposed to learn to write, and Claude "
            "writes the first draft, you skipped the class — because the "
            "drafting was the thinking. Reading a finished draft teaches you "
            "almost nothing. Writing it is what teaches you the thing."
        ),
        "screen": "A page; draft lines draw in one by one; a crutch arrives and "
                  "a strike crosses the lines.",
        "lane": "manim", "scene_class": "B05_DraftExample",
    },
    {
        "beat_id": "B06", "act": "2", "voice": "Liam",
        "narration_text": (
            "Or take facts. Claude can invent a citation, a date, a quote, and "
            "deliver it with total confidence. Researchers call that "
            "hallucination. So the rule is simple: if you will not check a "
            "fact, do not ask Claude for it. Your name on the output means you "
            "checked."
        ),
        "screen": "A page of ghost lines; a magnifier sweeps over it; a "
                  "terracotta check lands with 'check it'.",
        "lane": "manim", "scene_class": "B06_Verify",
    },
    {
        "beat_id": "B07", "act": "3", "voice": "Liam",
        "narration_text": (
            "Commit before the answer. Which of these is a do-not-use? A: quiz "
            "me on a chapter. B: write my report. C: explain a confusing "
            "concept. D: give feedback on my draft. One of these skips the "
            "learning that was supposed to be yours. Pick it now."
        ),
        "screen": "Four option cards in a row: A quiz / B write / C explain / D feedback.",
        "lane": "manim", "scene_class": "B07_Predict",
    },
    {
        "beat_id": "B08", "act": "3", "voice": "Liam",
        "narration_text": (
            "It is B. Writing your report skips the drafting, and the drafting "
            "was the skill. A, C, and D are all scaffold uses — quizzing, "
            "explaining, feedback. You stay in the driver's seat, and Claude "
            "stays a tool."
        ),
        "screen": "Card B slides away; terracotta checks land on A, C, D; the "
                  "ladder stands under them.",
        "lane": "manim", "scene_class": "B08_Answer",
    },
    {
        "beat_id": "B09", "act": "3", "voice": "Liam",
        "narration_text": (
            "So draw the line here. Use AI for leverage, to climb higher than "
            "you could alone. Do not use it in place of the thing you are "
            "supposed to learn. Scaffold, not crutch. That is the whole card."
        ),
        "screen": "A vertical line draws down the frame: ladder and scaffold on "
                  "the left, crutch on the right; a terracotta check on the left.",
        "lane": "manim", "scene_class": "B09_Line",
    },
    {
        "beat_id": "BHTF", "act": "do_today", "voice": "Liam",
        "narration_text": (
            "Your turn. Paste this into Claude: list five things I use you for "
            "each week. Run each through the hide-it test — would I hide this "
            "use from my boss? Mark each one scaffold or crutch. Then run your "
            "own checks: does its verdict match your gut, and would you tape "
            "its one-sentence summary to your laptop?"
        ),
        "screen": "A drawn Claude.ai composer; the prompt types in; two check "
                  "lines appear: your gut, the laptop test.",
        "lane": "manim", "scene_class": "BHTF_YourTurn",
    },
    {
        "beat_id": "BOUT", "act": "outro", "voice": "Liam",
        "narration_text": "Claude, When Not. From Humanitarians AI. Liam, in for Bear.",
        "screen": "Title 'Claude, When Not.'; the watermark @NikBearBrown.",
        "lane": "manim", "scene_class": "BOUT_Outro",
    },
]

METADATA = {
    "title": "Claude, When Not.",
    "slug": "claude-when-not",
    "skill": "show-tell",
    "style_preset": "show-tell",
    "register": "Teardown",
    "channel": "claude-liam",
    "persona": "Liam (in for Bear)",
    "voice": "am_onyx",
    "engine": "kokoro",
    "watermark": "@NikBearBrown",
    "playlist": "How to use AI",
    "topic": "CLAUDE · WHEN NOT TO USE AI",
    "thesis": "Knowing when NOT to use it IS the AI skill.",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": (
        "show-tell bookends are drawn Manim scenes (hesitant writer, term cards, "
        "drawn composer, spoken outro) rather than Remotion interface scenes — "
        "single-renderer pipeline, same as the other general-audience redos."
    ),
}


def dur_s(text, extra=PAUSE):
    return round(len(text.split()) / WPS + extra)


def build():
    beats = []
    for b in BEATS:
        d = dict(b)
        est = dur_s(b["narration_text"])
        if b["beat_id"] == "BOUT":
            est += 1  # spoken-outro tail pad
        d["estimated_duration_s"] = est
        d["audio_file"] = f"mp3/beat-{b['beat_id']}.mp3"
        d["shot"] = {
            "type": "MANIM",
            "manim": {"class": b["scene_class"]},
        }
        # show-tell sparse waiver: one hero object on cream underfills Gate V.
        if b["beat_id"] not in ("BDEFS", "B07"):
            d["qc"] = {
                "sparse_by_design": True,
                "sparse_reason": "show-tell single-hero-object composition; "
                                 "waives Gate V underfill and clustered only",
            }
        beats.append(d)
    return {"metadata": METADATA, "beats": beats}


if __name__ == "__main__":
    sheet = build()
    beats = sheet["beats"]
    ids = [b["beat_id"] for b in beats]
    assert len(beats) == 13, len(beats)
    assert len(set(ids)) == 13, "duplicate beat ids"
    for b in beats:
        assert b["narration_text"].strip(), b["beat_id"]
        assert b["shot"]["manim"]["class"].startswith(b["beat_id"]), b["beat_id"]
    bidea = beats[0]
    assert bidea["beat_id"] == "BIDEA"
    assert bidea["narration_text"].startswith("Hallo."), "greeting"
    assert "Liam, in for Bear" in bidea["narration_text"], "persona lock"
    total = sum(b["estimated_duration_s"] for b in beats)
    assert 170 <= total <= 260, f"total {total}s outside 2:50-4:20 band"
    with open("beat_sheet.json", "w") as f:
        json.dump(sheet, f, indent=2)
    print(f"beats={len(beats)} total={total}s (~{total//60}m{total%60:02d}s)")
    print("beat_sheet.json written")
