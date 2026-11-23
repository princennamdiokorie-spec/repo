// Export each element of the concept-4 Don Julio flyer as its own transparent PNG for the PSD.
// Usage: node export-layers.js <outDir>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const SOURCE = path.resolve(__dirname, 'flyer-psd.html');
const LAYERS = [
  { name: 'Background (clean scene)', show: ['#L-scene'] },
  { name: 'Don Julio labels', show: ['#L-labels'] },
  { name: 'Bottom shade', show: ['#L-shade'] },
  { name: 'GRAND OPENING title', show: ['#L-title-refined'] },
  { name: 'Kova logo (A in GRAND)', show: ['#L-symbol'] },
  { name: 'KOVA LIFESTYLE PRESENTS', show: ['.top'] },
  { name: 'KOVA LIFESTYLE (under title)', show: ['.club'] },
  { name: 'Date Thu Dec 10th-12th', show: ['#L-date'] },
  { name: 'DOORS OPEN AT 10PM', show: ['#L-doors'] },
  { name: 'The Night Begins...', show: ['#L-script'] },
  { name: 'FOR MORE INFO CALL', show: ['.info'] },
  { name: 'Instagram / email line', show: ['#L-insta'] },
  { name: 'Kova Lifestyle (bottom)', show: ['.name'] },
  { name: '30 OLEH ROAD, OFF AWOLOWO', show: ['#L-address'] },
];

(async () => {
  const outDir = path.resolve(process.argv[2] || 'layers');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 872, height: 1168 }, deviceScaleFactor: 2 });
  const manifest = [];
  for (const [i, layer] of LAYERS.entries()) {
    await page.goto('file://' + SOURCE);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(300);
    await page.evaluate((sel) => {
      document.documentElement.style.background = 'transparent';
      document.body.style.background = 'transparent';
      const keep = sel.flatMap((s) => [...document.querySelectorAll(s)]);
      for (const el of document.querySelectorAll('.f > *')) {
        if (!keep.some((k) => el === k || el.contains(k))) el.style.setProperty('display', 'none', 'important');
      }
    }, layer.show);
    const file = `${String(i).padStart(2, '0')}.png`;
    await page.screenshot({ path: path.join(outDir, file), omitBackground: true });
    manifest.push({ file, name: layer.name, blend: 'normal' });
  }
  fs.writeFileSync(path.join(outDir, 'manifest.json'), JSON.stringify(manifest, null, 2));
  await browser.close();
  process.stdout.write(`exported ${manifest.length} layers\n`);
})();
