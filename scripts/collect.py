#!/usr/bin/env python3
"""Collect revision/CI/release state only for allowlisted repositories."""
from pathlib import Path
import json
import os
import urllib.request
import urllib.error
import datetime
import tempfile
import sys

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_PATH = ROOT / "data/projects.json"
SNAPSHOT_PATH = ROOT / "data/snapshot.json"

projects = json.loads(PROJECTS_PATH.read_text(encoding="utf-8"))["projects"]
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


def load_previous():
    if not SNAPSHOT_PATH.exists():
        return None
    try:
        return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None


previous = load_previous()
previous_by_id = {
    item.get("id"): item for item in (previous or {}).get("projects", []) if item.get("id")
}

snapshot = {
    "collected_at": datetime.datetime.now(datetime.timezone.utc)
    .isoformat()
    .replace("+00:00", "Z"),
    "projects": [],
}

failures = []

for project in projects:
    repo = project["repository"]
    project_id = project["id"]
    try:
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
                "id": project_id,
                "repository": repo,
                "revision": commit["sha"][:7],
                "ci": runs[0]["conclusion"] if runs else "unknown",
                "release": release,
            }
        )
    except Exception as exc:
        failures.append(f"{repo}: {exc}")
        # Preserve last valid project snapshot when collection fails.
        if project_id in previous_by_id:
            kept = dict(previous_by_id[project_id])
            kept["collection_error"] = "preserved_previous_snapshot"
            snapshot["projects"].append(kept)
        else:
            snapshot["projects"].append(
                {
                    "id": project_id,
                    "repository": repo,
                    "revision": "unknown",
                    "ci": "unknown",
                    "release": None,
                    "collection_error": str(exc)[:200],
                }
            )

if failures:
    # Do not treat partial API failure as success telemetry.
    snapshot["collection_status"] = "partial"
    snapshot["collection_errors"] = failures
else:
    snapshot["collection_status"] = "ok"

with tempfile.NamedTemporaryFile(
    "w", delete=False, dir=SNAPSHOT_PATH.parent, encoding="utf-8"
) as handle:
    json.dump(snapshot, handle, indent=2)
    handle.write("\n")
    temporary_path = handle.name
Path(temporary_path).replace(SNAPSHOT_PATH)

if failures:
    print("Collection completed with preserved/unknown entries:")
    for item in failures:
        print(" -", item)
    # Exit 0 so the workflow can still re-render assets and keep last valid public state.
    # Missing data is recorded as unknown, never as success.
else:
    print("Collection completed for", len(snapshot["projects"]), "allowlisted repositories.")
