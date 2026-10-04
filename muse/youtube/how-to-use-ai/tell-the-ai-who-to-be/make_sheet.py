#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for tell-the-ai-who-to-be.

SHOW-TELL film #2 of the How-to-AI series (channel claude-liam, Liam in for Bear).
REFACTOR of nikbearbrown/humanitarians-youtube-muse
claude/claude-for-education/claude-liam-prompt-tutorial-lesson-03-role-prompting
(Kore persona, technical/course audience) rewritten for a smart general audience:
role prompting as "tell the AI who to be" — register calibration, not costume.

Source argument kept: role = register calibration across four axes (vocabulary,
assumed knowledge, tone, depth); role vs persona; the "does the role change what
counts as a good answer?" test. Everything else rewritten.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "tell-the-ai-who-to-be"
TITLE = "Tell the AI who to be"


def beat(bid, narration, cls, image, show):
    return {
        "beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
        "narration_text": narration,
        "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
        "voice": "am_onyx", "engine": "kokoro",
        "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image,
                 "show": show, "manim": {"class": cls}, "motion_claim": image},
    }


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration,
         "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


B = [
    beat("B00",
         "The trick is one line at the start of your prompt. Act as a chef. "
         "That line has a name: a role prompt. It doesn't change what you asked for "
         "\u2014 you still want a lemon pasta recipe. It changes who you're asking.",
         "B00_RoleLine",
         "A prompt card drops onto the stage; a tag reading 'act as a chef' drops onto it; "
         "the card slides into the Claude window.",
         [{"at": 0.05, "event": "prompt card drops in"},
          {"at": 0.15, "event": "role tag lands on the card"},
          {"at": 0.30, "event": "Claude window arrives; card slides in"}]),
    beat("B01",
         "Now, the role is not a costume. Think of it as four dials: the words it picks, "
         "what it assumes you already know, how formal its tone is, and how deep it goes. "
         "The moment a role lands, all four dials turn at once. The AI doesn't become a chef, "
         "and it doesn't believe it's one. Those four dials together are called the register "
         "\u2014 and a role calibrates the register.",
         "B01_Calibrate",
         "Four slider rows appear beside the card \u2014 words, knowledge, tone, depth \u2014 "
         "and their knobs snap to new positions when the role tag lands.",
         [{"at": 0.05, "event": "card with role tag on stage"},
          {"at": 0.14, "event": "four sliders fade in; knobs snap to calibrated positions"}]),
    beat("B02",
         "Watch the dials move. The role lands \u2014 act as a patient tutor \u2014 and all four "
         "dials swing: words toward simple, knowledge toward nothing-assumed, tone warmer, "
         "depth shorter. Same question in, a different answer out, and nobody added any facts. "
         "The role only set the register.",
         "B02_DialsMove",
         "Four centred sliders and an answer page; a 'patient tutor' tag drops in, every knob "
         "slides to its end, and the answer page swaps to short simple lines.",
         [{"at": 0.05, "event": "sliders centred; neutral answer page"},
          {"at": 0.09, "event": "'patient tutor' tag lands; knobs swing; answer page changes"}]),
    beat("B03",
         "Now the classic experiment. Ask two doctors the same question. The pediatric oncologist "
         "is talking to a child: simple words, nothing assumed, warm, and short. The pathologist "
         "is presenting at grand rounds: technical, precise, and deep. Same facts, same question "
         "\u2014 two completely different answers. The role added no facts. It only set the register.",
         "B03_TwoDoctors",
         "One question card splits into two lanes \u2014 'for a child' and 'grand rounds' \u2014 "
         "a short simple answer page and a dense technical one, with a scan line sweeping the dense page.",
         [{"at": 0.05, "event": "question card"},
          {"at": 0.15, "event": "two answer pages land"},
          {"at": 0.25, "event": "role tags land; scan line sweeps the dense page"}]),
    beat("B04",
         "A role is small and functional: you are an expert tax attorney. A persona is the whole "
         "costume: you are Marcus, a sardonic nineteen-seventies tax attorney who speaks in "
         "nautical metaphors. The role calibrates the answer. The persona adds a character with "
         "a voice. Both are valid tools \u2014 a role tunes the register, a persona adds the voice. "
         "Know which one you need.",
         "B04_RoleVsPersona",
         "Two cards side by side: the left gets one small tag ('role'), the right gets a tag plus "
         "a giant quotation mark and extra voice tags ('persona').",
         [{"at": 0.05, "event": "two cards"},
          {"at": 0.16, "event": "role tag pins to the left card"},
          {"at": 0.25, "event": "persona costume \u2014 tags and quote mark \u2014 lands on the right"}]),
    beat("B05",
         "When is the line worth typing? Two piles. Feedback, explaining, advice \u2014 here the "
         "audience decides what's good, so set the role. Extracting a date, doing a sum \u2014 the "
         "job doesn't care about register, so the role adds nothing. The test is simple: does the "
         "role change what counts as a good answer? If it can't change what good looks like, skip it.",
         "B05_WhenItHelps",
         "Two open boxes: 'role helps' takes cards labelled feedback, explaining, advice and earns "
         "a check; 'skip it' takes a date and a sum and earns a cross.",
         [{"at": 0.05, "event": "two boxes land"},
          {"at": 0.09, "event": "cards drop into the left box; check lands"},
          {"at": 0.37, "event": "cards drop into the right box; cross lands"}]),
    beat("B06",
         "One last tip. 'Act as a genius' is vague \u2014 and a vague role calibrates nothing. Make "
         "the role specific instead, and give it an audience: 'act as a patient math tutor for a "
         "ten-year-old.' Say the job, say who it's for, and put the line first.",
         "B06_SpecificBeatsVague",
         "A prompt card carries a grey 'genius' tag that gets crossed out, then two specific tags "
         "land: 'patient math tutor' and 'for a ten-year-old'.",
         [{"at": 0.05, "event": "card with grey 'genius' tag"},
          {"at": 0.15, "event": "'genius' tag crossed out"},
          {"at": 0.30, "event": "specific role tags land"}]),
]

OPEN = [
    remotion("BIDEA", "the question",
             "Hallo. This is Liam, in for Bear. Every AI user discovers this trick sooner or later: "
             "before your question, you tell the AI who to be. Act as a chef. Act as an expert editor. "
             "Act as a patient tutor. And the answers come out different. So this film is about what "
             "that one line is really doing \u2014 and when it's worth typing.",
             "BrutalistHesitantWriter",
             {"text": "write me a recipe for lemon pasta",
              "triggerWords": "write me a recipe",
              "replacementWords": "act as a chef and write me a recipe",
              "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1,
              "mistakeRate": 2, "jitter": 20, "seed": SLUG, "banner": ""},
             [{"at": 0.0, "event": "types the naive request"},
              {"at": 0.6, "event": "backspaces 'write me a recipe' \u2192 'act as a chef and write me a recipe'"}],
             lead_silence_s=0.8,
             motion_claim="The writer types the naive request and corrects it into a role prompt.",
             qc={"sparse_by_design": True,
                 "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
    remotion("BDEFS", "terms",
             "Three terms for this film. A role prompt: a line at the start of your prompt that gives "
             "the AI a job to act as. Register: how an answer is pitched \u2014 its words, what it "
             "assumes you know, its tone, and how deep it goes. And a persona: a whole invented "
             "character with a voice of its own.",
             "ClaudeDefinitions",
             {"title": "Terms In This Film",
              "terms": [
                  {"term": "role prompt",
                   "meaning": "a line at the start of your prompt that gives the AI a job to act as"},
                  {"term": "register",
                   "meaning": "how an answer is pitched \u2014 words, assumed knowledge, tone, depth"},
                  {"term": "persona",
                   "meaning": "a whole invented character with a voice of its own"}],
              "folderLabel": "@NikBearBrown"},
             [{"at": 0.12, "event": "'role prompt' lands"},
              {"at": 0.5, "event": "'register' lands"},
              {"at": 0.78, "event": "'persona' lands"}],
             gate="CARD",
             qc={"sparse_by_design": True,
                 "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Ask one question twice. First, start it with: act as an expert explaining to a curious "
             "beginner. Then ask the same question again, starting with: act as an expert explaining "
             "to a fellow expert. Put the two answers side by side.")
YOURTURN = remotion("BHTF", "your turn",
                    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
                    "Can you point to three words that appear in only one of the two answers? "
                    "And which answer was actually more useful to you \u2014 and why?",
                    "ClaudeComposerAsk",
                    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN",
                     "segment": "Tell the AI Who to Be", "command": YT_PROMPT,
                     "runningText": "paste this into Claude\u2026",
                     "output": ["Check: three words that appear in only one answer.",
                                "Check: which answer was more useful to you \u2014 and why?"],
                     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
                    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
                     {"at": 0.1, "event": "the prompt types in full"},
                     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, "
                 "minimal labels, with the voice carrying the explanation. The negative space is the style, "
                 "so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.",
          "estimated_duration_s": 4.5, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE, "slug": SLUG,
                                          "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

# ---- assertions: beat count + total duration + structural sanity ----
assert len(B) == 11, f"expected 11 beats, got {len(B)}"
total = sum(b["estimated_duration_s"] for b in B)
assert 180 <= total <= 320, f"total estimated duration {total}s outside 180-320s band"
manim_beats = [b for b in B if b["lane"] == "manim"]
assert len(manim_beats) == 7, f"expected 7 manim body beats, got {len(manim_beats)}"
for b in manim_beats:
    assert b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"), b["beat_id"]
idea = next(b for b in B if b["beat_id"] == "BIDEA")
tw = idea["shot"]["remotion"]["props"]["triggerWords"]
assert tw in idea["shot"]["remotion"]["props"]["text"], "triggerWords must appear verbatim in text"
assert not tw.rstrip().endswith(("?", "!", ".")), "triggerWords must not end in punctuation"
rw = idea["shot"]["remotion"]["props"]["replacementWords"]
assert not rw.rstrip().endswith(("?", "!", ".")), "replacementWords must not end in punctuation"
for bid in ("BIDEA", "BDEFS", "BHTF", "BOUT"):
    bb = next(b for b in B if b["beat_id"] == bid)
    assert bb["lane"] == "bookend" and "remotion" in bb["shot"], bid

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE \u00b7 PROMPTING BASICS",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hallo (German/Dutch)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + "
                             "terms card, no verdict card; Your Turn is the Claude.ai composer; "
                             "spoken outro stays.",
    "audience": "smart general audience \u2014 curious non-experts; every term explained on first use",
    "source_doc": "REFACTOR of nikbearbrown/humanitarians-youtube-muse "
                  "claude/claude-for-education/claude-liam-prompt-tutorial-lesson-03-role-prompting "
                  "(Anthropic Prompt Engineering Interactive Tutorial, Lesson 03: Role Prompting). "
                  "Argument and facts kept; script and visuals rewritten for a general audience.",
    "playlist": "How to AI", "chapter_number": 2,
    "tags": ["role prompting", "prompt engineering", "Claude", "AI basics", "how to AI",
             "Nik Bear Brown"]},
    "beats": B}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(total), "s")
