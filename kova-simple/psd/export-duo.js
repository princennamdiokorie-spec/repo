// Export the two-host flyer (build/duo.html) for an editable PSD (same method as export.js):
//  - raster layers for the artwork, each rendered alone on transparency
//  - a spec for every text line (font, size, weight, tracking, colour, left x, baseline)
//    plus a raster preview of that line, so the PSD looks right before Photoshop re-renders it.
// Usage: node export.js <outDir>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const FLYER = process.env.FLYER || 'flyer-swap.html';           // e.g. FLYER=flyer-red.html for the red theme
const URL = 'file://' + path.resolve(__dirname, '../build', 'duo.html');
const DPR = 2;
const OUT = path.resolve(process.argv[2] || 'out');

const RASTER = [
  { name: 'Background', keepBg: true, show: ['.grain'] },
  { name: 'Halo & stars', show: ['svg.fx'] },
  { name: 'Highprince (photo)', show: ['#p2'] },
  { name: 'Yhemolee (photo)', show: ['#p1'] },
  { name: 'Kova logo', show: ['.logo'] },
  { name: 'Divider', show: ['.rule'] },
  { name: 'Contact icons', show: ['.c2 svg', '.c2 .bar'] },
];
const TEXT = [
  ['KOVA LIFESTYLE PRESENTS', '.presents'],
  ['HOSTED BY (Yhemolee)', '#h1 .lb'],
  ['YHEMOLEE', '#h1 .nm'],
  ['HOSTED BY (Highprince)', '#h2 .lb'],
  ['HIGHPRINCE', '#h2 .nm'],
  ['GRAND OPENING', '.title'],
  ['KOVA LIFESTYLE', '.kicker'],
  ['Date', '.d1'],
  ['Doors + address', '.d2'],
  ['RESERVATIONS', '.res'],
  ['Phone', '.c1'],
  ['Email', '.c2 .it:first-child'],
  ['Instagram / Snapchat handle', '.c2 .it:last-child'],
];

async function load(page) {
  await page.goto(URL);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(400);
  // wrap every text node in a span (so it can be shown alone and measured) – layout is unchanged
  await page.evaluate(() => {
    const w = document.createTreeWalker(document.querySelector('.f'), NodeFilter.SHOW_TEXT);
    const nodes = []; while (w.nextNode()) if (w.currentNode.nodeValue.trim()) nodes.push(w.currentNode);
    for (const n of nodes) { const s = document.createElement('span'); s.className = '__t'; n.parentNode.insertBefore(s, n); s.appendChild(n); }
  });
}

async function isolate(page, selectors, keepBg) {
  await page.addStyleTag({ content: `
    html,body,.f{background:${keepBg ? '' : 'transparent'} !important}
    .f *{visibility:hidden !important}
    ${selectors.map(s => `${s},${s} *`).join(',')}{visibility:visible !important}` });
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: DPR });
  const manifest = { width: 1080 * DPR, height: 1350 * DPR, raster: [], text: [] };

  await load(page);
  await page.screenshot({ path: path.join(OUT, 'composite.png') });

  for (const [i, l] of RASTER.entries()) {
    await load(page); await isolate(page, l.show, l.keepBg);
    const file = `r${i}.png`;
    await page.screenshot({ path: path.join(OUT, file), omitBackground: !l.keepBg });
    manifest.raster.push({ name: l.name, file });
  }

  for (const [i, [name, sel]] of TEXT.entries()) {
    await load(page);
    const spec = await page.evaluate(({ sel, DPR }) => {
      const el = document.querySelector(sel);
      const spans = [...el.querySelectorAll('.__t')];
      const rgb = (c) => { const m = c.match(/[\d.]+/g).map(Number); return { r: m[0], g: m[1], b: m[2], a: m.length > 3 ? m[3] : 1 }; };
      // baseline: zero-height inline-block probe at the start of the first text span
      const probe = document.createElement('span'); probe.style.cssText = 'display:inline-block;width:0;height:0;vertical-align:baseline';
      spans[0].insertBefore(probe, spans[0].firstChild);
      const baseline = probe.getBoundingClientRect().top; probe.remove();
      const range = document.createRange(); range.setStartBefore(spans[0].firstChild); range.setEndAfter(spans[spans.length - 1].lastChild);
      const left = range.getBoundingClientRect().left;
      const runs = spans.map((s) => {
        const cs = getComputedStyle(s); const fill = cs.webkitTextFillColor || cs.color;
        return { text: s.textContent, family: cs.fontFamily.split(',')[0].replace(/["']/g, '').trim(), weight: +cs.fontWeight,
                 size: parseFloat(cs.fontSize) * DPR, letterSpacing: parseFloat(cs.letterSpacing) * DPR || 0,
                 color: rgb(cs.color), transparent: rgb(fill).a === 0 };
      });
      return { x: left * DPR, baseline: baseline * DPR, runs };
    }, { sel, DPR });
    // show the line's own box (the chrome title paints its gradient from it) and its text, not its icons
    await page.addStyleTag({ content: `html,body,.f{background:transparent !important} .f *{visibility:hidden !important}
      ${sel}, ${sel} .__t, ${sel} .__t *{visibility:visible !important}` });
    const file = `t${i}.png`;
    await page.screenshot({ path: path.join(OUT, file), omitBackground: true });
    manifest.text.push({ name, file, ...spec });
  }
  fs.writeFileSync(path.join(OUT, 'manifest.json'), JSON.stringify(manifest, null, 2));
  await browser.close();
  console.log(`exported ${manifest.raster.length} raster + ${manifest.text.length} text layers to ${OUT}`);
})();
