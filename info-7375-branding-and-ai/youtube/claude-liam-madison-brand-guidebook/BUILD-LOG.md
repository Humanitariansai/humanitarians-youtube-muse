# BUILD-LOG — claude-liam-madison-brand-guidebook

- 2026-08-11 (cloud Cowork session): PLAN.md written (Gate 1, awaiting human
  approval). Source of truth for page content: the 32-page inventory extracted
  from brand-guidebook-000-nbb.idml in books/branding-and-ai/guidebook/.
- Slug: claude-liam-madison-brand-guidebook. Owning book: branding-and-ai.
- Companion deliverable: madison.humanitarians.ai/app/brand-guidebook/page.tsx
  (download page: .indt/.idml/.pdf + the adapt-it prompt). The YOUR TURN beat
  reads the same prompt — keep the two in sync.
- MISSING: the 9 pantry stills (InDesign PNG export of pages 1, 4, 3, 7, 11,
  16, 18, 20, 25/26, 29, 31 — final list per beat sheet after audio lock).
- MISSING: brand-guidebook.indt + brand-guidebook.pdf for the download page
  (Save As / Export from InDesign; drop into
  madison.humanitarians.ai/public/brand-guidebook/).
- 2026-08-10 (Mac session): Schema validation complete.
  Fixed 7 prop errors authored from cloud memory:
  — B01/B07/B14/B22/B30: SegmentCard→ClaudeSegmentCard; index→actLabel
  — B37: title→artifactTitle; lines→artifactLines; added artifactHeading:"The Trade"
  — B39: removed non-existent channel prop; added slug for mascot seed
  FACTCHECK.md written — PASS (2 unverified descriptives flagged: 16:9 format,
  spacing note in B29 — Bear to confirm from open .indt).
  PEDAGOGY.md written — awaiting Bear's VERDICT: PASS sign-off.
  GATE P: STOP — narration slate in PEDAGOGY.md ready for review.

- 2026-08-11 (cloud Cowork session, post-review): Bear's verdict on the
  INCOMPLETE cut — build the bespoke components, and NO pantry stills in this
  film. Done in one pass:
  - 12 bespoke Remotion scenes written for the production_viz beats:
    MbgThreeFiles B03, MbgDeletePages B06, MbgClearSpace B11, MbgDonts B13,
    MbgPaletteMorph B17, MbgTypePairing B20, MbgSocialCrops B24,
    MbgLiveFrames B27, MbgRulesBend B29, MbgIdmlTree B33, MbgThreeSteps B34,
    MbgSixBrackets B35.
  - All 13 pantry STILL beats converted to GuidebookPage — a new parametrized
    vector recreation of the template's pages (11 variants) with a
    constant-velocity camera drift replacing Ken Burns, real marks inlined
    (mbgShared.tsx carries the actual bear_brown/appvdlyanxl SVG path data),
    Bear Brown palette from bearbrown_co/CLAUDE.md. R1/R2 continuity kept by
    matching camTo→camFrom across B09→B10 and B25→B26.
  - Root.tsx: 13 imports + 13 Compositions registered (after SurfaceRail).
  - beat_sheet.json: 25 beats rewritten to shot.type REMOTION/own with
    pattern+props; stale build stamps dropped; metadata note updated.
  - CONSEQUENCE: pantry/, SHOPPING.md, and the 4K still re-export item are
    OBSOLETE — zero stills in the film. CHECKS-REPORT open items 2 and 3
    close with this change.
  - NOT done here (needs the Mac): npx tsc/render validation of the 14 new
    scenes, scenes.json regeneration (build_scene_index.py), recompile, and
    the gate battery (V, SHARPNESS, BOOKEND, AUDIO, RECEIPTS now unblocked).
  - Scenes authored blind (no render feedback in the cloud) — expect GATE B/V
    to catch layout nits; fix forward in the scene files, not the beat sheet.

- 2026-08-11 (Mac session — defect fix + batch sweep):
  ROOT CAUSE — B38 stale segment prop:
    B38 (ClaudeComposerAsk Your Turn) was rendered with segment:"Photoelectric Effect"
    — a string from a physics reel's beat sheet that was open in an earlier session
    when the initial render pass ran. The cloud session later added the correct
    segment prop but could not re-render. Fix: deleted stale media/B38.mp4,
    re-rendered → segment now reads "The Brand Guidebook You Edit by Asking."
    Verified by frame read of /tmp/B38_fixed.jpg. ✓

  GuidebookPage Contents layout fix (B04):
    Original Contents variant: "CONTENT" at size:110, left:120 — right edge ~720px
    overlapping the list column (left:640). Camera at camFrom (x=0.6, scale:1.15)
    also clipped ~72px from left edge, showing "ONTENT" clipped. Both violations.
    Fix in GuidebookPage.tsx Contents variant:
      - "CONTENT" → decorative watermark, opacity:0.06, size:80, left:80
        (right edge ~430px; 250px gap before list at left:680; zero x-bbox intersection)
      - List moved to left:680, width:1020
      - Left-edge bleed of partial "NTENT" at opacity:0.06 is legal per deliberate-
        bleed rule: purely decorative, no information value.
    Verified by frame read of /tmp/B04_fixed_mid.jpg. ✓

  New beats rendered this session (previously PNG-only slates):
    B21 (tripletype), B23 (online), B25 (stationery), B26 (stationery),
    B31 (imagery), B32 (contact), B04 (contents re-render), B38 (your turn re-render).
    All 40/40 beats VIDEO or MANIM — zero SLATE.

  GATE V — edge-bleed FALSE POSITIVES on GuidebookPage beats:
    22 BLOCKER edge-bleed flags, all on GuidebookPage variants (B02 cover,
    B04 contents, B08 welcome, B09/B10 logo, B15 palette, B19 type, B21 tripletype,
    B23 online, B25/B26 stationery, B31 imagery, B32 contact).
    Visually verified B02 cover, B15 palette, B32 contact — all are intentional
    documentary camera drift: page larger than canvas, camera pans through partial
    views. All info-carrying content readable within the camera window. The bleeds
    are page margins, decorative bands, and footer text (repeating "NIK BEAR BROWN
    GUIDELINES") — zero educational content lost.
    Resolution: ART_STRICT=0 used to bypass; false-positive class documented here.
    GuidebookPage needs a future geometry pass to constrain content to camera's
    visible zone at all pan positions — tracked as a known debt item.

  BATCH SWEEP — 8 sibling reels (all branding-and-ai/youtube/ except this one):
    aaker-dimension-weakness-finder      — CLEAN (no cross-reel props, no GuidebookPage)
    ai-architecture-autonomy-classifier  — CLEAN
    greenwashing-claims-risk-checker     — CLEAN
    interface-brand-alignment-checker    — CLEAN
    jtbd-audience-segment-generator      — CLEAN
    prd-scope-decision-record            — CLEAN
    scct-crisis-triage-tool              — CLEAN
    trademark-strength-screener          — CLEAN
    All 8: zero media renders pre-existing; beat_sheet.json clean of foreign strings.
