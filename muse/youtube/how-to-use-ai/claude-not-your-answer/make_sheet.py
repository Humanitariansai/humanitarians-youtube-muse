#!/usr/bin/env python3
"""make_sheet.py — "Claude, Not Your Answer." (show-tell, general audience).

Source: mirror repo nikbearbrown/humanitarians-youtube-muse,
claude-for-artificial-intelligence/hai-not-your-answer/ (11 beats,
"Stop using your own Claude at work."). Rewritten for the humanitarians AI
YouTube channel: smart, pragmatic general audience, not AI experts. Every
term explained in plain words; the privacy mechanism shown, not told.

The argument: on a personal AI plan your chats can train the model and be
kept for years; one toggle stops it going forward; some things never go in.

Run: python3 make_sheet.py   -> writes beat_sheet.json (13 beats).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "claude-not-your-answer"
TITLE = "Claude, Not Your Answer."

WPS = 2.5  # words per second (~150 wpm)


def est(narration):
    return round(len(narration.split()) / WPS, 1)


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim",
            "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": est(narration),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image,
                     "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


B = [
 beat("B00",
      "Picture the scene. You are on a deadline, Claude is open, and the "
      "document you need summarized is right there. You paste it in and get "
      "your answer in seconds. That paste \u2014 quick, harmless-feeling \u2014 "
      "is what this film is about.",
      "B00_ThePaste",
      "Your chat window; a document slides in from the left and a ring marks the paste.",
      [{"at": 0.05, "event": "chat window lands"},
       {"at": 0.35, "event": "document slides into the window"},
       {"at": 0.7, "event": "a ring marks the paste"}]),
 beat("B01",
      "In April 2023, Samsung let its engineers use ChatGPT. Within about "
      "three weeks, three leaks: source code pasted to fix a bug, equipment "
      "code pasted to fix a defect, and a whole meeting uploaded for minutes. "
      "Samsung banned the tools and warned of disciplinary action.",
      "B01_Samsung",
      "Three documents drop one by one into a chat window; a ban stamp lands over it.",
      [{"at": 0.1, "event": "chat window"},
       {"at": 0.35, "event": "first document drops in"},
       {"at": 0.55, "event": "second document drops in"},
       {"at": 0.7, "event": "third document drops in"},
       {"at": 0.88, "event": "ban stamp lands"}]),
 beat("B02",
      "Here is why the paste matters. On a personal Claude plan \u2014 Free, "
      "Pro, or Max \u2014 your chats can train the model, and be kept up to "
      "five years. Since September 2025, that training is on by default.",
      "B02_TheMechanism",
      "A cable runs from your chat window to a dark training server; its lights come on; a '5 years' tag lands.",
      [{"at": 0.1, "event": "chat window and training server"},
       {"at": 0.4, "event": "cable draws; server lights come on"},
       {"at": 0.65, "event": "'5 years' tag lands"},
       {"at": 0.85, "event": "the ON toggle"}]),
 beat("B03",
      "The fix is one toggle. In Claude: Settings, then Privacy, and switch "
      "the training toggle off. Do it before your next conversation, not after.",
      "B03_TheToggle",
      "A settings panel; the Privacy row highlights; a cursor flips the training toggle from ON to OFF.",
      [{"at": 0.1, "event": "settings panel"},
       {"at": 0.4, "event": "Privacy row highlights"},
       {"at": 0.65, "event": "cursor flips the toggle OFF"}]),
 beat("B04",
      "The same switch exists everywhere. ChatGPT: Settings, Data controls, "
      "turn off Improve the model for everyone. Grok: on X, Settings, Privacy "
      "and safety, uncheck training. Gemini: on Google's My Activity page, "
      "turn off Gemini Apps activity.",
      "B04_Everywhere",
      "Three app panels \u2014 ChatGPT, Grok, Gemini \u2014 each with a toggle that flips OFF in turn.",
      [{"at": 0.1, "event": "three panels land"},
       {"at": 0.35, "event": "ChatGPT toggle flips"},
       {"at": 0.6, "event": "Grok toggle flips"},
       {"at": 0.8, "event": "Gemini toggle flips"}]),
 beat("B05",
      "One catch: the toggle only works going forward. It cannot pull back "
      "anything already used in a training run. So flip it now \u2014 not after "
      "your next session.",
      "B05_GoingForward",
      "The OFF toggle; an arrow runs forward from it; a sealed box marked 'already used' stays shut.",
      [{"at": 0.15, "event": "toggle OFF"},
       {"at": 0.4, "event": "arrow runs forward"},
       {"at": 0.65, "event": "sealed 'already used' box stays shut"}]),
 beat("B06",
      "I am not a lawyer \u2014 but a lawyer could frame a paste three ways. "
      "Breaking your NDA: the AI company is an outside party. Breaking data "
      "protection law, depending on where you live. Or breaking your own "
      "company's IT policy.",
      "B06_Legal",
      "Three seals stamp down in a row: NDA, data law, IT policy.",
      [{"at": 0.2, "event": "NDA seal stamps"},
       {"at": 0.5, "event": "data-law seal stamps"},
       {"at": 0.75, "event": "IT-policy seal stamps"}]),
 beat("B07",
      "So run a clean room. Four things never go into a personal AI account: "
      "client names, internal financials, source code, meeting recordings. And "
      "anonymize before you paste \u2014 swap real names for placeholders.",
      "B07_CleanRoom",
      "Four documents each get an X; then one document's real name swaps to a placeholder.",
      [{"at": 0.1, "event": "four documents"},
       {"at": 0.35, "event": "X marks land one by one"},
       {"at": 0.7, "event": "a name swaps to a placeholder"}]),
 beat("B08",
      "And if your company will pay for it: work and enterprise plans do not "
      "train on your data at all. If sensitive data is your daily work, that "
      "is the plan to ask for.",
      "B08_Enterprise",
      "An office block rises; a shield with a check lands on it: no training.",
      [{"at": 0.15, "event": "office block rises"},
       {"at": 0.55, "event": "shield lands"},
       {"at": 0.75, "event": "check draws; 'no training'"}]),
]

OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. You use Claude at work, and the answers "
    "are good. So the real question is not whether to use it. It is what you "
    "should never paste into it.",
    "BrutalistHesitantWriter",
    {"text": "Can I paste my work\ninto Claude?",
     "triggerWords": "paste my work",
     "replacementWords": "paste anything confidential",
     "fontSize": 70, "charSize": 22, "charMs": 22, "hesitateBetween": 6,
     "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Can I paste my work'"},
     {"at": 0.55, "event": "backspaces 'paste my work' -> 'paste anything confidential'"}],
    lead_silence_s=0.8,
    motion_claim="The writer types the naive paste question and corrects it to the real one: what is confidential.",
    qc={"sparse_by_design": True,
        "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms you will need. Training: when a company uses your chats to "
    "teach its model. Retention: how long it keeps those chats. And a clean "
    "room: a personal rule that sensitive stuff never enters the chat at all.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "training",
                "meaning": "a company using your chats to teach its model"},
               {"term": "retention",
                "meaning": "how long the company keeps your chats"},
               {"term": "clean room",
                "meaning": "a rule: sensitive stuff never enters the chat"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'training' lands"},
     {"at": 0.5, "event": "'retention' lands"},
     {"at": 0.78, "event": "'clean room' lands"}],
    gate="CARD",
    qc={"sparse_by_design": True,
        "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Look through our past chats and list every piece of work data I pasted "
             "in \u2014 names, numbers, code, meetings \u2014 and flag what should never "
             "have gone in.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things "
    "yourself: in Claude, open Settings, then Privacy, and confirm the training "
    "toggle is off. And delete any chat holding something confidential.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE \u00b7 YOUR TURN",
     "segment": "Audit Your AI Privacy", "command": YT_PROMPT,
     "runningText": "paste this into Claude\u2026",
     "output": ["Check: Claude \u2192 Settings \u2192 Privacy \u2014 the training toggle is off.",
                "Check: any chat holding something confidential is deleted."],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.0, "event": "Composer opens \u2014 'Your turn.'"},
     {"at": 0.1, "event": "the prompt types in full"},
     {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream "
                 "stage per beat, minimal labels, with the voice carrying the explanation. "
                 "The negative space is the style, so only underfill and clustered are waived; "
                 "edge-bleed, empty-frame and contrast still apply.")
for b in B:
    if b["lane"] == "manim":
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend",
          "proof_gate": "SHOW",
          "narration_text": TITLE + " At Nik Bear Brown.",
          "estimated_duration_s": est(TITLE + " At Nik Bear Brown."),
          "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                               "props": {"title": TITLE, "slug": SLUG,
                                         "handle": "@NikBearBrown",
                                         "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE \u00b7 AI PRIVACY AT WORK",
    "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hallo (clean per prior films)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant "
                             "writer + terms card, no verdict card; Your Turn is the "
                             "Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience \u2014 not necessarily AI experts",
    "source_doc": "mirror repo nikbearbrown/humanitarians-youtube-muse, "
                  "claude-for-artificial-intelligence/hai-not-your-answer/ "
                  "(read 2026-10-03); facts re-checked against primary sources, "
                  "see FACTCHECK.md",
    "playlist": "How to Use AI", "chapter_number": 0,
    "tags": ["Claude", "AI privacy", "model training", "opt out", "data retention",
             "Samsung", "clean room", "Nik Bear Brown"]},
    "beats": B}

# ---- assertions: beat count, classes, durations, bookend contracts ----
CLASS_OF = {"B00": "B00_ThePaste", "B01": "B01_Samsung",
            "B02": "B02_TheMechanism", "B03": "B03_TheToggle",
            "B04": "B04_Everywhere", "B05": "B05_GoingForward",
            "B06": "B06_Legal", "B07": "B07_CleanRoom",
            "B08": "B08_Enterprise"}
IDS = [b["beat_id"] for b in B]
assert len(B) == 13, f"expected 13 beats, got {len(B)}"
assert len(set(IDS)) == 13, "duplicate beat ids"
assert IDS[0] == "BIDEA" and IDS[-1] == "BOUT", "bookend order"
for b in B:
    assert b["narration_text"].strip(), f"{b['beat_id']}: empty narration"
    assert b["estimated_duration_s"] > 0, f"{b['beat_id']}: bad duration"
    assert b["voice"] == "am_onyx" and b["engine"] == "kokoro", \
        f"{b['beat_id']}: voice/engine"
manim_ids = [b["beat_id"] for b in B if b.get("lane") == "manim"]
assert manim_ids == [f"B{i:02d}" for i in range(9)], f"body beats: {manim_ids}"
for b in B:
    if b.get("lane") == "manim":
        assert b["shot"]["manim"]["class"] == CLASS_OF[b["beat_id"]], \
            f"{b['beat_id']}: class mismatch"
bidea = B[0]
props = bidea["shot"]["remotion"]["props"]
assert bidea.get("lead_silence_s") == 0.8
assert props["triggerWords"] in props["text"]
for k in ("triggerWords", "replacementWords"):
    assert not props[k].endswith(("?", ".", "!")), f"BIDEA {k} ends in punctuation"
bout = B[-1]
assert bout.get("kind") == "outro_voice" and bout.get("tail_silence_s") == 1.0
assert "YOUR TURN" in [b for b in B if b["beat_id"] == "BHTF"][0]["shot"]["remotion"]["props"]["topic"]
total = sum(b["estimated_duration_s"] for b in B)
assert 150 <= total <= 240, f"total {total}s outside 150-240 band"

(HERE / "beat_sheet.json").write_text(
    json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(total, 1), "s;",
      len(manim_ids), "manim scenes")
