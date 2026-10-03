#!/usr/bin/env python3
"""gen_galaxies.py — deterministic synthetic galaxy cutouts for the reel.

WHY SYNTHETIC. This episode is about sorting galaxy IMAGES, so it needs images.
Real SDSS/DECaLS cutouts would drag in per-image licensing and a network fetch,
and — more to the point — the beats need a *controlled* set: one clean exemplar
of each morphology, a hero galaxy that can be voted on, and dense fields of
hundreds of objects to carry the scale claims. So every galaxy here is drawn
from a physical-ish recipe with a fixed seed.

HONESTY. These are ILLUSTRATIONS OF MORPHOLOGY CLASSES, not observations, and
every scene that shows them captions them as synthetic. No claim in the reel
rests on a pixel produced by this file — the numbers all come from the papers
cited in FACTCHECK.md. Same seed in, same PNGs out.

RECIPES
  elliptical   Sersic-ish smooth blob, axis ratio 0.55-0.95, no structure
  spiral       bulge + two logarithmic arms + HII knots along the arms
  barred       bulge + straight bar + arms launched from the bar ends
  edge-on      thin exponential disc + a darker dust lane through the midplane
  merger       two cores with a tidal bridge and an asymmetric envelope

Run:  python gen_galaxies.py        (writes ./galaxies/*.png and ./field_*.png)
"""
from __future__ import annotations

import math
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "galaxies")

# Sky is not black on a printed page — a very dark warm charcoal sits better on
# cream than pure #000 and keeps the tiles from punching holes in the layout.
# NOTE this is a FLUX level, not a display level: the asinh stretch at the end
# lifts it, so it has to be set low or every tile comes out mid-grey.
SKY = np.array([3.0, 3.0, 4.2])

# Warm core, cooler arms: the usual old-bulge / young-disc colour gradient,
# desaturated so the tiles never compete with the brand's one terracotta accent.
CORE_RGB = np.array([255.0, 236.0, 205.0])
DISC_RGB = np.array([176.0, 198.0, 232.0])
ARM_RGB = np.array([205.0, 222.0, 245.0])


def _canvas(n):
    return np.tile(SKY, (n, n, 1)).astype(np.float64)


def _grid(n):
    ax = np.linspace(-1.0, 1.0, n)
    return np.meshgrid(ax, ax)


def _add_blob(img, cx, cy, sx, sy, theta, amp, rgb):
    """Add an oriented 2-D Gaussian of light."""
    n = img.shape[0]
    X, Y = _grid(n)
    xr = (X - cx) * math.cos(theta) + (Y - cy) * math.sin(theta)
    yr = -(X - cx) * math.sin(theta) + (Y - cy) * math.cos(theta)
    g = np.exp(-0.5 * ((xr / sx) ** 2 + (yr / sy) ** 2))
    img += amp * g[:, :, None] * rgb[None, None, :] / 255.0
    return img


def _add_point(img, cx, cy, s, amp, rgb):
    n = img.shape[0]
    X, Y = _grid(n)
    g = np.exp(-0.5 * (((X - cx) ** 2 + (Y - cy) ** 2) / s ** 2))
    img += amp * g[:, :, None] * rgb[None, None, :] / 255.0
    return img


def _starfield(img, rng, count=15):
    """A sparse field of foreground stars — what makes a cutout read as a cutout."""
    for _ in range(count):
        cx, cy = rng.uniform(-1, 1), rng.uniform(-1, 1)
        s = rng.uniform(0.005, 0.013)
        amp = rng.uniform(30.0, 320.0)
        img = _add_point(img, cx, cy, s, amp, np.array([255.0, 250.0, 240.0]))
    return img


# Everything above is accumulated in linear "flux"; the display stretch is applied
# once, at the end, with FIXED constants so every tile in the reel shares one
# scale. asinh (not a power law) is what surveys actually use: it is linear near
# zero so faint arms survive, and logarithmic at the top so the bulge does not
# bloom into a white disc — which is exactly what a naive linear stretch does.
SOFT = 8.0
FMAX = 1100.0
_NORM = math.asinh(FMAX / SOFT)


def _finish(img, rng, noise=1.1):
    img = img + rng.normal(0, noise, img.shape)
    img = 255.0 * np.arcsinh(np.clip(img, 0, None) / SOFT) / _NORM
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


# ── morphologies ─────────────────────────────────────────────────────────────
def elliptical(n, seed):
    rng = np.random.RandomState(seed)
    img = _canvas(n)
    img = _starfield(img, rng)
    q = rng.uniform(0.58, 0.95)
    r = rng.uniform(0.090, 0.130)
    th = rng.uniform(0, math.pi)
    # de Vaucouleurs-ish: a bright core with a long faint envelope, no structure
    for k, amp in ((0.55, 820.0), (1.2, 210.0), (2.4, 44.0), (4.4, 9.0)):
        img = _add_blob(img, 0, 0, r * k, r * q * k, th, amp, CORE_RGB)
    return _finish(img, rng)


def spiral(n, seed, arms=2, barred=False):
    rng = np.random.RandomState(seed)
    img = _canvas(n)
    img = _starfield(img, rng)
    incl = rng.uniform(0.74, 1.0)          # cos(inclination) — mild tilt only
    pa = rng.uniform(0, math.pi)
    pitch = rng.uniform(0.17, 0.26)        # smaller pitch = more windings
    bulge = rng.uniform(0.038, 0.058)
    rmax = rng.uniform(0.60, 0.72)

    # exponential disc
    img = _add_blob(img, 0, 0, rmax * 0.62, rmax * 0.62 * incl, pa, 22.0, DISC_RGB)
    img = _add_blob(img, 0, 0, rmax * 0.30, rmax * 0.30 * incl, pa, 30.0, DISC_RGB)

    bar_len = rng.uniform(0.13, 0.19) if barred else 0.0
    if barred:
        img = _add_blob(img, 0, 0, bar_len, bar_len * 0.20, pa, 240.0, CORE_RGB)
        img = _add_blob(img, 0, 0, bar_len * 1.25, bar_len * 0.34, pa, 70.0, CORE_RGB)

    # logarithmic arms as a dense run of small overlapping knots
    r0 = bar_len if barred else 0.050
    for a in range(arms):
        phase = pa + a * (2 * math.pi / arms)
        for t in np.linspace(0.0, 4.2, 320):
            rad = r0 + 0.055 * (math.exp(pitch * t) - 1.0) * 2.2
            if rad > rmax:
                break
            ang = phase + t
            x = rad * math.cos(ang)
            y = rad * math.sin(ang) * incl
            w = 0.017 + 0.007 * (rad / rmax)
            amp = 15.0 * math.exp(-1.5 * rad / rmax)
            img = _add_point(img, x, y, w, amp, ARM_RGB)
            if rng.random() < 0.05:      # star-forming knots along the arm
                img = _add_point(img, x + rng.normal(0, 0.012),
                                 y + rng.normal(0, 0.012),
                                 rng.uniform(0.009, 0.015),
                                 rng.uniform(30.0, 90.0),
                                 np.array([225.0, 238.0, 255.0]))

    # bulge last so it sits on top of the arms
    for k, amp in ((0.7, 700.0), (1.6, 150.0), (3.2, 26.0)):
        img = _add_blob(img, 0, 0, bulge * k, bulge * k * incl, pa, amp, CORE_RGB)
    return _finish(img, rng)


def edge_on(n, seed):
    rng = np.random.RandomState(seed)
    img = _canvas(n)
    img = _starfield(img, rng)
    th = rng.uniform(-0.40, 0.40)
    length = rng.uniform(0.36, 0.48)
    thick = rng.uniform(0.030, 0.046)
    X, Y = _grid(n)
    xr = X * math.cos(th) + Y * math.sin(th)
    yr = -X * math.sin(th) + Y * math.cos(th)

    img = _add_blob(img, 0, 0, length * 1.15, thick * 3.2, th, 24.0, DISC_RGB)
    img = _add_blob(img, 0, 0, length, thick * 1.5, th, 120.0, CORE_RGB)
    img = _add_blob(img, 0, 0, thick * 2.6, thick * 2.2, th, 620.0, CORE_RGB)

    # Dust lane: absorption, so it MULTIPLIES the light rather than subtracting a
    # fixed amount — and it is bounded by the disc's own extent so it cannot run
    # off the edge of the tile as a stray line.
    lane = np.exp(-0.5 * (yr / (thick * 0.42)) ** 2)
    envelope = np.exp(-0.5 * (xr / (length * 0.95)) ** 2)
    img *= (1.0 - 0.80 * (lane * envelope))[:, :, None]
    return _finish(img, rng)


def merger(n, seed):
    rng = np.random.RandomState(seed)
    img = _canvas(n)
    img = _starfield(img, rng)
    ax, ay = rng.uniform(-0.30, -0.16), rng.uniform(-0.16, 0.16)
    bx, by = rng.uniform(0.16, 0.30), rng.uniform(-0.16, 0.16)
    for (cx, cy, s, peak) in ((ax, ay, rng.uniform(0.055, 0.085), 640.0),
                              (bx, by, rng.uniform(0.040, 0.065), 430.0)):
        img = _add_blob(img, cx, cy, s * 2.6, s * 2.0, rng.uniform(0, 3.14), 20.0, DISC_RGB)
        img = _add_blob(img, cx, cy, s, s * 0.84, rng.uniform(0, 3.14), peak, CORE_RGB)
    # tidal bridge between the two cores
    for t in np.linspace(0, 1, 90):
        x = ax + (bx - ax) * t
        y = ay + (by - ay) * t + 0.07 * math.sin(math.pi * t)
        img = _add_point(img, x, y, 0.022, 7.0, ARM_RGB)
    # and the two tails thrown off outward
    for (sx, sy, dx, dy) in ((ax, ay, -0.42, 0.26), (bx, by, 0.42, -0.28)):
        for t in np.linspace(0, 1, 70):
            img = _add_point(img, sx + dx * t, sy + dy * t + 0.12 * t * t,
                             0.020 + 0.014 * t, 8.0 * (1 - t) ** 1.4, ARM_RGB)
    return _finish(img, rng)


# ── catalogue ────────────────────────────────────────────────────────────────
KINDS = {
    "elliptical": lambda n, s: elliptical(n, s),
    "spiral": lambda n, s: spiral(n, s, arms=2, barred=False),
    "spiral3": lambda n, s: spiral(n, s, arms=3, barred=False),
    "barred": lambda n, s: spiral(n, s, arms=2, barred=True),
    "edgeon": lambda n, s: edge_on(n, s),
    "merger": lambda n, s: merger(n, s),
}

# The exemplars each beat calls out by name. Seeds are fixed and logged in
# SOURCES.md so any of these can be regenerated byte-identically.
EXEMPLARS = [
    ("spiral", 101), ("spiral", 102), ("spiral", 103), ("spiral", 104),
    ("barred", 201), ("barred", 202), ("barred", 203),
    ("elliptical", 301), ("elliptical", 302), ("elliptical", 303), ("elliptical", 304),
    ("edgeon", 401), ("edgeon", 402), ("edgeon", 403),
    ("merger", 501), ("merger", 502),
    ("spiral3", 601), ("spiral3", 602),
]

# The hero galaxy — the one the vote-fraction beat actually votes on. A barred
# spiral on purpose: "does it have a bar?" is the GZ2 question where volunteers
# genuinely disagree, which is what makes the vote fraction worth predicting.
HERO = ("barred", 777)


def _field(path, cols, rows, tile, seed, gap=2):
    """One pre-composited sheet of many galaxies — far cheaper for Manim to load
    than hundreds of separate ImageMobjects, and it is what the scale beats need."""
    rng = np.random.RandomState(seed)
    names = list(KINDS)
    # Roughly the real morphology mix: mostly smooth/elliptical and small
    # featureless things, a minority of clean spirals, mergers rare.
    weights = np.array([0.34, 0.24, 0.06, 0.12, 0.16, 0.08])
    W = cols * tile + (cols - 1) * gap
    H = rows * tile + (rows - 1) * gap
    sheet = Image.new("RGB", (W, H), tuple(SKY.astype(int)))
    for r in range(rows):
        for c in range(cols):
            kind = names[rng.choice(len(names), p=weights)]
            g = KINDS[kind](tile, int(rng.randint(0, 10 ** 6)))
            sheet.paste(g, (c * (tile + gap), r * (tile + gap)))
    sheet.save(path)
    return path


def rotations(src="spiral_101.png", degs=(0, 45, 90, 135)):
    """Pre-rotated copies of ONE cutout, kept square.

    B08 is about feeding the same image in at several orientations. Rotating an
    ImageMobject inside Manim turns the tile into a diamond and desyncs it from
    its frame, so the rotation is baked here instead — which is also closer to
    the truth: this is the data augmentation the architecture actually applies.
    `expand=False` keeps the canvas square; corners fill with the sky level.
    """
    made = []
    base = Image.open(os.path.join(OUT, src))
    sky = tuple(int(255.0 * math.asinh(v / SOFT) / _NORM) for v in SKY)
    for d in degs:
        r = base.rotate(d, resample=Image.BICUBIC, expand=False, fillcolor=sky)
        q = os.path.join(OUT, f"rot_{d:03d}.png")
        r.save(q)
        made.append(q)
    return made


def shallow(src="spiral_103.png", out="spiral_103_shallow.png"):
    """The SAME galaxy as a shallower, coarser survey would record it.

    B08's point needs two cutouts that are recognisably the same object and
    recognisably different data: fewer faint pixels, softer resolution, more
    noise. Downsample, re-upsample, add read noise, clip the faint end.
    """
    im = Image.open(os.path.join(OUT, src))
    n = im.size[0]
    small = im.resize((n // 4, n // 4), Image.BILINEAR).resize((n, n), Image.BILINEAR)
    a = np.asarray(small).astype(np.float64)
    rng = np.random.RandomState(4242)
    a = a * 0.82 + rng.normal(0, 7.0, a.shape)          # shallower + noisier
    a = np.clip(a - 6.0, 0, 255)                        # faint end lost
    q = os.path.join(OUT, out)
    Image.fromarray(a.astype(np.uint8), "RGB").save(q)
    return q


def main():
    os.makedirs(OUT, exist_ok=True)
    made = []
    for kind, seed in EXEMPLARS:
        p = os.path.join(OUT, f"{kind}_{seed}.png")
        KINDS[kind](256, seed).save(p)
        made.append(p)
    p = os.path.join(OUT, "hero.png")
    KINDS[HERO[0]](512, HERO[1]).save(p)
    made.append(p)

    made.extend(rotations())
    made.append(shallow())

    # scale sheets
    made.append(_field(os.path.join(HERE, "field_12x7.png"), 12, 7, 96, seed=9001))
    made.append(_field(os.path.join(HERE, "field_28x16.png"), 28, 16, 40, seed=9002))
    for p in made:
        print("wrote", os.path.relpath(p, HERE))


if __name__ == "__main__":
    main()
