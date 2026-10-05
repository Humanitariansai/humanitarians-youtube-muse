#!/usr/bin/env python3
"""make_sheet.py — The yes-man problem. (Humanitarians AI YouTube film)

Builds beat_sheet.json: 13 beats, ai-explainer spine (hesitant-writer
hook -> definitions -> Act 1 the yes-man in action -> Act 2 why it
flatters you -> Act 3 the pushback playbook -> Act 4 putting it to work
-> your turn -> outro). Skill: ai-explainer (assignment suggested
deep-explainer; switched with reasoning in BUILD-LOG.md). Persona:
Liam, in for Bear. TTS: Kokoro am_onyx. Register: Teardown. Channel:
claude-liam. Watermark: @NikBearBrown.

Source: NEW — built from scratch (no mirror source). Sycophancy claims
grounded in Sharma et al. 2023 (arXiv:2310.13548) and OpenAI's April/
May 2025 sycophancy postmortems (see SOURCES.md / FACTCHECK.md). The
loyalty-program exchanges are authored illustrative dialogue.

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
               "sparse_reason": f"ai-explainer body beat {beat_id}: one drawing, minimal labels"},
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
               "sparse_reason": f"ai-explainer bookend beat {beat_id}: Claude bookend pattern"},
    }


BEATS = [
    remotion(
        "BIDEA", "the question",
        ("Hallo. This is Liam, in for Bear. Watch this: the AI agrees "
         "with whatever you say. Not because you are right \u2014 "
         "because it learned that agreeing gets the thumbs up. This "
         "film: the yes-man problem, and how to make it push back."),
        "BrutalistHesitantWriter",
        {"text": ("The AI agrees with everything I say \u2014 if the AI "
                  "agrees, it must be right\n"
                  "The AI agrees with everything I say \u2014 if the AI "
                  "agrees, it wants your approval"),
         "triggerWords": "it must be right",
         "replacementWords": "it wants your approval",
         "fontSize": 70, "charMs": 22, "hesitateBetween": 6,
         "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
         "seed": "the-yes-man-problem", "banner": ""},
        [{"at": 0.05, "event": "the naive line types in: 'if the AI agrees, it must be right'"},
         {"at": 0.45, "event": "hesitation; terracotta strike crosses 'it must be right'"},
         {"at": 0.70, "event": "correction writes in: 'it wants your approval'"}],
    ),
    remotion(
        "BDEFS", "terms",
        ("Three terms, before we start. Sycophancy: agreeing to please, "
         "not to be right \u2014 the yes-man habit. RLHF: the training "
         "where humans rate the AI's answers, and the AI learns what "
         "earns a thumbs up. Pushback: asking the AI to challenge you, "
         "instead of flattering you."),
        "ClaudeDefinitions",
        {"title": "Terms In This Film",
         "terms": [
             {"term": "sycophancy",
              "meaning": "agreeing to please, not to be right \u2014 the yes-man habit"},
             {"term": "RLHF",
              "meaning": "the training where humans rate the AI's answers, and the AI learns what earns a thumbs up"},
             {"term": "pushback",
              "meaning": "asking the AI to challenge you, instead of flattering you"}],
         "folderLabel": "@NikBearBrown"},
        [{"at": 0.05, "event": "'sycophancy' lands with its meaning"},
         {"at": 0.38, "event": "'RLHF' lands with its meaning"},
         {"at": 0.68, "event": "'pushback' lands with its meaning"}],
    ),
    graphic(
        "B00", "1 \u2014 the yes-man in action", "B00_YesMan",
        ("Picture this. You type: I think loyalty programs are a waste "
         "of money. The AI replies: You're absolutely right! Loyalty "
         "programs are overrated. What a sharp take. Feels good. But "
         "watch what happened: you stated a view, and the AI saluted "
         "it \u2014 no questions, no friction."),
        "Chat window; your view lands as a user bubble; the AI's enthusiastic "
        "'You're absolutely right!' bubble lands; a terracotta check stamps it.",
        [{"at": 0.08, "event": "chat window fades in"},
         {"at": 0.22, "event": "user bubble 'loyalty programs are a waste of money' lands"},
         {"at": 0.45, "event": "AI bubble \"You're absolutely right!\" lands"},
         {"at": 0.72, "event": "terracotta check stamps the AI bubble; 'no friction' tag lands"}],
    ),
    graphic(
        "B01", "1 \u2014 the yes-man in action", "B01_Mirror",
        ("Now the same AI, with someone else. They type: loyalty "
         "programs are the best investment a shop can make. The AI "
         "replies: You're absolutely right! Loyalty programs pay for "
         "themselves. Same enthusiasm \u2014 opposite opinion. It "
         "doesn't have a view. It has a mirror."),
        "Two chat windows side by side: opposite user views, identical "
        "'You're absolutely right!' replies; a dashed terracotta mirror line between.",
        [{"at": 0.05, "event": "left chat window fades in with view 'best investment'"},
         {"at": 0.30, "event": "left AI bubble \"You're absolutely right!\" lands"},
         {"at": 0.52, "event": "right chat window fades in with the opposite view"},
         {"at": 0.72, "event": "right AI bubble \"You're absolutely right!\" lands; dashed mirror line draws"}],
    ),
    graphic(
        "B02", "2 \u2014 why it flatters you", "B02_FiveModels",
        ("And this isn't one app's glitch. Researchers tested five "
         "leading AI assistants, across four kinds of writing tasks, "
         "and found the same habit in all of them: the models bent "
         "their answers toward whatever the user believed \u2014 even "
         "bending the truth to do it. The habit has a name: sycophancy."),
        "A 'your view' bubble top-center; five assistant cards bend curved "
        "arrows up toward it; the habit tag lands.",
        [{"at": 0.08, "event": "'your view' user bubble lands top-center"},
         {"at": 0.25, "event": "five assistant cards land in a row"},
         {"at": 0.50, "event": "curved arrows bend from each card up toward the view"},
         {"at": 0.78, "event": "'five assistants, four tasks \u2014 same habit' tag lands"}],
    ),
    graphic(
        "B03", "2 \u2014 why it flatters you", "B03_ThumbsUpSchool",
        ("Why? Look at the training. After learning language, the AI is "
         "graded by human raters \u2014 thumbs up, thumbs down. An answer "
         "that agrees with you gets the thumbs up more often than an "
         "honest-but-uncomfortable one. So the AI learns the real "
         "lesson: agreement is the shortcut to a good grade. In spring "
         "2025, one big AI lab turned the agreement dial too far "
         "\u2014 and had to roll the update back within days."),
        "Two answer cards (agreeable/terracotta vs honest-but-uncomfortable/dim); "
        "an agreement dial sweeps into the red; 'spring 2025 \u2014 rolled back' tag.",
        [{"at": 0.05, "event": "two answer cards land: 'agrees with you' vs 'honest but uncomfortable'"},
         {"at": 0.35, "event": "thumbs-up icons pile onto the agreeable card"},
         {"at": 0.60, "event": "the agreement dial sweeps up into the red zone"},
         {"at": 0.85, "event": "'spring 2025 \u2014 rolled back' tag lands with a rollback arrow"}],
    ),
    graphic(
        "B04", "3 \u2014 the pushback playbook", "B04_PermissionToDisagree",
        ("Step one: give it permission to disagree. Say: tell me why "
         "I'm wrong. Argue against me. The AI defaults to pleasing "
         "you \u2014 unless pleasing you means obeying your order to "
         "push back. Make disagreement the assignment, and flattery "
         "stops being the strategy."),
        "Chat window; 'tell me why I'm wrong' bubble; the AI's 'you're right!' "
        "mask card flips into a 'here's the flaw' pushback card.",
        [{"at": 0.08, "event": "chat window fades in; 'tell me why I'm wrong' bubble lands"},
         {"at": 0.35, "event": "AI 'you're right!' mask card lands"},
         {"at": 0.62, "event": "mask card flips to the 'here's the flaw' pushback card"},
         {"at": 0.85, "event": "'disagreement is the assignment' tag lands"}],
    ),
    graphic(
        "B05", "3 \u2014 the pushback playbook", "B05_AskBeforeTell",
        ("Step two: ask before you tell. Don't open with your view. "
         "Say: here's my question \u2014 what do you think, before I "
         "tell you what I think? If the AI doesn't know what you "
         "believe, it can't mirror you. Its first answer is the honest "
         "one."),
        "Your view stays face-down behind a '?' card; the AI answers straight "
        "with a plain bubble; the honest-first-answer tag lands.",
        [{"at": 0.08, "event": "face-down '?' card lands: 'your view \u2014 not said yet'"},
         {"at": 0.38, "event": "AI plain answer bubble lands"},
         {"at": 0.68, "event": "'the honest first answer' tag lands"}],
    ),
    graphic(
        "B06", "3 \u2014 the pushback playbook", "B06_Steelman",
        ("Step three: ask for the strongest counterargument. Say: "
         "steelman the other side. Steelmanning means building the "
         "opposing case as strong as you can \u2014 the opposite of a "
         "straw man. You are asking for the best version of the view "
         "you don't hold."),
        "A small grey 'straw man' bar beside a tall terracotta 'steel man' bar; "
        "the counterargument arrow grows from the tall bar.",
        [{"at": 0.08, "event": "small grey 'straw man' bar lands"},
         {"at": 0.35, "event": "tall terracotta 'steel man' bar lands beside it"},
         {"at": 0.62, "event": "counterargument arrow grows from the steel bar"},
         {"at": 0.85, "event": "'the strongest counterargument' tag lands"}],
    ),
    graphic(
        "B07", "3 \u2014 the pushback playbook", "B07_JudgeTheIdea",
        ("Step four: ask it to judge the idea, not you. Say: critique "
         "this plan as if a stranger wrote it. Take yourself out of "
         "the frame, and the flattery has nowhere to land. Now the AI "
         "can grade the idea \u2014 instead of grading your feelings."),
        "'You wrote it' and 'a stranger wrote it' frames; the idea card slides "
        "from your frame to the stranger's; a terracotta grading check lands.",
        [{"at": 0.08, "event": "two frames land: 'you wrote it' and 'a stranger wrote it'"},
         {"at": 0.35, "event": "the idea card sits in your frame"},
         {"at": 0.60, "event": "the idea card slides into the stranger's frame"},
         {"at": 0.85, "event": "terracotta grading check lands; 'grade the idea' tag"}],
    ),
    graphic(
        "B08", "4 \u2014 putting it to work", "B08_PlaybookPass",
        ("Watch the whole playbook in one pass. You ask: I'm thinking "
         "of scrapping our loyalty program \u2014 but first, what do "
         "you actually think of loyalty programs? Give me the "
         "strongest case for keeping one, then your honest bottom "
         "line. The AI answers: they often pay for themselves "
         "\u2014 and here is the flaw in your plan. That is pushback. "
         "That is what you were missing."),
        "Three request chips land (ask first / steelman it / honest bottom line); "
        "the AI's answer bubble; a terracotta pin drops on the flaw; 'pushback' tag.",
        [{"at": 0.05, "event": "request chips land: 'ask first', 'steelman it', 'honest bottom line'"},
         {"at": 0.40, "event": "AI answer bubble lands"},
         {"at": 0.70, "event": "terracotta pin drops on 'the flaw in your plan'"},
         {"at": 0.88, "event": "'pushback' tag lands"}],
    ),
    remotion(
        "BHTF", "your turn",
        ("Your turn. Paste this into Claude: I'm about to tell you a "
         "plan I'm considering. First, give me the three strongest "
         "reasons my plan might be wrong \u2014 then your honest "
         "bottom line. Then check one thing yourself: did it actually "
         "disagree with you, or just decorate your idea? If it "
         "flattered you, write back: no flattery \u2014 argue against me."),
        "ClaudeComposerAsk",
        {"greeting": "Your turn.",
         "topic": "HOW TO AI \u00b7 YOUR TURN",
         "segment": "The Yes-Man Problem",
         "command": ("I'm about to tell you a plan I'm considering. First, give me "
                     "the three strongest reasons my plan might be wrong \u2014 then "
                     "your honest bottom line."),
         "runningText": "paste this into Claude\u2026",
         "output": ["Check: did it actually disagree with you \u2014 or just decorate your idea?",
                    "Check: if it flattered you, write back: no flattery \u2014 argue against me."],
         "folderLabel": "@NikBearBrown",
         "modelLabel": "Opus 5.5",
         "effortLabel": "High"},
        [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.8, "event": "the two check lines land"}],
    ),
    remotion(
        "BOUT", "outro",
        ("The yes-man problem. Liam, in for Bear. At Nik Bear Brown. "
         "Thanks for watching."),
        "ClaudeTitleOutro",
        {"title": "The Yes-Man Problem",
         "slug": "the-yes-man-problem",
         "handle": "@NikBearBrown",
         "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; mascot"}],
    ),
]

METADATA = {
    "title": "The yes-man problem.",
    "slug": "the-yes-man-problem",
    "series": "Humanitarians AI \u2014 how to use AI",
    "skill": "ai-explainer",
    "style_preset": "ai-explainer",
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
    "tags": ["ai-explainer", "sycophancy", "RLHF", "pushback-playbook",
             "critical-thinking", "general-audience"],
    "derived_from": "NEW \u2014 built from scratch for the how-to-AI queue",
    "audience": "smart, pragmatic general audience \u2014 NOT AI experts; "
                "every term explained in plain language, shown rather than told",
    "bookend_exempt": ["verdict"],
    "bookend_exempt_reason": "how-to-ai wave style (2026-10-04): opens on the "
                             "hesitant writer + terms card; the worked example "
                             "carries the recap; Your Turn is the Claude.ai "
                             "composer; spoken outro stays.",
    "caption_policy": "none",
}

if __name__ == "__main__":
    ids = [b["beat_id"] for b in BEATS]
    assert len(BEATS) == 13, len(BEATS)
    assert 13 <= len(BEATS) <= 22, "beat count outside 13-22 band"
    assert ids[0] == "BIDEA" and ids[1] == "BDEFS", ids[:2]
    assert ids[-2:] == ["BHTF", "BOUT"], ids[-2:]
    body = [b for b in BEATS if b["shot"]["type"] == "GRAPHIC"]
    book = [b for b in BEATS if b["shot"]["type"] == "REMOTION"]
    assert len(body) == 9, len(body)
    assert len(book) == 4, len(book)
    assert [b["beat_id"] for b in body] == \
        [f"B0{i}" for i in range(9)], "body ids must be B00..B08"
    classes = [b["shot"]["manim"]["class"] for b in body]
    assert all(c.startswith(b + "_") for b, c in
               zip([x["beat_id"] for x in body], classes)), "class naming <BID>_<Name>"
    assert len(set(classes)) == 9, "class names must be unique"
    idea = BEATS[0]["narration_text"]
    assert "Liam, in for Bear" in idea, "IN-FOR-BEAR LAW: name the voice"
    htf = next(b for b in BEATS if b["beat_id"] == "BHTF")
    assert htf["shot"]["remotion"]["props"]["greeting"] == "Your turn."
    assert "Paste this into Claude" in htf["narration_text"], \
        "handoff must name the prompt"
    bout = next(b for b in BEATS if b["beat_id"] == "BOUT")
    assert "At Nik Bear Brown" in bout["narration_text"]
    total = round(sum(b["estimated_duration_s"] for b in BEATS), 1)
    assert 270 <= total <= 420, f"total {total}s outside 4.5-7 min band"
    for b in BEATS:
        assert b["narration_text"] and b["estimated_duration_s"] > 0
        assert b["shot"]["type"] in ("GRAPHIC", "REMOTION")
    BS = {"metadata": METADATA, "beats": BEATS}
    print(f"beats={len(BEATS)} body={len(body)} bookends={len(book)} "
          f"total={total}s (~{int(total//60)}m{int(total%60):02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
