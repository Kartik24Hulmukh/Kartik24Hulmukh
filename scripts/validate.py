#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []

for f in ["data/projects.json", "data/claims.json", "data/now.json", "data/snapshot.json"]:
    try:
        json.loads((root / f).read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"{f}: {e}")

md = (root / "README.md").read_text(encoding="utf-8")
assets = [
    "masthead-light.svg",
    "masthead-dark.svg",
    "rgit-light.svg",
    "rgit-dark.svg",
    "kairo-receipt-light.svg",
    "kairo-receipt-dark.svg",
    "notebook-light.svg",
    "notebook-dark.svg",
]
for f in assets:
    if not (root / "assets" / f).exists():
        errors.append("Missing assets/" + f)

for required in [
    "software for people nearby",
    "field note 01",
    "receipt 02",
    "systems notebook",
    "corrections desk",
]:
    if required not in md.lower():
        errors.append("Missing README section: " + required)

# Forbid overclaims in public-facing profile text.
if re.search(
    r"(?i)unhackable|100% secure|industry-leading|prompt-injection-proof|production-proven|world-class|revolutionary|autonomous security|100% accurate",
    md,
):
    errors.append("Forbidden overclaim in README")

if "BUILD CONSOLE" in md.upper() or "build-console" in md:
    errors.append("Obsolete Build Console language remains")

# Reject obsolete Build Console asset references.
for bad in ["build-console.svg", "telemetry.svg", "project-rgit.svg", "project-kairo.svg"]:
    if bad in md:
        errors.append("Obsolete asset reference: " + bad)
    if (root / "assets" / bad).exists():
        errors.append("Obsolete asset still present: assets/" + bad)

# Ensure picture elements use relative paths.
if "./assets/" not in md:
    errors.append("README should reference local assets")

# Evidence atlas files
for f in ["docs/index.html", "docs/styles.css", "docs/app.js"]:
    if not (root / f).exists():
        errors.append("Missing " + f)

# Role language sanity
projects = json.loads((root / "data/projects.json").read_text(encoding="utf-8"))["projects"]
by_id = {p["id"]: p for p in projects}
if by_id.get("rgit", {}).get("role") != "Founder · Product Engineer · Operator":
    errors.append("RGIT role language drifted")
if "Lead Builder" not in by_id.get("kairo", {}).get("role", ""):
    errors.append("Kairo role language drifted")
if by_id.get("xray", {}).get("role") != "Engineering Contributor":
    errors.append("X-Ray role language drifted")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Verified Noticeboard validation passed.")
