# SOURCES — Claude, Patched.

Fresh cli-explainer build. No `cli-ideas.md`/`simulation-ideas.md` scout card
exists in `ai1-cli` — this reel instead satisfies the skill's own trigger
condition directly: "use it when the source is a thing you built." The thing
built is this session's real fix to Remotion's macOS-compatibility crash in
the `brutalist.art` toolkit itself.

## Every command and number shown on screen is a real transcript from this
session — DOUBLE-CHECK LAW / ACTUAL-CODE LAW discipline: nothing invented.

| On-screen claim | Verified against | Verdict |
|---|---|---|
| Crash: `Symbol not found: _AVCaptureDeviceTypeContinuityCamera` in `libavdevice.dylib`, "built for macOS 15.0... newer than running OS" | actual `npx remotion render` stderr, this session | OK — verbatim from real error output |
| `otool -l ... libavdevice.dylib \| grep -A3 LC_BUILD_VERSION` → `minos 15.0` (installed version, 4.0.486 at the time) | actually run this session | OK |
| This Mac is macOS 13.4 | `sw_vers` output, this session | OK |
| Version sweep: `npm pack @remotion/compositor-darwin-arm64@4.0.$v` + `otool` probe across versions 320-448 | actually run this session (probe script, `/tmp/remotion-probe/`) | OK |
| 4.0.431 through 4.0.438 → `minos 13.0`; 4.0.439 → `minos 15.0` | actual `otool` output, this session, narrowed by binary search | OK — exact boundary verified twice (coarse sweep then narrow sweep) |
| Fix: pin `remotion`/`@remotion/cli`/`@remotion/paths` to `4.0.438` in `runtime/remotion/package.json`, reinstall, renders succeed | actual `package.json` edit + `npm install` + successful test render, this session | OK |
| B01's framing ("every reel in this toolkit ends at the same Remotion render choke point") | direct consequence of `run.sh`'s pipeline (Manim → Remotion → compile), observed this session across the ai-explainer build | OK — general toolkit architecture claim, not a specific number |

## Corrections applied

None — this reel narrates a debugging session that happened directly in this
conversation; there is no external source to fact-check against or correct.

## Honesty notes

- The B00 "three RESULT lines" and B04/B07 rhetorical-pattern framing
  (branches, tracks) are dramatized PRESENTATION of the real findings above,
  not new claims — every number/quote inside them traces to the table above.
- No Manim beats: this machine doesn't have `pangocairo`/`pkg-config`
  installed, so both OUTPUT beats use registered Remotion rhetorical
  patterns (`BinaryBranch`, `DivergentFates`) instead, per the skill's
  documented Remotion-output option.
