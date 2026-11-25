"""Make a colour-themed copy of the spotlight flyer (flyer-swap.html -> flyer-<theme>.html)
plus hue-shifted logo/emblem assets. The map replaces every blue/navy colour with its
counterpart; the same map is written to theme-<theme>.json for the PSD builder.
Usage: python3 make_theme.py red"""
import json, re, sys
import numpy as np
from PIL import Image

THEMES = {
  'red': {   # sampled from the client's 11th-Dec flyer: bg #290217, glow area #5e0322, logo red #c34b4c / #f1898c
    'hue_shift': 135,                     # blue chrome (≈215°) -> crimson chrome (≈350°)
    'map': {
      # backgrounds (navy -> wine)
      '#040a1c': '#240115', '#06112e': '#330219', '#0b2257': '#5e0322', '#020814': '#140009', '#1b4fb0': '#a8102e',
      # glow + accents (electric blue -> crimson / light rose)
      '#2a8cff': '#e0193a', '#5aa8ff': '#ff5a72', '#7cc4ff': '#ff8a98',
      'rgba(42,140,255,': 'rgba(224,25,58,', 'rgba(60,150,255,': 'rgba(235,40,70,', 'rgba(30,100,230,': 'rgba(200,16,46,',
      'rgba(230,242,255,': 'rgba(255,230,236,',
      # blue-tinted whites -> rose whites
      '#e8f3ff': '#ffe8ec', '#e6f2ff': '#ffe6ea', '#e9f2ff': '#ffe9ed', '#cfe6ff': '#ffcfd8', '#eaf4ff': '#ffeaee', '#dbeaff': '#ffdbe2',
      '#e8eef7': '#f7e8ec', '#9fb0c8': '#c89fab',
      # text silvers (cool -> warm)
      '#c9ced8': '#d8c9ce', '#eef2f8': '#f8eef1', '#e8ecf3': '#f3e8eb', '#d8dee9': '#e9d8dd', '#8f9ab0': '#b08f99',
      # GRAND OPENING chrome: mid stop matched to the wine background, shadow to deep wine
      '#e6ebf3': '#f3e6ea', '#9aa6b8': '#b8838f', '#f4f7fb': '#fbf4f6', '#c3cbd8': '#d8c3c9', '#1a2b55': '#4a0418',
    },
    'chrome': [['#ffffff', 0], ['#f3e6ea', .38], ['#b8838f', .55], ['#fbf4f6', .72], ['#d8c3c9', 1]],
    'shadow': '#4a0418', 'glow': '#e0193a',
  },
  'emerald': {   # 12 Dec: deep emerald with champagne-gold accents (mature, distinct from blue/red)
    'hue_shift': 300,                     # blue chrome (≈215°) -> emerald chrome (≈155°)
    'map': {
      '#040a1c': '#01140e', '#06112e': '#021d15', '#0b2257': '#04382a', '#020814': '#000c08', '#1b4fb0': '#0e7a55',
      '#2a8cff': '#18b07a', '#5aa8ff': '#5fd4a5', '#7cc4ff': '#e8cf9a',
      'rgba(42,140,255,': 'rgba(24,176,122,', 'rgba(60,150,255,': 'rgba(40,190,135,', 'rgba(30,100,230,': 'rgba(14,122,85,',
      'rgba(230,242,255,': 'rgba(232,250,242,',
      '#e8f3ff': '#e8fff6', '#e6f2ff': '#e6fff4', '#e9f2ff': '#e9fff6', '#cfe6ff': '#cff5e5', '#eaf4ff': '#eafff7', '#dbeaff': '#dbf7ea',
      '#e8eef7': '#e8f4ef', '#9fb0c8': '#9fc8b6',
      '#c9ced8': '#c9d8d1', '#eef2f8': '#eef8f3', '#e8ecf3': '#e8f3ee', '#d8dee9': '#d8e9e1', '#8f9ab0': '#8fb0a2',
      '#e6ebf3': '#e6f3ed', '#9aa6b8': '#8fb3a3', '#f4f7fb': '#f4fbf8', '#c3cbd8': '#c3d8ce', '#1a2b55': '#043322',
    },
    'chrome': [['#ffffff', 0], ['#e6f3ed', .38], ['#8fb3a3', .55], ['#f4fbf8', .72], ['#c3d8ce', 1]],
    'shadow': '#043322', 'glow': '#18b07a',
  },
}

name = sys.argv[1]; T = THEMES[name]
src = open('flyer-swap.html').read()
out = src
for a, b in sorted(T['map'].items(), key=lambda kv: -len(kv[0])):
    n = len(re.findall(re.escape(a), out, flags=re.I))
    out = re.sub(re.escape(a), b, out, flags=re.I)
    if n == 0: print('note: not found', a)
# assets
for asset in ['kova-logo-transparent', 'kova-symbol-hd']:
    im = Image.open(f'../assets/{asset}.png').convert('RGBA')
    hsv = np.asarray(im.convert('RGB').convert('HSV')).astype(int)
    hsv[..., 0] = (hsv[..., 0] + round(T['hue_shift'] / 360 * 255)) % 256
    rgb = Image.fromarray(hsv.astype(np.uint8), 'HSV').convert('RGB'); rgb.putalpha(im.getchannel('A'))
    rgb.save(f'../assets/{asset}-{name}.png')
    out = out.replace(f'../assets/{asset}.png', f'../assets/{asset}-{name}.png')
left = [c for c in ['#2a8cff', '#7cc4ff', '#040a1c', '#0b2257', 'rgba(42,140,255'] if c in out.lower()]
assert not left, ('blue left over', left)
open(f'flyer-{name}.html', 'w').write(out)
json.dump({'chrome': T['chrome'], 'shadow': T['shadow'], 'glow': T['glow']}, open(f'theme-{name}.json', 'w'), indent=1)
print('wrote', f'flyer-{name}.html', f'theme-{name}.json')
