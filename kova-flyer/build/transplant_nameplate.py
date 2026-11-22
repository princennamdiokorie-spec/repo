"""Transplant the edited nameplate from an AI-edited plaque onto the clean transparent plaque.

The edit comes back opaque and at a different scale, so it is registered to the
original with ORB features + a similarity transform, then only the nameplate
rectangle is copied across (feathered), keeping the original's clean alpha.

Usage: python3 transplant_nameplate.py <original_rgba.png> <edited.png> <out.png> [debug.png]
"""
import sys

import cv2
import numpy as np

# Nameplate panel in grand-opening-title-B.png (cropped 2048x1282) pixels: inside the frame bevel.
PLATE = (335, 905, 1715, 1065)  # x0, y0, x1, y1
FEATHER = 6


def register(orig_rgb: np.ndarray, edit_rgb: np.ndarray) -> np.ndarray:
    """Return a 2x3 matrix mapping edited-image pixels onto original pixels."""
    orb = cv2.ORB_create(8000)
    g1 = cv2.cvtColor(orig_rgb, cv2.COLOR_RGB2GRAY)
    g2 = cv2.cvtColor(edit_rgb, cv2.COLOR_RGB2GRAY)
    # match only outside the nameplate, where the two images should agree
    mask = np.full(g1.shape, 255, np.uint8)
    x0, y0, x1, y1 = PLATE
    mask[y0 - 40:y1 + 40, x0 - 40:x1 + 40] = 0
    k1, d1 = orb.detectAndCompute(g1, mask)
    k2, d2 = orb.detectAndCompute(g2, None)
    matches = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d2, d1)
    src = np.float32([k2[m.queryIdx].pt for m in matches])
    dst = np.float32([k1[m.trainIdx].pt for m in matches])
    M, inliers = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=3)
    if M is None or inliers.sum() < 50:
        sys.exit(f"registration failed ({0 if inliers is None else int(inliers.sum())} inliers)")
    scale = np.hypot(M[0, 0], M[1, 0])
    sys.stderr.write(f"inliers {int(inliers.sum())}/{len(matches)}  scale {scale:.4f}  shift {M[0, 2]:.1f},{M[1, 2]:.1f}\n")
    return M


def main(orig_path: str, edit_path: str, out_path: str, debug_path: str | None) -> None:
    orig = cv2.cvtColor(cv2.imread(orig_path, cv2.IMREAD_UNCHANGED), cv2.COLOR_BGRA2RGBA)
    edit = cv2.cvtColor(cv2.imread(edit_path, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
    h, w = orig.shape[:2]
    M = register(orig[..., :3], edit)
    warped = cv2.warpAffine(edit, M, (w, h), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)

    x0, y0, x1, y1 = PLATE
    m = np.zeros((h, w), np.float32)
    m[y0:y1, x0:x1] = 1.0
    m = cv2.GaussianBlur(m, (0, 0), FEATHER)
    m[y0 + FEATHER * 2:y1 - FEATHER * 2, x0 + FEATHER * 2:x1 - FEATHER * 2] = 1.0
    out = orig.astype(np.float32)
    out[..., :3] = out[..., :3] * (1 - m[..., None]) + warped.astype(np.float32) * m[..., None]
    cv2.imwrite(out_path, cv2.cvtColor(out.round().astype(np.uint8), cv2.COLOR_RGBA2BGRA))

    if debug_path:  # residual outside the plate shows how well the two line up
        diff = np.abs(warped.astype(int) - orig[..., :3].astype(int)).mean(2)
        solid = orig[..., 3] > 250
        ring = solid.copy()
        ring[y0 - 60:y1 + 60, x0 - 60:x1 + 60] = False
        sys.stderr.write(f"mean abs diff outside plate: {diff[ring].mean():.1f}\n")
        cv2.imwrite(debug_path, np.clip(diff * 3, 0, 255).astype(np.uint8))


if __name__ == "__main__":
    if len(sys.argv) not in (4, 5):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) == 5 else None)
