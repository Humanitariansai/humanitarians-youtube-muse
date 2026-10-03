# PROMPTS.md — "AI will fail." (why-ai-will-fail)

TTS voice: Kokoro `am_onyx` (Liam). One narration prompt per beat, in
script order. These are the exact strings in `beat_sheet.json`
(`narration_text`); regenerate that file with `python3 make_sheet.py`
rather than editing by hand. Bear renders audio locally — no audio is
committed.

## Per-beat narration (Kokoro input)

**B00 — COLD OPEN** (19.0 s)
> This is Humanitarians AI -- Liam, in for Bear. In 1977, the founder of
> one of the biggest computer companies on Earth said this: 'There is no
> reason for any individual to have a computer in his home.' He was the
> expert. He knew the industry cold. And he could not have been more wrong.

**B01 — OVERVIEW** (23.4 s)
> Tonight's pattern, in one breath: for over a century, the smartest
> people in every industry have looked at the next big thing and said,
> 'that will never work' -- and been wrong, nearly every time. There's a
> reason, and it has a name: the better you know the current game, the
> worse you are at seeing the next one. Today the loudest version is three
> words: AI will fail.

**B02 — THE LIST** (25.5 s)
> The list runs from 1977 to 2008 and beyond. Ken Olsen, founder of
> computer giant DEC: no one will want a computer at home. DEC is gone;
> there are roughly two billion PCs. Robert Metcalfe, inventor of
> Ethernet, said the internet would 'catastrophically collapse' in 1996.
> It didn't -- he blended his printed column and drank it on stage. Steve
> Ballmer, Microsoft's CEO: the iPhone had 'no chance.' Apple has sold
> over two billion.

**B03 — BLOCKBUSTER** (21.4 s)
> My favorite: 2008, Jim Keyes, CEO of Blockbuster: 'I've been frankly
> confused by this fascination that everybody has with Netflix.'
> Streaming -- movies over the internet, no store, no late fees -- looked
> like a toy to him. Netflix went on to pass three hundred million
> subscribers. Blockbuster has exactly one store left. It's in Bend,
> Oregon. People visit it like a museum.

**B04 — ELLISON + VALENTI** (27.9 s)
> Same year, Larry Ellison, CEO of Oracle, on cloud computing -- renting
> computers over the internet instead of owning them: 'It's complete
> gibberish. It's insane. When is this idiocy going to stop?' The cloud
> became a market of hundreds of billions a year, and Oracle now sells
> tens of billions of it -- to power AI, ironically. In 1982, Hollywood's
> top lobbyist called the VCR 'the Boston strangler' to filmmakers. Home
> video went on to earn Hollywood more than the box office.

**B05 — PENICILLIN** (23.1 s)
> And it's not just businessmen. In 1941, the British Medical Journal --
> the most respected medical journal in the world -- reviewed the biggest
> study yet of penicillin and concluded it had no use beyond the
> laboratory. Penicillin went on to become the most important drug of the
> twentieth century, saving hundreds of millions of lives. The gatekeepers
> of knowledge, writing in their own journal, got it completely wrong.

**B06 — INSIDER TRAP** (25.2 s)
> Why does this keep happening? These weren't stupid people. They were
> the best in the world at the current game -- and that was the problem.
> Blockbuster's CEO understood video rental better than anyone alive. But
> Netflix wasn't a better Blockbuster. It was a different game entirely:
> no stores, no late fees, movies by mail, then the internet. Grade the
> new thing on the old game's scoreboard, and it always looks like a toy.

**B07 — TOY CURVE** (26.6 s)
> Here's what the skeptics get right: the new thing usually IS bad at
> first. Early streaming video was a pixelated, buffering mess -- the
> skeptics had real evidence. But they were measuring a snapshot, not a
> trajectory. What matters isn't how good it is today. It's the direction
> it's moving, and how fast. 'Bad now' and 'failing' are not the same
> thing. Everything on that list of wrong calls looked like a toy -- right
> up until it didn't.

**B08 — FAMILIAR FORM** (27.9 s)
> Now listen to today's AI skeptics with that pattern in your ear. 'AI
> hallucinates' -- it makes things up, confidently: invented court cases,
> hands with six fingers. That's the pixel-soup stage. 'The productivity
> gains don't show in the data' -- in 1987 an economist said the same of
> computers: 'you can see the computer age everywhere but in the
> productivity statistics.' Daron Acemoglu now estimates AI adds half a
> percent to productivity over a decade. Maybe. Or maybe that's a snapshot.

**B09 — HONEST PART** (27.9 s)
> Let's be fair, the Teardown way: the skeptics are describing the present
> accurately. AI really does write like a genius one minute and a confused
> kid the next. Ted Chiang called it 'a blurry JPEG of the web.' That
> stings because it's partly true. The question the pattern forces isn't
> 'is AI flawed today?' -- it is. The question is: are you judging a
> trajectory by a snapshot? When smart people confuse the two, history
> says bet on the trajectory.

**B10 — ASYMMETRIC BET** (29.0 s)
> So what do you do? Run the bet both ways. If AI turns out to matter and
> you learned it -- you're ready. If it matters and you waited -- you're
> catching up from behind, in a faster market. If it's overhyped and you
> learned it -- you lost some hours and picked up a useful skill. If it's
> overhyped and you ignored it -- you saved those hours. Three of the four
> futures reward learning. The downside of learning is small. The downside
> of dismissing is large.

**B11 — VERDICT** (26.9 s)
> Here's the verdict. One: for a century, confident experts have declared
> the future dead on arrival -- and been wrong nearly every time. Two: the
> mechanism is the insider trap -- the better you know the current game,
> the worse you see the next one. Three: judge the trajectory, not the
> snapshot. Four: the bet is asymmetric -- learning is cheap, dismissing
> is expensive. One question to carry with you: am I scoring the new thing
> on the old game's scoreboard?

**B12 — YOUR TURN** (27.6 s)
> Your turn. Take this prompt to Claude -- or any AI you use -- and run
> the pattern on today's skepticism yourself: 'Find the five most common
> reasons people say AI will fail. For each one: give me the strongest
> version of the argument, the past technology it most resembles, and what
> would prove it right or wrong. Be a fair referee.' Read the answer
> twice -- once for the arguments, once for the resemblances. That's the
> pattern, working for you now.

**B13 — OUTRO** (3.8 s)
> AI will fail. Liam, in for Bear -- at Nik Bear Brown.

## The handoff prompt (B12, for the viewer to copy)

```
Find the five most common reasons people say AI will fail. For each one:
give me the strongest version of the argument, the past technology it
most resembles, and what would prove it right or wrong. Be a fair referee.
```

## Kokoro notes

- Voice `am_onyx`; keep default rate. The `--` markers are read as brief
  pauses; quoted lines get natural emphasis.
- Estimated total: 335.2 s at 2.9 wps — planning estimate only. The
  measured MP3s are the clock; conform the Manim scenes to them, not the
  reverse.
