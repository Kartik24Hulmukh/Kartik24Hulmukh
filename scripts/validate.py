#!/usr/bin/env python3
from pathlib import Path
import json,sys,re,yaml
R=Path(__file__).resolve().parents[1]; errors=[]
required=['README.md','assets/hero-light.svg','assets/hero-dark.svg','docs/index.html','docs/styles.css','docs/app.js','docs/data/projects.json']
for f in required:
 if not (R/f).exists():errors.append('Missing '+f)
try:d=json.loads((R/'docs/data/projects.json').read_text())
except Exception as e:d={};errors.append('JSON '+str(e))
if len(d.get('projects',[]))!=3:errors.append('Expected three projects')
for p in d.get('projects',[]):
 for k in ['id','name','role','maturity','summary','repo','boundary','interaction']:
  if not p.get(k):errors.append(f'{p.get("id","?")} missing {k}')
alltext='\n'.join(p.read_text(errors='ignore') for p in R.rglob('*') if p.is_file() and p.suffix in {'.md','.html','.css','.js','.json','.svg','.yml','.py'})
for bad in [('rgit'+' rozgar'),('unified'+'-experience')]:
 if bad.lower() in alltext.lower():errors.append('Excluded project reference found')
unsupported=[('guaranteed'+' selection'),('un'+'hackable'),('100%'+' secure'),('independently validated'+' system')]
for bad in unsupported:
 if bad.lower() in alltext.lower():errors.append('Unsupported phrase found')
for p in list((R/'.github').rglob('*.yml')):
 try:yaml.safe_load(p.read_text())
 except Exception as e:errors.append(f'{p}: {e}')
if re.search(r'<script[^>]+src=["\']https?://',(R/'docs/index.html').read_text(),re.I):errors.append('External script found')
if errors:print('\n'.join(errors));sys.exit(1)
print('Systems in Motion validation passed.')
