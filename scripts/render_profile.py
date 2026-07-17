#!/usr/bin/env python3
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'docs/data/evidence.json').read_text())
OUT=ROOT/'assets'; OUT.mkdir(exist_ok=True)

def make(dark):
 bg='#0b0d0f' if dark else '#f2eee6'; ink='#f0eadf' if dark else '#17191b'; muted='#8c989f' if dark else '#59636a'; frame='#8b673f' if dark else '#9a6b37'; grid='#2c3439' if dark else '#d2cbc0'
 colors=[p['color'] for p in DATA['projects']]
 paths=[]
 for i,p in enumerate(DATA['projects']):
  y=205+i*80; c=colors[i]; label=html.escape(p['name']); maturity=html.escape(p['maturity'].upper());
  paths.append(f'<path d="M100 {y} C320 {y-18} 490 {y+24} 730 {y-8} S980 {y+18} 1100 {y}" fill="none" stroke="{c}" stroke-width="5"/><circle cx="100" cy="{y}" r="7" fill="{c}"/><text x="126" y="{y-14}" class="small" fill="{muted}">0{i+1} / {maturity}</text><text x="126" y="{y+18}" class="label" fill="{ink}">{label}</text>')
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="650" viewBox="0 0 1200 650" role="img" aria-labelledby="t d"><title id="t">The Proof Loom</title><desc id="d">Four project strands pass through a mechanical evidence loom from source to boundary.</desc><style>.title{{font:700 58px Georgia,serif;letter-spacing:-1.5px}}.sub{{font:18px Arial,sans-serif}}.small{{font:11px Arial,sans-serif;letter-spacing:1.4px}}.label{{font:700 18px Georgia,serif}}</style><rect width="1200" height="650" fill="{bg}"/><path d="M54 108H1146" stroke="{grid}"/><text x="54" y="70" class="small" fill="{frame}">KARTIK HULMUKH / PUBLIC EVIDENCE INSTRUMENT / JULY 2026</text><text x="54" y="155" class="title" fill="{ink}">THE PROOF LOOM</text><text x="735" y="132" class="sub" fill="{muted}">Pull the claim. Inspect the strand.</text><text x="735" y="160" class="sub" fill="{frame}">Break the evidence.</text><rect x="75" y="182" width="1050" height="352" fill="none" stroke="{frame}" stroke-width="4"/><path d="M75 182v352M1125 182v352" stroke="{frame}" stroke-width="14"/>{''.join(paths)}<path d="M460 190v330" stroke="{frame}" stroke-width="22"/><path d="M448 190h24l-5 330h-14z" fill="{frame}"/><text x="54" y="590" class="small" fill="{muted}">SOURCE</text><text x="350" y="590" class="small" fill="{muted}">CLAIM</text><text x="650" y="590" class="small" fill="{muted}">TEST</text><text x="980" y="590" class="small" fill="{muted}">BOUNDARY</text><text x="54" y="625" class="small" fill="{muted}">OPERATE THE INTERACTIVE MODEL → kartik24hulmukh.github.io/Kartik24Hulmukh/</text></svg>'''
for dark in (False,True):
 (OUT/f'proof-loom-{"dark" if dark else "light"}.svg').write_text(make(dark),encoding='utf-8')
print('Rendered profile assets.')
