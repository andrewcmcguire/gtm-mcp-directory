# Tavus: products, MCP servers and connect URLs, one vendor page

> Tavus (tavus.io): 1 product in The GTM MCP Directory, 1 with an official MCP server, 1 answering a live handshake, 29 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Tavus

# Tavus

1 product in the directory
1 official MCP server
1 live handshake
Data baked 2026-09-12

Vendor domain: [tavus.io](https://tavus.io) · vendor page id tavus-io

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 1 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 0 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 29 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 694 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/Tavus-Engineering](https://github.com/Tavus-Engineering), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Tavus](../tools/tavus.md)

Developer platform for building real-time, two-way conversational AI video agents ("Conversational Video Interface") - positioned for GTM use cases like greeting website visitors and booking meetings, not primarily batch personalized-outbound video.

[Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED

- **Endpoint probe**: answered, asking for a key, 2026-09-04

- **Connect URL**: [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp) (endpoint)

- **Tools catalogued**: 29 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 free to start, a solo operator gets API access without talking to anyone.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

2 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp) (Tavus, endpoint, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [Tavus](../tools/tavus.md) tavus-cli community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
pip install tavus-cli
```

quoted from [https://pypi.org/project/tavus-cli/](https://pypi.org/project/tavus-cli/) on 2026-09-12, via pypi, a third party source

1 more install command, harvested 2026-09-12, all on the [tool page](../tools/tavus.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

[github.com/Tavus-Engineering](https://github.com/Tavus-Engineering) tied to the vendor by rule 3, account website tavus.io has the vendor's domain, confidence strong

- **Public repositories**: 10, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [tavus-intake](https://github.com/Tavus-Engineering/tavus-intake) | other | | 4 | 2026-09-07 | |
| [tavus-interviewer](https://github.com/Tavus-Engineering/tavus-interviewer) | other | | 3 | 2026-09-07 | |
| [dj_charlie](https://github.com/Tavus-Engineering/dj_charlie) | other | | 1 | 2026-06-23 | |
| [tavus-audio-passthrough-demo](https://github.com/Tavus-Engineering/tavus-audio-passthrough-demo) | docs or examples | | 1 | 2026-04-09 | |
| [tavus-examples](https://github.com/Tavus-Engineering/tavus-examples) | docs or examples | Examples and guides for using Tavus's Conversational Video Interface (CVI) & Video Gen APIs | 86 | 2026-04-06 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 694 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
