"""Cut text/title layers from base4.png and prepare the clean GPT scene.

Outputs (assets/): scene-prepped.png, layer-title.png, layer-date.png,
layer-doors.png, layer-script.png, layer-insta.png, layer-address.png
"""
import cv2
import numpy as np

base = cv2.imread('base4.png')
h, w = base.shape[:2]
L = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY).astype(float)
B, G, R = [base[..., i].astype(float) for i in range(3)]


def save(name, alpha, box):
    x0, y0, x1, y1 = box
    a = np.zeros((h, w)); a[y0:y1, x0:x1] = alpha[y0:y1, x0:x1]
    rgba = np.dstack([base, (a * 255).clip(0, 255)]).astype(np.uint8)
    cv2.imwrite(f'layer-{name}.png', rgba)


def text_alpha(thresh, grow, lo, span):
    core = (L > thresh).astype(np.uint8) * 255
    zone = cv2.GaussianBlur(cv2.dilate(core, np.ones((grow, grow), np.uint8)), (0, 0), grow / 3) / 255
    return np.clip((L - lo) / span, 0, 1) * zone


# title (big chrome letters + logo A): large bright components plus their glow
box = (150, 100, 1600, 665)
m = np.zeros((h, w), np.uint8); x0, y0, x1, y1 = box
m[y0:y1, x0:x1] = (L[y0:y1, x0:x1] > 85).astype(np.uint8) * 255
m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(m)
keep = np.isin(lab, [i for i in range(1, n) if st[i, 4] > 400]).astype(np.uint8) * 255
zone = cv2.GaussianBlur(cv2.dilate(keep, np.ones((25, 25), np.uint8)), (0, 0), 8) / 255
save('title', np.maximum(keep / 255.0, np.clip((L - 30) / 90, 0, 1) * zone), box)

save('date', text_alpha(150, 15, 35, 120), (130, 870, 530, 1160))
blue_txt = np.clip((B - 150) / 70, 0, 1) * np.clip((B - R - 60) / 60, 0, 1)   # the blue '10PM'
save('doors', np.maximum(text_alpha(150, 11, 40, 130), blue_txt), (1360, 880, 1600, 1030))
save('insta', text_alpha(170, 7, 50, 140), (260, 2075, 1480, 2112))
save('address', text_alpha(170, 7, 50, 140), (400, 2215, 1350, 2265))

# neon script: blue-dominant pixels only (skin and sequins are excluded)
blue = np.clip((B - np.maximum(R, G * 0.55) - 40) / 90, 0, 1) * np.clip((B - 110) / 80, 0, 1)
save('script', blue, (480, 1650, 1280, 2010))

# scene: fade the sparkler tops out below the KOVA LIFESTYLE line (row ~750)
sc = cv2.imread('scene-clean.png').astype(float)
Ls = sc.mean(2)
keepw = (Ls < 140).astype(float)
num = cv2.GaussianBlur(sc * keepw[..., None], (0, 0), 14); den = cv2.GaussianBlur(keepw, (0, 0), 14)[..., None] + 1e-6
calm = num / den
ys = np.arange(h)[:, None]
ramp = np.clip((880 - ys) / 120, 0, 1)            # sparks fade out by row 760, below the KOVA LIFESTYLE line
cols = np.zeros((1, w))
for x0, x1 in [(360, 580), (780, 980), (1150, 1420)]:
    cols[0, x0:x1] = 1
cols = cv2.GaussianBlur(cols, (0, 0), 25)
fade = (ramp * cols)[..., None]
cv2.imwrite('scene-prepped.png', (sc * (1 - fade) + calm * fade).clip(0, 255).astype(np.uint8))
print('ok')
