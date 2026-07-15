#!/usr/bin/env python3
from pathlib import Path
import json, os, urllib.request, datetime, tempfile

ROOT = Path(__file__).resolve().parents[1]
projects = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))["projects"]
token = os.environ.get("GITHUB_TOKEN", "")
headers = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "kartik-profile-evidence",
}
if token:
    headers["Authorization"] = "Bearer " + token


def get(url):
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


snapshot = {
    "collected_at": datetime.datetime.now(datetime.timezone.utc)
    .isoformat()
    .replace("+00:00", "Z"),
    "projects": [],
}

for project in projects:
    repo = project["repository"]
    api = "https://api.github.com/repos/" + repo
    info = get(api)
    branch = info["default_branch"]
    commit = get(api + "/commits/" + branch)
    runs = get(
        api
        + "/actions/runs?branch="
        + branch
        + "&status=completed&per_page=1"
    ).get("workflow_runs", [])
    releases = get(api + "/releases?per_page=5")
    release = next(
        (
            item["tag_name"]
            for item in releases
            if not item["draft"] and not item["prerelease"]
        ),
        None,
    )
    snapshot["projects"].append(
        {
            "id": project["id"],
            "repository": repo,
            "revision": commit["sha"][:7],
            "ci": runs[0]["conclusion"] if runs else "unknown",
            "release": release,
        }
    )

path = ROOT / "data/snapshot.json"
with tempfile.NamedTemporaryFile(
    "w", delete=False, dir=path.parent, encoding="utf-8"
) as handle:
    json.dump(snapshot, handle, indent=2)
    handle.write("\n")
    temporary_path = handle.name
Path(temporary_path).replace(path)
