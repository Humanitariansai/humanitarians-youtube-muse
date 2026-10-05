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


# ═════════════════════════════ CAPTIONS THAT WRITE THEMSELVES — scenes ═════════════════════════════
# 8 Manim scenes (B00–B07), one per body beat. Cast, kept whole film: the
# phone video (the hero), caption lines, the dark AI block, the captioning
# tool, check stamps. Labels sit beside objects (never inside, never on
# terracotta), type floor 32, all coords inside ±6.2 x / ±3.3 y. Every play
# lands before mid−0.3 s or starts after mid+0.3 s (GATE T samples the
# midpoint), paced by until()/finish() against beat_sheet.json.

config.pixel_width = 1920
config.pixel_height = 1080


def phone_video(x, y, w=3.4, h=5.0):
    """The hero object: a phone playing the video. Frame, white screen, play triangle."""
    frame = RoundedRectangle(corner_radius=0.35, width=w, height=h, fill_color=CARD,
                             fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    screen = RoundedRectangle(corner_radius=0.2, width=w - 0.5, height=h - 0.6, fill_color="#FFFFFF",
                              fill_opacity=1, stroke_color=INK, stroke_width=2).move_to([x, y, 0])
    tri = Polygon([x - 0.35, y + 0.5, 0], [x - 0.35, y - 0.5, 0], [x + 0.45, y, 0],
                  fill_color=DARK_L, fill_opacity=1, stroke_color=INK, stroke_width=3)
    return VGroup(frame, screen, tri)


def capcard(x, y, s, w=None):
    """A caption line: white card with an ink outline, ink words. Sized to the text."""
    w = w or (len(s) * 0.22 + 0.8)
    card = RoundedRectangle(corner_radius=0.2, width=w, height=0.55, fill_color=CARD,
                            fill_opacity=1, stroke_color=INK, stroke_width=2.5).move_to([x, y, 0])
    t = T(s, 32).move_to([x, y - 0.02, 0])
    return VGroup(card, t)


def ai_block(x, y, w=2.0, h=2.2):
    """The AI: a dark block with two ghost ports. Returns (block_group, label)."""
    body = RoundedRectangle(corner_radius=0.2, width=w, height=h, fill_color=DARK_L,
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    ports = VGroup(*[Dot([x - 0.5 + i * 1.0, y + 0.5, 0], radius=0.09, color=GHOST) for i in range(2)])
    label = T("the AI", 32).move_to([x, y - h / 2 - 0.55, 0])
    return VGroup(body, ports), label


def tool_card(x, y):
    """The captioning tool: a kraft card with a 'captions' button. Returns (card, button, btn_label)."""
    card = RoundedRectangle(corner_radius=0.25, width=6.4, height=3.2, fill_color=CARD,
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    btn = RoundedRectangle(corner_radius=0.3, width=2.6, height=0.75, fill_color="#FFFFFF",
                           fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y + 0.4, 0])
    btn_label = T("captions", 32).move_to([x, y + 0.38, 0])
    label = T("caption tool", 32).move_to([x, y + 2.15, 0])
    return VGroup(card), VGroup(btn, btn_label), label


class B00_PhoneVideo(Scene):
    def construct(self):
        phone = phone_video(-1.4, 0.1)
        shadow = Ellipse(width=4.2, height=1.0, fill_color=GHOST, fill_opacity=1,
                         stroke_width=0).move_to([-1.4, -2.62, 0])
        label = T("your video", 36).move_to([2.2, 0.4, 0])
        self.play(GrowFromCenter(shadow), run_time=0.8)
        self.play(FadeIn(phone, shift=DOWN * 1.2), run_time=1.2)
        until(self, "the birthday toast", lead=1.2)
        self.play(FadeIn(label, shift=UP * 0.2), run_time=0.8)
        until(self, "in the sound", lead=0.6)
        finish(self)


class B01_WhatCaptions(Scene):
    def construct(self):
        phone = phone_video(-1.4, 0.1)
        shadow = Ellipse(width=4.2, height=1.0, fill_color=GHOST, fill_opacity=1,
                         stroke_width=0).move_to([-1.4, -2.62, 0])
        label = T("captions", 36).move_to([2.6, 0.3, 0])
        lines = [capcard(-1.4, y, s, w=2.7) for y, s in
                 [(-0.95, "sound off"), (-1.5, "on screen"), (-2.05, "on time")]]
        self.play(FadeIn(shadow), FadeIn(phone), run_time=1.5)
        until(self, "each line appearing", lead=1.5)
        self.play(FadeIn(lines[0], shift=UP * 0.15), run_time=0.7)
        until(self, "with the sound off", lead=1.0)
        self.play(FadeIn(lines[1], shift=UP * 0.15), run_time=0.7)
        until(self, "on the screen", lead=1.5)
        self.play(FadeIn(lines[2], shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(label, shift=UP * 0.2), run_time=0.6)
        finish(self)


class B02_ThePass(Scene):
    def construct(self):
        phone = phone_video(-4.4, 0.0, w=2.2, h=3.4)
        block, blabel = ai_block(0.0, 0.0)
        arcs = VGroup(*[Arc(radius=r, start_angle=-0.87, angle=1.74, color=INK, stroke_width=5)
                        .move_to([-2.9, 0.0, 0]) for r in (0.6, 1.0, 1.4)])
        lines = [capcard(3.4, y, s) for y, s in
                 [(0.9, "hello"), (0.2, "good morning"), (-0.5, "see you soon")]]
        ticks = VGroup(*[Dot([3.4 + (len(s) * 0.22 + 0.8) / 2 + 0.35, y, 0], radius=0.09, color=TERRA)
                         for (y, s) in [(0.9, "hello"), (0.2, "good morning"), (-0.5, "see you soon")]])
        label = T("one pass", 36).move_to([3.4, -1.55, 0])
        self.play(FadeIn(phone), FadeIn(block), FadeIn(blabel), run_time=1.5)
        until(self, "It listens")
        self.play(*[Create(a) for a in arcs], run_time=1.2)
        until(self, "writes down what it hears", lead=1.0)
        self.play(*[FadeIn(l, shift=LEFT * 0.3) for l in lines], run_time=1.4)
        until(self, "The draft is ready", lead=1.0)
        self.play(*[GrowFromCenter(t) for t in ticks], run_time=0.8)
        until(self, "By hand")
        self.play(FadeIn(label, shift=UP * 0.15), run_time=0.6)
        finish(self)


class B03_OpenIt(Scene):
    def construct(self):
        card, button, clabel = tool_card(0.6, 0.5)
        phone = phone_video(-4.8, 0.5, w=2.0, h=3.2)
        cur = cursor(0.6, 1.35)
        lines = [capcard(0.6, y, s, w=3.2) for y, s in
                 [(-1.7, "hello"), (-2.25, "good morning"), (-2.8, "see you soon")]]
        self.play(FadeIn(card), FadeIn(button), FadeIn(clabel), run_time=1.5)
        until(self, "Almost everything", lead=0.6)
        self.play(MoveAlongPath(phone, Line([-4.8, 0.5, 0], [-1.2, 0.5, 0])), run_time=1.6)
        until(self, "Look for it", lead=1.8)
        self.play(FadeIn(cur), run_time=0.5)
        self.play(button.animate.scale(0.94), run_time=0.25)
        self.play(button.animate.scale(1 / 0.94), run_time=0.25)
        until(self, "Your video goes in", lead=0.2)
        self.play(*[FadeIn(l, shift=UP * 0.15) for l in lines], run_time=1.2)
        finish(self)


class B04_PressButton(Scene):
    def construct(self):
        card, button, clabel = tool_card(0.6, 0.5)
        cur = cursor(0.6, 1.35)
        lines = [capcard(0.6, y, s, w=3.2) for y, s in
                 [(-1.7, "hello"), (-2.25, "good morning"), (-2.8, "see you soon")]]
        tick = check(3.1, -2.2, s=0.28, color=TERRA, w=8)
        label = T("the draft", 32).move_to([-3.1, -2.2, 0])
        self.play(FadeIn(card), FadeIn(button), FadeIn(clabel), run_time=1.5)
        until(self, "press the captions button", lead=1.2)
        self.play(FadeIn(cur), run_time=0.5)
        until(self, "and let it run")
        self.play(button.animate.scale(0.94), run_time=0.25)
        self.play(button.animate.scale(1 / 0.94), run_time=0.25)
        until(self, "The AI writes the whole draft itself", lead=0.8)
        self.play(FadeIn(lines[0], shift=UP * 0.15), run_time=0.6)
        until(self, "Then play it back", lead=0.1)
        self.play(FadeIn(lines[1], shift=UP * 0.15), FadeIn(lines[2], shift=UP * 0.15), run_time=0.8)
        until(self, "The timing will be close", lead=0.8)
        self.play(GrowFromCenter(tick), FadeIn(label, shift=UP * 0.15), run_time=0.7)
        finish(self)


class B05_CheckIt(Scene):
    def construct(self):
        texts = ["welcome to the show", "see you on Maine street", "tonight at eight"]
        lines = VGroup(*[capcard(-0.3, y, s, w=6.6) for y, s in zip((1.5, 0.45, -0.6), texts)])
        fixed = capcard(-0.3, 0.45, "see you on Main street", w=6.6)
        under = Line([-2.83, 0.02, 0], [2.23, 0.02, 0], color=TERRA, stroke_width=6)
        tick = check(3.9, 0.45, s=0.28, color=TERRA, w=8)
        l1 = T("names", 32).move_to([4.9, 1.2, 0])
        l2 = T("odd words", 32).move_to([4.9, -0.3, 0])
        self.play(*[FadeIn(l, shift=UP * 0.15) for l in lines], run_time=1.2)
        until(self, "names, places, and unusual words", lead=0.8)
        self.play(Create(under), run_time=0.7)
        until(self, "Scan the draft for those", lead=1.2)
        self.play(FadeOut(lines[1]), run_time=0.4)
        self.play(FadeIn(fixed, shift=UP * 0.1), run_time=0.6)
        until(self, "fix the jargon", lead=0.6)
        self.play(GrowFromCenter(tick), FadeIn(l1, shift=UP * 0.15), FadeIn(l2, shift=UP * 0.15), run_time=0.7)
        finish(self)


class B06_TwoWays(Scene):
    def construct(self):
        v1 = RoundedRectangle(corner_radius=0.2, width=3.0, height=2.0, fill_color="#FFFFFF",
                              fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([-3.2, 0.6, 0])
        caps1 = VGroup(capcard(-3.2, 0.35, "hello", w=2.0), capcard(-3.2, -0.25, "on time", w=2.0))
        lab1 = T("burned in", 32).move_to([-3.2, -1.15, 0])
        v2 = RoundedRectangle(corner_radius=0.2, width=2.2, height=2.0, fill_color="#FFFFFF",
                              fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([2.2, 0.6, 0])
        pg = RoundedRectangle(corner_radius=0.12, width=1.3, height=2.0, fill_color=CARD,
                              fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([4.15, 0.6, 0])
        plines = VGroup(*[Line([3.75, 1.15 - i * 0.45, 0], [4.55, 1.15 - i * 0.45, 0],
                               color=GHOST, stroke_width=5) for i in range(3)])
        lab2 = T("caption file", 32).move_to([3.0, -1.15, 0])
        dot = Dot([-3.2, 1.95, 0], radius=0.13, color=TERRA)
        self.play(FadeIn(v1), FadeIn(caps1), FadeIn(lab1), FadeIn(v2), FadeIn(pg), FadeIn(plines),
                  FadeIn(lab2), run_time=1.5)
        until(self, "Burned in means", lead=1.0)
        self.play(FadeIn(dot), run_time=0.5)
        until(self, "A caption file means", lead=2.0)
        self.play(MoveAlongPath(dot, Line(dot.get_center(), [3.0, 1.95, 0])), run_time=0.9)
        until(self, "For short feeds", lead=0.8)
        self.play(MoveAlongPath(dot, Line(dot.get_center(), [-3.2, 1.95, 0])), run_time=0.8)
        until(self, "For YouTube", lead=0.6)
        self.play(MoveAlongPath(dot, Line(dot.get_center(), [3.0, 1.95, 0])), run_time=0.8)
        finish(self)


class B07_WhoWatches(Scene):
    def construct(self):
        base = Line([-4.4, -1.6, 0], [1.6, -1.6, 0], color=INK, stroke_width=4)
        bar_on = Rectangle(width=1.1, height=1.1, fill_color=BAR2, fill_opacity=1,
                           stroke_width=0).move_to([-2.6, -1.05, 0])
        bar_off = Rectangle(width=1.1, height=3.2, fill_color=BAR1, fill_opacity=1,
                            stroke_width=0).move_to([0.0, 0.0, 0])
        lab_on = T("sound on", 32).move_to([-2.6, -2.15, 0])
        lab_off = T("sound off", 32).move_to([0.0, -2.15, 0])
        hero = T("9 in 10", 64, bold=True).move_to([0.0, 2.15, 0])
        src1 = T("per Verizon survey, 2019", 32).move_to([3.2, -0.9, 0])
        src2 = T("per WHO", 32).move_to([3.2, -1.45, 0])
        self.play(FadeIn(base), FadeIn(bar_on), FadeIn(lab_on), run_time=1.0)
        until(self, "Nine in ten", lead=0.8)
        self.play(GrowFromCenter(bar_off), FadeIn(hero, shift=DOWN * 0.2), FadeIn(lab_off, shift=UP * 0.15),
                  run_time=1.4)
        until(self, "says the World Health Organization", lead=1.5)
        self.play(FadeIn(src1, shift=UP * 0.15), FadeIn(src2, shift=UP * 0.15), run_time=0.8)
        finish(self)
