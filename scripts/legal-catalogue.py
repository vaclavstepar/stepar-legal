"""Build the published document catalogue from exact current source files."""
import hashlib, json, os, re
from html import unescape
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
COUNTRIES={'cz','sk','pl','ro','hu','de','es','fr','hr','bg','si','at'}
def build(root, commit):
    docs=[]
    for source in sorted(root.glob('*/*-current.html')):
        country=source.parent.name
        if country not in COUNTRIES: continue
        slug=source.name.removesuffix('-current.html')
        if not re.fullmatch('[a-z][a-z0-9-]*',slug): raise ValueError(source)
        loader=source.with_name(slug+'.html')
        if not loader.is_file(): raise ValueError('Missing stable iframe: '+str(source))
        raw=source.read_bytes(); html=raw.decode('utf-8')
        match=re.search(r'<title[^>]*>(.*?)</title>',html,re.I|re.S)
        title=unescape(re.sub('<[^>]+>','',match[1])).strip() if match else slug
        docs.append(dict(country=country.upper(),slug=slug,title=title,path=source.relative_to(root).as_posix(),iframePath=loader.relative_to(root).as_posix(),sha256=hashlib.sha256(raw).hexdigest(),size=len(raw)))
    if not docs: raise ValueError('Empty legal catalogue')
    return dict(schema=1,commit=commit,documents=docs)
if __name__=='__main__':
    commit=os.environ.get('GITHUB_SHA','')
    if not re.fullmatch('[a-f0-9]{40}',commit): raise ValueError('GITHUB_SHA is required')
    (ROOT/'catalogue.json').write_text(json.dumps(build(ROOT,commit),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
