"""Plaque flyer 4K: replace the old plaque with the new 'KOVA LIFESTYLE / GRAND OPENING' plaque.
Old plaque (BiRefNet mask, crop at y=650) is removed and the background behind it
rebuilt; the new plaque (AI-upscaled, solid alpha) is centred on the old one's centre.
Output: plaque-flyer-v2-base.png (no presents line)."""
import cv2
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

fl = cv2.imread('plaque-flyer-namefix.png').astype(np.float32); h, w = fl.shape[:2]
old = np.zeros((h, w), np.float32)
m = cv2.imread('oldplaque-mask.png', 0).astype(np.float32) / 255
old[650:650 + m.shape[0], :m.shape[1]] = m
old = ndi.binary_fill_holes(old > 0.3).astype(np.float32)

NEW_W, NEW_H = 2421, 1700
CX, CY = 1535, 1586                        # old plaque centre

# rebuild background behind the old plaque: inpaint at 1/4 size, upsample, add grain
q = 4
small = cv2.resize(fl, (w // q, h // q), interpolation=cv2.INTER_AREA).clip(0, 255).astype(np.uint8)
hole = cv2.dilate((cv2.resize(old, (w // q, h // q)) > 0.2).astype(np.uint8) * 255, np.ones((5, 5), np.uint8))
filled = cv2.inpaint(small, hole, 15, cv2.INPAINT_TELEA)
filled = cv2.resize(cv2.GaussianBlur(filled, (0, 0), 2), (w, h), interpolation=cv2.INTER_CUBIC).astype(np.float32)
rng = np.random.default_rng(2)
filled += cv2.GaussianBlur(rng.normal(0, 5, (h, w)).astype(np.float32), (0, 0), 1)[..., None]
hm = cv2.GaussianBlur(cv2.dilate(old.astype(np.uint8), np.ones((21, 21))).astype(np.float32), (0, 0), 6)[..., None]
bg = fl * (1 - hm) + filled * hm

rgb = np.asarray(Image.open('plaque-v2-up.png').convert('RGB'))[..., ::-1].astype(np.float32)
a = np.asarray(Image.open('plaque-v2.png').getchannel('A').resize((NEW_W, NEW_H), Image.LANCZOS)).astype(np.float32) / 255
x0, y0 = CX - NEW_W // 2, CY - NEW_H // 2
# soft drop shadow so it sits in the scene like the old one
sh = np.zeros((h, w), np.float32); sh[y0:y0 + NEW_H, x0:x0 + NEW_W] = a
sh = cv2.GaussianBlur(np.roll(sh, 18, 0), (0, 0), 22)[..., None] * 0.55
out = bg * (1 - sh)
reg = out[y0:y0 + NEW_H, x0:x0 + NEW_W]
out[y0:y0 + NEW_H, x0:x0 + NEW_W] = reg * (1 - a[..., None]) + rgb * a[..., None]
cv2.imwrite('plaque-flyer-v2-base.png', out.clip(0, 255).astype(np.uint8))
print('placed at', x0, y0, NEW_W, NEW_H)
