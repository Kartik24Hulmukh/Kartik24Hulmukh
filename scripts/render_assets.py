#!/usr/bin/env python3
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'assets'; A.mkdir(exist_ok=True)

def esc(x): return html.escape(str(x))
def shell(title, subtitle, body, h=260):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="{esc(title)}">
<style>:root{{color-scheme:light dark}}.bg{{fill:#0b0f14}}.panel{{fill:#111821;stroke:#263241}}.t{{fill:#f4f7fb;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}}.m{{fill:#8fa3b8;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}}.a{{fill:#66e3ff}}.g{{fill:#68e09b}}.o{{fill:#ffb86b}}.r{{fill:#ff7777}}@media(prefers-color-scheme:light){{.bg{{fill:#f7f9fc}}.panel{{fill:#fff;stroke:#dbe3ec}}.t{{fill:#16202b}}.m{{fill:#526579}}}}</style><rect class="bg" width="1200" height="{h}" rx="18"/><rect class="panel" x="20" y="20" width="1160" height="{h-40}" rx="14"/><text class="t" x="52" y="66" font-size="28" font-weight="700">{esc(title)}</text><text class="m" x="52" y="94" font-size="14">{esc(subtitle)}</text>{body}</svg>'''

body='''<circle class="g" cx="57" cy="43" r="5"/><text class="m" x="70" y="48" font-size="13">AVAILABLE / BUILDING IN PUBLIC</text><text class="t" x="52" y="148" font-size="48" font-weight="800">KARTIK // BUILD CONSOLE</text><text class="a" x="52" y="190" font-size="21">products for communities × systems that leave evidence</text><text class="m" x="52" y="226" font-size="15">Mumbai · build → test → explain → improve</text>'''
A.joinpath('build-console.svg').write_text(shell('BUILD SIGNAL / PROFILE ENTRY','Independent product and systems builder',body,280), encoding='utf-8')

def project(name, role, headline, status, accent):
 body=f'''<text class="{accent}" x="52" y="130" font-size="14">{esc(role.upper())}</text><text class="t" x="52" y="172" font-size="32" font-weight="700">{esc(headline)}</text><text class="m" x="52" y="213" font-size="15">STATUS: {esc(status.upper())}  ·  ROLE AND BOUNDARIES ARE PUBLIC</text><text class="t" x="1070" y="172" font-size="32">↗</text>'''
 return shell(name,'SELECTED BUILD / OPEN TO INSPECTION',body,250)
A.joinpath('project-rgit.svg').write_text(project('RGIT Rozgar','Founder · Product Engineer · Operator','A campus exchange built around participation and trust.','deployed','g'), encoding='utf-8')
A.joinpath('project-kairo.svg').write_text(project('Kairo-Phantom','Lead Builder · Maintainer','An offline AI agent that leaves evidence behind.','pre-launch','a'), encoding='utf-8')

snap=json.loads((ROOT/'data/snapshot.json').read_text(encoding='utf-8'))
y=130; rows=[]
for p in snap['projects']:
 cls='g' if p['ci']=='success' else ('r' if p['ci']=='failure' else 'o')
 rows.append(f'<text class="t" x="52" y="{y}" font-size="17">{esc(p["repository"])}</text><text class="m" x="650" y="{y}" font-size="15">{esc(p["revision"])}</text><circle class="{cls}" cx="900" cy="{y-6}" r="6"/><text class="{cls}" x="917" y="{y}" font-size="15">CI {esc(p["ci"]).upper()}</text>')
 y+=38
body=''.join(rows)+f'<text class="m" x="52" y="{y+14}" font-size="13">LAST VALID SNAPSHOT · {esc(snap["collected_at"])} · CLICK TO INSPECT JSON</text>'
A.joinpath('telemetry.svg').write_text(shell('LIVE ENGINEERING SIGNAL','ALLOWLISTED REPOSITORY STATE — NOT A PRODUCTIVITY SCORE',body,330), encoding='utf-8')
