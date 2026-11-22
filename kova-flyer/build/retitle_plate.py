"""Replace the nameplate wording on title plaque B.

Step 1 (this script, `blank`): rebuild the brushed-metal nameplate where the old
lettering sat, by interpolating each column between clean plate rows above and
below the text and adding back horizontal brushed texture.
Step 2 (`compose`): lay a transparent PNG of the new lettering on the blank plate.

Usage:
  python3 retitle_plate.py blank   <plaque.png> <out_blank.png>
  python3 retitle_plate.py compose <blank.png> <text.png> <out.png>
"""
import sys

import numpy as np
from PIL import Image

# Nameplate geometry in plaque-B pixels (2048 x 1282 source).
TEXT_X0, TEXT_X1 = 378, 1674   # old lettering, horizontally (inside the rivets)
TEXT_Y0, TEXT_Y1 = 930, 1048   # old lettering incl. its blue extrusion
CLEAN_ABOVE = (914, 926)       # clean plate rows above the text
CLEAN_BELOW = (1050, 1058)     # clean plate rows below the text
TEXT_CENTER = ((TEXT_X0 + TEXT_X1) // 2, (TEXT_Y0 + TEXT_Y1) // 2 - 4)


def blank(src: str, out: str) -> None:
    im = np.asarray(Image.open(src).convert("RGBA")).astype(np.float64)
    top = im[CLEAN_ABOVE[0]:CLEAN_ABOVE[1], TEXT_X0:TEXT_X1, :3].mean(0)
    bot = im[CLEAN_BELOW[0]:CLEAN_BELOW[1], TEXT_X0:TEXT_X1, :3].mean(0)
    h = TEXT_Y1 - TEXT_Y0
    t = np.linspace(0, 1, h)[:, None, None]
    fill = top[None] * (1 - t) + bot[None] * t
    # brushed texture: horizontal streaks taken from the clean strip, tiled down the band
    strip = im[CLEAN_ABOVE[0]:CLEAN_ABOVE[1], TEXT_X0:TEXT_X1, :3]
    detail = strip - strip.mean(0, keepdims=True)
    reps = int(np.ceil(h / detail.shape[0]))
    rng = np.random.default_rng(3)
    rows = [np.roll(detail, rng.integers(0, detail.shape[1]), axis=1) for _ in range(reps)]
    tex = np.concatenate(rows, 0)[:h]
    fill = np.clip(fill + tex * 0.9, 0, 255)
    # feather the band edges so no seam shows
    w = TEXT_X1 - TEXT_X0
    fy = np.minimum(np.minimum(np.arange(h), np.arange(h)[::-1]) / 4.0, 1.0)
    fx = np.minimum(np.minimum(np.arange(w), np.arange(w)[::-1]) / 6.0, 1.0)
    feather = (fy[:, None] * fx[None, :])[:, :, None]
    region = im[TEXT_Y0:TEXT_Y1, TEXT_X0:TEXT_X1, :3]
    im[TEXT_Y0:TEXT_Y1, TEXT_X0:TEXT_X1, :3] = region * (1 - feather) + fill * feather
    Image.fromarray(im.round().astype(np.uint8), "RGBA").save(out)


def compose(blank_path: str, text_path: str, out: str) -> None:
    base = Image.open(blank_path).convert("RGBA")
    text = Image.open(text_path).convert("RGBA")
    max_w = 1262  # width of the original lettering
    if text.width > max_w:
        text = text.resize((max_w, round(text.height * max_w / text.width)), Image.LANCZOS)
    x = (392 + 1660) // 2 - text.width // 2
    y = TEXT_CENTER[1] - text.height // 2
    base.alpha_composite(text, (x, y))
    base.save(out)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "blank" and len(sys.argv) == 4:
        blank(sys.argv[2], sys.argv[3])
    elif cmd == "compose" and len(sys.argv) == 5:
        compose(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit(__doc__)
