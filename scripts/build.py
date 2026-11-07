#!/usr/bin/env python3
"""Regenerate .claude-plugin/marketplace.json from scripts/picks.json.

Usage: scripts/build.py CLONES_DIR
CLONES_DIR holds one reviewed clone per pick, named after the pick. Each entry is pinned
to the commit that clone is at, so run this only after reviewing that commit.
"""
import json, subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
clones = Path(sys.argv[1])
picks = json.loads((root / "scripts/picks.json").read_text())
plugins = []
for p in picks["plugins"]:
    clone = clones / p["name"]
    base = clone / p.get("path", "")
    sha = subprocess.check_output(["git", "-C", str(clone), "rev-parse", "HEAD"], text=True).strip()
    meta = json.loads((base / ".claude-plugin/plugin.json").read_text())
    if meta["name"] != p["name"]:
        sys.exit(f"{p['name']}: plugin.json says {meta['name']}")
    if p.get("path"):
        source = {"source": "git-subdir", "url": f"https://github.com/{p['repo']}.git", "path": p["path"], "sha": sha}
    else:
        source = {"source": "github", "repo": p["repo"], "sha": sha}
    tags = []
    if not p["repo"].startswith("danielrosehill/"):
        tags.append("third-party")
    if list(base.glob("hooks/hooks.json")):
        tags.append("runs-hooks")
    if (base / ".mcp.json").exists():
        tags.append("connects-mcp")
    entry = {"name": p["name"], "source": source, "description": p.get("description") or meta["description"],
             "category": p["category"]}
    if tags:
        entry["tags"] = tags
    plugins.append(entry)
out = {"name": "canopy-recommended", "owner": {"name": "Daniel Rosehill"},
       "metadata": {"description": "Plugins that help an agent work on your local network, for Canopy users. Pinned to reviewed commits."},
       "plugins": plugins}
(root / ".claude-plugin/marketplace.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(len(plugins), "plugins")
