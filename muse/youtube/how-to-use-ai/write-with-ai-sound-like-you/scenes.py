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
# ═════════════════════════════ BODY SCENES ═════════════════════════════
# One drawn illustration per beat. Labels sit beside objects (never inside an
# outline, never on terracotta), leader lines keep >= 0.3 units of gap, type >= 32.
# Every play adds at least one new non-text shape (Gate A); MoveAlongPath stands
# alone in its play (the stub's .animate proxy is not callable).


class B00_RobotDraft(Scene):
    """The problem: every first draft comes out in the AI's default voice."""
    def construct(self):
        iso = Iso(0, -0.4, 1.0)
        block = iso.mcp(-0.75, -0.75, 0)
        self.play(FadeIn(block), run_time=1.0)
        until(self, "And every first draft")
        pages = [iso.page(1.0 + i * 0.42, -0.6 - i * 0.42, 0.1, w=1.05, d=1.35) for i in range(3)]
        self.play(FadeIn(pages[0]), run_time=0.8)
        until(self, "Polite, padded")
        self.play(FadeIn(pages[1]), FadeIn(pages[2]), run_time=0.9)
        until(self, "It sounds like everyone")
        label = T("default voice", 36).move_to([5.7, 0.55, 0])
        leader = Line([3.85, 0.55, 0], [4.35, 0.55, 0], color=INK, stroke_width=3)
        self.play(Create(leader), FadeIn(label), run_time=0.8)
        finish(self)


class B01_NoSample(Scene):
    """Why: the AI has nothing to copy, so an empty tray still yields generic pages."""
    def construct(self):
        iso = Iso(0, -0.4, 1.0)
        block = iso.mcp(-0.75, -0.75, 0)
        self.play(FadeIn(block), run_time=0.8)
        until(self, "Because the AI has nothing to copy")
        tray = DashedVMobject(Rectangle(width=2.6, height=1.4, stroke_color=DIM, stroke_width=3, fill_opacity=0))
        tray.move_to([-3.5, 1.15, 0])
        tlabel = T("no sample", 32).move_to([-3.5, -0.25, 0])
        self.play(Create(tray), FadeIn(tlabel), run_time=0.9)
        until(self, "falls back on its safest habit")
        p1 = iso.page(1.0, -0.6, 0.1, w=1.05, d=1.35)
        p2 = iso.page(1.42, -1.02, 0.16, w=1.05, d=1.35)
        self.play(FadeIn(p1), FadeIn(p2), run_time=0.9)
        finish(self)


class B02_MatchMyVoice(Scene):
    """Fix one: paste a sample of your own writing — 'match this voice'."""
    def construct(self):
        iso = Iso(0, -0.4, 1.0)
        block = iso.mcp(-0.2, -0.9, 0)
        self.play(FadeIn(block), run_time=0.8)
        until(self, "Take one email or paragraph")
        wrap = VGroup(iso.page(-3.6, 0.6, 0, w=1.05, d=1.35))
        ylab = T("your email", 32).move_to([-3.77, -2.6, 0])
        self.play(FadeIn(wrap), FadeIn(ylab), run_time=0.9)
        until(self, "paste it into your prompt")
        path = ArcBetweenPoints(np.array([-3.77, -1.3, 0]), np.array([0.3, -0.5, 0]), angle=-0.6)
        self.play(MoveAlongPath(wrap, path), run_time=1.2)
        until(self, "It is copying you now")
        out = iso.page(2.3, -0.7, 0.15, w=1.05, d=1.35)
        chk = check(3.35, 1.05, s=0.2, color=TERRA)
        olab = T("sounds like you", 32).move_to([2.9, 1.95, 0])
        self.play(FadeOut(wrap), FadeIn(out), FadeIn(chk), FadeIn(olab), run_time=1.0)
        finish(self)


class B03_BanTheGiveaways(Scene):
    """Fix two: cross out the telltale phrases — delve, fast-paced world, em-dashes."""
    def construct(self):
        card = RoundedRectangle(width=5.0, height=3.4, corner_radius=0.15,
                                fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0, -0.3, 0])
        t1 = T("delve", 36).move_to([0, 0.55, 0])
        t2 = T("in today's fast-paced world", 36).scale_to_fit_width(2.8).move_to([0, -0.25, 0])
        t3 = T("— — —", 36).move_to([0, -1.05, 0])
        self.play(FadeIn(card), FadeIn(t1), FadeIn(t2), FadeIn(t3), run_time=1.0)
        until(self, "delve")
        x1 = VGroup(Line([-0.75, 0.83, 0], [0.75, 0.27, 0], color=INK, stroke_width=7),
                    Line([-0.75, 0.27, 0], [0.75, 0.83, 0], color=INK, stroke_width=7))
        self.play(Create(x1), run_time=0.6)
        until(self, "in today's fast-paced world")
        x2 = VGroup(Line([-1.5, 0.03, 0], [1.5, -0.53, 0], color=INK, stroke_width=7),
                    Line([-1.5, -0.53, 0], [1.5, 0.03, 0], color=INK, stroke_width=7))
        self.play(Create(x2), run_time=0.6)
        until(self, "a forest of em-dashes")
        x3 = VGroup(Line([-0.8, -0.77, 0], [0.8, -1.33, 0], color=INK, stroke_width=7),
                    Line([-0.8, -1.33, 0], [0.8, -0.77, 0], color=INK, stroke_width=7))
        self.play(Create(x3), run_time=0.6)
        until(self, "more like a person")
        label = T("the giveaways", 36).move_to([4.6, 0.55, 0])
        leader = Line([2.65, 0.55, 0], [3.25, 0.55, 0], color=INK, stroke_width=3)
        self.play(Create(leader), FadeIn(label), run_time=0.7)
        finish(self)


class B04_DictateThenClean(Scene):
    """Fix three: dictate rough thoughts, let the AI clean them up."""
    def construct(self):
        bubble = RoundedRectangle(width=3.0, height=1.8, corner_radius=0.3,
                                  fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-3.6, 0.7, 0])
        tail = Polygon([-4.7, -0.2, 0], [-4.1, -0.2, 0], [-4.75, -0.75, 0],
                       fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4)
        blab = T("rough thoughts", 32).move_to([-3.6, -1.0, 0])
        self.play(FadeIn(bubble), FadeIn(tail), FadeIn(blab), run_time=0.9)
        until(self, "dictate your rough ones")
        scribs = [Line([-4.85 + 0.05 * i, 1.15 - 0.3 * i, 0], [-3.6 + 0.1 * i, 1.05 - 0.3 * i, 0],
                       color=DIM, stroke_width=5) for i in range(4)]
        self.play(LaggedStart(*[Create(s) for s in scribs], lag_ratio=0.35), run_time=1.2)
        until(self, "ask it to clean them up")
        iso = Iso(0, -0.4, 1.0)
        clean = iso.page(2.2, -0.6, 0, w=1.05, d=1.35)
        clab = T("cleaned up", 32).move_to([2.29, -0.25, 0])
        self.play(FadeIn(clean), FadeIn(clab), run_time=0.9)
        finish(self)


class B05_YourFinalPass(Scene):
    """Fix four: circle the line that isn't you, swap it in your own words."""
    def construct(self):
        card = RoundedRectangle(width=4.6, height=2.6, corner_radius=0.15,
                                fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-0.5, -0.35, 0])
        l1 = T("I hope this email finds you well", 32).scale_to_fit_width(3.6).move_to([-0.5, 0.25, 0])
        l2 = T("Delving into our proposal", 32).scale_to_fit_width(3.6).move_to([-0.5, -0.35, 0])
        l3 = T("Please advise at your convenience", 32).scale_to_fit_width(3.6).move_to([-0.5, -0.95, 0])
        self.play(FadeIn(card), FadeIn(l1), FadeIn(l2), FadeIn(l3), run_time=1.0)
        until(self, "Read the draft out loud")
        ring = Ellipse(width=3.9, height=0.72, stroke_color=INK, stroke_width=4, fill_opacity=0).move_to([-0.5, -0.35, 0])
        self.play(Create(ring), run_time=0.7)
        until(self, "change it in your own words")
        l2b = T("Here is the proposal", 32).scale_to_fit_width(3.6).move_to([-0.5, -0.35, 0])
        self.play(FadeOut(l2), FadeIn(l2b), run_time=0.7)
        until(self, "that has to be yours")
        chk = check(2.15, 0.35, s=0.2, color=TERRA)
        label = T("your pass", 32).move_to([3.5, -0.35, 0])
        leader = Line([2.0, -0.35, 0], [2.45, -0.35, 0], color=INK, stroke_width=3)
        self.play(Create(leader), FadeIn(label), FadeIn(chk), run_time=0.8)
        finish(self)


class B06_TheEmail(Scene):
    """The demo: the default draft beside the fixed one — same facts, one sounds human."""
    def construct(self):
        iso = Iso(0, -0.4, 1.0)
        lx, ly = -3.9, 0.8
        lslab = iso.box(lx, ly, 0, 1.05, 1.35, 0.06)
        llines = VGroup(*[Line(iso.p(lx + 0.18, ly + 1.35 * f, 0.07), iso.p(lx + 0.87, ly + 1.35 * f, 0.07),
                              color=BAR1, stroke_width=5) for f in (0.3, 0.5, 0.7)])
        left = VGroup(lslab, llines)
        llab = T("default", 32).move_to([-3.33, -2.62, 0])
        self.play(FadeIn(left), FadeIn(llab), run_time=0.9)
        until(self, "The fixed version says")
        rx, ry = 2.9, 0.8
        rslab = iso.box(rx, ry, 0, 1.05, 1.35, 0.06)
        rlines = VGroup(*[Line(iso.p(rx + 0.18, ry + 1.35 * f, 0.07), iso.p(rx + 0.87, ry + 1.35 * f, 0.07),
                              color=INK, stroke_width=5) for f in (0.3, 0.5, 0.7)])
        right = VGroup(rslab, rlines)
        rlab = T("your voice", 32).move_to([1.69, -2.62, 0])
        self.play(FadeIn(right), FadeIn(rlab), run_time=0.9)
        until(self, "sounds like a person")
        chk = check(2.9, -0.1, s=0.22, color=TERRA)
        self.play(FadeIn(chk), run_time=0.6)
        finish(self)
