/* Shared display layer. Does not edit the approved *-current.html source. */
(() => {
  'use strict';
  const script = document.currentScript;
  const file = script && script.dataset.document;
  if (!file || !/^[a-z][a-z0-9-]*-current\.html$/.test(file)) return;
  const source = new URL(file, location.href);
  if (source.origin !== location.origin) return;
  const layout = `
    html,body{height:auto!important;min-height:0!important;margin:0!important;padding:0!important}
    body{display:flow-root!important}
    main,.terms,.loading{padding-bottom:0!important;margin-bottom:0!important;min-height:0!important}
    main>:last-child,.terms>:last-child,.loading>:last-child{margin-bottom:0!important}
    p,li{text-align:justify!important;text-align-last:start!important;hyphens:auto;overflow-wrap:break-word}
    h1,h2,h3,h4,h5,h6{text-align:start!important}
  `;
  function install() {
    const style = document.createElement('style');
    style.id = 'stepar-legal-layout';
    style.textContent = layout;
    document.head.appendChild(style);
    let scheduled = false, force = false, previous = -1;
    function send() {
      scheduled = false;
      if (!document.body || document.documentElement.clientWidth < 1) return;
      // scrollHeight on <html> includes the OLD iframe viewport and cannot shrink.
      const height = Math.ceil(document.body.getBoundingClientRect().height) + 2;
      if (height < 2 || height > 120000 || (!force && height === previous)) return;
      previous = height;
      force = false;
      // Legacy snippets receive an intrinsic size too; the new global listener
      // receives the final message after any older per-frame +24px handler.
      parent.postMessage({ type: 'stepar-legal-height', height }, '*');
      parent.postMessage({ type: 'stepar-legal:height', height }, '*');
    }
    function schedule(always = false) {
      force = force || always;
      if (!scheduled) { scheduled = true; requestAnimationFrame(send); }
    }
    if (typeof ResizeObserver !== 'undefined') new ResizeObserver(() => schedule()).observe(document.body);
    new MutationObserver(() => schedule()).observe(document.body, {
      childList: true, subtree: true, characterData: true, attributes: true
    });
    window.addEventListener('resize', () => schedule());
    window.addEventListener('load', () => schedule(true));
    document.addEventListener('load', () => schedule(), true);
    if (document.fonts) {
      document.fonts.ready.then(() => schedule(true));
      if (document.fonts.addEventListener) document.fonts.addEventListener('loadingdone', () => schedule(true));
    }
    window.addEventListener('message', event => {
      if (event.source === parent && event.data && event.data.type === 'stepar-legal:measure') schedule(true);
    });
    schedule(true);
  }
  (async () => {
    try {
      source.searchParams.set('_legal', String(Date.now()));
      const response = await fetch(source.href, { cache: 'no-store', credentials: 'omit' });
      if (!response.ok) throw new Error('HTTP ' + response.status);
      const html = await response.text();
      // Old inline height observers used viewport scrollHeight. Remove only
      // those display helpers from the rendered copy, preserving source bytes.
      const doc = new DOMParser().parseFromString(html, 'text/html');
      doc.querySelectorAll('script').forEach(item => {
        if (item.textContent.includes('stepar-legal-height') && item.textContent.includes('postMessage')) item.remove();
      });
      document.open();
      document.write('<!doctype html>\n' + doc.documentElement.outerHTML);
      document.close();
      install();
    } catch (error) {
      document.body.dataset.legalLoadError = String(error);
      install();
      // A direct-document link remains in the loader even when loading fails.
    }
  })();
})();
