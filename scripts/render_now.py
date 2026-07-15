#!/usr/bin/env python3
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]; readme=root/'README.md'
text=readme.read_text(encoding='utf-8'); a='<!-- NOW:START -->'; b='<!-- NOW:END -->'
items=json.loads((root/'data/now.json').read_text(encoding='utf-8'))['items']
block=a+'\n'+'\n'.join('- '+x for x in items)+'\n'+b
start=text.index(a); end=text.index(b,start)+len(b)
readme.write_text(text[:start]+block+text[end:], encoding='utf-8')
