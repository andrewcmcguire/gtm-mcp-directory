# Official vs community MCP servers: what the difference actually costs you

> Official means the vendor ships and maintains the server. Community means somebody else does. 156 against 26 across 293 GTM tools.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / Definitions

**Definitions**

# What is the difference between an official and a community MCP server?

**The short answer**

An official MCP server is built and maintained by the vendor whose system it exposes. A community server does the same job but is maintained by somebody else, which means it can be abandoned, can lag behind API changes, and can disappear without the vendor ever knowing it existed.

Both kinds work. The difference is not quality on the day you install it, it is who is responsible on the day it breaks.

When a vendor changes an endpoint, an official server is updated by the team that made the change. A community server is updated when its author notices, has time, and still cares. Neither outcome is guaranteed, but only one of them has an organisation behind it.

## What counts as official here

Official means first party and nothing else. A server built by a third party integration platform such as Zapier, Composio or viaSocket is recorded as community no matter how well it works or how large the company behind it is, because the vendor whose data is being exposed did not write it and does not maintain it. That rule is applied to every entry without exception.

## The split across this directory

156 entries are official. 26 are community. 87 had no server found at all, and 15 could not be settled either way and are published as unknown rather than guessed into a bucket.

Community servers cluster. Video Prospecting alone accounts for 6 of the 26, against 3 official servers in that category, which is the one place in this data where the community outbuilt the vendors.

## What to check before depending on a community server

- When the repo last moved. This directory does not publish that yet: the repo health rail has not been run, and a star count without the date it was taken is a lie, so nothing is shown rather than something stale. 66 entries already carry a github.com URL somewhere in their fields, which is the seed for that work.

- Whether the vendor acknowledges it anywhere in their own docs.

- What credential it wants, and how much of your account that credential can touch.

The 26 community servers in this directory are listed with their URLs and their auth models, and every one links to the entry it came from.

## Sources

- [modelcontextprotocol/servers, the reference server repository](https://github.com/modelcontextprotocol/servers) https://github.com/modelcontextprotocol/servers
- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is an MCP server?](what-is-an-mcp-server.md)
- [What does agent ready mean for a GTM tool?](what-does-agent-ready-mean.md)
- [Which GTM tools have official MCP servers?](which-gtm-tools-have-official-mcp-servers.md)
- [How do I build an MCP server for a tool that does not have one?](how-do-i-build-an-mcp-server-for-a-tool-that-has-none.md)

## In the directory

- [The community servers](../lists/community-mcp-servers.md)
- [The official servers](../lists/official-mcp-servers.md)
