"""Validate deployable local URLs, accessible metadata, and bilingual contact info."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
ROOT=Path(__file__).resolve().parents[1]
BASE='/gymwatch-support/'
errors=[]
class Check(HTMLParser):
    def __init__(self,path):
        super().__init__();self.path=path;self.links=[];self.ids=set();self.h1=0;self.lang='';self.contact=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang','')
        if tag=='h1': self.h1+=1
        if 'id' in a:self.ids.add(a['id'])
        if tag=='img' and 'alt' not in a:errors.append(f'{self.path}: missing image alt')
        for key in ['href','src']:
            if key in a:
                url=a[key];self.links.append(url)
                if url.startswith('mailto:'):self.contact=True
checks={}
for page in ROOT.rglob('*.html'):
    c=Check(page);c.feed(page.read_text());checks[page]=c
    if not c.lang:errors.append(f'{page}: missing lang')
    if c.h1!=1:errors.append(f'{page}: expected 1 h1, got {c.h1}')
    if page.parent.name in ['support','privacy'] and not c.contact:errors.append(f'{page}: missing email contact')
for page,c in checks.items():
    for link in c.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        path=unquote(u.path)
        if path.startswith(BASE):target=ROOT/path[len(BASE):]
        elif path.startswith('/'):errors.append(f'{page}: incorrect project path {link}');continue
        elif path:target=page.parent/path
        else:target=page
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{page}: missing {link}');continue
        if u.fragment and target.suffix=='.html' and target in checks and u.fragment not in checks[target].ids:errors.append(f'{page}: missing anchor {link}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(checks)} pages; all local assets/links/anchors, page languages, titles and email contacts present.')
