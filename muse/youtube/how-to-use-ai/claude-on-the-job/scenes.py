"""scenes.py — "Claude, On the Job." (show-tell, slug claude-on-the-job).

PASTE of the show-tell iso_kit (do not import: Gate A copies only this file),
then 9 Manim body-beat scenes, one per beat, class name = beat id + "_" + name.

Cast (kept whole-film): the machine = a dark block; you = a small ink human
figure; the machine's output = flat white pages; judgment marks = terracotta
check/dot; tiers = a four-block stack (dark, grey, kraft, white).

Pacing: until()/finish() read beat_sheet.json (narration is the clock).
Drawing laws: labels beside objects (>=32pt), terracotta only for checks/dots/
scan line, numerals ink, every scene adds new non-text shapes after its first
frame, all coords inside the safe frame.
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


# ═════════════════════════════ B00 — the hero: the tier map ═════════════════════════════
class B00_TierMap(Scene):
    def construct(self):
        iso = Iso(0, -0.6, 0.9)
        tiers = [
            iso.box(-1.8, -1.1, 0.00, 3.6, 2.2, 0.55, DARK_TOP, DARK_L, DARK_R),
            iso.box(-1.8, -1.1, 0.63, 3.6, 2.2, 0.55, BAR1, "#7C8288", "#6E747A"),
            iso.box(-1.8, -1.1, 1.26, 3.6, 2.2, 0.55, BOX_TOP, BOX_L, BOX_R),
            iso.box(-1.8, -1.1, 1.89, 3.6, 2.2, 0.55, PAGE_TOP, PAGE_L, PAGE_R),
        ]
        tier_ys = [-0.35, 0.21, 0.78, 1.35]
        nums = [T(str(i + 1), size=44, bold=True).move_to([-3.05, tier_ys[i], 0]) for i in range(4)]
        title = T("tier diagram").move_to([0, -2.95, 0])
        floor = shadow(0, -2.0, 4.6)
        fig = human(2.9, -1.3)
        tag_m = T("machine").move_to([4.3, -0.9, 0])
        lead_m = Line([3.95, -0.9, 0], [2.75, -0.75, 0], color=DIM, stroke_width=3)
        tag_y = T("you").move_to([4.3, 1.35, 0])
        lead_y = Line([3.95, 1.35, 0], [2.75, 1.2, 0], color=DIM, stroke_width=3)

        self.play(FadeIn(floor), FadeIn(tiers[0]), FadeIn(nums[0]), FadeIn(title), run_time=0.9)
        until(self, "The machine owns the bottom")
        self.play(FadeIn(tiers[1]), FadeIn(nums[1]), run_time=0.7)
        until(self, "You own the top")
        self.play(FadeIn(tiers[2]), FadeIn(nums[2]), run_time=0.7)
        until(self, "wrong level")
        self.play(FadeIn(tiers[3]), FadeIn(nums[3]), FadeIn(fig), run_time=0.7)
        self.play(fig.animate.shift(UP * 2.3), run_time=1.0)
        self.play(FadeIn(tag_m), FadeIn(lead_m), FadeIn(tag_y), FadeIn(lead_y), run_time=0.6)
        finish(self)


# ═════════════════════════════ B01 — Tier 1: the machine is superhuman ═════════════════════════════
class B01_TierOne(Scene):
    def construct(self):
        iso = Iso(0, -0.3, 1.0)
        machine = iso.mcp(-0.65, -0.65, 0)
        floor = shadow(0, -1.35, 2.6)
        label = T("machine").move_to([2.6, 0.5, 0])
        lead = Line([2.25, 0.5, 0], [1.5, 0.35, 0], color=DIM, stroke_width=3)
        fig = human(-2.8, -1.0)
        fig_ghost = human(-2.8, -1.0, color=GHOST)
        pages = [iso.page(-0.55, -0.7, 0.7 + i * 0.5) for i in range(5)]

        self.play(FadeIn(floor), FadeIn(machine), FadeIn(label), FadeIn(lead), FadeIn(fig), run_time=0.9)
        until(self, "The machine is superhuman here")
        self.play(FadeIn(pages[0], shift=DOWN * 1.4), run_time=0.45)
        self.play(FadeIn(pages[1], shift=DOWN * 1.4), run_time=0.45)
        until(self, "No one memorizes")
        self.play(FadeIn(pages[2], shift=DOWN * 1.4), run_time=0.45)
        self.play(FadeIn(pages[3], shift=DOWN * 1.4), run_time=0.45)
        self.play(FadeIn(pages[4], shift=DOWN * 1.4), run_time=0.45)
        until(self, "Racing it here")
        self.play(FadeOut(fig), FadeIn(fig_ghost), run_time=0.7)
        finish(self)


# ═════════════════════════════ B02 — Tier 2: contested space ═════════════════════════════
class B02_Contested(Scene):
    def construct(self):
        iso = Iso(-3.4, -0.4, 0.85)
        machine = iso.mcp(-0.6, -0.6, 0, 1.2, 1.2, 0.7)
        floor_m = shadow(-3.4, -1.35, 2.4)
        fig = human(3.4, -1.2)
        page = Iso(0, -0.3, 0.9).page(-0.55, -0.7, 0)
        label = T("contested").move_to([0, 2.0, 0])
        lead = Line([0.25, 1.75, 0], [0.2, 0.6, 0], color=DIM, stroke_width=3)
        call = T("your call").move_to([4.75, -0.2, 0])
        lead_c = Line([4.4, -0.2, 0], [3.85, -0.55, 0], color=DIM, stroke_width=3)
        dot = Dot(np.array([0.2, 0.15, 0]), radius=0.09, color=TERRA)

        self.play(FadeIn(floor_m), FadeIn(machine), FadeIn(fig), FadeIn(page), FadeIn(label), FadeIn(lead), run_time=1.0)
        until(self, "contested space")
        self.play(page.animate.shift(LEFT * 1.6), run_time=0.7)
        until(self, "rough work")
        self.play(page.animate.shift(RIGHT * 3.2), run_time=0.7)
        until(self, "you keep the judgment")
        self.play(GrowFromCenter(dot), FadeIn(call), FadeIn(lead_c), run_time=0.6)
        finish(self)


# ═════════════════════════════ B03 — Tier 3: judgment ═════════════════════════════
class B03_Judgment(Scene):
    def construct(self):
        iso = Iso(0, -0.3, 0.9)
        page = iso.page(-0.55, -0.7, 0)
        floor = shadow(0, -1.5, 2.6)
        fig = human(2.9, -1.1)
        lens = Circle(radius=0.34, color=INK, stroke_width=5).move_to([-0.5, -0.9, 0])
        handle = Line([-0.5 + 0.24, -0.9 - 0.24, 0], [-0.5 + 0.62, -0.9 - 0.62, 0], color=INK, stroke_width=5)
        glass = VGroup(lens, handle)
        label_o = T("the output").move_to([-3.6, 0.6, 0])
        lead_o = Line([-3.25, 0.6, 0], [-1.3, 0.15, 0], color=DIM, stroke_width=3)
        label_j = T("your judgment").move_to([3.4, 1.1, 0])
        lead_j = Line([3.05, 1.1, 0], [2.0, 0.6, 0], color=DIM, stroke_width=3)
        tick = check(0.9, 0.5, s=0.26, color=TERRA, w=9)

        self.play(FadeIn(floor), FadeIn(page), FadeIn(fig), FadeIn(label_o), FadeIn(lead_o), run_time=1.0)
        until(self, "Read the output")
        self.play(FadeIn(glass), run_time=0.5)
        until(self, "does it serve the real goal")
        self.play(glass.animate.shift(UP * 0.9), run_time=0.8)
        until(self, "Only a person knows")
        self.play(GrowFromCenter(tick), FadeIn(label_j), FadeIn(lead_j), run_time=0.6)
        finish(self)


# ═════════════════════════════ B04 — Tier 4: irreducible ═════════════════════════════
class B04_Irreducible(Scene):
    def construct(self):
        iso = Iso(-3.0, -0.6, 0.85)
        machine = iso.mcp(-0.6, -0.6, 0, 1.2, 1.2, 0.7)
        machine_dim = iso.box(-0.6, -0.6, 0, 1.2, 1.2, 0.7, top=GHOST, left=GHOST, right=GHOST)
        floor = shadow(-3.0, -1.5, 2.4)
        fig = human(-1.7, -1.2)
        arm = Line([-1.55, -0.85, 0], [-0.9, -0.55, 0], color=INK, stroke_width=7)
        p1 = Iso(0.2, -0.6, 0.85).page(-0.55, -0.7, 0)
        p2 = Iso(2.4, -0.6, 0.85).page(-0.55, -0.7, 0)
        q1 = T("?", size=52, bold=True).move_to([0.2, 0.15, 0])
        q2 = T("?", size=52, bold=True).move_to([2.4, 0.15, 0])
        dot = Dot(np.array([2.4, 0.75, 0]), radius=0.1, color=TERRA)
        label = T("irreducible").move_to([-4.35, 1.7, 0])
        lead = Line([-3.95, 1.7, 0], [-3.5, 0.5, 0], color=DIM, stroke_width=3)
        decide = T("you decide").move_to([2.4, -2.4, 0])
        lead_d = Line([2.4, -2.15, 0], [2.4, -1.35, 0], color=DIM, stroke_width=3)

        self.play(FadeIn(floor), FadeIn(machine), FadeIn(fig), FadeIn(label), FadeIn(lead), run_time=1.0)
        until(self, "which problem is worth solving")
        self.play(FadeOut(machine), FadeIn(machine_dim), run_time=0.7)
        until(self, "whether to trust the answer at all")
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(q1), FadeIn(q2), FadeIn(arm), run_time=0.8)
        until(self, "irreducible")
        self.play(GrowFromCenter(dot), FadeIn(decide), FadeIn(lead_d), run_time=0.6)
        finish(self)


# ═════════════════════════════ B05 — conducting ═════════════════════════════
class B05_Conducting(Scene):
    def construct(self):
        iso = Iso(-2.8, -0.5, 0.95)
        machine = iso.mcp(-0.6, -0.6, 0, 1.2, 1.2, 0.7)
        floor = shadow(-2.8, -1.5, 2.5)
        fig = human(2.6, -1.2)
        baton = Line([2.35, -0.8, 0], [2.95, -0.05, 0], color=INK, stroke_width=8)
        page = Iso(-2.8, 0.55, 0.95).page(-0.55, -0.7, 0)
        label = T("conduct").move_to([0, 2.35, 0])
        lead = Line([0.35, 2.1, 0], [1.75, 0.55, 0], color=DIM, stroke_width=3)

        self.play(FadeIn(floor), FadeIn(machine), FadeIn(fig), FadeIn(baton), FadeIn(label), FadeIn(lead), run_time=1.0)
        until(self, "Conducting")
        self.play(FadeIn(page), run_time=0.5)
        until(self, "catching the mistakes")
        self.play(page.animate.shift(RIGHT * 2.4), run_time=0.7)
        self.play(page.animate.shift(RIGHT * 2.2 + DOWN * 0.8), run_time=0.7)
        until(self, "That is the job now")
        self.play(baton.animate.shift(UP * 0.55), run_time=0.5)
        finish(self)


# ═════════════════════════════ B06 — the daily loop ═════════════════════════════
class B06_DailyLoop(Scene):
    def construct(self):
        iso = Iso(0, -2.4, 0.8)
        machine = iso.mcp(-0.6, -0.6, 0, 1.2, 1.2, 0.7)
        floor = shadow(0, -3.0, 2.4)
        tasks_list = [pill(-4 + i * 2.0, 1.6, 1.7) for i in range(5)]
        tasks = VGroup(*tasks_list)
        label = T("one task a day").move_to([-4.3, 2.7, 0])
        lead = Line([-3.95, 2.7, 0], [-3.35, 2.0, 0], color=DIM, stroke_width=3)
        page = Iso(0, -0.9, 0.8).page(-0.55, -0.7, 0.55)
        scan = Line([-0.85, -0.75, 0], [0.85, -0.75, 0], color=TERRA, stroke_width=7)
        spot = Circle(radius=0.3, color=INK, stroke_width=5).move_to([0.35, -0.35, 0])
        weak = T("weak spot").move_to([2.9, -0.4, 0])
        lead_w = Line([2.5, -0.4, 0], [0.75, -0.35, 0], color=DIM, stroke_width=3)

        self.play(*[FadeIn(t) for t in tasks_list], FadeIn(label), FadeIn(lead), FadeIn(floor), FadeIn(machine), run_time=1.0)
        until(self, "Run it through Claude")
        first = tasks_list[0]
        self.play(first.animate.shift(RIGHT * 4.0), run_time=0.6)
        self.play(first.animate.shift(DOWN * 3.0), run_time=0.6)
        until(self, "Read every line")
        self.play(FadeIn(page), FadeIn(scan), run_time=0.5)
        self.play(scan.animate.shift(UP * 1.3), run_time=0.7)
        self.play(FadeOut(scan), run_time=0.3)
        until(self, "Name one thing it got wrong")
        self.play(Create(spot), FadeIn(weak), FadeIn(lead_w), run_time=0.6)
        finish(self)


# ═════════════════════════════ B07 — what never leaves your desk ═════════════════════════════
class B07_NeverDelegate(Scene):
    def construct(self):
        iso = Iso(0, -0.2, 0.9)
        page = iso.page(-0.55, -0.7, 0)
        floor = shadow(0, -1.45, 2.6)
        sigline = Line([-1.0, -1.35, 0], [1.0, -1.35, 0], color=INK, stroke_width=3)
        label = T("your name owns it").move_to([-3.6, -1.9, 0])
        lead = Line([-3.2, -1.9, 0], [-1.4, -1.5, 0], color=DIM, stroke_width=3)
        words = ["you sign", "your cost", "your name"]
        pills = VGroup(*[pill(-3.0 + i * 3.0, 1.9, 2.3) for i in range(3)])
        caps = VGroup(*[T(w, size=32).move_to([-3.0 + i * 3.0, 1.9, 0]) for i, w in enumerate(words)])
        checks = VGroup(*[check(-3.0 + i * 3.0 - 1.55, 1.9, s=0.17, color=INK, w=8) for i in range(3)])
        base = Rectangle(width=1.2, height=0.35, fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([0, 1.9, 0])
        handle = Line([0, 2.05, 0], [0, 2.75, 0], color=INK, stroke_width=8)
        stamp = VGroup(base, handle)

        self.play(FadeIn(floor), FadeIn(page), FadeIn(sigline), FadeIn(label), FadeIn(lead), run_time=1.0)
        until(self, "Anything you sign your name to")
        self.play(FadeIn(pills), FadeIn(caps), run_time=0.7)
        until(self, "Your reputation")
        self.play(stamp.animate.shift(DOWN * 2.4), run_time=0.6)
        self.play(stamp.animate.shift(UP * 2.4), run_time=0.5)
        until(self, "your judgment owns it")
        self.play(*[GrowFromCenter(c) for c in checks], run_time=0.6)
        finish(self)


# ═════════════════════════════ B08 — the one that's yours ═════════════════════════════
class B08_YoursAlone(Scene):
    def construct(self):
        words = ["draft email", "fact question", "fire vendor", "summarize meeting"]
        xs = [-2.0, 2.0, -2.0, 2.0]
        ys = [1.0, 1.0, -0.7, -0.7]
        pill_list = [pill(xs[i], ys[i], 3.4, h=0.7) for i in range(4)]
        pills = VGroup(*pill_list)
        cap_list = [T(words[i], size=32).move_to([xs[i], ys[i], 0]) for i in range(4)]
        caps = VGroup(*cap_list)
        ghost_pills = VGroup(*[pill(xs[i], ys[i], 3.4, h=0.7, fill=GHOST) for i in [0, 1, 3]])
        ghost_caps = VGroup(*[T(words[i], size=32, color=DIM).move_to([xs[i], ys[i], 0]) for i in [0, 1, 3]])
        label = T("yours alone").move_to([0, 2.6, 0])
        cur = cursor(-2.0, 1.85)
        tick = check(0.35, -0.7, s=0.26, color=TERRA, w=9)

        self.play(FadeIn(pills), FadeIn(caps), FadeIn(label), run_time=1.0)
        until(self, "Which one is yours alone")
        self.play(FadeIn(cur), run_time=0.4)
        self.play(cur.animate.shift(RIGHT * 4.0 + DOWN * 1.7), run_time=0.7)
        until(self, "The vendor call")
        self.play(GrowFromCenter(tick), run_time=0.5)
        until(self, "only you can own the decision")
        self.play(FadeOut(VGroup(pill_list[0], pill_list[1], pill_list[3])),
                  FadeOut(VGroup(cap_list[0], cap_list[1], cap_list[3])),
                  FadeIn(ghost_pills), FadeIn(ghost_caps), run_time=0.7)
        finish(self)
