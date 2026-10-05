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

# ═════════════════════════════ FILM: the-long-game ═════════════════════════════
# Show-tell body scenes: one isometric drawing per beat, Claude palette.
# Cast, kept the same all film: the stack of pages (the finished document),
# the outline card (the skeleton, with its section rows), section pages,
# ink arrows (the handoff between sections), terracotta checks and dots
# (flags and approvals), the scan line (the stitching read-through).
# Labels sit beside objects, never inside; text >= 32.
# Pacing is narration-driven via until()/finish() from the kit above.
# Class names are literal `class BNN_Name(Scene):` so run.sh finds them.

def _shadow(x, y, w, h):
    return Ellipse(width=w, height=h, color=GHOST, fill_opacity=1, stroke_width=0).move_to([x, y, 0.0])


def _stack(iso, x0, y0, w=2.2, d=2.8, n=5, step=0.16):
    """The document as a neat stack of pages."""
    return VGroup(*[iso.page(x0, y0, i * step, w, d) for i in range(n)])


def _jumble(iso):
    """Five pages scattered: the all-at-once mess. (x0, y0, w, d, rotation)"""
    spec = [(-3.6, 0.7, 1.7, 2.1, 0.18),
            (-1.0, 1.2, 1.7, 2.1, -0.22),
            (1.8, 0.9, 1.7, 2.1, 0.12),
            (-2.4, -1.7, 1.7, 2.1, -0.10),
            (0.6, -1.8, 1.7, 2.1, 0.25)]
    pages = []
    for x, y, w, d, ang in spec:
        p = iso.page(x, y, 0.0, w, d)
        p.rotate(ang)
        pages.append(p)
    return pages


def _jumble2(iso):
    """A tighter four-page jumble for the side-by-side's left half."""
    spec = [(-3.9, 0.6, 1.4, 1.8, 0.18),
            (-2.3, 1.2, 1.4, 1.8, -0.20),
            (-1.4, -0.9, 1.4, 1.8, 0.12),
            (-3.3, -1.5, 1.4, 1.8, -0.14)]
    pages = []
    for x, y, w, d, ang in spec:
        p = iso.page(x, y, 0.0, w, d)
        p.rotate(ang)
        pages.append(p)
    return pages


def _flag(iso, x, y, w, d, r=0.11):
    """A terracotta flag dot on a page: something the voice calls out."""
    return Dot(iso.p(x + w / 2, y + d / 2, 0.12), radius=r, color=TERRA)


def _outline_card(iso, x0, y0, w=2.4, d=3.0):
    """The skeleton: a white card with its numbered section rows. Returns (group, rows)."""
    card = iso.box(x0, y0, 0.0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
    rows = []
    for i, (name, yy) in enumerate(zip(["the need", "the plan", "the budget", "the team"],
                                       [y0 + d - 0.55, y0 + d - 1.35, y0 + d - 2.15, y0 + d - 2.95])):
        t = T(f"{i + 1}  {name}", size=32)
        p = iso.p(x0 + 0.28, yy, 0.10)
        t.move_to([p[0] + t.width / 2, p[1], 0.0])
        rows.append(t)
    return VGroup(card, *rows), rows


class B00_Stack(Scene):
    def construct(self):
        iso = Iso(0, -0.5, 1.0)
        shadow = _shadow(0, -2.5, 6.4, 1.3)
        stack = _stack(iso, -1.1, -1.4)
        label = T("the goal", size=36).move_to([-4.55, 1.35, 0.0])
        leader = Line([-3.7, 1.2, 0.0], [-2.85, 0.72, 0.0], color=INK, stroke_width=3)
        title = Line(iso.p(-0.9, 0.9, 0.78), iso.p(0.7, 0.9, 0.78), color=INK, stroke_width=6)
        self.play(FadeIn(shadow), run_time=0.3)
        self.play(FadeIn(stack, shift=np.array([0.0, 2.6, 0.0])), rate_func=ease_in, run_time=0.7)
        until(self, "Start with the goal")
        self.play(FadeIn(label), FadeIn(leader), run_time=0.5)
        until(self, "reads like one person")
        self.play(Create(title), run_time=0.5)
        finish(self)


class B01_AllAtOnce(Scene):
    def construct(self):
        iso = Iso(0, -0.5, 1.0)
        shadow = _shadow(0, -2.5, 6.4, 1.3)
        stack = _stack(iso, -1.1, -1.4)
        goal = T("the goal", size=36).move_to([-4.55, 1.35, 0.0])
        glead = Line([-3.7, 1.2, 0.0], [-2.85, 0.72, 0.0], color=INK, stroke_width=3)
        self.add(shadow, stack, goal, glead)

        pages = _jumble(iso)
        d1 = _flag(iso, -1.0, 1.2, 1.7, 2.1)
        d2 = _flag(iso, -2.4, -1.7, 1.7, 2.1)
        d3 = _flag(iso, 1.8, 0.9, 1.7, 2.1)
        label = T("all at once", size=36).move_to([-4.35, 2.05, 0.0])
        leader = Line([-3.35, 1.9, 0.0], [-2.75, 1.35, 0.0], color=INK, stroke_width=3)

        until(self, "So she asked for the whole thing")
        self.play(FadeOut(stack), FadeOut(goal), FadeOut(glead),
                  *[FadeIn(p, shift=np.array([0.0, 1.6, 0.0])) for p in pages],
                  run_time=0.9, rate_func=ease_in)
        until(self, "Out came twenty pages")
        self.play(FadeIn(label), FadeIn(leader), run_time=0.5)
        until(self, "the middle repeated the beginning")
        self.play(FadeIn(d1), FadeIn(d2), run_time=0.4)
        until(self, "page twelve contradicted page three")
        self.play(FadeIn(d3), run_time=0.4)
        finish(self)


class B02_Drift(Scene):
    def construct(self):
        iso = Iso(0, -0.5, 1.0)
        shadow = _shadow(0, -2.5, 6.4, 1.3)
        old = _jumble(iso)
        self.add(shadow, *old)

        iso2 = Iso(0, -0.3, 1.0)
        shadow2 = _shadow(0, -2.35, 9.6, 1.3)
        pa = iso2.page(-4.35, -1.35, 0.0, 1.9, 2.4)
        pb = iso2.page(-0.95, -1.35, 0.0, 1.9, 2.4)
        pc = iso2.page(2.45, -1.35, 0.0, 1.9, 2.4)
        n3 = T("3", size=32).move_to(iso2.p(-4.35 + 0.35, -1.35 + 0.42, 0.10))
        n9 = T("9", size=32).move_to(iso2.p(-0.95 + 0.35, -1.35 + 0.42, 0.10))
        n14 = T("14", size=32).move_to(iso2.p(2.45 + 0.35, -1.35 + 0.42, 0.10))
        drift = T("it drifts", size=32).move_to([0.0, 2.6, 0.0])
        f1 = _flag(iso2, -0.95 + 0.35, -1.35 + 1.45, 1.0, 0.6, r=0.10)
        f2 = _flag(iso2, -0.95 + 0.95, -1.35 + 1.45, 1.0, 0.6, r=0.10)
        f3 = _flag(iso2, 2.45 + 0.55, -1.35 + 1.05, 1.0, 0.6, r=0.10)
        staple = VGroup(Line([-1.2, 1.05, 0.0], [1.4, 1.05, 0.0], color=INK, stroke_width=5),
                        Line([-1.2, 1.05, 0.0], [-1.2, 0.72, 0.0], color=INK, stroke_width=5),
                        Line([1.4, 1.05, 0.0], [1.4, 0.72, 0.0], color=INK, stroke_width=5))

        until(self, "Here\u2019s why")
        self.play(*[FadeOut(p) for p in old], FadeOut(shadow),
                  FadeIn(shadow2), FadeIn(pa), FadeIn(pb), FadeIn(pc), run_time=0.7)
        until(self, "Nobody can keep twenty pages straight")
        self.play(FadeIn(n3), FadeIn(n9), FadeIn(n14), FadeIn(drift), run_time=0.5)
        until(self, "Facts drift")
        self.play(FadeIn(f1), FadeIn(f2), run_time=0.3)
        until(self, "the tone wobbles")
        self.play(FadeIn(f3), run_time=0.3)
        until(self, "five short ones")
        self.play(Create(staple), run_time=0.4)
        finish(self)


class B03_Outline(Scene):
    def construct(self):
        iso2 = Iso(0, -0.3, 1.0)
        shadow2 = _shadow(0, -2.35, 9.6, 1.3)
        pa = iso2.page(-4.35, -1.35, 0.0, 1.9, 2.4)
        pb = iso2.page(-0.95, -1.35, 0.0, 1.9, 2.4)
        pc = iso2.page(2.45, -1.35, 0.0, 1.9, 2.4)
        drift = T("it drifts", size=32).move_to([0.0, 2.6, 0.0])
        self.add(shadow2, pa, pb, pc, drift)

        iso = Iso(0, -0.4, 1.0)
        shadow = _shadow(0, -2.5, 5.2, 1.1)
        oc, rows = _outline_card(iso, -1.2, -1.5)
        cp = iso.p(0.7, 1.0, 0.10)
        chk = check(cp[0], cp[1], s=0.24, color=TERRA)
        label = T("move one: outline", size=32).move_to([0.0, 2.75, 0.0])

        until(self, "Move one: the outline")
        self.play(FadeOut(pa), FadeOut(pb), FadeOut(pc), FadeOut(drift), FadeOut(shadow2),
                  FadeIn(shadow), FadeIn(oc), run_time=0.7)
        until(self, "section-by-section skeleton")
        self.play(*[Create(r) for r in rows], run_time=1.0)
        until(self, "approve it")
        self.play(FadeIn(chk), run_time=0.4)
        until(self, "The outline is the contract")
        self.play(FadeIn(label), run_time=0.4)
        finish(self)


class B04_SectionOne(Scene):
    def construct(self):
        iso = Iso(0, -0.4, 1.0)
        shadow = _shadow(0, -2.5, 5.2, 1.1)
        oc, _rows = _outline_card(iso, -1.2, -1.5)
        self.add(shadow, oc)

        iso2 = Iso(2.4, -0.5, 0.9)
        page = iso2.page(0.0, 0.0, 0.0, 1.7, 2.2)
        arrow = Arrow(start=[-0.55, 0.35, 0.0], end=[1.15, 0.1, 0.0], color=INK, stroke_width=6, buff=0.1)
        label = T("move two: sections", size=32).move_to([0.0, 2.75, 0.0])
        chk = check(2.35, 0.75, s=0.22, color=TERRA)

        until(self, "Move two")
        self.play(oc.animate.shift(np.array([-1.8, 0.0, 0.0])),
                  FadeIn(page, shift=np.array([0.0, 2.0, 0.0])), run_time=0.8, rate_func=ease_in)
        until(self, "writes section one")
        self.play(Create(arrow), FadeIn(label), run_time=0.7)
        until(self, "check in one sitting")
        self.play(FadeIn(chk), run_time=0.4)
        finish(self)


class B05_Handoff(Scene):
    def construct(self):
        iso = Iso(0, -0.4, 1.0)
        shadow = _shadow(0, -2.5, 5.2, 1.1)
        oc, _rows = _outline_card(iso, -1.2, -1.5)
        oc.shift(np.array([-1.8, 0.0, 0.0]))
        iso2 = Iso(2.4, -0.5, 0.9)
        page1 = iso2.page(0.0, 0.0, 0.0, 1.7, 2.2)
        arrow1 = Arrow(start=[-0.55, 0.35, 0.0], end=[1.15, 0.1, 0.0], color=INK, stroke_width=6, buff=0.1)
        chk1 = check(2.35, 0.75, s=0.22, color=TERRA)
        lab = T("move two: sections", size=32).move_to([0.0, 2.75, 0.0])
        self.add(shadow, oc, page1, arrow1, chk1, lab)

        page2 = iso2.page(-1.9, -1.9, 0.0, 1.7, 2.2)
        arrow2 = Arrow(start=[-0.5, 0.1, 0.0], end=[1.5, -0.95, 0.0], color=INK, stroke_width=6, buff=0.1)
        arrow3 = Arrow(start=[2.0, -0.35, 0.0], end=[2.0, -0.85, 0.0], color=INK, stroke_width=6, buff=0.08)
        chk2 = check(2.35, -1.05, s=0.22, color=TERRA)
        label = T("move three: the handoff", size=32).move_to([0.0, 2.75, 0.0])

        until(self, "Move three is the handoff")
        self.play(FadeOut(lab), FadeOut(chk1),
                  FadeIn(page2, shift=np.array([0.0, 2.0, 0.0])), run_time=0.8, rate_func=ease_in)
        until(self, "gets the outline")
        self.play(Create(arrow2), run_time=0.6)
        until(self, "plus section one")
        self.play(Create(arrow3), run_time=0.6)
        until(self, "That is what keeps")
        self.play(FadeIn(chk2), FadeIn(label), run_time=0.5)
        finish(self)


class B06_Stitching(Scene):
    def construct(self):
        iso = Iso(0, -0.3, 0.9)
        shadow = _shadow(0, -2.35, 10.4, 1.3)
        pages = [iso.page(x0, 0.0, 0.0, 1.7, 2.2) for x0 in (-3.9, 0.0, 3.9)]
        nums = [T(s, size=32).move_to(iso.p(x0 + 1.35, 0.35, 0.10))
                for x0, s in zip((-3.9, 0.0, 3.9), ("1", "2", "3"))]
        dup = Line(iso.p(0.25, 1.45, 0.10), iso.p(1.45, 1.45, 0.10), color=INK, stroke_width=6)
        scan = Line([-5.2, 1.9, 0.0], [5.2, 1.9, 0.0], color=TERRA, stroke_width=5)
        label = T("the stitching", size=36).move_to([0.0, 2.7, 0.0])
        self.add(shadow)

        until(self, "Then the stitching")
        self.play(*[FadeIn(p, shift=np.array([0.0, 1.8, 0.0])) for p in pages],
                  *[FadeIn(n) for n in nums], FadeIn(dup), run_time=0.9, rate_func=ease_in)
        until(self, "Read the whole thing end to end")
        self.play(FadeIn(scan), run_time=0.3)
        until(self, "out loud if you can")
        self.play(scan.animate.shift(np.array([0.0, -3.4, 0.0])), run_time=1.2)
        until(self, "and fix only the seams")
        self.play(FadeOut(scan), FadeOut(dup, shift=np.array([0.0, 0.9, 0.0])), run_time=0.5)
        until(self, "You are not rewriting")
        self.play(FadeIn(label), run_time=0.4)
        finish(self)


class B07_SideBySide(Scene):
    def construct(self):
        iso6 = Iso(0, -0.3, 0.9)
        shadow6 = _shadow(0, -2.35, 10.4, 1.3)
        old_pages = [iso6.page(x0, 0.0, 0.0, 1.7, 2.2) for x0 in (-3.9, 0.0, 3.9)]
        old_label = T("the stitching", size=36).move_to([0.0, 2.7, 0.0])
        shadow = _shadow(0, -2.45, 11.6, 1.3)
        self.add(shadow6, *old_pages, old_label)

        jl = Iso(-0.6, -0.5, 0.9)
        left = _jumble2(jl)
        llab = T("one giant prompt", size=34).move_to([-3.4, 1.35, 0.0])
        llead = Line([-2.75, 1.15, 0.0], [-2.5, 0.5, 0.0], color=INK, stroke_width=3)

        jr = Iso(2.9, -0.5, 0.95)
        right = _stack(jr, -1.0, -1.3, w=2.0, d=2.6, n=4, step=0.18)
        rchk = check(3.0, 0.1, s=0.24, color=TERRA)
        rlab = T("the long game", size=34).move_to([2.9, 1.9, 0.0])
        rlead = Line([2.5, 1.7, 0.0], [2.62, 0.75, 0.0], color=INK, stroke_width=3)

        until(self, "Same proposal, same AI")
        self.play(*[FadeOut(p) for p in old_pages], FadeOut(old_label), FadeOut(shadow6),
                  FadeIn(shadow), *[FadeIn(p) for p in left], run_time=0.8)
        until(self, "On the left")
        self.play(FadeIn(llab), FadeIn(llead), run_time=0.4)
        until(self, "On the right")
        self.play(FadeIn(right), FadeIn(rchk), run_time=0.8)
        until(self, "A document that holds together")
        self.play(FadeIn(rlab), FadeIn(rlead), run_time=0.4)
        finish(self)


class B08_Habit(Scene):
    def construct(self):
        jl = Iso(-0.6, -0.5, 0.9)
        left = _jumble2(jl)
        jr = Iso(2.9, -0.5, 0.95)
        right = _stack(jr, -1.0, -1.3, w=2.0, d=2.6, n=4, step=0.18)
        shadow = _shadow(0, -2.45, 11.6, 1.3)
        self.add(shadow, *left, right)

        card = Rectangle(width=4.8, height=3.4, fill_color=CARD, fill_opacity=1,
                         stroke_color=INK, stroke_width=4).move_to([0.0, 0.05, 0.0])
        r1 = T("outline first", size=32).move_to([0.0, 0.95, 0.0])
        r2 = T("one section per prompt", size=32).move_to([0.0, 0.15, 0.0])
        r3 = T("stitch at the end", size=32).move_to([0.0, -0.65, 0.0])
        chk = check(1.95, -1.15, s=0.24, color=TERRA)

        until(self, "Make it a habit")
        self.play(*[FadeOut(p) for p in left], FadeOut(right), FadeIn(card), run_time=0.7)
        until(self, "Outline first")
        self.play(Create(r1), run_time=0.4)
        until(self, "One section per prompt")
        self.play(Create(r2), run_time=0.4)
        until(self, "Stitch at the end")
        self.play(Create(r3), run_time=0.4)
        until(self, "play it in three moves")
        self.play(FadeIn(chk), run_time=0.4)
        finish(self)
