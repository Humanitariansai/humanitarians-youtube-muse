"""scenes.py — Manim scenes for claude-hai-gravitational-wave-detection.

*Knowing the Noise by Name.* — ai-explainer, claude-hai channel.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY — never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta — the ONE accent, as a MARK: rule, spike, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream).
                  Terracotta #D97757 as text on cream is 2.74:1 and fails WCAG
                  even at large sizes, so the brand accent stays a mark and the
                  documented `warn` token carries any word that must read hot.

LAYOUT BAND PLAN (every scene obeys it — this is what keeps the gates green)
  y = +3.02   title            (chrome)
  y = +2.66   hairline         (chrome)
  y = +2.4 … -1.9   the figure
  y = -2.50   the closing line, with its terracotta underline at -2.78
  y = -3.20   the citation, left-anchored   (chrome)
  y = -3.12   the @HumanitariansAI wordmark bug, right-anchored (chrome, LOGO LAW)

  Manim frame is 14.222 x 8.0 units. GATE V's title-safe inset maps to
  x +-6.4, y +-3.6; everything here stays inside x +-6.15, y +-3.30, and the
  title/cite pair guarantees the content bbox spans the safe area so the
  canvas-fill floor is met.

RULES OBSERVED
  - No MathTex / no LaTeX (this machine has no dvisvgm).
  - No slant=ITALIC on multi-word Text (Pango collapses the spaces).
  - Numbers appear only beside their citation line.
  - Nothing is removed once shown: GATE V samples each beat at 50% and 85%,
    so every scene must be fully populated and steady by half-way.
"""
from manim import *
import glob
import os
# Explicit: `from manim import *` re-exports numpy as np at render time, but
# GATE A executes construct() against a stub that does not, so the import has
# to be its own line or the pre-flight raises NameError.
import numpy as np

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
TITLE_Y  = 3.02
HAIR_Y   = 2.66
CLOSE_Y  = -2.50
UNDER_Y  = -2.78
CITE_Y   = -3.20
BUG_Y    = -3.12


# ── Type helpers ─────────────────────────────────────────────────────────────
def _t(txt, size=26, color=None, weight=None):
    """Serif label. Single Text mobject — never multi-word italic."""
    kw = {"font_size": size, "color": color if color is not None else INK}
    if SERIF:
        kw["font"] = SERIF
    if weight:
        kw["weight"] = weight
    return Text(txt, **kw)


def _fit(m, max_w, at):
    """Scale a mobject down to max_w if needed, then centre it at `at`."""
    if m.width > max_w:
        m.scale(max_w / m.width)
    m.move_to(at)
    return m


def _chip(txt, size=20, fill=ACC, fg=CARD):
    """Accent chip: terracotta ground, white glyphs (3.1:1 — a mark, not body)."""
    label = _t(txt, size=size, color=fg)
    box = RoundedRectangle(
        width=label.width + 0.46, height=label.height + 0.30,
        corner_radius=0.12, color=fill, fill_color=fill, fill_opacity=1.0,
        stroke_width=0)
    label.move_to(box.get_center())
    return VGroup(box, label)


def _quiet_chip(txt, size=20):
    label = _t(txt, size=size, color=INK)
    box = RoundedRectangle(
        width=label.width + 0.46, height=label.height + 0.28,
        corner_radius=0.12, color=GHOST, fill_color=CARD, fill_opacity=1.0,
        stroke_width=1.6)
    label.move_to(box.get_center())
    return VGroup(box, label)


def _card(w, h, at, radius=0.16, stroke=GHOST, sw=1.8):
    return RoundedRectangle(width=w, height=h, corner_radius=radius,
                            color=stroke, stroke_width=sw,
                            fill_color=CARD, fill_opacity=1.0).move_to(at)


def chrome(scene, title, cite=None):
    """Standing furniture: title + hairline + wordmark bug + citation line."""
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
    """The beat's closing line, in the accented text token, with a rule under it."""
    line = _fit(_t(text, size=size, color=ACCT, weight="BOLD"), max_w,
                [cx, CLOSE_Y, 0])
    under = _underline(line, buff=0.16)
    scene.play(FadeIn(line, shift=UP * 0.10), run_time=0.75)
    scene.play(Create(under), run_time=0.4)
    return VGroup(line, under)


def _underline(m, color=ACC, sw=4, buff=0.14, pad=0.10):
    """A rule the width of `m`, sat under it.

    Built from LEFT/RIGHT + set_width + next_to rather than from
    `m.get_left()[0]` arithmetic: GATE A executes scenes against a geometry
    STUB where a Text's width is unknowable, so coordinates derived from
    get_left()/get_right() land outside the frame and trip the pre-flight.
    """
    ln = Line(LEFT, RIGHT, color=color, stroke_width=sw)
    ln.set_width(max(float(m.width) + pad * 2, 0.4))
    ln.next_to(m, DOWN, buff=buff)
    return ln


def _strike(m, color=ACC, sw=4, pad=0.16):
    """A rule struck through `m` — same stub-safe construction as _underline.

    Flagged `_qc_intentional` so GATE B's TEXT-ON-CURVE rule exempts it: a
    strike-through is *supposed* to cross its label, and the audit provides
    this hook for exactly that (editor's marks, rings, strikes).
    """
    ln = Line(LEFT, RIGHT, color=color, stroke_width=sw)
    ln.set_width(max(float(m.width) + pad * 2, 0.4))
    ln.move_to(m.get_center())
    ln._qc_intentional = True
    return ln


def _tick(x, y, h=0.24, color=INK, op=0.35, sw=2.4):
    return Line([x, y - h / 2, 0], [x, y + h / 2, 0],
                color=color, stroke_width=sw, stroke_opacity=op)


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER  (13.57 s)
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "AI in Astronomy & Space Science  ·  Ep. 03",
               cite="brutalist.art  ·  ai-explainer  ·  Pragmatist register")

        name = _t("Om Mali", size=98, weight="BOLD").move_to([-3.15, 1.15, 0])
        self.play(Write(name), run_time=1.2)

        hair = _underline(name, sw=7, buff=0.22, pad=0.12)
        self.play(Create(hair), run_time=0.7)

        role = _t("Humanitarians AI  ·  presenter", size=29, color=SOFT)
        role.move_to([-3.15, -0.22, 0])
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.6)

        sub = _fit(_t("how LIGO learned to name its own noise", size=26,
                      color=SOFT), 5.5, [-3.15, -1.02, 0])
        self.play(FadeIn(sub), run_time=0.6)

        panel = _card(5.5, 3.5, [3.15, 0.45, 0])
        self.play(Create(panel), run_time=0.8)

        l1 = _t("The hard part here", size=32).move_to([3.15, 1.45, 0])
        l2 = _t("is not the physics.", size=32).move_to([3.15, 0.90, 0])
        div = Line([1.05, 0.42, 0], [5.25, 0.42, 0], color=RULE, stroke_width=2)
        l3 = _t("It is trusting", size=34, color=ACCT, weight="BOLD")
        l3.move_to([3.15, -0.12, 0])
        l4 = _t("the instrument.", size=34, color=ACCT, weight="BOLD")
        l4.move_to([3.15, -0.68, 0])

        self.play(FadeIn(l1, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(l2, shift=UP * 0.08), run_time=0.5)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(l3, shift=UP * 0.08), run_time=0.6)
        self.play(FadeIn(l4, shift=UP * 0.08), run_time=0.6)

        closer(self, "Ep. 03  ·  Gravity Spy, and where it stops working.",
               cx=-0.4, size=28, max_w=8.6)
        self.wait(4.4)


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — EXECUTIVE SUMMARY  (18.86 s)
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath")

        field = _card(5.2, 4.3, [-3.45, 0.20, 0])
        self.play(Create(field), run_time=0.7)

        # The field is cleared where the caption goes. Text laid over the tick
        # strokes is a GATE B TEXT-ON-CURVE error and, more to the point, is
        # genuinely harder to read — so the noise makes room for the label.
        CLEAR = (-4.70, -0.70, -2.55, -0.02)   # x0, y0, x1, y1
        ticks = VGroup()
        rng = np.random.RandomState(17)
        for i in range(154):
            x = -5.75 + (i % 14) * 0.355 + rng.uniform(-0.05, 0.05)
            y = 2.02 - (i // 14) * 0.31 + rng.uniform(-0.04, 0.04)
            if CLEAR[0] < x < CLEAR[2] and CLEAR[1] < y < CLEAR[3]:
                continue
            ticks.add(_tick(x, y, h=rng.uniform(0.12, 0.24), op=0.30))
        self.play(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.004),
                  run_time=1.6)

        real = _tick(-3.62, 0.47, h=0.62, color=ACC, op=1.0, sw=6)
        ring = Circle(radius=0.46, color=ACC, stroke_width=3).move_to([-3.62, 0.47, 0])
        self.play(Create(real), Create(ring), run_time=0.7)
        lbl = _t("one real signal", size=20, color=ACCT).move_to([-3.62, -0.36, 0])
        back = Rectangle(width=lbl.width + 0.24, height=lbl.height + 0.14,
                         color=CARD, fill_color=CARD, fill_opacity=1,
                         stroke_width=0).move_to(lbl.get_center())
        self.play(FadeIn(back), FadeIn(lbl), run_time=0.4)

        lines = [
            _t("Far more noise than signal.", size=33),
            _t("Every glitch becomes a picture.", size=33),
            _t("People name the pictures.", size=33),
            _t("A network learns the names.", size=33),
        ]
        for ln, y in zip(lines, [1.95, 1.10, 0.25, -0.60]):
            _fit(ln, 6.1, [2.75, y, 0])
            self.play(FadeIn(ln, shift=RIGHT * 0.18), run_time=0.55)

        tiles = VGroup()
        for i, nm in enumerate(("Blip", "Whistle", "Koi Fish")):
            tx = 1.20 + i * 1.60
            tile = _card(1.38, 0.92, [tx, -1.62, 0], radius=0.08)
            chip = _t(nm, size=18, color=SOFT).move_to([tx, -1.62, 0])
            tiles.add(VGroup(tile, chip))
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.12) for t in tiles],
                              lag_ratio=0.25), run_time=1.0)

        closer(self, "Naming the noise is the trust step.", cx=0.4, size=34)
        self.wait(7.6)


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE STAKES  (19.80 s)
# ═════════════════════════════════════════════════════════════════════════════
class B03_NearMiss(Scene):

    SEC = 1.72      # units per second on the axis

    def _x(self, t):
        return t * self.SEC

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "GW170817  ·  17 August 2017",
               cite="LIGO/Virgo GW170817 · Fermi-GBM GRB 170817A · schematic traces")

        h_y, l_y = 1.62, 0.22
        x0, x1 = -5.6, 3.05

        h_lbl = _t("HANFORD", size=23, color=SOFT).move_to([-4.85, h_y + 0.66, 0])
        l_lbl = _t("LIVINGSTON", size=23, color=SOFT).move_to([-4.60, l_y + 0.66, 0])
        self.play(FadeIn(h_lbl), FadeIn(l_lbl), run_time=0.4)

        rng = np.random.RandomState(5)

        def trace(y0):
            pts = []
            for i in range(110):
                x = x0 + i * (x1 - x0) / 109.0
                pts.append([x, y0 + rng.uniform(-0.10, 0.10), 0])
            return VMobject().set_points_as_corners(pts).set_stroke(INK, 2.2)

        h_tr, l_tr = trace(h_y), trace(l_y)
        self.play(Create(h_tr), Create(l_tr), run_time=1.3)

        # ---- axis + merger --------------------------------------------------
        axis = Line([x0, -1.55, 0], [x1, -1.55, 0], color=INK, stroke_width=3)
        self.play(Create(axis), run_time=0.6)
        mline = DashedLine([0, -1.72, 0], [0, 2.42, 0], color=INK,
                           stroke_width=2.4, dash_length=0.12)
        mlbl = _t("MERGER  ·  t = 0", size=21).move_to([0, -1.95, 0])
        self.play(Create(mline), FadeIn(mlbl), run_time=0.7)

        # ---- the glitch, 1.1 s before ---------------------------------------
        gx = self._x(-1.1)
        spike = VMobject().set_points_as_corners([
            [gx - 0.14, l_y, 0], [gx - 0.07, l_y + 0.84, 0],
            [gx, l_y - 0.74, 0], [gx + 0.07, l_y + 0.56, 0],
            [gx + 0.14, l_y, 0],
        ]).set_stroke(ACC, 5)
        self.play(Create(spike), run_time=0.6)
        glbl = _t("glitch  ·  1.1 s before", size=21, color=ACCT)
        glbl.move_to([gx - 1.30, l_y - 0.92, 0])
        self.play(FadeIn(glbl), run_time=0.4)

        # Livingston greys downstream (never below ~45% legibility)
        dead = Rectangle(width=x1 - (gx + 0.22) + 0.1, height=0.95,
                         color=BG, fill_color=BG, fill_opacity=0.55,
                         stroke_width=0).move_to([(gx + 0.22 + x1) / 2, l_y, 0])
        self.play(FadeIn(dead), run_time=0.6)

        # ---- what the automated search could do ------------------------------
        node = _card(2.5, 0.92, [4.70, h_y, 0], radius=0.12)
        node_l = _t("joint search", size=21, color=SOFT).move_to([4.70, h_y, 0])
        a_ok = Arrow([x1 + 0.05, h_y, 0], [3.50, h_y, 0], color=INK,
                     stroke_width=3, buff=0.02, tip_length=0.16)
        self.play(Create(node), FadeIn(node_l), GrowArrow(a_ok), run_time=0.8)

        a_no = DashedLine([2.55, l_y, 0], [3.50, h_y - 0.55, 0],
                          color=GHOST, stroke_width=3, dash_length=0.1)
        cross = VGroup(
            Line([2.32, l_y + 0.24, 0], [2.76, l_y - 0.24, 0], color=ACC, stroke_width=4),
            Line([2.32, l_y - 0.24, 0], [2.76, l_y + 0.24, 0], color=ACC, stroke_width=4))
        self.play(Create(a_no), run_time=0.4)
        self.play(Create(cross), run_time=0.4)

        stamp = _chip("SINGLE DETECTOR", size=20).move_to([4.70, 0.52, 0])
        alert = _quiet_chip("first public alert", size=20).move_to([4.70, -0.46, 0])
        self.play(FadeIn(stamp, scale=1.08), run_time=0.6)
        self.play(FadeIn(alert), run_time=0.5)

        # ---- Fermi, +1.7 s ----------------------------------------------------
        fx = self._x(1.7)
        ftick = Line([fx, -1.55, 0], [fx, -1.05, 0], color=INK, stroke_width=3)
        fdot = Dot([fx, -1.05, 0], radius=0.09, color=INK)
        flbl = _t("FERMI  ·  GRB 170817A  ·  +1.7 s", size=21)
        flbl.move_to([fx - 0.10, -1.95, 0]).align_to([1.35, 0, 0], LEFT)
        self.play(Create(ftick), FadeIn(fdot), FadeIn(flbl), run_time=0.7)

        closer(self, "One glitch, and the alert went out on one detector.",
               cx=-0.3, size=30)
        self.wait(4.6)


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE PROBLEM: VOLUME  (14.83 s)
# ═════════════════════════════════════════════════════════════════════════════
class B04_MillionGlitches(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Observing Run 1  ·  51.5 days",
               cite="about 10^6 glitches above an SNR 6 threshold in the 51.5 d of O1  ·  Zevin et al. 2017")

        cells = VGroup()
        for i in range(51):
            cx = -5.95 + i * 0.236
            cells.add(Rectangle(width=0.20, height=0.44, color=GHOST,
                                stroke_width=1.2, fill_color=GHOST,
                                fill_opacity=0.0).move_to([cx, 2.10, 0]))
        self.play(LaggedStart(*[Create(c) for c in cells], lag_ratio=0.006),
                  run_time=1.0)
        filled = VGroup(*[c.copy().set_fill(INK, 0.55).set_stroke(INK, 1.2)
                          for c in cells])
        self.play(LaggedStart(*[FadeIn(c) for c in filled], lag_ratio=0.012),
                  run_time=1.3)
        daylbl = _t("51.5 days of data", size=21, color=SOFT).move_to([0, 1.62, 0])
        self.play(FadeIn(daylbl), run_time=0.4)

        big = _t("1,000,000", size=100, color=ACCT, weight="BOLD")
        big.move_to([-3.20, 0.42, 0])
        self.play(Write(big), run_time=1.4)
        blabel = _t("glitches logged", size=29).move_to([-3.20, -0.52, 0])
        self.play(FadeIn(blabel), run_time=0.4)
        cite2 = _t("Zevin et al. 2017", size=20, color=SOFT).move_to([-3.20, -1.06, 0])
        self.play(FadeIn(cite2), run_time=0.35)

        stack = VGroup()
        for i in range(195):
            sx = 1.15 + (i % 15) * 0.31
            sy = 1.02 - (i // 15) * 0.145
            stack.add(Rectangle(width=0.23, height=0.10, color=INK,
                                stroke_width=0, fill_color=INK,
                                fill_opacity=0.42).move_to([sx, sy, 0]))
        self.play(LaggedStart(*[FadeIn(s) for s in stack], lag_ratio=0.003),
                  run_time=1.2)
        vs = _t("the queue", size=21, color=SOFT).move_to([3.32, 1.44, 0])

        people = VGroup()
        for i in range(6):
            px = 2.28 + i * 0.42
            people.add(VGroup(
                Line([px, -1.02, 0], [px, -0.72, 0], color=ACC, stroke_width=4),
                Dot([px, -0.60, 0], radius=0.075, color=ACC)))
        plbl = _t("the team that vets it", size=21, color=SOFT)
        plbl.move_to([3.32, -1.42, 0])
        self.play(FadeIn(vs), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(p) for p in people], lag_ratio=0.1),
                  FadeIn(plbl), run_time=0.8)

        closer(self, "Hand sorting does not scale.", cx=-0.4, size=33)
        self.wait(3.2)


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE PROBLEM: SIMILARITY  (15.55 s)
#  Both features are drawn in the SAME compact footprint on purpose: at the
#  time-frequency scale that matters, a high-mass merger and a blip glitch are
#  near twins. Drawing them as obviously different shapes would be a nicer
#  picture and a false one.
# ═════════════════════════════════════════════════════════════════════════════
class B05_Impostor(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The impostor",
               cite="schematic morphologies, not detector data  ·  Cabero et al. 2019")

        lf = _card(5.4, 2.9, [-3.05, 1.15, 0])
        rf = _card(5.4, 2.9, [3.05, 1.15, 0])
        self.play(Create(lf), Create(rf), run_time=0.8)

        axes = VGroup()
        for cx in (-3.05, 3.05):
            axes.add(Line([cx - 2.35, -0.02, 0], [cx + 2.35, -0.02, 0],
                          color=GHOST, stroke_width=2))
            axes.add(Line([cx - 2.35, -0.02, 0], [cx - 2.35, 2.36, 0],
                          color=GHOST, stroke_width=2))
        self.add(axes)
        ax_lbls = VGroup()
        for cx in (-3.05, 3.05):
            f = _t("frequency", size=17, color=SOFT).rotate(PI / 2)
            f.move_to([cx - 2.62, 1.15, 0])
            t = _t("time", size=17, color=SOFT).move_to([cx, -0.34, 0])
            ax_lbls.add(f, t)
        self.play(FadeIn(ax_lbls), run_time=0.4)

        # Both features are drawn with the SAME envelope on purpose. The only
        # difference is the drift: the merger's bands lean right as frequency
        # rises (the chirp), the blip's do not. That is what a consistency
        # check has to separate, and it is why it often cannot.
        def smear(cx, drift):
            g = VGroup()
            for k in range(26):
                u = k / 25.0
                y = 0.22 + u * 1.70
                w = 0.40 * (1.0 - abs(u - 0.45) * 0.85)
                xc = cx + drift * (u - 0.5)
                g.add(Line([xc - max(w, 0.07), y, 0], [xc + max(w, 0.07), y, 0],
                           color=INK, stroke_width=6))
            return g

        chirp = smear(-3.05, 0.95)
        self.play(LaggedStart(*[Create(c) for c in chirp], lag_ratio=0.02),
                  run_time=1.2)
        llbl = _t("MERGER    real signal", size=24).move_to([-3.05, -0.92, 0])
        self.play(FadeIn(llbl), run_time=0.4)

        blip = smear(3.05, 0.0)
        self.play(LaggedStart(*[Create(b) for b in blip], lag_ratio=0.02),
                  run_time=1.2)
        rlbl = _t("BLIP    instrument noise", size=24).move_to([3.05, -0.92, 0])
        self.play(FadeIn(rlbl), run_time=0.4)

        same = _fit(_t("same footprint  ·  about ten milliseconds, wide band  ·  about two blips per hour, per detector",
                       size=20, color=SOFT), 11.0, [0, -1.42, 0])
        self.play(FadeIn(same), run_time=0.5)

        self.wait(2.2)      # the comparison holds — legibility contract

        brace = Line([-5.35, -1.88, 0], [5.35, -1.88, 0], color=GHOST,
                     stroke_width=2.4)
        blbl = _t("standard signal-consistency check", size=21, color=SOFT)
        blbl.move_to([0, -2.16, 0])
        self.play(Create(brace), FadeIn(blbl), run_time=0.6)

        v1 = _quiet_chip("looks like a merger", size=20).move_to([-3.05, -2.74, 0])
        v2 = _quiet_chip("looks like a merger", size=20).move_to([3.05, -2.74, 0])
        self.play(FadeIn(v1), FadeIn(v2), run_time=0.6)
        v2b = _chip("MISREAD", size=22).move_to([3.05, -2.74, 0])
        self.play(Transform(v2, v2b), run_time=0.8)
        self.wait(1.6)


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THE FRAMEWORK  (20.29 s)
# ═════════════════════════════════════════════════════════════════════════════
STATIONS = [
    ("1", "RENDER", "every glitch becomes\nfour spectrograms"),
    ("2", "LABEL", "volunteers name\nthe shapes"),
    ("3", "TRAIN", "a CNN learns\nfrom those names"),
    ("4", "SORT", "the machine sorts\nthe flood first"),
]
ST_X = [-4.62, -1.54, 1.54, 4.62]


class B06_Framework(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Gravity Spy  ·  the loop",
               cite="Zevin et al. 2017  ·  Glanzer et al. 2022")

        groups = []
        for (num, name, sub), cx in zip(STATIONS, ST_X):
            box = _card(2.78, 3.10, [cx, 0.75, 0])
            disc = Circle(radius=0.24, color=ACC, fill_color=ACC,
                          fill_opacity=1.0, stroke_width=0)
            disc.move_to([cx - 1.02, 1.94, 0])
            n = _t(num, size=22, color=CARD).move_to(disc.get_center())
            title = _t(name, size=27, weight="BOLD").move_to([cx + 0.20, 1.94, 0])
            body = _fit(_t(sub, size=19, color=SOFT), 2.42, [cx, -0.42, 0])
            groups.append(VGroup(box, disc, n, title, body))

        for g in groups:
            self.play(FadeIn(g[0]), run_time=0.32)

        # glyph zone: y 0.52 … 1.36, clear of the header and the body text
        glyphs = [VGroup(), VGroup(), VGroup(), VGroup()]
        for i in range(4):
            glyphs[0].add(Rectangle(width=1.5, height=0.17, color=INK,
                                    stroke_width=1.5, fill_color=CARD,
                                    fill_opacity=1
                                    ).move_to([ST_X[0], 1.32 - i * 0.27, 0]))
        for i, nm in enumerate(("Blip", "Whistle", "Koi Fish")):
            glyphs[1].add(_quiet_chip(nm, size=16).move_to([ST_X[1], 1.32 - i * 0.42, 0]))
        for i, cnt in enumerate((4, 3, 2)):
            for j in range(cnt):
                glyphs[2].add(Dot([ST_X[2] - 0.70 + i * 0.70,
                                   1.32 - j * 0.28 - (4 - cnt) * 0.14, 0],
                                  radius=0.070, color=INK))
        for i in range(4):
            glyphs[3].add(Rectangle(width=0.42, height=0.34, color=INK,
                                    stroke_width=1.5, fill_color=CARD,
                                    fill_opacity=1
                                    ).move_to([ST_X[3] - 0.78 + i * 0.52, 0.94, 0]))

        for i, g in enumerate(groups):
            self.play(FadeIn(g[1]), FadeIn(g[2]), FadeIn(g[3]), run_time=0.34)
            self.play(LaggedStart(*[FadeIn(m) for m in glyphs[i]],
                                  lag_ratio=0.08), run_time=0.6)
            self.play(FadeIn(g[4]), run_time=0.34)
            if i < 3:
                a = Arrow([ST_X[i] + 1.42, 0.75, 0], [ST_X[i + 1] - 1.42, 0.75, 0],
                          color=INK, stroke_width=3, buff=0.02, tip_length=0.16)
                self.play(GrowArrow(a), run_time=0.3)

        arc = ArcBetweenPoints([ST_X[3], -0.86, 0], [ST_X[1], -0.86, 0],
                               angle=-TAU / 7, color=ACC, stroke_width=5)
        tip = Triangle(color=ACC, fill_color=ACC, fill_opacity=1, stroke_width=0)
        tip.scale(0.13).rotate(PI / 2).move_to([ST_X[1] + 0.06, -0.86, 0])
        self.play(Create(arc), run_time=1.0)
        self.play(FadeIn(tip), run_time=0.25)

        closer(self, "Unsure cases route back to people.", cx=1.4, size=30)
        self.wait(5.4)


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — WORKED EXAMPLE  (15.51 s)
#  The framework rail stays on screen while one blip walks it. The four windows
#  show the SAME event: the wider the window, the thinner the feature looks.
# ═════════════════════════════════════════════════════════════════════════════
class B07_WorkedExample(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "One blip, through the loop",
               cite="four time windows: ±0.25, 0.5, 1.0, 2.0 s, shown together  ·  Zevin et al. 2017")

        rail_x = [-4.7, -1.6, 1.5, 4.6]
        # The rail is drawn as connectors BETWEEN the chips, not as one line
        # running under them: a stroke passing behind a label is a GATE B
        # TEXT-ON-CURVE error even when the chip's opaque box hides it.
        line = VGroup(*[Line([a, 2.30, 0], [b, 2.30, 0], color=RULE, stroke_width=2)
                        for a, b in ((-5.70, -5.55), (-3.85, -2.45),
                                     (-0.75, 0.65), (2.35, 3.75), (5.45, 5.60))])
        self.play(Create(line), run_time=0.3)
        rail = VGroup(*[_quiet_chip(n, size=20).move_to([cx, 2.30, 0])
                        for n, cx in zip(("RENDER", "LABEL", "TRAIN", "SORT"), rail_x)])
        self.play(LaggedStart(*[FadeIn(c) for c in rail], lag_ratio=0.15),
                  run_time=0.8)

        marker = Dot([rail_x[0], 1.78, 0], radius=0.13, color=ACC)
        self.play(FadeIn(marker, scale=1.4), run_time=0.4)

        # ---- station 1: the four windows, same event -------------------------
        spec = [("0.25 s", -4.55, 1.02, 0.62), ("0.5 s", -1.80, 1.02, 0.38),
                ("1.0 s", -4.55, -0.95, 0.22), ("2.0 s", -1.80, -0.95, 0.12)]
        for name, tx, ty, wide in spec:
            t = _card(2.42, 1.44, [tx, ty, 0], radius=0.08)
            inner = VGroup()
            for k in range(13):
                u = k / 12.0
                w = wide * (1.0 - abs(u - 0.42) * 1.0)
                inner.add(Line([tx - max(w, 0.028), ty - 0.48 + u * 0.96, 0],
                               [tx + max(w, 0.028), ty - 0.48 + u * 0.96, 0],
                               color=INK, stroke_width=3.4))
            lab = _t(name, size=19, color=SOFT).move_to([tx, ty - 0.94, 0])
            self.play(FadeIn(VGroup(t, inner), scale=1.03), FadeIn(lab),
                      run_time=0.42)
        same = _t("same event, four scales", size=21, color=SOFT)
        same.move_to([-4.55, -2.28, 0])
        self.play(FadeIn(same), run_time=0.4)

        # ---- the human call ---------------------------------------------------
        self.play(marker.animate.move_to([rail_x[1], 1.78, 0]), run_time=0.5)
        hhead = _t("the human call", size=23, color=SOFT).move_to([3.10, 1.62, 0])
        self.play(FadeIn(hhead), run_time=0.35)
        marks = VGroup()
        for i in range(3):
            px = 1.35 + i * 0.44
            marks.add(VGroup(Line([px, 0.72, 0], [px, 1.02, 0], color=ACC,
                                  stroke_width=4),
                             Dot([px, 1.14, 0], radius=0.08, color=ACC)))
        call = _chip("BLIP", size=24).move_to([4.10, 0.94, 0])
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.15),
                  run_time=0.5)
        self.play(FadeIn(call, scale=1.1), run_time=0.45)
        vsub = _t("volunteers who have seen thousands", size=18, color=SOFT)
        _fit(vsub, 4.6, [3.10, 0.32, 0])
        self.play(FadeIn(vsub), run_time=0.35)

        div = Line([0.60, -0.05, 0], [6.05, -0.05, 0], color=RULE, stroke_width=2)
        self.play(Create(div), run_time=0.3)

        # ---- the machine call --------------------------------------------------
        self.play(marker.animate.move_to([rail_x[2], 1.78, 0]), run_time=0.45)
        mhead = _t("the machine call", size=23, color=SOFT).move_to([3.10, -0.42, 0])
        self.play(FadeIn(mhead), run_time=0.35)
        net = VGroup()
        for i, cnt in enumerate((4, 3, 2)):
            for j in range(cnt):
                net.add(Dot([1.05 + i * 0.62, -1.02 - j * 0.30 + (4 - cnt) * 0.15, 0],
                            radius=0.075, color=INK))
        self.play(LaggedStart(*[FadeIn(n) for n in net], lag_ratio=0.04),
                  run_time=0.6)
        self.play(marker.animate.move_to([rail_x[3], 1.78, 0]), run_time=0.45)

        outcard = _card(2.9, 1.42, [4.45, -1.32, 0])
        out1 = _t("BLIP", size=38, color=ACCT, weight="BOLD").move_to([4.45, -1.02, 0])
        out2 = _t("in milliseconds", size=19, color=SOFT).move_to([4.45, -1.68, 0])
        self.play(Create(outcard), run_time=0.4)
        self.play(FadeIn(out1, scale=1.06), FadeIn(out2), run_time=0.55)

        closer(self, "Trained on the human calls.", cx=1.9, size=30, max_w=5.6)
        self.wait(1.6)


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — THE RESULT  (14.29 s)
# ═════════════════════════════════════════════════════════════════════════════
class B08_Result(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What it actually delivers",
               cite="97.1% = CNN average accuracy on held-out test data (Zevin et al. 2017)  ·  counts through O3 (Glanzer et al. 2022)")

        ring_bg = Circle(radius=1.34, color=GHOST, stroke_width=16)
        ring_bg.move_to([-4.15, 1.05, 0])
        self.play(Create(ring_bg), run_time=0.5)
        arc = Arc(radius=1.34, start_angle=PI / 2, angle=-TAU * 0.971,
                  color=ACC, stroke_width=16).move_to(ring_bg.get_center())
        self.play(Create(arc), run_time=1.3)
        pct = _t("97.1%", size=62, color=ACCT, weight="BOLD")
        pct.move_to([-4.15, 1.16, 0])
        plb = _t("average accuracy", size=21, color=SOFT).move_to([-4.15, 0.46, 0])
        self.play(FadeIn(pct, scale=1.08), FadeIn(plb), run_time=0.7)

        strip = VGroup()
        for i in range(20):
            strip.add(Rectangle(width=0.22, height=0.40, color=INK,
                                stroke_width=1.4, fill_color=CARD,
                                fill_opacity=1).move_to([-5.95 + i * 0.29, -0.80, 0]))
        self.play(LaggedStart(*[Create(s) for s in strip], lag_ratio=0.04),
                  run_time=0.9)
        slb = _fit(_t("20 named classes:  Blip · Koi Fish · Whistle · Scattered Light · …",
                      size=20, color=SOFT), 6.1, [-3.10, -1.38, 0])
        self.play(FadeIn(slb), run_time=0.4)

        base_x, maxw, maxv = 0.55, 3.40, 379805.0
        for name, val, y in (("HANFORD", 233981, 1.60), ("LIVINGSTON", 379805, 0.30)):
            lab = _t(name, size=21, color=SOFT).move_to([0, y + 0.52, 0])
            lab.align_to([base_x, 0, 0], LEFT)
            track = Rectangle(width=maxw, height=0.50, color=GHOST,
                              stroke_width=1.4, fill_opacity=0)
            track.move_to([base_x + maxw / 2, y, 0])
            self.play(FadeIn(lab), Create(track), run_time=0.4)
            w = maxw * (val / maxv)
            bar = Rectangle(width=w, height=0.50, color=INK, stroke_width=0,
                            fill_color=INK, fill_opacity=0.82)
            bar.move_to([base_x + w / 2, y, 0])
            num = _t(f"{val:,}", size=27, weight="BOLD")
            num.move_to([0, y, 0]).align_to([base_x + maxw + 0.28, 0, 0], LEFT)
            self.play(GrowFromEdge(bar, LEFT), run_time=0.75)
            self.play(FadeIn(num), run_time=0.35)

        tot = _fit(_t("613,786 labelled through O3", size=30, color=ACCT,
                      weight="BOLD"), 5.2, [3.25, -0.85, 0])
        under = _underline(tot, sw=3.4, buff=0.12)
        self.play(FadeIn(tot, shift=UP * 0.08), run_time=0.6)
        self.play(Create(under), run_time=0.35)

        closer(self, "High accuracy, at a scale people could not reach.",
               cx=-0.3, size=29)
        self.wait(1.8)


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — WHERE IT FAILS  (16.85 s)
# ═════════════════════════════════════════════════════════════════════════════
BIN_X = [-5.30, -3.68, -2.06, -0.44, 1.18, 2.80, 4.42]
BIN_NAMES = ["Blip", "Koi Fish", "Whistle", "Scattered\nLight", "+16 more"]


class B09_UnseenClass(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The hole in the method",
               cite="Paired Doves and Helix identified by volunteers in beta testing  ·  Zevin et al. 2017")

        BIN_Y, IN_Y = 0.55, 1.98

        inlbl = _t("incoming glitches", size=21, color=SOFT).move_to([0, 2.50, 0])
        self.play(FadeIn(inlbl), run_time=0.35)

        tiles = VGroup()
        for i, bx in enumerate(BIN_X):
            col = ACC if i >= 5 else INK
            sw = 3.2 if i >= 5 else 1.6
            tiles.add(Rectangle(width=0.70, height=0.48, color=col, stroke_width=sw,
                                fill_color=CARD, fill_opacity=1
                                ).move_to([bx, IN_Y, 0]).set_z_index(6))
        self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.08),
                  run_time=0.9)

        # ---- the trained bins ------------------------------------------------
        bins = VGroup()
        for nm, bx in zip(BIN_NAMES, BIN_X[:5]):
            box = Rectangle(width=1.44, height=1.12, color=INK, stroke_width=1.8,
                            fill_color=CARD, fill_opacity=1).move_to([bx, BIN_Y, 0])
            lab = _fit(_t(nm, size=18, color=SOFT), 1.26, [bx, BIN_Y - 0.26, 0])
            bins.add(VGroup(box, lab))
        self.play(LaggedStart(*[FadeIn(b) for b in bins], lag_ratio=0.12),
                  run_time=0.9)
        klbl = _t("the classes it was trained on", size=21, color=SOFT)
        klbl.move_to([-2.06, -0.30, 0])
        self.play(FadeIn(klbl), run_time=0.4)

        # ---- the five that fit — they land INSIDE their bin --------------------
        self.play(*[tiles[i].animate.scale(0.62).move_to([BIN_X[i], BIN_Y + 0.34, 0])
                    for i in range(5)], run_time=0.8)

        # the stream keeps arriving
        more = VGroup()
        for i, bx in enumerate(BIN_X):
            more.add(Rectangle(width=0.70, height=0.48, color=INK, stroke_width=1.6,
                               fill_color=CARD, fill_opacity=1).move_to([bx, IN_Y, 0]))
        self.play(LaggedStart(*[FadeIn(m) for m in more], lag_ratio=0.05),
                  run_time=0.6)

        # ---- the two that do not ----------------------------------------------
        q1 = _t("?", size=42, color=ACCT, weight="BOLD").move_to([2.80, 1.48, 0])
        q2 = _t("?", size=42, color=ACCT, weight="BOLD").move_to([4.42, 1.48, 0])
        self.play(FadeIn(q1), FadeIn(q2), run_time=0.5)

        ans = _quiet_chip("nearest known class", size=20).move_to([3.35, -1.18, 0])
        self.play(FadeIn(ans), run_time=0.5)
        strike = _strike(ans, pad=0.10)
        wrong = _t("confidently wrong", size=21, color=ACCT).move_to([3.35, -1.72, 0])
        self.play(Create(strike), FadeIn(wrong), run_time=0.6)

        # ---- people reach past the bins ----------------------------------------
        hand = VGroup(Line([-5.82, -1.55, 0], [-5.82, -1.22, 0], color=ACC,
                           stroke_width=5),
                      Dot([-5.82, -1.10, 0], radius=0.10, color=ACC))
        hlbl = _fit(_t("volunteers reach past the bins", size=21, color=SOFT),
                    3.9, [-3.45, -1.42, 0])
        self.play(FadeIn(hand), FadeIn(hlbl), run_time=0.5)

        nb, nl = VGroup(), VGroup()
        for bx, nm in ((2.80, "Paired\nDoves"), (4.42, "Helix")):
            nb.add(Rectangle(width=1.44, height=1.12, color=ACC, stroke_width=2.6,
                             fill_color=CARD, fill_opacity=1).move_to([bx, BIN_Y, 0]))
            nl.add(_fit(_t(nm, size=18, color=ACCT), 1.26, [bx, BIN_Y - 0.26, 0]))
        self.play(Create(nb), run_time=0.7)
        self.play(FadeIn(nl), run_time=0.45)
        self.play(tiles[5].animate.scale(0.62).move_to([2.80, BIN_Y + 0.34, 0]),
                  tiles[6].animate.scale(0.62).move_to([4.42, BIN_Y + 0.34, 0]),
                  run_time=0.7)
        flbl = _fit(_t("found by people, not by the network", size=21, color=SOFT),
                    3.9, [3.61, -0.30, 0])
        self.play(FadeIn(flbl), run_time=0.4)

        closer(self, "A classifier cannot name what it has never seen.",
               cx=-0.4, size=31, max_w=9.2)
        self.wait(3.0)


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — SCOPE  (21.29 s)
# ═════════════════════════════════════════════════════════════════════════════
class B10_Scope(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What this tool is not for",
               cite="BayesWave: LIGO-T1700406  ·  matched-filtering searches: PyCBC Live · GstLAL · MBTA")

        cols = [(-4.08, "DETECT", "find the wave\nin the strain"),
                (0.00, "CLEAN ONE EVENT", "subtract this\nparticular glitch"),
                (4.08, "NAME THE CATEGORY", "sort all noise into\nnamed classes")]
        for cx, head, sub in cols:
            p = _card(3.84, 4.10, [cx, 0.28, 0])
            self.play(Create(p), run_time=0.4)
        for cx, head, sub in cols:
            h = _fit(_t(head, size=25, weight="BOLD"), 3.5, [cx, 1.92, 0])
            s = _fit(_t(sub, size=19, color=SOFT), 3.4, [cx, 1.24, 0])
            self.play(FadeIn(h), FadeIn(s), run_time=0.35)

        g1 = VGroup(*[Line([-5.55 + i * 0.49, 0.24, 0], [-5.55 + i * 0.49, 0.80, 0],
                           color=INK, stroke_width=3, stroke_opacity=0.65)
                      for i in range(7)])
        g1lbl = _t("a bank of templates", size=18, color=SOFT).move_to([-4.08, -0.18, 0])
        g2 = VGroup(
            Line([-1.45, 0.50, 0], [-0.75, 0.50, 0], color=INK, stroke_width=3),
            Line([-0.75, 0.50, 0], [-0.60, 0.96, 0], color=ACC, stroke_width=4),
            Line([-0.60, 0.96, 0], [-0.42, 0.04, 0], color=ACC, stroke_width=4),
            Line([-0.42, 0.04, 0], [-0.28, 0.50, 0], color=ACC, stroke_width=4),
            Line([-0.28, 0.50, 0], [1.45, 0.50, 0], color=INK, stroke_width=3))
        g2lbl = _t("one glitch, removed", size=18, color=SOFT).move_to([0.0, -0.18, 0])
        g3 = VGroup()
        for i in range(4):
            g3.add(Rectangle(width=0.50, height=0.38, color=INK, stroke_width=1.6,
                             fill_color=CARD, fill_opacity=1
                             ).move_to([2.74 + i * 0.72, 0.80, 0]))
            g3.add(Arrow([2.74 + i * 0.72, 0.54, 0], [2.74 + i * 0.72, 0.16, 0],
                         color=GHOST, stroke_width=2, buff=0.02, tip_length=0.1))
        g3lbl = _t("the whole stream, named", size=18, color=SOFT)
        g3lbl.move_to([4.08, -0.18, 0])

        self.play(LaggedStart(*[Create(m) for m in g1], lag_ratio=0.06),
                  FadeIn(g1lbl), run_time=0.8)
        self.play(LaggedStart(*[Create(m) for m in g2], lag_ratio=0.10),
                  FadeIn(g2lbl), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(m) for m in g3], lag_ratio=0.06),
                  FadeIn(g3lbl), run_time=0.9)

        o1 = _quiet_chip("MATCHED FILTERING", size=19).move_to([-4.08, -0.86, 0])
        o1n = _t("classical signal processing", size=18, color=SOFT)
        o1n.move_to([-4.08, -1.42, 0])
        o2 = _quiet_chip("BAYESWAVE", size=19).move_to([0.0, -0.86, 0])
        o2n = _t("one event, modelled", size=18, color=SOFT).move_to([0.0, -1.42, 0])
        o3 = _chip("GRAVITY SPY", size=19).move_to([4.08, -0.86, 0])
        o3n = _t("continuous, at scale", size=18, color=SOFT).move_to([4.08, -1.42, 0])
        self.play(FadeIn(o1), FadeIn(o1n), run_time=0.45)
        self.play(FadeIn(o2), FadeIn(o2n), run_time=0.45)
        self.play(FadeIn(o3), FadeIn(o3n), run_time=0.45)

        # strike the two jobs this classifier does not do — through their chips
        for chip in (o1, o2):
            s = _strike(chip, pad=0.14)
            self.play(Create(s), run_time=0.45)
        notme = _t("not this classifier", size=20, color=ACCT)
        notme.move_to([-2.04, -1.92, 0])
        self.play(FadeIn(notme), run_time=0.4)

        ring = RoundedRectangle(width=3.98, height=4.24, corner_radius=0.18,
                                color=ACC, stroke_width=3.6, fill_opacity=0)
        ring.move_to([4.08, 0.28, 0])
        self.play(Create(ring), run_time=0.7)

        closer(self, "Use it for the category, not the catch.", cx=-0.6, size=31)
        self.wait(4.4)
