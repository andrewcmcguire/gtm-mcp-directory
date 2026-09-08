# Zapier: products, MCP servers and connect URLs, one vendor page

> Zapier (zapier.com): 2 products in The GTM MCP Directory, 2 with an official MCP server, 0 answering a live handshake, 15 tools catalogued. Data baked 2026-09-08.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Zapier

# Zapier

2 products in the directory
2 official MCP servers
0 live handshakes
Data baked 2026-09-08

Vendor domain: [zapier.com](https://zapier.com) · vendor page id zapier-com

**The rollup**

- **Products**: 2, facts checked by hand 2026-09-07

- **Official MCP servers**: 2 of 2, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 2

- **Live handshake**: 0 of 2 answered an MCP initialize, 2 probed, 2026-09-04

- **Repo local**: 0 of 2: a server you install and run yourself

- **Docs only**: 2 of 2: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 15 named across 2 measured servers, harvested 2026-09-08

- **Bench tested**: 0 of 2 here, 1 of 336 across the directory

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 2**

### [Zapier](../tools/zapier.md)

A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://zapier.com/mcp](https://zapier.com/mcp) (docs page)

- **Tools catalogued**: 0 named, harvested 2026-09-08, catalogue dynamic, the server exposes the customer's own workspace

- **last_checked**: 2026-09-07

### [Zapier MCP](../tools/zapier-mcp.md)

Zapier's own MCP endpoint, letting Claude, ChatGPT, Cursor, and other MCP clients trigger the same 9,000+ app actions Zapier already exposes to its classic trigger-action Zaps.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://mcp.zapier.com/login?redirectTo=%2Fmcp](https://mcp.zapier.com/login?redirectTo=%2Fmcp) (docs page)

- **Tools catalogued**: 15 named, harvested 2026-09-08, catalogue dynamic, the server exposes the customer's own workspace

- **last_checked**: 2026-09-07

**The gates, in plain words**

2 of 2 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

3 distinct job labels, the union across 2 products, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://zapier.com/mcp](https://zapier.com/mcp) (Zapier, docs page, probed 2026-09-04)
- [https://mcp.zapier.com/login?redirectTo=%2Fmcp](https://mcp.zapier.com/login?redirectTo=%2Fmcp) (Zapier MCP, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 2 products are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-08 by build_directory.py (phase 1).
