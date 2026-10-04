#!/usr/bin/env python3
"""make_sheet.py — Trust, but verify (Film 21, "How to AI").

Builds beat_sheet.json: 10 beats, three acts, ~266 s.
Run: python3 make_sheet.py
Durations: ~150 wpm speech plus ~2 s of breathing room per beat.

Film identity: Persona Liam ("Liam, in for Bear"); Kokoro am_onyx;
Teardown register; channel claude-liam; watermark @NikBearBrown.
"""
import json
from pathlib import Path

BEATS = [
    {
        "id": "BIDEA", "scene": "M01", "dur_s": 29, "act": "hook",
        "voice": "Muse",
        "line": "This is Liam, in for Bear. Watch this. An AI assistant just told a friend of mine \u2014 with total confidence \u2014 that humans only use ten percent of their brains. He believed it. He'd heard it before. And it's completely false. That mix \u2014 confident machine, true-sounding claim \u2014 is why you need a habit. Not hope. A sixty-second habit. This film builds it with you.",
        "screen": "Chat card with the confident 10%-of-brain claim; a red X draws across it; a FALSE tag plate lands."
    },
    {
        "id": "BDEFS", "scene": "M02", "dur_s": 30, "act": "hook",
        "voice": "Muse",
        "line": "Five terms, twenty seconds. A hallucination is the AI inventing something that sounds true \u2014 not lying, inventing. Confident tone is the machine sounding sure; it's a style, not a fact. A primary source is where the fact actually lives \u2014 the study, the filing, the dataset. An independent check is a second source that didn't copy the first. And stakes: what it costs you if the claim is wrong.",
        "screen": "Five stacked term plates appear one by one: hallucination / confident tone / primary source / independent check / stakes."
    },
    {
        "id": "B01", "scene": "M03", "dur_s": 30, "act": "1",
        "voice": "Muse",
        "line": "Step one: ask how sure it is, and what would change its mind. Ask, 'How confident are you in that?' A good answer gives a number and the evidence behind it. A bad answer does something revealing \u2014 it stays at one hundred percent while showing you nothing. An honest expert hedges. And if it can't name what would prove it wrong, it's not an expert. It's a rumor.",
        "screen": "Two confidence meters: 100%-with-no-evidence struck through; 60%-with-evidence checked."
    },
    {
        "id": "B02", "scene": "M04", "dur_s": 32, "act": "1",
        "voice": "Muse",
        "line": "Step two: ask for the source \u2014 then actually open it. Here's the demo. I asked an AI for sleep tips. It answered, quote: 'A 2023 study in the Journal of Sleep Medicine found that a banana before bed helps you fall asleep forty percent faster.' Plausible. Footnoted. I opened the link \u2014 a dead page. No study, no journal issue. The claim evaporated on step two. A citation you never open is decoration.",
        "screen": "Answer card with the banana-sleep claim and footnote link; cursor taps it; 404 dead-page card; claim struck through and greys out."
    },
    {
        "id": "B03", "scene": "M05", "dur_s": 27, "act": "2",
        "voice": "Muse",
        "line": "Step three: cross-check with one independent search \u2014 typed by you, not the AI. Asking the same machine to verify its own work is like letting a student grade their own exam. Search the claim yourself, and look for a source that didn't copy the first one. Two independent sources saying the same thing? The claim has legs. One echo chamber? It doesn't.",
        "screen": "Three source cards: A and B earn green checks; C (copied A) gets a red X and an echo tag."
    },
    {
        "id": "B04", "scene": "M06", "dur_s": 27, "act": "2",
        "voice": "Muse",
        "line": "Step four, for numbers: make it show its work. A number with no date and no math is a magic trick. Ask two questions \u2014 when was this measured, and how did you get it? If it can't show the arithmetic \u2014 the dataset, the formula, the steps \u2014 treat the number as a rumor with good lighting. Real math leaves footprints.",
        "screen": "Big 40% card; WHEN and HOW plates fly in; hollow dataset\u2192formula\u2192steps flow; a ? plate greys the number."
    },
    {
        "id": "B05", "scene": "M07", "dur_s": 26, "act": "2",
        "voice": "Muse",
        "line": "Now the calibration \u2014 because nobody has time to do this for everything. Match the checking to the stakes. Trivia for a quiz night? Let it ride. A medical claim, a money decision, a fact you'll repeat to someone else? Run all four steps. Low stakes, light touch. High stakes, full habit. Sixty seconds for anything that could cost you.",
        "screen": "Stakes bar low\u2192high; quiz-night zone vs health/money zone; marker slides to the high zone."
    },
    {
        "id": "B06", "scene": "M08", "dur_s": 25, "act": "3",
        "voice": "Muse",
        "line": "Here's your card. One \u2014 how sure are you, and what would change your mind? Two \u2014 show me the source, and open it. Three \u2014 cross-check with one independent search. Four \u2014 numbers show their work. Sixty seconds, four questions. The AI is a brilliant intern with no shame. You stay the editor. That's the whole job.",
        "screen": "The habit card: four numbered rows land one by one; the whole habit on one card."
    },
    {
        "id": "B07", "scene": "M09", "dur_s": 33, "act": "3",
        "voice": "Muse",
        "line": "Your turn. Copy this into your AI app: 'From now on, when one of your claims could change a real decision, attach your confidence level, your source, and what would change your mind. If you don't know, say so.' That teaches the machine your standard. Run it on the next claim that matters \u2014 a health tip, a price, a fact for work \u2014 and watch which step catches something. Liam, in for Bear. You've got the habit.",
        "screen": "Your turn. composer with the paste-ready prompt; use-case chips: a health tip \u00b7 a price \u00b7 a fact for work."
    },
    {
        "id": "B08", "scene": "M10", "dur_s": 7, "act": "3",
        "voice": "Muse",
        "line": "Trust, but verify. At Nik Bear Brown. This was Liam, in for Bear.",
        "screen": "Title card: Trust, but verify. @NikBearBrown; Liam, in for Bear. sign-off."
    },
]

META = {
    "title": "Trust, but verify",
    "slug": "trust-but-verify",
    "film": 21,
    "series": "Humanitarians AI \u2014 How to AI",
    "audience": "smart, pragmatic general audience (non-AI-experts)",
    "skill": "ai-explainer",
    "engine": "kokoro",
    "voice_kokoro": "am_onyx",
    "voice_note": "Synthetic Kokoro voice (am_onyx) narrating as Liam, in for Bear.",
    "persona": "Muse",
    "register": "Teardown",
    "channel": "claude-liam",
    "watermark": "@NikBearBrown",
    "palette": {"ink": "#111111", "paper": "#F7F3EA", "accent": "#B8472F",
                "blue": "#2F6BB8", "green": "#2E8B57", "grey": "#8A8578",
                "card": "#FFFFFF"},
    "aspect_ratio": "16:9",
    "derived_from": "fellows/aujaswi-a/2026-08-19-how-to-spot-unreliable-ai-research (REFACTOR for general audience)",
}


def main():
    assert len(BEATS) == 10, f"expected 10 beats, got {len(BEATS)}"
    ids = [b["id"] for b in BEATS]
    assert len(set(ids)) == len(ids), "duplicate beat ids"
    for b, want in zip(BEATS, [f"M{i:02d}" for i in range(1, 11)]):
        assert b["scene"] == want, f'{b["id"]}: scene {b["scene"]} != {want}'
        assert b["dur_s"] > 0 and b["line"].strip(), f'{b["id"]}: bad duration/line'
        assert b["voice"] == "Muse", f'{b["id"]}: voice must be Muse'
    total = sum(b["dur_s"] for b in BEATS)
    assert 180 <= total <= 360, f"runtime {total}s outside 3\u20136 min window"
    assert total == 266, f"expected 266 s total, got {total}"
    # verdict beat must carry all four habit steps
    verdict = next(b for b in BEATS if b["id"] == "B06")["line"]
    for needle in ["how sure are you", "source", "independent search", "show their work"]:
        assert needle in verdict, f"verdict missing: {needle}"
    sheet = {"metadata": META, "beats": BEATS}
    out = Path(__file__).parent / "beat_sheet.json"
    out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {out}: {len(BEATS)} beats, {total} s")


if __name__ == "__main__":
    main()
