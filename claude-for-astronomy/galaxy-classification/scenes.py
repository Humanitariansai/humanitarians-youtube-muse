"""scenes.py — Manim scenes for claude-hai-galaxy-classification.

*Learning What the Crowd Would Say.* — ai-explainer, claude-hai, Ep. 04.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY — never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta — the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream).
                  Terracotta as text on cream is 2.74:1 and fails WCAG at every
                  size, so the brand accent stays a mark.

LAYOUT BAND PLAN (every scene obeys it — this is what keeps the gates green)
  y = +3.02   title            (chrome)
  y = +2.66   hairline         (chrome)
  y = +2.4 … -1.9   the figure
  y = -2.50   the closing line, terracotta rule at -2.78
  y = -3.20   the citation, left-anchored   (chrome)
  y = -3.12   the @HumanitariansAI wordmark bug, right-anchored (chrome, LOGO LAW)

  Manim frame is 14.222 x 8.0 units. GATE V's title-safe inset maps to
  x +-6.4, y +-3.6; everything here stays inside x +-6.15, y +-3.30.

GALAXY IMAGERY
  Every cutout is SYNTHETIC, produced by assets/gen_galaxies.py from seeded
  morphology recipes. Scenes that could be mistaken for showing observations
  caption them. Cutouts are framed dark tiles on the cream ground — plates on a
  page — and never carry the accent colour.

GATE NOTES (learned the expensive way on Ep. 03)
  - `import numpy as np` explicitly: GATE A's stub does not re-export it.
  - Never build a Line from `mob.get_left()[0]`; under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set `_qc_intentional` or GATE B calls it text-on-curve.
  - Never run a stroke behind a label, even under an opaque chip.
  - ImageMobject is not a VMobject: group it with `Group`, never `VGroup`.
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
ASSETS = HERE / "assets"

# ── Palette ──────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
SOFT  = ManimColor("#6E6A57")
GHOST = ManimColor("#B9B4A0")
ACC   = ManimColor("#D97757")
ACCT  = ManimColor("#A44A32")
CARD  = ManimColor("#FFFFFF")
RULE  = ManimColor("#D9D4C4")
PLATE = ManimColor("#20202A")     # stand-in tone if an asset is missing

X_MAX, Y_MAX = 6.15, 3.30
TITLE_Y  = 3.02
HAIR_Y   = 2.66
CLOSE_Y  = -2.50
UNDER_Y  = -2.78
CITE_Y   = -3.20
BUG_Y    = -3.12


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


def _quiet_chip(txt, size=20, w=None):
    label = _t(txt, size=size, color=INK)
    box = RoundedRectangle(width=(w or label.width + 0.46),
                           height=label.height + 0.28, corner_radius=0.12,
                           color=GHOST, fill_color=CARD, fill_opacity=1.0,
                           stroke_width=1.6)
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
    """Struck-through rule. Flagged `_qc_intentional` — a strike is SUPPOSED to
    cross its label, and GATE B provides this hook for exactly that."""
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


# ── Galaxy cutout helpers ────────────────────────────────────────────────────
def _cutout(name, side, at, frame=True):
    """A square synthetic galaxy cutout, framed like a plate in a paper.

    Returns a `Group` (not VGroup): ImageMobject is not a VMobject. Falls back to
    a flat plate if the asset is missing so a scene can never fail to render.
    """
    path = ASSETS / "galaxies" / name
    parts = []
    try:
        img = ImageMobject(str(path))
        img.height = side
        img.move_to(at)
        parts.append(img)
    except Exception:
        parts.append(Rectangle(width=side, height=side, color=PLATE,
                               fill_color=PLATE, fill_opacity=1,
                               stroke_width=0).move_to(at))
    if frame:
        parts.append(Rectangle(width=side, height=side, color=GHOST,
                               stroke_width=1.6, fill_opacity=0).move_to(at))
    return Group(*parts)


def _sheet(name, width, at, frame=True):
    """A pre-composited field of many galaxies, sized by WIDTH."""
    path = ASSETS / name
    parts = []
    h = width * 0.5707      # 12x7 sheet aspect; overridden below when known
    try:
        img = ImageMobject(str(path))
        img.width = width
        img.move_to(at)
        h = float(img.height)
        parts.append(img)
    except Exception:
        parts.append(Rectangle(width=width, height=h, color=PLATE,
                               fill_color=PLATE, fill_opacity=1,
                               stroke_width=0).move_to(at))
    if frame:
        parts.append(Rectangle(width=width, height=h, color=GHOST,
                               stroke_width=1.6, fill_opacity=0).move_to(at))
    return Group(*parts)


def _mark(x, y, color=INK, h=0.20, sw=3.0, op=0.85):
    """One tally mark — a person who looked at one galaxy."""
    return Line([x, y - h / 2, 0], [x, y + h / 2, 0],
                color=color, stroke_width=sw, stroke_opacity=op)


def _prop_bar(at, w, frac, h=0.34, left=ACC, right=GHOST):
    """A proportion bar: the share who chose each answer. The whole point of the
    episode is that THIS, not a word, is the training target."""
    x0 = at[0] - w / 2
    a = Rectangle(width=w * frac, height=h, color=left, fill_color=left,
                  fill_opacity=1, stroke_width=0)
    a.move_to([x0 + w * frac / 2, at[1], 0])
    b = Rectangle(width=w * (1 - frac), height=h, color=right, fill_color=right,
                  fill_opacity=0.55, stroke_width=0)
    b.move_to([x0 + w * frac + w * (1 - frac) / 2, at[1], 0])
    edge = Rectangle(width=w, height=h, color=INK, stroke_width=1.4,
                     fill_opacity=0).move_to([at[0], at[1], 0])
    return VGroup(a, b, edge)


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER  (12.42 s)
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "AI in Astronomy & Space Science  ·  Ep. 04",
               cite="brutalist.art  ·  ai-explainer  ·  Pragmatist register")

        name = _t("Om Mali", size=98, weight="BOLD").move_to([-3.15, 1.15, 0])
        self.play(Write(name), run_time=1.1)
        hair = _underline(name, sw=7, buff=0.22, pad=0.12)
        self.play(Create(hair), run_time=0.6)

        role = _t("Humanitarians AI  ·  presenter", size=29, color=SOFT)
        role.move_to([-3.15, -0.24, 0])
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        sub = _fit(_t("what Galaxy Zoo actually predicts", size=26, color=SOFT),
                   5.5, [-3.15, -1.02, 0])
        self.play(FadeIn(sub), run_time=0.5)

        panel = _card(5.5, 3.5, [3.15, 0.45, 0])
        self.play(Create(panel), run_time=0.7)

        l1 = _t("It does not learn", size=31).move_to([3.15, 1.52, 0])
        l2 = _t("what a galaxy is.", size=31).move_to([3.15, 0.98, 0])
        self.play(FadeIn(l1, shift=UP * 0.08), run_time=0.45)
        self.play(FadeIn(l2, shift=UP * 0.08), run_time=0.45)
        s1, s2 = _strike(l1, pad=0.10), _strike(l2, pad=0.10)
        self.play(Create(s1), Create(s2), run_time=0.5)

        div = Line([1.05, 0.50, 0], [5.25, 0.50, 0], color=RULE, stroke_width=2)
        self.play(Create(div), run_time=0.3)

        l3 = _t("It learns what people", size=32, color=ACCT, weight="BOLD")
        l3.move_to([3.15, -0.05, 0])
        l4 = _t("would say about it.", size=32, color=ACCT, weight="BOLD")
        l4.move_to([3.15, -0.62, 0])
        self.play(FadeIn(l3, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(l4, shift=UP * 0.08), run_time=0.5)

        closer(self, "Ep. 04  ·  Galaxy Zoo, and what it actually predicts.",
               cx=-0.4, size=28, max_w=8.6)
        self.wait(3.4)


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — EXECUTIVE SUMMARY  (16.55 s)
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="synthetic cutout, generated for this episode")

        tile = _cutout("spiral_101.png", 2.7, [-4.30, 1.05, 0])
        self.play(FadeIn(tile), run_time=0.7)

        # many people look at the SAME galaxy and do not agree
        marks = VGroup()
        for i in range(18):
            x = -5.55 + (i % 9) * 0.32
            y = -0.62 - (i // 9) * 0.34
            marks.add(_mark(x, y, color=INK if i % 3 else ACC, h=0.24))
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.05),
                  run_time=1.0)
        mlbl = _t("many people, one galaxy", size=20, color=SOFT)
        mlbl.move_to([-4.30, -1.42, 0])
        self.play(FadeIn(mlbl), run_time=0.4)

        bar = _prop_bar([-4.30, -1.92, 0], 2.7, 0.63)
        self.play(FadeIn(bar), run_time=0.6)

        lines = [
            _t("Shape is a clue to history.", size=32),
            _t("But shape is a judgement call.", size=32),
            _t("So keep the disagreement.", size=32),
        ]
        for ln, y in zip(lines, [1.75, 0.75, -0.25]):
            _fit(ln, 6.4, [2.35, y, 0])
            self.play(FadeIn(ln, shift=RIGHT * 0.18), run_time=0.55)

        closer(self, "Then train a network to predict the disagreement.",
               cx=0.0, size=32, max_w=9.6)
        self.wait(6.0)


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE SUBJECT  (16.60 s)
# ═════════════════════════════════════════════════════════════════════════════
SHAPES = [
    ("elliptical_301.png", "SMOOTH", "no disc, no features"),
    ("spiral_103.png", "SPIRAL", "a disc with arms"),
    ("barred_201.png", "BARRED", "a bar through the middle"),
    ("edgeon_401.png", "EDGE ON", "a disc seen side on"),
    ("merger_501.png", "MERGER", "two galaxies colliding"),
]
SHAPE_X = [-4.8, -2.4, 0.0, 2.4, 4.8]


class B03_Shapes(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What is being sorted",
               cite="synthetic cutouts, generated for this episode · shape encodes formation history")

        for (fn, label, sub), cx in zip(SHAPES, SHAPE_X):
            tile = _cutout(fn, 2.2, [cx, 0.90, 0])
            lab = _t(label, size=25, weight="BOLD").move_to([cx, -0.52, 0])
            s = _fit(_t(sub, size=18, color=SOFT), 2.3, [cx, -1.02, 0])
            self.play(FadeIn(tile, scale=1.04), run_time=0.42)
            self.play(FadeIn(lab), FadeIn(s), run_time=0.34)
            if label == "BARRED":
                ring = Ellipse(width=1.15, height=0.52, color=ACC,
                               stroke_width=3.4).move_to([cx, 0.90, 0])
                self.play(Create(ring), run_time=0.45)

        closer(self, "Shape carries the history. That is why anyone labels it.",
               cx=-0.2, size=29, max_w=9.6)
        self.wait(4.6)


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE CROWD  (20.27 s)
# ═════════════════════════════════════════════════════════════════════════════
class B04_Crowd(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Galaxy Zoo  ·  11 July 2007",
               cite="900,000 galaxies and ~38 classifications each: Lintott et al. 2011 · launch rate: A Zoo of Galaxies (2013)")

        sheet = _sheet("field_12x7.png", 5.5, [-3.25, 1.15, 0])
        self.play(FadeIn(sheet), run_time=0.9)

        big = _t("900,000", size=74, color=ACCT, weight="BOLD")
        big.move_to([-3.25, -1.05, 0])
        self.play(Write(big), run_time=1.0)
        blbl = _t("galaxy images, put online for anyone", size=22, color=SOFT)
        _fit(blbl, 5.5, [-3.25, -1.70, 0])
        self.play(FadeIn(blbl), run_time=0.4)

        rate = _t("20,000", size=52, weight="BOLD").move_to([3.15, 1.92, 0])
        rlbl = _t("classifications an hour", size=23, color=SOFT)
        rlbl.move_to([3.15, 1.34, 0])
        rsub = _t("within twelve hours of launch", size=19, color=SOFT)
        rsub.move_to([3.15, 0.92, 0])
        self.play(Write(rate), run_time=0.7)
        self.play(FadeIn(rlbl), FadeIn(rsub), run_time=0.45)

        div = Line([0.55, 0.52, 0], [6.05, 0.52, 0], color=RULE, stroke_width=2)
        self.play(Create(div), run_time=0.3)

        # the design decision that actually matters: repeat looks on ONE galaxy
        one = _cutout("spiral_102.png", 1.25, [1.35, -0.42, 0])
        self.play(FadeIn(one), run_time=0.45)
        tally = VGroup()
        for i in range(38):
            x = 2.55 + (i % 19) * 0.185
            y = -0.10 - (i // 19) * 0.34
            tally.add(_mark(x, y, color=ACC, h=0.24, sw=2.6))
        self.play(LaggedStart(*[Create(m) for m in tally], lag_ratio=0.02),
                  run_time=1.3)
        tl = _t("38 looks per galaxy, on average", size=22, color=ACCT)
        _fit(tl, 4.6, [4.05, -1.12, 0])
        self.play(FadeIn(tl), run_time=0.45)
        note = _t("one galaxy", size=18, color=SOFT).move_to([1.35, -1.22, 0])
        self.play(FadeIn(note), run_time=0.3)

        closer(self, "The point is not the crowd. It is the repeat looks.",
               cx=-0.2, size=30, max_w=9.4)
        self.wait(4.4)


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE TREE  (13.82 s)
# ═════════════════════════════════════════════════════════════════════════════
class B05_Tree(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Not a name. A path.",
               cite="11 tasks in the Galaxy Zoo 2 tree, 2 to 7 answers each · Willett et al. 2013")

        hero = _cutout("hero.png", 2.9, [-4.45, 0.75, 0])
        hlbl = _t("one galaxy", size=20, color=SOFT).move_to([-4.45, -0.98, 0])
        self.play(FadeIn(hero), run_time=0.6)
        self.play(FadeIn(hlbl), run_time=0.3)

        q0 = _quiet_chip("smooth, or features?", size=21).move_to([1.15, 1.95, 0])
        self.play(FadeIn(q0), run_time=0.5)

        a_no = _quiet_chip("smooth", size=19).move_to([-0.55, 0.85, 0])
        a_yes = _chip("features", size=19).move_to([2.75, 0.85, 0])
        e1 = Line([0.55, 1.68, 0], [-0.35, 1.12, 0], color=GHOST, stroke_width=2.2)
        e2 = Line([1.75, 1.68, 0], [2.55, 1.12, 0], color=ACC, stroke_width=3.2)
        self.play(Create(e1), Create(e2), run_time=0.4)
        self.play(FadeIn(a_no), FadeIn(a_yes), run_time=0.45)

        q1 = _quiet_chip("is there a bar?", size=21).move_to([3.55, -0.28, 0])
        e3 = Line([2.90, 0.58, 0], [3.35, -0.02, 0], color=ACC, stroke_width=3.2)
        self.play(Create(e3), run_time=0.3)
        self.play(FadeIn(q1), run_time=0.45)

        q2 = _quiet_chip("how many arms?", size=21).move_to([3.55, -1.48, 0])
        e4 = Line([3.55, -0.56, 0], [3.55, -1.22, 0], color=ACC, stroke_width=3.2)
        self.play(Create(e4), run_time=0.3)
        self.play(FadeIn(q2), run_time=0.45)

        depth = _t("your answer decides the next question", size=20, color=SOFT)
        _fit(depth, 4.3, [-0.30, -1.48, 0])
        self.play(FadeIn(depth), run_time=0.4)

        closer(self, "The label is a path through the tree.", cx=-0.4, size=30)
        self.wait(2.6)


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THE FRAMEWORK  (19.50 s)
# ═════════════════════════════════════════════════════════════════════════════
STATIONS = [
    ("1", "ASK", "one galaxy,\none decision tree"),
    ("2", "TALLY", "many people,\none proportion"),
    ("3", "TRAIN", "a CNN learns\nthe proportion"),
    ("4", "PREDICT", "a fraction for a\ngalaxy nobody saw"),
]
ST_X = [-4.62, -1.54, 1.54, 4.62]


class B06_Framework(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The loop",
               cite="active learning and vote-fraction training: Walmsley et al. 2022")

        groups = []
        for (num, name, sub), cx in zip(STATIONS, ST_X):
            box = _card(2.78, 3.10, [cx, 0.75, 0])
            disc = Circle(radius=0.24, color=ACC, fill_color=ACC,
                          fill_opacity=1.0, stroke_width=0)
            disc.move_to([cx - 1.02, 1.94, 0])
            n = _t(num, size=22, color=CARD).move_to(disc.get_center())
            title = _t(name, size=26, weight="BOLD").move_to([cx + 0.26, 1.94, 0])
            body = _fit(_t(sub, size=19, color=SOFT), 2.42, [cx, -0.42, 0])
            groups.append(VGroup(box, disc, n, title, body))

        for g in groups:
            self.play(FadeIn(g[0]), run_time=0.30)

        # station glyphs live in the band y 0.50 … 1.40, clear of header and body
        glyph_builders = []

        g1 = Group(_cutout("spiral_104.png", 0.86, [ST_X[0] - 0.60, 0.95, 0]))
        tree = VGroup(
            Line([ST_X[0] + 0.30, 1.30, 0], [ST_X[0] + 0.02, 0.98, 0], color=INK, stroke_width=2),
            Line([ST_X[0] + 0.30, 1.30, 0], [ST_X[0] + 0.62, 0.98, 0], color=INK, stroke_width=2),
            Line([ST_X[0] + 0.62, 0.98, 0], [ST_X[0] + 0.40, 0.66, 0], color=INK, stroke_width=2),
            Line([ST_X[0] + 0.62, 0.98, 0], [ST_X[0] + 0.86, 0.66, 0], color=INK, stroke_width=2),
            Dot([ST_X[0] + 0.30, 1.30, 0], radius=0.055, color=INK),
            Dot([ST_X[0] + 0.62, 0.98, 0], radius=0.055, color=INK))
        glyph_builders.append(Group(g1, tree))

        g2 = VGroup()
        for i in range(12):
            g2.add(_mark(ST_X[1] - 0.62 + (i % 6) * 0.25, 1.28 - (i // 6) * 0.28,
                         color=INK, h=0.20, sw=2.4))
        g2.add(_prop_bar([ST_X[1], 0.66, 0], 1.85, 0.63, h=0.26))
        glyph_builders.append(g2)

        g3 = VGroup()
        g3.add(_prop_bar([ST_X[2] - 0.78, 1.16, 0], 0.95, 0.63, h=0.22))
        for i, cnt in enumerate((3, 2)):
            for j in range(cnt):
                g3.add(Dot([ST_X[2] + 0.28 + i * 0.52,
                            1.06 - j * 0.30 - (3 - cnt) * 0.15, 0],
                           radius=0.070, color=INK))
        glyph_builders.append(g3)

        g4 = Group(_cutout("elliptical_302.png", 0.80, [ST_X[3] - 0.62, 1.10, 0]))
        out = VGroup(_prop_bar([ST_X[3] + 0.42, 1.10, 0], 1.10, 0.18, h=0.24),
                     _t("0.18", size=17, color=ACCT).move_to([ST_X[3] + 0.42, 0.66, 0]))
        glyph_builders.append(Group(g4, out))

        for i, g in enumerate(groups):
            self.play(FadeIn(g[1]), FadeIn(g[2]), FadeIn(g[3]), run_time=0.30)
            self.play(FadeIn(glyph_builders[i]), run_time=0.45)
            self.play(FadeIn(g[4]), run_time=0.30)
            if i < 3:
                a = Arrow([ST_X[i] + 1.42, 0.75, 0], [ST_X[i + 1] - 1.42, 0.75, 0],
                          color=INK, stroke_width=3, buff=0.02, tip_length=0.16)
                self.play(GrowArrow(a), run_time=0.26)

        arc = ArcBetweenPoints([ST_X[3], -0.86, 0], [ST_X[0], -0.86, 0],
                               angle=-TAU / 9, color=ACC, stroke_width=5)
        tip = Triangle(color=ACC, fill_color=ACC, fill_opacity=1, stroke_width=0)
        tip.scale(0.13).rotate(PI / 2).move_to([ST_X[0] + 0.06, -0.86, 0])
        self.play(Create(arc), run_time=0.9)
        self.play(FadeIn(tip), run_time=0.22)

        closer(self, "Active learning returns only the galaxies it is unsure about.",
               cx=-0.2, size=28, max_w=9.8)
        self.wait(3.2)


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — WORKED EXAMPLE  (16.19 s)
# ═════════════════════════════════════════════════════════════════════════════
class B07_VoteFraction(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "One galaxy, one fraction",
               cite="the 63/37 split is ILLUSTRATIVE, not a published measurement · method: Walmsley et al. 2022")

        rail_x = [-4.7, -1.6, 1.5, 4.6]
        rail_seg = VGroup(*[Line([a, 2.30, 0], [b, 2.30, 0], color=RULE, stroke_width=2)
                            for a, b in ((-5.70, -5.45), (-3.95, -2.35),
                                         (-0.80, 0.70), (2.40, 3.70), (5.50, 5.62))])
        self.play(Create(rail_seg), run_time=0.3)
        rail = VGroup(*[_quiet_chip(n, size=19).move_to([cx, 2.30, 0])
                        for n, cx in zip(("ASK", "TALLY", "TRAIN", "PREDICT"), rail_x)])
        self.play(LaggedStart(*[FadeIn(c) for c in rail], lag_ratio=0.12),
                  run_time=0.7)

        hero = _cutout("hero.png", 2.7, [-4.40, 0.70, 0])
        self.play(FadeIn(hero), run_time=0.6)
        ring = Ellipse(width=1.35, height=0.60, color=ACC, stroke_width=3.4)
        ring.move_to([-4.40, 0.70, 0])
        self.play(Create(ring), run_time=0.45)
        hl = _t("a faint bar", size=21, color=SOFT).move_to([-4.40, -0.92, 0])
        self.play(FadeIn(hl), run_time=0.35)

        # 100 marks: 63 say bar, 37 do not
        grid = VGroup()
        # column-major: the first 63 marks fill the LEFT columns, so the
        # "63 say bar" / "37 say no bar" labels beneath read left-to-right and
        # match the proportion bar under them. Row-major filled top-down and
        # silently contradicted both.
        for i in range(100):
            x = -1.85 + (i // 10) * 0.30
            y = 1.62 - (i % 10) * 0.30
            grid.add(_mark(x, y, color=ACC if i < 63 else GHOST, h=0.22, sw=3.0,
                           op=1.0 if i < 63 else 0.9))
        self.play(LaggedStart(*[Create(m) for m in grid], lag_ratio=0.008),
                  run_time=1.5)
        g1 = _t("63 say bar", size=20, color=ACCT).move_to([-1.10, -1.32, 0])
        g2 = _t("37 say no bar", size=20, color=SOFT).move_to([0.95, -1.32, 0])
        self.play(FadeIn(g1), FadeIn(g2), run_time=0.4)

        bar = _prop_bar([-0.40, -1.80, 0], 3.0, 0.63)
        self.play(FadeIn(bar), run_time=0.5)

        notlab = _t("barred", size=30).move_to([3.90, 1.42, 0])
        notcap = _t("not the target", size=19, color=SOFT).move_to([3.90, 0.96, 0])
        self.play(FadeIn(notlab), FadeIn(notcap), run_time=0.45)
        self.play(Create(_strike(notlab, pad=0.14)), run_time=0.4)

        target = _t("0.63", size=64, color=ACCT, weight="BOLD")
        target.move_to([3.90, 0.02, 0])
        tcap = _t("the training target", size=21, color=SOFT).move_to([3.90, -0.58, 0])
        self.play(Write(target), run_time=0.7)
        self.play(FadeIn(tcap), run_time=0.35)

        pred = _quiet_chip("network predicts 0.61", size=19).move_to([3.90, -1.32, 0])
        self.play(FadeIn(pred), run_time=0.45)

        closer(self, "The target is a number, not a word.", cx=-0.4, size=31)
        self.wait(1.8)


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — THE DESIGN TELL  (18.94 s)
# ═════════════════════════════════════════════════════════════════════════════
class B08_NoUp(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "A galaxy has no up",
               cite="rotation-invariant architecture, Galaxy Challenge 2014 · Dieleman, Willett & Dambre 2015")

        # Tiles are PRE-rotated in assets/gen_galaxies.py and stay square.
        # Rotating an ImageMobject here would turn each tile into a diamond,
        # desync it from its frame, and overlap its neighbours.
        rots = [0, 45, 90, 135]
        tiles, labels = Group(), VGroup()
        for i, deg in enumerate(rots):
            cx = -4.95 + i * 1.62
            tiles.add(_cutout(f"rot_{deg:03d}.png", 1.44, [cx, 1.52, 0]))
            labels.add(_t(f"{deg}°", size=20, color=SOFT).move_to([cx, 0.58, 0]))

        for t, l in zip(tiles, labels):
            self.play(FadeIn(t, scale=1.05), FadeIn(l), run_time=0.42)

        block = _card(3.4, 1.8, [4.10, 1.52, 0])
        blab = _t("shared weights", size=25, weight="BOLD").move_to([4.10, 1.86, 0])
        bsub = _t("one network, four views", size=19, color=SOFT)
        bsub.move_to([4.10, 1.32, 0])
        self.play(Create(block), run_time=0.5)
        self.play(FadeIn(blab), FadeIn(bsub), run_time=0.4)

        # A bus under the tiles, then ONE arrow into the block — four arrows
        # crossing the tiles was unreadable.
        # The drops start BELOW the degree labels: a stroke running through a
        # label is a GATE B text-on-curve error and reads as a strike-through.
        bus = VGroup()
        for i in range(4):
            cx = -4.95 + i * 1.62
            bus.add(Line([cx, 0.28, 0], [cx, -0.34, 0], color=GHOST, stroke_width=2))
        bus.add(Line([-4.95, -0.34, 0], [1.30, -0.34, 0], color=GHOST, stroke_width=2))
        self.play(LaggedStart(*[Create(m) for m in bus], lag_ratio=0.08),
                  run_time=0.8)
        feed = Arrow([1.30, -0.34, 0], [2.30, 1.30, 0], color=INK,
                     stroke_width=3, buff=0.06, tip_length=0.18)
        self.play(GrowArrow(feed), run_time=0.5)

        ring = RoundedRectangle(width=3.64, height=2.04, corner_radius=0.18,
                                color=ACC, stroke_width=3.4, fill_opacity=0)
        ring.move_to([4.10, 1.52, 0])
        self.play(Create(ring), run_time=0.6)

        note = _fit(_t("rotate the image and the answer must not change",
                       size=24, color=INK), 6.6, [-1.30, -1.00, 0])
        self.play(FadeIn(note), run_time=0.5)
        note2 = _fit(_t("so the symmetry of the problem became structure in the model",
                        size=20, color=SOFT), 7.2, [-0.60, -1.54, 0])
        self.play(FadeIn(note2), run_time=0.45)

        closer(self, "The physics tells the network what to ignore.",
               cx=-0.3, size=30)
        self.wait(4.4)


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — THE RESULT  (16.06 s)
# ═════════════════════════════════════════════════════════════════════════════
class B09_Result(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What it actually delivers",
               cite="~99% on confident volunteer answers: Walmsley et al. 2022 · 8.67M galaxies: Galaxy Zoo DESI · Rubin: ~20 billion over ten years")

        # accuracy dial
        ring_bg = Circle(radius=1.16, color=GHOST, stroke_width=14)
        ring_bg.move_to([-4.55, 1.10, 0])
        self.play(Create(ring_bg), run_time=0.45)
        arc = Arc(radius=1.16, start_angle=PI / 2, angle=-TAU * 0.99,
                  color=ACC, stroke_width=14).move_to(ring_bg.get_center())
        self.play(Create(arc), run_time=1.1)
        pct = _t("99%", size=54, color=ACCT, weight="BOLD")
        pct.move_to([-4.55, 1.18, 0])
        self.play(FadeIn(pct, scale=1.08), run_time=0.5)
        plb = _fit(_t("on confident volunteer answers", size=19, color=SOFT),
                   3.4, [-4.55, -0.36, 0])
        self.play(FadeIn(plb), run_time=0.35)

        # predicted vs actual vote fraction, inside a 5-10% band
        ax_o = np.array([-1.65, -0.62, 0.0])
        span = 2.75
        xa = Line(ax_o, ax_o + np.array([span, 0, 0]), color=INK, stroke_width=2.2)
        ya = Line(ax_o, ax_o + np.array([0, span, 0]), color=INK, stroke_width=2.2)
        self.play(Create(xa), Create(ya), run_time=0.45)
        band = Polygon(ax_o + np.array([0, 0.30, 0]),
                       ax_o + np.array([span - 0.30, span, 0]),
                       ax_o + np.array([span, span, 0]),
                       ax_o + np.array([span, span - 0.30, 0]),
                       ax_o + np.array([0.30, 0, 0]),
                       ax_o + np.array([0, 0, 0]),
                       color=ACC, fill_color=ACC, fill_opacity=0.20,
                       stroke_width=0)
        self.play(FadeIn(band), run_time=0.4)
        rng = np.random.RandomState(4)
        pts = VGroup()
        for _ in range(34):
            u = rng.uniform(0.05, 0.95)
            v = np.clip(u + rng.normal(0, 0.045), 0.02, 0.98)
            pts.add(Dot(ax_o + np.array([u * span, v * span, 0]),
                        radius=0.045, color=INK, fill_opacity=0.8))
        self.play(LaggedStart(*[FadeIn(p) for p in pts], lag_ratio=0.02),
                  run_time=0.9)
        bl = _t("predicted vote fraction vs actual", size=19, color=SOFT)
        _fit(bl, 3.5, [-0.28, -1.02, 0])
        bl2 = _t("inside 5 to 10 percent", size=20, color=ACCT)
        _fit(bl2, 3.2, [-0.28, -1.48, 0])
        self.play(FadeIn(bl), FadeIn(bl2), run_time=0.45)

        # the catalogue
        cnt = _t("8,670,000", size=52, color=ACCT, weight="BOLD")
        cnt.move_to([3.95, 1.55, 0])
        self.play(Write(cnt), run_time=0.9)
        clbl = _fit(_t("galaxies measured this way", size=22, color=SOFT),
                    4.2, [3.95, 0.92, 0])
        self.play(FadeIn(clbl), run_time=0.35)
        div = Line([1.85, 0.42, 0], [6.05, 0.42, 0], color=RULE, stroke_width=2)
        self.play(Create(div), run_time=0.3)
        nxt = _fit(_t("next: Rubin's ten-year survey", size=21, color=INK),
                   4.2, [3.95, -0.02, 0])
        nxt2 = _t("about 20 billion galaxies", size=25, weight="BOLD")
        _fit(nxt2, 4.2, [3.95, -0.58, 0])
        self.play(FadeIn(nxt), run_time=0.35)
        self.play(FadeIn(nxt2), run_time=0.45)

        closer(self, "Accurate against the crowd, at survey scale.",
               cx=-0.4, size=30)
        self.wait(1.8)


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — WHERE IT FAILS  (18.58 s)
# ═════════════════════════════════════════════════════════════════════════════
class B10_Ceilings(Scene):

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Two ceilings",
               cite="domain shift between surveys: arXiv 2412.15533 · the crowd-ceiling is this episode's own inference, not a citation")

        left = _card(5.75, 4.05, [-3.10, 0.42, 0])
        right = _card(5.75, 4.05, [3.10, 0.42, 0])
        self.play(Create(left), Create(right), run_time=0.6)

        h1 = _t("It predicts people", size=27, weight="BOLD").move_to([-3.10, 2.02, 0])
        h2 = _t("It does not travel", size=27, weight="BOLD").move_to([3.10, 2.02, 0])
        self.play(FadeIn(h1), FadeIn(h2), run_time=0.4)

        # LEFT: crowd and model agree with each other, and both miss the truth
        axis = Line([-5.55, 0.62, 0], [-0.65, 0.62, 0], color=INK, stroke_width=2.4)
        self.play(Create(axis), run_time=0.35)
        crowd = Dot([-4.15, 0.62, 0], radius=0.11, color=INK)
        model = Dot([-3.95, 0.62, 0], radius=0.11, color=ACC)
        truth = Dot([-1.55, 0.62, 0], radius=0.11, color=INK)
        cl = _t("crowd", size=19, color=SOFT).move_to([-4.42, 1.10, 0])
        ml = _t("model", size=19, color=ACCT).move_to([-3.72, 0.16, 0])
        tl = _t("truth", size=19, color=SOFT).move_to([-1.55, 1.10, 0])
        self.play(FadeIn(crowd), FadeIn(cl), run_time=0.35)
        self.play(FadeIn(model), FadeIn(ml), run_time=0.35)
        self.play(FadeIn(truth), FadeIn(tl), run_time=0.35)
        brk = VGroup(
            Line([-3.95, -0.28, 0], [-1.55, -0.28, 0], color=ACC, stroke_width=3.2),
            Line([-3.95, -0.28, 0], [-3.95, -0.10, 0], color=ACC, stroke_width=3.2),
            Line([-1.55, -0.28, 0], [-1.55, -0.10, 0], color=ACC, stroke_width=3.2))
        self.play(Create(brk), run_time=0.5)
        lnote = _fit(_t("it cannot be more right than the crowd", size=21,
                        color=ACCT), 5.2, [-3.10, -0.78, 0])
        self.play(FadeIn(lnote), run_time=0.45)
        lnote2 = _fit(_t("where the crowd is wrong, it is wrong with them",
                         size=19, color=SOFT), 5.2, [-3.10, -1.28, 0])
        self.play(FadeIn(lnote2), run_time=0.4)

        # RIGHT: same sky, different telescope, different pixel distribution
        # The SAME galaxy as two different instruments record it: survey B is
        # shallower and coarser. Showing one image twice would have illustrated
        # nothing — the whole claim is that the pixels differ.
        a = _cutout("spiral_103.png", 1.55, [1.70, 0.88, 0])
        b = _cutout("spiral_103_shallow.png", 1.55, [4.50, 0.88, 0])
        self.play(FadeIn(a), run_time=0.4)
        self.play(FadeIn(b), run_time=0.4)
        al = _t("survey A  ·  deep", size=19, color=SOFT).move_to([1.70, -0.10, 0])
        bl = _t("survey B  ·  shallow", size=19, color=SOFT).move_to([4.50, -0.10, 0])
        self.play(FadeIn(al), FadeIn(bl), run_time=0.3)
        arrow = Arrow([2.55, 0.88, 0], [3.65, 0.88, 0], color=INK,
                      stroke_width=3, buff=0.05, tip_length=0.16)
        self.play(GrowArrow(arrow), run_time=0.35)
        x = VGroup(Line([2.88, 1.12, 0], [3.32, 0.64, 0], color=ACC, stroke_width=4.4),
                   Line([2.88, 0.64, 0], [3.32, 1.12, 0], color=ACC, stroke_width=4.4))
        self.play(Create(x), run_time=0.4)
        rnote = _fit(_t("distributional mismatch", size=21, color=ACCT),
                     5.2, [3.10, -0.78, 0])
        self.play(FadeIn(rnote), run_time=0.4)
        rnote2 = _fit(_t("trained on one telescope, it does not transfer to the next",
                         size=19, color=SOFT), 5.35, [3.10, -1.28, 0])
        self.play(FadeIn(rnote2), run_time=0.4)

        closer(self, "It predicts people, not truth.", cx=-0.4, size=31)
        self.wait(2.6)
