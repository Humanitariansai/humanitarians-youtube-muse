# SCRIPT.md — Claude, Unstuck (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-troubleshooting` (Teardown, Ch.14 "Troubleshooting and
Staying Current") — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop); cold open replaced
with the BrutalistHesitantWriter; close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
My plugin's broken. Where's the fix that matches my screen? Wrong target —
the real question is what matches the concept.

## Act I — When it breaks

**NB01 — Frustration, not the bug** (source B01)
Things will go wrong — a plugin misbehaves, a connection drops, a result
disappoints. The real risk isn't the bug. It's letting quiet frustration
turn into giving up. Diagnosing keeps you in the game.

**NB02 — Surface vs. bedrock** (source B02)
Here's the discipline. The interface — buttons, menus, wording — changes
constantly. Underneath sits something durable: what the plugin is for,
what it can and can't do. Troubleshoot from there.

## Act II — The common failures

**NB03 — Five familiar shapes** (source B03)
Most breakage takes one of five shapes: won't appear, won't authenticate,
results feel generic, everything runs slow, or a command isn't recognized.
Each has a durable cause — and a durable fix.

**NB04 — Reopen to reload** (source B04)
Plugin missing after you installed it? Plugins load when the app starts,
so a mid-session install may not show yet. Close it completely, reopen it,
and it loads. Still missing? Reinstall it from the sidebar.

**NB05 — Credentials go stale** (source B05)
A service that won't authenticate almost always means stale credentials —
a token expired, a password changed, access got revoked. Disconnect the
service and reconnect it. If your company gates outside access, you may
need IT's approval.

**NB06 — Broad by default** (source B06)
Results feel generic? That's not a fault — the defaults are deliberately
broad. Feed it your context: your brand voice, your process, your
standards. The output sharpens past the point where it's actually useful.

**NB07 — Shrink the scope** (source B07)
Slow operations usually reach outside your machine — a database lookup, a
web search, a CRM query all cost more than local work. The fix is scope:
ask for one date range, one folder, not everything everywhere.

**NB08 — Type slash, look** (source B08)
A slash-command not recognized? Make sure the plugin is installed and
enabled, then type a single slash to see every command available right
now. Still missing? The plugin most likely needs a restart.

## Act III — The four steps

**NB09 — Check, then toggle** (source B09)
Two quick diagnostics first. Check the plugins list to see what's
installed and active — your first move for anything plugin-related. If
one's misbehaving, disable it, then re-enable it. That reloads its config
and clears most glitches.

**NB10 — Four steps, in order** (source B10)
Then the loop that resolves most problems, in order. One: is the plugin
installed and active? Two: are its connections authorized? Three: try a
simpler request to isolate the issue. Four: restart. Most trouble dies
inside those four steps.

**NB11 — Isolate by shrinking** (source B11)
That third step carries more weight than its size suggests. Shrink the
request until it works, then grow it back. The exact moment it breaks
again tells you precisely where the problem lives.

## Act IV — Staying current

**NB12 — Nothing sits still** (source B12)
Plugins don't sit still. Anthropic improves the official ones, and
community creators ship their own updates. Each release can add
capabilities, fix bugs, or run faster — so what you learned last month
may behave differently today.

**NB13 — The screen dates** (source B13)
And that's the catch. Most updates apply automatically, so the interface
shifts underneath you. Anything written down about the screen starts
dating the moment it's written. The concept underneath does not.

**NB14 — Check the live sources** (source B14)
So verify specifics against sources that stay current. Each plugin's own
docs — on its page and inside the app. The plugin directory, where others
have already solved your problem. And the official channels — the
Anthropic blog and release notes — for what actually changed.

**NB15 — A monthly habit** (source B15)
Make it a habit. Set a monthly reminder to browse the directory and see
what's new. And when a plugin you rely on changes, read the changelog — a
new feature might be exactly what you were missing.

Source B16 ("Because that's the real skill here... the interface dates,
the mental model doesn't") is not carried as a separate body beat — it
already states the reel's carry-out almost verbatim, so its content folds
directly into BCRY instead of being said twice.

## Close

**BCRY — carry-out**
When something breaks, don't chase the screen — return to what the plugin
is for, and check the docs for what's current. The interface dates; the
mental model doesn't.

**BHTF — your turn**
Your turn. Paste this into Claude: a plugin I installed isn't showing up
and I'm not sure why. Diagnose it with me: ask whether I restarted after
installing, whether the plugins list shows it as active, and whether its
connections are authorized. Then give me the four-step check to run in
order, and point me to the one official source to check in case something
changed.

**BOUT — outro**
Claude, Unstuck — troubleshooting and staying current. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–NB01 | a plugin breaking feels like a bug; the real risk is giving up on it |
| Wrong guess | B00 → NB02 | "the fix has to match my exact screen" corrected to "return to the concept" |
| Mechanism | NB03–NB11 | five failure shapes, each with a durable cause and fix; the four-step loop |
| Anchor | NB08 → NB09–NB10 | checking `/plugins` first (NB08's fix), then the same check opens the four-step loop |
| Both directions | NB12 → NB13 | updates keep the plugin current (good); they also mean the interface itself keeps shifting (the catch) |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct description of
product behavior (plugins load on start, credentials expire, defaults are
broad, scope affects latency, `/plugins` lists active plugins, updates are
automatic, docs/directory/release-notes are the current sources) — not an
inference about hidden internals. Per simple's ONE-FLAG LAW, when the
source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 24 core beats (deep-explainer chassis: 4 act-title cards
C01–C04 + 16 numbered body beats B01–B16 + V01 verdict recap + H01
your-turn + O01 outro), plus a trailing duplicate blank-narration
BVDT/BHTF/BOUT bookend triad not counted among the 24 (per
`metadata.build.of: 24`). hai-simple's spine has no act-title-card slot,
no separate verdict-recap beat (Plain register carries one carry-out
sentence, not a bulleted recap — CARRY-OUT LAW), and no duplicate bookend
tail, so: the 4 act cards were dropped (their titles now land as narration
transitions instead of separate beats); B16 (already a near-verbatim
statement of the reel's own carry-out) folded into BCRY instead of being
kept as its own beat, since keeping it would say the same thing as BCRY
twice; the 16 numbered body beats carried over one-to-one as NB01–NB15 (no
merge was needed — each source beat already carries exactly one fact, so
merging any pair would have doubled up an idea rather than combining two
half-ideas); and the source's own body-close (V01 recap / H01 your-turn /
O01 outro) was kept as the reel's one close (BCRY/BHTF/BOUT, V01's bullet
recap re-expressed as BCRY's single sentence), dropping the duplicate
blank-narration bookend triad rather than rendering two closes back to
back. Logged per BUILD-LOG.md.
