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
# show-tell-the-creative-engineer. Cast: the SKETCH (white page = design), the CODE (dark block =
# engineering), the BOX (kraft = the built thing); terracotta tape = the one somebody judged worth making.

def small_box(ox, oy, s=0.36, w=2.4, d=2.4, h=1.7, taped=False):
    iso = Iso(ox, oy, s)
    g = VGroup(iso.box(0, 0, 0, w, d, h))
    if taped:
        g.add(iso.tape(0, 0, h, w, d, drop=0.3 * h))
    return g


def box_center_x(ox, s=0.36, w=2.4, d=2.4):
    return ox + (w - d) * C30 * s / 2


def shadow_under(ox, oy, s=0.36, w=2.4, d=2.4):
    iso = Iso(ox, oy, s)
    sh = iso.quad([(0.1, -0.3, 0), (w + 0.3, -0.3, 0), (w + 0.3, d - 0.1, 0), (0.1, d - 0.1, 0)], "#BFB4A0", sw=0)
    sh.set_z_index(-1)
    return sh


BAR_W = 1.5
BASE_Y = -2.3
UNIT = 4.4 / 161          # 161 minutes → 4.4 units tall


class B00_Cheap(Scene):
    def construct(self):
        left = Rectangle(width=BAR_W, height=0.01, fill_color=BAR2, fill_opacity=1, stroke_width=0).move_to([-2.2, BASE_Y, 0], aligned_edge=DOWN)
        right = Rectangle(width=BAR_W, height=0.01, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([2.2, BASE_Y, 0], aligned_edge=DOWN)
        self.add(left, right)
        until(self, "build the same small web server")
        self.play(left.animate.stretch_to_fit_height(161 * UNIT).move_to([-2.2, BASE_Y, 0], aligned_edge=DOWN),
                  right.animate.stretch_to_fit_height(161 * UNIT).move_to([2.2, BASE_Y, 0], aligned_edge=DOWN), run_time=1.6)
        self.play(FadeIn(T("alone", 40).move_to([-2.2, -2.9, 0])), FadeIn(T("with Copilot", 40).move_to([2.2, -2.9, 0])), run_time=0.5)
        until(self, "a hundred and sixty minutes")
        n161 = T("161 min", 44, bold=True).move_to([-2.2, BASE_Y + 161 * UNIT + 0.45, 0])
        self.play(FadeIn(n161, shift=DOWN * 0.15), run_time=0.5)
        until(self, "took about seventy")
        n71 = T("71 min", 44, bold=True).move_to([2.2, BASE_Y + 71 * UNIT + 0.45, 0])
        self.play(right.animate.stretch_to_fit_height(71 * UNIT).move_to([2.2, BASE_Y, 0], aligned_edge=DOWN), run_time=1.4)
        self.play(FadeIn(n71, shift=DOWN * 0.15), run_time=0.5)
        until(self, "Building got cheap")
        dot = Dot([2.2 + BAR_W / 2 + 0.45, BASE_Y + 71 * UNIT - 0.25, 0], radius=0.14, color=TERRA)
        self.play(GrowFromCenter(dot), run_time=0.4)
        finish(self)


ROW_X = [-4.6, -2.3, 0.0, 2.3, 4.6]


class B01_Judgment(Scene):
    def construct(self):
        boxes = VGroup(*[small_box(x, -1.3) for x in ROW_X])
        for b in boxes:
            b.shift(UP * 4.2)
        self.add(boxes)
        until(self, "Anyone can make the box")
        self.play(LaggedStart(*[b.animate.shift(DOWN * 4.2) for b in boxes], lag_ratio=0.18, rate_func=ease_in), run_time=1.6)
        self.play(FadeIn(VGroup(*[shadow_under(x, -1.3) for x in ROW_X])), run_time=0.3)
        until(self, "The hard part")
        self.play(*[b.animate.set_fill(opacity=0.35) for i, b in enumerate(boxes) if i != 2], run_time=0.8)   # fills only: ink outlines keep Gate V contrast
        until(self, "whether it's any good")
        chosen = small_box(0.0, -1.3, taped=True)
        self.play(FadeOut(boxes[2]), FadeIn(chosen), run_time=0.3)
        self.play(chosen.animate.shift(UP * 0.9), run_time=0.7)
        until(self, "That's judgment")
        self.play(FadeIn(T("judgment", 44).move_to([0, -2.7, 0]), shift=UP * 0.2), run_time=0.6)
        finish(self)


class B02_DesignerBuilds(Scene):
    def construct(self):
        P = Iso(-4.0, -0.7, 0.95)   # page spans x -5.73..-2.6 (Gate V title-safe)
        sketch = P.page(0, 0, 0, w=1.7, d=2.1)
        self.play(FadeIn(sketch, shift=RIGHT * 0.3), run_time=0.7)
        self.play(FadeIn(T("sketch", 40).move_to([-4.2, -2.5, 0])), run_time=0.4)
        until(self, "turn a sketch into a working thing")
        line = CubicBezier(np.array([-2.4, 0.2, 0]), np.array([-1.0, 1.2, 0]), np.array([0.4, 1.2, 0]), np.array([1.6, 0.4, 0]),
                           color=INK, stroke_width=5)
        self.play(Create(line), run_time=0.9)
        first = small_box(2.4, -1.6, s=0.5)
        first.shift(UP * 4.5); self.add(first)
        self.play(first.animate.shift(DOWN * 4.5), run_time=0.8, rate_func=ease_in)
        until(self, "throw it out")
        self.play(first.animate.shift(DOWN * 3.0 + RIGHT * 1.2).rotate(-0.4), run_time=0.7, rate_func=ease_in)
        self.remove(first)
        until(self, "try again")
        second = small_box(2.4, -1.6, s=0.5, taped=True)
        second.shift(UP * 4.5); self.add(second)
        self.play(second.animate.shift(DOWN * 4.5), run_time=0.8, rate_func=ease_in)
        self.play(FadeIn(shadow_under(2.4, -1.6, s=0.5)), FadeIn(T("built", 40).move_to([box_center_x(2.4, 0.5) + 0.1, -2.5, 0])), run_time=0.5)
        finish(self)


class B03_CoderCompetes(Scene):
    def construct(self):
        L = Iso(-4.6, -0.6, 1.0)
        coder = L.mcp(0, 0, 0, 1.6, 1.6, 0.8)
        self.play(FadeIn(coder, shift=DOWN * 0.4), run_time=0.7)
        self.play(FadeIn(T("coder", 40).move_to([-4.6, -1.9, 0])), run_time=0.4)
        until(self, "the tools already do in minutes")
        spots = [(1.4, 0.4), (3.6, 0.4), (1.4, -1.5), (3.6, -1.5)]
        copies = VGroup(*[Iso(x, y, 0.75).mcp(0, 0, 0, 1.6, 1.6, 0.8) for x, y in spots])
        self.play(LaggedStart(*[GrowFromCenter(c) for c in copies], lag_ratio=0.35), run_time=2.2)
        self.play(FadeIn(T("AI", 44).move_to([2.5, -2.75, 0])), run_time=0.4)
        until(self, "on the machine's ground")
        ring = SurroundingRectangle(copies, buff=0.35, corner_radius=0.2, stroke_color=GHOST, stroke_width=4)
        self.play(Create(ring), run_time=0.8)
        finish(self)


class B04_Loop(Scene):
    def construct(self):
        loop = Circle(radius=1.35, color=DIM, stroke_width=6).move_to([-0.6, 0.3, 0])
        self.play(Create(loop), run_time=0.9)
        dot = Dot(loop.point_from_proportion(0), radius=0.13, color=TERRA)
        self.add(dot)
        until(self, "ten times in a day")
        pile = []
        for i in range(4):
            self.play(MoveAlongPath(dot, loop), run_time=0.55, rate_func=linear)
            v = small_box(3.2 + (i % 2) * 1.1, -1.9 + (i // 2) * 0.95, s=0.26)
            v.set_opacity(0.45 if i < 3 else 1.0)
            self.play(FadeIn(v, shift=RIGHT * 0.4), run_time=0.25)
            pile.append(v)
        self.play(FadeIn(T("versions", 40).move_to([3.9, -2.9, 0])), run_time=0.4)
        until(self, "which one is worth keeping")
        keep = small_box(-5.2, -1.5, s=0.36, taped=True)
        self.play(FadeIn(keep, shift=LEFT * 0.4), run_time=0.7)
        until(self, "That choice is yours")
        self.play(FadeIn(T("keep", 40).move_to([box_center_x(-5.2), -2.3, 0])), run_time=0.5)
        finish(self)


SLAB_X = [-4.8, -1.6, 1.6, 4.8]
VERBS = ["Ideate", "Build", "Brand", "Ship"]


def slab(x):
    return Iso(x, -0.9, 0.5).box(-1.1, -1.1, 0, 2.2, 2.2, 0.4)


class B05_FourVerbs(Scene):
    def construct(self):
        slabs, labels = [], []
        hopper = small_box(0, 0, s=0.22)
        cues = ["Ideate:", "Build:", "Brand:", "Ship:"]
        for i, (x, verb) in enumerate(zip(SLAB_X, VERBS)):
            until(self, cues[i], lead=0.4)
            s = slab(x); lab = T(verb, 42).move_to([x, -2.2, 0])
            slabs.append(s); labels.append(lab)
            target = np.array([x, 0.05, 0])
            if i == 0:
                hopper.move_to(target + UP * 3)
                self.play(FadeIn(s, shift=UP * 0.3), FadeIn(lab), hopper.animate.move_to(target), run_time=0.7)
            else:
                self.play(FadeIn(s, shift=UP * 0.3), FadeIn(lab), run_time=0.4)
                self.play(hopper.animate.move_to(target), run_time=0.5, rate_func=smooth)
        until(self, "Build is the one that got cheap")
        self.play(slabs[1].animate.set_fill(GHOST, opacity=1).set_stroke(GHOST), run_time=0.8)
        until(self, "The other three")
        dots = VGroup(*[Dot([SLAB_X[i], -2.75, 0], radius=0.11, color=TERRA) for i in (0, 2, 3)])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.3), run_time=0.9)
        finish(self)


HEIGHTS = [1.0, 2.4, 1.5, 2.9, 1.9]


class B06_Signal(Scene):
    def construct(self):
        def row(heights, taped_idx=None):
            return VGroup(*[small_box(x, -1.4, s=0.34, h=h, taped=(i == taped_idx)) for i, (x, h) in enumerate(zip(ROW_X, heights))])
        varied = row(HEIGHTS)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.3) for b in varied], lag_ratio=0.15), run_time=1.2)
        self.play(FadeIn(T("GitHub app", 40).move_to([0, -2.75, 0])), run_time=0.4)
        until(self, "they all start to look the same")
        same = row([1.7] * 5)
        self.play(*[Transform(a, b) for a, b in zip(varied, same)], run_time=1.2)
        until(self, "what you chose to make")
        chosen = small_box(ROW_X[3], -1.4, s=0.34, h=1.7, taped=True)
        self.play(FadeOut(varied[3]), FadeIn(chosen), run_time=0.3)
        self.play(chosen.animate.shift(UP * 0.8), *[b.animate.set_fill(opacity=0.35) for i, b in enumerate(varied) if i != 3], run_time=0.7)
        self.play(FadeIn(T("and why", 40).move_to([box_center_x(ROW_X[3], 0.34) + 0.05, 1.55, 0])), run_time=0.5)
        finish(self)


class B07_Both(Scene):
    def construct(self):
        M = Iso(0.0, -1.9, 0.7)
        W, D, H = 3.0, 3.0, 1.8
        back, front = M.open_box(0, 0, 0, W, D, H)
        self.play(FadeIn(back), FadeIn(front), run_time=0.5)
        page = Iso(-5.0, 0.2, 0.7).page(0, 0, 0, w=1.6, d=2.0)
        block = Iso(3.4, 0.4, 0.7).mcp(0, 0, 0, 1.4, 1.4, 0.7)
        page.set_z_index(1); block.set_z_index(1)
        until(self, "a designer who can build")
        self.play(FadeIn(page, shift=RIGHT * 0.3), FadeIn(block, shift=LEFT * 0.3), run_time=0.6)
        self.play(page.animate.move_to(M.p(1.0, 1.9, 0.6)), block.animate.move_to(M.p(2.0, 1.2, 0.5)), run_time=1.3)
        until(self, "your creative sense")
        lid = VGroup(M.box(0, 0, H, W, D, 0.2), M.tape(0, 0, H + 0.2, W, D, drop=0.3))
        lid.set_z_index(3)
        lid.shift(UP * 2.5); self.add(lid)
        self.play(lid.animate.shift(DOWN * 2.5), run_time=0.8, rate_func=ease_in)
        until(self, "worth more, not less")
        self.play(FadeIn(T("creative engineer", 44).move_to([0, -2.85, 0]), shift=UP * 0.2), run_time=0.6)
        finish(self)
