"""Plaque flyer 4K: move the Kova logo up by SHIFT px (client: more space for the
presents line). The logo is located by template match (logo-pos.txt), its pixels
(with glow) are cut with a soft mask from the real logo's alpha, the hole is
refilled from the background, and the same pixels are laid back SHIFT px higher.
Input: plaque-flyer-namefix.png. Output: plaque-flyer-logoup.png"""
import cv2
import numpy as np

SHIFT = 80
im = cv2.imread('plaque-flyer-namefix.png').astype(np.float32); h, w = im.shape[:2]
x, y, lw, lh = [int(v) for v in open('logo-pos.txt').read().split()]
logo = cv2.imread('../../kova-flyer/logo/kova-logo-transparent.png', cv2.IMREAD_UNCHANGED)
a = cv2.resize(logo[..., 3], (lw, lh), interpolation=cv2.INTER_AREA).astype(np.float32) / 255
m = np.zeros((h, w), np.float32); m[y:y + lh, x:x + lw] = a
mask = cv2.GaussianBlur(cv2.dilate((m > 0.05).astype(np.uint8), np.ones((31, 31))).astype(np.float32), (0, 0), 6)

# refill the background under the old logo (quarter-size inpaint keeps it smooth)
q = 4
small = cv2.resize(im, (w // q, h // q), interpolation=cv2.INTER_AREA).clip(0, 255).astype(np.uint8)
hole = (cv2.resize(mask, (w // q, h // q)) > 0.05).astype(np.uint8) * 255
filled = cv2.inpaint(small, cv2.dilate(hole, np.ones((3, 3), np.uint8)), 10, cv2.INPAINT_TELEA)
filled = cv2.resize(cv2.GaussianBlur(filled, (0, 0), 1.5), (w, h), interpolation=cv2.INTER_CUBIC).astype(np.float32)
rng = np.random.default_rng(3)
filled += cv2.GaussianBlur(rng.normal(0, 4, (h, w)).astype(np.float32), (0, 0), 1)[..., None]
bg = im * (1 - mask[..., None]) + filled * mask[..., None]

# lay the original logo pixels back, SHIFT px higher
moved = np.zeros_like(im); moved[:h - SHIFT] = im[SHIFT:]
mm = np.zeros((h, w), np.float32); mm[:h - SHIFT] = mask[SHIFT:]
out = bg * (1 - mm[..., None]) + moved * mm[..., None]
cv2.imwrite('plaque-flyer-logoup.png', out.clip(0, 255).astype(np.uint8))
print('logo now spans y', y - SHIFT, y + lh - SHIFT)
