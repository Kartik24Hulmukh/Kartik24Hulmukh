#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
readme = (ROOT/'README.md').read_text(encoding='utf-8')

for marker in ('<!-- dynamic:start -->','<!-- dynamic:end -->'):
    if readme.count(marker) != 1:
        errors.append(f'{marker} must appear exactly once')

banned = [
    'passionate developer', 'cutting-edge', 'revolutionary', '10x engineer',
    '100x engineer', 'building the future', 'world-class', 'rockstar developer'
]
for phrase in banned:
    if phrase.lower() in readme.lower():
        errors.append(f'banned hype phrase found: {phrase}')

for path in ('data/projects.json','data/claims.json'):
    try: json.loads((ROOT/path).read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'{path}: {exc}')

for match in re.findall(r'\[[^\]]+\]\(([^)]+)\)', readme):
    if match.startswith('file:///'):
        errors.append(f'local file link found: {match}')

if errors:
    print('\n'.join(f'ERROR: {e}' for e in errors))
    sys.exit(1)
print('Profile validation passed')
