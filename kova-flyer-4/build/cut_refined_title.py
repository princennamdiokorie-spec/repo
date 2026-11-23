"""Cut only the GRAND OPENING title (with its logo A and glow) out of the GPT-refined flyer.

The refined title sits in the same place as ours, so our own title mask (from
base4.png) limits the cut: stage lights in the busier refined background are
never picked up. Output: layer-title-refined.png (full-size RGBA).
"""
import cv2
import numpy as np

ref = cv2.imread('../flyer-gpt-refined.png')
ours = cv2.imread('base4.png')
h, w = ref.shape[:2]
x0, y0, x1, y1 = 150, 100, 1600, 650          # title rows only: stops above "KOVA LIFESTYLE"

def letters(img):
    L = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    m = np.zeros((h, w), np.uint8)
    m[y0:y1, x0:x1] = (L[y0:y1, x0:x1] > 85).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    return np.isin(lab, [i for i in range(1, n) if st[i, 4] > 400]).astype(np.uint8) * 255, L

ours_keep, _ = letters(ours)
allowed = cv2.dilate(ours_keep, np.ones((41, 41), np.uint8))       # where a title letter can be
ref_keep, Lr = letters(ref)
ref_keep &= allowed
zone = cv2.GaussianBlur(cv2.dilate(ref_keep, np.ones((27, 27), np.uint8)), (0, 0), 8) / 255
alpha = np.maximum(ref_keep / 255.0, np.clip((Lr - 35) / 90, 0, 1) * zone)
alpha[:y0] = 0; alpha[y1:] = 0
cv2.imwrite('layer-title-refined.png', np.dstack([ref, (alpha * 255).astype(np.uint8)]))
print('title pixels', int((alpha > .5).sum()))
