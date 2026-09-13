# MeetGeek: products, MCP servers and connect URLs, one vendor page

> MeetGeek (meetgeek.ai): 1 product in The GTM MCP Directory, 1 with an official MCP server, 1 answering a live handshake, 6 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
MeetGeek

# MeetGeek

1 product in the directory
1 official MCP server
1 live handshake
Data baked 2026-09-12

Vendor domain: [meetgeek.ai](https://meetgeek.ai) · vendor page id meetgeek-ai

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-25

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-25

- **Community MCP servers**: 0 of 1

- **Live handshake**: 1 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 6 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 1,251 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/meetgeekai](https://github.com/meetgeekai), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [MeetGeek](../tools/meetgeek.md)

Automatic meeting recorder and transcriber that produces summaries, highlights and conversation analytics across Zoom, Teams and Meet.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED

- **Endpoint probe**: answered, asking for a key, 2026-09-04

- **Connect URL**: [https://mcp.meetgeek.ai/mcp](https://mcp.meetgeek.ai/mcp) (endpoint)

- **Tools catalogued**: 6 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-08-25

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)

2 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://mcp.meetgeek.ai/mcp](https://mcp.meetgeek.ai/mcp) (MeetGeek, endpoint, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [MeetGeek](../tools/meetgeek.md) meetgeek community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
npm install -g meetgeek-cli
```

quoted from [https://www.npmjs.com/package/meetgeek-cli](https://www.npmjs.com/package/meetgeek-cli) on 2026-09-12, via npm, a third party source

harvested 2026-09-12, all on the [tool page](../tools/meetgeek.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/meetgeekai](https://github.com/meetgeekai) tied to the vendor by rule 1, the directory already classed this repo first-party and its owner is an Organization, confidence strong

- **Public repositories**: 5, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-03-12

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [onechart](https://github.com/meetgeekai/onechart) | other | | 0 | 2026-03-12 | v1.0.13 |
| [meetgeek-mcp-server](https://github.com/meetgeekai/meetgeek-mcp-server) | MCP server | Official MeetGeek MCP Server | 23 | 2026-02-05 | |
| [meetgeekai-n8n-node](https://github.com/meetgeekai/meetgeekai-n8n-node) | SDK | n8n community node for integrating with the Meetgeek app | 4 | 2025-10-17 | |
| [meetgeek-mcp-test](https://github.com/meetgeekai/meetgeek-mcp-test) | MCP server | | 0 | 2025-07-23 | |
| [release-action](https://github.com/meetgeekai/release-action) | infrastructure | | 0 | 2024-06-05 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 1,251 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
