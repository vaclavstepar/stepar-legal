"""Render the six customer pages and operator iframe catalogue from reviewed JSON."""
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://vaclavstepar.github.io/stepar-legal/de/'
PAGES = [
 ('unternehmen', 'Über unser Unternehmen', 'Informationen für Kunden'),
 ('versand', 'Versand und Zahlung', 'Informationen für Kunden'),
 ('reklamace', 'Reklamationen', 'Informationen für Kunden'),
 ('online-widerrufen', 'Online widerrufen', 'Informationen für Kunden'),
 ('op', 'AGB', 'Rechtliche Informationen'),
 ('privacy', 'Datenschutzerklärung', 'Rechtliche Informationen'),
 ('otkaz', 'Widerrufsbelehrung', 'Rechtliche Informationen'),
 ('gewaehrleistung', 'Gesetzliche Gewährleistung und Verbraucherrechte', 'Rechtliche Informationen'),
]
RESIZE = """<script>(()=>{const send=()=>parent.postMessage({type:'stepar-legal-height',height:Math.ceil(document.documentElement.scrollHeight)},'*');new ResizeObserver(send).observe(document.body);addEventListener('load',send);send();})();</script>"""
STYLE = 'body{margin:0;font:15px/1.65 Arial,sans-serif;color:#222;background:transparent}main{max-width:1040px;padding:24px 18px 48px;margin:auto}h1{font-size:30px;line-height:1.2}h2{font-size:21px;line-height:1.3;margin-top:30px}p{white-space:pre-line;overflow-wrap:anywhere}a{color:inherit}img.notice{display:block;width:100%;max-width:900px;height:auto;margin:20px auto} @media print{main{padding:0}}'

def block(b):
    tag = {'title':'h1','heading':'h2','paragraph':'p'}[b['kind']]
    text = escape(b['text'])
    for link in b.get('links', []):
        text = text.replace(escape(link['text']), '<a href="'+escape(link['url'],quote=True)+'" target="_top" rel="noopener">'+escape(link['text'])+'</a>', 1)
    return '<'+tag+'>'+text+'</'+tag+'>'

pages = json.loads((ROOT/'de/customer-pages-source.json').read_text())
for key, blocks in pages.items():
    title = escape(blocks[0]['text'])
    html = '<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>'+title+'</title><style>'+STYLE+'</style></head><body><main>'
    if key == 'gewaehrleistung' and (ROOT/'de/eu-gewaehrleistung-de.svg').exists():
        html += block(blocks[0])+'<img class="notice" src="eu-gewaehrleistung-de.svg" alt="Harmonisierte EU-Mitteilung: mindestens zwei Jahre gesetzliche Gewährleistung; kostenlose Reparatur oder Ersatzlieferung und unter gesetzlichen Voraussetzungen Preisminderung oder Erstattung. Vollständige Erläuterungen folgen im Text.">'
        blocks = blocks[1:]
    html += '\n'.join(block(b) for b in blocks)+'</main>'+RESIZE+'</body></html>\n'
    (ROOT/f'de/{key}-current.html').write_text(html)
    archive = ROOT/f'archive/de/{key}-2026-11-12-v1.1.html'
    # This renderer is used for the unpublished initial customer-page edition only.
    if archive.exists() and archive.read_text() != html:
        raise RuntimeError("Refusing to overwrite archived text: " + str(archive))
    if not archive.exists():
        archive.write_text(html)
    (ROOT/f'de/{key}.html').write_text('<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>'+title+'</title></head><body><div class="loading"><p>Das Dokument wird geladen… <a href="'+key+'-current.html">Dokument direkt öffnen</a></p></div><script src="../assets/legal-loader.js" data-document="'+key+'-current.html"></script></body></html>\n')

def snippet(key, title):
    return '<iframe id="stepar-de-'+key+'" src="'+BASE+key+'.html" title="'+title+'" style="display:block;width:100%;height:600px;border:0;background:transparent" loading="eager"></iframe>\n<script src="https://vaclavstepar.github.io/stepar-legal/assets/legal-parent.js" defer></script>\n<p><a href="'+BASE+key+'-current.html" target="_blank" rel="noopener">Dokument separat öffnen, speichern oder drucken</a></p>'

parts=['<!doctype html><html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>www.stepar-med.de – stránky a iframe</title><style>body{font:16px/1.6 system-ui,sans-serif;margin:0;color:#222;background:#f4f5f6}main{max-width:1060px;margin:auto;padding:32px 20px}h1,h2{color:#74182c}article{background:white;border:1px solid #ddd;border-radius:10px;padding:20px;margin:16px 0}a{color:#74182c}textarea{width:100%;min-height:240px;box-sizing:border-box;font:13px/1.5 monospace;padding:12px}aside{background:#fff4d8;border:1px solid #ead08b;padding:16px;border-radius:8px}.meta{color:#555}summary,button{cursor:pointer}button{margin:12px 0;padding:9px 14px;border:0;border-radius:5px;background:#74182c;color:white}</style></head><body><main><h1>www.stepar-med.de – texty a iframe</h1><p class="meta">Připraveno 12. 11. 2026 · osm stránek ve dvou sekcích podle rakouského e-shopu.</p><aside><strong>Před spuštěním:</strong> texty nenahrazují nastavení obchodu. Na stránku Online widerrufen vložte pod úvod také nativní formulář Weby24 a ověřte finální potvrzení i e-mail. U dopravy nastavte GLS 6 €, zdarma při hodnotě zboží nad 200 €, pouze dobírku, GoPay a bankovní převod podle potvrzení vlastníka z 12. 11. 2026. Právní texty nejsou advokátní certifikací. <a href="https://github.com/vaclavstepar/stepar-legal/blob/main/docs/de-shopstart-2026-11-12.md">Podrobná kontrola před spuštěním</a>.</aside>']
last=None
for key,title,group in PAGES:
    if group!=last:parts.append('<h2>'+group+'</h2>');last=group
    code=snippet(key,title)
    (ROOT/f'de/iframe-{key}.txt').write_text(code+'\n')
    note='<p><strong>Jen úvodní text:</strong> samotný iframe nepřijímá odstoupení. Pod něj patří nativní formulář Online widerrufen z Weby24, jako u Rakouska.</p>' if key=='online-widerrufen' else ''
    parts.append('<article><h3>'+escape(title)+'</h3><p><a href="'+key+'.html" target="_blank" rel="noopener">Otevřít stránku</a> · <a href="iframe-'+key+'.txt">Samostatný kód iframe</a></p>'+note+'<details><summary>Zobrazit kód pro vložení</summary><textarea readonly aria-label="iframe '+escape(title)+'">'+escape(code)+'</textarea><button type="button" onclick="navigator.clipboard.writeText(this.previousElementSibling.value).then(()=>this.textContent=\'Zkopírováno\').catch(()=>this.textContent=\'Označte a zkopírujte kód ručně\')">Kopírovat iframe</button></details></article>')
parts.append('</main></body></html>\n')
(ROOT/'de/index.html').write_text(''.join(parts))
print('Rendered six pages and eight iframe snippets.')

