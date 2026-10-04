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


# ═════════════════════════════ LEARN ANYTHING FASTER — scenes ═════════════════════════════
# 5 Manim scenes (B00–B04), one per body beat. Cast, kept whole film: the kraft
# house (the topic), the tutor card, the learner ("you"), question pills, checks.
# Labels sit beside objects (never inside, never on terracotta), type floor 32,
# all coords inside ±6.2 x / ±3.3 y. Every animation finishes clear of the clip
# midpoint (GATE T samples there): plays land before mid−0.3 s or start after
# mid+0.3 s, paced by until()/finish() against beat_sheet.json.

config.pixel_width = 1920
config.pixel_height = 1080


def draw_house(iso, x0, y0):
    """Kraft isometric house: wall box + gable roof + door. Returns VGroup."""
    w, d, h, rh = 2.2, 1.8, 1.3, 0.9
    walls = iso.box(x0, y0, 0, w, d, h)
    x1, y1, z1 = x0 + w, y0 + d, h
    ym = y0 + d / 2
    slope_f = iso.quad([(x0, y0, z1), (x1, y0, z1), (x1, ym, z1 + rh), (x0, ym, z1 + rh)], BOX_R)
    slope_b = iso.quad([(x0, y1, z1), (x1, y1, z1), (x1, ym, z1 + rh), (x0, ym, z1 + rh)], BOX_L)
    gable_l = Polygon(iso.p(x0, y0, z1), iso.p(x0, y1, z1), iso.p(x0, ym, z1 + rh),
                      fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    gable_r = Polygon(iso.p(x1, y0, z1), iso.p(x1, y1, z1), iso.p(x1, ym, z1 + rh),
                      fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=4)
    dx = x0 - 0.03  # door sits just proud of the x = x0 wall face
    door = iso.quad([(dx, y0 + 0.55, 0), (dx, y0 + 1.15, 0),
                     (dx, y0 + 1.15, 0.72), (dx, y0 + 0.55, 0.72)], DARK_L, stroke=INK, sw=3)
    return VGroup(walls, slope_f, slope_b, gable_l, gable_r, door)


def tutor_card(x, y, w=2.4, h=1.7):
    """The AI as tutor: white card, ink outline, terracotta 'on' lamp. Returns (card_group, label)."""
    card = RoundedRectangle(corner_radius=0.2, width=w, height=h, fill_color=CARD,
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    lamp = Dot([x + w / 2 - 0.35, y + h / 2 - 0.35, 0], radius=0.09, color=TERRA)
    label = T("tutor", 32).move_to([x, y - h / 2 - 0.55, 0])
    return VGroup(card, lamp), label


def learner(x, y):
    """The viewer: head circle + kraft torso. Returns (figure_group, label)."""
    head_c = Circle(radius=0.38, stroke_color=INK, stroke_width=4, fill_opacity=0).move_to([x, y + 0.55, 0])
    torso = RoundedRectangle(corner_radius=0.22, width=0.95, height=0.95, fill_color=BOX_L,
                             fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y - 0.4, 0])
    label = T("you", 32).move_to([x, y - 1.45, 0])
    return VGroup(head_c, torso), label


def qpill(x, y):
    """A question pill carrying '?'. Ink outline so it reads on the cream stage."""
    p = RoundedRectangle(corner_radius=0.31, width=1.1, height=0.62, fill_color=CARD,
                         fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    q = T("?", 40).move_to([x, y - 0.03, 0])
    return VGroup(p, q)


def opt_pill(x, y, s):
    """A wider pill carrying a short option phrase."""
    w = len(s) * 0.24 + 0.9
    p = RoundedRectangle(corner_radius=0.31, width=w, height=0.62, fill_color=CARD,
                         fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    t = T(s, 32).move_to([x, y - 0.03, 0])
    return VGroup(p, t)


class B00_House(Scene):
    def construct(self):
        iso = Iso(-2.0, -0.9, 0.85)
        house = draw_house(iso, 0, 0)
        shadow = Ellipse(width=3.8, height=0.9, fill_color=GHOST, fill_opacity=1,
                         stroke_width=0).move_to([-2.05, -0.75, 0])
        label = T("a mortgage", 36).move_to([0.9, 0.3, 0])
        self.play(GrowFromCenter(shadow), run_time=0.8)
        self.play(FadeIn(house, shift=DOWN * 1.2), run_time=1.2)
        self.play(FadeIn(label, shift=UP * 0.2), run_time=0.8)
        until(self, "Watch what the three moves")
        finish(self)


class B01_ExplainSimple(Scene):
    def construct(self):
        iso = Iso(-2.0, -0.9, 0.85)
        house = draw_house(iso, 0, 0)
        shadow = Ellipse(width=3.8, height=0.9, fill_color=GHOST, fill_opacity=1,
                         stroke_width=0).move_to([-2.05, -0.75, 0])
        hlabel = T("a mortgage", 36).move_to([0.9, 0.3, 0])
        tutor, tlabel = tutor_card(3.3, 1.0)
        xs = (-3.0, -0.2, 2.6)
        blocks = VGroup(*[RoundedRectangle(corner_radius=0.12, width=1.9, height=1.1,
                                           fill_color=BOX_TOP, fill_opacity=1,
                                           stroke_color=INK, stroke_width=4).move_to([x, 0.3, 0])
                           for x in xs])
        blabels = VGroup(*[T(s, 32).move_to([x, -2.75, 0])
                           for s, x in zip(("borrow", "interest", "pay back"), xs)])
        dot = Dot([-3.0, -1.05, 0], radius=0.13, color=TERRA)
        self.play(FadeIn(shadow), FadeIn(house), FadeIn(hlabel), run_time=1.0)
        self.play(FadeIn(tutor), FadeIn(tlabel), run_time=1.0)
        until(self, "A mortgage, plainly", lead=0.6)
        self.play(*[b.animate.shift(DOWN * 2.2) for b in blocks], run_time=1.6)
        self.play(FadeIn(blabels), run_time=0.8)
        until(self, "you borrow a large sum", lead=0.5)
        self.play(FadeIn(dot), run_time=0.5)
        until(self, "Interest is the price", lead=0.3)
        self.play(MoveAlongPath(dot, Line(dot.get_center(), [-0.2, -1.05, 0])), run_time=0.9)
        until(self, "you pay it all back", lead=0.3)
        self.play(MoveAlongPath(dot, Line(dot.get_center(), [2.6, -1.05, 0])), run_time=0.9)
        finish(self)


class B02_QuizMode(Scene):
    def construct(self):
        iso = Iso(-4.3, 1.1, 0.5)
        house = draw_house(iso, 0, 0)
        tutor, tlabel = tutor_card(3.3, 1.0)
        who, ylabel = learner(-2.6, 0.2)
        q1 = qpill(1.9, 0.9)
        answer = Line([-2.0, -0.35, 0], [-0.9, -0.35, 0], color=INK, stroke_width=6)
        tick = check(-1.45, 0.35, s=0.28, color=TERRA, w=8)
        q2 = qpill(0.5, 0.9)
        tag = T("one at a time", 32).move_to([-0.5, -1.9, 0])
        self.play(FadeIn(house), FadeIn(tutor), FadeIn(tlabel), run_time=1.0)
        self.play(FadeIn(who), FadeIn(ylabel), run_time=1.0)
        until(self, "what is interest", lead=1.0)
        self.play(MoveAlongPath(q1, Line([1.9, 0.9, 0], [-1.2, 0.9, 0])), run_time=1.6)
        self.play(FadeIn(answer), run_time=0.8)
        until(self, "It checks you", lead=0.4)
        self.play(GrowFromCenter(tick), run_time=0.7)
        until(self, "does the next question arrive", lead=1.2)
        self.play(FadeIn(q2, shift=DOWN * 0.4), run_time=1.2)
        self.play(FadeIn(tag, shift=UP * 0.2), run_time=0.8)
        finish(self)


class B03_Socratic(Scene):
    def construct(self):
        iso = Iso(-4.3, 1.1, 0.5)
        house = draw_house(iso, 0, 0)
        tutor, tlabel = tutor_card(3.3, 1.0)
        who, ylabel = learner(-2.6, 0.2)
        opt1 = opt_pill(0.3, -1.55, "the loan")
        opt2 = opt_pill(0.3, -2.45, "the interest")
        dot = Dot([-2.6, 1.5, 0], radius=0.13, color=TERRA)
        arrow = CurvedArrow([1.9, 1.5, 0], [-1.7, 1.5, 0], angle=-0.5, color=INK, stroke_width=5)
        aha = Dot([-2.6, 1.75, 0], radius=0.16, color=TERRA)
        ahalabel = T("aha", 36).move_to([-2.6, 2.3, 0])
        self.play(FadeIn(house), FadeIn(tutor), FadeIn(tlabel), run_time=1.0)
        self.play(FadeIn(who), FadeIn(ylabel), run_time=1.0)
        until(self, "Ask me leading questions", lead=0.8)
        self.play(FadeIn(opt1), FadeIn(opt2), run_time=1.2)
        self.play(FadeIn(dot), run_time=0.6)
        until(self, "where does the money go first", lead=1.0)
        self.play(MoveAlongPath(dot, Line(dot.get_center(), [0.3, -2.45, 0])), run_time=0.9)
        until(self, "It asks a sharper question", lead=0.8)
        self.play(Create(arrow), run_time=1.2)
        until(self, "the insight lands", lead=0.6)
        self.play(GrowFromCenter(aha), FadeIn(ahalabel, shift=DOWN * 0.15), run_time=1.0)
        finish(self)


class B04_YourTopic(Scene):
    def construct(self):
        iso = Iso(-2.0, -0.9, 0.85)
        house = draw_house(iso, 0, 0)
        card = RoundedRectangle(corner_radius=0.25, width=2.6, height=3.0, fill_color=CARD,
                                fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0.8, 0.2, 0])
        qm = T("?", 96).move_to([0.8, 0.35, 0])
        clabel = T("your topic", 32).move_to([0.8, -1.85, 0])
        dots = VGroup(*[Dot([2.9, y, 0], radius=0.13, color=TERRA) for y in (0.9, 0.2, -0.5)])
        self.play(FadeIn(house), run_time=0.8)
        until(self, "was only the demo", lead=0.2)
        self.play(house.animate.shift(LEFT * 2.5).scale(0.7),
                  FadeIn(card), FadeIn(qm), run_time=1.2)
        self.play(FadeIn(clabel, shift=UP * 0.15), run_time=0.8)
        until(self, "Same three moves", lead=0.8)
        self.play(*[GrowFromCenter(d) for d in dots], run_time=0.9)
        finish(self)
