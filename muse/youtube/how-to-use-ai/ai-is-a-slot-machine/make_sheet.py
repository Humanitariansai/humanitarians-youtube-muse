#!/usr/bin/env python3
"""make_sheet.py — AI is a slot machine. (Humanitarians AI YouTube film)

Builds beat_sheet.json: 16 beats, show-tell spine (hesitant writer -> terms
-> the machine -> five stages -> gambler's playbook -> recap -> your turn ->
outro). Skill: show-tell. Persona: Liam, in for Bear. TTS: Kokoro am_onyx.
Register: Teardown. Channel: claude-liam. Watermark: @NikBearBrown.

Source argument (mirror repo nikbearbrown/humanitarians-youtube-muse,
claude-for-artificial-intelligence/ai-is-a-slot-machine): the five stages of
AI use (denial, anger, bargaining, depression, acceptance), with the
mechanism "AI is probabilistic, not deterministic — a slot machine", and the
acceptance-stage strategy "the AI gambler: generate many, keep the best".
Rewritten for a smart, pragmatic general audience: every term explained in
plain language, in the same breath it is first used.

Run: python3 make_sheet.py   (writes beat_sheet.json in cwd)
Durations: ~150 wpm narration => words/2.5 + small pause, rounded.
"""
import json

BEATS = [
    {
        "id": "BIDEA", "scene": "M01", "dur_s": 24, "act": "hook",
        "voice": "Muse", "greeting": "Hallo",
        "line": ("Hallo. This is Liam, in for Bear. AI is a truth machine \u2014 no. "
                 "AI is a slot machine. Every prompt is a pull of the lever, and "
                 "nobody can predict what comes out. This film walks you through "
                 "the five stages people keep running into with AI \u2014 and the "
                 "last one, where you pull the lever like a pro."),
        "screen": ("Hesitant writer: a hand writes 'AI is a truth machine.', "
                   "strikes through 'truth machine', and corrects it to "
                   "'AI is a slot machine.'"),
        "shot": {"type": "MANIM", "manim": {"class": "M01_Bidea"},
                 "show": [{"at": "0.05", "event": "paper card fades in; hand cursor writes the naive line"},
                          {"at": "0.45", "event": "terracotta strike-through crosses 'truth machine'"},
                          {"at": "0.65", "event": "'slot machine' writes in beside it"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "show-tell bookend beat: one card, one correction"}}},
    {
        "id": "BDEFS", "scene": "M02", "dur_s": 18, "act": "hook",
        "voice": "Muse",
        "line": ("Four terms. Prompt: what you type to the AI. Probabilistic: "
                 "the opposite of deterministic \u2014 same input, different answer "
                 "every time you run it. Hallucination: a confident wrong answer. "
                 "And the AI gambler: the person who finally gets it \u2014 pull "
                 "many times, keep the best."),
        "screen": ("Four term cards appear one by one: prompt / probabilistic / "
                   "hallucination / the AI gambler."),
        "shot": {"type": "MANIM", "manim": {"class": "M02_Bdefs"},
                 "show": [{"at": "0.05", "event": "card 1 'prompt' lands"},
                          {"at": "0.30", "event": "card 2 'probabilistic' lands"},
                          {"at": "0.55", "event": "card 3 'hallucination' lands"},
                          {"at": "0.78", "event": "card 4 'the AI gambler' lands, terracotta edge"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "show-tell bookend beat: four cards on cream"}}},
    {
        "id": "B00", "scene": "M03", "dur_s": 16, "act": "1",
        "voice": "Muse",
        "line": ("Meet the machine. It looks like a slot machine with a keyboard. "
                 "You type a prompt, pull the lever, and out comes an answer \u2014 "
                 "words, pictures, code, whatever you asked for. One pull, one "
                 "answer. That's the whole machine."),
        "screen": ("The slot machine builds itself: cabinet, reel window, answer "
                   "tray, lever. 'prompt in' arrow above, 'answer out' arrow below."),
        "shot": {"type": "MANIM", "manim": {"class": "M03_Machine"},
                 "show": [{"at": "0.05", "event": "cabinet grows up from a shadow"},
                          {"at": "0.30", "event": "reel window and tray fade in"},
                          {"at": "0.55", "event": "lever drops in on the right, knob terracotta"},
                          {"at": "0.80", "event": "'prompt in' / 'answer out' arrows label the flow"}]}},
    {
        "id": "B01", "scene": "M04", "dur_s": 20, "act": "1",
        "voice": "Muse",
        "line": ("But here's the catch. The machine never quite answers the same "
                 "way twice. Pull the lever three times on the same prompt and you "
                 "often get three different answers \u2014 a poem, a list, a joke. "
                 "The engine inside \u2014 called "
                 "a model \u2014 is guessing the most likely next word, every word, "
                 "every time. That is what probabilistic means."),
        "screen": ("One prompt card stays fixed; the lever pulls three times and "
                   "three different answer cards land in the tray: a poem, a list, "
                   "a joke."),
        "shot": {"type": "MANIM", "manim": {"class": "M04_Probabilistic"},
                 "show": [{"at": "0.10", "event": "prompt card 'write about the sea' pins above the machine"},
                          {"at": "0.30", "event": "lever pulls; answer card 1 'a poem' lands"},
                          {"at": "0.55", "event": "lever pulls; answer card 2 'a list' lands"},
                          {"at": "0.78", "event": "lever pulls; answer card 3 'a joke' lands"}]}},
    {
        "id": "B02", "scene": "M05", "dur_s": 18, "act": "1",
        "voice": "Muse",
        "line": ("And that breaks people. The way we react to AI follows a pattern "
                 "\u2014 borrowed from the five stages of grief: denial, anger, "
                 "bargaining, depression, and finally acceptance. Psychologist "
                 "Elisabeth K\u00fcbler-Ross first described those stages in 1969 \u2014 "
                 "and every AI user seems to walk the same road."),
        "screen": ("A five-step meter lights left to right: denial, anger, "
                   "bargaining, depression, acceptance. The last step glows "
                   "terracotta."),
        "shot": {"type": "MANIM", "manim": {"class": "M05_Stages"},
                 "show": [{"at": "0.10", "event": "the five-step meter draws"},
                          {"at": "0.30", "event": "denial, anger, bargaining light up"},
                          {"at": "0.60", "event": "depression lights"},
                          {"at": "0.85", "event": "acceptance lights in terracotta"}]}},
    {
        "id": "B03", "scene": "M06", "dur_s": 16, "act": "2",
        "voice": "Muse",
        "line": ("Stage one: denial. The AI gave you one bad answer, and you've "
                 "been telling that story ever since \u2014 it's useless. Or the "
                 "other flavor of denial: you paste its answers straight into "
                 "your work and never check, because the machine said so."),
        "screen": ("An answer card stamped with a red X; a speech loop circles "
                   "back: 'it's useless'."),
        "shot": {"type": "MANIM", "manim": {"class": "M06_Denial"},
                 "show": [{"at": "0.10", "event": "answer card lands in the tray"},
                          {"at": "0.35", "event": "a terracotta X stamps the card"},
                          {"at": "0.60", "event": "speech loop draws around the card: 'it's useless'"},
                          {"at": "0.85", "event": "loop arrows keep circling"}]}},
    {
        "id": "B04", "scene": "M07", "dur_s": 16, "act": "2",
        "voice": "Muse",
        "line": ("Stage two: anger. You get a wrong answer, you screenshot it, you "
                 "post it. Look at this idiot machine. The anger feels good. But "
                 "it keeps you exactly where you are \u2014 arguing with the slot "
                 "machine instead of playing it."),
        "screen": ("A phone with screenshot frames beside the machine; angry "
                   "zigzag bolts strike the cabinet, which shakes."),
        "shot": {"type": "MANIM", "manim": {"class": "M07_Anger"},
                 "show": [{"at": "0.10", "event": "phone slides in, screenshots stack"},
                          {"at": "0.45", "event": "terracotta anger bolts strike the cabinet"},
                          {"at": "0.70", "event": "cabinet shakes side to side"}]}},
    {
        "id": "B05", "scene": "M08", "dur_s": 18, "act": "2",
        "voice": "Muse",
        "line": ("Stage three: bargaining. This is where most people get stuck. "
                 "You hunt for the perfect prompt \u2014 the magic words that make "
                 "the machine pay out every time. There is no perfect prompt. "
                 "There is only a lever, and it pays out on average, not on command."),
        "screen": ("A figure polishes one lever with dials and gauges; the label "
                   "reads 'the perfect prompt'."),
        "shot": {"type": "MANIM", "manim": {"class": "M08_Bargaining"},
                 "show": [{"at": "0.10", "event": "single lever on a plinth; figure's hand polishes it"},
                          {"at": "0.45", "event": "dials and gauges grow around the lever"},
                          {"at": "0.75", "event": "label 'the perfect prompt' lands under it"}]}},
    {
        "id": "B06", "scene": "M09", "dur_s": 16, "act": "2",
        "voice": "Muse",
        "line": ("Stage four: depression. Six hours at the keyboard, tweaking and "
                 "re-rolling, and nothing you can use. Most people quit AI right "
                 "here. But the machine didn't beat you \u2014 the strategy did. "
                 "One perfect pull was never the game."),
        "screen": ("A clock face spins; the tray sits empty; the lever droops."),
        "shot": {"type": "MANIM", "manim": {"class": "M09_Depression"},
                 "show": [{"at": "0.10", "event": "clock face fades in above the machine"},
                          {"at": "0.40", "event": "clock hands spin fast"},
                          {"at": "0.70", "event": "tray shown empty; lever droops"}]}},
    {
        "id": "B07", "scene": "M10", "dur_s": 18, "act": "3",
        "voice": "Muse",
        "line": ("Stage five: acceptance. The AI gambler. She pulls the lever a "
                 "hundred times, keeps the five best answers, and throws the rest "
                 "away. A bad output isn't failure \u2014 it's a pull that didn't "
                 "hit. The next one might. The ratio is the whole game."),
        "screen": ("The lever pumps fast; answer cards flood the trays; the five "
                   "best rise with checks while the rest fade out."),
        "shot": {"type": "MANIM", "manim": {"class": "M10_Gambler"},
                 "show": [{"at": "0.10", "event": "lever starts pumping; cards flood the trays"},
                          {"at": "0.50", "event": "five cards rise above the pile with terracotta checks"},
                          {"at": "0.80", "event": "the rest fade to ghost grey"}]}},
    {
        "id": "B08", "scene": "M11", "dur_s": 18, "act": "3",
        "voice": "Muse",
        "line": ("So how do you get there? The gambler's playbook, rule one: "
                 "treat the machine as probabilistic. Default to asking for three "
                 "versions in every prompt. Give me three different angles on "
                 "this. You'll never go back to one-shot prompting once you've "
                 "seen your options side by side."),
        "screen": ("One prompt card fans into three answer cards, side by side; "
                   "'ask for 3' tag."),
        "shot": {"type": "MANIM", "manim": {"class": "M11_ThreeVersions"},
                 "show": [{"at": "0.15", "event": "prompt card pins above the machine"},
                          {"at": "0.45", "event": "three answer cards fan out side by side"},
                          {"at": "0.80", "event": "'ask for 3' tag stamps the prompt"}]}},
    {
        "id": "B09", "scene": "M12", "dur_s": 20, "act": "3",
        "voice": "Muse",
        "line": ("Rule two: stop yelling at the machine and start managing it "
                 "\u2014 like an intern. When it gives you something wrong, you "
                 "don't quit, you correct. And this one line beats ninety percent "
                 "of magic prompts: you missed the point \u2014 ask me clarifying "
                 "questions. A junior that asks questions is a junior that learns."),
        "screen": ("Answer card gets a correction arrow; a speech bubble reads "
                   "'ask me clarifying questions'; a check lands."),
        "shot": {"type": "MANIM", "manim": {"class": "M12_Intern"},
                 "show": [{"at": "0.15", "event": "wrong answer card lands with an X"},
                          {"at": "0.40", "event": "correction arrow redraws it into a better card"},
                          {"at": "0.70", "event": "speech bubble 'ask me clarifying questions' pops up"},
                          {"at": "0.88", "event": "check lands on the bubble"}]}},
    {
        "id": "B10", "scene": "M13", "dur_s": 18, "act": "3",
        "voice": "Muse",
        "line": ("Rule three: think in batches, not in perfect prompts. Ask for "
                 "five options. Regenerate the weak parts. The answer you're "
                 "trying to coax out of one magic pull is already sitting inside "
                 "the batch \u2014 pull enough times."),
        "screen": ("Five answer cards in a row; the weak ones regenerate into "
                   "strong ones; 'pull enough times' tag."),
        "shot": {"type": "MANIM", "manim": {"class": "M13_Batches"},
                 "show": [{"at": "0.15", "event": "five cards land in a row"},
                          {"at": "0.50", "event": "two weak cards flip into strong ones"},
                          {"at": "0.80", "event": "'pull enough times' tag lands"}]}},
    {
        "id": "BVDT", "scene": "M14", "dur_s": 18, "act": "recap",
        "voice": "Muse",
        "line": ("So: the machine is probabilistic \u2014 same prompt, different "
                 "answer every time. The five stages run denial, anger, "
                 "bargaining, depression, then acceptance. And the gambler's "
                 "playbook is three rules: ask for three versions, manage it "
                 "like an intern, and think in batches."),
        "screen": ("Three recap lines reveal with dot bullets, one per act."),
        "shot": {"type": "MANIM", "manim": {"class": "M14_Recap"},
                 "show": [{"at": "0.10", "event": "recap line 1 reveals: probabilistic"},
                          {"at": "0.40", "event": "recap line 2 reveals: the five stages"},
                          {"at": "0.70", "event": "recap line 3 reveals: the three rules"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "show-tell recap beat: three lines on cream"}}},
    {
        "id": "BHTF", "scene": "M15", "dur_s": 22, "act": "do_today",
        "voice": "Muse",
        "line": ("Your turn. Take the task you're procrastinating on right now "
                 "\u2014 the email, the plan, the draft \u2014 and run the slot "
                 "machine on it. Paste this into Claude: give me five different "
                 "versions of this, then ask me clarifying questions about which "
                 "one to keep. Then keep the best and trash the rest. That's the "
                 "whole game."),
        "screen": ("Do-today card: the suggested prompt reads in, then two "
                   "viewer checks: keep the best / trash the rest."),
        "shot": {"type": "MANIM", "manim": {"class": "M15_YourTurn"},
                 "show": [{"at": "0.15", "event": "composer card fades in"},
                          {"at": "0.35", "event": "the suggested prompt types in"},
                          {"at": "0.75", "event": "two checks land: keep the best, trash the rest"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "show-tell handoff beat: prompt card on cream"}}},
    {
        "id": "BOUT", "scene": "M16", "dur_s": 10, "act": "outro",
        "voice": "Muse",
        "line": ("AI is a slot machine. Liam, in for Bear. At Nik Bear Brown. "
                 "Thanks for watching."),
        "screen": ("Title card: 'AI is a slot machine.' with the terracotta "
                   "period; @NikBearBrown handle beneath."),
        "shot": {"type": "MANIM", "manim": {"class": "M16_Outro"},
                 "show": [{"at": "0.10", "event": "title writes in, serif"},
                          {"at": "0.60", "event": "terracotta period drops; handle fades in"}],
                 "qc": {"sparse_by_design": True,
                         "sparse_reason": "show-tell outro beat: title card"}}},
]

METADATA = {
    "title": "AI is a slot machine.",
    "slug": "ai-is-a-slot-machine",
    "series": "Humanitarians AI — how to use AI",
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
    "bookend_exempt_reason": ("show-tell drops the composer cold open and the "
                              "verdict card; the film opens on the hesitant "
                              "writer and recaps in BVDT."),
    "playlist": "how-to-use-ai",
    "tags": ["ai-explainer", "slot-machine", "probabilistic", "five-stages",
             "prompting", "general-audience"],
    "derived_from": ("nikbearbrown/humanitarians-youtube-muse:"
                     "claude-for-artificial-intelligence/ai-is-a-slot-machine"),
    "audience": "smart, pragmatic general audience; not necessarily AI experts",
}

if __name__ == "__main__":
    ids = [b["id"] for b in BEATS]
    assert len(BEATS) == 16, len(BEATS)
    assert 13 <= len(BEATS) <= 22, "beat count outside 13-22 band"
    assert ids[0] == "BIDEA" and ids[1] == "BDEFS", ids[:2]
    assert ids[-3:] == ["BVDT", "BHTF", "BOUT"], ids[-3:]
    body = [b for b in BEATS if b["act"] in ("1", "2", "3")]
    assert len(body) == 11, len(body)
    recap = next(b for b in BEATS if b["id"] == "BVDT")["line"].lower()
    for kw in ["probabilistic", "denial", "anger", "bargaining", "depression",
               "acceptance", "three versions", "intern", "batches"]:
        assert kw in recap, f"recap missing {kw!r}"
    idea = BEATS[0]["line"]
    assert "Liam, in for Bear" in idea, "IN-FOR-BEAR LAW: name the voice"
    htf = next(b for b in BEATS if b["id"] == "BHTF")["line"]
    assert "Paste this into Claude" in htf, "handoff must name the prompt"
    total = sum(b["dur_s"] for b in BEATS)
    assert 270 <= total <= 420, f"total {total}s outside 4.5-7 min band"
    BS = {"metadata": METADATA, "beats": BEATS}
    print(f"beats={len(BEATS)} body={len(body)} "
          f"total={total}s (~{total//60}m{total%60:02d}s)")
    with open("beat_sheet.json", "w") as f:
        json.dump(BS, f, indent=2)
