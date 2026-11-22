// Render flyer HTML files to PNG: node render.js flyer1-gate.html [more.html]
// SCALE=<factor> SUFFIX=<text> override the 2x output, e.g. 4K portrait: SCALE=2.8444 SUFFIX=-4k
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const scale = Number(process.env.SCALE || 2);
  const suffix = process.env.SUFFIX || '';
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: scale });
  for (const file of process.argv.slice(2)) {
    await page.goto('file://' + path.resolve(__dirname, file));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    const out = path.resolve(__dirname, '..', path.basename(file, '.html') + suffix + '.png');
    await page.screenshot({ path: out, timeout: 300000 });  // heavy filters are slow at 4K
    console.log('rendered', out);
  }
  await browser.close();
})();
