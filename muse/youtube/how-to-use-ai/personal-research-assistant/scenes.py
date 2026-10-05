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
        stack = VGroup(*[self.box(x0, y0, z0, w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
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

# FILM HELPERS - "Your personal research assistant" (original to this film).
# Flat UI shapes in the Claude palette: brief cards and chips, source pages,
# report pages with claim lines and terracotta citation dots, date plates,
# the "?" flag plate, labels and leaders. All coordinates stay inside
# +-6.2 x +-3.3; labels sit beside objects (or as adjacent captions), never
# inside an outline; type floor 32; leader lines keep >=0.3 gap from labels.


def shadow(x, y, w=4.4, h=0.7):
    return Ellipse(width=w, height=h, fill_color="#D9D4C7",
                   fill_opacity=1, stroke_width=0).move_to([x, y, 0])


def label(s, x, y, size=36):
    return T(s, size=size, color=INK).move_to([x, y, 0])


def leader(x1, y1, x2, y2):
    return Line([x1, y1, 0], [x2, y2, 0], color=INK, stroke_width=3)


def flatcard(x, y, w, h, fill="#FFFFFF", sw=3, outline=INK):
    return RoundedRectangle(width=w, height=h, corner_radius=0.22,
                            fill_color=fill, fill_opacity=1,
                            stroke_color=outline, stroke_width=sw).move_to([x, y, 0])


def chip(x, y, s, size=34):
    """A brief chip: ink-outlined pill with its word."""
    p = pill(x, y, len(s) * size * 0.0075 + 0.9, h=0.62, fill="#FFFFFF")
    p.set_stroke(INK, width=2)
    t = T(s, size=size).move_to([x, y, 0])
    return VGroup(p, t)


def srcpage(x, y, w=1.5, h=1.9, dim=False):
    """A source page: white card, three ghost lines, one terracotta dot. `dim` = rejected/old."""
    fill = "#FFFFFF" if not dim else "#E4E1D8"
    outl = INK if not dim else "#A9A49A"
    body = flatcard(x, y, w, h, fill=fill, outline=outl, sw=3 if not dim else 2)
    lines = VGroup(*[Line([x - w / 2 + 0.28, y + h / 2 - 0.55 - i * 0.34, 0],
                         [x + w / 2 - 0.28, y + h / 2 - 0.55 - i * 0.34, 0],
                         color=GHOST if not dim else "#C9C4B8", stroke_width=4)
                     for i in range(3)])
    d = Dot([x - w / 2 + 0.32, y + h / 2 - 0.3, 0], radius=0.075,
            color=TERRA if not dim else "#A9A49A")
    return VGroup(body, lines, d)


def report(x, y, w, h, nclaims):
    """A report page: white slab with `nclaims` ghost claim lines. Returns (group, lines)."""
    body = flatcard(x, y, w, h, fill="#FFFFFF", outline=INK, sw=3)
    lines = [Line([x - w / 2 + 0.55, y + h / 2 - 0.55 - i * 0.5, 0],
                  [x + w / 2 - 0.35, y + h / 2 - 0.55 - i * 0.5, 0],
                  color=GHOST, stroke_width=5)
             for i in range(nclaims)]
    return VGroup(body, VGroup(*lines)), lines


def dot_solid(x, y, r=0.085):
    return Dot([x, y, 0], radius=r, color=TERRA)


def dot_hollow(x, y, r=0.085):
    return Circle(radius=r, stroke_color=TERRA, stroke_width=5,
                  fill_opacity=0).move_to([x, y, 0])


def datelab(s, x, y, ink=True):
    """A date plate: small rounded plate with a year."""
    w = len(s) * 36 * 0.0075 + 0.7
    p = RoundedRectangle(width=w, height=0.72, corner_radius=0.18,
                         fill_color="#FFFFFF" if ink else "#E4E1D8",
                         fill_opacity=1,
                         stroke_color=INK if ink else "#A9A49A",
                         stroke_width=3 if ink else 2).move_to([x, y, 0])
    t = T(s, size=36, color=INK if ink else "#8B8F96").move_to([x, y, 0])
    return VGroup(p, t)


def qflag(x, y):
    """The '?' flag plate: a small card with a terracotta question mark."""
    p = flatcard(x, y, 0.85, 0.85, fill="#FFFFFF", outline=INK, sw=3)
    q = T("?", size=44, color=TERRA, bold=True).move_to([x, y + 0.02, 0])
    return VGroup(p, q)


def deskbox(ox, oy, s=0.9):
    """The research desk / brief box: an open iso box + landing shadow."""
    iso = Iso(ox=ox, oy=oy, s=s)
    back, front = iso.open_box(-1.5, -1.1, 0, 3.0, 2.2, 1.2)
    sh = shadow(ox, oy - 1.5 * s, w=4.6 * s)
    return back, front, sh


# ═════════════════════════════ SCENES (one per body beat) ═════════════════════════════


class B00_HeroDesk(Scene):
    """The hero: a brief goes in, sources get read, a cited report comes back."""

    def construct(self):
        back, front, sh = deskbox(-2.9, -0.9)
        self.play(FadeIn(sh), FadeIn(back), FadeIn(front), run_time=0.7)
        until(self, "This is deep research.")
        c = chip(-2.9, 2.5, "the brief")
        c.set_z_index(1)
        self.play(FadeIn(c), run_time=0.4)
        self.play(c.animate.shift(DOWN * 2.7), run_time=0.5)
        until(self, "You hand it a brief,")
        pages = VGroup(*[srcpage(-5.0 + i * 1.3, 1.75, w=1.1, h=1.45) for i in range(5)])
        self.play(*[FadeIn(p) for p in pages], lag_ratio=0.15, run_time=1.2)
        until(self, "not one page, dozens")
        rep, lines = report(3.2, 0.0, w=3.5, h=2.7, nclaims=4)
        self.play(GrowFromCenter(rep), run_time=0.7)
        until(self, "brings back a report")
        dots = VGroup(*[dot_solid(3.2 - 3.5 / 2 + 0.3, 0.0 + 2.7 / 2 - 0.55 - i * 0.5)
                        for i in range(4)])
        self.play(*[FadeIn(d) for d in dots], lag_ratio=0.15, run_time=0.8)
        until(self, "each claim points to a source.")
        lab = label("deep research", -2.9, -2.95)
        self.play(FadeIn(lab), run_time=0.5)
        until(self, "never sleeps.")
        finish(self)


class B01_TheDecision(Scene):
    """The brief starts with the decision: the decision card drops into the brief box."""

    def construct(self):
        back, front, sh = deskbox(-3.0, -0.7)
        self.play(FadeIn(sh), FadeIn(back), FadeIn(front), run_time=0.7)
        until(self, "The brief starts with the decision,")
        dim_card = flatcard(3.3, 0.3, w=2.7, h=1.2, fill="#E4E1D8", outline="#A9A49A", sw=2)
        dim_lab = T("the topic", size=36, color="#8B8F96").move_to([3.3, -0.65, 0])
        self.play(FadeIn(dim_card), FadeIn(dim_lab), run_time=0.5)
        until(self, "'Research electric bikes'")
        card = flatcard(-3.0, 2.6, w=2.7, h=1.2)
        dot = Dot([-3.0 - 2.7 / 2 + 0.32, 2.6 + 1.2 / 2 - 0.3, 0], radius=0.08, color=TERRA)
        card.set_z_index(3); dot.set_z_index(3)
        self.play(FadeIn(card), FadeIn(dot), run_time=0.4)
        self.play(card.animate.shift(DOWN * 2.4), dot.animate.shift(DOWN * 2.4), run_time=0.5)
        until(self, "I'm choosing a bike")
        lab = T("your decision", size=36, color=INK).move_to([-3.0, -2.6, 0])
        self.play(FadeIn(lab), run_time=0.4)
        until(self, "Tell it what you're deciding,")
        self.play(FadeOut(dim_card), FadeOut(dim_lab), run_time=0.5)
        until(self, "gets you an answer.")
        ck = check(-3.0, 0.2, s=0.28, color=TERRA, w=9)
        self.play(GrowFromCenter(ck), run_time=0.5)
        until(self, "the research has an aim.")
        finish(self)


class B02_TheScope(Scene):
    """The scope: source pages split into 'in scope' and 'out of scope' piles; a date plate lands."""

    def construct(self):
        pages = [srcpage(-3.25 + i * 1.3, 1.5, w=1.15, h=1.5) for i in range(6)]
        self.play(*[FadeIn(p) for p in pages], lag_ratio=0.1, run_time=0.9)
        until(self, "Then the scope:")
        keep = VGroup(*pages[:3])
        drop = VGroup(*pages[3:])
        self.play(keep.animate.shift(LEFT * 1.6 + DOWN * 1.3),
                  drop.animate.shift(RIGHT * 1.6 + DOWN * 1.3), run_time=0.7)
        until(self, "what counts, and what doesn't.")
        cks = VGroup(*[check(-4.85 + i * 1.3, 1.15, s=0.16, color=INK, w=6) for i in range(3)])
        self.play(*[GrowFromCenter(c) for c in cks], lag_ratio=0.12, run_time=0.6)
        until(self, "Tell it where to look")
        dimmed = VGroup(*[srcpage(2.25 + i * 1.3, 0.2, w=1.15, h=1.5, dim=True) for i in range(3)])
        strikes = VGroup(*[Line([2.25 + i * 1.3 - 0.45, 0.55, 0], [2.25 + i * 1.3 + 0.45, -0.15, 0],
                                color="#A9A49A", stroke_width=5) for i in range(3)])
        self.play(FadeOut(drop), run_time=0.3)
        self.play(FadeIn(dimmed), run_time=0.4)
        self.play(*[Create(s) for s in strikes], lag_ratio=0.1, run_time=0.5)
        until(self, "what to skip,")
        lab1 = label("in scope", -4.85, -1.35)
        lab2 = label("out of scope", 3.55, -1.35)
        self.play(FadeIn(lab1), FadeIn(lab2), run_time=0.5)
        until(self, "And set a date window.")
        dp = datelab("last 5 years", 0, -2.55)
        self.play(GrowFromCenter(dp), run_time=0.5)
        until(self, "Research from last year")
        finish(self)


class B03_DemandProof(Scene):
    """The demanded shape: a citation dot lands on every claim line; one line gets the '?' flag."""

    def construct(self):
        rep, lines = report(-2.0, 0.2, w=4.2, h=3.0, nclaims=4)
        self.play(GrowFromCenter(rep), run_time=0.7)
        until(self, "Now tell it the shape of the answer.")
        line_ys = [0.2 + 3.0 / 2 - 0.55 - i * 0.5 for i in range(4)]
        for ly in line_ys:
            d = dot_solid(-2.0 - 4.2 / 2 + 0.3, ly)
            self.play(FadeIn(d), run_time=0.3)
        until(self, "A citation for every claim")
        flag = qflag(2.6, line_ys[-1])
        self.play(GrowFromCenter(flag), run_time=0.5)
        until(self, "flag anything you could not verify.")
        cap = T("couldn't verify", size=32, color=DIM).move_to([2.6, line_ys[-1] - 0.75, 0])
        self.play(FadeIn(cap), run_time=0.4)
        until(self, "An honest")
        lab = label("citation per claim", -2.0, -2.75)
        self.play(FadeIn(lab), run_time=0.5)
        until(self, "beats a confident guess.")
        finish(self)


class B04_ThreeLayers(Scene):
    """Read it in layers: the report fans into summary / claims / sources; the cursor picks sources."""

    def construct(self):
        rep, lines = report(0, 0.9, w=3.4, h=2.2, nclaims=4)
        self.play(GrowFromCenter(rep), run_time=0.7)
        until(self, "When the report lands,")
        words = ["summary", "claims", "sources"]
        xs = [-3.7, 0.0, 3.7]
        cards = VGroup(*[flatcard(x, 0.5, w=2.9, h=1.7) for x in xs])
        caps = VGroup(*[T(w, size=36, color=INK).move_to([x, 0.5 - 1.7 / 2 - 0.42, 0])
                        for x, w in zip(xs, words)])
        dots = VGroup(*[Dot([x - 2.9 / 2 + 0.32, 0.5 + 1.7 / 2 - 0.3, 0], radius=0.08, color=TERRA)
                        for x in xs])
        self.play(FadeOut(rep), run_time=0.3)
        self.play(*[GrowFromCenter(c) for c in cards],
                  *[FadeIn(d) for d in dots], run_time=0.8)
        self.play(FadeIn(caps), run_time=0.4)
        until(self, "read it in layers.")
        cur = cursor(3.7, 1.5, s=0.5)
        self.play(FadeIn(cur), run_time=0.4)
        until(self, "the source list.")
        ring = RoundedRectangle(width=2.9 + 0.3, height=1.7 + 0.3, corner_radius=0.3,
                               fill_opacity=0, stroke_color=TERRA, stroke_width=6).move_to([3.7, 0.5, 0])
        self.play(GrowFromCenter(ring), run_time=0.5)
        until(self, "Where did it actually look?")
        lab = label("read sources first", 0, -2.5)
        self.play(FadeIn(lab), run_time=0.5)
        until(self, "the ground it stands on.")
        finish(self)


class B05_SpotCheck(Scene):
    """Spot-check two citations: one source holds, the other is a dead page."""

    def construct(self):
        rep, lines = report(-2.4, 0.3, w=3.6, h=2.8, nclaims=3)
        dots = [dot_solid(-3.9, 1.15 - i * 0.5) for i in range(3)]
        self.play(GrowFromCenter(rep), run_time=0.6)
        self.play(*[FadeIn(d) for d in dots], lag_ratio=0.12, run_time=0.5)
        until(self, "Then spot-check two citations.")
        cur = cursor(-3.9, 1.55, s=0.5)
        self.play(FadeIn(cur), run_time=0.4)
        until(self, "Open them yourself.")
        page = srcpage(3.0, 0.9, w=2.6, h=2.0)
        self.play(FadeIn(page), run_time=0.5)
        ck = check(3.0, 0.9, s=0.3, color=INK, w=9)
        self.play(GrowFromCenter(ck), run_time=0.5)
        until(self, "Does the source really say")
        self.play(FadeOut(page), FadeOut(ck), run_time=0.3)
        dead = flatcard(3.0, 0.9, w=2.6, h=2.0, fill="#E4E1D8", outline="#A9A49A", sw=2)
        self.play(FadeIn(dead), run_time=0.4)
        x1 = Line([1.9, 1.7, 0], [4.1, 0.1, 0], color=TERRA, stroke_width=8)
        x2 = Line([1.9, 0.1, 0], [4.1, 1.7, 0], color=TERRA, stroke_width=8)
        self.play(Create(x1), Create(x2), run_time=0.5)
        until(self, "When one doesn't,")
        lab = label("spot-check two", -2.4, -2.5)
        self.play(FadeIn(lab), run_time=0.5)
        until(self, "the full checking habit.")
        finish(self)


class B06_HollowCitations(Scene):
    """The shiny report whose citation dots turn hollow; one opens onto an empty page."""

    def construct(self):
        rep, lines = report(-1.2, 0.2, w=3.8, h=3.0, nclaims=4)
        solids = [dot_solid(-2.8, 1.15 - i * 0.5) for i in range(4)]
        self.play(GrowFromCenter(rep), run_time=0.6)
        self.play(*[FadeIn(d) for d in solids], lag_ratio=0.1, run_time=0.5)
        until(self, "Distrust the shiny report")
        for i, s in enumerate(solids):
            h = dot_hollow(-2.8, 1.15 - i * 0.5)
            self.play(FadeOut(s), FadeIn(h), run_time=0.3)
        until(self, "but open them")
        cur = cursor(-2.8, 1.05, s=0.5)
        self.play(FadeIn(cur), run_time=0.4)
        empty = flatcard(3.6, 0.2, w=2.4, h=2.2)
        self.play(FadeIn(empty), run_time=0.5)
        until(self, "there's nothing behind them.")
        x1 = Line([2.6, 1.1, 0], [4.6, -0.7, 0], color=TERRA, stroke_width=8)
        x2 = Line([2.6, -0.7, 0], [4.6, 1.1, 0], color=TERRA, stroke_width=8)
        self.play(Create(x1), Create(x2), run_time=0.5)
        until(self, "Confidence is not evidence.")
        lab = label("hollow", -1.2, -2.5)
        self.play(FadeIn(lab), run_time=0.5)
        until(self, "If the citations don't hold,")
        finish(self)


class B07_TheEcho(Scene):
    """The echo: citations circle between two AI reports; the chain must reach a human source."""

    def construct(self):
        repA, _ = report(-3.4, 0.5, w=2.7, h=2.5, nclaims=3)
        repB, _ = report(-0.2, 0.5, w=2.7, h=2.5, nclaims=3)
        self.play(GrowFromCenter(repA), GrowFromCenter(repB), run_time=0.7)
        until(self, "Distrust the echo.")
        arc1 = ArcBetweenPoints((-2.3, 1.75, 0), (-0.9, 1.75, 0), angle=1.0,
                               color=INK, stroke_width=5)
        arc2 = ArcBetweenPoints((-0.9, -0.75, 0), (-2.3, -0.75, 0), angle=1.0,
                               color=INK, stroke_width=5)
        self.play(Create(arc1), Create(arc2), run_time=0.7)
        until(self, "which cites another AI answer back.")
        page = srcpage(3.9, 0.5, w=1.9, h=2.3)
        self.play(FadeIn(page), run_time=0.5)
        chain = Line([1.15, 0.5, 0], [2.95, 0.5, 0], color=INK, stroke_width=5)
        self.play(Create(chain), run_time=0.5)
        ck = check(3.9, 0.5, s=0.22, color=INK, w=7)
        self.play(GrowFromCenter(ck), run_time=0.5)
        until(self, "Follow the chain until you reach a human source")
        lab = label("the echo", -1.8, -2.5)
        self.play(FadeIn(lab), run_time=0.5)
        until(self, "a named expert.")
        finish(self)


class B08_CheckDates(Scene):
    """Check the dates: old pages dim; then the tall report balances on a single source."""

    def construct(self):
        rep, lines = report(-1.6, 1.0, w=3.8, h=2.4, nclaims=4)
        pages = [srcpage(x, -1.5, w=1.5, h=1.9) for x in (-4.35, -1.45, 1.45, 4.35)]
        self.play(GrowFromCenter(rep), run_time=0.6)
        self.play(*[FadeIn(p) for p in pages], lag_ratio=0.1, run_time=0.6)
        until(self, "And check the dates.")
        dp1 = datelab("2026", -2.9, -2.85, ink=True)
        dp2 = datelab("2019", 2.9, -2.85, ink=True)
        self.play(GrowFromCenter(dp1), GrowFromCenter(dp2), run_time=0.5)
        until(self, "A 2019 source is fine for history")
        dim_old = [srcpage(x, -1.5, w=1.5, h=1.9, dim=True) for x in (1.45, 4.35)]
        self.play(FadeOut(pages[2]), FadeOut(pages[3]), run_time=0.3)
        self.play(FadeIn(dim_old[0]), FadeIn(dim_old[1]), run_time=0.4)
        dp2g = datelab("2019", 2.9, -2.85, ink=False)
        self.play(FadeOut(dp2), FadeIn(dp2g), run_time=0.4)
        until(self, "anything that changed since.")
        keep = pages[1]
        self.play(FadeOut(pages[0]), FadeOut(dim_old[0]), FadeOut(dim_old[1]),
                  FadeOut(dp1), FadeOut(dp2g), run_time=0.4)
        self.play(keep.animate.move_to([-1.6, -1.7, 0]), run_time=0.6)
        until(self, "everything leans on one source,")
        lab = label("check the dates", 3.8, 1.9)
        lead = leader(0.5, 1.6, 1.55, 1.85)
        self.play(FadeIn(lab), Create(lead), run_time=0.5)
        until(self, "however long the report is.")
        finish(self)


class B09_TheMap(Scene):
    """The closing rule: the report is a map, not the answer — you stay the editor."""

    def construct(self):
        back, front, sh = deskbox(-4.6, -1.0, s=0.65)
        rep, lines = report(0.6, 0.3, w=4.2, h=2.6, nclaims=4)
        self.play(FadeIn(sh), FadeIn(back), FadeIn(front), run_time=0.5)
        self.play(GrowFromCenter(rep), run_time=0.6)
        until(self, "Last rule:")
        pen = cursor(0.6, 1.5, s=0.55)
        self.play(FadeIn(pen), run_time=0.4)
        strike = Line([-0.95, 0.55, 0], [2.35, 0.55, 0], color=TERRA, stroke_width=6)
        self.play(Create(strike), run_time=0.5)
        until(self, "you still walk the ground yourself.")
        plate = flatcard(3.9, -1.9, w=2.5, h=0.95)
        ptext = T("you decide", size=36, color=INK).move_to([3.9, -1.9, 0])
        self.play(GrowFromCenter(plate), run_time=0.5)
        self.play(FadeIn(ptext), run_time=0.3)
        until(self, "You are the editor;")
        lab = label("a map, not the answer", -1.3, -2.7)
        self.play(FadeIn(lab), run_time=0.5)
        until(self, "The decision stays yours.")
        finish(self)
