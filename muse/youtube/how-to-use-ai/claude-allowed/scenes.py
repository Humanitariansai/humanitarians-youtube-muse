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

# ═════════════════════════════ SCENES (show-tell, claude-allowed) ═════════════════════════════
# One isometric drawing per body beat. Same cast: the policy page. Liam explains.


class B00_PolicyPage(Scene):
    """The hero object: the AI-use policy. A highlighter lands on the exception."""

    def construct(self):
        iso = Iso(0.0, 0.15, 1.15)
        doc = VGroup(
            iso.page(-0.78, -0.62, 0.55, 1.56, 1.85),
            iso.page(-0.72, -0.57, 0.68, 1.56, 1.85),
        )
        label_a = T("AI-use policy", 36).move_to([-4.2, 1.9, 0])
        leader_a = Line([-3.7, 1.78, 0], [-2.15, 1.1, 0], color=INK, stroke_width=2.5)
        band = iso.quad(
            [(-0.55, 0.42, 0.76), (0.55, 0.42, 0.76),
             (0.55, 0.60, 0.76), (-0.55, 0.60, 0.76)],
            TERRA, sw=0)
        label_b = T("the exception", 36).move_to([2.55, 1.95, 0])
        leader_b = Line([0.25, 1.42, 0], [2.05, 1.83, 0], color=INK, stroke_width=2.5)

        self.play(FadeIn(doc), run_time=1.2)
        until(self, "Schools have one.")
        self.play(FadeIn(label_a), FadeIn(leader_a), run_time=0.9)
        until(self, "hides inside a single exception.")
        self.play(FadeIn(band), run_time=0.9)
        self.play(FadeIn(label_b), FadeIn(leader_b), run_time=0.9)
        finish(self)


class B01_Scope(Scene):
    """Six policy slips sort into two rows: banned vs open."""

    def construct(self):
        iso = Iso(0, -0.7, 1.0)
        head_ban = T("banned", 46, bold=True).move_to([-3.05, 2.45, 0])
        head_open = T("open", 46, bold=True).move_to([3.05, 2.45, 0])
        divider = Line([0, -2.7, 0], [0, 2.7, 0], color=DIM, stroke_width=3)

        self.play(FadeIn(head_ban), FadeIn(head_open), FadeIn(divider), run_time=1.0)

        banned = [("graded work", -4.5), ("as your own", -3.05), ("undisclosed", -1.6)]
        until(self, "That's the scope")
        for text, x in banned:
            slip = iso.page(0, 0, 0, 1.25, 1.5).move_to([x, -0.35, 0])
            cap = T(text, 34).move_to([x, -1.75, 0])
            self.play(FadeIn(slip), FadeIn(cap), run_time=0.8)

        opened = [("practice", 1.6), ("get fluent", 3.05), ("own time", 4.5)]
        until(self, "Not: never use AI.")
        for text, x in opened:
            slip = iso.page(0, 0, 0, 1.25, 1.5).move_to([x, -0.35, 0])
            cap = T(text, 34).move_to([x, -1.75, 0])
            self.play(FadeIn(slip), FadeIn(cap), run_time=0.8)

        until(self, "Not: never practice on your own time.")
        ok = check(4.5, 2.45, s=0.2, color=TERRA)
        self.play(FadeIn(ok), run_time=0.7)
        finish(self)


class B02_Trap(Scene):
    """The exception phrase splits into three readings; the envelope is the safe move."""

    def construct(self):
        plate = RoundedRectangle(width=8.6, height=1.1, corner_radius=0.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to([0, 2.0, 0])
        phrase = T("except for educational purposes", 40).move_to([0, 2.0, 0])
        cap = T("the exception", 36).move_to([0, 2.85, 0])

        self.play(FadeIn(plate), FadeIn(phrase), FadeIn(cap), run_time=1.2)

        until(self, "One teacher reads that")
        cons = VGroup(*[
            Line([x, 1.45, 0], [x, 0.9, 0], color="#9C8462", stroke_width=3)
            for x in (-3.5, 0.0, 3.5)
        ])
        self.play(FadeIn(cons), run_time=0.8)

        for reading, x in (("allow any use", -3.5), ("tools only", 0.0), ("no AI at all", 3.5)):
            card = RoundedRectangle(width=2.9, height=1.5, corner_radius=0.15,
                                    fill_color="#FFFFFF", fill_opacity=1,
                                    stroke_color=INK, stroke_width=3).move_to([x, 0.1, 0])
            word = T(reading, 32).move_to([x, 0.1, 0])
            self.play(FadeIn(card), FadeIn(word), run_time=0.8)

        until(self, "So ask first,")
        env = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.12,
                               fill_color="#FFFFFF", fill_opacity=1,
                               stroke_color=INK, stroke_width=3).move_to([0, -1.9, 0])
        flap = VGroup(
            Line([-1.3, -1.15, 0], [0, -1.55, 0], color=INK, stroke_width=2),
            Line([1.3, -1.15, 0], [0, -1.55, 0], color=INK, stroke_width=2),
        )
        tag = T("ask \u00b7 in writing", 36).move_to([0, -2.95, 0])
        self.play(FadeIn(env), FadeIn(flap), FadeIn(tag), run_time=1.0)
        ok = check(1.7, -1.6, s=0.2, color=TERRA)
        self.play(FadeIn(ok), run_time=0.7)
        finish(self)


class B03_Fluency(Scene):
    """A workbench; three fluency items drop in one by one."""

    def construct(self):
        bench = RoundedRectangle(width=11.0, height=1.6, corner_radius=0.15,
                                 fill_color="#E8E4D9", fill_opacity=1,
                                 stroke_width=0).move_to([0, -1.6, 0])
        self.play(FadeIn(bench), run_time=1.0)

        iso = Iso(0, -0.7, 1.0)
        until(self, "Practice prompting on your own time.")
        page = iso.page(0, 0, 0, 1.25, 1.5).move_to([-3.6, 0.1, 0])
        lab1 = T("prompt", 36).move_to([-3.6, 1.5, 0])
        self.play(FadeIn(page), FadeIn(lab1), run_time=0.9)

        until(self, "Quiz yourself on your own material.")
        card = RoundedRectangle(width=1.7, height=1.9, corner_radius=0.12,
                                fill_color="#FFFFFF", fill_opacity=1,
                                stroke_color=INK, stroke_width=3).move_to([0, 0.1, 0])
        dot = Dot([0, 0.55, 0], radius=0.09, color=TERRA)
        lab2 = T("quiz", 36).move_to([0, 1.5, 0])
        self.play(FadeIn(card), FadeIn(dot), FadeIn(lab2), run_time=0.9)

        until(self, "Anthropic's AI Fluency course")
        iso_b = Iso(3.6, -0.9, 0.9)
        book = iso_b.box(-0.5, -0.5, 0, 1.0, 1.2, 1.5)
        tag = pill(4.95, 0.45, 1.15)
        free = T("free", 32).move_to([4.95, 0.45, 0])
        lab3 = T("free course", 36).move_to([3.35, 1.5, 0])
        self.play(FadeIn(book), FadeIn(tag), FadeIn(free), FadeIn(lab3), run_time=1.0)
        finish(self)


class B04_Predict(Scene):
    """Sparse beat: the commit question."""

    def construct(self):
        q = T("?", 200).move_to([0, 0.5, 0])
        self.play(FadeIn(q), run_time=1.0)
        until(self, "What actually gets people caught?")
        cap = T("the use \u2014 or something else?", 44).move_to([0, -1.7, 0])
        self.play(FadeIn(cap), run_time=0.8)
        dot = Dot([0, -2.6, 0], radius=0.12, color=TERRA)
        self.play(FadeIn(dot), run_time=0.6)
        finish(self)


class B05_Reveal(Scene):
    """Same output, two paths: disclosed vs undisclosed."""

    def construct(self):
        iso = Iso(0, -0.3, 1.0)
        page_l = iso.page(0, 0, 0, 1.5, 1.8).move_to([-2.9, 0.1, 0])
        page_r = iso.page(0, 0, 0, 1.5, 1.8).move_to([2.9, 0.1, 0])
        self.play(FadeIn(page_l), FadeIn(page_r), run_time=1.2)

        until(self, "It's not the use. It's the undisclosed use.")
        ok = check(-4.55, 0.1, s=0.22, color=TERRA)
        lab_l = T("disclosed", 40).move_to([-2.9, 1.95, 0])
        self.play(FadeIn(ok), FadeIn(lab_l), run_time=0.9)

        until(self, "Same output, different path.")
        no = Cross(stroke_color=INK, stroke_width=8).scale(1.2).move_to([4.55, 0.1, 0])
        lab_r = T("undisclosed", 40).move_to([2.9, 1.95, 0])
        self.play(FadeIn(no), FadeIn(lab_r), run_time=0.9)

        sub_l = T("the conversation", 36).move_to([-2.9, -1.95, 0])
        sub_r = T("the violation", 36).move_to([2.9, -1.95, 0])
        self.play(FadeIn(sub_l), FadeIn(sub_r), run_time=0.8)
        finish(self)
