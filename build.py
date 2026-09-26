"""content.json + template.html -> public/index.html. Standard library only."""
from pathlib import Path
import json
from html import escape

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
def e(value):
    return escape(value, quote=True)
cards = []
for n, p in enumerate(data['projects'], 1):
    tags = ''.join(f'<li>{e(t)}</li>' for t in p['tags'])
    detail_link = f'<a class="case-link" href="{e(p["detail"])}">{e(p.get("detailLabel", "設計・実装・運用の詳細を見る →"))}</a>' if p.get('detail') else ''
    cards.append(f'''<article class="project {e(p['id'])}" data-category="{e(p['category'])}">
    <div class="project-art" aria-hidden="true"><span class="art-label">{n:02d} / {e(p['category'])}</span><div class="art-title">{e(p['title']).replace(chr(10), '<br>')}</div><span class="art-caption">{ 'INDEPENDENT FILM · 39 MIN' if p['id']=='film' else 'KOKI YOSHIKAWA / SELECTED WORK' }</span></div>
    <div class="project-body"><p class="eyebrow">{e(p['type'])}</p><h3>{e(p['name'])}</h3><p>{e(p['description'])}</p><ul class="tags">{tags}</ul>{detail_link}</div></article>''')
page = (ROOT / 'template.html').read_text(encoding='utf-8')
for key in ('name','nameEn','headline','intro','about','email'):
    page = page.replace('{{'+key+'}}', e(data[key]).replace('\n','<br>'))
page = page.replace('{{projects}}', '\n'.join(cards))
assert '{{' not in page, 'Unresolved template field'
out = ROOT / 'public'
out.mkdir(exist_ok=True)
(out / 'index.html').write_text(page, encoding='utf-8')
for name in ('style.css','app.js','training.html','training-flow.svg','training-timeline.svg','training-avatar.svg','halucination.html','film.js','pixverse.html','domo-ads.html','voice.html'):
    (out / name).write_text((ROOT / name).read_text(encoding='utf-8'), encoding='utf-8')
print(f'Built {len(cards)} projects: {out / "index.html"}')
