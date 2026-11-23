"""Final composite of the marquee 4K: background, shrunk plaque, hair in front, presents line.
Usage: python3 compose.py  (run edit_marquee.py first; render _presents.png with render_text.js)"""
import cv2
import numpy as np
from PIL import Image

CAP = 38              # presents-line cap height (px at 4K); was 50, reduced on request
CENTRE_Y = 185        # vertical centre of the line's caps, kept where it was

bg = cv2.imread('bg.png').astype(np.float32); h, w = bg.shape[:2]
def over(img, layer):
    a = layer[..., 3:4].astype(np.float32) / 255
    return img * (1 - a) + layer[..., :3].astype(np.float32) * a
out = over(bg, cv2.imread('plaque.png', cv2.IMREAD_UNCHANGED))
out = over(out, cv2.imread('hair.png', cv2.IMREAD_UNCHANGED))
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
out = out * (1 - glow) + np.array([255, 140, 40]) * glow
out = over(out, lay.clip(0, 255))
cv2.imwrite('../grand-opening-marquee-4k-kova-lifestyle.png', out.clip(0, 255).astype(np.uint8))
print('presents width', crop.width, 'cap', CAP)
