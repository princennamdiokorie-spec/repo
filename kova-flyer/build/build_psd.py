"""Stack the per-layer PNGs from export-layers.js into a layered PSD.

Each layer is cropped to its visible pixels and placed at its original offset,
named, and given its blend mode. Then the PSD is re-opened, flattened, and
compared with the reference render to prove the layers rebuild the flyer.

Usage: python3 build_psd.py <layers_dir> <out.psd> <reference.png>
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from psd_tools import PSDImage
from psd_tools.api.layers import PixelLayer
from psd_tools.constants import BlendMode, Compression

BLENDS = {"normal": BlendMode.NORMAL, "screen": BlendMode.SCREEN}


def build(layers_dir: Path, out: Path) -> None:
    manifest = json.loads((layers_dir / "manifest.json").read_text())
    first = Image.open(layers_dir / manifest[0]["file"])
    psd = PSDImage.new(mode="RGB", size=first.size, depth=8)
    for entry in manifest:
        im = Image.open(layers_dir / entry["file"]).convert("RGBA")
        box = im.getbbox()
        if box is None:
            sys.exit(f"layer '{entry['name']}' rendered empty")
        layer = PixelLayer.frompil(im.crop(box), psd, entry["name"], top=box[1], left=box[0],
                                   compression=Compression.RLE)
        layer.blend_mode = BLENDS[entry["blend"]]
        psd.append(layer)
    psd.save(out)


def verify(out: Path, reference: Path) -> None:
    psd = PSDImage.open(out)
    names = [layer.name for layer in psd]
    print(f"{out.name}: {psd.width}x{psd.height}, {len(names)} layers")
    for layer in psd:
        print(f"  {layer.name:<40} {layer.blend_mode.name.lower():<7} {layer.bbox}")
    flat = np.asarray(psd.composite(force=True).convert("RGB")).astype(int)
    ref = np.asarray(Image.open(reference).convert("RGB")).astype(int)
    diff = np.abs(flat - ref).mean(2)
    print(f"flattened vs reference: mean diff {diff.mean():.2f}/255, 99th pct {np.percentile(diff, 99):.1f}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    layers, out_psd, ref = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    build(layers, out_psd)
    verify(out_psd, ref)
