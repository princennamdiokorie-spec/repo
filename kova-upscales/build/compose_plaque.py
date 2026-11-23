"""Plaque flyer 4K: swap the nameplate back to the original 'OF KOVA LIFESTYLE'
(our title-B plaque, registered onto the flyer and AI-upscaled; see plaque_M.npy and
np-crop-x4.png) and add 'KOVA LIFESTYLE PRESENTS' at the top.
Input: plaque-flyer-namefix.png, _presents.png. Output: ../grand-opening-plaque-4k-kova-lifestyle.png"""
import cv2
import numpy as np
from PIL import Image

CAP, CENTRE_Y = 38, 110       # same size as on the marquee flyer; above the logo, clear of the neon line

base = cv2.imread('plaque-flyer-namefix.png').astype(np.float32); h, w = base.shape[:2]
t = np.asarray(Image.open('_presents.png').convert('RGBA')); a = t[..., 3]
wt = (t[..., :3].min(2) > 200) & (a > 200); r = wt.sum(1)
ys = np.where(r > 0.12 * r.max())[0]; xs = np.where((a > 128).sum(0) > 0)[0]
s = CAP / (ys.max() - ys.min()); pad = 20
crop = Image.fromarray(t).crop((xs.min() - pad, ys.min() - pad, xs.max() + pad, ys.max() + pad))
crop = crop.resize((round(crop.width * s), round(crop.height * s)), Image.LANCZOS)
px = round(w / 2 - crop.width / 2); py = round(CENTRE_Y - CAP / 2 - pad * s)
lay = np.zeros((h, w, 4), np.float32); arr = np.asarray(crop).astype(np.float32)
lay[py:py + arr.shape[0], px:px + arr.shape[1]] = arr
glow = cv2.GaussianBlur(lay[..., 3], (0, 0), 8)[..., None] / 255 * 0.45
out = base * (1 - glow) + np.array([255, 140, 40]) * glow
al = lay[..., 3:4] / 255; out = out * (1 - al) + lay[..., :3] * al
cv2.imwrite('../grand-opening-plaque-4k-kova-lifestyle.png', out.clip(0, 255).astype(np.uint8))
print('ok')
