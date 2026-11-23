"""Alignment check for a rendered flyer: every text/graphic row's centre and the gaps between rows.
Run before sending any flyer. Flags rows whose centre is more than TOL px off the flyer centre.
Usage: python3 check_alignment.py <flyer.png> [css_scale=2]"""
import sys
import numpy as np
from PIL import Image

TOL = 3
img = np.asarray(Image.open(sys.argv[1]).convert('L')).astype(int)
S = float(sys.argv[2]) if len(sys.argv) > 2 else 2
h, w = img.shape; cx = w / 2 / S
x0, x1 = int(w * .1), int(w * .9)                     # inside the frame
rows, s = [], None
for y in range(int(h * .06), int(h * .97)):
    on = (img[y, x0:x1] > 140).sum() > 3
    if on and s is None: s = y
    if not on and s is not None: rows.append((s, y - 1)); s = None
prev, bad = None, 0
for a, b in rows:
    xs = np.where((img[a:b + 1, x0:x1] > 140).any(0))[0]
    c = (xs.min() + xs.max()) / 2 / S + x0 / S
    gap = '' if prev is None else f'gap {a / S - prev:5.0f}'
    flag = '  <-- OFF CENTRE' if abs(c - cx) > TOL and (b - a) / S > 6 else ''
    bad += bool(flag)
    print(f'y {a / S:6.0f}-{b / S:<6.0f} centre {c:7.1f} {gap}{flag}'); prev = b / S
print('OK: all rows centred' if not bad else f'{bad} row(s) off centre')
