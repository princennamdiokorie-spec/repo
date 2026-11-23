"""Marquee 4K: replace the old sign with the new 'KOVA LIFESTYLE / Grand / OPENING' sign.
bg.png (from edit_marquee.py) already has the old sign removed; the new sign goes on,
then her hair (hair.png) in front, then compose adds the presents line.
Output: plaque.png is replaced by the new sign layer (sign-layer.png)."""
import cv2
import numpy as np
from PIL import Image

W, H = 2284, 1480
BOTTOM, CX = 1765, 1536            # bottom edge where the old sign's was, so her hair overlaps it the same way
h, w = 3840, 3072
rgb = np.asarray(Image.open('sign-v2-up.png').convert('RGB'))[..., ::-1]
a = np.asarray(Image.open('sign-v2.png').getchannel('A').resize((W, H), Image.LANCZOS))
x0, y0 = CX - W // 2, BOTTOM - H
lay = np.zeros((h, w, 4), np.uint8)
lay[y0:y0 + H, x0:x0 + W, :3] = rgb; lay[y0:y0 + H, x0:x0 + W, 3] = a
cv2.imwrite('sign-layer.png', lay)
print('sign at', x0, y0, W, H)
