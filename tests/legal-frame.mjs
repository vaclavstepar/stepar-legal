import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const parentCode = fs.readFileSync(new URL('../assets/legal-parent.js', import.meta.url), 'utf8');
const clientCode = fs.readFileSync(new URL('../assets/legal-loader.js', import.meta.url), 'utf8');

// Run the parent in an isolated DOM stub: no browser, network or customer data.
const listeners = {}, observers = [], frames = [];
function frame(src) {
  const attrs = { src, height: '12000' }, css = { height: '12000px', 'min-height': '6000px' };
  return { attrs, css, getAttribute: key => attrs[key], setAttribute: (key, value) => { attrs[key] = value; },
    style: { setProperty: (key, value) => { css[key] = value; } },
    contentWindow: { postMessage: () => {} }, addEventListener: () => {} };
}
frames.push(frame('https://vaclavstepar.github.io/stepar-legal/de/op.html'));
frames.push(frame('https://vaclavstepar.github.io/other-repository/de/op.html'));
frames.push(frame('https://vaclavstepar.github.io/stepar-legal/cz/op.html'));
const win = { addEventListener: (key, fn) => { (listeners[key] ||= []).push(fn); } };
const doc = { baseURI: 'https://www.stepar.cz/', readyState: 'complete', documentElement: {}, querySelectorAll: () => frames };
class Observer { constructor(cb) { observers.push(cb); } observe() {} }
const sandbox = { window: win, document: doc, MutationObserver: Observer, URL, WeakSet, Array, Math, Number };
vm.runInNewContext(parentCode, sandbox);
function message(origin, source, height) { for (const fn of listeners.message) fn({ origin, source, data: { type: 'stepar-legal:height', height } }); }
message('https://evil.example', frames[0].contentWindow, 200);
message('https://vaclavstepar.github.io', {}, 200);
message('https://vaclavstepar.github.io', frames[1].contentWindow, 200);
assert.equal(frames[0].css.height, '12000px');
assert.equal(frames[1].css.height, '12000px');
message('https://vaclavstepar.github.io', frames[0].contentWindow, 802);
assert.equal(frames[0].css.height, '802px');
assert.equal(frames[0].css['min-height'], '0px');
assert.equal(frames[0].attrs.scrolling, 'no');
message('https://vaclavstepar.github.io', frames[0].contentWindow, 202);
assert.equal(frames[0].css.height, '202px', 'Legacy fixed/minimum heights must shrink');
assert.equal(frames[2].css.height, '12000px', 'Only the sending frame may change');
for (const invalid of [0, -1, NaN, Infinity, '80', 120001]) message('https://vaclavstepar.github.io', frames[0].contentWindow, invalid);
assert.equal(frames[0].css.height, '202px');
vm.runInNewContext(parentCode, sandbox);
assert.equal(listeners.message.length, 1, 'Repeated snippets must share a single receiver');

// The child must measure intrinsic body height, never the old iframe viewport.
let bodyHeight = 200, width = 900;
const queue = [], sent = [], resizeCallbacks = [], childListeners = {}, styles = [];
const parent = { postMessage: payload => sent.push(payload) };
const body = { getBoundingClientRect: () => ({ height: bodyHeight }), dataset: {} };
const childDoc = {
  currentScript: { dataset: { document: 'op-current.html' } },
  body, documentElement: { get clientWidth() { return width; }, scrollHeight: 12000 },
  head: { appendChild: item => styles.push(item) }, createElement: () => ({}),
  open() {}, write() {}, close() {}, addEventListener() {}
};
const childWin = { innerHeight: 12000, addEventListener: (key, fn) => { childListeners[key] = fn; } };
class ChildResize { constructor(cb) { resizeCallbacks.push(cb); } observe() {} }
class Parser { parseFromString() { return { documentElement: { outerHTML: '<html><body><p>Text</p></body></html>' }, querySelectorAll: () => [] }; } }
const childSandbox = { window: childWin, document: childDoc, parent, location: { href: 'https://vaclavstepar.github.io/stepar-legal/de/op.html', origin: 'https://vaclavstepar.github.io' }, URL, Date, Math, Number,
  MutationObserver: Observer, ResizeObserver: ChildResize, DOMParser: Parser,
  requestAnimationFrame: fn => queue.push(fn), fetch: async () => ({ ok: true, text: async () => '<html><body><p>Text</p></body></html>' }) };
vm.runInNewContext(clientCode, childSandbox);
await new Promise(resolve => setImmediate(resolve));
function flush() { let n = 0; while (queue.length) { assert.ok(n++ < 10, 'No resize feedback loop'); queue.shift()(); } }
flush();
assert.equal(sent.at(-1).height, 202);
assert.ok(styles[0].textContent.includes('text-align:justify'));
bodyHeight = 80; resizeCallbacks[0](); flush();
assert.equal(sent.at(-1).height, 82, 'Smaller content must shrink even inside a 12000px viewport');
bodyHeight = 650; resizeCallbacks[0](); flush();
assert.equal(sent.at(-1).height, 652, 'Wrapping/fonts/images may grow the frame');
const count = sent.length;
childListeners.message({ source: {}, data: { type: 'stepar-legal:measure' } }); flush();
assert.equal(sent.length, count);
childListeners.message({ source: parent, data: { type: 'stepar-legal:measure' } }); flush();
assert.equal(sent.length, count + 2, 'Late-loaded parent must receive a fresh measurement');
width = 0; bodyHeight = 0; resizeCallbacks[0](); flush();
assert.equal(sent.at(-1).height, 652, 'Hidden frames must not collapse to zero');
console.log('PASS: shrink/grow independent of viewport; secure exact-window/origin/path checks; rejects invalid heights; idempotent receiver; late parent and hidden frames.');
