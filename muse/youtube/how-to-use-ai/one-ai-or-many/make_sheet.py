#!/usr/bin/env python3
"""make_sheet.py — "One AI or many?" (#24 of 24, how-to-use-ai).

Builds beat_sheet.json: 12 beats, three acts. Run: python3 make_sheet.py
Durations: narration at ~150 wpm (2.5 wps), rounded up, plus small pauses;
body beats ~22-27 s. ai-explainer skill, Liam in for Bear, am_onyx.
Companion: everyone-wants-one-ai ("ChatGPT or Claude?") — referenced, not contradicted.
"""
import json

BS = {
    "title": "One AI or many?",
    "film": "one-ai-or-many",
    "series": "Humanitarians AI — how-to-use-ai (general-audience redos)",
    "skill": "ai-explainer",
    "channel": "claude-liam",
    "persona": "Liam",
    "in_for_bear": True,
    "voice_kokoro": "am_onyx",
    "register": "Teardown",
    "watermark": "@NikBearBrown",
    "greeting": "Ciao, Liam",
    "beats": [
        {
            "id": "B00", "scene": "M01", "dur_s": 18, "act": "hook",
            "voice": "Liam",
            "line": "Ciao. This is Liam, in for Bear. Everyone wants one AI \u2014 one subscription, one app, done. But the wrong question will eat your week: which AI is best? Here is the liberating truth, up front.",
            "screen": "Composer sketch: window, 'Ciao, Liam', typed question, three short answer lines fade in."
        },
        {
            "id": "B01", "scene": "M02", "dur_s": 24, "act": "hook",
            "voice": "Liam",
            "line": "Here\u2019s the whole film in one breath. For most everyday work, the differences between the top AI tools are smaller than the difference between using one well and using one badly. So stop shopping. Pick one, learn it properly, and only add a second when you hit a specific wall. That\u2019s the film. Now the details.",
            "screen": "Writer types 'The question isn\u2019t which AI is smartest.' \u2014 'smartest.' struck, replaced by 'It\u2019s whether you\u2019ve learned to use one well.'"
        },
        {
            "id": "B02", "scene": "M03", "dur_s": 24, "act": "1",
            "voice": "Liam",
            "line": "Four words, plain. An AI tool: the app you talk to \u2014 the one you pay for. A prompt: what you type into it. A wall: a job your tool genuinely cannot do \u2014 real walls are rare, and specific. And a leaderboard: a chart scoring AI tools, which goes stale every few weeks. That\u2019s the vocabulary.",
            "screen": "Four term cards land one by one: AI tool / prompt / wall / leaderboard."
        },
        {
            "id": "B03", "scene": "M04", "dur_s": 26, "act": "1",
            "voice": "Liam",
            "line": "Picture two gaps. The gap between the best AI tool and the second best: small \u2014 a few percentage points on a chart, invisible in your actual week. Now the gap between using your tool well and using it badly: huge. Same tool, same subscription, totally different results. One of those gaps is worth your evenings. It is not the first one.",
            "screen": "Small near-equal bar pair ('the gap between tools') vs wide bar pair ('the gap between users'); terracotta accents the large pair."
        },
        {
            "id": "B04", "scene": "M05", "dur_s": 24, "act": "2",
            "voice": "Liam",
            "line": "And that chart the winner came from? It has a shelf life. Top AI tools trade places every few weeks \u2014 new releases, new scores, new king. Chasing the leaderboard is chasing a finish line that moves while you run. Your evenings go in; nothing stays learned.",
            "screen": "Podium of three generic tool icons; month labels M1/M2/M3, a different icon on the top step each month."
        },
        {
            "id": "B05", "scene": "M06", "dur_s": 26, "act": "2",
            "voice": "Liam",
            "line": "Here\u2019s the part nobody selling you a switch will say: your skill transfers. How to ask well, how to judge a draft, when to push back, when to stop \u2014 none of that lives inside one app. Learn it once, carry it to any tool, including next year\u2019s winner. That is why the leaderboard can change under you and you stay standing.",
            "screen": "Toolbox 'your skill' with four tiles (ask well / judge drafts / push back / know when to stop) slides from Tool A to Tool B to 'next year\u2019s winner'."
        },
        {
            "id": "B06", "scene": "M07", "dur_s": 27, "act": "2",
            "voice": "Liam",
            "line": "So the rule. One: pick the AI you already have \u2014 the one your company pays for, or the one sitting on your phone. Two: learn it properly. This series teaches you how: asking well, showing examples, checking the draft. A year with one tool, used seriously, beats a month each with twelve.",
            "screen": "Rule card: big '1' \u2014 'pick the one you have'; checklist lands: ask well, show examples, check the draft; 'this series teaches you how'."
        },
        {
            "id": "B07", "scene": "M08", "dur_s": 27, "act": "2",
            "voice": "Liam",
            "line": "Now the honest exception: sometimes one tool can\u2019t do the job. There are four walls worth a second. One: serious image work, and yours is weak there. Two: heavy coding. Three: your files and team already live in another tool\u2019s world. Four: price \u2014 a cheaper tool that does your job is a fine tool. A wall is specific. \u2018Maybe better\u2019 is not a wall.",
            "screen": "Four wall bricks land: images / code / your files\u2019 home / price; a second tool icon rises only behind the walls."
        },
        {
            "id": "B08", "scene": "M09", "dur_s": 22, "act": "3",
            "voice": "Liam",
            "line": "Count the real cost of tool-shopping: an hour of reviews, an evening migrating chats, a month of half-used subscriptions. That is time you didn\u2019t spend getting good. Our companion film said the stack is the answer \u2014 true. This film says: build it slowly. One tool, mastered. A second, only at a named wall.",
            "screen": "Hours drain into a 'shopping' bag vs feed a 'getting good' bar; closing card: 'build the stack slowly'."
        },
        {
            "id": "BVDT", "scene": "M10", "dur_s": 32, "act": "recap",
            "voice": "Liam",
            "line": "So the verdict. Pick one AI and learn it properly \u2014 the hours go into your skill, not into shopping. Your skill transfers to any tool, including next year\u2019s winner. Add a second only at a specific wall: images, code, your files\u2019 home, or price. And when in doubt, run your own thirty-minute test \u2014 the one benchmark that never goes stale. If a leaderboard ever changes what you do on a Tuesday, believe the leaderboard.",
            "screen": "Five verdict lines with dot bullets, revealed one by one."
        },
        {
            "id": "BHTF", "scene": "M10", "dur_s": 25, "act": "do_today",
            "voice": "Liam",
            "line": "Your turn. Paste this into Claude: \u2018Interview me about my week \u2014 my writing, my images, my spreadsheets \u2014 then give me one reason to keep my current AI tool and one reason to add a second. Name the wall.\u2019 Answer honestly. If it can\u2019t name a wall, you have your answer: one tool, learned well.",
            "screen": "Prompt card: the paste-into-Claude interview prompt."
        },
        {
            "id": "BOUT", "scene": "M10", "dur_s": 12, "act": "outro",
            "voice": "Liam",
            "line": "One AI or many? Liam, in for Bear. Thanks for watching.",
            "screen": "Title card: 'One AI or many?' + @NikBearBrown."
        }
    ]
}

if __name__ == "__main__":
    beats = BS["beats"]
    assert len(beats) == 12, len(beats)
    assert 11 <= len(beats) <= 16, "beat count outside 11-16 band"
    for b in beats:
        assert b["scene"].startswith("M") and b["id"] not in ("",), b
        assert b["voice"] == "Liam", b
        words = len(b["line"].split())
        # narration clock: ~150 wpm => dur_s must cover the words (+3 s slack)
        assert b["dur_s"] >= words / 2.5, f"{b['id']}: {words}w needs >={words/2.5:.1f}s"
    body = [b["id"] for b in beats if b["act"] in ("1", "2", "3")]
    assert len(body) == 7, len(body)
    recap = next(b for b in beats if b["id"] == "BVDT")
    assert "verdict" in recap["line"].lower(), "recap must be the verdict"
    total = sum(b["dur_s"] for b in beats)
    assert 240 <= total <= 360, f"total {total}s outside 4-6 min band"
    print(f"beats={len(beats)} body={len(body)} total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
    print("beat_sheet.json written")
