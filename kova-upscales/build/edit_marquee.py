"""Marquee 4K flyer edits, all in code.

1. Nameplate: replace "OF KOVA NIGHT CLUB" with "OF KOVA LIFESTYLE" (new
   lettering rendered separately as nameplate-text.png, matched to the original).
2. Shrink the plaque about its bottom-centre (SCALE) so its top comes down (BiRefNet plaque mask), keep her
   visible hair in front of it, and fill the background it uncovers.
3. Fix the venue-line typo "LIFSTYLE" -> "LIFESTYLE" (rendered as venue-text.png).
"Presents" line and the final composite are done in compose.html.

Inputs in build/: plaque-mask (crop at 380,0), woman-mask-crop (crop at 800,1550),
nameplate-text.png, venue-text.png. Outputs: build/bg.png, build/plaque.png, build/hair.png
"""
import cv2
import numpy as np

SCALE = 0.905                     # shrink about the sign's bottom-centre: top comes down ~155px, words stay clear of her hair
ANCHOR = (1547.0, 1745.0)
SRC = '../grand-opening-marquee-4k-orig.png'

im = cv2.imread(SRC).astype(np.float32)
h, w = im.shape[:2]


def place(mask_path, x0, y0):
    m = cv2.imread(mask_path, 0).astype(np.float32) / 255
    full = np.zeros((h, w), np.float32)
    full[y0:y0 + m.shape[0], x0:x0 + m.shape[1]] = m
    return full


plaque = place('plaque-mask.png', 380, 0)
woman = place('woman-mask-crop.png', 800, 1550)
hair = woman * (1 - plaque)                        # only the hair that is already in front of the sign
hair[2300:] = 0                                    # the hair layer is only needed near the sign


def erase_and_fill(img, box, white_thresh, extrude, sig, blue=False):
    """Remove light lettering (plus its dark extrusion) inside box, refill from the plate face."""
    x0, y0, x1, y1 = box
    sub = img[y0:y1, x0:x1]
    hsv = cv2.cvtColor(sub.clip(0, 255).astype(np.uint8), cv2.COLOR_BGR2HSV)
    txt = ((hsv[..., 2] > white_thresh) & (hsv[..., 1] < 70))
    if blue:                                       # also the light-blue separator bar
        txt |= (hsv[..., 2] > 150) & (sub[..., 0] > sub[..., 2] + 60)
    txt = txt.astype(np.uint8)
    k = np.ones((extrude * 2 + 1, extrude * 2 + 1), np.uint8)
    m = cv2.dilate(txt, k)
    m = np.maximum(m, np.roll(np.roll(m, extrude, 0), extrude // 2, 1))   # extrusion sits below-right
    keep = 1.0 - m.astype(np.float32)
    num = cv2.GaussianBlur(sub * keep[..., None], (0, 0), sig[0], sigmaY=sig[1])
    den = cv2.GaussianBlur(keep, (0, 0), sig[0], sigmaY=sig[1])[..., None] + 1e-6
    a = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 1.5)[..., None]
    img[y0:y1, x0:x1] = sub * (1 - a) + (num / den) * a


def overlay(img, rgba_path, x, y):
    t = cv2.imread(rgba_path, cv2.IMREAD_UNCHANGED).astype(np.float32)
    a = t[..., 3:4] / 255
    th, tw = t.shape[:2]
    img[y:y + th, x:x + tw] = img[y:y + th, x:x + tw] * (1 - a) + t[..., :3] * a


# 1) nameplate wording
erase_and_fill(im, (660, 1388, 2440, 1566), 195, 9, (70, 5))
nx, ny = [int(v) for v in open('nameplate-text.pos').read().split()]
overlay(im, 'nameplate-text.png', nx, ny)

# 3) venue typo (bottom line, not part of the plaque)
erase_and_fill(im, (380, 3530, 2720, 3640), 170, 4, (60, 6), blue=True)
vx, vy = [int(v) for v in open('venue-text.pos').read().split()]
overlay(im, 'venue-text.png', vx, vy)

# 2) background with the plaque removed: inpaint at 1/4 size (large hole), add back grain
small = cv2.resize(im, (w // 4, h // 4), interpolation=cv2.INTER_AREA).clip(0, 255).astype(np.uint8)
hole = (cv2.resize(plaque, (w // 4, h // 4)) > 0.15).astype(np.uint8) * 255
hole = cv2.dilate(hole, np.ones((5, 5), np.uint8))
filled = cv2.inpaint(small, hole, 12, cv2.INPAINT_TELEA)
filled = cv2.GaussianBlur(filled, (0, 0), 3)
filled = cv2.resize(filled, (w, h), interpolation=cv2.INTER_CUBIC).astype(np.float32)
rng = np.random.default_rng(1)
grain = cv2.GaussianBlur(rng.normal(0, 6, (h, w)).astype(np.float32), (0, 0), 1.2)[..., None]
hole_full = cv2.GaussianBlur(cv2.dilate((plaque > 0.15).astype(np.uint8), np.ones((15, 15))).astype(np.float32), (0, 0), 6)[..., None]
bg = im * (1 - hole_full) + (filled + grain) * hole_full

# moved plaque layer and hair layer (premultiplied-safe: store straight colour + alpha)
ax, ay = ANCHOR
M = np.float32([[SCALE, 0, ax * (1 - SCALE)], [0, SCALE, ay * (1 - SCALE)]])
src = np.dstack([im, plaque * 255])
plq = cv2.warpAffine(src, M, (w, h), flags=cv2.INTER_CUBIC, borderValue=0)
hr = np.dstack([im, hair * 255])

cv2.imwrite('bg.png', bg.clip(0, 255).astype(np.uint8))
cv2.imwrite('plaque.png', plq.clip(0, 255).astype(np.uint8))
cv2.imwrite('hair.png', hr.clip(0, 255).astype(np.uint8))
print('ok')
