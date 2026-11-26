// Build an editable PSD of the blue spotlight flyer from export.js output.
// Text lines become real Photoshop type layers (Montserrat / Cinzel, size, tracking, colours,
// two-colour lines as style runs); the GRAND OPENING chrome is a gradient-overlay + drop-shadow +
// outer-glow layer style, so it stays editable too. Each text layer also carries its rendered
// pixels, so the file previews correctly before Photoshop re-renders the type.
// Usage: node build.js <exportDir> <out.psd> [theme.json]
const fs = require('fs');
const path = require('path');
const { PNG } = require('pngjs');
const { writePsdBuffer } = require('ag-psd');

const [dir, out] = [path.resolve(process.argv[2]), path.resolve(process.argv[3])];
const m = JSON.parse(fs.readFileSync(path.join(dir, 'manifest.json'), 'utf8'));

const FONTS = { 'Montserrat:400': 'Montserrat-Regular', 'Montserrat:500': 'Montserrat-Medium', 'Montserrat:600': 'Montserrat-SemiBold',
                'Montserrat:700': 'Montserrat-Bold', 'Cinzel:600': 'Cinzel-SemiBold', 'Cinzel:900': 'Cinzel-Black' };

function loadCropped(file, full = false) {
  const png = PNG.sync.read(fs.readFileSync(path.join(dir, file)));
  const { width: w, height: h, data } = png;
  if (full) return { left: 0, top: 0, imageData: { width: w, height: h, data: new Uint8ClampedArray(data) } };
  let x0 = w, y0 = h, x1 = -1, y1 = -1;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) if (data[(y * w + x) * 4 + 3] > 0) {
    if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
  if (x1 < 0) throw new Error(file + ' is empty');
  const cw = x1 - x0 + 1, ch = y1 - y0 + 1, out = new Uint8ClampedArray(cw * ch * 4);
  for (let y = 0; y < ch; y++) out.set(data.subarray(((y + y0) * w + x0) * 4, ((y + y0) * w + x0 + cw) * 4), y * cw * 4);
  return { left: x0, top: y0, imageData: { width: cw, height: ch, data: out } };
}

const style = (r) => {
  const font = FONTS[`${r.family}:${r.weight}`];
  if (!font) throw new Error('no font mapping for ' + r.family + ' ' + r.weight);
  return { font: { name: font }, fontSize: r.size, tracking: Math.round(r.letterSpacing / r.size * 1000), autoKerning: true,
           fillColor: r.transparent ? { r: 255, g: 255, b: 255 } : { r: r.color.r, g: r.color.g, b: r.color.b } };
};

const hex = (h) => ({ r: parseInt(h.slice(1, 3), 16), g: parseInt(h.slice(3, 5), 16), b: parseInt(h.slice(5, 7), 16) });
// theme: chrome gradient stops, shadow and glow for the GRAND OPENING layer style (default = blue flyer)
const TH = process.argv[4] ? JSON.parse(fs.readFileSync(process.argv[4], 'utf8'))
  : { chrome: [['#ffffff', 0], ['#e6ebf3', .38], ['#9aa6b8', .55], ['#f4f7fb', .72], ['#c3cbd8', 1]], shadow: '#1a2b55', glow: '#2a8cff' };
const CHROME = {   // matches the flyer's CSS linear-gradient(180deg, ...) on the title
  gradientOverlay: [{ enabled: true, blendMode: 'normal', opacity: 1, angle: -90, type: 'linear', scale: 1, align: true,
    gradient: { name: 'Kova chrome ' + (process.argv[4] ? path.basename(process.argv[4], '.json') : 'blue'), type: 'solid', smoothness: 1,
      colorStops: TH.chrome.map(([c, l]) => ({ color: hex(c), location: l, midpoint: 50 })),
      opacityStops: [{ opacity: 1, location: 0, midpoint: 50 }, { opacity: 1, location: 1, midpoint: 50 }] } }],
  dropShadow: [{ enabled: true, blendMode: 'normal', color: hex(TH.shadow), opacity: 1, angle: 90, useGlobalLight: false,
    distance: { units: 'Pixels', value: 4 }, size: { units: 'Pixels', value: 0 } }],
  outerGlow: { enabled: true, blendMode: 'screen', color: hex(TH.glow), opacity: TH.glowOpacity ?? .45, size: { units: 'Pixels', value: TH.glowSize ?? 32 } },
};

const raster = m.raster.map((r, i) => ({ name: r.name, ...loadCropped(r.file, i === 0) }));
const text = m.text.map((t) => {
  const s0 = style(t.runs[0]);
  const layer = {
    name: t.name, ...loadCropped(t.file),
    text: { text: t.runs.map(r => r.text).join(''), transform: [1, 0, 0, 1, t.x, t.baseline], antiAlias: 'smooth', shapeType: 'point',
            style: s0, styleRuns: t.runs.map(r => ({ length: r.text.length, style: style(r) })), paragraphStyle: { justification: 'left' } },
  };
  if (t.runs.some(r => r.transparent)) layer.effects = CHROME;
  return layer;
});

const comp = PNG.sync.read(fs.readFileSync(path.join(dir, 'composite.png')));
const psd = {
  width: m.width, height: m.height,
  imageData: { width: comp.width, height: comp.height, data: new Uint8ClampedArray(comp.data) },
  children: [
    { name: 'Artwork', opened: true, children: raster },
    { name: 'Text (editable)', opened: true, children: text },
  ],
};
fs.writeFileSync(out, writePsdBuffer(psd, { invalidateTextLayers: true, generateThumbnail: false }));
console.log('wrote', out, (fs.statSync(out).size / 1e6).toFixed(1) + ' MB', raster.length + ' artwork + ' + text.length + ' text layers');
