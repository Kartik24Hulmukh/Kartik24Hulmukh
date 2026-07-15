#!/usr/bin/env python3
import json, os, re, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- dynamic:start -->'
END = '<!-- dynamic:end -->'
API = 'https://api.github.com'
TOKEN = os.environ.get('GH_TOKEN', '')


def request_json(path):
    req = urllib.request.Request(API + path, headers={
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'kartik-profile-renderer',
        **({'Authorization': f'Bearer {TOKEN}'} if TOKEN else {}),
        'X-GitHub-Api-Version': '2022-11-28',
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return None


def esc(value):
    return str(value).replace('|', '\\|').replace('\n', ' ').strip()


def project_row(project):
    repo = project['repo']
    branch = project['branch']
    metadata = request_json(f'/repos/{repo}') or {}
    commit = request_json(f'/repos/{repo}/commits/{branch}') or {}
    runs = request_json(f'/repos/{repo}/actions/runs?branch={branch}&per_page=10') or {}
    releases = request_json(f'/repos/{repo}/releases/latest') or {}

    sha = (commit.get('sha') or '')[:7]
    revision = ('[`' + sha + '`](https://github.com/' + repo + '/commit/' + str(commit.get('sha')) + ')') if sha else 'unavailable'

    completed = [r for r in runs.get('workflow_runs', []) if r.get('status') == 'completed']
    if completed:
        run = completed[0]
        conclusion = run.get('conclusion') or 'unknown'
        ci = f'[{esc(conclusion)}]({run.get("html_url")})'
    else:
        ci = 'not published'

    tag = releases.get('tag_name')
    release = f'[{esc(tag)}]({releases.get("html_url")})' if tag else 'not published'
    return f'| {esc(project["name"])} | {revision} | {ci} | {release} |'


def main():
    readme = ROOT / 'README.md'
    text = readme.read_text(encoding='utf-8')
    if text.count(START) != 1 or text.count(END) != 1:
        raise SystemExit('README dynamic markers must each appear exactly once')

    projects = json.loads((ROOT / 'data/projects.json').read_text(encoding='utf-8'))['projects']
    rows = '\n'.join(project_row(p) for p in projects)
    block = (
        START
        + '\n## Live repository status\n\n'
        + "_This block is generated from GitHub's API. It reports repository state, not personal worth or activity theatre._\n\n"
        + '| Project | Revision | CI | Latest release |\n'
        + '|---|---|---|---|\n'
        + rows
        + '\n'
        + END
    )
    updated = re.sub(re.escape(START) + r'.*?' + re.escape(END), block, text, flags=re.S)
    readme.write_text(updated, encoding='utf-8')

if __name__ == '__main__':
    main()
