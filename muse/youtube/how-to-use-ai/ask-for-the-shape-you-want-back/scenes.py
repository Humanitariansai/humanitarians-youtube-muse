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
"""
Body scenes for "Ask for the Shape You Want Back" (How to AI #4).
Show-tell style: one isometric drawing per beat on a cream stage, minimal
labels (ink, >=32pt, beside objects, leader-line gap), terracotta only for
tape/dots/checks/scan line. Class names are literal `class BNN_Name(Scene):`
so run.sh finds them; helpers attach after the class line.
until()/finish() read beat_sheet.json in this folder (the measured audio clock).
"""

def shadow(x, y, w=3.2, h=0.5):
    return Ellipse(width=w, height=h, fill_color=DIM, fill_opacity=0.30, stroke_width=0).move_to([x, y, 0])

def lbl(text, x, y, size=38):
    return T(text, size=size, color=INK).move_to([x, y, 0])

def leader(x0, y0, x1, y1):
    return Line([x0, y0, 0], [x1, y1, 0], color=DIM, stroke_width=3)

class B00_BlocksBox(Scene):
    def construct(self):
        iso = Iso(ox=-2.6, oy=-0.9, s=1.0)
        back, front = iso.open_box(0, 0, 0, 2.6, 2.6, 1.4)
        self.add(shadow(-2.6, -2.5))
        self.play(Create(back), Create(front), run_time=1.2)
        blocks = VGroup(*[iso.box(0.25 + 1.25 * (i % 2), 0.25 + 1.25 * (i // 2), 0.05, 1.1, 1.1, 0.55,
                                   top=c, left=c, right=c)
                          for i, c in enumerate([BAR1, BAR2, BAR3, GHOST])])
        self.play(GrowFromCenter(blocks[0]), GrowFromCenter(blocks[1]), run_time=1.6, rate_func=ease_in)
        until(self, "Your prompt decides")
        self.play(GrowFromCenter(blocks[2]), GrowFromCenter(blocks[3]), run_time=1.6, rate_func=ease_in)
        lab = lbl("the facts", 1.6, 0.6)
        until(self, "Same facts, any shape")
        self.play(FadeIn(lab), run_time=0.8)
        until(self, "how to ask for the one you actually need")
        finish(self)

class B01_BuriedInProse(Scene):
    def construct(self):
        iso = Iso(ox=0, oy=0, s=1.0)
        slab = iso.box(-2.6, -2.2, 0, 3.4, 3.2, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        lines = VGroup(*[Line(iso.p(-2.4, -2.2 + 3.2 * f, 0.07), iso.p(0.8, -2.2 + 3.2 * f, 0.07),
                              color=GHOST, stroke_width=4)
                         for f in (0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90)])
        self.add(shadow(0, -2.9, w=4.2))
        self.play(Create(slab), run_time=1.4)
        until(self, "answers in prose")
        self.play(FadeIn(lines), run_time=1.6)
        dot = Dot(iso.p(0.2, -0.4, 0.1), radius=0.11, color=TERRA)
        lab = lbl("buried", 3.4, 0.4)
        lead = leader(2.2, -0.1, 3.0, 0.3)
        until(self, "it is buried")
        self.play(FadeIn(dot), FadeIn(lab), FadeIn(lead), run_time=1.2)
        until(self, "the price hides")
        scan = Line(iso.p(-2.4, 0.6, 0.1), iso.p(1.0, 0.6, 0.1), color=TERRA, stroke_width=6)
        self.play(Create(scan), run_time=0.8)
        scan2 = Line(iso.p(-2.4, -0.5, 0.1), iso.p(1.0, -0.5, 0.1), color=TERRA, stroke_width=6)
        self.play(Transform(scan, scan2), run_time=0.9)
        until(self, "the one number you came for")
        finish(self)

class B02_AskForATable(Scene):
    def construct(self):
        ask = pill(0, 2.6, 7.0)
        askt = T("table: price, battery, weight", size=40, color=INK).move_to([0, 2.6, 0])
        self.play(FadeIn(ask), FadeIn(askt), run_time=1.4)
        card = RoundedRectangle(width=6.4, height=3.4, corner_radius=0.25, fill_color=CARD,
                                fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0, -0.4, 0])
        band = Rectangle(width=5.9, height=0.8, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([0, 0.9, 0])
        until(self, "compare the two laptops in a table")
        self.play(Create(card), Create(band), run_time=1.4)
        heads = VGroup(*[T(h, size=38, color=INK).move_to([-2.1 + 2.1 * i, 0.9, 0])
                         for i, h in enumerate(["price", "battery", "weight"])])
        rows = VGroup(*[RoundedRectangle(width=5.8, height=0.55, corner_radius=0.2, fill_color=c,
                                         fill_opacity=1, stroke_width=0).move_to([0, -0.1 - 0.75 * i, 0])
                        for i, c in enumerate([BAR3, "#E7E2D6", BAR3])])
        self.play(FadeIn(heads), run_time=1.0)
        self.play(GrowFromEdge(rows[0], LEFT), GrowFromEdge(rows[1], LEFT), GrowFromEdge(rows[2], LEFT), run_time=1.6)
        until(self, "finds the winner")
        ck = check(-2.9, -1.6, s=0.28, color=TERRA, w=9)
        wlab = lbl("the winner", 3.9, -1.6)
        self.play(GrowFromCenter(ck), FadeIn(wlab), run_time=1.2)
        finish(self)

class B03_GiveItASize(Scene):
    def construct(self):
        iso = Iso(ox=0, oy=0, s=1.0)
        slab = iso.box(-1.8, -2.6, 0, 3.6, 4.2, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        upper = VGroup(*[Line(iso.p(-1.6, -2.6 + 4.2 * f, 0.07), iso.p(1.6, -2.6 + 4.2 * f, 0.07),
                              color=GHOST, stroke_width=4) for f in (0.88, 0.78, 0.68, 0.58, 0.48)])
        lower = VGroup(*[Line(iso.p(-1.6, -2.6 + 4.2 * f, 0.07), iso.p(1.6, -2.6 + 4.2 * f, 0.07),
                              color=GHOST, stroke_width=4) for f in (0.36, 0.26, 0.16, 0.06)])
        self.add(shadow(0, -3.2, w=4.4))
        self.play(Create(slab), FadeIn(upper), FadeIn(lower), run_time=1.8)
        until(self, "keep it under a hundred words")
        cnt = T("340", size=110, color=INK, bold=True).move_to([3.4, 0.6, 0])
        lab = lbl("under 100 words", 3.4, -0.8)
        self.play(FadeIn(cnt), FadeIn(lab), run_time=1.2)
        until(self, "shrinks to the short one")
        trim = Line(iso.p(-1.9, -1.1, 0.1), iso.p(1.9, -1.1, 0.1), color=INK, stroke_width=7)
        self.play(Create(trim), run_time=0.8)
        self.play(FadeOut(lower), run_time=1.0)
        cnt96 = T("96", size=110, color=INK, bold=True).move_to([3.4, 0.6, 0])
        self.play(FadeOut(cnt), FadeIn(cnt96), run_time=0.8)
        until(self, "You set the budget")
        finish(self)

class B04_PickTheTone(Scene):
    def construct(self):
        iso = Iso(ox=0, oy=0, s=1.0)
        p1 = iso.page(-4.9, -1.4, 0, w=2.6, d=2.4)
        p2 = iso.page(2.3, -1.4, 0, w=2.6, d=2.4)
        self.add(shadow(-2.6, -2.6, w=3.0), shadow(2.6, -2.6, w=3.0))
        self.play(Create(p1[0]), FadeIn(p1[1]), Create(p2[0]), FadeIn(p2[1]), run_time=1.8)
        until(self, "Write this as a friendly email")
        l1 = lbl("friendly email", -2.6, 1.9)
        l2 = lbl("formal letter", 2.6, 1.9)
        self.play(FadeIn(l1), FadeIn(l2), run_time=1.2)
        until(self, "which suit to put on")
        ck = check(-3.6, -0.4, s=0.34, color=TERRA, w=10)
        self.play(GrowFromCenter(ck), run_time=1.0)
        until(self, "only if you say so")
        finish(self)

class B05_MatchTheDestination(Scene):
    def construct(self):
        phone = RoundedRectangle(width=2.2, height=3.6, corner_radius=0.35, fill_color=CARD,
                                 fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-4.2, -0.3, 0])
        rep = RoundedRectangle(width=3.0, height=3.6, corner_radius=0.15, fill_color=CARD,
                               fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0, -0.3, 0])
        code = RoundedRectangle(width=3.0, height=3.6, corner_radius=0.15, fill_color=CARD,
                                fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([4.2, -0.3, 0])
        self.add(shadow(-4.2, -2.4, w=2.6), shadow(0, -2.4, w=3.2), shadow(4.2, -2.4, w=3.2))
        self.play(Create(phone), Create(rep), Create(code), run_time=1.6)
        until(self, "read on your phone")
        l1 = lbl("phone", -4.2, 2.0); l2 = lbl("report", 0, 2.0); l3 = lbl("code", 4.2, 2.0)
        self.play(FadeIn(l1), FadeIn(l2), FadeIn(l3), run_time=1.2)
        until(self, "A school report")
        bullets = VGroup(*[Dot([-4.2, 0.5 - 0.55 * i, 0], radius=0.09, color=INK) for i in range(3)])
        head = Rectangle(width=2.2, height=0.4, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([0, 0.9, 0])
        self.play(GrowFromCenter(bullets), GrowFromEdge(head, LEFT), run_time=1.2)
        until(self, "written in curly braces")
        brace = T("{", size=130, color=INK).move_to([3.4, 0.7, 0])
        jlines = VGroup(*[Line([3.9, 0.1 - 0.4 * i, 0], [5.1, 0.1 - 0.4 * i, 0], color=GHOST, stroke_width=5)
                          for i in range(3)])
        self.play(FadeIn(brace), FadeIn(jlines), run_time=1.2)
        finish(self)

class B06_Prefill(Scene):
    def construct(self):
        iso = Iso(ox=0, oy=0, s=1.0)
        page = iso.page(-2.4, -2.2, 0, w=4.8, d=3.4)
        self.add(shadow(0, -3.0, w=5.2))
        self.play(Create(page[0]), run_time=1.4)
        until(self, "its API")
        brace = T("{", size=120, color=INK).move_to([-1.5, 0.9, 0])
        self.play(FadeIn(brace), run_time=1.0)
        until(self, "an opening curly brace")
        jlines = VGroup(*[Line([-0.9, 0.9 - 0.45 * i, 0], [1.9, 0.9 - 0.45 * i, 0], color=GHOST, stroke_width=5)
                          for i in range(4)])
        self.play(FadeIn(jlines), run_time=1.4)
        until(self, "document this trick as prefilling")
        dot = Dot([2.15, -0.9, 0], radius=0.1, color=TERRA)
        lab = lbl("prefill", 3.6, 1.2)
        lead = leader(2.5, 0.9, 3.2, 1.1)
        self.play(FadeIn(dot), FadeIn(lab), FadeIn(lead), run_time=1.2)
        finish(self)

class B07_CheckTheFacts(Scene):
    def construct(self):
        card = RoundedRectangle(width=5.6, height=3.0, corner_radius=0.25, fill_color=CARD,
                                fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-1.2, -0.2, 0])
        band = Rectangle(width=5.2, height=0.7, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([-1.2, 0.95, 0])
        heads = VGroup(*[T(h, size=36, color=INK).move_to([-2.9 + 1.7 * i, 0.95, 0]) for i, h in enumerate(["a", "b", "c"])])
        rows = VGroup(*[RoundedRectangle(width=5.0, height=0.5, corner_radius=0.2, fill_color=BAR3,
                                         fill_opacity=1, stroke_width=0).move_to([-1.2, 0.1 - 0.7 * i, 0])
                        for i in range(3)])
        self.add(shadow(-1.2, -2.1, w=5.8))
        self.play(Create(card), Create(band), FadeIn(heads), run_time=1.6)
        self.play(FadeIn(rows), run_time=1.0)
        until(self, "easier to trust")
        ck = check(-4.4, -1.9, s=0.3, color=INK, w=9)
        lab = lbl("check the facts", 2.9, -1.9)
        self.play(GrowFromCenter(ck), FadeIn(lab), run_time=1.2)
        until(self, "never makes the facts true")
        ring = Circle(radius=0.5, color=TERRA, stroke_width=7).move_to([-1.2, -0.6, 0])
        self.play(Create(ring), run_time=0.9)
        until(self, "before you copy the layout")
        finish(self)

class B08_ThenStop(Scene):
    def construct(self):
        ask = pill(0, 0.9, 7.6)
        askt = T("compare the two laptops", size=40, color=INK).move_to([0, 0.9, 0])
        self.play(FadeIn(ask), FadeIn(askt), run_time=1.4)
        until(self, "under forty words")
        c1 = lbl("table", -2.6, -0.9); c2 = lbl("40 words", 0, -0.9); c3 = lbl("pirate voice", 2.6, -0.9)
        lab = lbl("then stop", 0, 2.4)
        self.play(FadeIn(c1), FadeIn(c2), FadeIn(c3), FadeIn(lab), run_time=1.4)
        until(self, "reading it would have taken")
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(c3), run_time=0.9)
        clean = pill(0, -0.9, 8.2)
        cleant = T("table, 100 words, friendly", size=40, color=INK).move_to([0, -0.9, 0])
        self.play(FadeIn(clean), FadeIn(cleant), run_time=1.2)
        until(self, "Then stop")
        finish(self)
