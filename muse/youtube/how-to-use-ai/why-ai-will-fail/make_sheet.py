#!/usr/bin/env python3
"""make_sheet.py — build beat_sheet.json for "AI will fail." (why-ai-will-fail).

Film: Humanitarians AI YouTube channel, claude-liam brand.
Persona: Liam ("Liam, in for Bear"). TTS: Kokoro am_onyx. Register: Teardown.
Skill: ai-explainer (one tight insight: the expert-dismissal pattern -> AI).
Audience: smart, pragmatic general audience — every term explained in plain
language, show-don't-tell visuals (Manim, one scene class per beat).

Run:  python3 make_sheet.py
Writes beat_sheet.json next to this file and asserts:
  - exactly 14 beats, each with narration + a Manim scene class that exists
    in scenes.py,
  - per-beat duration in a sane band,
  - total runtime inside the 4-7 minute band (duration is an output, the band
    is a sanity gate, not a target).
"""

import json
import re
from pathlib import Path

WPS = 2.9  # planning estimate, words per second (measured Kokoro audio is the clock)
HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- beats --- #
# narration: final Liam Teardown script. shot.show: ordered visual events.
BEATS = [
    {
        "beat_id": "B00",
        "act": "COLD OPEN",
        "scene": "SceneColdOpen",
        "narration_text": (
            "This is Humanitarians AI -- Liam, in for Bear. In 1977, the founder "
            "of one of the biggest computer companies on Earth said this: "
            "'There is no reason for any individual to have a computer in his "
            "home.' He was the expert. He knew the industry cold. "
            "And he could not have been more wrong."
        ),
        "visual_intent": "Hook: the Olsen quote typeset on a card, then stamped WRONG.",
        "show": [
            {"at": "open", "event": "Cream stage; giant '1977' fades in."},
            {"at": "quote lands", "event": "Quote card draws on; the Olsen line types out letter by letter."},
            {"at": "'could not have been more wrong'", "event": "Terracotta WRONG stamp slams onto the card."},
        ],
        "terms_explained": [],
    },
    {
        "beat_id": "B01",
        "act": "OVERVIEW",
        "scene": "SceneOverview",
        "narration_text": (
            "Tonight's pattern, in one breath: for over a century, the smartest "
            "people in every industry have looked at the next big thing and "
            "said, 'that will never work' -- and been wrong, nearly every time. "
            "There's a reason, and it has a name: the better you know the current "
            "game, the worse you are at seeing the next one. Today the loudest "
            "version is three words: AI will fail."
        ),
        "visual_intent": "BLUF: a century timeline lights up; the pattern equation assembles.",
        "show": [
            {"at": "open", "event": "A timeline draws from 1925 to 2026; dots pop in at wrong-call years."},
            {"at": "'it has a name'", "event": "Three cards assemble: 'the expert is sure' + 'the future arrives' = 'wrong call'."},
        ],
        "terms_explained": [],
    },
    {
        "beat_id": "B02",
        "act": "ACT I — A CENTURY OF WRONG CALLS",
        "scene": "SceneTheList",
        "narration_text": (
            "The list runs from 1977 to 2008 and beyond. Ken Olsen, founder of "
            "computer giant DEC: no one will want a computer at home. DEC is "
            "gone; there are roughly two billion PCs. Robert Metcalfe, inventor "
            "of Ethernet, said the internet would 'catastrophically collapse' in "
            "1996. It didn't -- he blended his printed column and drank it on "
            "stage. Steve Ballmer, Microsoft's CEO: the iPhone had 'no chance.' "
            "Apple has sold over two billion."
        ),
        "visual_intent": "Four evidence cards cascade onto the timeline: year, expert, quote, outcome.",
        "show": [
            {"at": "each case", "event": "A card flips in: year stamp, name, the quote, then the outcome line in terracotta."},
            {"at": "Metcalfe", "event": "A blender-ish swirl mark draws over the 1995 card -- he drank his words."},
        ],
        "terms_explained": ["Ethernet: the wiring standard that lets computers talk on a local network"],
    },
    {
        "beat_id": "B03",
        "act": "ACT I — A CENTURY OF WRONG CALLS",
        "scene": "SceneBlockbuster",
        "narration_text": (
            "My favorite: 2008, Jim Keyes, CEO of Blockbuster: 'I've been frankly "
            "confused by this fascination that everybody has with Netflix.' "
            "Streaming -- movies over the internet, no store, no late fees -- "
            "looked like a toy to him. Netflix went on to pass three hundred "
            "million subscribers. Blockbuster has exactly one store left. It's in "
            "Bend, Oregon. People visit it like a museum."
        ),
        "visual_intent": "Split screen: the Keyes quote left; Netflix counter climbs right; Blockbuster shrinks to one dot.",
        "show": [
            {"at": "quote", "event": "Keyes quote card draws on the left, verbatim."},
            {"at": "'three hundred million'", "event": "A terracotta counter spins up to 300M+ on the right."},
            {"at": "'one store left'", "event": "The Blockbuster square shrinks to a single dot labeled 'Bend, Oregon'."},
        ],
        "terms_explained": ["streaming: movies over the internet, no store, no late fees"],
    },
    {
        "beat_id": "B04",
        "act": "ACT I — A CENTURY OF WRONG CALLS",
        "scene": "SceneEllisonValenti",
        "narration_text": (
            "Same year, Larry Ellison, CEO of Oracle, on cloud computing -- "
            "renting computers over the internet instead of owning them: 'It's "
            "complete gibberish. It's insane. When is this idiocy going to stop?' "
            "The cloud became a market of hundreds of billions a year, and "
            "Oracle now sells tens of billions of it -- to power AI, ironically. "
            "In 1982, Hollywood's top lobbyist called the VCR 'the Boston "
            "strangler' to filmmakers. Home video went on to earn Hollywood more "
            "than the box office."
        ),
        "visual_intent": "Two quote cards; each gets its outcome banner sliding in underneath.",
        "show": [
            {"at": "Ellison quote", "event": "Left card: Ellison quote; outcome banner slides in: 'cloud: hundreds of billions/yr -- Oracle sells it now'."},
            {"at": "Valenti quote", "event": "Right card: Valenti quote; outcome banner slides in: 'home video > box office'."},
        ],
        "terms_explained": ["cloud computing: renting computers over the internet instead of owning them", "VCR: the box that played movies on tape at home"],
    },
    {
        "beat_id": "B05",
        "act": "ACT I — A CENTURY OF WRONG CALLS",
        "scene": "ScenePenicillin",
        "narration_text": (
            "And it's not just businessmen. In 1941, the British Medical Journal "
            "-- the most respected medical journal in the world -- reviewed the "
            "biggest study yet of penicillin and concluded it had no use beyond "
            "the laboratory. Penicillin went on to become the most important "
            "drug of the twentieth century, saving hundreds of millions of "
            "lives. The gatekeepers of knowledge, writing in their own journal, "
            "got it completely wrong."
        ),
        "visual_intent": "The 1941 journal page dissolves into a field of dots: lives saved.",
        "show": [
            {"at": "open", "event": "A journal page fades in; the 1941 BMJ verdict types across it."},
            {"at": "'most important drug'", "event": "The page dissolves; a grid of dots blooms -- each a stand-in for lives saved."},
        ],
        "terms_explained": ["penicillin: the first widely used antibiotic, the mold drug that kills bacteria"],
    },
    {
        "beat_id": "B06",
        "act": "ACT II — WHY SMART PEOPLE GET IT WRONG",
        "scene": "SceneInsiderTrap",
        "narration_text": (
            "Why does this keep happening? These weren't stupid people. They "
            "were the best in the world at the current game -- and that was the "
            "problem. Blockbuster's CEO understood video rental better than "
            "anyone alive. But Netflix wasn't a better Blockbuster. It was a "
            "different game entirely: no stores, no late fees, movies by mail, "
            "then the internet. Grade the new thing on the old game's scoreboard, "
            "and it always looks like a toy."
        ),
        "visual_intent": "Diagram: the incumbent optimizes the old axis; the newcomer enters on a new axis the old scoreboard cannot see.",
        "show": [
            {"at": "open", "event": "Bars grow on the 'old game' axis: stores, late fees -- Blockbuster's scoreboard."},
            {"at": "'different game entirely'", "event": "A new curve enters from the side on its own axis -- no stores, by mail, then internet."},
            {"at": "'always looks like a toy'", "event": "A dashed line from the old scoreboard reaches for the new curve and misses; a '?' appears."},
        ],
        "terms_explained": ["the old game's scoreboard: judging the new thing by the old industry's metrics"],
    },
    {
        "beat_id": "B07",
        "act": "ACT II — WHY SMART PEOPLE GET IT WRONG",
        "scene": "SceneToyCurve",
        "narration_text": (
            "Here's what the skeptics get right: the new thing usually IS bad at "
            "first. Early streaming video was a pixelated, buffering mess -- the "
            "skeptics had real evidence. But they were measuring a snapshot, not "
            "a trajectory. What matters isn't how good it is today. It's the "
            "direction it's moving, and how fast. 'Bad now' and 'failing' are not "
            "the same thing. Everything on that list of wrong calls looked like "
            "a toy -- right up until it didn't."
        ),
        "visual_intent": "The toy curve: quality over time. Skeptic pins at the low end; the trajectory arrow rockets up.",
        "show": [
            {"at": "open", "event": "Axes draw: time vs quality. A curve crawls, then bends sharply upward."},
            {"at": "'pixelated, buffering mess'", "event": "Pins drop on the low end: 'pixel soup', 'buffering', 'will fail'."},
            {"at": "'direction it's moving'", "event": "A terracotta arrow rides the curve upward, labeled 'trajectory'."},
        ],
        "terms_explained": ["snapshot vs trajectory: one frozen moment vs the direction and speed of travel"],
    },
    {
        "beat_id": "B08",
        "act": "ACT III — THE AI SKEPTICS",
        "scene": "SceneFamiliarForm",
        "narration_text": (
            "Now listen to today's AI skeptics with that pattern in your ear. "
            "'AI hallucinates' -- it makes things up, confidently: invented "
            "court cases, hands with six fingers. That's the pixel-soup stage. "
            "'The productivity gains don't show in the data' -- in 1987 an "
            "economist said the same of computers: 'you can see the computer "
            "age everywhere but in the productivity statistics.' Daron Acemoglu "
            "now estimates AI adds half a percent to productivity over a decade. "
            "Maybe. Or maybe that's a snapshot."
        ),
        "visual_intent": "Then/now pairs: each old dismissal is wired to its modern twin.",
        "show": [
            {"at": "open", "event": "'THEN' cards fade in left: streaming pixel soup, Solow 1987 productivity."},
            {"at": "'today's AI skeptics'", "event": "'NOW' cards fade in right: AI hallucinates, Acemoglu 2024."},
            {"at": "each pair", "event": "Terracotta arrows wire each THEN card to its NOW twin."},
        ],
        "terms_explained": [
            "hallucinate: when the AI makes things up and states them confidently",
            "productivity statistics: the official numbers tracking output per worker",
        ],
    },
    {
        "beat_id": "B09",
        "act": "ACT III — THE AI SKEPTICS",
        "scene": "SceneHonestPart",
        "narration_text": (
            "Let's be fair, the Teardown way: the skeptics are describing the "
            "present accurately. AI really does write like a genius one minute "
            "and a confused kid the next. Ted Chiang called it 'a blurry JPEG "
            "of the web.' That stings because it's partly true. The question "
            "the pattern forces isn't 'is AI flawed today?' -- it is. The "
            "question is: are you judging a trajectory by a snapshot? When "
            "smart people confuse the two, history says bet on the trajectory."
        ),
        "visual_intent": "A frozen 'snapshot' frame vs a film strip of the trajectory; the verdict ring lands on the trajectory.",
        "show": [
            {"at": "open", "event": "Left: a photo frame freezes one low point of the curve -- 'AI today: flawed'."},
            {"at": "'trajectory by a snapshot'", "event": "Right: a three-frame film strip shows the curve climbing -- motion, not a moment."},
            {"at": "'bet on the trajectory'", "event": "A terracotta ring draws around the film strip."},
        ],
        "terms_explained": ["a blurry JPEG of the web: looks right at a glance, falls apart when you zoom in"],
    },
    {
        "beat_id": "B10",
        "act": "ACT IV — THE ASYMMETRIC BET",
        "scene": "SceneAsymmetricBet",
        "narration_text": (
            "So what do you do? Run the bet both ways. If AI turns out to matter "
            "and you learned it -- you're ready. If it matters and you waited -- "
            "you're catching up from behind, in a faster market. If it's "
            "overhyped and you learned it -- you lost some hours and picked up a "
            "useful skill. If it's overhyped and you ignored it -- you saved "
            "those hours. Three of the four futures reward learning. The "
            "downside of learning is small. The downside of dismissing is large."
        ),
        "visual_intent": "A 2x2 payoff matrix fills in; three cells check, one doesn't.",
        "show": [
            {"at": "open", "event": "The 2x2 grid draws: rows 'AI matters / AI is hype', columns 'you learned / you waited'."},
            {"at": "each future", "event": "Cells fill: 'ready', 'catching up', 'lost some hours', 'saved some hours'."},
            {"at": "'three of the four'", "event": "Terracotta checks land on three cells; a banner: 'learning is cheap; dismissing is expensive'."},
        ],
        "terms_explained": ["asymmetric bet: the two mistakes don't cost the same"],
    },
    {
        "beat_id": "B11",
        "act": "VERDICT",
        "scene": "SceneVerdict",
        "narration_text": (
            "Here's the verdict. One: for a century, confident experts have "
            "declared the future dead on arrival -- and been wrong nearly every "
            "time. Two: the mechanism is the insider trap -- the better you know "
            "the current game, the worse you see the next one. Three: judge the "
            "trajectory, not the snapshot. Four: the bet is asymmetric -- "
            "learning is cheap, dismissing is expensive. One question to carry "
            "with you: am I scoring the new thing on the old game's scoreboard?"
        ),
        "visual_intent": "The verdict card: four takeaways check off in sequence.",
        "show": [
            {"at": "each point", "event": "A terracotta dot checks in beside each verdict line, in narration order."},
        ],
        "terms_explained": [],
    },
    {
        "beat_id": "B12",
        "act": "YOUR TURN",
        "scene": "SceneYourTurn",
        "narration_text": (
            "Your turn. Take this prompt to Claude -- or any AI you use -- and "
            "run the pattern on today's skepticism yourself: 'Find the five "
            "most common reasons people say AI will fail. For each one: give me "
            "the strongest version of the argument, the past technology it most "
            "resembles, and what would prove it right or wrong. Be a fair "
            "referee.' Read the answer twice -- once for the arguments, once "
            "for the resemblances. That's the pattern, working for you now."
        ),
        "visual_intent": "The handoff prompt types itself onto a card, ready to copy.",
        "show": [
            {"at": "open", "event": "A prompt card draws on; the header reads 'Your turn -- try it yourself'."},
            {"at": "prompt read", "event": "The prompt types out line by line as Liam reads it aloud."},
            {"at": "close", "event": "A footer fades in: 'paste this into Claude...'."},
        ],
        "terms_explained": [],
    },
    {
        "beat_id": "B13",
        "act": "OUTRO",
        "scene": "SceneOutro",
        "narration_text": "AI will fail. Liam, in for Bear -- at Nik Bear Brown.",
        "visual_intent": "Title restate, poster-style, with the terracotta period and the @NikBearBrown handle.",
        "show": [
            {"at": "open", "event": "'AI will fail.' writes on, the period landing in terracotta."},
            {"at": "sign-off", "event": "A rule draws; '@NikBearBrown' fades in beneath."},
        ],
        "terms_explained": [],
    },
]

METADATA = {
    "title": "AI will fail.",
    "slug": "why-ai-will-fail",
    "topic": "AI SKEPTICS",
    "brand": "claude-liam",
    "channel": "https://www.youtube.com/@humanitariansai",
    "channel_identifier": "claude-liam",
    "persona": "Liam",
    "greeting": "Liam, in for Bear",
    "voice": "am_onyx",
    "voice_kokoro": "am_onyx",
    "engine": "kokoro",
    "register": "Teardown",
    "watermark": "@NikBearBrown",
    "skill": "ai-explainer",
    "audience": "smart, pragmatic general audience; every term explained in plain language",
    "derived_from": "nikbearbrown/humanitarians-youtube-muse:claude-for-artificial-intelligence/why-ai-will-fail",
}


def word_count(text):
    return len(re.findall(r"[A-Za-z0-9']+", text))


def build_sheet():
    beats = []
    for b in BEATS:
        words = word_count(b["narration_text"])
        duration = round(words / WPS, 1)
        beats.append(
            {
                "beat_id": b["beat_id"],
                "act": b["act"],
                "scene": b["scene"],
                "voice": "am_onyx",
                "engine": "kokoro",
                "narration_text": b["narration_text"],
                "word_count": words,
                "estimated_duration_s": duration,
                "shot": {
                    "type": "MANIM",
                    "source": "own",
                    "scene_class": b["scene"],
                    "visual_intent": b["visual_intent"],
                    "show": b["show"],
                    "terms_explained": b["terms_explained"],
                },
            }
        )
    return {"metadata": METADATA, "beats": beats}


def main():
    sheet = build_sheet()
    beats = sheet["beats"]
    total = round(sum(b["estimated_duration_s"] for b in beats), 1)

    # ---- assertions: beat count, durations, scene coverage ---- #
    assert len(beats) == 14, f"expected 14 beats, got {len(beats)}"
    for b in beats:
        d = b["estimated_duration_s"]
        assert 3.0 <= d <= 45.0, f"{b['beat_id']}: duration {d}s outside 3-45s band"
        assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
        assert b["shot"]["scene_class"], f"{b['beat_id']}: missing scene class"
    assert 240.0 <= total <= 420.0, f"total {total}s outside 240-420s band"

    # every beat's scene class must exist in scenes.py
    src = (HERE / "scenes.py").read_text()
    found = set(re.findall(r"^class (\w+)\(Scene\)", src, re.M))
    missing = [b["scene"] for b in beats if b["scene"] not in found]
    assert not missing, f"scene classes missing from scenes.py: {missing}"

    # beat ids unique, ordered
    ids = [b["beat_id"] for b in beats]
    assert len(set(ids)) == len(ids), "duplicate beat ids"

    out = HERE / "beat_sheet.json"
    out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")

    print(f"beats: {len(beats)}")
    for b in beats:
        print(f"  {b['beat_id']:>4}  {b['word_count']:>3}w  {b['estimated_duration_s']:>5.1f}s  {b['scene']}")
    print(f"total estimated runtime: {total:.1f}s ({total/60:.1f} min)")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
