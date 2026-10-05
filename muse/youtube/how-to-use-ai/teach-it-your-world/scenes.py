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

"""
teach-it-your-world — scenes.py (ai-explainer).

The iso_kit.py block (top of file) is pasted verbatim from
brutalist.art/skills/make/show-tell/templates/iso_kit.py — Gate A copies only
scenes.py, so the kit must live here, not be imported.

Cast for the whole film: the big dim "internet knowledge" circle, kraft
document boxes (open_box + tape), flat pages that drop into boxes, standing
shelf pages, a meaning-map dot scatter, numbered habit cards, terracotta
checks/glow rings. House palette: cream stage, warm ink, one terracotta
accent, EB Garamond. Every scene carries the @NikBearBrown bug (lower-right),
keeps type >= 36 px, labels beside objects with leader gaps, and lands all
motion in the first ~40% of the beat — then until() holds on a settled
labelled frame and finish() pads to the audio.
"""


# ═════════════════════════════ local helpers ═════════════════════════════
def bug():
    """Channel watermark bug, lower-right, inside the safe area."""
    return Text("@NikBearBrown", font_size=16, color=INK,
                fill_opacity=0.45).move_to(np.array([5.35, -3.05, 0.0]))


def label(text, x, y, size=40):
    return T(text, size=size, color=INK).move_to([x, y, 0])


def leader(x0, x1, y, color=DIM):
    """A short dim leader line; callers keep >= 0.3 gap to the label."""
    return Line([x0, y, 0], [x1, y, 0], color=color, stroke_width=3)


def squig(x, y, w=1.6, color=DIM, sw=6):
    """One wobbly guess-line centred on (x, y)."""
    pts = [np.array([x - w / 2 + w * i / 8, y + 0.12 * ((i % 2) * 2 - 1), 0.0])
           for i in range(9)]
    return VMobject().set_points_smoothly(pts).set_color(color).set_stroke(width=sw)


def solid(x, y, w=1.6, color=INK, sw=6):
    """One straight answer-line centred on (x, y)."""
    return Line([x - w / 2, y, 0], [x + w / 2, y, 0], color=color, stroke_width=sw)


def page_rect(x, y, w=0.75, h=1.05, stroke=DIM):
    """A standing page card."""
    return RoundedRectangle(width=w, height=h, corner_radius=0.08,
                            fill_color=CARD, fill_opacity=1,
                            color=stroke, stroke_width=4).move_to([x, y, 0])


# ═════════════════════════════ B02 — the gap ═════════════════════════════
class B02_TheGap(Scene):
    def construct(self):
        self.add(bug())
        world = Circle(radius=1.9, color=DIM, stroke_width=5,
                       fill_color=GHOST, fill_opacity=0.4).move_to([-2.6, 0.3, 0])
        lab_w = label("the internet", -2.6, -2.2, size=36)
        iso = Iso(2.4, -1.7, 1.0)
        docs = VGroup(iso.box(0, 0, 0, 1.8, 1.5, 1.1),
                      iso.tape(0, 0, 1.1, 1.8, 1.5))
        lab_d = label("your docs", 2.53, -2.5, size=36)
        self.play(FadeIn(world), FadeIn(lab_w), FadeIn(docs), FadeIn(lab_d), run_time=0.8)
        qcard = RoundedRectangle(width=2.9, height=1.0, corner_radius=0.2,
                                 fill_color=CARD, fill_opacity=1, color=INK,
                                 stroke_width=5).move_to([-2.6, 2.65, 0])
        qtext = T("on call Friday?", size=32, color=INK).move_to([-2.6, 2.65, 0])
        self.play(FadeIn(qcard), FadeIn(qtext), run_time=0.5)
        shaft = Line([-1.85, 2.1, 0], [-1.45, 1.25, 0], color=INK, stroke_width=7)
        ahead = Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=0
                         ).scale(0.3).rotate(-62 * DEGREES).move_to([-1.4, 1.15, 0])
        self.play(Create(shaft), FadeIn(ahead), run_time=0.5)
        guess = VGroup(*[squig(-2.6, 0.9 - 0.55 * i, w=1.7) for i in range(3)])
        qmark = T("?", size=64, color=INK).move_to([-1.0, 0.15, 0])
        self.play(GrowFromCenter(guess), FadeIn(qmark), run_time=0.6)
        until(self, "it guesses")
        finish(self)


# ═════════════════════════════ B03 — the fix ═════════════════════════════
class B03_TheFix(Scene):
    def construct(self):
        self.add(bug())
        iso = Iso(0, -1.55, 1.0)
        back, front = iso.open_box(0, 0, 0, 2.0, 1.8, 1.1)
        lab = label("give it the source", 0, -2.75, size=36)
        self.play(FadeIn(back), FadeIn(front), FadeIn(lab), run_time=0.7)
        for i in range(3):
            pg = iso.page(0.35 + 0.12 * i, 0.15 + 0.10 * i, 2.4, 1.1, 1.4)
            self.play(FadeIn(pg), run_time=0.3)
            self.play(pg.animate.shift(DOWN * (1.7 + 0.15 * i)), run_time=0.45)
        card = RoundedRectangle(width=3.0, height=2.2, corner_radius=0.2,
                                fill_color=CARD, fill_opacity=1, color=INK,
                                stroke_width=5).move_to([4.1, 0.2, 0])
        wob = VGroup(*[squig(4.1, 0.9 - 0.5 * i, w=1.8) for i in range(3)])
        self.play(FadeIn(card), FadeIn(wob), run_time=0.5)
        sol = VGroup(*[solid(4.1, 0.9 - 0.5 * i, w=1.8) for i in range(3)])
        self.play(FadeOut(wob), FadeIn(sol), run_time=0.4)
        ck = check(4.1, -1.5, s=0.22, color=TERRA, w=8)
        self.play(GrowFromCenter(ck), run_time=0.4)
        until(self, "the file goes into the chat")
        finish(self)


# ═════════════════════════════ B04 — the librarian ═════════════════════════════
class B04_TheLibrarian(Scene):
    def construct(self):
        self.add(bug())
        shelf = Line([-5.6, -1.1, 0], [0.6, -1.1, 0], color=INK, stroke_width=6)
        pages = VGroup(*[page_rect(-5.0 + 1.25 * i, -0.5) for i in range(5)])
        lab = label("librarian", -2.5, -2.3)
        qcard = RoundedRectangle(width=1.7, height=0.85, corner_radius=0.2,
                                 fill_color=CARD, fill_opacity=1, color=INK,
                                 stroke_width=5).move_to([3.9, 1.9, 0])
        qtext = T("rota?", size=36, color=INK).move_to([3.9, 1.9, 0])
        acard = RoundedRectangle(width=2.7, height=1.9, corner_radius=0.2,
                                 fill_color=CARD, fill_opacity=1, color=INK,
                                 stroke_width=5).move_to([3.9, -0.7, 0])
        self.play(FadeIn(shelf), FadeIn(pages), FadeIn(lab),
                  FadeIn(qcard), FadeIn(qtext), FadeIn(acard), run_time=0.8)
        glow = VGroup(*[RoundedRectangle(width=0.9, height=1.2, corner_radius=0.08,
                                         color=TERRA, stroke_width=7, fill_opacity=0
                                         ).move_to([-3.75 + 2.5 * i, -0.5, 0])
                         for i in range(2)])
        self.play(Create(glow), run_time=0.5)
        movers = VGroup(pages[1], pages[3])
        self.play(movers.animate.move_to([3.9, -0.7, 0]), run_time=0.7)
        lines = VGroup(*[solid(3.9, -0.1 - 0.45 * i, w=1.9) for i in range(3)])
        self.play(FadeOut(movers), FadeOut(glow), FadeIn(lines), run_time=0.4)
        until(self, "Librarian, not scanner.")
        finish(self)


# ═════════════════════════════ B05 — meaning map ═════════════════════════════
class B05_MeaningMap(Scene):
    def construct(self):
        self.add(bug())
        scatter = VGroup(*[Dot([x, y, 0], radius=0.09, color=DIM) for x, y in
                            [(-4.8, 1.4), (-3.9, -0.6), (-3.0, 1.8), (-2.2, -1.4),
                             (1.8, 1.6), (2.6, -1.2), (4.6, 1.2), (5.2, -0.4)]])
        cluster = VGroup(*[Dot([x, y, 0], radius=0.12, color=INK) for x, y in
                            [(-1.0, 0.5), (-0.3, 0.9), (0.4, 0.2)]])
        l_inv = label("invoice", -1.95, 0.15, size=32)
        l_rec = label("receipt", -0.3, 1.7, size=32)
        l_bill = label("bill", 1.2, -0.2, size=32)
        ring = Circle(radius=1.05, color=TERRA, stroke_width=6).move_to([-0.3, 0.55, 0])
        ele = Dot([4.4, -1.6, 0], radius=0.12, color=INK)
        l_ele = label("elephant", 4.4, -2.25, size=32)
        lab = label("near = similar meaning", -0.3, -2.85, size=36)
        self.play(FadeIn(scatter), FadeIn(cluster),
                  FadeIn(l_inv), FadeIn(l_rec), FadeIn(l_bill), run_time=0.7)
        self.play(Create(ring), run_time=0.5)
        self.play(FadeIn(ele), FadeIn(l_ele), FadeIn(lab), run_time=0.5)
        until(self, "not the elephant")
        finish(self)


# ═════════════════════════════ B06 — what to upload ═════════════════════════════
class B06_WhatToUpload(Scene):
    def construct(self):
        self.add(bug())
        isos = [Iso(-4.9, -1.7, 0.8), Iso(-0.85, -1.7, 0.8), Iso(3.2, -1.7, 0.8)]
        boxes = VGroup()
        for iso in isos:
            back, front = iso.open_box(0, 0, 0, 1.9, 1.7, 1.0)
            boxes.add(back, front)
        labs = VGroup(label("your notes", -4.81, -2.85, size=36),
                      label("work docs", -0.76, -2.85, size=36),
                      label("only-you-know", 3.29, -2.85, size=36))
        self.play(FadeIn(boxes), FadeIn(labs), run_time=0.7)
        for iso in isos:
            pg = iso.page(0.4, 0.15, 2.3, 1.1, 1.3)
            self.play(FadeIn(pg), run_time=0.3)
            self.play(pg.animate.shift(DOWN * 1.75), run_time=0.45)
        until(self, "belongs in the AI's world too")
        finish(self)


# ═════════════════════════════ B07 — three habits ═════════════════════════════
class B07_ThreeHabits(Scene):
    def construct(self):
        self.add(bug())
        cards, nums, lines, dots = VGroup(), VGroup(), VGroup(), VGroup()
        texts = [("give it", "the source"), ("pin it:", "only from these"), ("make it", "quote")]
        for i, (l1, l2) in enumerate(texts):
            x = -4.1 + 4.1 * i
            cards.add(RoundedRectangle(width=3.3, height=2.1, corner_radius=0.2,
                                       fill_color=CARD, fill_opacity=1, color=INK,
                                       stroke_width=5).move_to([x, 0.35, 0]))
            nums.add(T(str(i + 1), size=52, color=INK, bold=True).move_to([x, 1.05, 0]))
            lines.add(T(l1, size=30, color=INK).move_to([x, 0.35, 0]))
            lines.add(T(l2, size=30, color=INK).move_to([x, -0.2, 0]))
            dots.add(Dot([x, 0.72, 0], radius=0.07, color=TERRA))
        self.play(FadeIn(cards), FadeIn(nums), FadeIn(lines), FadeIn(dots), run_time=0.8)
        for i in range(3):
            x = -4.1 + 4.1 * i
            ck = check(x, -1.15, s=0.22, color=TERRA, w=8)
            self.play(GrowFromCenter(ck), run_time=0.35)
        until(self, "beats a confident paragraph")
        finish(self)


# ═════════════════════════════ B08 — where it bites ═════════════════════════════
class B08_WhereItBites(Scene):
    def construct(self):
        self.add(bug())
        # panel 1: the half-empty box (blind spots)
        iso = Iso(-5.3, -1.9, 0.7)
        back, front = iso.open_box(0, 0, 0, 1.7, 1.5, 0.9)
        lab1 = label("blind spots", -4.35, -2.9, size=32)
        self.play(FadeIn(back), FadeIn(front), FadeIn(lab1), run_time=0.6)
        # panel 2: stale page vs fresh page
        stale = page_rect(-0.9, 0.1, w=1.3, h=1.7)
        web = VGroup(*[Arc(radius=0.35, start_angle=a * DEGREES, angle=70 * DEGREES,
                            arc_center=[-0.9, 0.75, 0], color=DIM, stroke_width=4)
                       for a in (200, 260, 320)])
        fresh = page_rect(0.75, 0.1, w=1.3, h=1.7, stroke=INK)
        lab2 = label("stale in, stale out", -0.08, -1.6, size=32)
        self.play(FadeIn(stale), FadeIn(web), FadeIn(fresh), FadeIn(lab2), run_time=0.6)
        # panel 3: the wrong document gets quoted, not flagged
        wrong = page_rect(4.3, 0.1, w=1.3, h=1.7)
        x1 = Line([3.85, 0.55, 0], [4.75, -0.35, 0], color=INK, stroke_width=9)
        x2 = Line([3.85, -0.35, 0], [4.75, 0.55, 0], color=INK, stroke_width=9)
        quote = VGroup(*[solid(4.3, -1.35 - 0.35 * i, w=1.9) for i in range(2)])
        lab3 = label("wrong doc = confident quote", 4.3, -2.35, size=30)
        self.play(FadeIn(wrong), GrowFromCenter(VGroup(x1, x2)), FadeIn(quote),
                  FadeIn(lab3), run_time=0.7)
        until(self, "confident garbage out")
        finish(self)
