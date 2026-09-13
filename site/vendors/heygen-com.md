# HeyGen: products, MCP servers and connect URLs, one vendor page

> HeyGen (heygen.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 1 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
HeyGen

# HeyGen

1 product in the directory
1 official MCP server
1 live handshake
Data baked 2026-09-12

Vendor domain: [heygen.com](https://heygen.com) · vendor page id heygen-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 1 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 739 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: none tied to heygen.com with evidence on 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [HeyGen](../tools/heygen.md)

AI avatar/video-generation platform with a documented sales-prospecting motion - batch-personalize one template into many prospect-specific versions (dynamic name/company/pain-point variables), with native HubSpot automation that generates and attaches a...

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED

- **Endpoint probe**: answered, asking for a key, 2026-09-04

- **Connect URL**: [https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/) (endpoint)

- **Tools catalogued**: not measured

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 paid and self serve, API access by paying, no sales call.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)

2 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/) (HeyGen, endpoint, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [HeyGen](../tools/heygen.md) heygen official CLI

```
curl -fsSL https://static.heygen.ai/cli/install.sh | bash
```

quoted from [https://developers.heygen.com/cli](https://developers.heygen.com/cli) on 2026-09-12, via shell

Login or key hint: heygen auth

3 subcommands seen, harvested 2026-09-12, all on the [tool page](../tools/heygen.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

No GitHub organisation could be tied to heygen.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: heygen-com, HeyGen-Official, HeyGen-Ai-App, heygen-fork, Heygent-core. A name match alone is never accepted; the account has to point at the vendor domain.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 739 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
