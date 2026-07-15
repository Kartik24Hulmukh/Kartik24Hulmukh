#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]; errors=[]
for f in ['data/projects.json','data/claims.json','data/now.json','data/snapshot.json']:
 try: json.loads((root/f).read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'{f}: {e}')
md=(root/'README.md').read_text(encoding='utf-8')
for token in ['<!-- NOW:START -->','<!-- NOW:END -->','assets/build-console.svg','assets/telemetry.svg']:
 if md.count(token)!=1: errors.append(f'Expected exactly one {token}')
for f in ['assets/build-console.svg','assets/project-rgit.svg','assets/project-kairo.svg','assets/telemetry.svg']:
 if not (root/f).exists(): errors.append(f'Missing {f}')
if re.search(r'(?i)unhackable|100% secure|industry-leading|prompt-injection-proof',md): errors.append('Forbidden overclaim in README')
if errors: print('\n'.join(errors)); sys.exit(1)
print('Profile validation passed.')
