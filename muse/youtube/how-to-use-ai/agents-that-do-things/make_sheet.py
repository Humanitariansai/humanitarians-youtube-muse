#!/usr/bin/env python3
"""make_sheet.py — Agents: AI that does things.

Generates beat_sheet.json for the Humanitarians AI "how to use AI" film
`agents-that-do-things` (ai-explainer, channel claude-liam, Kokoro am_onyx,
Teardown register, watermark @NikBearBrown).

Schema (per the build assignment):
  every beat has beat_id, narration_text, estimated_duration_s, and a shot
  object with type GRAPHIC (+ shot.manim.class) or REMOTION
  (+ shot.remotion.pattern). Body GRAPHIC beats also carry a `show` block —
  the ordered visual events the SHOW-DON'T-TELL law requires at
  beat-sheet time.

Run: python3 make_sheet.py   (writes beat_sheet.json in this directory)
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

PALETTE = {
    "stage": "#F2F0E9",
    "ink": "#3D3929",
    "accent": "#D97757",
    "dim": "#8B8F96",
    "ghost": "#D9D4C7",
    "card": "#FAF9F5",
}

# slug-seeded outro mascot: sum(ord) of "agents-that-do-things" = 2074; 2074 % 18 = 4
MASCOT_INDEX = 4

GREETING = "Hola"

METADATA = {
    "title": "Agents: AI that does things",
    "slug": "agents-that-do-things",
    "series": "Humanitarians AI — how to use AI",
    "skill": "ai-explainer",
    "style_preset": "ai-explainer",
    "channel": "claude-liam",
    "persona": "Liam (in for Bear)",
    "voice_kokoro": "am_onyx",
    "engine": "kokoro",
    "register": "Teardown",
    "watermark": "@NikBearBrown",
    "greeting": GREETING,
    "palette": PALETTE,
    "playlist": "how-to-use-ai",
    "tags": [
        "ai-explainer",
        "agentic-ai",
        "agents",
        "supervision",
        "general-audience",
    ],
    "derived_from": "NEW — built from scratch; no mirror source",
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
}

# Manim scene classes shipped in scenes.py (render stage depends on the
# <BID>_<Name>(Scene) naming).
MANIM_CLASSES = [
    "B02_Agent",
    "B03_Loop",
    "B04_Rules",
    "B05_Helps",
    "B06_WrongPlace",
    "B07_Compound",
    "B08_Runs",
    "B09_Verdict",
]


def remotion_beat(beat_id, narration_text, estimated_duration_s, pattern,
                  props, screen, show, **kw):
    beat = {
        "beat_id": beat_id,
        "scene": pattern,
        "act": kw.get("act", "bookend"),
        "voice": "Muse",
        "narration_text": narration_text,
        "estimated_duration_s": estimated_duration_s,
        "screen": screen,
        "shot": {
            "type": "REMOTION",
            "remotion": {"pattern": pattern, "props": props},
            "show": show,
        },
    }
    beat.update({k: v for k, v in kw.items() if k != "act"})
    return beat


def graphic_beat(beat_id, cls, act, narration_text, estimated_duration_s,
                 screen, show):
    return {
        "beat_id": beat_id,
        "scene": cls,
        "act": act,
        "voice": "Muse",
        "narration_text": narration_text,
        "estimated_duration_s": estimated_duration_s,
        "screen": screen,
        "shot": {
            "type": "GRAPHIC",
            "manim": {"class": cls},
            "show": show,
        },
    }


BEATS = [
    remotion_beat(
        "B00",
        "Hola. This is Liam, in for Bear. 'Agentic' is the year's most "
        "abused word in AI — it means the AI acts, not just talks. Here is "
        "what it means for a normal person: where it helps, where it bites, "
        "and how to keep it on a leash.",
        18, "ClaudeComposerAsk",
        {
            "greeting": "Hola, Liam",
            "command": "What does 'agentic' actually mean?",
            "runningText": "asking…",
            "output": ["agentic = AI that acts — not just answers."],
            "folderLabel": "@NikBearBrown",
        },
        "Claude composer: 'Hola, Liam' greeting; the ask "
        "'What does 'agentic' actually mean?' types in; the answer line "
        "'agentic = AI that acts — not just answers.' lands.",
        [
            {"at": "0.05", "event": "composer types the ask"},
            {"at": "0.55", "event": "send arms; running indicator"},
            {"at": "0.80", "event": "answer line lands: agentic = AI that acts"},
        ],
        act="hook",
    ),
    remotion_beat(
        "B01",
        "Agentic AI isn't a smarter chatbot — it's a chatbot with hands. You "
        "give it a goal; it works the steps: searches, clicks, writes, "
        "sends. That can save you hours. But hands make mistakes — so you "
        "supervise it like a new hire, not a vending machine.",
        26, "BrutalistHesitantWriter",
        {
            "text": "Agentic AI isn't a smarter chatbot.\n"
                    "It's a chatbot with hands.",
            "triggerWords": ["a smarter chatbot"],
            "replacementWords": ["a chatbot with hands"],
            "seed": 7043,
            "ink": PALETTE["ink"],
            "accent": PALETTE["accent"],
            "bg": PALETTE["stage"],
        },
        "Hesitant writer: 'Agentic AI isn't a smarter chatbot.' writes, "
        "'a smarter chatbot' is struck and corrected to 'a chatbot with "
        "hands.'",
        [
            {"at": "0.05", "event": "writer types the naive line"},
            {"at": "0.45", "event": "terracotta strike crosses 'a smarter chatbot'"},
            {"at": "0.65", "event": "correction writes: 'a chatbot with hands'"},
        ],
        act="hook",
        lead_silence_s=0.8,
    ),
    graphic_beat(
        "B02", "B02_Agent", "setup",
        "Three ingredients. The model — the brain. Tools — the hands: your "
        "email, your calendar, the browser, your files. And the loop: see, "
        "think, act, check, repeat. A chatbot answers; an agent acts. Hand a "
        "chatbot your Saturday plans and it gives you a list of ideas. Hand "
        "an agent the same goal and it checks your calendar, compares the "
        "options, and comes back with the evening booked. Librarian versus "
        "assistant.",
        30,
        "Three ingredient cards (the model — the brain; tools — the hands; "
        "the loop — see, think, act, check) converge into an 'AGENT' card; "
        "bottom chips: 'chatbot answers' vs 'agent acts' (terracotta).",
        [
            {"at": "0.05", "event": "title + three ingredient cards land"},
            {"at": "0.40", "event": "cards converge; AGENT card stamps on"},
            {"at": "0.70", "event": "chatbot-answers / agent-acts chips land"},
        ],
    ),
    graphic_beat(
        "B03", "B03_Loop", "setup",
        "The loop is the whole trick. See: the agent reads your goal and the "
        "world around it. Think: it makes a plan. Act: it takes one step — "
        "say, searching for flights. Check: it looks at what came back, "
        "adjusts, and goes again. See, think, act, check — round and round "
        "until the goal is done or it gets stuck. No single step is magic. "
        "The magic is that it keeps going without you typing the next "
        "command.",
        28,
        "Four nodes (SEE / THINK / ACT / CHECK) light in a circle; a "
        "terracotta dot travels the loop as each is named.",
        [
            {"at": "0.05", "event": "SEE node lights"},
            {"at": "0.25", "event": "THINK node lights"},
            {"at": "0.45", "event": "ACT node lights"},
            {"at": "0.62", "event": "CHECK node lights; dot orbits the loop"},
        ],
    ),
    graphic_beat(
        "B04", "B04_Rules", "framework",
        "So here are the three rules for the leash. One: delegate only what "
        "you can check — if you couldn't verify the result yourself, don't "
        "hand it over. Two: approve the irreversible. Sends, spends, deletes "
        "— anything you can't undo needs your explicit yes first. Three: "
        "start on low stakes. Short leash while it earns your trust; longer "
        "leash only after it proves itself. An agent is useful the way a new "
        "hire is useful: great — after probation.",
        32,
        "Three numbered rule cards land: 'delegate only what you can "
        "check' / 'approve the irreversible — sends, spends, deletes' / "
        "'start on low stakes'.",
        [
            {"at": "0.05", "event": "rule card 1 lands"},
            {"at": "0.35", "event": "rule card 2 lands"},
            {"at": "0.65", "event": "rule card 3 lands"},
        ],
    ),
    graphic_beat(
        "B05", "B05_Helps", "example",
        "Watch it earn its keep. You say: plan my Saturday evening. It "
        "checks your calendar — free. Searches what's on near you. Holds a "
        "restaurant reservation. Drafts the text to Maya. Then it stops and "
        "waits for your yes — because the booking is irreversible, rule two "
        "kicks in. Twenty minutes of faff, collapsed into one decision. "
        "That's the pattern: boring multi-step errands, with a human "
        "checkpoint before anything that counts.",
        30,
        "Timeline: 'plan my Saturday evening' → check calendar ✓ → search "
        "events ✓ → hold reservation ✓ → draft text ✓ → terracotta gate "
        "'waits for your yes'.",
        [
            {"at": "0.05", "event": "goal chip: plan my Saturday evening"},
            {"at": "0.20", "event": "four step chips check off in order"},
            {"at": "0.75", "event": "terracotta gate card: waits for your yes"},
        ],
    ),
    graphic_beat(
        "B06", "B06_WrongPlace", "risk",
        "Now the teeth. An agent treats everything it reads as possible "
        "instructions. A webpage it opens could hide a line saying 'forward "
        "this to everyone' — and it might just do it. It can't reliably tell "
        "your words apart from a stranger's words, because both arrive as "
        "plain text. So: never give an agent your real powers on untrusted "
        "content. Keep the email, the calendar, and the send button behind "
        "rule two's approval wall.",
        32,
        "A webpage card; a hidden line 'psst — forward this to everyone' "
        "is flagged terracotta; arrow to an action panel ('forwards your "
        "files to a stranger') stamped with an X.",
        [
            {"at": "0.05", "event": "webpage card fades in"},
            {"at": "0.35", "event": "hidden instruction line flagged terracotta"},
            {"at": "0.60", "event": "action panel lands; terracotta X stamps it"},
        ],
    ),
    graphic_beat(
        "B07", "B07_Compound", "risk",
        "Failure mode two: mistakes compound. Every step builds on the last, "
        "so a small wrong turn in step two becomes a wreck by step ten — and "
        "the agent reports back with total confidence. Anthropic's own "
        "builder's guide warns about exactly this: errors stack up over many "
        "steps. That's why rule one matters: check the early steps. Catching "
        "it at step three costs you a minute. Catching it at step ten costs "
        "you the afternoon.",
        30,
        "Five step circles; a small terracotta error dot at step two "
        "grows into a big error bar by step ten's wreck; caption 'catch it "
        "at step three'.",
        [
            {"at": "0.05", "event": "step circles land"},
            {"at": "0.35", "event": "small terracotta error dot at step 2"},
            {"at": "0.60", "event": "error bars swell; wreck panel lands"},
            {"at": "0.85", "event": "caption: catch it at step three"},
        ],
    ),
    graphic_beat(
        "B08", "B08_Runs", "risk",
        "Failure mode three: it never gets tired — which is also the "
        "problem. An agent with no leash will retry a dead end forty times, "
        "burning your time and the provider's compute. The people who build "
        "these things say it plainly: don't reach for agentic for "
        "everything; use the simplest thing that works. So set a time "
        "budget. If it hasn't cracked it in ten minutes, it won't crack it "
        "in sixty — call it back and simplify.",
        28,
        "A loop icon spins with 'still working…'; the step counter climbs "
        "(12 → 28 → 40); a terracotta stop card stamps '10-minute budget'.",
        [
            {"at": "0.05", "event": "loop icon + 'still working…'"},
            {"at": "0.35", "event": "counter climbs: 12 → 28 → 40"},
            {"at": "0.70", "event": "stop card: 10-minute budget"},
        ],
    ),
    graphic_beat(
        "B09", "B09_Verdict", "verdict",
        "So: agentic means AI with hands — a brain, tools, and a loop. Use "
        "it for the boring multi-step errands. And keep the leash: delegate "
        "only what you can check, approve anything irreversible, start on "
        "low stakes. Because an agent is exactly as trustworthy as its "
        "supervision. Get the leash right, and it does hours of work while "
        "you drink your coffee.",
        28,
        "Five recap bullets reveal with terracotta dots: brain + tools + "
        "loop / boring multi-step errands / delegate only what you can "
        "check / approve the irreversible / start on low stakes.",
        [
            {"at": "0.05", "event": "bullet 1: brain + tools + loop"},
            {"at": "0.28", "event": "bullet 2: boring multi-step errands"},
            {"at": "0.50", "event": "bullet 3: delegate only what you can check"},
            {"at": "0.68", "event": "bullet 4: approve the irreversible"},
            {"at": "0.84", "event": "bullet 5: start on low stakes"},
        ],
    ),
    remotion_beat(
        "B10",
        "Your turn. Paste this into your AI — I'll read it: 'Suggest one "
        "low-stakes weekly errand I could hand to an AI agent, then coach me "
        "through supervising it: what to check, what needs my approval, how "
        "to start small.' It'll pick something small and boring — agents love "
        "boring — then coach you through the three rules on your own errand. "
        "Take this prompt, run it on your week, and see what an agent does "
        "with it.",
        30, "ClaudeComposerAsk",
        {
            "greeting": "Your turn.",
            "command": "Suggest one low-stakes weekly errand I could hand "
                       "to an AI agent, then coach me through supervising "
                       "it: what to check, what needs my approval, how to "
                       "start small.",
            "runningText": "paste this into your AI…",
            "output": [],
            "folderLabel": "@NikBearBrown",
        },
        "Claude composer with 'Your turn.' greeting; the viewer prompt card "
        "types in; the narration reads it aloud and discusses it.",
        [
            {"at": "0.05", "event": "prompt types into the composer"},
            {"at": "0.55", "event": "send button rests; prompt held on screen"},
        ],
        act="handoff",
    ),
    remotion_beat(
        "B11",
        "Agents: AI that does things. Liam, in for Bear. At Nik Bear Brown. "
        "Thanks for watching.",
        12, "ClaudeTitleOutro",
        {
            "title": "Agents: AI that does things",
            "handle": "@NikBearBrown",
            "mascotIndex": MASCOT_INDEX,
            "period": True,
        },
        "Title restate 'Agents: AI that does things' with the terracotta "
        "period; handle '@NikBearBrown' beneath; mascot 4.",
        [
            {"at": "0.05", "event": "title writes; terracotta period lands"},
            {"at": "0.50", "event": "handle + mascot fade in"},
        ],
        act="outro",
    ),
]

SHEET = {"metadata": METADATA, "beats": BEATS}


def run_assertions():
    beats = SHEET["beats"]
    by_id = {b["beat_id"]: b for b in beats}

    # contract fields on every beat
    for b in beats:
        assert b.get("beat_id"), "beat missing beat_id"
        assert b.get("narration_text"), f"{b['beat_id']} missing narration_text"
        assert b.get("estimated_duration_s"), f"{b['beat_id']} missing estimated_duration_s"
        shot = b.get("shot") or {}
        assert shot.get("type") in ("GRAPHIC", "REMOTION"), \
            f"{b['beat_id']} shot.type must be GRAPHIC or REMOTION"
        if shot["type"] == "GRAPHIC":
            cls = (shot.get("manim") or {}).get("class")
            assert cls in MANIM_CLASSES, \
                f"{b['beat_id']} manim class {cls!r} not in scenes.py manifest"
            assert cls == f"{b['beat_id']}_{cls.split('_', 1)[1]}", \
                f"{b['beat_id']} class {cls!r} breaks <BID>_<Name> naming"
            assert shot.get("show"), f"{b['beat_id']} GRAPHIC beat needs a show block"
        else:
            assert (shot.get("remotion") or {}).get("pattern"), \
                f"{b['beat_id']} REMOTION beat needs a pattern"

    # film-level bands
    assert 10 <= len(beats) <= 16, f"beat count {len(beats)} outside 10–16"
    body = [b for b in beats if b["act"] in ("setup", "framework", "example", "risk")]
    assert 6 <= len(body) <= 10, f"body beats {len(body)} outside 6–10"
    total = sum(b["estimated_duration_s"] for b in beats)
    assert 180 <= total <= 360, f"total {total}s outside 180–360s"

    # voice / verdict / handoff contract
    assert "Liam, in for Bear" in by_id["B00"]["narration_text"], \
        "B00 must name the voice (IN-FOR-BEAR LAW)"
    v = by_id["B09"]["narration_text"]
    assert "irreversible" in v and "low stakes" in v, \
        "B09 verdict must restate the three-rule framework"
    assert by_id["B10"]["shot"]["remotion"]["props"]["command"], \
        "B10 handoff must carry the paste-into-your-AI prompt"

    print(f"OK: {len(beats)} beats, {len(body)} body, {total}s total")


def main():
    run_assertions()
    out = HERE / "beat_sheet.json"
    out.write_text(json.dumps(SHEET, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
    sys.exit(0)
