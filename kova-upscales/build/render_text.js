// Render replacement text matched to the originals' measured cap height and width.
// Writes nameplate-text.png/.pos and venue-text.png/.pos in build/.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const PAGE = `<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;800&display=block" rel="stylesheet">
<style>
html,body{margin:0;background:transparent}
.t{position:absolute;left:40px;top:40px;white-space:nowrap}
.plate{font:800 200px/1 Montserrat,sans-serif;
  background:linear-gradient(180deg,#ffffff 0%,#f4f6fa 55%,#d9dee7 100%);-webkit-background-clip:text;background-clip:text;color:transparent;
  filter:drop-shadow(0 4px 0 #13265a) drop-shadow(1px 6px 0 #071433) drop-shadow(0 10px 8px rgba(0,0,0,.55))}
.venue{font:600 100px/1 Montserrat,sans-serif;color:#fff}
.venue .bar{display:inline-block;width:.07em;height:.72em;margin:0 .2em 0 0;background:#8cc4ff;box-shadow:0 0 .08em #3d8bff;vertical-align:-.02em}
</style></head><body><div class="t" id="t"></div></body></html>`;

async function capHeightAndWidth(page, cls, html, spacing) {
  await page.evaluate(([c, h, s]) => { const t = document.getElementById('t'); t.className = 't ' + c; t.innerHTML = h; t.style.letterSpacing = s + 'px'; }, [cls, html, spacing]);
  await page.evaluate(() => document.fonts.ready);
  const buf = await page.screenshot({ omitBackground: true, clip: { x: 0, y: 0, width: 4200, height: 420 } });
  return buf;
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 4200, height: 420 } });
  await page.setContent(PAGE); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(500);
  const jobs = JSON.parse(process.argv[2]);
  for (const j of jobs) {
    const buf = await capHeightAndWidth(page, j.cls, j.html, j.spacing);
    fs.writeFileSync(path.join(__dirname, j.out), buf);
  }
  await browser.close();
})();
