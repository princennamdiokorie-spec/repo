// Render the Noir flyer with given query, then report ink bounds of each text block (css px).
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const q = process.argv[2], out = process.argv[3];
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.resolve('signature.html') + '?' + q); await p.evaluate(() => document.fonts.ready);
  await p.waitForLoadState('networkidle'); await p.waitForTimeout(500);
  const boxes = await p.evaluate(() => { const g = s => { const x = document.querySelector(s).getBoundingClientRect(); return [x.top, x.bottom]; };
    return { the: g('.v1 .the'), club: g('#club'), rl: g('.v1 .rl') }; });
  await p.screenshot({ path: out }); await b.close();
  console.log(JSON.stringify(boxes));
})();
