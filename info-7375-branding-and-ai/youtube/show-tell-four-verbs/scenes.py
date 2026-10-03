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
# show-tell-four-verbs — the DRAWN beats (B00–B04, B06, B09). B05/B07/B08 are ShowTellCard cards.
# Cast: four kraft SLABS (the verbs), the BOX (a project), the dark BLOCK (tech / an API),
# the white PAGE (a spec, documentation), terracotta = the move that matters.
# Fades touch fills only; every scene adds new geometry (Gate A sees only this file).

def small_box(ox, oy, s=0.34, w=2.4, d=2.4, h=1.7, taped=False):
    iso = Iso(ox, oy, s)
    g = VGroup(iso.box(0, 0, 0, w, d, h))
    if taped:
        g.add(iso.tape(0, 0, h, w, d, drop=0.3 * h))
    return g


SLAB_X = [-4.8, -1.6, 1.6, 4.8]
VERBS = ["Ideate", "Build", "Brand", "Ship"]


def slab(x, ghost=False):
    g = Iso(x, -0.9, 0.5).box(-1.1, -1.1, 0, 2.2, 2.2, 0.4)
    if ghost:
        g.set_fill(GHOST, opacity=1).set_stroke(DIM)
    return g


def on_slab(x):
    return np.array([x, 0.05, 0])


class B00_FourVerbs(Scene):
    def construct(self):
        # the engineer's project is on stage from the first second (Gate V empty-frame at 50%)
        proj = small_box(0.0, -0.9, s=0.42)
        shadow = Iso(0.0, -0.9, 0.42).quad([(0.1, -0.3, 0), (2.7, -0.3, 0), (2.7, 2.3, 0), (0.1, 2.3, 0)], "#BFB4A0", sw=0)
        shadow.set_z_index(-1)
        proj.shift(UP * 4); self.add(proj)
        self.play(proj.animate.shift(DOWN * 4), run_time=0.9, rate_func=rate_functions.ease_out_bounce)
        self.play(FadeIn(shadow), run_time=0.3)
        until(self, "invested accordingly")
        self.play(Wiggle(proj, scale_value=1.04, rotation_angle=0.02 * TAU), run_time=0.8)
        cues = ["Ideate.", "Build.", "Brand.", "Ship."]
        for k, (x, verb, c) in enumerate(zip(SLAB_X, VERBS, cues)):
            until(self, c, lead=0.25)
            s_ = slab(x)
            anims = [FadeIn(s_, shift=UP * 0.4), FadeIn(T(verb, 42).move_to([x, -2.2, 0]))]
            if k == 0:
                anims += [FadeOut(shadow), proj.animate.scale(0.22 / 0.42).move_to(on_slab(SLAB_X[0]))]
            self.play(*anims, run_time=0.4)
        finish(self)


class B01_Gap(Scene):
    def construct(self):
        spec = Iso(-5.4, 1.2, 0.45).page(0, 0, 0, w=1.6, d=2.0)
        blk = Iso(-2.6, 1.1, 0.5).mcp(0, 0, 0, 1.4, 1.4, 0.7)
        self.play(FadeIn(spec), FadeIn(blk), run_time=0.6)
        spec_lab = T("spec", 40).move_to([-5.1, 0.55, 0])
        self.play(FadeIn(spec_lab), run_time=0.3)
        until(self, "they'll build it")
        self.play(spec.animate.move_to(blk.get_center()).scale(0.4).set_opacity(0), FadeOut(spec_lab), run_time=0.7)
        out = small_box(0.3, 1.1, s=0.3)
        self.play(FadeIn(out, shift=RIGHT * 0.6), run_time=0.5)
        until(self, "whether it's worth building")
        shelf = Line([-5.3, -2.0, 0], [5.3, -2.0, 0], color=DIM, stroke_width=6)
        xs = [-4.3, -2.15, 0.0, 2.15, 4.3]
        boxes = VGroup(*[small_box(x, -1.95, s=0.3) for i, x in enumerate(xs) if i != 3])
        self.play(Create(shelf), LaggedStart(*[FadeIn(b, shift=DOWN * 0.3) for b in boxes], lag_ratio=0.15), run_time=1.0)
        until(self, "talking to real people")
        dot = Dot([-5.0, -2.35, 0], radius=0.12, color=TERRA)
        self.add(dot)
        self.play(dot.animate.move_to([xs[3], -2.35, 0]), run_time=1.3, rate_func=smooth)
        until(self, "a real gap")
        ghost = small_box(xs[3], -1.95, s=0.3)
        ghost.set_fill(opacity=0).set_stroke(DIM, width=4)
        self.play(Create(ghost), run_time=0.7)
        self.play(FadeIn(T("the gap", 40).move_to([xs[3], -2.95, 0])), run_time=0.4)
        finish(self)


class B02_TechFirst(Scene):
    def construct(self):
        B = Iso(-0.9, -1.6, 0.75)
        blk = B.mcp(0, 0, 0, 2.0, 2.0, 0.8)
        blk.shift(UP * 4); self.add(blk)
        self.play(blk.animate.shift(DOWN * 4), run_time=0.8, rate_func=ease_in)
        self.play(FadeIn(T("tech first", 42).move_to([-4.3, -1.3, 0])), run_time=0.4)
        until(self, "build a project around it")
        proj = B.box(0.3, 0.3, 0.8, 1.4, 1.4, 1.3)
        proj.set_z_index(2)
        self.play(FadeIn(proj, shift=UP * 0.5), run_time=0.8)
        until(self, "glue a user need on")
        tag = Iso(0, 0, 0.55).page(0, 0, 0, w=1.2, d=1.5)
        tag.rotate(0.5).move_to([2.9, 1.4, 0]); tag.set_z_index(3)
        self.play(FadeIn(tag), run_time=0.3)
        self.play(tag.animate.move_to([0.6, 0.2, 0]).rotate(-0.25), run_time=0.6)
        until(self, "nobody wanted")
        self.play(tag.animate.shift(DOWN * 2.6 + RIGHT * 1.2).rotate(-0.6).set_opacity(0), run_time=1.0, rate_func=ease_in)
        finish(self)


PLINTH_X = [-4.6, -2.3, 0.0, 2.3, 4.6]


def plinth_box(x, s=0.35):
    iso = Iso(x, -1.8, s)
    return VGroup(iso.box(0, 0, 0, 2.4, 2.4, 1.0, BOX_IN1, BOX_IN2, BOX_FLOOR), iso.box(0.3, 0.3, 1.0, 1.8, 1.8, 1.5))


class B03_Necessary(Scene):
    def construct(self):
        centre = plinth_box(0.0)
        self.play(FadeIn(centre, shift=UP * 0.4), run_time=0.7)
        until(self, "deep technical judgment")
        self.play(FadeIn(T("necessary", 42).move_to([0, -2.5, 0])), run_time=0.4)
        until(self, "no longer sets you apart")
        others = VGroup(*[plinth_box(x) for x in PLINTH_X if x != 0.0])
        self.play(LaggedStart(*[GrowFromCenter(o) for o in others], lag_ratio=0.2), run_time=1.3)
        until(self, "It isn't sufficient")
        self.play(FadeIn(T("not sufficient", 42).move_to([0, -3.1, 0])), run_time=0.4)
        finish(self)


class B04_Docs(Scene):
    def construct(self):
        A = Iso(2.4, -1.0, 0.8)
        api = A.mcp(0, 0, 0, 1.8, 1.8, 0.9)
        app = Iso(-4.6, -1.0, 0.8).mcp(0, 0, 0, 1.8, 1.8, 0.9)
        self.play(FadeIn(api), FadeIn(app), run_time=0.6)
        self.play(FadeIn(T("API", 44).move_to([2.9, -2.3, 0])), run_time=0.3)
        until(self, "can't tell what it's for")
        start = np.array([-3.0, -1.05, 0])
        mid = np.array([0.2, -1.6, 0])
        half = CubicBezier(start, start + np.array([1.2, -0.9, 0]), mid + np.array([-1.0, -0.4, 0]), mid, color=INK, stroke_width=5)
        self.play(Create(half), run_time=1.0)
        until(self, "Documentation isn't decoration")
        docs = A.page(0.2, 0.2, 0.9, w=1.4, d=1.4)
        docs.set_z_index(2)
        docs.shift(UP * 2.5); self.add(docs)
        self.play(docs.animate.shift(DOWN * 2.5), run_time=0.7, rate_func=ease_in)
        self.play(FadeIn(T("docs", 42).move_to([3.3, 1.35, 0])), run_time=0.3)
        until(self, "connects the API")
        end = A.p(0.0, 0.9, 0.45)
        rest = CubicBezier(mid, mid + np.array([1.0, 0.4, 0]), end + np.array([-0.8, -0.6, 0]), end, color=INK, stroke_width=5)
        self.play(Create(rest), run_time=0.8)
        lamp = Dot(A.p(1.8 * 0.2, 0, 0.9 * 0.75), radius=0.1, color=TERRA)
        self.play(GrowFromCenter(lamp), run_time=0.4)
        finish(self)


class B06_Ship(Scene):
    def construct(self):
        posts = VGroup(Iso(-1.3, -1.9, 0.5).box(0, 0, 0, 0.45, 0.45, 5.2, DARK_TOP, DARK_L, DARK_R),
                       Iso(1.1, -1.9, 0.5).box(0, 0, 0, 0.45, 0.45, 5.2, DARK_TOP, DARK_L, DARK_R))
        lintel = Line([-1.3, 0.95, 0], [1.5, 0.95, 0], color=DIM, stroke_width=8)
        self.play(FadeIn(posts, shift=UP * 0.3), Create(lintel), run_time=0.8)
        box = small_box(-4.6, -1.7, s=0.34); box.set_z_index(3)
        self.play(FadeIn(box), run_time=0.4)
        until(self, "a public link")
        self.play(box.animate.shift(RIGHT * 7.4), run_time=1.6, rate_func=smooth)
        self.play(FadeIn(T("public", 42).move_to([0.1, -2.7, 0])), run_time=0.4)
        until(self, "feedback from real use")
        target = np.array([3.9, -0.6, 0])
        curves = [CubicBezier(np.array([6.0, y, 0]), np.array([5.4, y, 0]), target + np.array([0.9, 0.2 * k, 0]), target, color=DIM, stroke_width=4)
                  for k, y in zip((1, 0, -1), (1.7, 0.1, -1.5))]
        self.play(*[Create(c) for c in curves], run_time=0.8)
        self.play(FadeIn(T("feedback", 42).move_to([5.0, 2.35, 0])), run_time=0.4)
        until(self, "every guess you made")
        dots = [Dot(c.get_start(), radius=0.1, color=TERRA) for c in curves]
        self.add(*dots)
        self.play(*[MoveAlongPath(d, c) for d, c in zip(dots, curves)], run_time=1.0, rate_func=linear)
        until(self, "real users touch it")
        taped = small_box(2.8, -1.7, s=0.34, taped=True); taped.set_z_index(3)
        self.play(FadeOut(box), FadeIn(taped), *[FadeOut(d) for d in dots], run_time=0.5)
        finish(self)


class B09_Career(Scene):
    def construct(self):
        slabs = VGroup(*[slab(x, ghost=(i == 1)) for i, x in enumerate(SLAB_X)])
        labels = VGroup(*[T(v, 42).move_to([x, -2.2, 0]) for x, v in zip(SLAB_X, VERBS)])
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.3) for s in slabs], lag_ratio=0.15), FadeIn(labels), run_time=1.0)
        hopper = small_box(0, 0, s=0.22)
        hopper.move_to(on_slab(SLAB_X[0]) + UP * 2.5); self.add(hopper)
        until(self, "A clear audience")
        self.play(hopper.animate.move_to(on_slab(SLAB_X[0])), run_time=0.4, rate_func=ease_in)
        for x in SLAB_X[1:]:
            self.play(hopper.animate.move_to(on_slab(x)), run_time=0.5)
        until(self, "Not a company")
        final = small_box(0, 0, s=0.22, taped=True); final.move_to(on_slab(SLAB_X[3]))
        self.play(FadeOut(hopper), FadeIn(final), run_time=0.3)
        until(self, "A career")
        self.play(FadeIn(T("a career", 44).move_to([4.8, 1.35, 0]), shift=DOWN * 0.15), run_time=0.5)
        finish(self)
