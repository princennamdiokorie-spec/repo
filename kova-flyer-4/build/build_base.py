"""Rebuild the concept-4 base from flyer-clean.png (AI flyer with old subtitle and emblem removed).

Steps: erase the top line, the AI bottle emblems and the bottom 'Kova Night Club'
line; lift the GRAND OPENING title up by SHIFT px; then composite the Kova symbol,
re-coloured with the title letters' own chrome palette and sized to their cap height.
"""
import cv2
import numpy as np
from PIL import Image, ImageFilter

SHIFT = 120
CAP_TOP, BASELINE = 277, 493          # GRAND caps in flyer-clean.png
GAP_CX = 857                          # centre of the gap between R and N
LABELS = [(645, 1478), (893, 1308), (1139, 1507)]

im = cv2.imread('flyer-clean.png'); h, w = im.shape[:2]
g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# chrome palette from the G and R: mean colour per luminance level
reg = im[CAP_TOP:BASELINE, 240:670].reshape(-1, 3).astype(float)
lum = reg.mean(1); keep = lum > 40; reg, lum = reg[keep], lum[keep]
lut = np.zeros((256, 3))
for v in range(256):
    sel = np.abs(lum - v) < 4
    lut[v] = reg[sel].mean(0) if sel.sum() > 20 else np.nan
idx = np.arange(256); good = ~np.isnan(lut[:, 0])
for c in range(3):
    lut[:, c] = np.interp(idx, idx[good], lut[good, c])
letter_lum_sorted = np.sort(lum)

# 1) erase top line, bottle emblems, bottom serif name
m = np.zeros((h, w), np.uint8)
m[41:81, 413:1331] = 255
m[2022:2071, 430:1312] = 255                  # 'FOR VIP AND INFO CALL ...' line
for cx, cy in LABELS:
    r = im[cy-62:cy+56, cx-75:cx+75]; b = (r.max(2) > 55).astype(np.uint8) * 255
    m[cy-62:cy+56, cx-75:cx+75] |= cv2.dilate(b, np.ones((9, 9), np.uint8))
bot = g[2120:2215, 480:1270] > 120
ys, xs = np.where(bot)
m[2120 + ys.min() - 10:2120 + ys.max() + 12, 480 + xs.min() - 14:480 + xs.max() + 14] = 255
im = cv2.inpaint(im, m, 7, cv2.INPAINT_TELEA)
g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 2) lift the title
Y0, Y1, X0, X1 = 200, 758, 150, 1600
tm = np.zeros((h, w), np.uint8); tm[Y0:Y1, X0:X1] = (g[Y0:Y1, X0:X1] > 85).astype(np.uint8) * 255
tm = cv2.morphologyEx(tm, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(tm)
keepm = np.zeros_like(tm)
for i in range(1, n):
    if st[i, 4] > 400:
        keepm[lab == i] = 255
mask = cv2.dilate(keepm, np.ones((13, 13), np.uint8))
alpha = cv2.GaussianBlur(mask, (0, 0), 3).astype(float) / 255
plate = cv2.inpaint(im, cv2.dilate(mask, np.ones((9, 9), np.uint8)), 9, cv2.INPAINT_TELEA)
mm = cv2.GaussianBlur(mask, (0, 0), 8)[..., None] / 255
plate = plate * (1 - mm) + cv2.GaussianBlur(plate, (0, 0), 16) * mm
lay = np.zeros_like(im, dtype=float); la = np.zeros((h, w))
lay[:h-SHIFT] = im[SHIFT:]; la[:h-SHIFT] = alpha[SHIFT:]
base = (plate * (1 - la[..., None]) + lay * la[..., None]).clip(0, 255).astype(np.uint8)

# 2b) sparkler fragments that travelled up with the title: small bright specks in
#     three boxes under OPENING (P, middle N/I, N next to G). Letters are large
#     components, sparks are small, so remove only the small ones.
bg = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
spark = np.zeros((h, w), np.uint8)
for x0, x1, y0, y1 in [(400, 500, 560, 660), (830, 940, 520, 660), (1270, 1380, 560, 660)]:
    sub = (bg[y0:y1, x0:x1] > 110).astype(np.uint8)
    n2, l2, s2, _ = cv2.connectedComponentsWithStats(sub, connectivity=8)
    for i in range(1, n2):
        if s2[i, 4] < 350:
            spark[y0:y1, x0:x1][l2 == i] = 255
# the middle burst touches the N's diagonal: take everything bright below that stroke
yy, xx = np.mgrid[540:660, 855:935]
below_diag = (yy - (500 + (xx - 860) * 1.1)) > 16
spark[540:660, 855:935] |= ((bg[540:660, 855:935] > 70) & below_diag).astype(np.uint8) * 255
sm = cv2.dilate(spark, np.ones((7, 7), np.uint8)).astype(float) / 255
keepw = 1 - sm                                           # normalised blur: fill from surroundings only
num = cv2.GaussianBlur(base.astype(float) * keepw[..., None], (0, 0), 9)
den = cv2.GaussianBlur(keepw, (0, 0), 9)[..., None] + 1e-6
fill = num / den
soft = cv2.GaussianBlur(sm, (0, 0), 2)[..., None]
base = (base * (1 - soft) + fill * soft).clip(0, 255).astype(np.uint8)

# 2c) sparkler tips: the streams were cut flat where the old title sat (~row 760).
#     Lighten-blend a copy of each stream shifted up, fading to nothing at the top.
TIP_SHIFT, CUT = 34, 760
for x0, x1 in [(400, 540), (840, 940), (1270, 1400)]:
    src = base[CUT + 5:CUT + 5 + 90, x0:x1].astype(float)
    ramp = np.linspace(0, 1, src.shape[0])[:, None, None] ** 1.5
    dst = base[CUT + 5 - TIP_SHIFT:CUT + 5 - TIP_SHIFT + 90, x0:x1].astype(float)
    sparkw = cv2.GaussianBlur(((src.max(2) > 170).astype(float)), (0, 0), 1.5)[..., None]  # spark pixels only
    base[CUT + 5 - TIP_SHIFT:CUT + 5 - TIP_SHIFT + 90, x0:x1] = (dst + (src - dst).clip(0) * ramp * sparkw).clip(0, 255).astype(np.uint8)

# 3) chrome symbol matched to the letters
sym = np.asarray(Image.open('kova-symbol.png').convert('RGBA')).astype(float)
cap = BASELINE - CAP_TOP
sh = cap; sw = round(sym.shape[1] * sh / sym.shape[0])
sym = np.asarray(Image.fromarray(sym.astype(np.uint8), 'RGBA').resize((sw, sh), Image.LANCZOS)).astype(float)
a = sym[..., 3] / 255; slum = sym[..., :3].mean(2)
inside = a > 0.5
ranks = np.searchsorted(np.sort(slum[inside]), slum, side='left') / max(inside.sum(), 1)
tgt = np.interp(ranks.clip(0, 1), np.linspace(0, 1, len(letter_lum_sorted)), letter_lum_sorted)
rgb_bgr = lut[tgt.clip(0, 255).astype(int)]
symc = np.dstack([rgb_bgr[..., ::-1], a * 255]).clip(0, 255).astype(np.uint8)
sym_img = Image.fromarray(symc, 'RGBA')
pad = 40
canvas = Image.new('RGBA', (sw + 2 * pad, sh + 2 * pad), (0, 0, 0, 0))
glow = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
halo = Image.new('RGBA', (sw, sh), (90, 170, 255, 0)); halo.putalpha(sym_img.getchannel('A'))
glow.alpha_composite(halo, (pad, pad)); glow = glow.filter(ImageFilter.GaussianBlur(12))
rim = Image.new('RGBA', (sw, sh), (200, 230, 255, 0))
edge = sym_img.getchannel('A').filter(ImageFilter.FIND_EDGES).filter(ImageFilter.GaussianBlur(1))
rim.putalpha(edge)
canvas.alpha_composite(glow); canvas.alpha_composite(glow)
canvas.alpha_composite(sym_img, (pad, pad)); canvas.alpha_composite(rim, (pad, pad))

out = Image.fromarray(cv2.cvtColor(base, cv2.COLOR_BGR2RGB)).convert('RGBA')
out.alpha_composite(canvas, (GAP_CX - sw // 2 - pad, CAP_TOP - SHIFT - pad))
out.convert('RGB').save('base4.png')
print('symbol', sw, 'x', sh)
