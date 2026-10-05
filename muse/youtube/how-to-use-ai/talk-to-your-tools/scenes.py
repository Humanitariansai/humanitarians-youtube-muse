"""scenes.py — show-tell: Talk to your tools (Liam, Teardown, claude-liam).

Nine drawn body beats, one Manim scene per beat. The iso_kit block is pasted
verbatim at the top (Gate A copies only this file — never import the kit).
Film helpers (chat window, doc cards, labels, transcript page, fragments,
bullets, owner pills, email card, lock) follow the kit; every scene class is
written literally as `class BNN_Name(Scene):`.

Drawing laws obeyed: labels sit beside objects (never inside, never on
terracotta); terracotta only for dots/checks; chart blocks not used; type >=
32; every coordinate inside +-6.2 x +-3.3; every scene adds a new non-text
shape after its first frame; no path_arc, no ease_in_quad/ease_out_cubic; no
MoveAlongPath + .animate on the same object in one play; major motion is kept
off the clip midpoint via until() phrase timing (see SHOTLIST.md).

Pacing: until()/finish() read beat_sheet.json beside this file (the measured
Kokoro audio at render time); with no sheet they degrade to short waits.
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


# ═════════════════════════════ shared helpers (chat window, doc cards, labels, email card, lock) ═════════════════════════════
def chat_window(cx=0.0, cy=0.0, w=5.2, h=3.1, composer=True, wide_composer=False):
    """Front-facing Claude chat window: ink-outlined cream card, thin dark title
    strip (carries contrast on the pale panel), composer pill at the bottom."""
    body = RoundedRectangle(width=w, height=h, corner_radius=0.18, fill_color=CARD,
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([cx, cy, 0])
    bar = RoundedRectangle(width=w - 0.04, height=0.5, corner_radius=0.15, fill_color=DARK_TOP,
                           fill_opacity=1, stroke_width=0).move_to([cx, cy + h / 2 - 0.26, 0])
    parts = [body, bar]
    if composer:
        cw = w * (0.86 if wide_composer else 0.8)
        comp = RoundedRectangle(width=cw, height=0.58, corner_radius=0.29, fill_color="#FFFFFF",
                                fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([cx, cy - h / 2 + 0.6, 0])
        parts.append(comp)
    return VGroup(*parts)


def doc_card(x, y, w=1.5, h=1.9, outline=DIM, dot=True, lines=3):
    """Small flat document card. Grey outline so it stays legible inside
    ink-outlined containers (GATE T: ink-in-ink reads as overlapping text)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=outline, stroke_width=2).move_to([x, y, 0])
    ls = VGroup(*[Line([x - w / 2 + 0.24, y + h / 2 - 0.42 - i * 0.36, 0],
                       [x + w / 2 - 0.24 - (0.35 if i == lines - 1 else 0), y + h / 2 - 0.42 - i * 0.36, 0],
                       color=GHOST, stroke_width=4) for i in range(lines)])
    parts = [card, ls]
    if dot:
        parts.append(Dot([x - w / 2 + 0.3, y + h / 2 - 0.24, 0], radius=0.06, color=TERRA))
    return VGroup(*parts)


def tag(text, lx, ly, ox, oy, size=36):
    """Ink label at (lx, ly) with a dim leader line from object point (ox, oy).
    The leader stops 0.35 units short of the label (GATE T: a touching leader fails)."""
    lab = T(text, size=size).move_to([lx, ly, 0])
    half = lab.width / 2 + 0.35
    d = np.array([lx - ox, ly - oy, 0.0])
    n = np.linalg.norm(d)
    d = d / n if n > 1e-6 else np.array([1.0, 0.0, 0.0])
    end = np.array([lx, ly, 0.0]) - d * half
    line = Line([ox, oy, 0], end, color=DIM, stroke_width=2)
    return VGroup(line, lab)


def transcript_page(x, y, w=2.6, h=3.4):
    """The film's messy transcript: white card, uneven ghost text lines
    (the ramble), one terracotta dot. Grey outline keeps it legible."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    fracs = [0.9, 0.55, 1.0, 0.7, 0.45, 0.95, 0.6, 0.85]
    ls = VGroup(*[Line([x - w / 2 + 0.24, y + h / 2 - 0.55 - i * 0.36, 0],
                       [x - w / 2 + 0.24 + (w - 0.7) * f, y + h / 2 - 0.55 - i * 0.36, 0],
                       color=GHOST, stroke_width=4) for i, f in enumerate(fracs)])
    dot = Dot([x - w / 2 + 0.3, y + h / 2 - 0.3, 0], radius=0.06, color=TERRA)
    return VGroup(card, ls, dot)


def scribbles(x, y):
    """Jagged ink polylines across the transcript (straight segments only —
    no curves, so the layout audit's --curve-strict stays quiet)."""
    paths = [
        [(-1.1, -0.9), (-0.6, -0.7), (-0.9, -0.4), (-0.3, -0.5)],
        [(-0.7, 0.2), (-0.2, 0.4), (-0.5, 0.7), (0.1, 0.6)],
        [(-1.0, 1.0), (-0.4, 1.2), (-0.7, 1.45)],
    ]
    return VGroup(*[VMobject().set_points_as_corners(
        [np.array([x + dx, y + dy, 0]) for dx, dy in p]).set_stroke(INK, width=3)
        for p in paths])


def bubble(x, y, text):
    """Small ink-outlined speech bubble with one short word."""
    lab = T(text, size=32).move_to([x, y - 0.02, 0])
    bg = RoundedRectangle(width=lab.width + 0.5, height=0.55, corner_radius=0.27,
                          fill_color="#FFFFFF", fill_opacity=1,
                          stroke_color=INK, stroke_width=2).move_to([x, y, 0])
    return VGroup(bg, lab)


def fragment_card(x, y, text, w=2.3):
    """A rough-notes fragment: white card with one short unfinished line."""
    card = RoundedRectangle(width=w, height=0.62, corner_radius=0.12, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    lab = T(text, size=32).move_to([x, y - 0.02, 0])
    return VGroup(card, lab)


def owner_pill(x, y, name):
    """Owner tag: ink-outlined pill with a name."""
    lab = T(name, size=32).move_to([x, y - 0.02, 0])
    bg = RoundedRectangle(width=lab.width + 0.5, height=0.5, corner_radius=0.25,
                          fill_color="#FFFFFF", fill_opacity=1,
                          stroke_color=INK, stroke_width=2).move_to([x, y, 0])
    return VGroup(bg, lab)


def email_card(x, y, w=2.2, h=1.6):
    """A follow-up email: white card with an ink envelope glyph."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    env = RoundedRectangle(width=w * 0.62, height=h * 0.5, corner_radius=0.06, fill_color=CARD,
                           fill_opacity=1, stroke_color=INK, stroke_width=2.5).move_to([x, y, 0])
    flap = VGroup(Line([x - w * 0.31, y + h * 0.25, 0], [x, y, 0], color=INK, stroke_width=2.5),
                  Line([x, y, 0], [x + w * 0.31, y + h * 0.25, 0], color=INK, stroke_width=2.5))
    return VGroup(card, env, flap)


def lock(x, y, s=1.0):
    """A padlock, drawn large with ink outlines (GATE T: tiny icons read as text)."""
    body = RoundedRectangle(width=0.9 * s, height=0.7 * s, corner_radius=0.1, fill_color=CARD,
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y - 0.1 * s, 0])
    shackle = Arc(radius=0.3 * s, angle=PI, arc_center=[x, y + 0.25 * s, 0],
                  stroke_color=INK, stroke_width=4)
    hole = Dot([x, y - 0.05 * s, 0], radius=0.07 * s, color=INK)
    return VGroup(shackle, body, hole)


# ═════════════════════════════ film helpers (talk-to-your-tools) ═════════════════════════════
DEEP_KRAFT = "#9C8462"  # connector cables: ink-edged cables fuse with dark blocks under GATE T


def calendar_card(x, y, w=1.9, h=1.7):
    """A small calendar: white card, grey band on top, 3x2 ghost date grid, one terracotta dot."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    band = RoundedRectangle(width=w - 0.06, height=0.34, corner_radius=0.08, fill_color=BAR1,
                            fill_opacity=1, stroke_width=0).move_to([x, y + h / 2 - 0.19, 0])
    cells = VGroup(*[RoundedRectangle(width=0.42, height=0.32, corner_radius=0.05,
                                      fill_color=CARD, fill_opacity=1, stroke_color=GHOST, stroke_width=2)
                     .move_to([x - 0.5 + c * 0.5, y - 0.15 - r * 0.42, 0])
                     for r in range(2) for c in range(3)])
    dot = Dot([x - 0.5 + 2 * 0.5, y - 0.15 - 0.42, 0], radius=0.06, color=TERRA)
    return VGroup(card, band, cells, dot)


def cable(x1, y1, x2, y2):
    """A connector cable: deep kraft, 6pt (GATE T: ink-edged cables fuse with dark blocks)."""
    return Line([x1, y1, 0], [x2, y2, 0], color=DEEP_KRAFT, stroke_width=6)


def plug_head(x, y, s=1.0, flip=False):
    """A plug: ink body, two kraft prongs. Prongs point +x unless flip (then -x)."""
    d = -1 if flip else 1
    body = RoundedRectangle(width=0.5 * s, height=0.7 * s, corner_radius=0.1 * s,
                            fill_color=INK, fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    prongs = VGroup(*[Line([x + d * 0.25 * s, y + (0.15 if i == 0 else -0.15) * s, 0],
                           [x + d * 0.62 * s, y + (0.15 if i == 0 else -0.15) * s, 0],
                           color=DEEP_KRAFT, stroke_width=5) for i in range(2)])
    return VGroup(body, prongs)


def socket_slot(x, y, s=1.0):
    """A dark socket slot straddling an app card's edge."""
    return RoundedRectangle(width=0.34 * s, height=0.8 * s, corner_radius=0.08,
                            fill_color=DARK_TOP, fill_opacity=1, stroke_width=0).move_to([x, y, 0])


def shield(x, y, s=1.0):
    """A sign-in shield: ink outline, no fill (the check is added separately)."""
    pts = [(0, 0.55), (0.42, 0.32), (0.42, -0.15), (0, -0.5), (-0.42, -0.15), (-0.42, 0.32)]
    return Polygon(*[[x + px * s, y + py * s, 0] for px, py in pts],
                   fill_opacity=0, stroke_color=INK, stroke_width=4)


def perm_row(x, y, text, w=4.2):
    """A permission row: white card, grey outline, short ink label left-aligned."""
    card = RoundedRectangle(width=w, height=0.62, corner_radius=0.12, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    lab = T(text, size=32)
    lab.move_to([x - w / 2 + 0.3 + lab.width / 2, y - 0.02, 0])
    return VGroup(card, lab)


def send_pill(x, y, w=2.2):
    """The send button: big ink pill, cream SEND."""
    bg = RoundedRectangle(width=w, height=0.8, corner_radius=0.4, fill_color=INK,
                          fill_opacity=1, stroke_width=0).move_to([x, y, 0])
    lab = T("SEND", size=36, color=STAGE, bold=True).move_to([x, y - 0.02, 0])
    return VGroup(bg, lab)


def tray(x, y, w=2.4, h=1.3):
    """An open tray for the pulled plug: ink outline, light kraft fill."""
    return RoundedRectangle(width=w, height=h, corner_radius=0.15, fill_color="#E8E2D4",
                            fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([x, y, 0])


def invite_card(x, y, w=3.2, h=2.1):
    """A calendar invite from a stranger: grey band, 'from: stranger', ink '?'."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    band = RoundedRectangle(width=w - 0.06, height=0.4, corner_radius=0.08, fill_color=BAR1,
                            fill_opacity=1, stroke_width=0).move_to([x, y + h / 2 - 0.22, 0])
    frm = T("from: stranger", size=32).move_to([x, y + 0.35, 0])
    q = T("?", size=64).move_to([x, y - 0.45, 0])
    return VGroup(card, band, frm, q)


def inbox_card(x, y, w=3.6, h=2.3):
    """An inbox: white card with mixed ink/ghost rows (the pile)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    rows = VGroup(*[Line([x - w / 2 + 0.3, y + h / 2 - 0.5 - i * 0.4, 0],
                         [x - w / 2 + 0.3 + (w - 0.9) * (0.9 if i % 2 == 0 else 0.55),
                          y + h / 2 - 0.5 - i * 0.4, 0],
                         color=INK if i < 2 else GHOST, stroke_width=5) for i in range(4)])
    return VGroup(card, rows)


def x_stamp(x, y, s=0.5):
    """An ink X stamp (rejections are ink, never terracotta)."""
    return VGroup(Line([x - s, y + s, 0], [x + s, y - s, 0], color=INK, stroke_width=7),
                  Line([x - s, y - s, 0], [x + s, y + s, 0], color=INK, stroke_width=7))


# ═════════════════════════════ scenes ═════════════════════════════
class B00_TheGap(Scene):
    """The pain: the chat window and the apps sit apart; you copy fragments
    over by hand; then a cable draws across the gap (the fix arrives)."""

    def construct(self):
        win = chat_window(-3.3, 0.2, w=4.4, h=2.9)
        email = email_card(2.4, 1.1, w=2.0, h=1.5)
        cal = calendar_card(4.7, -0.7)
        lab = tag("the gap", -0.2, 2.35, -1.1, 1.5)
        self.play(FadeIn(win), FadeIn(email), FadeIn(cal), FadeIn(lab), run_time=1.0)
        until(self, "paste the email")
        frag1 = fragment_card(2.4, 1.1, "bill due Friday")
        frag2 = fragment_card(4.7, -0.7, "invite: Tue 3pm")
        self.play(frag1.animate.scale(0.45).move_to([-3.3, -0.5, 0]),
                  frag2.animate.scale(0.45).move_to([-3.3, -0.82, 0]), run_time=1.2)
        until(self, "Connectors end the copying")
        cb = cable(-1.1, 0.2, 1.4, 0.6)
        spark = Dot([1.4, 0.6, 0], radius=0.07, color=TERRA)
        self.play(Create(cb), FadeIn(spark), run_time=1.0)
        finish(self)


class B01_ThePlug(Scene):
    """The fix: the plug slides into the socket on the email app card; the
    sign-in shield pops — the app asks you to sign in, not Claude."""

    def construct(self):
        win = chat_window(-3.6, 0.0, w=4.0, h=2.7)
        app = email_card(2.8, 0.0, w=2.4, h=1.9)
        sock = socket_slot(1.6, 0.0)
        plug = VGroup(cable(-1.6, 0.0, -0.05, 0.0), plug_head(0.2, 0.0))
        lab = tag("the plug", 2.8, 2.05, 2.8, 0.95)
        self.play(FadeIn(win), FadeIn(app), FadeIn(sock), FadeIn(plug), FadeIn(lab), run_time=1.0)
        until(self, "click connect")
        self.play(plug.animate.shift(RIGHT * 0.9), run_time=0.9)
        until(self, "You never type your password into Claude")
        sh = shield(3.5, 0.6, s=0.75)
        tick = check(3.5, 0.58, s=0.14, color=INK, w=6)
        self.play(GrowFromCenter(sh), FadeIn(tick), run_time=0.8)
        finish(self)


class B02_Permissions(Scene):
    """The screen that matters: the two read rows land with terracotta
    checks; the send row lands with an ink X — read is looking, send is acting."""

    def construct(self):
        panel = RoundedRectangle(width=5.0, height=2.9, corner_radius=0.15, fill_color=CARD,
                                 fill_opacity=1, stroke_color=INK, stroke_width=4).move_to([0, 0, 0])
        lab = tag("permissions", -3.4, 2.25, -2.5, 1.45)
        self.play(FadeIn(panel), FadeIn(lab), run_time=1.0)
        until(self, "read your email")
        r1 = perm_row(0, 0.85, "read email")
        r2 = perm_row(0, 0.05, "read calendar")
        c1 = check(1.6, 0.85, s=0.14, color=TERRA, w=6)
        c2 = check(1.6, 0.05, s=0.14, color=TERRA, w=6)
        self.play(FadeIn(r1), FadeIn(c1), FadeIn(r2), FadeIn(c2), run_time=0.9)
        until(self, "sending is acting")
        r3 = perm_row(0, -0.75, "send email")
        xs = x_stamp(1.6, -0.75, s=0.22)
        self.play(FadeIn(r3), FadeIn(xs), run_time=0.7)
        finish(self)


class B03_MorningBrief(Scene):
    """Automation 1: kraft lines draw from the calendar and the email card to
    a brief card that grows with three lines; terracotta dots land."""

    def construct(self):
        cal = calendar_card(-4.0, 0.9)
        email = email_card(-4.0, -1.2, w=1.9, h=1.4)
        lab = tag("morning brief", 1.6, 2.3, 1.6, 1.35)
        self.play(FadeIn(cal), FadeIn(email), FadeIn(lab), run_time=1.0)
        until(self, "Claude reads your calendar")
        k1 = cable(-3.05, 0.9, -0.1, 0.75)
        k2 = cable(-3.05, -1.2, -0.1, -0.45)
        card = RoundedRectangle(width=3.4, height=2.7, corner_radius=0.1, fill_color="#FFFFFF",
                                fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([1.6, 0, 0])
        lines = VGroup(*[Line([0.35, 0.75 - i * 0.6, 0], [2.95, 0.75 - i * 0.6, 0],
                               color=INK, stroke_width=5) for i in range(3)])
        self.play(Create(k1), Create(k2), GrowFromCenter(VGroup(card, lines)), run_time=1.0)
        until(self, "what can wait")
        dots = VGroup(*[Dot([0.12, 0.75 - i * 0.6, 0], radius=0.07, color=TERRA) for i in range(3)])
        self.play(FadeIn(dots), run_time=0.6)
        finish(self)


class B04_InboxTriage(Scene):
    """Automation 2: the inbox card splits into two stacks — 'needs you'
    (ink) and 'noise' (dim); a terracotta check lands on what matters."""

    def construct(self):
        inbox = inbox_card(0, 0.2)
        lab = tag("triage", -4.6, 1.95, -4.0, 0.8)
        self.play(FadeIn(inbox), FadeIn(lab), run_time=1.0)
        until(self, "what actually needs me", lead=0.5)
        s1 = RoundedRectangle(width=2.6, height=2.0, corner_radius=0.1, fill_color="#FFFFFF",
                              fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([-3.1, -0.2, 0])
        l1 = VGroup(*[Line([-4.1, 0.35 - i * 0.4, 0], [-2.3, 0.35 - i * 0.4, 0],
                            color=INK, stroke_width=5) for i in range(3)])
        lab1 = T("needs you", size=32).move_to([-3.1, 1.15, 0])
        s2 = RoundedRectangle(width=2.6, height=2.0, corner_radius=0.1, fill_color="#FFFFFF",
                              fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([3.1, -0.2, 0])
        l2 = VGroup(*[Line([2.1, 0.35 - i * 0.32, 0], [4.1 - (0.5 if i == 4 else 0), 0.35 - i * 0.32, 0],
                            color=GHOST, stroke_width=5) for i in range(5)])
        lab2 = T("noise", size=32).move_to([3.1, 1.15, 0])
        self.play(FadeIn(s1), FadeIn(l1), FadeIn(lab1), FadeIn(s2), FadeIn(l2), FadeIn(lab2),
                  FadeOut(inbox), run_time=1.0)
        until(self, "You read what matters")
        tick = check(-2.0, 0.55, s=0.15, color=TERRA, w=6)
        self.play(FadeIn(tick), run_time=0.6)
        finish(self)


class B05_MeetingPrep(Scene):
    """Automation 3 (companion to the meetings film): kraft lines draw from
    the invite and the thread; the prep card grows with a paragraph; a dot lands."""

    def construct(self):
        cal = calendar_card(-4.0, 0.9)
        email = email_card(-4.0, -1.2, w=1.9, h=1.4)
        lab = tag("meeting prep", 1.6, 2.3, 1.6, 1.2)
        self.play(FadeIn(cal), FadeIn(email), FadeIn(lab), run_time=1.0)
        until(self, "Before a call")
        k1 = cable(-3.05, 0.9, -0.1, 0.6)
        k2 = cable(-3.05, -1.2, -0.1, -0.4)
        self.play(Create(k1), Create(k2), run_time=0.8)
        until(self, "hands you a one-paragraph brief")
        card = RoundedRectangle(width=3.4, height=2.4, corner_radius=0.1, fill_color="#FFFFFF",
                                fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([1.6, 0, 0])
        lines = VGroup(*[Line([0.35, 0.6 - i * 0.4, 0], [2.95 - (0.6 if i == 3 else 0), 0.6 - i * 0.4, 0],
                               color=GHOST, stroke_width=5) for i in range(4)])
        self.play(GrowFromCenter(VGroup(card, lines)), run_time=1.0)
        until(self, "You walk in already knowing the room")
        dot = Dot([0.12, 0.6, 0], radius=0.07, color=TERRA)
        self.play(FadeIn(dot), run_time=0.5)
        finish(self)


class B06_YouSend(Scene):
    """Warning 1: the draft card grows; the ink SEND pill lands; an ink lock
    lands over the pill — the send button stays yours."""

    def construct(self):
        draft = doc_card(0, 0.5, w=3.4, h=2.0, lines=4)
        lab = tag("you send", -3.4, 2.05, -1.7, 1.4)
        self.play(FadeIn(draft), FadeIn(lab), run_time=1.0)
        until(self, "So let it write every draft it wants")
        send = send_pill(0, -1.55)
        self.play(FadeIn(send), run_time=0.8)
        until(self, "nothing leaves your outbox")
        lk = lock(0, -1.55, s=0.9)
        self.play(FadeIn(lk), run_time=0.7)
        finish(self)


class B07_PullThePlug(Scene):
    """Warning 2: the plug slides out of the socket along its cable and lands
    in the tray; a check stamps the tray — take keys back."""

    def construct(self):
        app = email_card(-2.2, 0.2, w=2.4, h=1.9)
        sock = socket_slot(-1.0, 0.2)
        plug = VGroup(plug_head(-0.35, 0.2, flip=True), cable(-0.1, 0.2, 2.0, 0.2))
        tr = tray(3.4, -0.9)
        lab = tag("pull the plug", -2.2, 2.2, -2.2, 1.15)
        self.play(FadeIn(app), FadeIn(sock), FadeIn(plug), FadeIn(tr), FadeIn(lab), run_time=1.0)
        until(self, "pull the plugs you don't use anymore")
        self.play(plug.animate.shift(RIGHT * 3.75 + DOWN * 1.1), run_time=1.0)
        until(self, "An unused connection is an unlocked door")
        tick = check(4.2, -0.5, s=0.16, color=TERRA, w=6)
        self.play(FadeIn(tick), run_time=0.6)
        finish(self)


class B08_StrangerInvite(Scene):
    """Warning 3: the stranger's invite drops in; an ink X stamps it; the card
    slides off stage — don't accept it, don't ask about it, delete it."""

    def construct(self):
        inv = invite_card(0, 0.2)
        lab = tag("strangers' invites", 3.7, 1.95, 1.6, 1.25)
        self.play(FadeIn(inv), FadeIn(lab), run_time=1.0)
        until(self, "Don't accept it")
        xs = x_stamp(0, 0.2, s=0.9)
        self.play(FadeIn(xs), run_time=0.6)
        until(self, "Delete it")
        self.play(inv.animate.shift(DOWN * 2.5), xs.animate.shift(DOWN * 2.5), run_time=0.6)
        self.play(FadeOut(inv), FadeOut(xs), run_time=0.4)
        finish(self)
