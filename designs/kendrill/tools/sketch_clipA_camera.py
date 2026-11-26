"""Code sketch of the Clip A drone move: three-quarter view from OUTSIDE the bridge.

Draws three 9:16 frames (0s, 4s, 8s) of what the camera sees, plus a top-down map
of the drone path versus the rejected draft (which flew along the deck).

usage: python3 sketch_clipA_camera.py out.png
"""
import math
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 540, 960          # one 9:16 panel
A = math.radians(22)     # bridge rises to the right
K = 0.6                  # squash across the deck (camera looks down at an angle)

SKY, WATER, DEEP = (150, 196, 230), (52, 128, 140), (36, 98, 112)
DECK, GIRDER, CABLE, PYLON = (120, 120, 124), (226, 214, 196), (245, 245, 245), (176, 176, 172)
CAR = (12, 12, 14)
ORDER = ["ESC", "G63", "LX", "JET", "G63", "ESC"]  # front -> back

try:
    FONT = ImageFont.truetype("DejaVuSans-Bold.ttf", 22)
    SMALL = ImageFont.truetype("DejaVuSans.ttf", 15)
except OSError:
    FONT = SMALL = ImageFont.load_default()


def project(u, v, h, zoom, sx, sy):
    """World (along bridge u, across v, height h) -> screen."""
    x = sx + zoom * (u * math.cos(A) + v * math.sin(A) * K)
    y = sy + zoom * (-u * math.sin(A) + v * math.cos(A) * K - h * 0.9)
    return x, y


def band(d, zoom, sx, sy, u0, u1, v0, v1, h0, h1, fill):
    pts = [project(u0, v0, h0, zoom, sx, sy), project(u1, v0, h0, zoom, sx, sy),
           project(u1, v1, h1, zoom, sx, sy), project(u0, v1, h1, zoom, sx, sy)]
    d.polygon(pts, fill=fill)


def view(zoom, sx, sy, horizon, cables_front, label):
    img = Image.new("RGB", (W, H), SKY)
    d = ImageDraw.Draw(img)
    # lagoon below the horizon, skyline on it
    d.rectangle([0, horizon, W, H], fill=WATER)
    d.rectangle([0, horizon + 0.55 * (H - horizon), W, H], fill=DEEP)
    for i, x in enumerate(range(0, W, 26)):
        bh = 12 + (i * 37) % 46
        d.rectangle([x, horizon - bh, x + 20, horizon], fill=(110, 116, 124))
    d.rectangle([0, horizon - 4, W, horizon + 3], fill=(200, 186, 150))  # shoreline

    L0, L1 = -900, 900
    # outer side face of the deck: we see it because the camera is OUTSIDE the bridge
    band(d, zoom, sx, sy, L0, L1, 32, 32, 0, -26, GIRDER)
    band(d, zoom, sx, sy, L0, L1, -32, 32, 0, 0, DECK)
    # black-and-white kerbs and median
    for v in (-30, 0, 30):
        for u in range(L0, L1, 16):
            col = (20, 20, 20) if (u // 16) % 2 else (240, 240, 240)
            band(d, zoom, sx, sy, u, u + 16, v - 2, v + 2, 1, 1, col)

    # single pylon on the median, splitting into two prongs at the top
    pu = 330
    base = project(pu, 0, 0, zoom, sx, sy)
    split = project(pu, 0, 300, zoom, sx, sy)
    d.line([base, split], fill=PYLON, width=max(3, int(16 * zoom)))
    for dv in (-14, 14):
        tip = project(pu + dv * 0.4, dv, 430, zoom, sx, sy)
        d.line([split, tip], fill=PYLON, width=max(2, int(10 * zoom)))
    top = project(pu, 0, 400, zoom, sx, sy)
    # cables fan to one side (toward the convoy)
    for u in range(40, pu - 20, 34):
        for v in (-30, 30):
            d.line([top, project(u, v, 1, zoom, sx, sy)], fill=CABLE, width=max(1, int(2 * zoom)))

    # convoy: right-hand (near) lane, driving AWAY toward the upper right
    for i, name in enumerate(ORDER):
        u = 60 - i * 34
        band(d, zoom, sx, sy, u - 11, u + 11, 9, 23, 3, 3, CAR)
        if zoom > 1.2:
            cx, cy = project(u, 16, 30, zoom, sx, sy)
            d.text((cx - 14, cy - 40), name, fill=(255, 230, 80), font=SMALL)
    ax, ay = project(130, 16, 4, zoom, sx, sy)
    bx, by = project(190, 16, 4, zoom, sx, sy)
    d.line([ax, ay, bx, by], fill=(255, 230, 80), width=4)
    d.polygon([(bx, by), (bx - 14, by + 2), (bx - 6, by + 12)], fill=(255, 230, 80))

    # foreground cables sweeping past the lens in the close view
    for x0 in cables_front:
        d.line([(x0, 0), (x0 - 260, H)], fill=(235, 235, 235), width=5)

    d.rectangle([0, 0, W, 40], fill=(20, 20, 20))
    d.text((12, 8), label, fill="white", font=FONT)
    return img


def top_map():
    img = Image.new("RGB", (W, H), WATER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 150], fill=(196, 186, 160))
    d.text((12, 110), "Ikoyi / Lagos skyline", fill=(40, 40, 40), font=SMALL)
    # bridge from above
    d.line([(40, 760), (500, 200)], fill=DECK, width=46)
    d.line([(40, 760), (500, 200)], fill=(240, 240, 240), width=2)
    d.ellipse([(318, 402), (342, 426)], fill=PYLON, outline=(60, 60, 60))
    d.text((350, 396), "pylon", fill="white", font=SMALL)
    for i in range(6):
        x, y = 170 + i * -22 + 14, 610 + i * 27 + 8
        d.rectangle([x - 7, y - 7, x + 7, y + 7], fill=CAR)
    d.text((40, 785), "convoy, right-hand lane", fill="white", font=SMALL)
    d.text((40, 803), "driving away (to the top right)", fill="white", font=SMALL)
    # NEW path: outside, over the water, three-quarter view, descending
    pts = [(500, 900), (440, 800), (360, 710), (300, 640)]
    d.line(pts, fill=(255, 230, 80), width=6)
    for (x, y), t in zip([pts[0], pts[2], pts[3]], ["0s high + far", "4s", "8s low, still outside"]):
        d.ellipse([x - 10, y - 10, x + 10, y + 10], fill=(255, 230, 80))
        tx = x - 20 - 8 * len(t) if x > 420 else x + 14
        d.text((tx, y - 8), t, fill="white", font=SMALL)
    d.line([(300, 640), (205, 610)], fill=(255, 230, 80), width=2)  # looking at the cars
    # OLD path: along the deck (rejected)
    for i in range(0, 300, 20):
        x0, y0 = 40 + i * 0.82, 760 - i
        d.line([(x0, y0), (x0 + 8, y0 - 10)], fill=(230, 60, 60), width=4)
    d.text((20, 870), "last draft: flew along the road  X", fill=(255, 120, 120), font=SMALL)
    d.rectangle([0, 0, W, 40], fill=(20, 20, 20))
    d.text((12, 8), "Map from above", fill="white", font=FONT)
    return img


def main():
    panels = [
        view(0.42, 300, 640, 230, [], "0s  high and far, outside"),
        view(0.85, 250, 680, 330, [], "4s  descending, closing in"),
        view(1.7, 230, 760, 430, [120, 300, 470], "8s  three-quarter, cut here"),
        top_map(),
    ]
    gap = 16
    sheet = Image.new("RGB", (len(panels) * W + (len(panels) + 1) * gap, H + 2 * gap), (28, 28, 30))
    for i, p in enumerate(panels):
        sheet.paste(p, (gap + i * (W + gap), gap))
    sheet.save(sys.argv[1])


if __name__ == "__main__":
    main()
