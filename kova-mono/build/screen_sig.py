"""Prepare a chrome title on black for SCREEN blending onto a black flyer.
Everything at or below the local glow level is pushed to black (screen ignores black),
chrome highlights are kept, and a soft halo is added back from the bright parts.
No cut-out mask, so no patches, holes or fringes. Usage: screen_sig.py <src> <out>"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

src, out = sys.argv[1], sys.argv[2]
im = np.asarray(Image.open(src).convert('RGB')).astype(float) / 255
L = im.mean(2); h, w = L.shape
q = 4
bg = ndi.median_filter(L[::q, ::q], size=31)
bg = ndi.zoom(ndi.gaussian_filter(bg, 2), q, order=1)[:h, :w]
t = np.clip(bg * .82, 0, .9)                              # local black point: below the glow, so chrome keeps its body; leftover glow stays soft
v = np.clip((L - t) / (1 - t), 0, 1) ** 1.05
rgb = im * (v / np.maximum(L, 1e-4))[..., None]
halo = ndi.gaussian_filter(v, 14) * .22                    # tight soft glow from the chrome itself
rgb = 1 - (1 - rgb) * (1 - halo[..., None])                # screen the halo in
# fade whatever glow is left to black away from the letters, so the image has no box edge
near = ndi.gaussian_filter((v > .25).astype(float), 30)
rgb = rgb * np.clip(near * 3.2, 0, 1)[..., None]
img = Image.fromarray((rgb.clip(0, 1) * 255).astype(np.uint8))
bb = img.convert('L').point(lambda x: 255 if x > 40 else 0).getbbox()
pad = 60
img.crop((bb[0] - pad, bb[1] - pad, bb[2] + pad, bb[3] + pad)).save(out)
print(out, bb)
