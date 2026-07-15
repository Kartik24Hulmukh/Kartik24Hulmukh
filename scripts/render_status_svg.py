#!/usr/bin/env python3
import json, os, urllib.request, urllib.error
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN = os.environ.get('GH_TOKEN', '')


def api(repo):
    req = urllib.request.Request('https://api.github.com/repos/' + repo, headers={
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'kartik-profile-svg',
        **({'Authorization': f'Bearer {TOKEN}'} if TOKEN else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.load(r)
    except Exception:
        return {}


def main():
    projects = json.loads((ROOT/'data/projects.json').read_text())['projects']
    rows = []
    for p in projects:
        meta = api(p['repo'])
        rows.append((p['name'], p['display_status'].upper(), meta.get('updated_at','')[:10] or 'NOT CHECKED'))

    row_svg = []
    y = 250
    for name, status, updated in rows:
        row_svg.append(f'<text x="78" y="{y}" class="project">{escape(name)}</text>')
        row_svg.append(f'<text x="790" y="{y}" class="status">{escape(status)}</text>')
        row_svg.append(f'<text x="1060" y="{y}" class="date">{escape(updated)}</text>')
        row_svg.append(f'<line x1="78" y1="{y+24}" x2="1202" y2="{y+24}" class="rule"/>')
        y += 68

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640" role="img" aria-labelledby="title desc">
<title id="title">Kartik Hulmukh — current work</title>
<desc id="desc">A restrained mission-control view of four current software projects and their honest lifecycle status.</desc>
<style>
  .bg{{fill:#0d1117}} .accent{{fill:#5e9fe8}} .title{{font:700 48px Arial,sans-serif;fill:#f0f6fc;letter-spacing:-1px}}
  .subtitle{{font:20px Arial,sans-serif;fill:#9da7b3}} .label{{font:700 13px Arial,sans-serif;fill:#5e9fe8;letter-spacing:2px}}
  .project{{font:600 22px Arial,sans-serif;fill:#f0f6fc}} .status{{font:700 15px Consolas,monospace;fill:#8bd3a8;letter-spacing:1px}}
  .date{{font:14px Consolas,monospace;fill:#7d8590}} .rule{{stroke:#30363d;stroke-width:1}}
  .motto{{font:700 19px Consolas,monospace;fill:#c9d1d9;letter-spacing:1px}}
</style>
<rect class="bg" width="1280" height="640" rx="20"/>
<rect class="accent" x="0" y="0" width="12" height="640" rx="6"/>
<text x="78" y="84" class="label">CURRENT WORK / PUBLIC STATUS</text>
<text x="78" y="145" class="title">Kartik Hulmukh</text>
<text x="78" y="182" class="subtitle">Useful software for communities and systems that need to be inspectable.</text>
<text x="78" y="216" class="label">PROJECT</text><text x="790" y="216" class="label">STATE</text><text x="1060" y="216" class="label">UPDATED</text>
{''.join(row_svg)}
<text x="78" y="575" class="motto">BUILD  →  TEST  →  EXPLAIN  →  IMPROVE</text>
</svg>"""
    (ROOT/'assets').mkdir(exist_ok=True)
    (ROOT/'assets/mission-control.svg').write_text(svg, encoding='utf-8')

if __name__ == '__main__':
    main()
