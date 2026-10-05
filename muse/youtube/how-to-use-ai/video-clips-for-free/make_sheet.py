#!/usr/bin/env python3
"""make_sheet.py — Video clips for free (How to AI #35, Wave 6 "Making things").

Builds beat_sheet.json: 13 beats, show-tell style. Run: python3 make_sheet.py
Narration durations: speech at ~150 wpm (words / 2.5).
Contract assertions run at generation time; see CHECKS-REPORT.md.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "video-clips-for-free"
TITLE = "Video clips for free"

WPM = 2.5
def est(narration):
    return round(len(narration.split()) / WPM, 1)

def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": est(narration),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show,
                     "manim": {"class": cls}, "motion_claim": image}}

def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": est(narration),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b

# ── Body beats (drawings; the film's cast: the vids.new window, the clip
#    frame, the "free tier" budget jar, the timeline, the script pages) ──
B = [
 beat("B00", "Google Vids is Google's video app. It opens at vids.new, and earlier this year it grew an AI clip maker: you type a sentence, and Veo turns it into a short, high-definition video clip.",
      "B00_VidsWindow",
      "A browser window with a dark title bar, label 'vids.new'; a film-clip frame grows out of it with a terracotta spark.",
      [{"at": 0.1, "event": "browser window fades in"},
       {"at": 0.3, "event": "clip frame grows out of the window"}]),
 beat("B01", "The unit is the clip: one short shot, a few seconds long, in high definition. Think of each clip as a single shot in your video — never the whole video.",
      "B01_OneClip",
      "One film-strip frame with a play triangle drops in; label 'one clip'.",
      [{"at": 0.1, "event": "clip frame drops in"},
       {"at": 0.5, "event": "label lands"}]),
 beat("B02", "A personal Google account gets a free monthly allowance of these clips. It isn't unlimited: treat it as a small monthly budget, and it refills each month.",
      "B02_TheBudget",
      "A kraft budget jar labelled 'free tier'; three clip boxes drop into it, one per spoken beat.",
      [{"at": 0.1, "event": "budget jar arrives"},
       {"at": 0.3, "event": "first clip drops in"},
       {"at": 0.55, "event": "two more clips drop in"}]),
 beat("B03", "Spend each clip where AI video wins: a shot you could never film yourself and won't find in stock footage. A drone flight over a volcano. A scene from history. A product shot that doesn't exist yet.",
      "B03_AIWins",
      "A clip frame holding a stylized volcano (dark silhouette, terracotta glow); an ink check lands; label 'AI wins'.",
      [{"at": 0.1, "event": "clip frame with volcano"},
       {"at": 0.5, "event": "check lands"}]),
 beat("B04", "Don't spend them on the generic stuff: a sunset, coffee pouring, hands typing. Vids comes with free stock footage — use stock for that, and keep your clips for the shots only AI can make.",
      "B04_Stock",
      "An open stock box with film strips, label 'stock'; the free-tier jar sits beside it, untouched.",
      [{"at": 0.1, "event": "stock box opens"},
       {"at": 0.4, "event": "jar stays full beside it"}]),
 beat("B05", "Plan before you spend. Write the video in Vids first: the script, the scenes, the shot list. Then spend clips only on the hero shots, and let stock cover everything else.",
      "B05_ScriptFirst",
      "Two script pages; a timeline with three slots; one AI clip drops into the hero slot, stock strips into the others; label 'script first'.",
      [{"at": 0.1, "event": "script pages land"},
       {"at": 0.35, "event": "timeline slots appear"},
       {"at": 0.6, "event": "hero clip drops in"}]),
 beat("B06", "Like a clip but want it longer? Extend it — grow the scene instead of starting over. You can also test several prompts at once. Just remember: every try spends one clip from the jar.",
      "B06_Extend",
      "A clip frame elongates to double width (extend arrow); a prompt pill spawns two test clips; one clip leaves the budget jar; label 'extend'.",
      [{"at": 0.1, "event": "clip frame"},
       {"at": 0.35, "event": "frame extends"},
       {"at": 0.65, "event": "jar loses one clip"}]),
 beat("B07", "The free tier covers clips. The extras — custom AI music, avatars that read your script — need a paid plan. Skip them for now: Vids ships with free stock music and voices, and nothing here stops your first video.",
      "B07_PaidExtras",
      "The free-tier jar with its clips; two dim cards 'music' and 'avatar' sit greyed behind it; label 'paid extras'.",
      [{"at": 0.1, "event": "jar with clips"},
       {"at": 0.4, "event": "dim music/avatar cards"}]),
 beat("B08", "One last thing. The free number has already moved before, and Google hasn't promised it stays put. Before you plan a video, check vids.new for the current limit — never plan around a number from a film.",
      "B08_CheckTheNumber",
      "The budget jar with a gauge; the needle swings to a new mark (the number changed); label 'check vids.new'.",
      [{"at": 0.1, "event": "jar with gauge"},
       {"at": 0.5, "event": "needle moves to a new mark"}]),
]

OPEN = [
 remotion("BIDEA", "the question",
    "Hallo. This is Liam, in for Bear. Google has quietly made AI video free for everyone. But the real question isn't whether you can make video clips for free. It's how you spend them.",
    "BrutalistHesitantWriter",
    {"text": "Can I make a whole video\nwith AI for free?", "triggerWords": "a whole video", "replacementWords": "video clips",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Can I make a whole video'"},
     {"at": 0.6, "event": "backspaces 'a whole video' → 'video clips' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive whole-video question and corrects it to the real one: how to spend free clips.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "Three terms. Vids: Google's video app, which opens at vids.new. Veo: the AI model that turns a sentence into a video clip. And the free tier: a free monthly allowance of clips — the current number is at vids.new.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "Vids", "meaning": "Google's video app — it opens at vids.new"},
               {"term": "Veo", "meaning": "the AI model that turns a sentence into a video clip"},
               {"term": "free tier", "meaning": "a free monthly allowance of clips (current number at vids.new)"}],
     "folderLabel": "@NikBearBrown", "durationSeconds": est("Three terms. Vids: Google's video app, which opens at vids.new. Veo: the AI model that turns a sentence into a video clip. And the free tier: a free monthly allowance of clips — the current number is at vids.new.")},
    [{"at": 0.12, "event": "'Vids' lands"}, {"at": 0.5, "event": "'Veo' lands"}, {"at": 0.78, "event": "'free tier' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Help me plan a 30-second announcement video for [my cause]: a one-paragraph script, a shot list, and "
             "mark each shot as AI clip or stock footage — AI clips only for shots I can't film or find in stock. "
             "End with the three hero shots I should generate first.")
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things yourself. "
    "Is every AI clip a shot you couldn't film or find in stock? And did you check vids.new for the current free number before generating?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "HOW TO AI — YOUR TURN", "segment": "Free Video Clips", "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": ["Check: every AI clip is a shot you couldn't film or find in stock.",
                "Check: you checked vids.new for the current free number first."],
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, with the voice carrying the explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, empty-frame and contrast still apply.")
for b in B:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}

B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "HOW TO AI · MAKING THINGS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "smart, pragmatic general audience — not AI experts; every term explained in plain words",
    "source_doc": "web research 2026-10-05 (see SOURCES.md): Google Vids free tier for personal accounts (Veo 3.1, April 2026)",
    "playlist": "How to AI", "chapter_number": 35, "series_wave": "Wave 6: Making things",
    "tags": ["Google Vids", "Veo", "AI video", "free tier", "video clips", "How to AI", "Nik Bear Brown"]},
    "beats": B}

# ── Contract assertions ──
def _assert(cond, msg):
    assert cond, msg

_assert(len(B) == 13, f"expected 13 beats, got {len(B)}")
ids = [b["beat_id"] for b in B]
_assert(len(ids) == len(set(ids)), "duplicate beat ids")
_assert(ids[0] == "BIDEA" and ids[-1] == "BOUT", "BIDEA first / BOUT last")
body = [b for b in B if b["lane"] == "manim"]
_assert([b["beat_id"] for b in body] == [f"B{i:02d}" for i in range(9)],
        f"body beats must be B00..B08, got {[b['beat_id'] for b in body]}")
for b in B:
    _assert(b["narration_text"].strip(), f"{b['beat_id']}: empty narration")
    _assert(b["estimated_duration_s"] > 0, f"{b['beat_id']}: bad duration")
    _assert(b["voice"] == "am_onyx", f"{b['beat_id']}: voice must be am_onyx (Kokoro code), got {b['voice']!r}")
    _assert(b["engine"] == "kokoro", f"{b['beat_id']}: engine must be kokoro")
    _assert(b["shot"].get("show"), f"{b['beat_id']}: empty shot.show")
for b in body:
    _assert(b["shot"]["type"] == "GRAPHIC" and b["shot"]["manim"]["class"].startswith(b["beat_id"] + "_"),
            f"{b['beat_id']}: manim class name must start with beat id")
idea = B[0]
_assert(idea.get("lead_silence_s") == 0.8, "BIDEA: lead_silence_s 0.8")
tw = idea["shot"]["remotion"]["props"]["triggerWords"]
_assert(tw in idea["shot"]["remotion"]["props"]["text"], "BIDEA: triggerWords must appear verbatim in text")
_assert(not tw.endswith(("?", "!", ".")), "BIDEA: triggerWords must not end in punctuation")
defs = B[1]
_assert(defs["shot"]["remotion"]["pattern"] == "ClaudeDefinitions", "BDEFS pattern")
_assert(all(len(t["term"]) <= 17 for t in defs["shot"]["remotion"]["props"]["terms"]),
        "BDEFS: ClaudeDefinitions truncates terms > ~17 chars")
_assert(defs["shot"]["remotion"]["props"]["durationSeconds"] > 0, "BDEFS: durationSeconds")
yt = [b for b in B if b["beat_id"] == "BHTF"][0]
_assert("YOUR TURN" in yt["shot"]["remotion"]["props"]["topic"], "BHTF topic must contain YOUR TURN")
_assert(YT_PROMPT in yt["narration_text"], "BHTF: prompt must be read verbatim in narration")
out = B[-1]
_assert(out.get("kind") == "outro_voice" and out.get("tail_silence_s") == 1.0, "BOUT: outro_voice + 1.0 s tail")
md = sheet["metadata"]
_assert(md["bookend_exempt"] == ["cold-open", "bvdt"], "bookend_exempt")
_assert(md["channel"] == "claude-liam" and md["voice"] == "am_onyx" and md["register"] == "Teardown", "identity constants")
total = sum(b["estimated_duration_s"] for b in B)
_assert(150 <= total <= 260, f"total duration {total}s outside 150–260 s band")

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(total, 1), "s")
