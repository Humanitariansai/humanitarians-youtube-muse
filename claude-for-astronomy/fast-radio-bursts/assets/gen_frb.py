#!/usr/bin/env python3
"""gen_frb.py — deterministic synthetic radio dynamic spectra for the reel.

WHY SYNTHETIC. This episode is about triaging radio candidates, so it needs
candidates: waterfall plots (frequency x time) of dispersed bursts, and the
interference that mimics them. Real telescope data would need per-archive
permissions and would not give the controlled set the beats require — one clean
burst at a known DM, one of each RFI class, a DM-time plane, and dense candidate
sheets that are almost all false positives. Every plot here is drawn from the
dispersion law with a fixed seed.

HONESTY. These are ILLUSTRATIONS OF SIGNAL MORPHOLOGY, not observations. No
claim in the reel rests on a pixel produced by this file; the numbers all come
from the papers cited in FACTCHECK.md. Scenes that show them caption them.

THE PHYSICS THAT MAKES IT DRAWABLE
  A burst leaving its source arrives later at lower frequencies:
      dt = k * DM * (nu^-2 - nu_ref^-2),   k = 4.148808 ms GHz^2 (pc cm^-3)^-1
  So a real burst sweeps across the band. Interference does not: it arrives at
  every frequency at once (DM = 0), or sits at one frequency forever. That
  difference IS the search.

RENDERING. Plots are ink-on-white so they sit on the reel's cream page the way a
figure sits in a paper — deliberately unlike Ep. 04's dark photographic plates.

Run:  python gen_frb.py     (writes ./plots/*.png)
"""
from __future__ import annotations

import math
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "plots")

# Plot ink: dark warm ink on a white plot ground, matching the reel's palette.
PAPER = np.array([255.0, 255.0, 255.0])
INK = np.array([61.0, 57.0, 41.0])
ACC = np.array([217.0, 119.0, 87.0])      # terracotta, for the ONE flagged burst

# CHIME's band, which is also the band Catalog 1 was taken in.
NU_LO, NU_HI = 0.400, 0.800               # GHz
K_DM = 4.148808                           # ms GHz^2 (pc cm^-3)^-1


def _paint(sig, accent=False, gamma=0.85):
    """Turn a 0..1 signal array into an ink-on-paper RGB image."""
    s = np.clip(sig, 0.0, 1.0) ** gamma
    col = ACC if accent else INK
    img = PAPER[None, None, :] * (1 - s[:, :, None]) + col[None, None, :] * s[:, :, None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def _noise(w, h, rng, level=0.020, base=0.058):
    """Receiver noise: Gaussian per channel, plus a little channel-to-channel
    gain variation so it reads like real data rather than a texture.

    Kept LIGHT on purpose, and then lightened again. Two reasons: a realistic
    noise floor turns the panel into grey static at the size these are shown,
    and -- the binding one -- GATE V counts any pixel more than 28/255 from the
    page colour as "ink" and then checks the MEAN ink luminance against the
    background. Mid-grey speckle over a large panel area drags that mean up and
    fails the whole beat as low-contrast. At this level the speckle stays below
    the threshold, so only the real features (the sweep, the frame, the type)
    count -- which is also what makes them read.

    The binding constraint is the RED channel. The page is warm cream and these
    panels are neutral grey, and GATE V compares against a coarsely quantised
    corner colour whose red lands near 248. So a neutral pixel only has to fall
    to about 223 before it reads as ink, which a realistic speckle does at +2
    sigma. Keeping the whole distribution above that is what this level buys."""
    n = rng.normal(0.0, level, (h, w))
    gain = 1.0 + rng.normal(0.0, 0.08, (h, 1))
    return np.clip(base + n * gain, 0.0, 1.0)


def _sweep_delay(nu, dm, t_ref):
    """Arrival time at frequency nu, in ms, for a burst of the given DM."""
    return t_ref + K_DM * dm * (nu ** -2 - NU_HI ** -2)


def band_sweep_ms(dm):
    """Total delay across the whole band for this DM.

    At CHIME's 400-800 MHz this is large: DM 500 sweeps about 9.7 SECONDS, not
    milliseconds. Real waterfall figures crop the time axis to the sweep, so the
    panels here do the same rather than pinning a fixed 100 ms window and
    letting the burst run off the edge.
    """
    return K_DM * dm * (NU_LO ** -2 - NU_HI ** -2)


def burst(w=384, h=256, dm=500.0, seed=1, width_ms=1.6, snr=1.0,
          t_span=None, scatter=0.0):
    """A dispersed burst in a frequency-time waterfall.

    Rows are frequency (top = NU_HI), columns are time over t_span ms.
    """
    rng = np.random.RandomState(seed)
    if t_span is None:
        t_span = band_sweep_ms(dm) * 1.30 or 100.0
    sig = _noise(w, h, rng)
    cols = np.arange(w)
    t = cols * (t_span / w)
    # the pulse is narrow next to the sweep, so give it at least a pixel or two
    px = t_span / w
    for r in range(h):
        nu = NU_HI - (NU_HI - NU_LO) * (r / (h - 1))
        t_arr = _sweep_delay(nu, dm, t_span * 0.10)
        if not (0 <= t_arr <= t_span):
            continue
        # scattering broadens the pulse toward low frequency (nu^-4)
        wid = width_ms + scatter * (NU_HI / nu) ** 4
        prof = np.exp(-0.5 * ((t - t_arr) / max(wid, 1.6 * px)) ** 2)
        # a real burst is patchy in frequency, not a smooth ribbon
        band = 0.55 + 0.45 * math.sin(r * 0.11 + seed) ** 2
        sig[r] += prof * snr * 0.95 * band
    return _paint(sig)


def rfi_zero_dm(w=384, h=256, seed=2, t_span=100.0):
    """Interference that hits every channel at once: DM = 0, no sweep.

    The microwave-oven / power-line / lightning signature, and precisely what a
    dispersion search exists to reject."""
    rng = np.random.RandomState(seed)
    sig = _noise(w, h, rng)
    t0 = t_span * rng.uniform(0.35, 0.62)
    t = np.arange(w) * (t_span / w)
    prof = np.exp(-0.5 * ((t - t0) / 2.2) ** 2)
    for r in range(h):
        sig[r] += prof * rng.uniform(0.7, 1.0)
    return _paint(sig)


def rfi_narrowband(w=384, h=256, seed=3):
    """Persistent transmitters: a few channels, on the whole time."""
    rng = np.random.RandomState(seed)
    sig = _noise(w, h, rng)
    for _ in range(rng.randint(3, 6)):
        r0 = rng.randint(4, h - 4)
        thick = rng.randint(1, 4)
        strength = rng.uniform(0.55, 0.95)
        for r in range(max(0, r0 - thick), min(h, r0 + thick)):
            sig[r] += strength * rng.uniform(0.7, 1.0)
    return _paint(sig)


def rfi_patch(w=384, h=256, seed=4):
    """A blob of interference: bursty, band-limited, no dispersion sweep."""
    rng = np.random.RandomState(seed)
    sig = _noise(w, h, rng)
    # margins and blob sizes scale with the tile: the contact sheets render
    # these at 40 px, where fixed pixel margins go negative.
    mr, mc = max(3, h // 8), max(3, w // 8)
    for _ in range(rng.randint(2, 4)):
        rc, cc = rng.randint(mr, h - mr), rng.randint(mc, w - mc)
        rr = rng.randint(max(2, h // 24), max(3, h // 6))
        cr = rng.randint(max(2, w // 60), max(3, w // 14))
        rs = np.arange(max(0, rc - rr), min(h, rc + rr))
        cs = np.arange(max(0, cc - cr), min(w, cc + cr))
        dr = ((rs - rc) / rr) ** 2
        dc = ((cs - cc) / cr) ** 2
        d = dr[:, None] + dc[None, :]
        sig[np.ix_(rs, cs)] += 0.85 * np.clip(1.0 - d, 0, None)
    return _paint(sig)


def dedispersed(w=384, h=256, seed=1, t_span=100.0, width_ms=1.6):
    """The same burst after correcting for the sweep: the pulse stands vertical.

    This is what dedispersion at the CORRECT trial DM produces, and it is why a
    bank of trial DMs is searched at all."""
    rng = np.random.RandomState(seed)
    sig = _noise(w, h, rng)
    t = np.arange(w) * (t_span / w)
    prof = np.exp(-0.5 * ((t - t_span * 0.5) / max(width_ms, 0.35)) ** 2)
    for r in range(h):
        band = 0.70 + 0.30 * math.sin(r * 0.11 + seed) ** 2
        sig[r] += prof * 1.05 * band
    return _paint(sig)


def dm_time(w=384, h=256, dm_true=500.0, seed=1, t_span=100.0, dm_half=None,
            dm_centre=None):
    """The DM-time plane: signal-to-noise against trial DM and arrival time.

    A real burst makes a bowtie that closes at one DM. Zero-DM interference
    peaks at the bottom edge and never closes. This is the second image the
    classifier is shown, and it is where the two cases look least alike."""
    rng = np.random.RandomState(seed + 77)
    sig = _noise(w, h, rng, level=0.018, base=0.054)
    t = np.arange(w) * (t_span / w)
    # A DM error of 1 pc cm^-3 already smears the pulse by ~19 ms across this
    # band, so the bowtie only spans a couple of DM units. Pick the window that
    # makes it fill the panel instead of hard-coding a DM range.
    if dm_half is None:
        dm_half = 0.42 * t_span / band_sweep_ms(1.0)
    # The panel is centred on the TRIAL DM the search is examining, which is not
    # necessarily where the signal is. For zero-DM interference the apex sits far
    # below the window, so the bowtie never closes inside the panel -- and that
    # is exactly the difference the classifier is being shown.
    centre = dm_true if dm_centre is None else dm_centre
    for r in range(h):
        trial = centre + dm_half * (1.0 - 2.0 * r / (h - 1))
        ddm = trial - dm_true
        smear = abs(band_sweep_ms(ddm))
        amp = 1.0 / (1.0 + (smear / 4.0) ** 2)
        wid = max(t_span / w * 1.8, smear * 0.55)
        sig[r] += amp * np.exp(-0.5 * ((t - t_span * 0.5) / wid) ** 2) * 0.95
    return _paint(sig)


def sheet(path, cols, rows, tile, seed, real_at=None, gap=3):
    """A contact sheet of candidates. Almost every one is interference; at most
    one is a burst, drawn in the accent colour so a beat can point at it. That
    ratio is the episode's whole problem in one picture."""
    rng = np.random.RandomState(seed)
    W = cols * tile + (cols - 1) * gap
    H = rows * tile + (rows - 1) * gap
    board = Image.new("RGB", (W, H), (226, 223, 212))
    kinds = (rfi_zero_dm, rfi_narrowband, rfi_patch)
    for r in range(rows):
        for c in range(cols):
            i = r * cols + c
            s = int(rng.randint(0, 10 ** 6))
            if real_at is not None and i == real_at:
                im = burst(tile, tile, dm=rng.uniform(300, 900), seed=s,
                           width_ms=2.0)
                lum = np.asarray(im.convert("L")).astype(np.float64) / 255.0
                im = _paint(1.0 - lum, accent=True)
            else:
                im = kinds[rng.choice(3, p=[0.45, 0.33, 0.22])](tile, tile, seed=s)
            board.paste(im, (c * (tile + gap), r * (tile + gap)))
    board.save(path)
    return path


def main():
    os.makedirs(OUT, exist_ok=True)
    made = []

    def w(name, im):
        im.save(os.path.join(OUT, name))
        made.append(name)

    # the hero burst, and the same burst dedispersed
    w("burst_dm500.png", burst(dm=500.0, seed=11, width_ms=1.7))
    w("burst_dm500_big.png", burst(w=512, h=384, dm=500.0, seed=11, width_ms=1.7))
    w("burst_dedispersed.png", dedispersed(seed=11, width_ms=1.7))
    w("burst_scattered.png", burst(dm=760.0, seed=12, width_ms=1.4, scatter=2.6))
    # The DM trio shares one time axis (sized for the largest DM) so the slope
    # difference is the thing you see. Auto-scaling each panel to its own sweep
    # made all three look identical, which is the opposite of the point.
    trio_span = band_sweep_ms(900.0) * 1.10
    w("burst_dm200.png", burst(dm=200.0, seed=13, width_ms=1.5, t_span=trio_span))
    w("burst_dm500_trio.png", burst(dm=500.0, seed=11, width_ms=1.7, t_span=trio_span))
    w("burst_dm900.png", burst(dm=900.0, seed=14, width_ms=2.1, t_span=trio_span))

    # the impostors
    w("rfi_zero_dm.png", rfi_zero_dm(seed=21))
    w("rfi_zero_dm_big.png", rfi_zero_dm(w=512, h=384, seed=21))
    w("rfi_narrowband.png", rfi_narrowband(seed=22))
    w("rfi_patch.png", rfi_patch(seed=23))

    # the DM-time plane, for a real burst and for zero-DM interference
    w("dmtime_burst.png", dm_time(dm_true=500.0, seed=11))
    # Zero-DM interference: put the window's LOWER edge at DM 0 so the apex sits
    # exactly on the bottom of the panel. Centring far above it (at the trial DM
    # the search was examining) is physically right but renders a blank panel,
    # which teaches nothing -- this way you see the bowtie fail to close.
    dmh = 0.42 * 100.0 / band_sweep_ms(1.0)
    w("dmtime_rfi.png", dm_time(dm_true=0.0, dm_centre=dmh, dm_half=dmh, seed=31))

    # candidate sheets: the haystack
    made.append(os.path.basename(sheet(os.path.join(OUT, "sheet_10x6.png"),
                                       10, 6, 96, seed=9101, real_at=37)))
    made.append(os.path.basename(sheet(os.path.join(OUT, "sheet_24x14.png"),
                                       24, 14, 40, seed=9102, real_at=201)))
    for n in made:
        print("wrote plots/" + n)


if __name__ == "__main__":
    main()
