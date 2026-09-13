# lemlist: products, MCP servers and connect URLs, one vendor page

> lemlist (lemlist.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 0 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
lemlist

# lemlist

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [lemlist.com](https://lemlist.com) · vendor page id lemlist-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-09-07

- **Official MCP servers**: 1 of 1, as recorded on 2026-09-07

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: not measured on any product of this vendor

- **Bench tested**: 0 of 1 here, 1 of 514 across the directory

- **Ships a CLI**: 0 of 1 official, 1 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: none tied to lemlist.com with evidence on 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [lemlist](../tools/lemlist.md)

Multichannel sales engagement platform combining lead database/enrichment, email/LinkedIn/call/SMS sequencing, and a unified inbox.

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://developer.lemlist.com/mcp/setup](https://developer.lemlist.com/mcp/setup) (docs page)

- **Tools catalogued**: not measured

- **last_checked**: 2026-09-07

**The gates, in plain words**

1 of 1 paid and self serve, API access by paying, no sales call.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)

8 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://developer.lemlist.com/mcp/setup](https://developer.lemlist.com/mcp/setup) (lemlist, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [lemlist](../tools/lemlist.md) lemlist community CLI

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

```
npm install -g @lemlist-official/cli
```

quoted from [https://www.npmjs.com/package/@lemlist-official/cli](https://www.npmjs.com/package/@lemlist-official/cli) on 2026-09-12, via npm, a third party source

harvested 2026-09-12, all on the [tool page](../tools/lemlist.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

**On GitHub**

No GitHub organisation could be tied to lemlist.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

1 candidate account seen and rejected by the evidence rules: ponyexpressss. A name match alone is never accepted; the account has to point at the vendor domain.

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 514 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
