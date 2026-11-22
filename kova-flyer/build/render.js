// Render flyer HTML files to PNG: node render.js flyer1-gate.html [more.html]
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  for (const file of process.argv.slice(2)) {
    await page.goto('file://' + path.resolve(__dirname, file));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    const out = path.resolve(__dirname, '..', path.basename(file, '.html') + '.png');
    await page.screenshot({ path: out });
    console.log('rendered', out);
  }
  await browser.close();
})();
