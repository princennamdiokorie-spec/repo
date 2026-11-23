"""Fit rendered text to the original's measured cap height and width, then save
the replacement text at the right scale and position.

For each line: render the ORIGINAL wording, solve letter-spacing so that its
width/cap-height ratio matches the original on the flyer, then render the NEW
wording with the same spacing, scale to the original cap height and centre it on
the original line's centre.
"""
import json
import subprocess

import numpy as np
from PIL import Image

LINES = {
    'nameplate': dict(cls='plate', old='OF KOVA NIGHT CLUB', new='OF KOVA LIFESTYLE',
                      cap=107, width=1734, cx=1547, cap_top=1430, white_cap=True),
    'venue': dict(cls='venue', old='KOVA LIFSTYLE <span class="bar"></span> 30 OLEH ROAD, OFF AWOLOWO',
                  new='KOVA LIFESTYLE <span class="bar"></span> 30 OLEH ROAD, OFF AWOLOWO',
                  cap=45, width=2271, cx=1543, cap_top=3566, white_cap=True),
}


def render(cls, html, spacing, out):
    subprocess.run(['node', 'render_text.js', json.dumps([dict(cls=cls, html=html, spacing=spacing, out=out)])], check=True)
    return np.asarray(Image.open(out).convert('RGBA'))


def measure(rgba):
    a = rgba[..., 3]; white = (rgba[..., :3].min(2) > 200) & (a > 200)
    rows = white.sum(1); ys = np.where(rows > 0.12 * rows.max())[0]   # cap band only (ignore comma tails)
    xs = np.where((a > 128).sum(0) > 0)[0]
    return ys.min(), ys.max(), xs.min(), xs.max()


for name, L in LINES.items():
    lo, hi = -10.0, 120.0 if L['cls'] == 'plate' else 140.0
    for _ in range(14):                                   # bisection on letter-spacing
        mid = (lo + hi) / 2
        y0, y1, x0, x1 = measure(render(L['cls'], L['old'], mid, f'_{name}.png'))
        ratio = (x1 - x0) / (y1 - y0)
        if ratio < L['width'] / L['cap']:
            lo = mid
        else:
            hi = mid
    spacing = (lo + hi) / 2
    new = render(L['cls'], L['new'], spacing, f'_{name}.png')
    y0, y1, x0, x1 = measure(new)
    s = L['cap'] / (y1 - y0)
    pad = 24
    crop = Image.fromarray(new).crop((x0 - pad, y0 - pad, x1 + pad, y1 + pad + 30))
    crop = crop.resize((round(crop.width * s), round(crop.height * s)), Image.LANCZOS)
    crop.save(f'{name}-text.png')
    px = round(L['cx'] - ((x1 - x0) / 2 + pad) * s)
    py = round(L['cap_top'] - pad * s)
    open(f'{name}-text.pos', 'w').write(f'{px} {py}')
    print(name, 'spacing', round(spacing, 2), 'scale', round(s, 4), 'size', crop.size, 'at', px, py,
          'new width', round((x1 - x0) * s))
