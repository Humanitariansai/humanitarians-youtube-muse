"""
scenes.py — show-tell drawings for tell-the-ai-who-to-be (film #2, How to AI).

Six isometric Manim scenes (B00..B06), one per body beat. The iso_kit block is
pasted at the top (Gate A copies only this file). Pacing: every motion is keyed
to a narration phrase in the first ~30% of its beat via until(), so no animation
is ever in progress at the clip midpoint, whatever the measured Kokoro audio
comes out as. finish() holds to the audio.
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


def role_tag(text, cx, cy, w=2.6, fill="#FFFFFF", stroke=INK):
    """A small white name-tag carrying a role. Ink text, terracotta seal dot."""
    tag = RoundedRectangle(width=w, height=0.72, corner_radius=0.36,
                           fill_color=fill, fill_opacity=1,
                           stroke_color=stroke, stroke_width=2.5).move_to([cx, cy, 0])
    t = T(text, size=34, color=INK).move_to([cx - 0.1, cy - 0.02, 0])
    dot = Dot([cx + w / 2 - 0.28, cy, 0], radius=0.09, color=TERRA)
    return VGroup(tag, t, dot)


def ai_window(cx, cy, w=3.4, h=2.6):
    """A pale Claude window carried by a grey title band (BAR1, not dark: GATE T)."""
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


def slider_bank(cx, top_y, w, labels, dy=0.9):
    """Four register sliders. Returns (group, knobs, row_ys); knobs start centred."""
    g = VGroup()
    knobs, rows = [], []
    for i, lab in enumerate(labels):
        y = top_y - i * dy
        rows.append(y)
        track = Line([cx - w / 2, y, 0], [cx + w / 2, y, 0], color=GHOST, stroke_width=7)
        t = T(lab, size=32, color=INK).move_to([cx - w / 2 - 1.0, y - 0.02, 0])
        k = Dot([cx, y, 0], radius=0.13, color=TERRA)
        knobs.append(k)
        g.add(track, t, k)
    return g, knobs, rows


# ═════════════════════════════ scenes ═════════════════════════════
class B00_RoleLine(Scene):
    def construct(self):
        shadow = floor_shadow(0.3, -2.75, 8.0)
        win = ai_window(3.3, 0.5)
        card = prompt_card(-2.6, 0.5, 3.2, 2.0, 4)
        lab = T("your prompt", size=36, color=INK).move_to([-2.6, -1.3, 0])
        tag = role_tag("act as a chef", -2.6, 2.9, w=2.7)

        self.play(FadeIn(shadow, win), run_time=0.7)
        until(self, "Act as a chef")
        self.play(FadeIn(card, lab), run_time=0.7)
        self.play(FadeIn(tag), run_time=0.6)
        self.play(tag.animate.shift(DOWN * 0.85), run_time=0.6)
        until(self, "That line has a name")
        carry = VGroup(card, tag, lab)
        self.play(carry.animate.shift(RIGHT * 5.9), run_time=0.8)
        until(self, "It changes who you're asking")
        finish(self)


class B01_Calibrate(Scene):
    def construct(self):
        shadow = floor_shadow(-0.7, -2.75, 9.0)
        card = prompt_card(-3.6, 0.3, 3.0, 1.9, 4)
        tag = role_tag("act as a chef", -3.6, 1.95, w=2.7)
        bank, knobs, rows = slider_bank(2.2, 1.5, 2.6,
                                        ["words", "knowledge", "tone", "depth"])
        targets = [1.2, 1.4, 1.5, 1.15]

        self.play(FadeIn(shadow, card, tag), run_time=0.7)
        until(self, "four dials")
        self.play(FadeIn(bank), run_time=0.7)
        self.play(AnimationGroup(*[k.animate.move_to([tx, y, 0])
                                   for k, tx, y in zip(knobs, targets, rows)]),
                  run_time=0.7)
        until(self, "The AI doesn't become")
        finish(self)


class B02_DialsMove(Scene):
    def construct(self):
        shadow = floor_shadow(-0.5, -2.75, 9.5)
        bank, knobs, rows = slider_bank(-2.6, 1.5, 3.0,
                                        ["words", "knowledge", "tone", "depth"])
        targets = [-3.7, -3.5, -3.3, -3.8]
        page = prompt_card(3.0, 0.15, 2.8, 2.4, 4)
        page2 = prompt_card(3.0, 0.15, 2.8, 2.4, 3, short=True)
        plab = T("the answer", size=34, color=INK).move_to([3.0, -1.5, 0])
        tag = role_tag("patient tutor", -2.6, 2.55, w=2.5)

        self.play(FadeIn(shadow, bank, page, plab), run_time=0.7)
        until(self, "The role lands")
        self.play(FadeIn(tag),
                  AnimationGroup(*[k.animate.move_to([tx, y, 0])
                                   for k, tx, y in zip(knobs, targets, rows)]),
                  FadeOut(page), FadeIn(page2),
                  run_time=1.0)
        until(self, "The role only set the register")
        finish(self)


class B03_TwoDoctors(Scene):
    def construct(self):
        shadow = floor_shadow(0, -3.0, 9.0)
        qcard = prompt_card(0, 2.2, 3.0, 1.5, 3)
        qlab = T("same question", size=34, color=INK).move_to([0, 0.92, 0])
        left = prompt_card(-2.9, -1.15, 2.6, 1.8, 3)
        right = prompt_card(2.9, -1.15, 2.6, 1.8, 8)
        llab = T("for a child", size=34, color=INK).move_to([-2.9, -2.6, 0])
        rlab = T("grand rounds", size=34, color=INK).move_to([2.9, -2.6, 0])
        t1 = role_tag("oncologist", -2.9, 0.35, w=2.3)
        t2 = role_tag("pathologist", 2.9, 0.35, w=2.4)

        self.play(FadeIn(shadow, qcard, qlab), run_time=0.7)
        until(self, "two doctors")
        self.play(FadeIn(left, right, llab, rlab), run_time=0.8)
        until(self, "pediatric oncologist")
        self.play(FadeIn(t1, t2), run_time=0.7)
        until(self, "It only set the register")
        finish(self)


class B04_RoleVsPersona(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 10.5)
        lc = prompt_card(-3.1, 0.2, 3.4, 2.2, 3)
        rc = prompt_card(3.1, 0.2, 3.4, 2.2, 3)
        llab = T("role", size=36, color=INK).move_to([-3.1, -1.75, 0])
        rlab = T("persona", size=36, color=INK).move_to([3.1, -1.75, 0])
        ltag = role_tag("expert tax attorney", -3.1, 1.8, w=3.1)
        quote = T("\u201c", size=190, color=GHOST).move_to([3.1, 0.35, 0])
        quote.set_z_index(-1)
        rtags = VGroup(role_tag("Marcus", 2.15, 2.0, w=1.8),
                       role_tag("sardonic", 4.05, 2.0, w=2.0),
                       role_tag("nautical metaphors", 3.1, 2.8, w=2.9))

        self.play(FadeIn(shadow, lc, rc, llab, rlab), run_time=0.7)
        until(self, "small and functional")
        self.play(FadeIn(ltag), run_time=0.7)
        until(self, "whole costume")
        self.play(FadeIn(quote, rtags), run_time=0.8)
        until(self, "Know which one you need")
        finish(self)


class B05_WhenItHelps(Scene):
    def construct(self):
        iso = Iso(0, 0, 1.0)
        shadow = floor_shadow(0, -3.05, 10.0)
        b1back, b1front = iso.open_box(-4.3, -0.9, 0, 2.8, 2.0, 1.1)
        tape = iso.tape(-4.3, -0.9, 1.1, 2.8, 2.0)
        b2back, b2front = iso.open_box(1.5, -0.9, 0, 2.8, 2.0, 1.1)
        llab = T("role helps", size=36, color=INK).move_to([-2.6, -2.95, 0])
        rlab = T("skip it", size=36, color=INK).move_to([2.42, -2.95, 0])
        left_tags = VGroup(role_tag("feedback", -2.6, 0.6, w=1.9, stroke=DIM),
                           role_tag("explaining", -2.6, -0.15, w=2.1, stroke=DIM),
                           role_tag("advice", -2.6, -0.9, w=1.7, stroke=DIM))
        chk = check(-1.15, -2.95, s=0.2, color=TERRA, w=7)
        right_tags = VGroup(role_tag("a date", 2.42, -0.7, w=1.7, stroke=DIM),
                            role_tag("a sum", 2.42, -1.45, w=1.6, stroke=DIM))
        cross = VGroup(Line([3.72, -3.13, 0], [4.08, -2.77, 0], color=INK, stroke_width=7),
                       Line([3.72, -2.77, 0], [4.08, -3.13, 0], color=INK, stroke_width=7))

        self.play(FadeIn(shadow, b1back, b1front, tape, b2back, b2front, llab, rlab),
                  run_time=0.7)
        until(self, "Two piles")
        self.play(FadeIn(left_tags), run_time=0.5)
        self.play(left_tags.animate.shift(DOWN * 0.9), FadeIn(chk), run_time=0.5)
        until(self, "Extracting a date")
        self.play(FadeIn(right_tags, cross), run_time=0.8)
        until(self, "skip it")
        finish(self)


class B06_SpecificBeatsVague(Scene):
    def construct(self):
        shadow = floor_shadow(0, -2.75, 8.0)
        card = prompt_card(0, 0.1, 3.6, 2.2, 3)
        genius = role_tag("genius", 0, 0.95, w=1.9, stroke=DIM)
        x1 = Line([-0.8, 0.62, 0], [0.8, 1.28, 0], color=INK, stroke_width=7)
        x2 = Line([-0.8, 1.28, 0], [0.8, 0.62, 0], color=INK, stroke_width=7)
        tag1 = role_tag("patient math tutor", 0, 0.95, w=2.9)
        tag2 = role_tag("for a ten-year-old", 0, 0.05, w=2.9)
        lab = T("specific beats vague", size=34, color=INK).move_to([0, -1.7, 0])

        self.play(FadeIn(shadow, card, genius), run_time=0.7)
        until(self, "is vague")
        self.play(FadeIn(x1, x2), run_time=0.7)
        until(self, "Make the role specific")
        self.play(FadeOut(genius, x1, x2), FadeIn(tag1, tag2, lab), run_time=0.8)
        until(self, "put the line first")
        finish(self)
