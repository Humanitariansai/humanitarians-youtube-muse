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


# ═════════════════════════════ the film ═════════════════════════════
# show-tell-costly-signals. Cast: CANDIDATES (sealed kraft boxes), SIGNALS (white page tags on top),
# a SORTER (grey lanes), AI (a dark server stack), terracotta tape = the costly, human part.
# Fades touch FILLS only, so the ink outlines keep Gate V contrast.

BS = 0.34                     # candidate box scale
BW, BD, BH = 2.4, 2.4, 1.7
ROW_X = [-4.4, -2.2, 0.0, 2.2, 4.4]
ROW_Y = -1.2


def cand(x, y=ROW_Y, s=BS, taped=False, tag=False):
    iso = Iso(x, y, s)
    g = VGroup(iso.box(0, 0, 0, BW, BD, BH))
    if taped:
        g.add(iso.tape(0, 0, BH, BW, BD, drop=0.3 * BH))
    if tag:
        g.add(tag_on(x, y, s))
    return g


def tag_on(x, y=ROW_Y, s=BS):
    return Iso(x, y, s).page(0.45, 0.45, BH, w=1.5, d=1.5)


def cand_shadow(x, y=ROW_Y, s=BS):
    iso = Iso(x, y, s)
    sh = iso.quad([(0.1, -0.3, 0), (BW + 0.3, -0.3, 0), (BW + 0.3, BD - 0.1, 0), (0.1, BD - 0.1, 0)], "#BFB4A0", sw=0)
    sh.set_z_index(-1)
    return sh


class B00_CantSee(Scene):
    def construct(self):
        row = VGroup(*[cand(x) for x in ROW_X])
        for b in row:
            b.shift(UP * 4.0)
        self.add(row)
        self.play(LaggedStart(*[b.animate.shift(DOWN * 4.0) for b in row], lag_ratio=0.15, rate_func=ease_in), run_time=1.6)
        self.play(FadeIn(VGroup(*[cand_shadow(x) for x in ROW_X])), run_time=0.3)
        until(self, "you can't see productivity")
        bracket = Line([-5.2, 1.0, 0], [5.2, 1.0, 0], color=DIM, stroke_width=6)
        self.play(Create(bracket), run_time=0.8)
        self.play(FadeIn(T("can't see inside", 42).move_to([0, 1.75, 0]), shift=DOWN * 0.15), run_time=0.5)
        until(self, "how does anyone choose")
        self.play(Wiggle(row[2], scale_value=1.05, rotation_angle=0.02 * TAU), run_time=0.9)
        finish(self)


class B01_Signal(Scene):
    def construct(self):
        self.add(VGroup(*[cand_shadow(x) for x in ROW_X]), VGroup(*[cand(x) for x in ROW_X]))
        until(self, "things you can show")
        tags = VGroup(*[tag_on(ROW_X[i]) for i in (1, 3)])
        for t in tags:
            t.shift(UP * 3.0)
        self.add(tags)
        self.play(LaggedStart(*[t.animate.shift(DOWN * 3.0) for t in tags], lag_ratio=0.3, rate_func=ease_in), run_time=1.1)
        self.play(FadeIn(T("signal", 42).move_to([0, -2.1, 0])), run_time=0.4)
        until(self, "a degree")
        marks = VGroup(*[Dot([ROW_X[i], -1.6, 0], radius=0.11, color=TERRA) for i in (1, 3)])   # new geometry for Gate A (moves alone don't count)
        self.play(Indicate(tags, color=None, scale_factor=1.12), LaggedStart(*[GrowFromCenter(m) for m in marks], lag_ratio=0.3), run_time=0.8)
        finish(self)


STAIR = Iso(-2.2, -2.3, 0.42)
STEP_W, STEP_D = 2.0, 2.4


def step_top(i, dx=0.5):
    return STAIR.p(i * STEP_W + dx * STEP_W, STEP_D * 0.5, 0.8 * (i + 1))


class B02_Costly(Scene):
    def construct(self):
        steps = VGroup(*[STAIR.box(i * STEP_W, 0, 0, STEP_W, STEP_D, 0.8 * (i + 1)) for i in range(4)])
        for i, st in enumerate(steps):
            st.set_z_index(-i)            # x runs right-UP (away from us): the front step is drawn last
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.3) for s in steps], lag_ratio=0.25), run_time=1.2)
        tag = STAIR.page(3 * STEP_W + 0.3, 0.4, 3.2, w=1.3, d=1.5); tag.set_z_index(1)
        self.play(FadeIn(tag, shift=DOWN * 0.3), run_time=0.4)
        until(self, "costlier for some")
        a = cand(0, 0, s=0.16); b = cand(0, 0, s=0.16); a.set_z_index(5); b.set_z_index(5)
        a.move_to(step_top(0, 0.3) + UP * 0.3); b.move_to(step_top(0, 0.75) + UP * 0.3)
        self.play(FadeIn(a), FadeIn(b), run_time=0.3)
        for i in (1, 2):
            self.play(a.animate.move_to(step_top(i, 0.3) + UP * 0.3), b.animate.move_to(step_top(min(i, 1), 0.75) + UP * 0.3), run_time=0.45)
        self.play(a.animate.move_to(step_top(3, 0.25) + UP * 0.3), run_time=0.45)
        until(self, "hard to fake cheaply")
        self.play(FadeIn(T("costly", 42).move_to([3.3, -1.2, 0])), run_time=0.4)
        finish(self)


STEM_END = np.array([-1.4, 0.0, 0])
UP_END = np.array([5.6, 1.5, 0]); DN_END = np.array([5.6, -1.5, 0])


def lanes():
    stem = Line([-5.8, 0, 0], STEM_END, color=DIM, stroke_width=8)
    up = Line(STEM_END, UP_END, color=DIM, stroke_width=8)
    dn = Line(STEM_END, DN_END, color=DIM, stroke_width=8)
    return stem, up, dn


class B03_Separating(Scene):
    def construct(self):
        stem, up, dn = lanes()
        self.play(Create(stem), run_time=0.6)
        self.play(Create(up), Create(dn), run_time=0.6)
        riders = [cand(0, 0, s=0.2, tag=(i % 2 == 0)) for i in range(4)]
        for i, r in enumerate(riders):
            r.move_to([-5.2 + i * 0.95, 0.35, 0])
        self.play(LaggedStart(*[FadeIn(r, shift=DOWN * 0.3) for r in riders], lag_ratio=0.2), run_time=0.9)
        until(self, "the signal separates people")
        ups = [r for i, r in enumerate(riders) if i % 2 == 0]; dns = [r for i, r in enumerate(riders) if i % 2 == 1]
        self.play(*[r.animate.move_to(UP_END + LEFT * (1.0 + k * 1.1) + UP * 0.1) for k, r in enumerate(ups)],
                  *[r.animate.move_to(DN_END + LEFT * (1.0 + k * 1.1) + UP * 0.1) for k, r in enumerate(dns)], run_time=1.4)
        until(self, "separating equilibrium")
        self.play(FadeIn(T("separating", 42).move_to([-3.6, -2.2, 0])), run_time=0.4)
        until(self, "a Nobel prize")
        dot = Dot([-3.6, -2.9, 0], radius=0.12, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.4)
        finish(self)


AI_ROW = [-1.6, 0.6, 2.8, 5.0]


class B04_AIPrints(Scene):
    def construct(self):
        S = Iso(-4.5, -1.2, 0.75)
        stack, lights = S.server(0, 0, 0, 1.4, 1.4, 0.46)
        self.add(stack, lights)
        self.add(VGroup(*[cand(x, s=0.3) for x in AI_ROW]))
        self.play(FadeIn(T("AI", 44).move_to([-4.3, -2.3, 0])), run_time=0.4)
        until(self, "nearly free")
        self.play(*[l.animate.set_color(TERRA) for l in lights], run_time=0.5)
        cues = ["A working demo app", "A clean cover letter", "A polished essay", "a logo"]
        for x, cue in zip(AI_ROW, cues):
            until(self, cue, lead=0.3)
            t = tag_on(x, s=0.3)
            start = S.p(0.7, 0.7, 1.5)
            t.move_to(start)
            self.add(t)
            self.play(t.animate.move_to(tag_on(x, s=0.3).get_center()), run_time=0.6)
        until(self, "less than half the time")
        self.play(Indicate(stack, color=None, scale_factor=1.05), run_time=0.8)
        finish(self)


class B05_Pooling(Scene):
    def construct(self):
        stem, up, dn = lanes()
        self.add(stem, up, dn)
        riders = [cand(0, 0, s=0.2, tag=True) for _ in range(4)]
        spots = [UP_END + LEFT * 1.0, UP_END + LEFT * 2.1, DN_END + LEFT * 1.0, DN_END + LEFT * 2.1]
        for r, p in zip(riders, spots):
            r.move_to(p + UP * 0.1)
        self.add(*riders)
        until(self, "it stops sorting")
        one = Line(STEM_END, [5.6, 0, 0], color=DIM, stroke_width=8)
        self.play(FadeOut(up), FadeOut(dn), Create(one), run_time=0.9)   # Create, not Transform: Gate A counts new geometry only
        pile = [np.array([4.6, 0.1, 0]), np.array([3.5, 0.1, 0]), np.array([2.4, 0.1, 0]), np.array([1.3, 0.1, 0])]
        self.play(*[r.animate.move_to(p) for r, p in zip(riders, pile)], run_time=1.0)
        until(self, "Spence called that pooling")
        self.play(FadeIn(T("pooling", 42).move_to([2.9, -1.3, 0])), run_time=0.4)
        until(self, "back to guessing")
        heap = RoundedRectangle(width=5.0, height=1.2, corner_radius=0.3, stroke_color=GHOST, stroke_width=5).move_to([2.95, 0.15, 0])
        self.play(Create(heap), *[r.animate.set_fill(opacity=0.4) for r in riders], run_time=0.8)   # new geometry for Gate A
        finish(self)


class B06_StillCostly(Scene):
    def construct(self):
        row = VGroup(*[cand(x, tag=True) for x in ROW_X])
        self.add(VGroup(*[cand_shadow(x) for x in ROW_X]), row)
        until(self, "what didn't get cheap")
        self.play(*[b.animate.set_fill(opacity=0.35) for i, b in enumerate(row) if i != 2], run_time=0.7)
        chosen = cand(ROW_X[2], taped=True)
        self.play(FadeOut(row[2]), FadeIn(chosen), run_time=0.3)
        self.play(chosen.animate.shift(UP * 1.2), run_time=0.7)
        dots = VGroup(*[Dot([-0.9 + k * 0.6, -2.0, 0], radius=0.12, color=TERRA) for k in range(4)])
        cues = ["Judgment", "Ideation", "Creative taste", "the effort"]
        for d, cue in zip(dots, cues):
            until(self, cue, lead=0.2)
            self.play(GrowFromCenter(d), run_time=0.35)
        self.play(FadeIn(T("judgment", 42).move_to([0, -2.75, 0])), run_time=0.4)
        finish(self)


PAGE_X = [0.8, 3.0, 5.1]
PAGE_LABELS = ["why", "versions", "users"]


class B07_ShowIt(Scene):
    def construct(self):
        M = Iso(-3.2, -2.0, 0.6)
        W, D, H = 2.8, 2.8, 1.8
        back, front = M.open_box(0, 0, 0, W, D, H)
        lid = VGroup(M.box(0, 0, H, W, D, 0.2), M.tape(0, 0, H + 0.2, W, D, drop=0.3))
        lid.set_z_index(3)
        self.add(back, front, lid)
        until(self, "show the expensive part")
        self.play(lid.animate.shift(UP * 2.2 + RIGHT * 0.5).set_opacity(0), run_time=0.9)
        cues = ["The problem you chose", "The versions you threw away", "What real users told you"]
        for x, lab, cue in zip(PAGE_X, PAGE_LABELS, cues):
            until(self, cue, lead=0.3)
            pg = Iso(x, 0.2, 0.55).page(0, 0, 0, w=1.5, d=1.9)
            start = M.p(1.4, 1.4, 1.2)
            pg.move_to(start); pg.set_z_index(1)
            self.add(pg)
            self.play(pg.animate.move_to(Iso(x, 0.2, 0.55).page(0, 0, 0, w=1.5, d=1.9).get_center()), run_time=0.7)
            self.play(FadeIn(T(lab, 40).move_to([x + 0.05, -0.9, 0])), run_time=0.3)
        until(self, "The reasons behind it")
        self.play(Indicate(front, color=None, scale_factor=1.04), run_time=0.7)
        finish(self)
