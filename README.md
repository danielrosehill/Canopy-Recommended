# Canopy Recommended

Plugins that help an agent work on your local network, for [Canopy](https://github.com/danielrosehill/Canopy) users:
the network itself, remote access, servers and smart home. Some are by the Canopy author and some are third-party.
Each one is pinned to a reviewed commit and stays in its author's repo.

## Install

With `canopy-connector` installed, ask your agent for the recommended plugins, or run
`/canopy-connector:recommended`. It shows a checklist and installs what you tick.

By hand:

```
/plugin marketplace add danielrosehill/Canopy-Recommended
/plugin install home-assistant-skills@canopy-recommended
```

To make them searchable on your Canopy server instead of installing them:

```
canopy add-marketplace danielrosehill/Canopy-Recommended
```

Plugin names are global on a Canopy server, so don't also index another marketplace that lists the same plugin.

Third-party plugins are tagged `third-party`, plugins that run hooks are tagged `runs-hooks`, and
plugins that connect an MCP server are tagged `connects-mcp`.
