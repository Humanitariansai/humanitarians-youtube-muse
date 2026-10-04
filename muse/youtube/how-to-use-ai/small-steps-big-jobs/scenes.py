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

# ═════════════════════════════ FILM: small-steps-big-jobs ═════════════════════════════
# Show-tell body scenes: one isometric drawing per beat, Claude palette.
# Cast, kept the same all film: the giant box (the whole job), step cards
# (iso pages), arrows (the handoff between steps), the mush page, and
# terracotta checks. Labels sit beside objects, never inside; text >= 32.
# Pacing is narration-driven via until()/finish() from the kit above.
# Class names are literal `class BNN_Name(Scene):` so run.sh finds them.

def _shadow(x, y, w, h):
    return Ellipse(width=w, height=h, color=GHOST, fill_opacity=1, stroke_width=0).move_to([x, y, 0.0])


def _zigzag(iso, pts, z=0.08):
    """A messy hand-drawn-looking scribble across a page: the giant answer."""
    return VGroup(*[Line(iso.p(a[0], a[1], z), iso.p(b[0], b[1], z), color=INK, stroke_width=6)
                    for a, b in zip(pts[:-1], pts[1:])])


_JUMBLE = [(-2.2, 0.8, 2.1, "budget", LEFT, 0.18),
           (-0.6, -0.4, 2.5, "layout", RIGHT, -0.14),
           (1.0, 0.9, 2.2, "materials", RIGHT, 0.22),
           (-1.2, 1.9, 2.8, "timeline", LEFT, -0.20),
           (0.6, -1.6, 2.4, "your taste", RIGHT, 0.12)]


def _jumble(iso):
    """The five small jobs tumbling out of the giant box, labels beside."""
    cards, labels = [], []
    for x, y, z, name, side, ang in _JUMBLE:
        c = iso.page(x, y, z, 1.1, 1.3)
        c.rotate(ang)
        cards.append(c)
        labels.append(T(name, size=32).next_to(c, side, buff=0.3))
    return cards, labels


class B00_GiantBox(Scene):
    def construct(self):
        iso = Iso(0, -0.6, 1.0)
        shadow = _shadow(0, -2.35, 6.0, 1.3)
        box = iso.box(-1.5, -1.5, 0.0, 3.0, 3.0, 2.4)
        tape = iso.tape(-1.5, -1.5, 2.4, 3.0, 3.0)
        label = T("the whole job", size=36).move_to([-4.7, 1.5, 0.0])
        leader = Line([-3.45, 1.32, 0.0], [-2.78, 0.9, 0.0], color=INK, stroke_width=3)
        self.play(FadeIn(shadow), run_time=0.3)
        self.play(FadeIn(box, shift=np.array([0.0, 2.6, 0.0])), rate_func=ease_in, run_time=0.7)
        until(self, "One giant box")
        self.play(Create(tape), FadeIn(label), FadeIn(leader), run_time=0.6)
        finish(self)


class B01_MushOut(Scene):
    def construct(self):
        iso = Iso(0, -0.6, 1.0)
        shadow = _shadow(0, -2.35, 6.0, 1.3)
        box = iso.box(-1.5, -1.5, 0.0, 3.0, 3.0, 2.4)
        tape = iso.tape(-1.5, -1.5, 2.4, 3.0, 3.0)
        label = T("the whole job", size=36).move_to([-4.7, 1.5, 0.0])
        leader = Line([-3.45, 1.32, 0.0], [-2.78, 0.9, 0.0], color=INK, stroke_width=3)
        self.add(shadow, box, tape, label, leader)
        g = VGroup(box, tape, label, leader)

        iso3 = Iso(2.6, -0.5, 0.85)
        page = iso3.page(0.0, 0.0, 0.0, 2.4, 3.0)
        scrib = _zigzag(iso3, [(0.4, 0.5), (2.0, 0.9), (0.5, 1.4), (1.9, 1.9), (0.6, 2.4), (1.7, 2.7)])
        mush_label = T("mush", size=36).move_to([5.5, 0.9, 0.0])
        mush_leader = Line([4.9, 0.8, 0.0], [4.45, 0.62, 0.0], color=INK, stroke_width=3)

        until(self, "Out comes a giant answer")
        self.play(g.animate.shift(np.array([0.0, 4.6, 0.0])), FadeIn(page), run_time=0.8)
        until(self, "and mush")
        self.play(FadeIn(mush_label), FadeIn(mush_leader), run_time=0.5)
        until(self, "Vague on the budget")
        self.play(Create(scrib), run_time=0.7)
        finish(self)


class B02_WhyFails(Scene):
    def construct(self):
        iso = Iso(0, -0.6, 1.0)
        iso3 = Iso(2.6, -0.5, 0.85)
        shadow = _shadow(0, -2.35, 6.0, 1.3)
        page = iso3.page(0.0, 0.0, 0.0, 2.4, 3.0)
        scrib = _zigzag(iso3, [(0.4, 0.5), (2.0, 0.9), (0.5, 1.4), (1.9, 1.9), (0.6, 2.4), (1.7, 2.7)])
        mush_label = T("mush", size=36).move_to([5.5, 0.9, 0.0])
        mush_leader = Line([4.9, 0.8, 0.0], [4.45, 0.62, 0.0], color=INK, stroke_width=3)
        self.add(shadow, page, scrib, mush_label, mush_leader)

        box = iso.box(-1.5, -1.5, 0.0, 3.0, 3.0, 2.4)
        tape = iso.tape(-1.5, -1.5, 2.4, 3.0, 3.0)
        mini = T("five small jobs", size=32).move_to([4.3, 2.2, 0.0])
        back, front = iso.open_box(-1.5, -1.5, 0.0, 3.0, 3.0, 2.0)
        cards, labels = _jumble(iso)

        until(self, "A big job is really")
        self.play(FadeOut(page), FadeOut(scrib), FadeOut(mush_label), FadeOut(mush_leader), run_time=0.6)
        until(self, "five small jobs")
        self.play(FadeIn(box), FadeIn(tape), FadeIn(mini), run_time=0.7)
        until(self, "wearing a trench coat")
        self.play(FadeOut(box), FadeOut(tape), FadeOut(mini), FadeIn(back), FadeIn(front), run_time=0.8)
        until(self, "Ask for all five at once")
        self.play(*[FadeIn(c, shift=np.array([0.0, 1.8, 0.0])) for c in cards], run_time=1.0, rate_func=ease_in)
        until(self, "the AI guesses at each one")
        self.play(*[FadeIn(l) for l in labels], run_time=0.6)
        finish(self)


class B03_StepOne(Scene):
    def construct(self):
        iso = Iso(0, -0.6, 1.0)
        shadow = _shadow(0, -2.35, 6.0, 1.3)
        back, front = iso.open_box(-1.5, -1.5, 0.0, 3.0, 3.0, 2.0)
        cards, labels = _jumble(iso)
        self.add(shadow, back, front, *cards, *labels)

        iso2 = Iso(0, -0.5, 1.1)
        shadow2 = _shadow(0, -1.85, 4.4, 1.0)
        card = iso2.page(-0.8, -1.0, 0.0, 1.6, 2.0)
        lab = T("step one: budget", size=34).next_to(card, RIGHT, buff=0.45)

        until(self, "Ask for one small job")
        self.play(FadeOut(back), FadeOut(front),
                  *[FadeOut(c) for c in cards], *[FadeOut(l) for l in labels], run_time=0.7)
        until(self, "Start with the part")
        self.play(FadeIn(shadow2), FadeIn(card, shift=np.array([0.0, 2.2, 0.0])), run_time=0.8, rate_func=ease_in)
        until(self, "what can we spend")
        self.play(FadeIn(lab), run_time=0.5)
        finish(self)


class B04_StepTwo(Scene):
    def construct(self):
        iso = Iso(0, -0.5, 1.1)
        shadow2 = _shadow(0, -1.85, 4.4, 1.0)
        cardB = iso.page(-0.8, -1.0, 0.0, 1.6, 2.0)
        labB = T("step one: budget", size=34).next_to(cardB, RIGHT, buff=0.45)
        self.add(shadow2, cardB, labB)

        shadowB = _shadow(0, -2.0, 7.6, 1.2)
        card1 = iso.page(-2.5, -1.0, 0.0, 1.5, 1.9)
        card2 = iso.page(1.0, -1.0, 0.0, 1.5, 1.9)
        arrow = Arrow(start=[-0.7, -1.0, 0.0], end=[0.8, -0.6, 0.0], color=INK, stroke_width=6, buff=0.1)
        toplab = T("step two: layout", size=34).move_to([0.0, 2.55, 0.0])
        chk1 = check(-2.1, -1.35, s=0.22, color=TERRA)

        until(self, "Then step two")
        self.play(FadeOut(cardB), FadeOut(labB), FadeOut(shadow2), FadeIn(shadowB), run_time=0.6)
        until(self, "The layout has to fit the budget")
        self.play(FadeIn(card1, shift=np.array([0.0, 2.0, 0.0])),
                  FadeIn(card2, shift=np.array([0.0, 2.0, 0.0])), run_time=0.9, rate_func=ease_in)
        until(self, "hand the AI the number")
        self.play(Create(arrow), FadeIn(toplab), run_time=0.8)
        until(self, "designing inside your answer")
        self.play(FadeIn(chk1), run_time=0.5)
        finish(self)


class B05_Materials(Scene):
    def construct(self):
        iso = Iso(0, -0.5, 1.1)
        shadowB = _shadow(0, -2.0, 7.6, 1.2)
        card1 = iso.page(-2.5, -1.0, 0.0, 1.5, 1.9)
        card2 = iso.page(1.0, -1.0, 0.0, 1.5, 1.9)
        arrow12 = Arrow(start=[-0.7, -1.0, 0.0], end=[0.8, -0.6, 0.0], color=INK, stroke_width=6, buff=0.1)
        toplab = T("step two: layout", size=34).move_to([0.0, 2.55, 0.0])
        chk1 = check(-2.1, -1.35, s=0.22, color=TERRA)
        self.add(shadowB, card1, card2, arrow12, toplab, chk1)

        shadowB3 = _shadow(0.8, -2.0, 9.4, 1.2)
        card3 = iso.page(3.5, -1.0, 0.0, 1.5, 1.9)
        arrow23 = Arrow(start=[2.6, 0.95, 0.0], end=[3.2, 1.3, 0.0], color=INK, stroke_width=6, buff=0.1)
        toplab3 = T("step three: materials", size=34).move_to([0.0, 2.55, 0.0])
        chk2 = check(1.71, 0.15, s=0.22, color=TERRA)
        chk3 = check(4.1, 1.8, s=0.22, color=TERRA)

        until(self, "Then materials")
        self.play(FadeOut(shadowB), FadeOut(toplab), FadeIn(shadowB3),
                  FadeIn(card3, shift=np.array([0.0, 2.0, 0.0])), run_time=0.9, rate_func=ease_in)
        until(self, "can't hold them")
        self.play(Create(arrow23), FadeIn(toplab3), run_time=0.7)
        until(self, "check in one glance")
        self.play(FadeIn(chk2), FadeIn(chk3), run_time=0.5)
        finish(self)


class B06_Timeline(Scene):
    def construct(self):
        iso = Iso(0, -0.5, 1.1)
        shadowB3 = _shadow(0.8, -2.0, 9.4, 1.2)
        card1 = iso.page(-2.5, -1.0, 0.0, 1.5, 1.9)
        card2 = iso.page(1.0, -1.0, 0.0, 1.5, 1.9)
        card3 = iso.page(3.5, -1.0, 0.0, 1.5, 1.9)
        arrow12 = Arrow(start=[-0.7, -1.0, 0.0], end=[0.8, -0.6, 0.0], color=INK, stroke_width=6, buff=0.1)
        arrow23 = Arrow(start=[2.6, 0.95, 0.0], end=[3.2, 1.3, 0.0], color=INK, stroke_width=6, buff=0.1)
        toplab3 = T("step three: materials", size=34).move_to([0.0, 2.55, 0.0])
        chk1 = check(-2.1, -1.35, s=0.22, color=TERRA)
        chk2 = check(1.71, 0.15, s=0.22, color=TERRA)
        chk3 = check(4.1, 1.8, s=0.22, color=TERRA)
        self.add(shadowB3, card1, card2, card3, arrow12, arrow23, toplab3, chk1, chk2, chk3)
        g = VGroup(shadowB3, card1, card2, card3, arrow12, arrow23, toplab3, chk1, chk2, chk3)

        card4 = iso.page(4.0, -1.0, 0.0, 1.5, 1.9)
        arrow34 = Arrow(start=[2.25, 2.1, 0.0], end=[3.7, 1.75, 0.0], color=INK, stroke_width=6, buff=0.1)
        toplab4 = T("step four: timeline", size=34).move_to([0.0, 2.55, 0.0])
        chk4 = check(4.57, 2.08, s=0.22, color=TERRA)

        until(self, "And the timeline comes last")
        self.play(g.animate.shift(np.array([-1.4, 0.0, 0.0])),
                  FadeIn(card4, shift=np.array([0.0, 2.0, 0.0])), run_time=1.0, rate_func=ease_in)
        until(self, "materials into timeline")
        self.play(FadeOut(toplab3), Create(arrow34), FadeIn(toplab4), run_time=0.7)
        until(self, "That handoff is the whole trick")
        self.play(FadeIn(chk4), run_time=0.5)
        finish(self)


class B07_SideBySide(Scene):
    def construct(self):
        iso = Iso(0, -0.5, 1.1)
        shadowB3 = _shadow(0.8, -2.0, 9.4, 1.2)
        card1 = iso.page(-2.5, -1.0, 0.0, 1.5, 1.9)
        card2 = iso.page(1.0, -1.0, 0.0, 1.5, 1.9)
        card3 = iso.page(3.5, -1.0, 0.0, 1.5, 1.9)
        card4 = iso.page(4.0, -1.0, 0.0, 1.5, 1.9)
        arrow12 = Arrow(start=[-0.7, -1.0, 0.0], end=[0.8, -0.6, 0.0], color=INK, stroke_width=6, buff=0.1)
        arrow23 = Arrow(start=[2.6, 0.95, 0.0], end=[3.2, 1.3, 0.0], color=INK, stroke_width=6, buff=0.1)
        arrow34 = Arrow(start=[2.25, 2.1, 0.0], end=[3.7, 1.75, 0.0], color=INK, stroke_width=6, buff=0.1)
        toplab4 = T("step four: timeline", size=34).move_to([0.0, 2.55, 0.0])
        chk1 = check(-2.1, -1.35, s=0.22, color=TERRA)
        chk2 = check(1.71, 0.15, s=0.22, color=TERRA)
        chk3 = check(4.1, 1.8, s=0.22, color=TERRA)
        chk4 = check(4.57, 2.08, s=0.22, color=TERRA)
        self.add(shadowB3, card1, card2, card3, card4, arrow12, arrow23, arrow34, toplab4,
                 chk1, chk2, chk3, chk4)

        isoM = Iso(-3.2, -0.5, 0.8)
        mush = isoM.page(0.0, 0.0, 0.0, 2.2, 2.6)
        scrib = _zigzag(isoM, [(0.3, 0.4), (1.9, 0.8), (0.4, 1.3), (1.8, 1.8), (0.5, 2.2)])
        shM = _shadow(-3.0, -1.15, 4.6, 1.0)
        isoS = Iso(2.6, -0.8, 0.9)
        stack = VGroup(*[isoS.page(-0.7, -0.6, i * 0.55, 1.4, 1.2) for i in range(4)])
        shS = _shadow(2.6, -1.75, 3.6, 0.9)
        labelL = T("one giant prompt", size=32).move_to([-3.4, 2.15, 0.0])
        labelR = T("small steps", size=32).move_to([2.6, 2.35, 0.0])
        topchk = check(3.1, 0.75, s=0.2, color=TERRA)

        until(self, "On the left")
        self.play(FadeOut(shadowB3), FadeOut(card1), FadeOut(card2), FadeOut(card3), FadeOut(card4),
                  FadeOut(arrow12), FadeOut(arrow23), FadeOut(arrow34), FadeOut(toplab4),
                  FadeOut(chk1), FadeOut(chk2), FadeOut(chk3), FadeOut(chk4),
                  FadeIn(shM), FadeIn(mush), FadeIn(shS), FadeIn(stack),
                  FadeIn(labelL), FadeIn(labelR), run_time=1.0)
        until(self, "Everything at once")
        self.play(Create(scrib), run_time=0.7)
        until(self, "Small steps, big jobs")
        self.play(FadeIn(topchk), run_time=0.5)
        finish(self)


class B08_OneJob(Scene):
    def construct(self):
        isoM = Iso(-3.2, -0.5, 0.8)
        mush = isoM.page(0.0, 0.0, 0.0, 2.2, 2.6)
        scrib = _zigzag(isoM, [(0.3, 0.4), (1.9, 0.8), (0.4, 1.3), (1.8, 1.8), (0.5, 2.2)])
        shM = _shadow(-3.0, -1.15, 4.6, 1.0)
        isoS = Iso(2.6, -0.8, 0.9)
        stack = VGroup(*[isoS.page(-0.7, -0.6, i * 0.55, 1.4, 1.2) for i in range(4)])
        shS = _shadow(2.6, -1.75, 3.6, 0.9)
        labelL = T("one giant prompt", size=32).move_to([-3.4, 2.15, 0.0])
        labelR = T("small steps", size=32).move_to([2.6, 2.35, 0.0])
        topchk = check(3.1, 0.75, s=0.2, color=TERRA)
        self.add(shM, mush, scrib, shS, stack, labelL, labelR, topchk)

        rule = RoundedRectangle(width=4.6, height=0.95, corner_radius=0.45,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=3).move_to([0.0, 2.62, 0.0])
        rule_text = T("one job per prompt", size=40).move_to([0.0, 2.62, 0.0])
        bigcheck = check(2.85, 2.62, s=0.26, color=TERRA)

        until(self, "One job per prompt")
        self.play(FadeOut(labelL), FadeOut(labelR), FadeIn(rule), FadeIn(rule_text), run_time=0.7)
        until(self, "split it in half")
        self.play(FadeIn(bigcheck), run_time=0.5)
        finish(self)
