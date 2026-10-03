# PROMPTS — "Your Weekly Video, Handled."

## Open slots: none

This reel has **no unfilled slots**. Every one of its 13 beats is machine-rendered
Remotion, so there is no pantry still to source, no slate to replace, and no
prompt card for a human to fulfil. `./art todo` should report an empty fill-list.

The section below therefore records the prompts that *built* the reel rather than
prompts that are owed — kept so the next fellow can regenerate any beat.

## Per-beat regeneration prompts

Each new component lives in `runtime/remotion/src/scenes/` in the toolkit and is
registered under the `hai-weekly-submission` folder in `Root.tsx`. To re-render
one beat only:

```bash
python3 runtime/scripts/remotion_scenes.py <reel> --only B07 --force
```

| Beat | Component | Prompt that produced it |
|---|---|---|
| B01 | `HaiSubmitRequirementGrid` | "The weekly deliverable as a multiplication: two topic cards on the left, two format chips fanning right from each (16:9 YouTube, 9:16 Shorts), a tally block counting to 4 on the far right. Footnote the two-week research-update floor. Claude palette, terracotta as the one accent." |
| B02 | `HaiSubmitClaudeSetup` | "A fidelity mock of the Claude desktop app: sidebar with recents and a folder chip, chat thread on the right. User message types itself, Claude replies in serif, a PERMISSION REQUESTED card rises with the real git clone URL in mono, a cursor travels to Allow and clicks it, then install lines tick green. The last frame must make the point: nothing was typed into a terminal." |
| B03 | `HaiSubmitBeatSheet` | "Left: one plain-English ask in a user bubble, plus a spark line reading 'authoring beat_sheet.json…'. Right: a beat_sheet.json table, columns BEAT / ACT / NARRATION / VISUAL, six rows staggering in with the lane tag colour-coded." |
| B04 | `HaiSubmitAudioClock` | "Audio-first, made visible. Two horizontal rails spanning the frame. Top: five audio blocks with deterministic waveforms, each labelled with its measured seconds. Dashed ticks drop from each. Bottom: visual blocks springing to exactly the same widths. State the rule: timing is never adjusted by hand." |
| B05 | `HaiSubmitReviewLoop` | "A four-node cycle — Claude compiles, YOU watch, YOU say what's off, Claude rebuilds — with the two human nodes filled terracotta and the two machine nodes white. A return arc draws underneath and closes the loop, labelled REPEAT UNTIL IT LANDS. Pull-quote on the asymmetry underneath." |
| B06 | `HaiSubmitFormats` | "A 4K 16:9 master frame on the left. A dashed ghost of it reflows — position and proportion interpolated — into a 9:16 portrait frame on the right, labelled DERIVED AUTOMATICALLY. Right rail lists the week's four real filenames and totals to 4 FILES · EVERY FRIDAY." |
| B07 | `HaiSubmitGitHubDocs` | "GitHub's own dark surface. Breadcrumb down into fellows/, a toolbar showing 'Pull request opened', six documentation files committing green with KB sizes, then a red NOT IN THE REPO — TOO LARGE divider with *.mp4 and *.mp3 struck through and redirected to Drive. Footer states the 25 MB rule. Exact repo URL beneath the panel." |
| B08 | `HaiSubmitForkBranch` | "A git-graph answering one question: do you have write access? Curved edges split from a decision node into a blue FORK lane (fork → push → pull request) and a green BRANCH lane (branch → push → pull request); both curve back and merge into a humanitarians-youtube / main node. Banner: the fellow only ever says 'submit my work' and approves." |
| B09 | `HaiSubmitDriveUpload` | "A Google Drive fidelity mock — Drive mark, search pill, 'Shared with me › HAI — Weekly Video Submissions', an Upload files button. Four 4K mp4 rows with progress bars filling at staggered rates to green ticks, a dashed drop zone, and a '4 of 4 uploaded' status bar. A terracotta DO THIS BY HAND badge, and the exact Drive URL beneath." |
| B10 | `HaiSubmitRecap` | "Two stretched columns. Left, white: CLAUDE HANDLES, seven green-ticked items, numeral 7. Right, terracotta: YOU HANDLE, three numbered items with sublines, numeral 3, closing with 'Not one of them requires a command line.'" |

## The prompt the reel hands to its viewer (B11)

```
Clone https://github.com/nikbearbrown/brutalist.art into this folder, install it,
and then ask me what my first weekly video should be about. Keep me out of the
terminal — just tell me what you need me to approve.
```
