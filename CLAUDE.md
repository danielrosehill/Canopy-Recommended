# Canopy-Recommended

Public marketplace of plugins recommended for [Canopy](https://github.com/danielrosehill/Canopy) users.
Plugins are listed by reference, never copied in. Scope: plugins for an agent working on the local networked
environment (network, remote access, servers, smart home). General agent tooling does not belong here.

Edit `scripts/picks.json`, never `marketplace.json` by hand: `scripts/build.py CLONES_DIR` generates it.

To add or update a plugin, shallow-clone its repo into CLONES_DIR under the plugin's name, and review that commit:
public repo, a licence, what any hooks or MCP servers do, and no private hostnames, addresses or names. Then rebuild,
and run `claude plugin validate .`. Every entry stays pinned to a reviewed commit, so an upstream change reaches
users only through a commit here.

Listing a plugin here as well as in another marketplace is fine, but a Canopy server indexing both gets a sync
error for each shared name, because plugin names are global in the catalogue.

Do not list `multisession` until its retired `iterations/` and `research/` folders are out of the plugin's repo
(reviewed 2026-11-07: they hold internal addresses and names).
