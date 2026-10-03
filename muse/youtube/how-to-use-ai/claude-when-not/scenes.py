"""
iso_kit.py — the show-tell drawing kit. PASTE this block at the top of a reel's scenes.py;
do not import it (Gate A copies only scenes.py into its sandbox).

Drawn isometric objects in the Claude palette: cardboard boxes (closed, open, taped), dark
MCP blocks with ports, flat skill pages, server stacks with lights, checks, a cursor, pills.
Pacing helpers read the reel's beat_sheet.json so scenes wait for their spoken phrase.

Every rule in ../SKILL.md "DRAWING LAWS" is already obeyed by these primitives; keep it that
way when you add one (label beside, never inside; terracotta never under text; dim greys
with gaps for chart blocks; type floor 32).
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ═════════════════════════════ ISO KIT (show-tell) ═════════════════════════════
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"          # kraft cardboard: top, left face, right face (deep enough for Gate V contrast)
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"     # inside walls + floor
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"        # MCP / server blocks
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"         # skill pages
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"                # chart segments, dim to ghost
SERIF = "EB Garamond"
C30 = 0.8660254
config.background_color = STAGE


def T(s, size=36, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")


class Iso:
    """Isometric projection: x runs right-up, y runs left-up, z runs up. (ox, oy) is where (0,0,0) lands."""
    def __init__(self, ox=0.0, oy=0.0, s=1.0):
        self.ox, self.oy, self.s = ox, oy, s

    def p(self, x, y, z=0.0):
        return np.array([self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * 0.5 * self.s + z * self.s, 0.0])

    def v(self, dx, dy, dz=0.0):
        return self.p(dx, dy, dz) - self.p(0, 0, 0)

    def quad(self, pts, fill, stroke=INK, sw=4):
        return Polygon(*[self.p(*q) for q in pts], fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)

    def box(self, x0, y0, z0, w, d, h, top=BOX_TOP, left=BOX_L, right=BOX_R, sw=4):
        """Closed box: the two front faces (x = x0 and y = y0) plus the top."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
        """(back, front): floor + inner back walls, then the front walls. Put contents between them."""
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        back = VGroup(
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], BOX_FLOOR),
            self.quad([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], BOX_IN1),
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], BOX_IN2))
        front = VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], BOX_L),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], BOX_R))
        back.set_z_index(0); front.set_z_index(2)
        return back, front

    def tape(self, x0, y0, z1, w, d, drop=0.35, t=0.22):
        """Terracotta tape across the top (along x) and down the left front face."""
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        """Dark MCP block with two light ports on its right front face."""
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        """A skill page lying flat: white slab, three ghost text lines, one terracotta dot."""
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        """A stack of dark server slabs; returns (stack, lights) — lights start ghost, turn terracotta."""
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    """Quadratic ease-in (things dropping into a box). Local: Gate A's stub has no ease_in_quad."""
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


# ═════════════════════════════ pacing (narration is the clock) ═════════════════════════════
try:
    _SHEET = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}


def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0


def until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured audio)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)


def finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ═════════════════════════════ FILM: "Claude, When Not." ═════════════════════
# show-tell style. The film's cast: a ladder (the thing you are learning to
# climb), a figure (you), a scaffold frame (AI as support), a crutch (AI as
# replacement), and pages (the work). The same objects recur every beat.
# All coordinates stay inside ±6.2 × ±3.3 (safe area). Type floor 32.
# Classes are named <BEATID>_Name so run.sh finds them.

config.pixel_width = 1920
config.pixel_height = 1080


def person(x, y, s=1.0, color=INK, lean=0.0):
    """Simple figure: head, torso, legs, one arm. lean shifts the head sideways."""
    g = VGroup()
    g.add(Circle(radius=0.28 * s, fill_color=color, fill_opacity=1,
                 stroke_width=0).move_to([x + lean, y + 0.62 * s, 0]))
    g.add(Line([x, y + 0.36 * s, 0], [x + lean * 0.6, y - 0.45 * s, 0],
               color=color, stroke_width=10))
    g.add(Line([x + lean * 0.6, y - 0.45 * s, 0],
               [x - 0.28 * s + lean * 0.6, y - 1.05 * s, 0],
               color=color, stroke_width=8))
    g.add(Line([x + lean * 0.6, y - 0.45 * s, 0],
               [x + 0.28 * s + lean * 0.6, y - 1.05 * s, 0],
               color=color, stroke_width=8))
    g.add(Line([x, y + 0.2 * s, 0], [x + 0.4 * s + lean, y - 0.2 * s, 0],
               color=color, stroke_width=8))
    return g


def ladder(x, y, w=1.6, h=4.4, rungs=6):
    """Kraft ladder, ink outlines: the skill you are building."""
    g = VGroup()
    for sx in (-w / 2, w / 2):
        g.add(Rectangle(width=0.24, height=h, fill_color=BOX_L, fill_opacity=1,
                        stroke_color=INK, stroke_width=3).move_to([x + sx, y, 0]))
    for i in range(rungs):
        ry = y - h / 2 + 0.55 + i * (h - 1.1) / (rungs - 1)
        g.add(Rectangle(width=w - 0.12, height=0.17, fill_color=BOX_R,
                        fill_opacity=1, stroke_color=INK,
                        stroke_width=2).move_to([x, ry, 0]))
    return g


def scaffold(x, y, w=3.6, h=5.2):
    """DIM grey frame around the ladder: AI as support, never the climb."""
    g = VGroup()
    for sx in (-w / 2, w / 2):
        g.add(Line([x + sx, y - h / 2, 0], [x + sx, y + h / 2, 0],
                   color=DIM, stroke_width=8))
    for f in (0.15, 0.5, 0.85):
        g.add(Line([x - w / 2, y - h / 2 + f * h, 0],
                   [x + w / 2, y - h / 2 + f * h, 0], color=DIM, stroke_width=6))
    return g


def crutch(x, y, s=1.0):
    """INK crutch with one terracotta tip dot: AI doing the work instead."""
    g = VGroup()
    g.add(Line([x, y + 1.05 * s, 0], [x, y - 1.25 * s, 0],
               color=INK, stroke_width=11))
    g.add(Line([x - 0.48 * s, y + 1.05 * s, 0], [x + 0.48 * s, y + 1.05 * s, 0],
               color=INK, stroke_width=13))
    g.add(Line([x - 0.32 * s, y + 0.3 * s, 0], [x + 0.32 * s, y + 0.3 * s, 0],
               color=INK, stroke_width=8))
    g.add(Dot([x, y - 1.32 * s, 0], radius=0.1 * s, color=TERRA))
    return g


def page(x, y, w=3.4, h=2.6, lines=3, line_color=GHOST):
    """A work page: card with ghost text lines and one terracotta dot."""
    g = VGroup()
    g.add(RoundedRectangle(corner_radius=0.18, width=w, height=h,
                           fill_color=CARD, fill_opacity=1, stroke_color=INK,
                           stroke_width=3).move_to([x, y, 0]))
    for i in range(lines):
        ly = y + h / 2 - 0.55 - i * 0.55
        g.add(Line([x - w / 2 + 0.5, ly, 0], [x + w / 2 - 0.5, ly, 0],
                   color=line_color, stroke_width=7))
    g.add(Dot([x - w / 2 + 0.5, y - h / 2 + 0.45, 0], radius=0.09, color=TERRA))
    return g


class BIDEA_HesitantWriter(Scene):
    """The naive question, struck through, corrected into the real one."""

    def construct(self):
        paper = RoundedRectangle(corner_radius=0.25, width=8.6, height=4.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=4).move_to([0, 0.1, 0])
        naive = T("let AI do everything for me", size=40, color=DIM).move_to([0, 1.1, 0])
        strike = Line([-2.8, 1.1, 0], [2.8, 1.1, 0], color=INK, stroke_width=7)
        real = T("learn when NOT to use it", size=48, color=INK, bold=True).move_to([0, -0.9, 0])
        tag = T("the real question", size=32, color=DIM).move_to([0, -2.15, 0])
        ok = check(4.9, -0.9, s=0.24, color=TERRA, w=10)

        self.play(FadeIn(paper), run_time=0.8)
        until(self, "naive version")
        self.play(Write(naive), run_time=0.9)
        self.play(Create(strike), run_time=0.5)
        until(self, "real one")
        self.play(Write(real), run_time=1.0)
        until(self, "whole film")
        self.play(FadeIn(tag), Create(ok), run_time=0.7)
        finish(self)


class BDEFS_Terms(Scene):
    """Four terms, one line each, on cards in a row."""

    def construct(self):
        terms = [
            ("scaffold", "a support that\nhelps you climb"),
            ("crutch", "a prop that does\nthe work for you"),
            ("hallucination", "AI invents a fact,\nsounds confident"),
            ("disclosure", "saying plainly\nwhere AI helped"),
        ]
        phrases = ["scaffold is", "crutch is", "hallucination is", "disclosure just"]
        for i, ((word, defi), ph) in enumerate(zip(terms, phrases)):
            x = -5.4 + i * 3.6
            card = RoundedRectangle(corner_radius=0.2, width=3.2, height=2.8,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([x, 0, 0])
            wt = T(word, size=38, color=INK, bold=True).move_to([x, 0.75, 0])
            dt = T(defi, size=32, color=INK).move_to([x, -0.55, 0])
            grp = VGroup(card, wt, dt)
            until(self, ph)
            self.play(FadeIn(grp, shift=UP * 0.3), run_time=0.7)
        finish(self)


class B01_Thesis(Scene):
    """The ladder; the figure climbs; the check lands at the top."""

    def construct(self):
        lad = ladder(-3.0, 0.0)
        fig = person(-3.0, -1.7)
        ok = check(-3.0, 2.75, s=0.26, color=TERRA, w=10)
        lab = T("the real skill", size=36, color=INK).move_to([3.2, 1.6, 0])
        leader = Line([1.2, 1.6, 0], [-2.2, 2.4, 0], color=DIM, stroke_width=4)

        self.play(FadeIn(lad), run_time=0.8)
        until(self, "real AI skill")
        self.play(FadeIn(fig, shift=UP * 0.4), run_time=0.7)
        until(self, "knowing when not to use it")
        self.play(Create(ok), run_time=0.6)
        until(self, "hangs off that one line")
        self.play(FadeIn(lab), Create(leader), run_time=0.7)
        finish(self)


class B02_UseList(Scene):
    """Scaffold draws around the ladder; five rungs light up, one per use."""

    def construct(self):
        lad = ladder(-1.2, 0.0, h=4.4)
        scaf = scaffold(-1.2, 0.0)
        dots = VGroup()
        for i in range(5):
            ry = -2.2 + 0.55 + i * (4.4 - 1.1) / 5 + 0.33
            dots.add(Dot([-1.2, ry, 0], radius=0.14, color=TERRA))
        lab = T("scaffold", size=40, color=INK, bold=True).move_to([3.6, 1.4, 0])
        leader = Line([2.3, 1.4, 0], [0.7, 1.0, 0], color=DIM, stroke_width=4)

        self.play(FadeIn(lad), run_time=0.8)
        until(self, "leverage")
        self.play(Create(scaf), run_time=1.0)
        for d, ph in zip(dots, ["Quiz yourself", "Get feedback", "explain",
                                "practice problems", "Plan and schedule"]):
            until(self, ph)
            self.play(GrowFromCenter(d), run_time=0.4)
        until(self, "That is a scaffold")
        self.play(FadeIn(lab), Create(leader), run_time=0.7)
        finish(self)


class B03_DontList(Scene):
    """The figure leans on a crutch; a page slips; the line is drawn."""

    def construct(self):
        cru = crutch(2.6, 0.2)
        fig = person(1.1, -0.5, lean=0.55)
        pg = page(-2.6, -0.6, w=3.0, h=2.2, lines=2)
        xmark = Cross(scale_factor=0.45, color=INK).move_to([-2.6, -0.6, 0])
        lab = T("crutch", size=40, color=INK, bold=True).move_to([-4.6, 2.2, 0])

        self.play(FadeIn(cru), run_time=0.8)
        until(self, "Do not use it")
        self.play(FadeIn(fig, shift=RIGHT * 0.3), run_time=0.7)
        until(self, "first draft")
        self.play(FadeIn(pg), run_time=0.6)
        until(self, "facts you will not check")
        self.play(Create(xmark), run_time=0.5)
        until(self, "That last one")
        self.play(FadeIn(lab), run_time=0.6)
        finish(self)


class B04_HideTest(Scene):
    """A page held openly; a second page slides behind the back; the ring finds it."""

    def construct(self):
        fig = person(-2.8, -0.6)
        open_pg = page(-2.8, 0.9, w=2.6, h=1.9, lines=2)
        hid_pg = page(-0.9, -1.4, w=2.4, h=1.7, lines=2)
        ring = Circle(radius=1.45, color=TERRA, stroke_width=9,
                      fill_opacity=0).move_to([-0.9, -1.4, 0])
        ok = check(-2.8, 2.15, s=0.22, color=TERRA, w=9)
        lab = T("the signal", size=36, color=INK).move_to([3.4, -1.4, 0])
        leader = Line([2.3, -1.4, 0], [0.6, -1.4, 0], color=DIM, stroke_width=4)

        self.play(FadeIn(fig), FadeIn(open_pg), run_time=0.9)
        until(self, "Would you hide")
        self.play(FadeIn(hid_pg, shift=LEFT * 0.6), run_time=0.8)
        until(self, "do not do it")
        self.play(Create(ring), run_time=0.7)
        until(self, "hiding means")
        self.play(Create(ok), FadeIn(lab), Create(leader), run_time=0.8)
        finish(self)


class B05_DraftExample(Scene):
    """Draft lines draw themselves; the crutch arrives; the strike falls."""

    def construct(self):
        pg = page(-2.2, 0.2, w=4.0, h=3.0, lines=0)
        lines = VGroup()
        for i in range(4):
            ly = 1.25 - i * 0.62
            lines.add(Line([-3.7, ly, 0], [-0.7, ly, 0], color=INK, stroke_width=7))
        cru = crutch(3.4, 0.0)
        strike = Line([-3.9, 0.2, 0], [-0.5, 0.2, 0], color=INK, stroke_width=9)
        lab = T("drafting = thinking", size=34, color=INK).move_to([0, -2.5, 0])

        self.play(FadeIn(pg), run_time=0.7)
        until(self, "Take drafting")
        for ln in lines:
            self.play(Create(ln), run_time=0.35)
        until(self, "Reading a finished draft")
        self.play(FadeIn(cru, shift=LEFT * 0.4), run_time=0.7)
        until(self, "Writing it")
        self.play(Create(strike), FadeIn(lab), run_time=0.7)
        finish(self)


class B06_Verify(Scene):
    """A page of ghost lines; the magnifier sweeps; the check lands."""

    def construct(self):
        pg = page(-1.4, 0.0, w=4.2, h=3.0, lines=3)
        lens = Circle(radius=0.95, color=INK, stroke_width=8,
                      fill_opacity=0).move_to([-2.4, 0.4, 0])
        handle = Line([-1.75, -0.25, 0], [-0.9, -1.1, 0], color=INK, stroke_width=9)
        ok = check(2.9, 1.6, s=0.26, color=TERRA, w=10)
        lab = T("check it", size=36, color=INK).move_to([2.9, 0.5, 0])

        self.play(FadeIn(pg), run_time=0.8)
        until(self, "Or take facts")
        self.play(FadeIn(lens), run_time=0.6)
        until(self, "hallucination")
        self.play(Create(handle), run_time=0.5)
        until(self, "you checked")
        self.play(Create(ok), FadeIn(lab), run_time=0.7)
        finish(self)


class B07_Predict(Scene):
    """Four option cards; commit before the answer."""

    def construct(self):
        opts = [("A", "quiz"), ("B", "write"), ("C", "explain"), ("D", "feedback")]
        cards = VGroup()
        for i, (letter, word) in enumerate(opts):
            x = -5.25 + i * 3.5
            card = RoundedRectangle(corner_radius=0.18, width=3.0, height=2.4,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([x, 0.2, 0])
            lt = T(letter, size=52, color=INK, bold=True).move_to([x, 0.85, 0])
            wt = T(word, size=34, color=INK).move_to([x, -0.55, 0])
            cards.add(VGroup(card, lt, wt))
        cur = cursor(4.4, 2.5)

        for c, ph in zip(cards, ["A: quiz", "B: write", "C: explain", "D: give"]):
            until(self, ph)
            self.play(FadeIn(c, shift=UP * 0.25), run_time=0.55)
        until(self, "Pick it now")
        self.play(FadeIn(cur), run_time=0.5)
        finish(self)


class B08_Answer(Scene):
    """B slides away; checks land on A, C, D; the ladder stands under them."""

    def construct(self):
        lad = ladder(-4.6, -0.6, w=1.3, h=3.6, rungs=5)
        opts = [("A", "quiz"), ("B", "write"), ("C", "explain"), ("D", "feedback")]
        cards, checks = VGroup(), VGroup()
        b_card = None
        for i, (letter, word) in enumerate(opts):
            x = -4.35 + i * 2.9
            card = RoundedRectangle(corner_radius=0.16, width=2.6, height=2.1,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([x, 0.9, 0])
            lt = T(letter, size=46, color=INK, bold=True).move_to([x, 1.45, 0])
            wt = T(word, size=32, color=INK).move_to([x, 0.25, 0])
            grp = VGroup(card, lt, wt)
            cards.add(grp)
            if letter == "B":
                b_card = grp
            else:
                checks.add(check(x, 2.35, s=0.2, color=TERRA, w=9))
        lab = T("scaffold uses", size=34, color=INK).move_to([2.9, -2.2, 0])

        self.play(FadeIn(lad), FadeIn(cards), run_time=1.0)
        until(self, "It is B")
        self.play(FadeOut(b_card, shift=DOWN * 0.6), run_time=0.7)
        until(self, "A, C, and D")
        for ck in checks:
            self.play(Create(ck), run_time=0.35)
        until(self, "Claude stays a tool")
        self.play(FadeIn(lab), run_time=0.6)
        finish(self)


class B09_Line(Scene):
    """The line, drawn: scaffold on the left, crutch on the right."""

    def construct(self):
        divider = Line([0, -2.7, 0], [0, 2.7, 0], color=INK, stroke_width=7)
        lad = ladder(-3.4, -0.2, w=1.5, h=3.8, rungs=5)
        fig = person(-3.4, -1.5, s=0.9)
        cru = crutch(3.4, -0.2)
        ok = check(-4.6, 1.9, s=0.24, color=TERRA, w=10)
        lab_l = T("leverage", size=36, color=INK).move_to([-3.4, -2.75, 0])
        lab_r = T("instead of you", size=34, color=INK).move_to([3.4, -2.75, 0])

        self.play(Create(divider), run_time=0.7)
        until(self, "draw the line here")
        self.play(FadeIn(lad), FadeIn(fig), run_time=0.8)
        until(self, "in place of the thing")
        self.play(FadeIn(cru), run_time=0.7)
        until(self, "Scaffold, not crutch")
        self.play(Create(ok), FadeIn(lab_l), FadeIn(lab_r), run_time=0.7)
        finish(self)


class BHTF_YourTurn(Scene):
    """The drawn composer: the prompt types in, two checks land."""

    def construct(self):
        win = RoundedRectangle(corner_radius=0.25, width=8.4, height=4.9,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=4).move_to([0, -0.1, 0])
        band = Rectangle(width=8.4, height=0.85, fill_color=BAR1, fill_opacity=1,
                         stroke_width=0).move_to([0, 1.925, 0])
        head = T("Claude", size=36, color=INK, bold=True).move_to([-3.5, 1.925, 0])
        l1 = T("list five things I use you for each week", size=32, color=INK).move_to([0, 0.9, 0])
        l2 = T("run each through the hide-it test", size=32, color=INK).move_to([0, 0.1, 0])
        l3 = T("mark each one scaffold or crutch", size=32, color=INK).move_to([0, -0.7, 0])
        ok1 = check(-3.4, -1.9, s=0.2, color=TERRA, w=9)
        c1 = T("your gut", size=32, color=INK).move_to([-2.2, -1.9, 0])
        ok2 = check(0.6, -1.9, s=0.2, color=TERRA, w=9)
        c2 = T("the laptop test", size=32, color=INK).move_to([2.2, -1.9, 0])

        self.play(FadeIn(win), FadeIn(band), FadeIn(head), run_time=0.9)
        until(self, "Your turn")
        self.play(Write(l1), run_time=0.7)
        until(self, "hide-it test")
        self.play(Write(l2), run_time=0.7)
        until(self, "Mark each one")
        self.play(Write(l3), run_time=0.7)
        until(self, "your own checks")
        self.play(Create(ok1), FadeIn(c1), Create(ok2), FadeIn(c2), run_time=0.8)
        finish(self)


class BOUT_Outro(Scene):
    """Spoken outro: title, watermark, one terracotta dot."""

    def construct(self):
        title = T("Claude, When Not.", size=72, color=INK, bold=True).move_to([0, 0.5, 0])
        handle = T("@NikBearBrown", size=40, color=DIM).move_to([0, -1.1, 0])
        dot = Dot([0, -2.0, 0], radius=0.12, color=TERRA)

        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(handle), run_time=0.6)
        self.play(GrowFromCenter(dot), run_time=0.4)
        finish(self)
