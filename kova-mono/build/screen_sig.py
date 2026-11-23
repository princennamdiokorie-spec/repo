"""Prepare a chrome title on black for SCREEN blending onto a black flyer.
Everything at or below the local glow level is pushed to black (screen ignores black),
chrome highlights are kept, and a soft halo is added back from the bright parts.
No cut-out mask, so no patches, holes or fringes. Usage: screen_sig.py <src> <out>"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

src, out = sys.argv[1], sys.argv[2]
GAMMA = float(sys.argv[3]) if len(sys.argv) > 3 else 1.05      # <1 lifts dark chrome (used for the darker title B)
GAIN = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
im = np.asarray(Image.open(src).convert('RGB')).astype(float) / 255
L = im.mean(2); h, w = L.shape
q = 4
bg = ndi.median_filter(L[::q, ::q], size=31)
bg = ndi.zoom(ndi.gaussian_filter(bg, 2), q, order=1)[:h, :w]
t = np.clip(bg * .82, 0, .9)                              # local black point: below the glow, so chrome keeps its body; leftover glow stays soft
v0 = np.clip((L - t) / (1 - t), 0, 1)
v = v0 ** 1.05
if GAMMA != 1.05 or GAIN != 1.0:
    # brighten the LETTERS only: soft mask of pixels that differ from the glow (chrome both
    # bright and dark), gaps inside strokes filled, so the glow around them is untouched
    lm = np.abs(L - bg) > .14
    lm = ndi.binary_closing(lm, np.ones((5, 5)))
    lab, n = ndi.label(lm); sz = ndi.sum(lm, lab, range(1, n + 1))
    lm = np.isin(lab, 1 + np.where(sz > 400)[0])
    holes = ndi.binary_fill_holes(lm) & ~lm
    hl, hn = ndi.label(holes); hs = ndi.sum(holes, hl, range(1, hn + 1))
    lm |= np.isin(hl, 1 + np.where(hs < 5000)[0])
    w = np.clip(ndi.gaussian_filter(ndi.binary_erosion(lm, iterations=2).astype(float), 2.0) * 1.3, 0, 1)
    vb = np.clip(v0 ** GAMMA * GAIN, 0, 1)
    v = v * (1 - w) + vb * w
rgb = im * (v / np.maximum(L, 1e-4))[..., None]
halo = ndi.gaussian_filter(v, 14) * .22                    # tight soft glow from the chrome itself
rgb = 1 - (1 - rgb) * (1 - halo[..., None])                # screen the halo in
# fade whatever glow is left to black away from the letters, so the image has no box edge
near = ndi.gaussian_filter((v > .25).astype(float), 30)
rgb = rgb * np.clip(near * 3.2, 0, 1)[..., None]
if GAMMA < 1:                                          # crisp edges for readability: unsharp mask on the letters only
    blur = ndi.gaussian_filter(rgb, (1.6, 1.6, 0))
    rgb = rgb + (rgb - blur) * .8 * w[..., None]
img = Image.fromarray((rgb.clip(0, 1) * 255).astype(np.uint8))
bb = img.convert('L').point(lambda x: 255 if x > 40 else 0).getbbox()
pad = 60
img.crop((bb[0] - pad, bb[1] - pad, bb[2] + pad, bb[3] + pad)).save(out)
print(out, bb)
