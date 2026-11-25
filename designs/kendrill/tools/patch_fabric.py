"""Remove a garment detail by filling a rectangle with cloned fabric texture.

fill = smooth (Laplace) interpolation of the surrounding pixels  +  high-frequency texture
cloned from a plain-fabric source patch, blended into the image with a feathered edge.

usage: python3 patch_fabric.py in.png out.png  x0 y0 x1 y1  dx dy  [x0 y0 x1 y1 dx dy ...]
  (x0,y0,x1,y1) = region to remove; (dx,dy) = offset to a plain-fabric source of the same size
"""
import sys
import numpy as np
from PIL import Image, ImageFilter


def _box(a, r, axis):
    pad = [(0, 0)] * a.ndim
    pad[axis] = (r, r)
    p = np.pad(a, pad, mode="edge")
    c = np.cumsum(p, axis=axis, dtype=np.float64)
    c = np.concatenate([np.zeros_like(np.take(c, [0], axis=axis)), c], axis=axis)
    n = a.shape[axis]
    hi = np.take(c, np.arange(2 * r + 1, 2 * r + 1 + n), axis=axis)
    lo = np.take(c, np.arange(0, n), axis=axis)
    return ((hi - lo) / (2 * r + 1)).astype(np.float32)


def blur(a, r):
    """Gaussian-like blur: three passes of a separable box filter."""
    out = a
    for _ in range(3):
        out = _box(_box(out, r, 0), r, 1)
    return out


def laplace_fill(img, x0, y0, x1, y1, iters=4000):
    """Harmonic fill of the rectangle from its 1-px border (smooth shading)."""
    pad = 1
    region = img[y0 - pad:y1 + pad, x0 - pad:x1 + pad].copy()
    inner = region[pad:-pad, pad:-pad]
    # start from a linear blend of left/right borders for speed
    h, w = inner.shape[:2]
    left = region[pad:-pad, 0:1]
    right = region[pad:-pad, -1:]
    t = np.linspace(0, 1, w)[None, :, None]
    inner[:] = left * (1 - t) + right * t
    for _ in range(iters):
        region[pad:-pad, pad:-pad] = 0.25 * (
            region[:-2, 1:-1] + region[2:, 1:-1] + region[1:-1, :-2] + region[1:-1, 2:]
        )
    return region[pad:-pad, pad:-pad]


def patch(img, x0, y0, x1, y1, dx, dy, feather=4):
    """Seamless clone: fill = source + harmonic correction that matches the target on every edge."""
    src_full = img[y0 + dy - 1:y1 + dy + 1, x0 + dx - 1:x1 + dx + 1]
    tgt_full = img[y0 - 1:y1 + 1, x0 - 1:x1 + 1]
    diff = tgt_full - src_full
    work = diff.copy()
    work[1:-1, 1:-1] = 0
    h, w = work.shape[:2]
    # harmonic interpolation of the boundary difference (Jacobi iterations)
    for _ in range(6000):
        work[1:-1, 1:-1] = 0.25 * (work[:-2, 1:-1] + work[2:, 1:-1] + work[1:-1, :-2] + work[1:-1, 2:])
    fill = src_full[1:-1, 1:-1] + work[1:-1, 1:-1]
    # feathered mask: 1 inside, ramping to 0 over `feather` px at the rectangle edge
    h, w = fill.shape[:2]
    yy = np.minimum(np.arange(h), np.arange(h)[::-1])[:, None]
    xx = np.minimum(np.arange(w), np.arange(w)[::-1])[None, :]
    m = np.clip(np.minimum(yy, xx) / feather, 0, 1)[:, :, None]
    img[y0:y1, x0:x1] = img[y0:y1, x0:x1] * (1 - m) + fill * m


def main():
    src, dst, *nums = sys.argv[1:]
    nums = [int(n) for n in nums]
    img = np.asarray(Image.open(src).convert("RGB"), dtype=np.float32)
    for i in range(0, len(nums), 6):
        x0, y0, x1, y1, dx, dy = nums[i:i + 6]
        patch(img, x0, y0, x1, y1, dx, dy)
    Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(dst)


if __name__ == "__main__":
    main()
