// Draws the profile README images: opens tools/profile-art.html in headless Chrome at desktop and
// phone widths and saves every card to assets/v10/ as WebP (Chrome encodes them, so no packages).
// usage: node tools/capture.mjs   (set CHROME to the browser binary if it is not in the usual place)
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const ROOT = resolve(import.meta.dirname, '..');
const OUT = join(ROOT, 'assets/v10');
const PAGE = pathToFileURL(join(ROOT, 'tools/profile-art.html')).href;
const CARDS = ['hero', 'work', 'experience', 'stack', 'contact'];
// Both come out 1800 px wide. Phones get a narrower page, so their text is drawn larger relative
// to the image and stays readable once GitHub shrinks it to the screen.
const SIZES = [{ suffix: '', width: 1600, scale: 1.125 }, { suffix: '-mobile', width: 560, scale: 3.2142857 }];
const DEVTOOLS = 9339;

const CHROME = process.env.CHROME || ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium'].find(existsSync);
if (!CHROME) throw new Error('Chrome not found; set CHROME to its binary');
if (!existsSync(join(ROOT, '../codehorizon/public/assets/fonts'))) throw new Error('expected the codehorizon repo next to this one, for fonts and screenshots');

const sleep = ms => new Promise(r => setTimeout(r, ms));
const profile = mkdtempSync(join(tmpdir(), 'profile-art-'));
// File access lets the page load the fonts and images from the codehorizon checkout beside it.
const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${DEVTOOLS}`, `--user-data-dir=${profile}`, '--hide-scrollbars',
  '--allow-file-access-from-files', '--no-first-run', '--no-default-browser-check', 'about:blank'], { stdio: 'ignore' });

try {
  let target;
  for (let i = 0; i < 60 && !target; i++) {
    await sleep(250);
    try { target = (await (await fetch(`http://127.0.0.1:${DEVTOOLS}/json/list`)).json()).find(t => t.type === 'page'); } catch { /* not up yet */ }
  }
  if (!target) throw new Error('Chrome did not start');
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((r, e) => { ws.onopen = r; ws.onerror = e; });
  let id = 0;
  const waiting = new Map();
  ws.onmessage = e => {
    const m = JSON.parse(e.data);
    if (!waiting.has(m.id)) return;
    const { ok, fail } = waiting.get(m.id);
    waiting.delete(m.id);
    m.error ? fail(new Error(m.error.message)) : ok(m.result);
  };
  const send = (method, params = {}) => new Promise((ok, fail) => { waiting.set(++id, { ok, fail }); ws.send(JSON.stringify({ id, method, params })); });
  const run = async js => (await send('Runtime.evaluate', { expression: js, awaitPromise: true, returnByValue: true })).result.value;

  mkdirSync(OUT, { recursive: true });
  await send('Page.enable');
  // Transparent behind the cards, so their rounded corners sit cleanly on GitHub's light and dark themes.
  await send('Emulation.setDefaultBackgroundColorOverride', { color: { r: 0, g: 0, b: 0, a: 0 } });
  for (const size of SIZES) {
    await send('Emulation.setDeviceMetricsOverride', { width: size.width, height: 1000, deviceScaleFactor: size.scale, mobile: false });
    await send('Page.navigate', { url: PAGE });
    await sleep(1500);
    await run('document.fonts.ready.then(() => true)');
    const height = await run('document.documentElement.scrollHeight');
    await send('Emulation.setDeviceMetricsOverride', { width: size.width, height, deviceScaleFactor: size.scale, mobile: false });
    await sleep(500);
    for (const card of CARDS) {
      const clip = await run(`(({ x, y, width, height }) => ({ x, y, width, height, scale: 1 }))(document.getElementById('${card}').getBoundingClientRect())`);
      const { data } = await send('Page.captureScreenshot', { format: 'webp', quality: 88, clip });
      const name = `${card}${size.suffix}.webp`;
      writeFileSync(join(OUT, name), Buffer.from(data, 'base64'));
      console.log(`assets/v10/${name}  ${Math.round(Buffer.byteLength(data, 'base64') / 1024)} KB`);
    }
  }
  ws.close();
} finally {
  if (chrome.exitCode === null) await new Promise(r => { chrome.once('exit', r); chrome.kill(); });
  rmSync(profile, { recursive: true, force: true, maxRetries: 5 });
}
