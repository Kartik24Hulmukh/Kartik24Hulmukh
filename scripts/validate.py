#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,yaml
ROOT=Path(__file__).resolve().parents[1]; errors=[]
try:data=json.loads((ROOT/'docs/data/evidence.json').read_text())
except Exception as e: data={}; errors.append(f'evidence.json: {e}')
projects=data.get('projects',[])
if len(projects)!=4: errors.append('Expected exactly four public project records')
required={'id','name','role','maturity','statement','repository','commit','evidence','boundaries','challenges'}
for i,p in enumerate(projects):
 missing=required-set(p)
 if missing: errors.append(f'Project {i} missing {sorted(missing)}')
 if not p.get('evidence'): errors.append(f'Project {i} has no evidence')
 if not p.get('boundaries'): errors.append(f'Project {i} has no boundaries')
 if not str(p.get('repository','')).startswith('https://github.com/'): errors.append(f'Project {i} repository must be GitHub HTTPS')
for f in ['README.md','docs/index.html','docs/styles.css','docs/app.js','assets/proof-loom-light.svg','assets/proof-loom-dark.svg']:
 if not (ROOT/f).exists(): errors.append('Missing '+f)
readme=(ROOT/'README.md').read_text()
for bad in ['unhackable','100% secure','industry-leading','prompt-injection-proof','independently validated system']:
 if bad.lower() in readme.lower(): errors.append('Forbidden claim: '+bad)
html=(ROOT/'docs/index.html').read_text()
for token in ['id="direct-index"','id="loom"','aria-live="polite"','Skip the interactive loom']:
 if token not in html: errors.append('HTML missing '+token)
for p in list((ROOT/'.github/workflows').glob('*.yml'))+list((ROOT/'.github/ISSUE_TEMPLATE').glob('*.yml')):
 try: yaml.safe_load(p.read_text())
 except Exception as e: errors.append(f'{p}: {e}')
if re.search(r'<script[^>]+src="https?://',html,re.I): errors.append('External script dependency found')
if errors:
 print('\n'.join(errors)); sys.exit(1)
print('Proof Loom validation passed.')
