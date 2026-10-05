"""
scenes.py — Make it remember (and forget), show-tell Manim body scenes.

PASTE of the show-tell iso_kit (do not import: Gate A copies only this file),
then film helpers, then nine scene classes named <BID>_<Name>(Scene).
Claude palette: stage #F2F0E9, ink #3D3929, terracotta #D97757.
Safe area: +/-6.2 x, +/-3.3 y. Type floor 32.

The recurring cast: the notebook (open kraft tray with note cards), chat
windows, the settings panel, the pencil, terracotta X marks and checks.
"""
from manim import *
import numpy as np
import json as _json, os as _os

# ============ ISO KIT (show-tell) — pasted from templates/iso_kit.py ============
STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; CARD = "#FAF9F5"
BOX_TOP, BOX_L, BOX_R = "#F3E9D8", "#DCC9AA", "#C7AE86"
BOX_IN1, BOX_IN2, BOX_FLOOR = "#CDB894", "#BFA67E", "#B39A72"
DARK_TOP, DARK_L, DARK_R = "#3A3530", "#26221F", "#1E1B18"
PAGE_TOP, PAGE_L, PAGE_R = "#FFFFFF", "#ECE7DF", "#E2DCD2"
BAR1, BAR2, BAR3 = "#8B8F96", "#B4AFA6", "#D9D4C7"
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
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        return VGroup(
            self.quad([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], left, sw=sw),
            self.quad([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], right, sw=sw),
            self.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top, sw=sw))

    def open_box(self, x0, y0, z0, w, d, h):
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
        ym = y0 + d / 2
        return VGroup(
            self.quad([(x0, ym - t, z1), (x0 + w, ym - t, z1), (x0 + w, ym + t, z1), (x0, ym + t, z1)], TERRA, sw=0),
            self.quad([(x0, ym - t, z1), (x0, ym + t, z1), (x0, ym + t, z1 - drop), (x0, ym - t, z1 - drop)], TERRA, sw=0))

    def mcp(self, x0, y0, z0, w=1.3, d=1.3, h=0.7):
        body = self.box(x0, y0, z0, w, d, h, DARK_TOP, DARK_L, DARK_R)
        ports = VGroup(*[self.box(x0 + w * f, y0 - 0.18, z0 + h * 0.3, w * 0.16, 0.18, h * 0.3, GHOST, BOX_IN1, BOX_IN2, sw=1)
                         for f in (0.22, 0.58)])
        return VGroup(body, ports)

    def page(self, x0, y0, z0, w=1.1, d=1.4):
        slab = self.box(x0, y0, z0, w, d, 0.06, PAGE_TOP, PAGE_L, PAGE_R, sw=1.5)
        zt = z0 + 0.06
        lines = VGroup(*[Line(self.p(x0 + 0.2, y0 + d * f, zt), self.p(x0 + w - 0.2, y0 + d * f, zt), color=GHOST, stroke_width=4)
                         for f in (0.3, 0.5, 0.7)])
        dot = Dot(self.p(x0 + 0.2, y0 + d * 0.86, zt), radius=0.06, color=TERRA)
        return VGroup(slab, lines, dot)

    def server(self, x0, y0, z0, w=1.4, d=1.4, slab=0.42, n=3):
        stack = VGroup(*[self.box(x0, y0, z0 + i * (slab + 0.04), w, d, slab, DARK_TOP, DARK_L, DARK_R) for i in range(n)])
        lights = VGroup(*[Dot(self.p(x0 + 0.25, y0, z0 + i * (slab + 0.04) + slab / 2), radius=0.06, color=GHOST) for i in range(n)])
        return stack, lights


def ease_in(t):
    return t * t


def check(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.75, 0], color=color, stroke_width=w),
                  Line([x - s * 0.3, y - s * 0.75, 0], [x + s * 1.1, y + s * 0.85, 0], color=color, stroke_width=w))


def cursor(x, y, s=0.45):
    return Polygon([x, y, 0], [x, y - s, 0], [x + s * 0.28, y - s * 0.72, 0], [x + s * 0.62, y - s * 0.66, 0],
                   fill_color=INK, fill_opacity=1, stroke_color=CARD, stroke_width=2)


def pill(x, y, w, h=0.62, fill="#FFFFFF"):
    return RoundedRectangle(width=w, height=h, corner_radius=h / 2, fill_color=fill, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


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

# ============ film helpers (make-it-remember) ============
# Cast: the notebook (open kraft tray, recurs B00-B05/B07/B08), note cards,
# chat windows + bubbles, the settings panel, the archive cabinet, the pencil,
# terracotta X marks / checks. Labels sit beside objects.

KRAFT_CABLE = "#9C8462"  # deep kraft for connectors (never ink-edged cables)


def lab(s, x, y, size=34, color=INK):
    return T(s, size=size, color=color).move_to([x, y, 0])


def floor_shadow(cx, w=3.0):
    return Ellipse(width=w, height=0.3, fill_color=GHOST, fill_opacity=1,
                   stroke_width=0).move_to([cx, -2.9, 0])


def chat_window(cx, cy, w, h):
    """Pale chat window: card body, dark title bar (contrast law), terracotta dot."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    bar = RoundedRectangle(width=w - 0.04, height=0.5, corner_radius=0.14,
                           fill_color=DARK_TOP, fill_opacity=1,
                           stroke_width=0).move_to([cx, cy + h / 2 - 0.27, 0])
    dot = Dot([cx - w / 2 + 0.45, cy + h / 2 - 0.27, 0], radius=0.09, color=TERRA)
    return VGroup(body, bar, dot)


def bubble(lines, cx, cy, w, fill=CARD):
    """Chat bubble with grey (DIM) outline so it stays distinct inside the ink window."""
    texts = VGroup(*[T(s, size=32) for s in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
    bg = RoundedRectangle(width=max(w, texts.width + 0.7),
                          height=texts.height + 0.55, corner_radius=0.22,
                          fill_color=fill, fill_opacity=1,
                          stroke_color=DIM, stroke_width=2.5).move_to([cx, cy, 0])
    texts.move_to(bg.get_center())
    return VGroup(bg, texts)


def note_card(lines, cx, cy, w=2.8):
    """A memory note card: white, ink outline, sits at z=1 inside the notebook tray."""
    texts = VGroup(*[T(s, size=32) for s in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
    bg = RoundedRectangle(width=max(w, texts.width + 0.7),
                          height=texts.height + 0.5, corner_radius=0.12,
                          fill_color="#FFFFFF", fill_opacity=1,
                          stroke_color=INK, stroke_width=3).move_to([cx, cy, 0])
    texts.move_to(bg.get_center())
    grp = VGroup(bg, texts)
    grp.set_z_index(1)
    return grp


def notebook_open(cx, cy, w=3.6):
    """The notebook: kraft tray (back) with a tall front wall; cards land between."""
    back = RoundedRectangle(width=w, height=1.3, corner_radius=0.12,
                            fill_color=BOX_FLOOR, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy + 0.55, 0])
    wall = RoundedRectangle(width=w, height=1.7, corner_radius=0.12,
                            fill_color=BOX_R, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy - 0.75, 0])
    wall.set_z_index(2)
    return VGroup(back, wall)


def notebook_closed(cx, cy, w=3.2, h=1.6):
    """The notebook with the lid on: kraft box, grey strap, one terracotta seal."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.12,
                            fill_color=BOX_R, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    strap = RoundedRectangle(width=w * 0.28, height=h + 0.02, corner_radius=0.06,
                             fill_color=DIM, fill_opacity=1,
                             stroke_width=0).move_to([cx, cy, 0])
    seal = Dot([cx, cy, 0], radius=0.11, color=TERRA)
    return VGroup(body, strap, seal)


def settings_panel(cx, cy, w=4.6, h=3.8):
    body = RoundedRectangle(width=w, height=h, corner_radius=0.16,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    rows = VGroup(*[RoundedRectangle(width=w - 0.9, height=0.52, corner_radius=0.1,
                                     fill_color=GHOST, fill_opacity=1,
                                     stroke_width=0).move_to(
                                         [cx, cy + h / 2 - 0.85 - i * 0.78, 0])
                     for i in range(4)])
    return VGroup(body, rows)


def kw_pill(text, cx, cy, w):
    bg = RoundedRectangle(width=w, height=0.72, corner_radius=0.36,
                          fill_color="#FFFFFF", fill_opacity=1,
                          stroke_color=INK, stroke_width=3).move_to([cx, cy, 0])
    t = T(text, size=32).move_to([cx, cy - 0.02, 0])
    return VGroup(bg, t)


def xmark(cx, cy, s=0.28, color=TERRA, w=8):
    return VGroup(
        Line([cx - s, cy + s, 0], [cx + s, cy - s, 0], color=color, stroke_width=w),
        Line([cx - s, cy - s, 0], [cx + s, cy + s, 0], color=color, stroke_width=w))


def pencil(cx, cy, s=1.0):
    body = Rectangle(width=1.3 * s, height=0.34 * s, fill_color=BOX_TOP,
                     fill_opacity=1, stroke_color=INK,
                     stroke_width=3).move_to([cx, cy, 0])
    tip = Polygon([cx + 0.65 * s, cy + 0.17 * s, 0],
                  [cx + 0.65 * s, cy - 0.17 * s, 0],
                  [cx + 1.05 * s, cy, 0],
                  fill_color=INK, fill_opacity=1, stroke_width=0)
    return VGroup(body, tip)


def archive_cabinet(cx, cy, w=2.6):
    """Dark archive cabinet: three drawers with ghost handles."""
    drawers = VGroup(*[RoundedRectangle(width=w, height=0.72, corner_radius=0.1,
                                        fill_color=DARK_TOP, fill_opacity=1,
                                        stroke_color=INK, stroke_width=3).move_to(
                                            [cx, cy + 0.76 - i * 0.8, 0])
                        for i in range(3)])
    handles = VGroup(*[RoundedRectangle(width=0.7, height=0.12, corner_radius=0.06,
                                        fill_color=GHOST, fill_opacity=1,
                                        stroke_width=0).move_to(
                                            [cx, cy + 0.76 - i * 0.8, 0])
                        for i in range(3)])
    return VGroup(drawers, handles)


def cable(a, b):
    return Line(a, b, color=KRAFT_CABLE, stroke_width=5)


# ============ scenes ============

class B00_TheNotebook(Scene):
    """What memory is: the spoken fact becomes a card; the notebook feeds a new chat."""

    def construct(self):
        sh = floor_shadow(-0.2, w=11.0)
        win1 = chat_window(-3.2, 0.4, 4.4, 3.4)
        nb = notebook_open(3.0, -0.6)
        lab_mem = lab("memory", 3.0, 1.85)
        self.play(FadeIn(sh), FadeIn(win1), FadeIn(nb), FadeIn(lab_mem), run_time=1.0)
        until(self, "Mention your café's move to Lisbon")
        bub = bubble(["moving my café", "to Lisbon"], -3.2, 1.05, w=3.2)
        card = note_card(["café in Lisbon"], 3.0, -0.15, w=3.0)
        self.play(FadeIn(bub), run_time=0.6)
        self.play(FadeIn(card), run_time=0.6)
        until(self, "Open a new chat next week")
        win2 = chat_window(-3.2, 0.4, 4.4, 3.4)
        lab_new = lab("new chat", -3.2, 2.55)
        cb = cable(np.array([1.2, -0.4, 0]), np.array([-1.0, -0.4, 0]))
        self.play(FadeOut(win1), FadeOut(bub), run_time=0.5)
        self.play(FadeIn(win2), FadeIn(lab_new), Create(cb), run_time=0.8)
        finish(self)


class B01_KeepWorthy(Scene):
    """What belongs on the notes: three recurring kinds, and the keeper test."""

    def construct(self):
        sh = floor_shadow(0, w=7.0)
        nb = notebook_open(0, -0.6, w=3.8)
        lab_mem = lab("memory", 0, 1.85)
        self.play(FadeIn(sh), FadeIn(nb), FadeIn(lab_mem), run_time=1.0)
        until(self, "What you're working on")
        c1 = note_card(["café in Lisbon"], 0, -0.15, w=3.0)
        self.play(FadeIn(c1), run_time=0.6)
        until(self, "How you like things done")
        c2 = note_card(["bullet points"], 0, -0.75, w=2.6)
        self.play(FadeIn(c2), run_time=0.6)
        until(self, "the details that keep coming up")
        c3 = note_card(["Ana: short updates"], 0, -1.35, w=3.1)
        self.play(FadeIn(c3), run_time=0.6)
        until(self, "The test:")
        ck = check(2.75, 1.1, s=0.22)
        lab_test = lab("the test", 4.3, 1.1)
        self.play(FadeIn(ck), FadeIn(lab_test), run_time=0.6)
        finish(self)


class B02_NeverIn(Scene):
    """What never goes in: secrets crossed out; sensitive topics guarded by defaults."""

    def construct(self):
        sh = floor_shadow(-0.6, w=11.0)
        nb = notebook_open(1.8, -0.7, w=3.4)
        lab_mem = lab("memory", 1.8, 1.75)
        self.play(FadeIn(sh), FadeIn(nb), FadeIn(lab_mem), run_time=1.0)
        until(self, "Passwords, card numbers, door codes")
        c1 = note_card(["passwords"], 1.8, -0.25, w=2.6)
        c2 = note_card(["card numbers"], 1.8, -0.85, w=2.9)
        c3 = note_card(["door codes"], 1.8, -1.45, w=2.6)
        self.play(FadeIn(c1), FadeIn(c2), FadeIn(c3), run_time=0.8)
        until(self, "And the sensitive stuff")
        x1 = xmark(1.8, -0.25); x2 = xmark(1.8, -0.85); x3 = xmark(1.8, -1.45)
        self.play(FadeIn(x1), FadeIn(x2), FadeIn(x3), run_time=0.7)
        until(self, "Claude leaves those out")
        p1 = kw_pill("health · beliefs · politics", -3.3, 0.9, w=5.4)
        lab_off = lab("off by default", -3.3, 0.1)
        self.play(FadeIn(p1), FadeIn(lab_off), run_time=0.7)
        until(self, "Even then, some things are never saved")
        p2 = kw_pill("never stored: ID numbers", -3.3, -1.0, w=5.4)
        lab_opt = lab("even with opt-in", -3.3, -1.8)
        self.play(FadeIn(p2), FadeIn(lab_opt), run_time=0.7)
        finish(self)


class B03_WhereItLives(Scene):
    """Where the notebook lives: Settings, then Memory, then Topics."""

    def construct(self):
        sh = floor_shadow(-0.6, w=11.0)
        panel = settings_panel(-2.8, 0.0, w=4.4, h=3.6)
        lab_set = lab("settings", -2.8, 2.3)
        self.play(FadeIn(sh), FadeIn(panel), FadeIn(lab_set), run_time=1.0)
        until(self, "Settings, then Memory, then Topics")
        p1 = kw_pill("Settings", -2.8, 1.0, w=2.6)
        p2 = kw_pill("Memory", -2.8, 0.05, w=2.6)
        p3 = kw_pill("Topics", -2.8, -0.9, w=2.6)
        self.play(FadeIn(p1), FadeIn(p2), FadeIn(p3), run_time=0.8)
        until(self, "The whole list")
        cur = cursor(-1.15, -0.55)
        nb = notebook_open(3.2, -0.6, w=3.2)
        card1 = note_card(["café in Lisbon"], 3.2, -0.15, w=2.8)
        card2 = note_card(["bullet points"], 3.2, -0.75, w=2.6)
        lab_mem = lab("memory", 3.2, 1.85)
        self.play(FadeIn(cur), FadeIn(nb), FadeIn(card1), FadeIn(card2),
                  FadeIn(lab_mem), run_time=0.9)
        finish(self)


class B04_FixOne(Scene):
    """Fix one note, delete the stale one."""

    def construct(self):
        sh = floor_shadow(0, w=7.0)
        nb = notebook_open(0, -0.6, w=3.8)
        lab_mem = lab("memory", 0, 1.85)
        card_off = note_card(["old office"], 0, -0.15, w=2.6)
        card_menu = note_card(["old menu"], 0, -0.85, w=2.6)
        self.play(FadeIn(sh), FadeIn(nb), FadeIn(lab_mem),
                  FadeIn(card_off), FadeIn(card_menu), run_time=1.0)
        until(self, "Lift the card, rewrite the line")
        pen = pencil(2.2, 0.9)
        card_new = note_card(["new office"], 0, 1.0, w=2.6)
        self.play(FadeIn(pen), FadeOut(card_off), FadeIn(card_new), run_time=0.8)
        until(self, "set it back")
        ck = check(2.2, -0.15, s=0.22)
        lab_fixed = lab("fixed", 3.35, -0.15)
        path = Line(np.array([0, 1.0, 0]), np.array([0, -0.15, 0]))
        self.play(MoveAlongPath(card_new, path),
                  FadeIn(ck), FadeIn(lab_fixed), run_time=0.8)
        until(self, "And the stale one? Delete it")
        xm = xmark(0, -0.85)
        self.play(FadeIn(xm), FadeOut(card_menu), run_time=0.7)
        finish(self)


class B05_TwoLevers(Scene):
    """The two big levers: Pause shelves the notebook; Reset empties it."""

    def construct(self):
        sh = floor_shadow(0, w=11.0)
        nb = notebook_open(0, -0.6, w=3.8)
        lab_mem = lab("memory", 0, 1.85)
        c1 = note_card(["café in Lisbon"], 0, -0.15, w=3.0)
        c2 = note_card(["bullet points"], 0, -0.75, w=2.6)
        p_pause = kw_pill("Pause", -3.6, 1.6, w=2.2)
        p_reset = kw_pill("Reset", 3.6, 1.6, w=2.2)
        self.play(FadeIn(sh), FadeIn(nb), FadeIn(lab_mem), FadeIn(c1), FadeIn(c2),
                  FadeIn(p_pause), FadeIn(p_reset), run_time=1.0)
        until(self, "Pause: the notebook stays on the shelf")
        cur = cursor(-2.3, 1.6)
        shelf = Line(np.array([-1.9, -2.35, 0]), np.array([1.9, -2.35, 0]),
                     color=KRAFT_CABLE, stroke_width=5)
        lab_shelf = lab("on the shelf", 0, -2.85)
        self.play(FadeIn(cur), FadeIn(shelf), FadeIn(lab_shelf), run_time=0.8)
        until(self, "Reset: the notebook empties")
        cur2 = cursor(4.9, 1.6)
        lab_gone = lab("gone — for good", 0, 1.0)
        self.play(FadeOut(cur), FadeIn(cur2), FadeOut(c1), FadeOut(c2),
                  FadeIn(lab_gone), run_time=0.9)
        until(self, "pause to take a break")
        cur3 = cursor(-2.3, 1.6)
        lab_safer = lab("the safer lever", -3.6, 0.75)
        self.play(FadeOut(cur2), FadeIn(cur3), FadeIn(lab_safer), run_time=0.7)
        finish(self)


class B06_Incognito(Scene):
    """Incognito: the chat that leaves no trace in memory."""

    def construct(self):
        sh = floor_shadow(-0.2, w=11.0)
        win = chat_window(-2.9, 0.3, 4.4, 3.2)
        inc = RoundedRectangle(width=2.8, height=0.5, corner_radius=0.25,
                             fill_color="#FFFFFF", fill_opacity=1,
                             stroke_width=0).move_to([-2.9, 1.63, 0])
        inc_t = T("incognito", size=32).move_to([-2.9, 1.61, 0])
        inc = VGroup(inc, inc_t)
        nb = notebook_closed(3.0, -1.0)
        lab_mem = lab("memory", 3.0, 0.5)
        lab_not = lab("not read, not written", 3.0, -2.45)
        self.play(FadeIn(sh), FadeIn(win), FadeIn(inc), FadeIn(nb),
                  FadeIn(lab_mem), FadeIn(lab_not), run_time=1.0)
        until(self, "The gift you're price-checking")
        bub = bubble(["a gift for Ana?"], -2.9, 0.6, w=3.0)
        self.play(FadeIn(bub), run_time=0.6)
        until(self, "Ask it, close it, gone")
        card = note_card(["a gift for Ana?"], -2.9, -0.7, w=3.0)
        self.play(FadeIn(card), run_time=0.6)
        xm = xmark(0.2, -0.7)
        self.play(FadeIn(xm), FadeOut(card), run_time=0.7)
        finish(self)


class B07_ChatDelete(Scene):
    """Memory is not the chat: delete the chat, the note stays."""

    def construct(self):
        sh = floor_shadow(-0.2, w=11.0)
        win = chat_window(-3.1, 0.3, 4.4, 3.2)
        lab_chat = lab("the chat", -3.1, 2.35)
        bub = bubble(["my deadline is Friday"], -3.1, 0.6, w=3.6)
        nb = notebook_open(3.1, -0.6, w=3.2)
        card = note_card(["deadline: Friday"], 3.1, -0.15, w=3.0)
        lab_nb = lab("the notebook", 3.1, 1.85)
        self.play(FadeIn(sh), FadeIn(win), FadeIn(lab_chat), FadeIn(bub),
                  FadeIn(nb), FadeIn(card), FadeIn(lab_nb), run_time=1.0)
        until(self, "Trash the chat all you want")
        xm = xmark(-3.1, 0.3, s=0.5, w=10)
        self.play(FadeIn(xm), run_time=0.5)
        self.play(FadeOut(win), FadeOut(bub), FadeOut(xm), FadeOut(lab_chat),
                  run_time=0.6)
        until(self, "the note stays")
        ck = check(4.95, -0.15, s=0.22)
        lab_stays = lab("stays", 5.75, -0.15)
        self.play(FadeIn(ck), FadeIn(lab_stays), run_time=0.6)
        finish(self)


class B08_NotArchive(Scene):
    """Memory is not the archive: two doors into the past, two switches."""

    def construct(self):
        sh = floor_shadow(0, w=11.0)
        nb = notebook_open(-3.4, -0.9, w=3.2)
        card = note_card(["café in Lisbon"], -3.4, -0.45, w=2.8)
        lab_mem = lab("memory", -3.4, 0.95)
        arc = archive_cabinet(3.4, -0.9)
        lab_arc = lab("archive", 3.4, 0.95)
        win = chat_window(0, 1.9, 3.2, 1.9)
        lab_new = lab("new chat", 0, 3.05)
        self.play(FadeIn(sh), FadeIn(nb), FadeIn(card), FadeIn(lab_mem),
                  FadeIn(arc), FadeIn(lab_arc), FadeIn(win), FadeIn(lab_new),
                  run_time=1.0)
        until(self, "The notes get loaded into new chats automatically")
        cb = cable(np.array([-1.8, -0.2, 0]), np.array([-1.6, 1.0, 0]))
        self.play(Create(cb), run_time=0.7)
        until(self, "the archive you search")
        cur = cursor(2.3, 0.35)
        lab_search = lab("search it yourself", 3.4, -2.5)
        self.play(FadeIn(cur), FadeIn(lab_search), run_time=0.7)
        until(self, "you can close either one")
        p_mem = kw_pill("memory: on", -3.4, -2.5, w=2.8)
        p_arc = kw_pill("archive: on", 3.4, -2.5, w=2.8)
        self.play(FadeOut(cur), FadeOut(lab_search), FadeIn(p_mem), FadeIn(p_arc),
                  run_time=0.7)
        finish(self)
