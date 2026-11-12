/* ŠTĚPAŘ legal iframe sizing. Install once in the shared e-shop HTML template. */
(() => {
  'use strict';
  if (window.__steparLegalParentV1) return;
  window.__steparLegalParentV1 = true;
  const origin = 'https://vaclavstepar.github.io';
  const managedPath = /^\/stepar-legal\/[a-z]{2}\/[a-z][a-z0-9-]*\.html$/;
  const registered = new WeakSet();
  function source(frame) {
    try {
      const url = new URL(frame.getAttribute('src') || '', document.baseURI);
      return url.origin === origin && managedPath.test(url.pathname) ? url : null;
    } catch (_) { return null; }
  }
  function request(frame) {
    if (source(frame) && frame.contentWindow) {
      frame.contentWindow.postMessage({ type: 'stepar-legal:measure' }, origin);
    }
  }
  function scan() {
    document.querySelectorAll('iframe[src]').forEach(frame => {
      if (!source(frame) || registered.has(frame)) return;
      registered.add(frame);
      frame.addEventListener('load', () => request(frame));
      request(frame);
    });
  }
  window.addEventListener('message', event => {
    if (event.origin !== origin) return;
    const data = event.data;
    if (!data || !['stepar-legal:height', 'stepar-legal-height'].includes(data.type)) return;
    const height = data.height;
    if (typeof height !== 'number' || !Number.isFinite(height) || height < 1 || height > 120000) return;
    const frame = Array.from(document.querySelectorAll('iframe[src]')).find(item =>
      source(item) && item.contentWindow === event.source);
    if (!frame) return;
    const value = Math.ceil(height) + 'px';
    frame.style.setProperty('height', value, 'important');
    frame.style.setProperty('min-height', '0px', 'important');
    frame.style.setProperty('max-height', 'none', 'important');
    frame.setAttribute('height', String(Math.ceil(height)));
    frame.setAttribute('scrolling', 'no');
    frame.style.setProperty('overflow', 'hidden');
  });
  function start() {
    scan();
    new MutationObserver(scan).observe(document.documentElement, {
      childList: true, subtree: true, attributes: true, attributeFilter: ['src']
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
  window.addEventListener('resize', () => document.querySelectorAll('iframe[src]').forEach(request));
})();
