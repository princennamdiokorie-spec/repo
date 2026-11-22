# Kova Night Club: grand opening flyer

**Status: FINAL** (approved 2026-11-22). Concept 4, "portal".

Event: Grand opening, 10–12 December, doors 10PM, 30 Oleh Road, off Awolowo.
Contact: 09166586974 · info@kova-lifestyle.com · @kova.lifestyle

## Final files

| File | What |
|---|---|
| `flyer4-portal.png` | 2160×2700 PNG |
| `flyer4-portal-4k.png` | 3072×3840 PNG (native 4K render) |
| `flyer4-portal.psd` | Layered PSD, 18 named layers (text layers are raster) |
| `title/grand-opening-title-B-night-club.png` | Title plaque, transparent |
| `logo/kova-logo-transparent.png` | Logo cut-out, transparent |

## Rebuild

From `build/`:

```bash
node render.js flyer4-portal.html
SCALE=2.8444 SUFFIX=-4k node render.js flyer4-portal.html
node export-layers.js /tmp/layers && python3 build_psd.py /tmp/layers ../flyer4-portal.psd ../flyer4-portal.png
```

Concepts 1–3 (`flyer1-gate`, `flyer2-arch`, `flyer3-spotlight`) are earlier
explorations, kept for reference.
