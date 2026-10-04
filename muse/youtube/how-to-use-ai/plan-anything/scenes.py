"""scenes.py — "Plan anything." (show-tell, slug plan-anything).

PASTE of the show-tell iso_kit (do not import: Gate A copies only this file),
then 8 Manim body-beat scenes, one per beat, class name = beat id + "_" + name.

Cast (kept whole-film): the plan = white iso pages with ghost lines; constraints
= small kraft chips dropping into an open kraft box; revision = an ink arc sweep
with a terracotta dot/check; done = terracotta checks on pills; you = a small
ink human figure.

Pacing: until()/finish() read beat_sheet.json (narration is the clock).
Drawing laws: labels beside objects (>=32pt), terracotta only for dots/checks/
the loop arrow, numerals ink, every scene adds new non-text shapes after its
first frame, all coords inside the safe frame.
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


# ═════════════════════════════ film helpers ═════════════════════════════
def human(x, y, s=1.0, color=INK):
    """The film's 'you': a small ink figure. Fixed numbers only."""
    head = Circle(radius=0.2 * s, fill_color=color, fill_opacity=1, stroke_width=0).move_to([x, y + 0.52 * s, 0])
    torso = Line([x, y + 0.3 * s, 0], [x, y - 0.32 * s, 0], color=color, stroke_width=int(9 * s))
    leg_l = Line([x, y - 0.32 * s, 0], [x - 0.2 * s, y - 0.72 * s, 0], color=color, stroke_width=int(7 * s))
    leg_r = Line([x, y - 0.32 * s, 0], [x + 0.2 * s, y - 0.72 * s, 0], color=color, stroke_width=int(7 * s))
    return VGroup(head, torso, leg_l, leg_r)


def shadow(x, y, w=2.4):
    return Ellipse(width=w, height=0.22, fill_color=GHOST, fill_opacity=0.8, stroke_width=0).move_to([x, y, 0])


def chip(iso, x0, y0, z0, w=1.0, d=1.0, h=0.32):
    """A constraint chip: a small kraft box."""
    return iso.box(x0, y0, z0, w, d, h)


def loop_arrow(x0, x1, y):
    """A terracotta arrow sweeping along a row: the loop's direction."""
    line = Line([x0, y, 0], [x1, y, 0], color=TERRA, stroke_width=7)
    head = Polygon([x1, y, 0], [x1 - 0.45, y + 0.22, 0], [x1 - 0.45, y - 0.22, 0],
                   fill_color=TERRA, fill_opacity=1, stroke_width=0)
    return VGroup(line, head)


def sweep_arc(x0, x1, y, angle=1.0):
    """An ink arc that sweeps across a plan: the complaint / revision motion."""
    arc = ArcBetweenPoints(np.array([x0, y, 0]), np.array([x1, y, 0]), angle=angle, color=INK, stroke_width=6)
    dot = Dot(np.array([x1, y, 0]), radius=0.09, color=TERRA)
    return VGroup(arc, dot)


# ═════════════════════════════ B00 — the hero: the planning loop ═════════════════════════════
class B00_TheLoop(Scene):
    def construct(self):
        iso = Iso(0, -1.3, 0.9)
        ts = [-3.3, -1.1, 1.1, 3.3]
        xs = [-4.86, -1.62, 1.62, 4.86]
        words = ["constraints", "draft", "revise", "checklist"]
        blocks = [iso.box(t - 0.75, -t - 0.75, 0, 1.5, 1.5, 0.6) for t in ts]
        labels = [T(words[i], size=32).move_to([xs[i], -2.7, 0]) for i in range(4)]
        floor = shadow(0, -2.15, 9.5)
        arrow = loop_arrow(-5.5, 5.5, -0.1)

        self.play(FadeIn(floor), FadeIn(blocks[0]), FadeIn(labels[0]), run_time=0.9)
        until(self, "It never gets tired of revising")
        self.play(FadeIn(blocks[1]), FadeIn(labels[1]), run_time=0.7)
        until(self, "constraints in")
        self.play(FadeIn(blocks[2]), FadeIn(labels[2]), run_time=0.7)
        until(self, "revisions")
        self.play(FadeIn(blocks[3]), FadeIn(labels[3]), FadeIn(arrow), run_time=0.8)
        finish(self)


# ═════════════════════════════ B01 — constraints first ═════════════════════════════
class B01_Constraints(Scene):
    def construct(self):
        iso = Iso(-1.6, -0.5, 0.85)
        back, front = iso.open_box(-1.0, -1.0, 0, 2.0, 2.0, 1.1)
        floor = shadow(-1.6, -1.85, 4.6)
        chips = [chip(iso, -0.5, -0.5, 0.02 + 0.36 * i) for i in range(3)]
        words = ["budget", "dates", "interests"]
        ys = [-0.35, -0.04, 0.27]
        labels = [T(words[i], size=32).move_to([1.4, ys[i], 0]) for i in range(3)]
        leads = [Line([-0.3, ys[i], 0], [0.65, ys[i], 0], color=DIM, stroke_width=3) for i in range(3)]
        fig = human(3.1, -1.3)

        self.play(FadeIn(floor), FadeIn(back), FadeIn(front), FadeIn(fig),
                  FadeIn(chips[0], shift=DOWN * 1.0), FadeIn(labels[0]), FadeIn(leads[0]), run_time=1.0)
        until(self, "not your dream trip")
        self.play(FadeIn(chips[1], shift=DOWN * 1.0), FadeIn(labels[1]), FadeIn(leads[1]), run_time=0.7)
        until(self, "a hundred and fifty dollars")
        self.play(FadeIn(chips[2], shift=DOWN * 1.0), FadeIn(labels[2]), FadeIn(leads[2]), run_time=0.7)
        finish(self)


# ═════════════════════════════ B02 — the draft itinerary ═════════════════════════════
class B02_DraftItinerary(Scene):
    def construct(self):
        page_a = Iso(-3.2, -0.5, 0.9).page(-0.55, -0.7, 0)
        page_b = Iso(0.9, -0.5, 0.9).page(-0.55, -0.7, 0)
        floor = shadow(-1.15, -1.5, 5.6)
        label_a = T("day one", size=32).move_to([-3.2, -1.95, 0])
        label_b = T("day two", size=32).move_to([0.9, -1.95, 0])
        dot = Dot(np.array([-1.15, 1.6, 0]), radius=0.1, color=TERRA)
        raw = T("raw material", size=32).move_to([-1.15, 2.3, 0])

        self.play(FadeIn(floor), FadeIn(page_a, shift=DOWN * 1.2), FadeIn(label_a), run_time=0.8)
        until(self, "sketch a two-day trip")
        self.play(FadeIn(page_b, shift=DOWN * 1.2), FadeIn(label_b), run_time=0.8)
        until(self, "an evening at a museum")
        self.play(GrowFromCenter(dot), FadeIn(raw), run_time=0.6)
        finish(self)


# ═════════════════════════════ B03 — revise: complain, slow it down ═════════════════════════════
class B03_Revise(Scene):
    def construct(self):
        iso = Iso(-1.4, -0.4, 0.85)
        page = iso.page(-0.55, -0.7, 0, 1.3, 1.6)
        floor = shadow(-1.4, -1.5, 3.4)
        stops = [iso.box(-0.4, -0.6, 0.12 + 0.38 * i, 1.0, 0.28, 0.18) for i in range(3)]
        label = T("the draft", size=32).move_to([-1.4, -1.45, 0])
        arc = sweep_arc(-2.3, -0.5, 0.9)
        mark = Dot(np.array([-0.99, -0.37, 0]), radius=0.09, color=TERRA)
        tick = check(-1.4, 0.55, s=0.24, color=TERRA, w=9)
        slower = T("slower", size=32).move_to([0.6, 0.55, 0])

        self.play(FadeIn(floor), FadeIn(page), FadeIn(stops[0]), FadeIn(stops[1]), FadeIn(stops[2]),
                  FadeIn(label), run_time=1.0)
        until(self, "complain")
        self.play(Create(arc), GrowFromCenter(mark), run_time=0.8)
        until(self, "Too rushed")
        self.play(FadeOut(stops[0]), FadeOut(mark),
                  stops[1].animate.shift(DOWN * 0.55), stops[2].animate.shift(DOWN * 1.1), run_time=0.8)
        until(self, "No sighing")
        self.play(GrowFromCenter(tick), FadeIn(slower), run_time=0.6)
        finish(self)


# ═════════════════════════════ B04 — the checklist ═════════════════════════════
class B04_Checklist(Scene):
    def construct(self):
        iso = Iso(-2.2, -0.3, 0.85)
        page = iso.page(-0.55, -0.7, 0, 1.3, 1.6)
        floor = shadow(-2.2, -1.75, 3.2)
        label = T("checklist", size=32).move_to([-2.2, -1.4, 0])
        words = ["pack", "book", "day before"]
        ys = [0.9, 0.1, -0.7]
        pills = [pill(1.6, ys[i], 2.6) for i in range(3)]
        caps = [T(words[i], size=32).move_to([1.6, ys[i], 0]) for i in range(3)]
        ticks = [check(-0.15, ys[i], s=0.17, color=TERRA, w=8) for i in range(3)]

        self.play(FadeIn(floor), FadeIn(page), FadeIn(label), run_time=0.9)
        until(self, "What to pack")
        self.play(FadeIn(pills[0]), FadeIn(caps[0]), GrowFromCenter(ticks[0]), run_time=0.6)
        until(self, "what to book")
        self.play(FadeIn(pills[1]), FadeIn(caps[1]), GrowFromCenter(ticks[1]), run_time=0.6)
        until(self, "what to double-check")
        self.play(FadeIn(pills[2]), FadeIn(caps[2]), GrowFromCenter(ticks[2]), run_time=0.6)
        finish(self)


# ═════════════════════════════ B05 — the pattern travels: projects ═════════════════════════════
class B05_Projects(Scene):
    def construct(self):
        iso = Iso(-2.9, -0.5, 0.85)
        back, front = iso.open_box(-1.0, -1.0, 0, 2.0, 2.0, 1.1)
        floor = shadow(-2.9, -1.85, 4.6)
        chips = [chip(iso, -0.5, -0.5, 0.02 + 0.36 * i) for i in range(2)]
        constraints = T("constraints", size=32).move_to([-2.9, -1.9, 0])
        title = T("a project", size=32).move_to([-0.85, 2.2, 0])
        iso2 = Iso(1.2, -0.5, 0.85)
        page = iso2.page(-0.55, -0.7, 0, 1.1, 1.4)
        greys = [BAR1, BAR2, BAR3]
        bars = [iso2.box(-0.4, -0.6 + 0.45 * i, 0.12, 0.8, 0.3, 0.14, top=greys[i], left=greys[i], right=greys[i])
                for i in range(3)]
        draft = T("draft", size=32).move_to([1.2, -1.6, 0])
        arc = sweep_arc(0.5, 1.9, 0.9)
        tick = check(1.2, 0.62, s=0.24, color=TERRA, w=9)
        launch = T("launch", size=32).move_to([1.2, 1.35, 0])

        self.play(FadeIn(floor), FadeIn(back), FadeIn(front),
                  FadeIn(chips[0], shift=DOWN * 1.0), FadeIn(chips[1], shift=DOWN * 1.0),
                  FadeIn(constraints), FadeIn(title), run_time=1.0)
        until(self, "A draft timeline")
        self.play(FadeIn(page), FadeIn(bars[0]), FadeIn(bars[1]), FadeIn(bars[2]), FadeIn(draft), run_time=0.9)
        until(self, "Revisions")
        self.play(FadeOut(bars[2]), Create(arc), run_time=0.8)
        until(self, "launch checklist")
        self.play(GrowFromCenter(tick), FadeIn(launch), run_time=0.6)
        finish(self)


# ═════════════════════════════ B06 — the pattern travels: budgets ═════════════════════════════
class B06_Budgets(Scene):
    def construct(self):
        iso = Iso(-2.9, -0.5, 0.85)
        back, front = iso.open_box(-1.0, -1.0, 0, 2.0, 2.0, 1.1)
        floor = shadow(-2.9, -1.85, 4.6)
        chips = [chip(iso, -0.5, -0.5, 0.02 + 0.36 * i) for i in range(2)]
        constraints = T("constraints", size=32).move_to([-2.9, -1.9, 0])
        title = T("a budget", size=32).move_to([-0.85, 2.2, 0])
        iso2 = Iso(1.2, -0.5, 0.85)
        page = iso2.page(-0.55, -0.7, 0, 1.1, 1.4)
        greys = [BAR1, BAR2, BAR3]
        segs = [iso2.box(-0.5 + 0.4 * i, -0.6, 0.12, 0.3, 0.9, 0.16, top=greys[i], left=greys[i], right=greys[i])
                for i in range(3)]
        draft = T("draft", size=32).move_to([1.2, -1.6, 0])
        arc = sweep_arc(0.5, 1.9, 0.9)
        tick = check(1.2, 0.62, s=0.24, color=TERRA, w=9)
        payday = T("payday", size=32).move_to([1.2, 1.35, 0])

        self.play(FadeIn(floor), FadeIn(back), FadeIn(front),
                  FadeIn(chips[0], shift=DOWN * 1.0), FadeIn(chips[1], shift=DOWN * 1.0),
                  FadeIn(constraints), FadeIn(title), run_time=1.0)
        until(self, "A draft")
        self.play(FadeIn(page), FadeIn(segs[0]), FadeIn(segs[1]), FadeIn(segs[2]), FadeIn(draft), run_time=0.9)
        until(self, "Revisions")
        self.play(FadeOut(segs[2]), Create(arc), run_time=0.8)
        until(self, "payday")
        self.play(GrowFromCenter(tick), FadeIn(payday), run_time=0.6)
        finish(self)


# ═════════════════════════════ B07 — you verify ═════════════════════════════
class B07_YouVerify(Scene):
    def construct(self):
        iso = Iso(0, -0.3, 0.85)
        page = iso.page(-0.55, -0.7, 0, 1.2, 1.5)
        floor = shadow(0, -1.5, 2.8)
        label = T("the plan", size=32).move_to([-2.75, 0.1, 0])
        lens = Circle(radius=0.34, color=INK, stroke_width=5).move_to([-0.3, -0.1, 0])
        handle = Line([-0.06, -0.34, 0], [0.32, -0.72, 0], color=INK, stroke_width=5)
        glass = VGroup(lens, handle)
        tick = check(0.55, 0.35, s=0.26, color=TERRA, w=9)
        fig = human(2.6, -1.2)
        verify = T("you verify", size=32).move_to([2.6, -2.5, 0])

        self.play(FadeIn(floor), FadeIn(page), FadeIn(label), run_time=0.9)
        until(self, "memory goes stale")
        self.play(FadeIn(lens), FadeIn(handle), run_time=0.6)
        until(self, "check it yourself")
        self.play(glass.animate.shift(UP * 0.9 + RIGHT * 0.3), GrowFromCenter(tick), run_time=0.8)
        until(self, "You verify")
        self.play(FadeIn(fig), FadeIn(verify), run_time=0.6)
        finish(self)
