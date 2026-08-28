# How do I check if a tool has an MCP server? The five places to look

> How to establish whether a vendor really ships an MCP server, who built it, and whether the claim survives contact with the URL. The exact checks this directory runs on every entry.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I check whether a tool has an MCP server?

**The short answer**

Check five places in this order: this directory, the vendor's own developer documentation, their GitHub organisation, the protocol's reference server repository, and the URL itself. A claim without a URL is not a server, and a URL that 404s is a claim that failed.

## The five places, in order

- **This directory.** 293 entries, each with an MCP status, the vendor's own mcp_url and mcp_auth printed verbatim, and the date the check was made.

- **The vendor's developer documentation.** Not the homepage. Marketing pages say AI powered; developer docs say what the endpoint is. 30 of 293 entries here record a documentation URL, which tells you something in itself about the other 263.

- **Their GitHub organisation.** 61 entries here already carry a github.com URL somewhere in their fields and 46 of those are in the mcp_url field itself, which usually means a local server you run yourself.

- **The protocol's reference repository**, which is where a large number of community servers are catalogued.

- **The URL.** Fetch it.

## What a fetch actually tells you

This directory's own rule, applied to every submission: a 200 passes. A 401 passes, because an auth gated live endpoint is still a live endpoint. A 403 is inconclusive and gets rechecked by hand. A 404 means the claim fails and the entry is recorded as none found rather than official.

## The distinction most people miss

Ask who built it before you ask whether it works. A wrapper published by an integration platform is a real, working server and it is not the vendor's. This directory records that as community, and 21 entries are in that bucket against 144 official.

## When the honest answer is unknown

7 entries here carry a status of unknown, because the check could not settle it either way. Unknown is a legal answer. Publishing a guess as a fact is how a directory becomes worthless, and it is the reason every status on this site carries the date it was established.

## Sources

- [modelcontextprotocol/servers, the reference server repository](https://github.com/modelcontextprotocol/servers) https://github.com/modelcontextprotocol/servers
- [Model Context Protocol, official documentation](https://modelcontextprotocol.io) https://modelcontextprotocol.io
- [The GTM MCP Directory, methodology](../methodology.md) this site
- [The GTM MCP Directory, submit a tool](../submit.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [What is the difference between an official and a community MCP server?](official-vs-community-mcp-server.md)
- [Which GTM tools have no MCP server?](which-gtm-tools-have-no-mcp-server.md)
- [How many of these GTM tools have actually been tested?](how-many-gtm-tools-are-bench-tested.md)
- [How do I audit my GTM stack for agent readiness?](how-do-i-audit-my-gtm-stack-for-agent-readiness.md)

## In the directory

- [Methodology](../methodology.md)
- [Submit a correction](../submit.md)
