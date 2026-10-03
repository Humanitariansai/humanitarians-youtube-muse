"""scenes.py — Manim scenes for fast-radio-bursts.

*Twenty Seconds to Decide.* — ai-explainer, claude-hai, Ep. 05.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY — never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta — the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

LAYOUT BAND PLAN (every scene obeys it — this is what keeps the gates green)
  y = +3.02   title            (chrome)
  y = +2.66   hairline         (chrome)
  y = +2.4 … -1.9   the figure
  y = -2.50   the closing line, terracotta rule at -2.78
  y = -3.20   the citation, left-anchored   (chrome)
  y = -3.12   the @HumanitariansAI wordmark bug, right-anchored (chrome, LOGO LAW)

  Manim frame is 14.222 x 8.0 units. GATE V's title-safe inset maps to
  x +-6.4, y +-3.6; everything here stays inside x +-6.15, y +-3.30.

PLOTS
  Every dynamic spectrum is SYNTHETIC, produced by assets/gen_frb.py from the
  dispersion relation. They are ink-on-white and FRAMED, so they read as figures
  in a paper — deliberately unlike Ep. 04's dark photographic plates. Scenes
  that could be mistaken for showing real data caption them.

GATE NOTES (learned the expensive way on Eps. 03 and 04)
  - `import numpy as np` explicitly: GATE A's stub does not re-export it.
  - Never build a Line from `mob.get_left()[0]`; under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set `_qc_intentional` or GATE B calls it text-on-curve.
  - Never run a stroke behind or through a label, even under an opaque chip.
  - ImageMobject is not a VMobject: group it with `Group`, never `VGroup`.
  - Do not rotate an ImageMobject; pre-bake rotations into the assets.
"""
from manim import *
import numpy as np
import glob
import os
from pathlib import Path

# ── EB Garamond, registered from the toolkit's bundled fonts ─────────────────
SERIF = None
try:
    import manimpango
    _homes = [os.environ.get("ART_HOME") or "",
              r"E:/NEU/Jobs/Humanitarians_AI/brutalist.art"]
    for _h in _homes:
        if not _h:
            continue
        for _f in glob.glob(os.path.join(_h, "runtime", "fonts", "EB_Garamond",
                                         "static", "*.ttf")):
            manimpango.register_font(_f)
    if "EB Garamond" in manimpango.list_fonts():
        SERIF = "EB Garamond"
except Exception:
    SERIF = None

HERE = Path(__file__).resolve().parent
PLOTS = HERE / "assets" / "plots"

# ── Palette ──────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
SOFT  = ManimColor("#6E6A57")
GHOST = ManimColor("#B9B4A0")
ACC   = ManimColor("#D97757")
ACCT  = ManimColor("#A44A32")
CARD  = ManimColor("#FFFFFF")
RULE  = ManimColor("#D9D4C4")

X_MAX, Y_MAX = 6.15, 3.30
TITLE_Y, HAIR_Y = 3.02, 2.66
CLOSE_Y, UNDER_Y = -2.50, -2.78
CITE_Y, BUG_Y = -3.20, -3.12


# ── Type helpers ─────────────────────────────────────────────────────────────
def _t(txt, size=26, color=None, weight=None):
    kw = {"font_size": size, "color": color if color is not None else INK}
    if SERIF:
        kw["font"] = SERIF
    if weight:
        kw["weight"] = weight
    return Text(txt, **kw)


def _fit(m, max_w, at):
    if m.width > max_w:
        m.scale(max_w / m.width)
    m.move_to(at)
    return m


def _chip(txt, size=20, fill=ACC, fg=CARD):
    label = _t(txt, size=size, color=fg)
    box = RoundedRectangle(width=label.width + 0.46, height=label.height + 0.30,
                           corner_radius=0.12, color=fill, fill_color=fill,
                           fill_opacity=1.0, stroke_width=0)
    label.move_to(box.get_center())
    return VGroup(box, label)


def _quiet_chip(txt, size=20):
    label = _t(txt, size=size, color=INK)
    box = RoundedRectangle(width=label.width + 0.46, height=label.height + 0.28,
                           corner_radius=0.12, color=GHOST, fill_color=CARD,
                           fill_opacity=1.0, stroke_width=1.6)
    label.move_to(box.get_center())
    return VGroup(box, label)


def _card(w, h, at, radius=0.16, stroke=GHOST, sw=1.8):
    return RoundedRectangle(width=w, height=h, corner_radius=radius,
                            color=stroke, stroke_width=sw,
                            fill_color=CARD, fill_opacity=1.0).move_to(at)


def _underline(m, color=ACC, sw=4, buff=0.14, pad=0.10):
    ln = Line(LEFT, RIGHT, color=color, stroke_width=sw)
    ln.set_width(max(float(m.width) + pad * 2, 0.4))
    ln.next_to(m, DOWN, buff=buff)
    return ln


def _strike(m, color=ACC, sw=4, pad=0.16):
    """Struck-through rule. `_qc_intentional` exempts it from GATE B's
    TEXT-ON-CURVE rule, which is what that hook exists for."""
    ln = Line(LEFT, RIGHT, color=color, stroke_width=sw)
    ln.set_width(max(float(m.width) + pad * 2, 0.4))
    ln.move_to(m.get_center())
    ln._qc_intentional = True
    return ln


def chrome(scene, title, cite=None):
    head = _fit(_t(title, size=36, weight="BOLD"), 11.4, [0, TITLE_Y, 0])
    hair = Line([-6.05, HAIR_Y, 0], [6.05, HAIR_Y, 0], color=RULE, stroke_width=2.4)
    bug = _t("@HumanitariansAI", size=19, color=SOFT)
    bug.move_to([0, BUG_Y, 0]).align_to([X_MAX, 0, 0], RIGHT)
    scene.play(FadeIn(head, shift=DOWN * 0.12), Create(hair), FadeIn(bug),
               run_time=0.8)
    group = VGroup(head, hair, bug)
    if cite:
        c = _t(cite, size=17, color=SOFT)
        if c.width > 8.4:
            c.scale(8.4 / c.width)
        c.move_to([0, CITE_Y, 0]).align_to([-X_MAX, 0, 0], LEFT)
        scene.play(FadeIn(c), run_time=0.4)
        group.add(c)
    return group


def closer(scene, text, cx=-0.6, size=31, max_w=8.8):
    line = _fit(_t(text, size=size, color=ACCT, weight="BOLD"), max_w,
                [cx, CLOSE_Y, 0])
    under = _underline(line, buff=0.16)
    scene.play(FadeIn(line, shift=UP * 0.10), run_time=0.75)
    scene.play(Create(under), run_time=0.4)
    return VGroup(line, under)


# ── Plot helpers ─────────────────────────────────────────────────────────────
def _plot(name, w, at, frame=True, h=None):
    """A synthetic dynamic spectrum, framed like a figure in a paper.

    Returns a `Group`: ImageMobject is not a VMobject. Falls back to a blank
    plate if the asset is missing so a scene can never fail to render.
    """
    path = PLOTS / name
    parts = []
    hh = h if h is not None else w * (2.0 / 3.0)
    try:
        img = ImageMobject(str(path))
        img.width = w
        img.move_to(at)
        hh = float(img.height)
        parts.append(img)
    except Exception:
        parts.append(Rectangle(width=w, height=hh, color=CARD, fill_color=CARD,
                               fill_opacity=1, stroke_width=0).move_to(at))
    if frame:
        parts.append(Rectangle(width=w, height=hh, color=GHOST, stroke_width=1.6,
                               fill_opacity=0).move_to(at))
    return Group(*parts)


def _tile_centre(at, plot_w, cols, rows, tile, gap, index):
    """World coords of one tile inside a contact sheet.

    B04 rings the single astronomical candidate in a 336-tile sheet. Eyeballing
    that position put the ring two tiles away from the burst, which is worse
    than no ring at all -- so it is derived from the same grid the generator
    used instead.
    """
    px_w = cols * tile + (cols - 1) * gap
    px_h = rows * tile + (rows - 1) * gap
    plot_h = plot_w * px_h / px_w
    cx_px = (index % cols) * (tile + gap) + tile / 2
    cy_px = (index // cols) * (tile + gap) + tile / 2
    x = at[0] + (cx_px / px_w - 0.5) * plot_w
    y = at[1] + (0.5 - cy_px / px_h) * plot_h
    return [x, y, 0], tile / px_w * plot_w


def _axes(at, w, h, xlab=None, ylab=None, size=17):
    """A bare frequency-time axis pair — the schematic before the data."""
    x0, y0 = at[0] - w / 2, at[1] - h / 2
    g = VGroup(Line([x0, y0, 0], [x0 + w, y0, 0], color=INK, stroke_width=2.2),
               Line([x0, y0, 0], [x0, y0 + h, 0], color=INK, stroke_width=2.2))
    labs = VGroup()
    if xlab:
        labs.add(_t(xlab, size=size, color=SOFT).move_to([at[0], y0 - 0.30, 0]))
    if ylab:
        r = _t(ylab, size=size, color=SOFT).rotate(PI / 2)
        r.move_to([x0 - 0.32, at[1], 0])
        labs.add(r)
    return g, labs


def _sweep(at, w, h, dm_frac=1.0, color=ACC, sw=4.5, n=46):
    """A dispersion curve drawn inside a box: arrival time goes as nu^-2, so the
    low-frequency end (bottom) lags. dm_frac scales how far it reaches."""
    x0, y0 = at[0] - w / 2, at[1] - h / 2
    pts = []
    for i in range(n):
        u = i / (n - 1)                      # 0 at top (high nu) to 1 at bottom
        nu = 1.0 - 0.5 * u                   # 1.0 down to 0.5, arbitrary units
        t = (nu ** -2 - 1.0) / 3.0           # 0 at top, 1 at the bottom
        pts.append([x0 + w * min(t * dm_frac, 1.0), y0 + h * (1.0 - u), 0])
    return VMobject().set_points_as_corners(pts).set_stroke(color, sw)


def _ring(at, r, seg=54, head=0.0, color=INK, sw=3.2):
    """The buffer, as a ring with a write head."""
    circle = Circle(radius=r, color=color, stroke_width=sw).move_to(at)
    ang = TAU * head - PI / 2
    dot = Dot([at[0] + r * math_cos(ang), at[1] + r * math_sin(ang), 0],
              radius=0.11, color=ACC)
    return circle, dot


def math_cos(a):
    return float(np.cos(a))


def math_sin(a):
    return float(np.sin(a))


def _net(at, layers=(4, 3, 2), dx=0.62, dy=0.30, r=0.072):
    """A small layered-network glyph."""
    g = VGroup()
    for i, cnt in enumerate(layers):
        for j in range(cnt):
            g.add(Dot([at[0] + (i - (len(layers) - 1) / 2) * dx,
                       at[1] + (j - (cnt - 1) / 2) * dy, 0],
                      radius=r, color=INK))
    return g


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER  (12.50 s)
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "AI in Astronomy & Space Science  ·  Ep. 05",
               cite="brutalist.art  ·  ai-explainer  ·  Pragmatist register")

        name = _t("Om Mali", size=98, weight="BOLD").move_to([-3.15, 1.15, 0])
        self.play(Write(name), run_time=1.1)
        hair = _underline(name, sw=7, buff=0.22, pad=0.12)
        self.play(Create(hair), run_time=0.6)

        role = _t("Humanitarians AI  ·  presenter", size=29, color=SOFT)
        role.move_to([-3.15, -0.24, 0])
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        sub = _fit(_t("the one method you cannot re-run", size=26, color=SOFT),
                   5.5, [-3.15, -1.02, 0])
        self.play(FadeIn(sub), run_time=0.5)

        panel = _card(5.5, 3.5, [3.15, 0.45, 0])
        self.play(Create(panel), run_time=0.7)

        r1 = _t("every other method", size=28).move_to([3.15, 1.56, 0])
        r1b = _t("re-run it on stored data", size=22, color=SOFT)
        r1b.move_to([3.15, 1.10, 0])
        loop = Arc(radius=0.30, start_angle=-PI * 0.75, angle=TAU * 0.78,
                   color=INK, stroke_width=3.2).move_to([3.15, 0.52, 0])
        self.play(FadeIn(r1), FadeIn(r1b), run_time=0.5)
        self.play(Create(loop), run_time=0.45)
        s = _strike(loop, pad=0.06)
        self.play(Create(s), run_time=0.4)

        div = Line([1.05, 0.12, 0], [5.25, 0.12, 0], color=RULE, stroke_width=2)
        self.play(Create(div), run_time=0.3)

        r2 = _t("this one", size=30, color=ACCT, weight="BOLD")
        r2.move_to([3.15, -0.32, 0])
        r2b = _t("decide now, or lose it", size=24, color=ACCT)
        r2b.move_to([3.15, -0.82, 0])
        arrow = Arrow([2.05, -1.32, 0], [4.25, -1.32, 0], color=ACC,
                      stroke_width=4, buff=0.02, tip_length=0.20)
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.4)
        self.play(GrowArrow(arrow), run_time=0.45)

        closer(self, "Ep. 05  ·  the decision that cannot be taken back.",
               cx=-0.4, size=28, max_w=8.6)
        self.wait(2.6)


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — EXECUTIVE SUMMARY  (18.65 s)
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="synthetic dynamic spectrum, generated for this episode")

        # One plot only. An earlier cut also stacked the 60-tile candidate sheet
        # here and it collided with three labels and the closing line -- and the
        # sheet is B04's job anyway. The BLUF beat stays simple on purpose.
        one = _plot("burst_dm500_big.png", 4.55, [-3.70, 0.86, 0])
        self.play(FadeIn(one), run_time=0.8)
        ol = _fit(_t("one candidate, and it sweeps", size=21, color=SOFT),
                  4.6, [-3.70, -1.02, 0])
        self.play(FadeIn(ol), run_time=0.4)

        lines = [
            _t("Space gives it a shape.", size=33),
            _t("Almost every candidate is us.", size=33),
            _t("A network sorts them live.", size=33),
        ]
        for ln, y in zip(lines, [1.90, 0.85, -0.20]):
            _fit(ln, 6.0, [2.85, y, 0])
            self.play(FadeIn(ln, shift=RIGHT * 0.18), run_time=0.55)

        last = _fit(_t("It keeps a few. It deletes the rest.", size=30,
                       color=ACCT), 6.0, [2.85, -1.28, 0])
        self.play(FadeIn(last, shift=UP * 0.10), run_time=0.6)

        closer(self, "Deleted, not archived.", cx=0.0, size=34)
        self.wait(9.0)


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE SIGNATURE  (17.11 s)
# ═════════════════════════════════════════════════════════════════════════════
class B03_Signature(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What space does to a burst",
               cite="delay goes as frequency to the minus two · dispersion measure sets the slope · synthetic")

        # The hero panel carries the whole source-to-arrival idea by itself: a
        # vertical line (all frequencies at once) TRANSFORMS into the sweep. An
        # earlier cut drew that as a separate schematic box plus a stacked trio,
        # and the trio (3:2 plots, 2.33 units tall each) ran over the title and
        # over itself.
        hero_at, hw = [-3.30, 0.80, 0], 4.90
        hero = _plot("burst_dm500_big.png", hw, hero_at)
        self.play(FadeIn(hero), run_time=0.7)

        hh = 4.90 * 384.0 / 512.0            # the _big asset is 512x384
        flat = Line([hero_at[0] - hw / 2 + 0.42, hero_at[1] - hh / 2 + 0.10, 0],
                    [hero_at[0] - hw / 2 + 0.42, hero_at[1] + hh / 2 - 0.10, 0],
                    color=ACC, stroke_width=5)
        self.play(Create(flat), run_time=0.6)
        c1 = _fit(_t("at the source: every frequency at once", size=21, color=SOFT),
                  5.0, [-3.30, -1.44, 0])
        self.play(FadeIn(c1), run_time=0.4)

        curve = _sweep(hero_at, hw - 0.80, hh - 0.20, dm_frac=0.95, sw=5)
        self.play(Transform(flat, curve), run_time=1.2)
        c2 = _fit(_t("on arrival: a curve", size=23, color=ACCT),
                  5.0, [-3.30, -1.94, 0])
        self.play(FadeIn(c2), run_time=0.4)

        # the trio, small, on ONE shared time axis so the slopes differ
        trio, labels = Group(), VGroup()
        for i, (fn, dm) in enumerate((("burst_dm200.png", "DM 200"),
                                      ("burst_dm500_trio.png", "DM 500"),
                                      ("burst_dm900.png", "DM 900"))):
            cy = 1.78 - i * 1.50
            trio.add(_plot(fn, 2.28, [4.35, cy, 0]))
            labels.add(_t(dm, size=19, color=SOFT).move_to([2.20, cy, 0]))
        for tp, lb in zip(trio, labels):
            self.play(FadeIn(tp), FadeIn(lb), run_time=0.42)
        tl = _fit(_t("one shared time axis", size=19, color=SOFT),
                  3.0, [4.35, -2.36, 0])
        self.play(FadeIn(tl), run_time=0.35)

        closer(self, "The steeper the curve, the more space it crossed.",
               cx=-2.10, size=28, max_w=7.6)
        self.wait(2.2)


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE HAYSTACK  (15.30 s)
# ═════════════════════════════════════════════════════════════════════════════
class B04_Haystack(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The haystack",
               cite="1.5 PB/day, 10^11 S/N values per second, ~10^5 candidates per day: CHIME/FRB RFI paper (2023) · synthetic tiles")

        sheet = _plot("sheet_24x14.png", 6.1, [-2.95, 0.70, 0])
        self.play(FadeIn(sheet), run_time=0.9)

        rows = [("1.5 PB", "of data, every day", 1.90),
                ("10 to the 11", "signal-to-noise values a second", 0.62),
                ("100,000", "candidates a day", -0.66)]
        for i, (big, sub, y) in enumerate(rows):
            col = ACCT if i == 2 else INK
            b = _t(big, size=52 if i != 1 else 40, color=col, weight="BOLD")
            b.move_to([3.75, y, 0])
            s = _fit(_t(sub, size=21, color=SOFT), 4.4, [3.75, y - 0.62, 0])
            self.play(Write(b), run_time=0.6)
            self.play(FadeIn(s), run_time=0.35)
            if i < 2:
                self.play(Create(Line([1.60, y - 0.94, 0], [5.95, y - 0.94, 0],
                                      color=RULE, stroke_width=2)), run_time=0.25)

        # sheet_24x14.png: 24x14 tiles of 40 px, 3 px gaps, burst at index 201.
        # Eyeballing this put the ring two tiles off the burst, which is worse
        # than no ring at all, so it is derived from the generator's own grid.
        at, tw = _tile_centre([-2.95, 0.70, 0], 6.1, 24, 14, 40, 3, 201)
        ring = Ellipse(width=tw * 2.4, height=tw * 2.4, color=ACC, stroke_width=3.6)
        ring.move_to(at)
        self.play(Create(ring), run_time=0.5)
        rl = _t("one of these is from space", size=21, color=ACCT)
        _fit(rl, 4.4, [-2.95, -1.62, 0])
        self.play(FadeIn(rl), run_time=0.4)

        closer(self, "Almost none of them are astronomical.", cx=-0.4, size=31)
        self.wait(2.2)


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE IMPOSTORS  (19.69 s)
# ═════════════════════════════════════════════════════════════════════════════
IMPOSTORS = [
    ("rfi_zero_dm.png", "ZERO DISPERSION", "every frequency at once"),
    ("rfi_narrowband.png", "NARROWBAND", "a transmitter, always on"),
    ("rfi_patch.png", "PATCHY", "bursty, band-limited, no sweep"),
]
IMP_X = [-4.05, 0.0, 4.05]


class B05_Impostors(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Most of it is us",
               cite="perytons traced to observatory microwave ovens: Petroff et al. 2015 · synthetic spectra")

        plots = Group()
        for (fn, lab, sub), cx in zip(IMPOSTORS, IMP_X):
            p = _plot(fn, 3.50, [cx, 1.02, 0])
            l = _t(lab, size=24, weight="BOLD").move_to([cx, -0.52, 0])
            s = _fit(_t(sub, size=19, color=SOFT), 3.6, [cx, -0.98, 0])
            plots.add(p)
            self.play(FadeIn(p, scale=1.03), run_time=0.42)
            self.play(FadeIn(l), FadeIn(s), run_time=0.34)

        # The curve is drawn ON plot 1 deliberately, but its LABEL goes above
        # the frame rather than floating over the data.
        want = _sweep([IMP_X[0], 1.02, 0], 3.1, 2.1, dm_frac=0.95, sw=3.6)
        wl = _t("the shape it wants", size=19, color=ACCT)
        wl.move_to([-4.05, 2.44, 0])
        self.play(Create(want), run_time=0.7)
        self.play(FadeIn(wl), run_time=0.35)

        note = _card(9.6, 0.92, [0.0, -1.76, 0])
        nt = _fit(_t("PARKES  ·  the peryton was the staff microwave oven, opened before its timer finished",
                     size=22), 9.2, [0.0, -1.76, 0])
        self.play(Create(note), run_time=0.5)
        self.play(FadeIn(nt), run_time=0.55)

        closer(self, "The false positives are man-made.", cx=-0.4, size=31)
        self.wait(4.2)


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THE FRAMEWORK  (22.12 s)
# ═════════════════════════════════════════════════════════════════════════════
STATIONS = [("1", "BUFFER"), ("2", "DEDISPERSE"), ("3", "CANDIDATE"),
            ("4", "CLASSIFY"), ("5", "KEEP")]
ST_X = [-4.85, -2.43, 0.0, 2.43, 4.85]


class B06_Framework(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The loop, and the clock",
               cite="35.5 s ring buffer, ~100 ms dumped on trigger: CHIME/FRB baseband pipeline (2021)")

        boxes = []
        for (num, name), cx in zip(STATIONS, ST_X):
            box = _card(2.24, 2.70, [cx, 0.92, 0])
            boxes.append(box)
            self.play(FadeIn(box), run_time=0.24)
        heads = VGroup()
        for (num, name), cx in zip(STATIONS, ST_X):
            disc = Circle(radius=0.21, color=ACC, fill_color=ACC,
                          fill_opacity=1.0, stroke_width=0)
            disc.move_to([cx - 0.78, 1.90, 0])
            n = _t(num, size=19, color=CARD).move_to(disc.get_center())
            ttl = _fit(_t(name, size=20, weight="BOLD"), 1.30, [cx + 0.30, 1.90, 0])
            heads.add(VGroup(disc, n, ttl))

        # station 1 — the ring buffer, with its write head
        ring, headdot = _ring([ST_X[0], 0.90, 0], 0.50, head=0.18)
        rlab = _t("35.5 s", size=18, color=ACCT).move_to([ST_X[0], -0.12, 0])
        # station 2 — a fan of trial dedispersion curves
        fan = VGroup()
        for k, f in enumerate((0.35, 0.6, 0.85, 1.0)):
            col = ACC if k == 3 else GHOST
            fan.add(_sweep([ST_X[1], 0.90, 0], 1.70, 1.34, dm_frac=f,
                           color=col, sw=2.6, n=26))
        flab = _t("trial delays", size=18, color=SOFT).move_to([ST_X[1], -0.12, 0])
        # station 3 — the candidate becomes two pictures
        # Side by side, not stacked: two 3:2 plots stacked are 2.14 units tall
        # and the card interior is only about 1.9.
        two = Group(_plot("burst_dm500.png", 0.96, [ST_X[2] - 0.52, 0.90, 0]),
                    _plot("dmtime_burst.png", 0.96, [ST_X[2] + 0.52, 0.90, 0]))
        tlab = _t("two pictures", size=18, color=SOFT).move_to([ST_X[2], -0.12, 0])
        # station 4 — the network
        net = _net([ST_X[3], 0.90, 0], layers=(4, 3, 2), dx=0.50, dy=0.26)
        nlab = _t("a network judges", size=18, color=SOFT).move_to([ST_X[3], -0.12, 0])
        # station 5 — the write
        slab = _chip("100 ms to disk", size=18).move_to([ST_X[4], 1.02, 0])
        s2 = _t("on a yes", size=18, color=SOFT).move_to([ST_X[4], -0.12, 0])

        glyphs = [Group(ring, headdot, rlab), VGroup(fan, flab),
                  Group(two, tlab), VGroup(net, nlab), VGroup(slab, s2)]
        for i in range(5):
            self.play(FadeIn(heads[i]), run_time=0.26)
            self.play(FadeIn(glyphs[i]), run_time=0.44)
            if i < 4:
                a = Arrow([ST_X[i] + 1.14, 0.92, 0], [ST_X[i + 1] - 1.14, 0.92, 0],
                          color=INK, stroke_width=2.6, buff=0.02, tip_length=0.14)
                self.play(GrowArrow(a), run_time=0.22)

        arc = ArcBetweenPoints([ST_X[4], -0.56, 0], [ST_X[0], -0.56, 0],
                               angle=-TAU / 11, color=GHOST, stroke_width=4)
        tip = Triangle(color=GHOST, fill_color=GHOST, fill_opacity=1, stroke_width=0)
        tip.scale(0.12).rotate(PI / 2).move_to([ST_X[0] + 0.06, -0.56, 0])
        self.play(Create(arc), run_time=0.8)
        self.play(FadeIn(tip), run_time=0.2)
        acap = _fit(_t("on a no, the buffer overwrites", size=22, color=INK),
                    6.0, [0.0, -1.72, 0])
        self.play(FadeIn(acap), run_time=0.5)

        closer(self, "The clock is part of the method.", cx=-0.4, size=30)
        self.wait(3.0)


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — WORKED EXAMPLE  (16.66 s)
# ═════════════════════════════════════════════════════════════════════════════
class B07_TwoPictures(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Two pictures per candidate",
               cite="frequency-time and DM-time images as CNN inputs: Agarwal et al. 2020 · synthetic spectra")

        rail_x = [-5.30, -2.65, 0.0, 2.65, 5.30]
        segs = VGroup(*[Line([a, 2.32, 0], [b, 2.32, 0], color=RULE, stroke_width=2)
                        for a, b in ((-6.00, -5.90), (-4.70, -3.25),
                                     (-1.85, -0.85), (0.85, 1.90), (3.55, 4.55))])
        self.play(Create(segs), run_time=0.3)
        rail = VGroup(*[_quiet_chip(n, size=17).move_to([cx, 2.32, 0])
                        for n, cx in zip(("BUFFER", "DEDISP", "CAND", "CLASSIFY", "KEEP"),
                                         rail_x)])
        self.play(LaggedStart(*[FadeIn(c) for c in rail], lag_ratio=0.1),
                  run_time=0.7)

        # top row: a real burst
        a1 = _plot("burst_dm500.png", 2.80, [-4.45, 1.15, 0])
        a2 = _plot("dmtime_burst.png", 2.80, [-1.30, 1.15, 0])
        self.play(FadeIn(a1), run_time=0.45)
        self.play(FadeIn(a2), run_time=0.45)
        al1 = _t("it sweeps", size=19, color=SOFT).move_to([-4.45, -0.20, 0])
        al2 = _t("and it focuses", size=19, color=ACCT).move_to([-1.30, -0.20, 0])
        self.play(FadeIn(al1), FadeIn(al2), run_time=0.35)
        v1 = _chip("BURST", size=21).move_to([4.80, 1.15, 0])

        # bottom row: an impostor
        b1 = _plot("rfi_zero_dm.png", 2.80, [-4.45, -1.42, 0])
        b2 = _plot("dmtime_rfi.png", 2.80, [-1.30, -1.42, 0])
        self.play(FadeIn(b1), run_time=0.45)
        self.play(FadeIn(b2), run_time=0.45)
        bl1 = _t("no sweep", size=19, color=SOFT).move_to([-4.45, -2.78, 0])
        bl2 = _t("never closes", size=19, color=SOFT).move_to([-1.30, -2.78, 0])
        self.play(FadeIn(bl1), FadeIn(bl2), run_time=0.35)
        v2 = _quiet_chip("REJECT", size=21).move_to([4.80, -1.42, 0])

        net = _net([2.35, -0.14, 0], layers=(3, 2), dx=0.52, dy=0.30)
        self.play(FadeIn(net), run_time=0.4)
        f1 = Arrow([0.25, 1.15, 0], [1.85, 0.12, 0], color=GHOST,
                   stroke_width=2.4, buff=0.06, tip_length=0.14)
        f2 = Arrow([0.25, -1.42, 0], [1.85, -0.40, 0], color=GHOST,
                   stroke_width=2.4, buff=0.06, tip_length=0.14)
        self.play(GrowArrow(f1), GrowArrow(f2), run_time=0.45)
        self.play(FadeIn(v1, scale=1.08), run_time=0.4)
        self.play(FadeIn(v2), run_time=0.35)
        self.wait(1.4)


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — THE DESIGN TELL  (18.50 s)
# ═════════════════════════════════════════════════════════════════════════════
class B08_FakeReal(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Fake positives, real negatives",
               cite="trained on simulated FRBs and real recorded RFI: Agarwal et al. 2020 (FETCH)")

        left = _card(5.55, 3.90, [-3.20, 0.62, 0])
        right = _card(5.55, 3.90, [3.20, 0.62, 0])
        self.play(Create(left), Create(right), run_time=0.6)
        h1 = _t("SIMULATED", size=25, weight="BOLD").move_to([-3.20, 2.22, 0])
        h2 = _t("RECORDED", size=25, weight="BOLD").move_to([3.20, 2.22, 0])
        s1 = _t("the positives", size=20, color=SOFT).move_to([-3.20, 1.76, 0])
        s2 = _t("the negatives", size=20, color=SOFT).move_to([3.20, 1.76, 0])
        self.play(FadeIn(h1), FadeIn(s1), FadeIn(h2), FadeIn(s2), run_time=0.45)

        gen = _sweep([-4.35, 0.52, 0], 1.70, 1.60, dm_frac=0.95, sw=3.4)
        gl = _t("a shape you generate", size=18, color=SOFT)
        gl.move_to([-4.35, -0.56, 0])
        self.play(Create(gen), run_time=0.6)
        self.play(FadeIn(gl), run_time=0.3)
        plus = _t("+", size=34, color=SOFT).move_to([-3.16, 0.52, 0])
        noisy = _plot("burst_dm500.png", 2.10, [-1.90, 0.52, 0])
        nl = _t("into real noise", size=18, color=SOFT).move_to([-1.90, -0.56, 0])
        self.play(FadeIn(plus), run_time=0.2)
        self.play(FadeIn(noisy), FadeIn(nl), run_time=0.5)

        negs = Group()
        for i, fn in enumerate(("rfi_zero_dm.png", "rfi_narrowband.png",
                                "rfi_patch.png")):
            negs.add(_plot(fn, 1.66, [1.52 + i * 1.72, 0.52, 0]))
        for n in negs:
            self.play(FadeIn(n), run_time=0.32)
        ngl = _t("recorded at the dish", size=18, color=SOFT)
        ngl.move_to([3.20, -0.56, 0])
        self.play(FadeIn(ngl), run_time=0.3)

        block = _card(3.30, 0.86, [0.0, -1.42, 0])
        bl = _t("one training set", size=22, weight="BOLD").move_to([0.0, -1.42, 0])
        self.play(Create(block), FadeIn(bl), run_time=0.5)
        ring = RoundedRectangle(width=3.46, height=1.02, corner_radius=0.16,
                                color=ACC, stroke_width=3.2, fill_opacity=0)
        ring.move_to([0.0, -1.42, 0])
        a1 = Arrow([-3.20, -1.02, 0], [-1.85, -1.30, 0], color=GHOST,
                   stroke_width=2.4, buff=0.06, tip_length=0.14)
        a2 = Arrow([3.20, -1.02, 0], [1.85, -1.30, 0], color=GHOST,
                   stroke_width=2.4, buff=0.06, tip_length=0.14)
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.4)
        self.play(Create(ring), run_time=0.5)

        l1 = _fit(_t("the fakes teach it what to want", size=21, color=INK),
                  4.6, [-3.20, -2.06, 0])
        l2 = _fit(_t("the real ones teach it what to refuse", size=21, color=ACCT),
                  4.9, [3.20, -2.06, 0])
        self.play(FadeIn(l1), run_time=0.4)
        self.play(FadeIn(l2), run_time=0.4)
        self.wait(3.4)


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — THE RESULT  (15.81 s)
# ═════════════════════════════════════════════════════════════════════════════
class B09_Result(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What it actually delivers",
               cite=">99.5% recall on test data: Agarwal et al. 2020 · false-positive reduction: CHIME/FRB (2023) · 536 bursts: Catalog 1 (2021)")

        ring_bg = Circle(radius=1.10, color=GHOST, stroke_width=13)
        ring_bg.move_to([-4.60, 1.16, 0])
        self.play(Create(ring_bg), run_time=0.4)
        arc = Arc(radius=1.10, start_angle=PI / 2, angle=-TAU * 0.995,
                  color=ACC, stroke_width=13).move_to(ring_bg.get_center())
        self.play(Create(arc), run_time=1.0)
        pct = _t("99.5%", size=46, color=ACCT, weight="BOLD")
        pct.move_to([-4.60, 1.22, 0])
        self.play(FadeIn(pct, scale=1.08), run_time=0.45)
        pl = _fit(_t("recall, on held-out test data", size=19, color=SOFT),
                  3.3, [-4.60, -0.24, 0])
        self.play(FadeIn(pl), run_time=0.35)

        # the funnel: 100,000 a day down to a handful
        top = 2.05
        widths = [(4.10, "~100,000 a day"), (2.60, "after RFI cuts"),
                  (0.85, "a few a day")]
        prev_w = None
        for i, (w, lab) in enumerate(widths):
            y = top - i * 1.10
            col = ACC if i == 2 else INK
            bar = Rectangle(width=w, height=0.42, color=col, fill_color=col,
                            fill_opacity=0.30 if i < 2 else 0.85, stroke_width=1.4)
            bar.move_to([-0.55, y, 0])
            lb = _t(lab, size=19, color=ACCT if i == 2 else SOFT)
            lb.move_to([-0.55, y - 0.46, 0])
            self.play(GrowFromCenter(bar), run_time=0.42)
            self.play(FadeIn(lb), run_time=0.3)

        cnt = _t("536", size=58, color=ACCT, weight="BOLD")
        cnt.move_to([4.35, 1.62, 0])
        self.play(Write(cnt), run_time=0.7)
        cl = _fit(_t("bursts in the first catalogue", size=20, color=SOFT),
                  3.5, [4.35, 0.98, 0])
        self.play(FadeIn(cl), run_time=0.3)
        div = Line([2.55, 0.60, 0], [6.05, 0.60, 0], color=RULE, stroke_width=2)
        self.play(Create(div), run_time=0.25)
        r1 = _t("62 repeats", size=26, weight="BOLD").move_to([4.35, 0.20, 0])
        r2 = _t("from 18 sources", size=20, color=SOFT).move_to([4.35, -0.30, 0])
        self.play(FadeIn(r1), run_time=0.35)
        self.play(FadeIn(r2), run_time=0.3)

        closer(self, "A handful a day, out of a hundred thousand.",
               cx=-0.4, size=30)
        self.wait(1.6)


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — WHERE IT FAILS  (19.84 s)
# ═════════════════════════════════════════════════════════════════════════════
class B10_TwoLimits(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Two limits",
               cite="both panels are this episode's own inference from the training design and the buffer, not published results")

        left = _card(5.75, 4.05, [-3.10, 0.42, 0])
        right = _card(5.75, 4.05, [3.10, 0.42, 0])
        self.play(Create(left), Create(right), run_time=0.6)
        h1 = _fit(_t("It finds what was simulated", size=25, weight="BOLD"),
                  5.4, [-3.10, 2.02, 0])
        h2 = _t("It cannot be re-run", size=25, weight="BOLD")
        h2.move_to([3.10, 2.02, 0])
        self.play(FadeIn(h1), FadeIn(h2), run_time=0.4)

        # LEFT: a boundary around the simulated shapes, one burst outside it
        rng = np.random.RandomState(7)
        cloud = VGroup()
        for _ in range(26):
            x = -3.55 + rng.normal(0, 0.62)
            y = 0.86 + rng.normal(0, 0.42)
            cloud.add(Dot([x, y, 0], radius=0.055, color=INK, fill_opacity=0.7))
        self.play(LaggedStart(*[FadeIn(d) for d in cloud], lag_ratio=0.03),
                  run_time=0.7)
        bound = Ellipse(width=2.90, height=1.86, color=INK, stroke_width=2.4)
        bound.move_to([-3.55, 0.86, 0])
        self.play(Create(bound), run_time=0.6)
        bl = _fit(_t("what somebody thought to simulate", size=19, color=SOFT),
                  4.9, [-3.10, -0.32, 0])
        self.play(FadeIn(bl), run_time=0.35)
        odd = _plot("burst_scattered.png", 1.55, [-1.12, 0.86, 0])
        self.play(FadeIn(odd), run_time=0.45)
        ol = _fit(_t("a shape nobody simulated, unflagged", size=19, color=ACCT),
                  5.0, [-3.10, -1.08, 0])
        self.play(FadeIn(ol), run_time=0.4)

        # RIGHT: the buffer overwrites the rejection
        ring, headdot = _ring([1.95, 0.98, 0], 0.66, head=0.30)
        self.play(Create(ring), FadeIn(headdot), run_time=0.55)
        rej = _plot("rfi_zero_dm.png", 1.40, [4.20, 0.98, 0])
        self.play(FadeIn(rej), run_time=0.4)
        arrow = Arrow([2.72, 0.98, 0], [3.42, 0.98, 0], color=GHOST,
                      stroke_width=2.6, buff=0.04, tip_length=0.14)
        self.play(GrowArrow(arrow), run_time=0.3)
        x = VGroup(Line([3.98, 1.22, 0], [4.42, 0.74, 0], color=ACC, stroke_width=4.4),
                   Line([3.98, 0.74, 0], [4.42, 1.22, 0], color=ACC, stroke_width=4.4))
        self.play(Create(x), run_time=0.4)
        oneway = Arrow([1.55, -0.22, 0], [4.65, -0.22, 0], color=ACC,
                       stroke_width=4, buff=0.02, tip_length=0.20)
        owl = _t("NO RE-RUN", size=22, color=ACCT, weight="BOLD")
        owl.move_to([3.10, -0.74, 0])
        self.play(GrowArrow(oneway), run_time=0.5)
        self.play(FadeIn(owl), run_time=0.35)
        rl = _fit(_t("the rejection is overwritten, not archived", size=19,
                     color=SOFT), 5.3, [3.10, -1.24, 0])
        self.play(FadeIn(rl), run_time=0.4)

        closer(self, "A miss here can never be audited.", cx=-0.4, size=31)
        self.wait(2.4)
