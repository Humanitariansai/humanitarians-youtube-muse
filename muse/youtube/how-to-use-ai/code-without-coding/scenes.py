"""
scenes.py — show-tell drawings for code-without-coding (How to AI).

Nine isometric Manim scenes (B00..B08), one per body beat. The iso_kit block is
pasted at the top (Gate A copies only this file). Pacing: every motion is keyed
to a narration phrase inside the first ~35% of its beat via until(), so nothing
is mid-motion at the clip midpoint under GATE T/Gate V sampling, whatever the
measured Kokoro audio comes out as. finish() holds to the audio.
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
            self.quad([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x1, y1, z1)], BOX_IN2))
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
def floor_shadow(cx=0.0, cy=-2.9, w=7.0):
    return Ellipse(width=w, height=0.7, fill_color=GHOST, fill_opacity=0.55,
                   stroke_width=0).move_to([cx, cy, 0])


def prompt_card(cx, cy, w=3.2, h=2.0, n_lines=4, short=False):
    """A flat prompt/answer page in iso. short=True draws short simple lines."""
    iso = Iso(cx, cy, 0.9)
    slab = iso.box(-w / 2, -h / 2, 0, w, h, 0.10, PAGE_TOP, PAGE_L, PAGE_R, sw=2)
    zt = 0.10
    lines = []
    for i in range(n_lines):
        f = 0.25 + 0.5 * i / max(1, n_lines - 1)
        x1 = -w / 2 + 0.35
        x2 = (-w / 2 + 0.35 + (w - 0.7) * 0.55) if short else (w / 2 - 0.35)
        lines.append(Line(iso.p(x1, -h / 2 + h * f, zt), iso.p(x2, -h / 2 + h * f, zt),
                          color=GHOST, stroke_width=5))
    return VGroup(slab, VGroup(*lines))


def name_tag(text, cx, cy, w=2.6, stroke=INK):
    """A small white name-tag carrying a word. Ink text, terracotta seal dot (house pattern)."""
    tag = RoundedRectangle(width=w, height=0.72, corner_radius=0.36,
                           fill_color="#FFFFFF", fill_opacity=1,
                           stroke_color=stroke, stroke_width=2.5).move_to([cx, cy, 0])
    t = T(text, size=34, color=INK).move_to([cx - 0.1, cy - 0.02, 0])
    dot = Dot([cx + w / 2 - 0.28, cy, 0], radius=0.09, color=TERRA)
    return VGroup(tag, t, dot)


def ai_window(cx, cy, w=3.4, h=2.6):
    """A pale AI tool window carried by a grey title band (BAR1, not dark: GATE T)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    band = Rectangle(width=w - 0.06, height=0.55, fill_color=BAR1, fill_opacity=1,
                     stroke_width=0).move_to([cx, cy + h / 2 - 0.30, 0])
    title = T("Claude", size=32, color=INK).move_to([cx - w / 2 + 0.75, cy + h / 2 - 0.30, 0])
    dots = VGroup(*[Dot([cx + w / 2 - 0.35 - 0.35 * i, cy + h / 2 - 0.30, 0],
                        radius=0.08, color=GHOST) for i in range(3)])
    line1 = Line([cx - w / 2 + 0.4, cy - 0.2, 0], [cx + w / 2 - 1.2, cy - 0.2, 0],
                 color=GHOST, stroke_width=5)
    cur = cursor(cx - w / 2 + 0.4, cy - 0.55)
    return VGroup(card, band, title, dots, line1, cur)


def button(x, y, w=2.0):
    """A clickable button: CARD pill with an ink outline (white needs the outline for Gate V)."""
    return RoundedRectangle(width=w, height=0.62, corner_radius=0.31,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=3).move_to([x, y, 0])


def ink_cross(cx, cy, arm=0.4, w=8):
    return VGroup(Line([cx - arm, cy - arm, 0], [cx + arm, cy + arm, 0], color=INK, stroke_width=w),
                  Line([cx - arm, cy + arm, 0], [cx + arm, cy - arm, 0], color=INK, stroke_width=w))


# ═════════════════════════════ scenes ═════════════════════════════
class B00_YourPage(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 8.0)
        page = prompt_card(0, 0.5, 3.4, 2.2, 4)
        page.shift(UP * 4.5)
        lab = T("your page", size=40, color=INK).move_to([0, -1.45, 0])
        ring = Circle(radius=2.6, stroke_color=INK, stroke_width=4).move_to([0, 0.5, 0])
        chk = check(2.9, 1.3, s=0.22, color=TERRA, w=8)

        self.play(FadeIn(shadow), run_time=0.5)
        until(self, "Imagine asking")
        self.play(page.animate.shift(DOWN * 4.5), rate_func=ease_in, run_time=0.8)
        until(self, "and getting it")
        self.play(FadeIn(lab), run_time=0.5)
        self.play(GrowFromCenter(ring), run_time=0.5)
        self.play(FadeOut(ring), FadeIn(chk), run_time=0.5)
        until(self, "That's the whole promise")
        finish(self)


class B01_HowItWorks(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.5)
        card = prompt_card(-3.7, 0.5, 2.8, 1.8, 3)
        clab = T("your words", size=34, color=INK).move_to([-3.7, -1.15, 0])
        win = ai_window(2.9, 0.5, 3.0, 2.4)
        lens = [1.5, 2.1, 1.2, 1.8]
        lines = VGroup(*[Line([1.75, 0.95 - 0.35 * i, 0], [1.75 + ln, 0.95 - 0.35 * i, 0],
                               color=DIM, stroke_width=5) for i, ln in enumerate(lens)])
        codelab = T("code", size=34, color=INK).move_to([2.9, -1.15, 0])
        page = prompt_card(-0.7, 0.5, 2.6, 1.8, 3)
        page.shift(UP * 3.5)
        plab = T("your page", size=34, color=INK).move_to([-0.7, -1.15, 0])

        self.play(FadeIn(shadow, card, clab, win), run_time=0.7)
        until(self, "Your words go into the tool")
        self.play(card.animate.shift(RIGHT * 3.5), run_time=0.8)
        self.play(FadeOut(card, clab), run_time=0.5)
        until(self, "it writes the code")
        self.play(FadeIn(lines, codelab), run_time=0.7)
        until(self, "your page comes back")
        self.play(page.animate.shift(DOWN * 3.5), rate_func=ease_in, run_time=0.8)
        self.play(FadeIn(plab), run_time=0.5)
        finish(self)


class B02_Checkable(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 11.0)
        c1 = prompt_card(-3.6, 0.7, 2.5, 1.7, 3)
        l1 = T("a page", size=34, color=INK).move_to([-3.6, -0.95, 0])
        c2 = prompt_card(0, 0.7, 2.5, 1.7, 3)
        l2 = T("a quiz", size=34, color=INK).move_to([0, -0.95, 0])
        c3 = prompt_card(3.6, 0.7, 2.5, 1.7, 3)
        l3 = T("a tracker", size=34, color=INK).move_to([3.6, -0.95, 0])
        banner = T("you can check it", size=38, color=INK).move_to([0, 2.35, 0])

        self.play(FadeIn(shadow), run_time=0.5)
        until(self, "First, what's safe to build")
        self.play(AnimationGroup(GrowFromCenter(c1), FadeIn(l1),
                                 GrowFromCenter(c2), FadeIn(l2),
                                 GrowFromCenter(c3), FadeIn(l3),
                                 lag_ratio=0.25), run_time=1.8)
        until(self, "first safety rule")
        self.play(FadeIn(banner), run_time=0.7)
        finish(self)


class B03_OnlyYou(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 9.0)
        ring = Circle(radius=1.7, stroke_color=DIM, stroke_width=5).move_to([0, 0.3, 0])
        page = prompt_card(0, 0.3, 2.2, 1.5, 3)
        lab = T("only you", size=36, color=INK).move_to([0, -2.0, 0])
        chk = check(1.15, -0.8, s=0.2, color=TERRA, w=8)
        secret = name_tag("password", 0, 2.94, w=2.4)
        slab2 = T("not passwords", size=34, color=INK).move_to([3.5, -1.9, 0])

        self.play(FadeIn(shadow, ring, page, lab, chk), run_time=0.9)
        until(self, "keep it personal")
        self.play(FadeIn(secret), run_time=0.4)
        until(self, "Passwords, payments")
        self.play(secret.animate.shift(DOWN * 0.6), run_time=0.5)
        self.play(secret.animate.shift(UP * 0.6), run_time=0.5)
        self.play(FadeOut(secret), FadeIn(slab2), run_time=0.6)
        finish(self)


class B04_TooBig(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.9, 9.0)
        pages = VGroup(*[prompt_card(0.15 * (i % 2) - 0.075, 0.9 - i * 0.5, 2.6, 1.3, 2)
                          for i in range(5)])
        cross = ink_cross(2.7, 1.3, arm=0.4)
        lab1 = T("too big", size=36, color=INK).move_to([0, -2.5, 0])
        clean = prompt_card(0, 0.5, 3.0, 2.0, 3)
        clean.shift(UP * 3.5)
        chk = check(2.6, 1.2, s=0.22, color=TERRA, w=8)
        lab2 = T("one small thing", size=36, color=INK).move_to([0, -1.75, 0])
        wreck = VGroup(pages, cross, lab1)

        self.play(FadeIn(shadow), run_time=0.5)
        until(self, "Mistake one")
        self.play(AnimationGroup(*[FadeIn(p) for p in pages], lag_ratio=0.18), run_time=1.5)
        self.play(pages.animate.rotate(0.06), run_time=0.4)
        self.play(VGroup(pages[3], pages[4]).animate.shift(DOWN * 2.0 + RIGHT * 0.8), run_time=0.6)
        self.play(FadeIn(cross, lab1), run_time=0.6)
        until(self, "Start small")
        self.play(FadeOut(wreck), run_time=0.6)
        self.play(clean.animate.shift(DOWN * 3.5), rate_func=ease_in, run_time=0.8)
        self.play(FadeIn(chk, lab2), run_time=0.6)
        finish(self)


class B05_NoSecrets(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 9.5)
        win = ai_window(2.4, 0.2, 3.2, 2.6)
        secret = name_tag("password", 2.4, 2.9, w=2.4)
        cross = ink_cross(2.4, 1.95, arm=0.45)
        lab = T("never paste", size=38, color=INK).move_to([-3.2, 0.5, 0])

        self.play(FadeIn(shadow, win, secret), run_time=0.8)
        until(self, "Mistake two")
        self.play(secret.animate.shift(DOWN * 0.95), run_time=0.7)
        until(self, "anything private")
        self.play(FadeIn(cross), run_time=0.5)
        until(self, "Never paste")
        self.play(secret.animate.shift(UP * 0.95), run_time=0.6)
        self.play(FadeOut(secret, cross), FadeIn(lab), run_time=0.6)
        finish(self)


class B06_TestIt(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.9, 10.0)
        page = prompt_card(0, 1.2, 3.2, 1.7, 3)
        btn1, btn2, btn3 = button(-2.4, -1.1), button(0, -1.1), button(2.4, -1.1)
        cur = cursor(-4.5, 1.5)
        chk1 = check(-2.4, -0.15, s=0.18, color=TERRA, w=7)
        chk2 = check(0, -0.15, s=0.18, color=TERRA, w=7)
        cross3 = ink_cross(2.4, -0.35, arm=0.3)
        bugdot = Dot([2.4, -1.1, 0], radius=0.1, color=TERRA)
        lab = T("click it yourself", size=36, color=INK).move_to([0, -2.35, 0])

        self.play(FadeIn(shadow, page, btn1, btn2, btn3), run_time=0.8)
        until(self, "Mistake three")
        self.play(FadeIn(cur), run_time=0.4)
        self.play(cur.animate.move_to([-2.4, -0.4, 0]), run_time=0.5)
        self.play(FadeIn(chk1), run_time=0.4)
        self.play(cur.animate.move_to([0, -0.4, 0]), run_time=0.5)
        self.play(FadeIn(chk2), run_time=0.4)
        until(self, "a bug hiding")
        self.play(cur.animate.move_to([2.4, -0.4, 0]), run_time=0.5)
        self.play(FadeIn(cross3, bugdot, lab), run_time=0.6)
        finish(self)


class B07_DescribeItBack(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.5)
        page = prompt_card(-2.7, 0.5, 2.8, 1.9, 3)
        bugdot = Dot([-1.7, 1.45, 0], radius=0.1, color=TERRA)
        blab = T("a bug", size=34, color=INK).move_to([-2.7, -1.35, 0])
        win = ai_window(3.1, 0.5, 2.8, 2.4)
        shaft = Line([-1.1, 0.5, 0], [1.5, 0.5, 0], color=INK, stroke_width=5)
        head = Polygon([1.5, 0.5, 0], [1.2, 0.68, 0], [1.2, 0.32, 0],
                       fill_color=INK, fill_opacity=1, stroke_width=0)
        arrow = VGroup(shaft, head)
        fixed = prompt_card(-2.7, 0.5, 2.8, 1.9, 3)
        chk = check(-0.7, 1.5, s=0.2, color=TERRA, w=8)
        lab2 = T("describe it back", size=36, color=INK).move_to([3.1, -1.35, 0])

        self.play(FadeIn(shadow, win), run_time=0.5)
        until(self, "don't panic")
        self.play(FadeIn(page, bugdot, blab), run_time=0.8)
        until(self, "Describe the problem back")
        self.play(Create(arrow), run_time=0.8)
        until(self, "It fixes the code")
        self.play(FadeOut(page, bugdot, blab), FadeIn(fixed), run_time=0.7)
        self.play(FadeIn(chk, lab2), run_time=0.6)
        finish(self)


class B08_WhyNow(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.0)
        hero = T("25%", size=150, color=INK, bold=True).move_to([-3.0, 0.7, 0])
        sub = T("AI-written code", size=36, color=INK).move_to([-3.0, -1.15, 0])
        curve = ParametricFunction(lambda t: np.array([t, -1.6 + 3.4 * ((t + 2.2) / 5.4) ** 2, 0]),
                                   t_range=[-2.2, 3.2, 0.05], color=INK, stroke_width=7)
        enddot = Dot([3.2, 1.8, 0], radius=0.11, color=TERRA)
        caption = T("per Y Combinator", size=32, color=INK).move_to([0.5, -2.2, 0])

        self.play(FadeIn(shadow), run_time=0.4)
        until(self, "A quarter")
        self.play(FadeIn(hero, sub), run_time=0.7)
        self.play(Create(curve), FadeIn(enddot), run_time=0.9)
        self.play(FadeIn(caption), run_time=0.6)
        finish(self)
