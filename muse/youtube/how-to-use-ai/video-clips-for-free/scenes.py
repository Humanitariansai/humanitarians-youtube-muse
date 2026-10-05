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
"""

Body scenes for "Video clips for free" (How to AI #35, Wave 6 "Making things").
Show-tell style: one drawing per beat on a cream stage, minimal labels
(ink, >=32pt, beside objects), terracotta only for dots/checks/arrows.
Class names are literal `class BNN_Name(Scene):` so run.sh finds them;
helpers attach after the class line. until()/finish() read beat_sheet.json
in this folder (the measured audio clock).
Cast (same objects, whole film): the vids.new browser window, the clip
frame, the kraft "free tier" budget jar, the timeline, the script pages.
"""

def shadow(x, y, w=3.2, h=0.5):
    return Ellipse(width=w, height=h, fill_color=DIM, fill_opacity=0.30, stroke_width=0).move_to([x, y, 0])

def lbl(text, x, y, size=38):
    return T(text, size=size, color=INK).move_to([x, y, 0])

def clip_frame(x, y, w=3.4, h=2.2, holes=True):
    """A film-strip frame: CARD card, ink outline, play triangle, sprocket holes."""
    frame = RoundedRectangle(width=w, height=h, corner_radius=0.15, fill_color=CARD,
                             fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])
    tri = Polygon([x - 0.28, y + 0.36, 0], [x - 0.28, y - 0.36, 0], [x + 0.38, y, 0],
                  fill_color=INK, fill_opacity=1, stroke_width=0)
    g = VGroup(frame, tri)
    if holes:
        n = max(3, int(w / 0.7))
        for i in range(n):
            hx = x - w / 2 + 0.35 + i * ((w - 0.7) / max(1, n - 1))
            for hy in (y + h / 2 - 0.22, y - h / 2 + 0.22):
                g.add(Square(side_length=0.13, fill_color=GHOST, fill_opacity=1,
                             stroke_width=0).move_to([hx, hy, 0]))
    return g

def strip(x, y, w=2.6, h=0.62):
    """A film strip: CARD bar with sprocket holes, ink outline."""
    bar = RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=CARD,
                           fill_opacity=1, stroke_color=INK, stroke_width=3).move_to([x, y, 0])
    g = VGroup(bar)
    n = max(3, int(w / 0.55))
    for i in range(n):
        hx = x - w / 2 + 0.3 + i * ((w - 0.6) / max(1, n - 1))
        g.add(Square(side_length=0.11, fill_color=GHOST, fill_opacity=1,
                     stroke_width=0).move_to([hx, y, 0]))
    return g

class B00_VidsWindow(Scene):
    def construct(self):
        win = RoundedRectangle(width=6.2, height=3.2, corner_radius=0.2, fill_color=CARD,
                               fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([-0.8, 0.3, 0])
        bar = Rectangle(width=6.2, height=0.75, fill_color=DARK_TOP, fill_opacity=1,
                        stroke_width=0).move_to([-0.8, 1.525, 0])
        dots = VGroup(*[Circle(radius=0.09, fill_color=CARD, fill_opacity=1, stroke_width=0)
                        .move_to([-3.5 + 0.42 * i, 1.525, 0]) for i in range(3)])
        self.add(shadow(-0.8, -1.55, w=6.6))
        self.play(Create(win), FadeIn(bar), FadeIn(dots), run_time=1.2)
        lab = lbl("vids.new", -0.8, -1.95)
        until(self, "opens at vids.new")
        self.play(FadeIn(lab), run_time=0.8)
        self.wait(0.5)
        clip = clip_frame(2.2, -2.1, w=2.6, h=1.6)
        spark = Dot([2.2, -1.05, 0], radius=0.1, color=TERRA)
        self.play(GrowFromCenter(clip), GrowFromCenter(spark), run_time=1.2, rate_func=ease_in)
        until(self, "high-definition video clip")
        finish(self)

class B01_OneClip(Scene):
    def construct(self):
        self.add(shadow(0, -1.5, w=5.0))
        clip = clip_frame(0, 0.2, w=4.6, h=2.8)
        frame_only = VGroup(clip[0], *clip[2:])  # frame + sprocket holes; play triangle arrives separately
        self.play(GrowFromCenter(frame_only), run_time=1.0, rate_func=ease_in)
        lab = lbl("one clip", 3.9, 0.2)
        until(self, "one short shot")
        self.play(FadeIn(clip[1]), FadeIn(lab), run_time=0.8)  # the play button lands: membership change
        until(self, "never the whole video")
        finish(self)

class B02_TheBudget(Scene):
    def construct(self):
        iso = Iso(ox=-1.8, oy=-1.2, s=1.0)
        back, front = iso.open_box(0, 0, 0, 2.4, 2.4, 1.5)
        self.add(shadow(-1.1, -2.6, w=3.6))
        self.play(Create(back), Create(front), run_time=1.2)
        lab = lbl("free tier", 3.0, 0.2)
        clips = VGroup(*[clip_frame(-1.5 + 0.9 * i, 0.9 + 0.45 * (i % 2), w=1.5, h=0.95, holes=False).set_z_index(1)
                         for i in range(3)])
        until(self, "free monthly allowance")
        self.play(FadeIn(lab), run_time=0.7)
        self.play(GrowFromCenter(clips[0]), run_time=0.7, rate_func=ease_in)
        self.wait(0.5)
        self.play(GrowFromCenter(clips[1]), GrowFromCenter(clips[2]), run_time=0.8, rate_func=ease_in)
        until(self, "refills each month")
        finish(self)

class B03_AIWins(Scene):
    def construct(self):
        self.add(shadow(0, -1.5, w=5.2))
        clip = clip_frame(0, 0.3, w=4.8, h=3.0)
        volc = Polygon([-1.7, -1.1, 0], [1.7, -1.1, 0], [0.15, 0.9, 0],
                       fill_color=INK, fill_opacity=1, stroke_color=INK, stroke_width=4)
        glow = Dot([0.15, 0.55, 0], radius=0.12, color=TERRA)
        self.play(GrowFromCenter(clip), run_time=1.0)
        self.play(FadeIn(volc), GrowFromCenter(glow), run_time=1.0)
        lab = lbl("AI wins", 3.9, 1.3)
        ck = check(2.9, 2.0, s=0.22, color=TERRA)
        until(self, "where AI video wins")
        self.play(FadeIn(lab), FadeIn(ck), run_time=0.8)
        until(self, "A drone flight over a volcano")
        finish(self)

class B04_Stock(Scene):
    def construct(self):
        iso = Iso(ox=-3.0, oy=-1.2, s=0.9)
        back, front = iso.open_box(0, 0, 0, 2.2, 2.2, 1.2)
        self.add(shadow(-2.3, -2.5, w=3.4))
        self.play(Create(back), Create(front), run_time=1.2)
        s1 = strip(-2.3, 0.7).set_z_index(1)
        s2 = strip(-2.0, -0.1).set_z_index(1)
        lab = lbl("stock", -2.15, 1.9)
        until(self, "the generic stuff")
        self.play(FadeIn(s1), FadeIn(s2), FadeIn(lab), run_time=1.0)
        self.wait(0.6)
        iso2 = Iso(ox=2.4, oy=-1.1, s=0.75)
        jar = iso2.box(0, 0, 0, 1.6, 1.6, 1.1)
        c1 = clip_frame(2.4, 0.75, w=1.2, h=0.8, holes=False)
        c2 = clip_frame(3.15, 0.85, w=1.2, h=0.8, holes=False)
        self.play(FadeIn(jar), GrowFromCenter(c1), GrowFromCenter(c2), run_time=1.0)
        until(self, "free stock footage")
        finish(self)

class B05_ScriptFirst(Scene):
    def construct(self):
        iso = Iso(ox=-4.6, oy=0.9, s=0.85)
        p1 = iso.page(0, 0, 0)
        p2 = iso.page(0.35, 0.35, 0.12)
        self.add(shadow(-4.0, -0.9, w=2.6))
        self.play(FadeIn(p1), FadeIn(p2), run_time=1.0)
        bar = RoundedRectangle(width=6.4, height=0.5, corner_radius=0.25, fill_color=DIM,
                               fill_opacity=1, stroke_width=0).move_to([0.9, -1.7, 0])
        slots = VGroup(*[RoundedRectangle(width=1.7, height=1.1, corner_radius=0.15, fill_color=GHOST,
                                          fill_opacity=1, stroke_width=0).move_to([-1.15 + 2.05 * i, -0.75, 0])
                         for i in range(3)])
        until(self, "Write the video in Vids first")
        self.play(FadeIn(bar), FadeIn(slots), run_time=1.0)
        hero = clip_frame(0.9, -0.75, w=1.7, h=1.1, holes=False)
        st1 = strip(-1.15, -0.75, w=1.7, h=0.62)
        st2 = strip(2.95, -0.75, w=1.7, h=0.62)
        lab = lbl("script first", 4.35, -2.6)
        self.wait(0.4)
        self.play(GrowFromCenter(hero), FadeIn(st1), FadeIn(st2), FadeIn(lab), run_time=1.0)
        until(self, "hero shots")
        finish(self)

class B06_Extend(Scene):
    def construct(self):
        fa = clip_frame(-3.3, 0.5, w=2.2, h=1.5)
        self.add(shadow(-3.3, -0.55, w=2.6))
        self.play(GrowFromCenter(fa), run_time=0.8)
        arr = Arrow([-2.05, 0.5, 0], [-1.35, 0.5, 0], color=TERRA, stroke_width=8,
                    buff=0.05, tip_length=0.25)
        fb = clip_frame(0.75, 0.5, w=3.9, h=1.5)
        until(self, "Extend it")
        self.play(GrowFromCenter(arr), GrowFromCenter(fb), run_time=1.0)
        pp = pill(-3.3, -1.9, 3.0)
        ppt = T("volcano", size=32, color=INK).move_to([-3.3, -1.9, 0])
        t1 = clip_frame(-0.3, -1.9, w=1.5, h=1.0, holes=False)
        t2 = clip_frame(1.5, -1.9, w=1.5, h=1.0, holes=False)
        iso = Iso(ox=3.4, oy=-0.6, s=0.6)
        back, front = iso.open_box(0, 0, 0, 1.7, 1.7, 1.0)
        jc = clip_frame(3.9, 0.75, w=1.1, h=0.75, holes=False).set_z_index(1)
        self.wait(0.3)
        self.play(FadeIn(pp), FadeIn(ppt), GrowFromCenter(t1), GrowFromCenter(t2),
                  Create(back), Create(front), GrowFromCenter(jc), run_time=1.2)
        lab = lbl("extend", 4.15, -1.5)
        self.play(FadeIn(lab), FadeOut(jc), run_time=0.7)
        until(self, "spends one clip")
        finish(self)

class B07_PaidExtras(Scene):
    def construct(self):
        iso = Iso(ox=-4.4, oy=-1.2, s=0.8)
        back, front = iso.open_box(0, 0, 0, 2.0, 2.0, 1.2)
        self.add(shadow(-3.7, -2.6, w=3.2))
        c1 = clip_frame(-3.9, 0.5, w=1.4, h=0.95, holes=False).set_z_index(1)
        c2 = clip_frame(-3.0, 0.7, w=1.4, h=0.95, holes=False).set_z_index(1)
        self.play(Create(back), Create(front), GrowFromCenter(c1), GrowFromCenter(c2), run_time=1.2)
        m1 = RoundedRectangle(width=2.3, height=1.5, corner_radius=0.15, fill_color=DIM,
                              fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0.9, 0.5, 0])
        m2 = RoundedRectangle(width=2.3, height=1.5, corner_radius=0.15, fill_color=DIM,
                              fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([3.6, 0.5, 0])
        l1 = lbl("music", 0.9, -0.65)
        l2 = lbl("avatar", 3.6, -0.65)
        until(self, "The extras")
        self.play(FadeIn(m1), FadeIn(m2), FadeIn(l1), FadeIn(l2), run_time=1.0)
        lab = lbl("paid extras", 2.25, 2.0)
        self.wait(0.5)
        self.play(FadeIn(lab), run_time=0.6)
        until(self, "Skip them for now")
        finish(self)

class B08_CheckTheNumber(Scene):
    def construct(self):
        iso = Iso(ox=-3.6, oy=-1.2, s=1.0)
        back, front = iso.open_box(0, 0, 0, 2.4, 2.4, 1.5)
        self.add(shadow(-2.9, -2.6, w=3.6))
        c1 = clip_frame(-3.1, 0.9, w=1.5, h=0.95, holes=False).set_z_index(1)
        c2 = clip_frame(-2.0, 1.1, w=1.5, h=0.95, holes=False).set_z_index(1)
        self.play(Create(back), Create(front), GrowFromCenter(c1), GrowFromCenter(c2), run_time=1.2)
        cx, cy, r = 2.9, -0.9, 1.25
        arc = Arc(radius=r, start_angle=0, angle=PI, arc_center=[cx, cy, 0],
                  color=DIM, stroke_width=6)
        ticks = VGroup(*[Line([cx + r * np.cos(a), cy + r * np.sin(a), 0],
                              [cx + (r - 0.22) * np.cos(a), cy + (r - 0.22) * np.sin(a), 0],
                              color=DIM, stroke_width=5)
                         for a in [np.pi * f for f in (0.08, 0.3, 0.5, 0.7, 0.92)]])
        n1 = Line([cx, cy, 0], [cx + 0.95 * np.cos(0.3 * np.pi), cy + 0.95 * np.sin(0.3 * np.pi), 0],
                  color=INK, stroke_width=8)
        hub = Dot([cx, cy, 0], radius=0.12, color=INK)
        lab = lbl("check vids.new", 2.9, 1.15)
        until(self, "has already moved before")
        self.play(Create(arc), FadeIn(ticks), FadeIn(n1), FadeIn(hub), FadeIn(lab), run_time=1.0)
        n2 = Line([cx, cy, 0], [cx + 0.95 * np.cos(0.7 * np.pi), cy + 0.95 * np.sin(0.7 * np.pi), 0],
                  color=INK, stroke_width=8)
        self.wait(0.6)
        self.play(FadeOut(n1), FadeIn(n2), run_time=0.8)
        until(self, "check vids.new")
        finish(self)
