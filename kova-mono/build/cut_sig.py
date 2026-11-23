"""Lift the chrome GRAND OPENING lettering off its black-with-grey-glow background.
Background estimate = large median of luminance (the smooth glow cloud). Letter pixels
differ from it either way (bright chrome or dark reflections/outlines). Small enclosed
gaps inside strokes are filled; large counters (inside O, D...) stay open. Inside the mask
the original pixels are kept whole; the generated grey cloud is replaced by a tight halo.
Usage: cut_sig.py <src> <out>"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

src, out = sys.argv[1], sys.argv[2]
im = np.asarray(Image.open(src).convert('RGB')).astype(float) / 255
L = im.mean(2); h, w = L.shape
q = 4
small = L[::q, ::q]
bg = ndi.median_filter(small, size=31)
bg = ndi.zoom(ndi.gaussian_filter(bg, 2), q, order=1)[:h, :w]
diff = np.abs(L - bg)
m = diff > .14
m = ndi.binary_closing(m, np.ones((5, 5)))
lab, n = ndi.label(m); sz = ndi.sum(m, lab, range(1, n + 1))
m = np.isin(lab, 1 + np.where(sz > 400)[0])
holes = ndi.binary_fill_holes(m) & ~m
hl, hn = ndi.label(holes); hs = ndi.sum(holes, hl, range(1, hn + 1))
m |= np.isin(hl, 1 + np.where(hs < 5000)[0])                 # fill gaps inside strokes, keep counters open
mf = np.clip(ndi.gaussian_filter(m.astype(float), .9) * 1.4, 0, 1)
halo = np.clip(ndi.gaussian_filter(m.astype(float), 16) * .5, 0, 1) * (1 - mf)
a = np.maximum(mf, halo)
# remove the glow's grey from inside the letters too: flat patches of glow caught at stroke edges
# drop to black (invisible on the black flyer) while bright chrome keeps its range
# near the outer edge of the letters (within EDGE px), pixels that match the glow's grey are
# leftover glow, not chrome: fade them to transparent. Deeper inside, strokes stay solid.
dist = ndi.distance_transform_edt(m)
# leftover glow is smooth, untextured mid-grey; chrome always has strong local contrast
mu = ndi.uniform_filter(L, 9); sd = np.sqrt(np.clip(ndi.uniform_filter(L * L, 9) - mu * mu, 0, None))
smooth_grey = (sd < .045) & (L > .2) & (L < .82)
blob = ndi.binary_opening(smooth_grey, np.ones((3, 3)))
drop = blob & (dist < 26)
drop = ndi.binary_dilation(drop, np.ones((3, 3))) & m
edge_keep = np.where(drop, 0.0, 1.0)
edge_keep = ndi.gaussian_filter(edge_keep, .8)
mf = mf * edge_keep
halo = np.clip(ndi.gaussian_filter(mf, 16) * .5, 0, 1) * (1 - mf)
a = np.maximum(mf, halo)
rgb = (im * mf[..., None] + 1.0 * halo[..., None]) / np.maximum(a[..., None], 1e-6)
img = Image.fromarray(np.dstack([rgb.clip(0, 1) * 255, a * 255]).astype(np.uint8), 'RGBA')
bb = Image.fromarray((mf * 255).astype(np.uint8)).point(lambda v: 255 if v > 40 else 0).getbbox()
pad = 50
img.crop((bb[0] - pad, bb[1] - pad, bb[2] + pad, bb[3] + pad)).save(out)
print(out, 'letters bbox', bb)
