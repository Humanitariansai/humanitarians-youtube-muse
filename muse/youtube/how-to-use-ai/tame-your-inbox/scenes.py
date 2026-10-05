"""scenes.py — show-tell: Tame your inbox (Liam, Teardown, claude-liam).

Six drawn body beats, one Manim scene per beat. The iso_kit block is pasted
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


# ═════════════════════════════ film helpers (tame-your-inbox) ═════════════════════════════
def pile_card(x, y, w=2.0, h=1.15):
    """One email in the pile: white card, grey outline, two ghost subject lines."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.08, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    ls = VGroup(*[Line([x - w / 2 + 0.22, y + 0.22 - i * 0.34, 0],
                       [x - w / 2 + 0.22 + (w - 0.7) * (0.95 if i == 0 else 0.6), y + 0.22 - i * 0.34, 0],
                       color=GHOST, stroke_width=4) for i in range(2)])
    return VGroup(card, ls)


def scan_line(x1, x2, y, w=4):
    """Terracotta scan line (reads are terracotta; rejections are ink)."""
    return Line([x1, y, 0], [x2, y, 0], color=TERRA, stroke_width=w)


def stack_card(x, y, w=2.4, h=2.0, ink_lines=3, dim_lines=0):
    """A sorted stack: white card with ink lines (needs you) or dim lines (noise)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    parts = [card]
    n = ink_lines + dim_lines
    for i in range(n):
        col = INK if i < ink_lines else GHOST
        frac = 0.9 if i % 2 == 0 else 0.6
        parts.append(Line([x - w / 2 + 0.28, y + h / 2 - 0.5 - i * 0.42, 0],
                          [x - w / 2 + 0.28 + (w - 0.8) * frac, y + h / 2 - 0.5 - i * 0.42, 0],
                          color=col, stroke_width=5))
    return VGroup(*parts)


def thread_stack(x, y, n=5):
    """A long thread: pages stacked tall with slight offsets."""
    cards = [doc_card(x + (0.06 if i % 2 == 0 else -0.06), y - 0.8 + i * 0.4,
                      w=2.0, h=0.95, lines=2) for i in range(n)]
    return VGroup(*cards)


def brief_card(x, y, w=3.4, h=2.7, nlines=3):
    """The three-line brief: white card with ink lines."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    lines = VGroup(*[Line([x - w / 2 + 0.3, y + h / 2 - 0.6 - i * 0.6, 0],
                          [x + w / 2 - 0.3, y + h / 2 - 0.6 - i * 0.6, 0],
                          color=INK, stroke_width=5) for i in range(nlines)])
    return VGroup(card, lines)


def draft_card(x, y, w=3.0, h=2.2):
    """The AI's draft: white card with ghost reply lines (it's guessing, so ghost)."""
    card = RoundedRectangle(width=w, height=h, corner_radius=0.1, fill_color="#FFFFFF",
                            fill_opacity=1, stroke_color=DIM, stroke_width=2).move_to([x, y, 0])
    fracs = [0.95, 0.7, 0.9, 0.55]
    lines = VGroup(*[Line([x - w / 2 + 0.3, y + h / 2 - 0.55 - i * 0.42, 0],
                          [x - w / 2 + 0.3 + (w - 0.9) * f, y + h / 2 - 0.55 - i * 0.42, 0],
                          color=GHOST, stroke_width=4) for i, f in enumerate(fracs)])
    return VGroup(card, lines)


def bin_can(x, y, w=2.2, h=2.2):
    """The trash bin: tapered, grey fill, ink outline and rim. Big backing
    shape in DIM-grey (Gate V: near-black fields read as giant text)."""
    pts = [(x - w / 2, y + h / 2), (x + w / 2, y + h / 2),
           (x + w * 0.36, y - h / 2), (x - w * 0.36, y - h / 2)]
    body = Polygon(*[[px, py, 0] for px, py in pts],
                   fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=4)
    rim = Line([x - w / 2 - 0.14, y + h / 2 + 0.07, 0], [x + w / 2 + 0.14, y + h / 2 + 0.07, 0],
               color=INK, stroke_width=5)
    ribs = VGroup(*[Line([x + dx * 0.5, y + h / 2 - 0.4, 0], [x + dx * 0.36, y - h / 2 + 0.3, 0],
                         color=GHOST, stroke_width=3) for dx in (-0.9, 0, 0.9)])
    return VGroup(body, ribs, rim)


def archive_tray(x, y, w=2.8, h=1.6):
    """The archive: an open tray, kraft fill, ink outline (reuse of tray())."""
    return tray(x, y, w=w, h=h)


# ═════════════════════════════ scenes ═════════════════════════════
class B00_ThePile(Scene):
    """The pain: an open tray; email cards drop in one by one until the pile
    overflows; terracotta dots land on the three that matter (buried)."""

    def construct(self):
        tr = tray(-1.2, -0.9, w=5.6, h=2.8)
        lab = tag("the pile", -5.2, 2.2, -3.8, 0.4)
        self.play(FadeIn(tr), FadeIn(lab), run_time=1.0)
        until(self, "Somewhere in here are a bill")
        spots = [(-3.1, -1.5), (-2.15, -1.05), (-1.2, -1.5), (-0.25, -1.05), (-2.6, -0.3), (-1.1, -0.25)]
        first = VGroup(*[pile_card(x, 2.7) for x, y in spots[:3]])
        self.play(FadeIn(first), run_time=0.5)
        self.play(*[c.animate.move_to([sx, sy, 0]) for c, (sx, sy) in zip(first, spots[:3])], run_time=1.0)
        until(self, "newsletters, receipts, promos")
        second = VGroup(*[pile_card(x, 2.7) for x, y in spots[3:]])
        self.play(FadeIn(second), run_time=0.5)
        self.play(*[c.animate.move_to([sx, sy, 0]) for c, (sx, sy) in zip(second, spots[3:])], run_time=1.0)
        until(self, "This one is about what you do once it's in", lead=0.4)
        dots = VGroup(*[Dot([sx, sy, 0], radius=0.07, color=TERRA) for sx, sy in (spots[1], spots[3], spots[4])])
        self.play(FadeIn(dots), run_time=0.6)
        finish(self)


class B01_Triage(Scene):
    """The first pass: a scan line sweeps the pile; it splits into two stacks
    — 'needs you' (ink) and 'noise' (dim); a terracotta check lands on what matters."""

    def construct(self):
        tr = tray(-1.2, -0.9, w=5.6, h=2.8)
        spots = [(-3.1, -1.5), (-2.15, -1.05), (-1.2, -1.5), (-0.25, -1.05), (-2.6, -0.3), (-1.1, -0.25)]
        pile = VGroup(*[pile_card(sx, sy) for sx, sy in spots])
        lab = tag("triage", -5.2, 2.2, -3.8, 0.4)
        self.play(FadeIn(tr), FadeIn(pile), FadeIn(lab), run_time=1.0)
        until(self, "what actually needs me")
        scan = scan_line(-4.0, 1.6, 0.3)
        self.play(Create(scan), scan.animate.shift(DOWN * 2.4), run_time=0.9)
        s1 = stack_card(-3.5, -0.5, ink_lines=3)
        lab1 = T("needs you", size=32).move_to([-3.5, 1.0, 0])
        s2 = stack_card(2.7, -0.5, dim_lines=4)
        lab2 = T("noise", size=32).move_to([2.7, 1.0, 0])
        self.play(FadeOut(scan), FadeOut(pile), FadeIn(s1), FadeIn(lab1), FadeIn(s2), FadeIn(lab2), run_time=0.5)
        until(self, "You read what matters")
        tick = check(-2.35, 0.15, s=0.15, color=TERRA, w=6)
        self.play(FadeIn(tick), run_time=0.6)
        finish(self)


class B02_TheSummary(Scene):
    """The summary: kraft lines draw from the long thread to a brief card
    that grows with three ink lines; terracotta dots land."""

    def construct(self):
        thread = thread_stack(-3.6, 0.1)
        lab = tag("the summary", 2.3, 2.35, 2.3, 1.55)
        self.play(FadeIn(thread), FadeIn(lab), run_time=1.0)
        until(self, "a dozen emails back and forth")
        k1 = cable(-2.6, 0.6, 0.6, 0.75)
        k2 = cable(-2.6, -0.4, 0.6, -0.35)
        brief = brief_card(2.3, 0.1)
        self.play(Create(k1), Create(k2), GrowFromCenter(brief), run_time=1.0)
        until(self, "You walk into the meeting")
        dots = VGroup(*[Dot([0.92, 1.05 - i * 0.6, 0], radius=0.07, color=TERRA) for i in range(3)])
        self.play(FadeIn(dots), run_time=0.6)
        finish(self)


class B03_TheDraft(Scene):
    """The draft: one email card; beside it a draft card grows with reply
    lines; an ink check lands — the AI guesses, you act."""

    def construct(self):
        email = email_card(-3.2, 0.2, w=2.2, h=1.6)
        lab = tag("the draft", 1.8, 2.05, 1.8, 1.3)
        self.play(FadeIn(email), FadeIn(lab), run_time=1.0)
        until(self, "it writes you a draft")
        draft = draft_card(1.8, 0.2)
        self.play(GrowFromCenter(draft), run_time=1.0)
        until(self, "only then hit send yourself")
        tick = check(3.05, 0.95, s=0.15, color=INK, w=6)
        self.play(FadeIn(tick), run_time=0.6)
        finish(self)


class B04_NeverAutoSend(Scene):
    """Rule 1: the draft card; the ink SEND pill lands; an ink lock lands
    over the pill — the send button stays yours."""

    def construct(self):
        draft = draft_card(0, 0.7, w=3.4, h=2.0)
        lab = tag("never auto-send", -3.9, 2.05, -1.7, 1.6)
        self.play(FadeIn(draft), FadeIn(lab), run_time=1.0)
        until(self, "the damage is done in one click")
        send = send_pill(0, -1.5)
        self.play(FadeIn(send), run_time=0.8)
        until(self, "the send button stays yours")
        lk = lock(0, -1.5, s=0.9)
        self.play(FadeIn(lk), run_time=0.7)
        finish(self)


class B05_NeverAutoDelete(Scene):
    """Rule 2: an email card hovers over the bin; an ink X stamps the bin
    (never delete); the card slides into the archive tray; a terracotta
    check stamps the tray — archive, don't delete."""

    def construct(self):
        bn = bin_can(-2.8, -0.8)
        email = pile_card(-2.8, 1.5, w=2.0, h=1.15)
        lab = tag("never auto-delete", -2.8, -2.55, -2.8, -1.9)
        self.play(FadeIn(bn), FadeIn(email), FadeIn(lab), run_time=1.0)
        until(self, "Never let it delete on its own")
        xs = x_stamp(-2.8, -0.8, s=0.55)
        self.play(FadeIn(xs), run_time=0.6)
        until(self, "tell it to archive the noise instead")
        arch = archive_tray(3.2, -0.8)
        self.play(GrowFromCenter(arch), email.animate.move_to([3.2, -0.8, 0]), run_time=1.0)
        until(self, "empty the trash yourself")
        tick = check(4.25, -0.35, s=0.15, color=TERRA, w=6)
        self.play(FadeIn(tick), run_time=0.6)
        finish(self)
