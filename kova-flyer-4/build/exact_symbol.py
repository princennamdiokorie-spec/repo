"""Replace the AI-redrawn symbol in GRAND (refined title) with the exact Kova symbol.

The symbol is coloured with the refined title letters' own chrome (sampled from
G and R), sized to their cap height and set on their baseline. The old symbol is
removed from layer-title-refined.png. Output: layer-title-refined.png (updated),
layer-symbol.png.
"""
import cv2
import numpy as np
from PIL import Image, ImageFilter

ref = cv2.imread('../flyer-gpt-refined.png')
title = cv2.imread('layer-title-refined.png', cv2.IMREAD_UNCHANGED)
h, w = ref.shape[:2]
g = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)

# cap height of GRAND in the refined flyer, measured on the R and D stems
def stem(x0, x1):                                  # first unbroken run only (stops above OPENING)
    on = (g[100:460, x0:x1] > 140).mean(1) > 0.5
    top = int(np.argmax(on)); end = top
    while end + 1 < len(on) and (on[end + 1] or on[end + 2: end + 6].any()):
        end += 1
    return top + 100, end + 100
(t1, b1), (t2, b2) = stem(480, 520), stem(1300, 1340)
cap_top, baseline = min(t1, t2), max(b1, b2)
# the old symbol sits between R and N: find that gap's bright extent
gap = g[cap_top - 30:baseline + 20, 690:1030] > 110
cols = np.where(gap.mean(0) > 0.02)[0] + 690
xs = cols
print('cap', cap_top, baseline, 'old symbol x', xs.min(), xs.max())
cx = (xs.min() + xs.max()) // 2

# remove the old symbol (and its glow) from the title layer
a = title[..., 3].astype(float)
box = np.zeros((h, w), np.uint8); box[cap_top - 45:baseline + 30, xs.min() - 12:xs.max() + 12] = 255
a *= 1 - cv2.GaussianBlur(box, (0, 0), 4) / 255
title[..., 3] = a.astype(np.uint8)
cv2.imwrite('layer-title-refined.png', title)

# chrome palette from G and R
reg = ref[cap_top:baseline, 240:670].reshape(-1, 3).astype(float)
lum = reg.mean(1); keep = lum > 40; reg, lum = reg[keep], lum[keep]
lut = np.full((256, 3), np.nan)
for v in range(256):
    sel = np.abs(lum - v) < 4
    if sel.sum() > 20: lut[v] = reg[sel].mean(0)
idx = np.arange(256); ok = ~np.isnan(lut[:, 0])
for c in range(3): lut[:, c] = np.interp(idx, idx[ok], lut[ok, c])
srt = np.sort(lum)

sym = Image.open('kova-symbol.png').convert('RGBA')
sh = baseline - cap_top; sw = round(sym.width * sh / sym.height)
s = np.asarray(sym.resize((sw, sh), Image.LANCZOS)).astype(float)
al = s[..., 3] / 255; sl = s[..., :3].mean(2); inside = al > .5
rank = np.searchsorted(np.sort(sl[inside]), sl) / inside.sum()
col = lut[np.interp(rank.clip(0, 1), np.linspace(0, 1, len(srt)), srt).clip(0, 255).astype(int)]
symimg = Image.fromarray(np.dstack([col[..., ::-1], al * 255]).clip(0, 255).astype(np.uint8), 'RGBA')

pad = 40
layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
halo = Image.new('RGBA', (sw, sh), (70, 160, 255, 0)); halo.putalpha(symimg.getchannel('A'))
glow = Image.new('RGBA', (w, h), (0, 0, 0, 0)); glow.alpha_composite(halo, (cx - sw // 2, cap_top))
glow = glow.filter(ImageFilter.GaussianBlur(10))
rim = Image.new('RGBA', (sw, sh), (210, 235, 255, 0))
rim.putalpha(symimg.getchannel('A').filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(1)))
layer.alpha_composite(glow); layer.alpha_composite(glow)
layer.alpha_composite(symimg, (cx - sw // 2, cap_top)); layer.alpha_composite(rim, (cx - sw // 2, cap_top))
layer.save('layer-symbol.png')
print('symbol', sw, 'x', sh, 'at', cx)
