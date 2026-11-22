// Render each element of Kova concept 2 on its own transparent canvas, one PNG per layer,
// so they can be stacked into a layered PSD. Usage: node export-layers.js <outDir>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const SOURCE = path.resolve(__dirname, 'flyer-stage.html');
const SCALE = 2;

// Bottom-to-top stacking order. `show` = CSS selectors drawn on this layer.
// the badge's glow/shadow lives on the container: keep it only on the disc layer, or it stacks per text layer
const NO_BADGE_GLOW = '.badge { filter: none !important; }';

const LAYERS = [
  { name: 'Background colour', show: [], keepBackground: true },
  { name: 'Stage background (blurred fill)', show: ['.bg-fill'] },
  { name: 'Stage background', show: ['.bg'] },
  { name: 'Top shade', show: ['.shade-top'] },
  { name: 'Bottom shade', show: ['.shade-bot'] },
  { name: 'Kova logo', show: ['.logo'] },
  { name: 'Grand Opening title (3D)', show: ['.title'] },
  { name: 'Bottles', show: ['.bottles'] },
  { name: 'Date badge disc', show: ['.badge'], extraCss: '.badge .ring-text, .badge .core, .badge .core * { visibility: hidden !important; }' },
  { name: 'Badge ring text', show: ['.badge .ring-text'], extraCss: NO_BADGE_GLOW },
  { name: 'Badge 10-12', show: ['.badge .n'], extraCss: NO_BADGE_GLOW },
  { name: 'Badge DECEMBER', show: ['.badge .m'], extraCss: NO_BADGE_GLOW },
  { name: 'Badge 10PM', show: ['.badge .t'], extraCss: NO_BADGE_GLOW },
  { name: 'Venue line', show: ['#venue'] },
  { name: 'Contact line (phone, email, socials)', show: ['#contact'] },
];

const soloCss = (layer) => `
  html, body, .f { background: ${layer.keepBackground ? '' : 'transparent'} !important; }
  .f * { visibility: hidden !important; }
  ${layer.show.map((s) => `${s}, ${s} *`).join(', ') || '.none'} { visibility: visible !important; }
  ${layer.blend ? layer.show.join(', ') + ' { mix-blend-mode: normal !important; }' : ''}
  ${layer.extraCss || ''}
`;

(async () => {
  const outDir = path.resolve(process.argv[2] || 'layers');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: SCALE });
  const manifest = [];
  for (const [i, layer] of LAYERS.entries()) {
    await page.goto('file://' + SOURCE);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(200); // let the fonts.ready positioning script run
    await page.addStyleTag({ content: soloCss(layer) });
    // visibility:hidden does not stop Chrome painting SVG filter output (the haze),
    // so remove every top-level element that holds none of this layer's targets
    await page.evaluate((selectors) => {
      const targets = selectors.flatMap((s) => [...document.querySelectorAll(s)]);
      for (const el of document.querySelectorAll('.f > *')) {
        if (!targets.some((t) => el === t || el.contains(t))) el.style.setProperty('display', 'none', 'important');
      }
    }, layer.show);
    if (layer.keepBackground) {
      // background only: hide every child of the frame
      await page.addStyleTag({ content: '.f > * { display: none !important; }' });
    }
    const file = `${String(i).padStart(2, '0')}.png`;
    await page.screenshot({ path: path.join(outDir, file), omitBackground: !layer.keepBackground });
    manifest.push({ file, name: layer.name, blend: layer.blend || 'normal' });
  }
  fs.writeFileSync(path.join(outDir, 'manifest.json'), JSON.stringify(manifest, null, 2));
  await browser.close();
  process.stdout.write(`exported ${manifest.length} layers to ${outDir}\n`);
})();
