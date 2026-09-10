# Sybill: products, MCP servers and connect URLs, one vendor page

> Sybill (sybill.ai): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 8 tools catalogued. Data baked 2026-09-10.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
Sybill

# Sybill

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-10

Vendor domain: [sybill.ai](https://sybill.ai) · vendor page id sybill-ai

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 8 named across 1 measured server, harvested 2026-09-10

- **Bench tested**: 0 of 1 here, 1 of 336 across the directory

- **Ships a CLI**: 0 of 1 official, 0 community only, 1 none found, harvested 2026-09-10

- **GitHub organisation**: none tied to sybill.ai with evidence on 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [Sybill](../tools/sybill.md)

AI sales assistant that analyzes call recordings, emails, and CRM data to produce deal insights, call summaries, and behavioral/sentiment reads on prospects.

[Official MCP](../mcp/official.md) · [Enterprise leaning](../gates/enterprise-leaning.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html) (docs page)

- **Tools catalogued**: 8 named, harvested 2026-09-10, catalogue fixed

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 enterprise leaning, self serve on paper and gated in practice.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Search across recorded calls](../jobs/search-call-library.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)

3 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html) (Sybill, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

No CLI found for any product of this vendor by the 2026-09-10 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**On GitHub**

No GitHub organisation could be tied to sybill.ai with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: sybill-ai-engineering, sybilla, SybillaTechnologies, sybill-gtm-engineering, sybill-ai-copilot-users. A name match alone is never accepted; the account has to point at the vendor domain.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 336 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-10 by build_directory.py (phase 1).
