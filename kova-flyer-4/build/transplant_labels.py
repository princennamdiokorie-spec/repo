"""Transfer the real Don Julio labels from the Alumni reference onto our three bottles.

Each label is matched by its centroid, principal axis and extents (reference cream
label -> our navy label), warped with that similarity-plus-scale transform, clipped
to our label's own mask (so fingers in front stay in front), white-balanced away
from the reference's magenta light, and given our scene's blue edge light.
Output: scene-donjulio.png
"""
import cv2
import numpy as np

ref = cv2.imread('alumni-ref.jpg')
sc = cv2.imread('scene-prepped.png')
raw = cv2.imread('scene-clean.png')


def comps(mask, min_area):
    n, lab, st, _ = cv2.connectedComponentsWithStats(mask)
    return [(lab == i) for i in range(1, n) if st[i, 4] > min_area]


def frame(m):
    ys, xs = np.nonzero(m); pts = np.c_[xs, ys].astype(float); c = pts.mean(0)
    evals, evecs = np.linalg.eigh(np.cov((pts - c).T))
    v = evecs[:, 1]                                   # long axis (labels are taller than wide)
    if v[1] < 0: v = -v
    u = np.array([v[1], -v[0]])
    pu, pv = (pts - c) @ u, (pts - c) @ v
    return c, u, v, np.percentile(pu, [2, 98]), np.percentile(pv, [2, 98])


hsv = cv2.cvtColor(ref, cv2.COLOR_BGR2HSV)
rm = ((hsv[..., 2] > 170) & (hsv[..., 1] < 90)).astype(np.uint8) * 255
rm[:820] = 0; rm[1130:] = 0; rm[:, :330] = 0; rm[:, 870:] = 0
rm = cv2.morphologyEx(rm, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
from scipy import ndimage as ndi
def hull(m):                                          # the label's full outer shape, red print included
    pts = cv2.convexHull(np.argwhere(m)[:, ::-1].astype(np.int32))
    out = np.zeros(m.shape, np.uint8); cv2.fillConvexPoly(out, pts, 1); return out.astype(bool)
refs = sorted((hull(m) for m in comps(rm, 5000)), key=lambda m: np.nonzero(m)[1].mean())

L = raw.max(2)
om = ((L < 70) & (raw[..., 0] > raw[..., 2] + 15)).astype(np.uint8) * 255
om[:1150] = 0; om[1650:] = 0; om[:, :450] = 0; om[:, 1300:] = 0
om = cv2.morphologyEx(om, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
om = cv2.morphologyEx(om, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
ours = sorted(comps(om, 8000), key=lambda m: np.nonzero(m)[1].mean())
assert len(refs) == 3 and len(ours) == 3, (len(refs), len(ours))

out = sc.astype(float)
h, w = sc.shape[:2]
# the reference's middle label is partly covered by a finger; all three are the same
# Don Julio Reposado label, so the unobstructed left one is used for every bottle
for rmask, omask in zip([refs[0]] * 3, ours):
    rc, ru, rv, rup, rvp = frame(rmask)
    oc, ou, ov, oup, ovp = frame(omask)
    su = (oup[1] - oup[0]) / (rup[1] - rup[0]); sv = (ovp[1] - ovp[0]) / (rvp[1] - rvp[0])
    # map ref point p: coords (a,b) in ref frame -> our frame scaled
    r_mid = rc + ru * rup.mean() + rv * rvp.mean(); o_mid = oc + ou * oup.mean() + ov * ovp.mean()
    FIT = 0.86                                        # shrink contents so nothing is clipped at the label edge
    A_ref = np.c_[ru, rv]; A_our = np.c_[ou * su * FIT, ov * sv * FIT]
    M = A_our @ np.linalg.inv(A_ref)                  # 2x2
    t = o_mid - M @ r_mid
    warp = cv2.warpAffine(ref, np.c_[M, t], (w, h), flags=cv2.INTER_CUBIC)
    wmask = cv2.warpAffine(rmask.astype(np.uint8) * 255, np.c_[M, t], (w, h), flags=cv2.INTER_LINEAR).astype(float) / 255
    # white balance: make the label's paper a neutral cream
    paper = warp[omask & (wmask > .9) & (warp.max(2) > 150)].reshape(-1, 3).astype(float)
    gain = np.array([186, 222, 238]) / np.median(paper, axis=0)   # BGR: warm cream paper (RGB 238,222,186)
    lab_img = (warp.astype(float) * gain).clip(0, 255)
    wm = cv2.GaussianBlur(cv2.erode((wmask > .5).astype(np.uint8), np.ones((9, 9))).astype(float), (0, 0), 7)[..., None]   # wide feather: no visible box
    fillc = np.median(lab_img[(wm[..., 0] > .9) & (lab_img.max(2) > 170)], axis=0)
    lab_img = lab_img * wm + fillc * (1 - wm)          # plain paper in the label's own colour around the print
    # cool down under blue club light, keep it a little dimmer than the glass highlights
    lab_img = lab_img * 0.94 + np.array([10, 2, -2])          # only a light touch of the blue club light
    lab_img = cv2.addWeighted(lab_img, 1.5, cv2.GaussianBlur(lab_img, (0, 0), 1.2), -0.5, 0)   # sharpen upscale
    a = cv2.GaussianBlur(cv2.erode(omask.astype(np.uint8) * 255, np.ones((5, 5), np.uint8)), (0, 0), 1.5) / 255
    # blue rim on the label edge, as the glass reflects the stage light
    edge = cv2.GaussianBlur((cv2.dilate(omask.astype(np.uint8), np.ones((9, 9))) - omask.astype(np.uint8)).astype(float), (0, 0), 3)
    out = out * (1 - a[..., None]) + lab_img.clip(0, 255) * a[..., None]
    out[..., 0] += edge * 40; out[..., 1] += edge * 10
cv2.imwrite('scene-donjulio.png', out.clip(0, 255).astype(np.uint8))
print('ok')
