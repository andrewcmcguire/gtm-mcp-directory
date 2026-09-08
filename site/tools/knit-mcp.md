# Knit MCP: MCP server status, API access gate and what it does

> A unified-API vendor that publishes hosted, serverless MCP servers for individual SaaS applications across... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Knit MCP

# Knit MCP

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07
CLI: knit-mcp (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [getknit.dev](https://getknit.dev) · entry id 07-knit-mcp · source 07-mcp-infrastructure.md line 292

**What it does**
A unified-API vendor that publishes hosted, serverless MCP servers for individual SaaS applications across CRM, ATS, HRIS, ticketing, accounting, calendar, email and e-sign, alongside its unified REST APIs and an LLM-tools surface for the same catalogue.

**AI features, separated from automation with an AI label on it**
None of its own. Knit is integration plumbing that normalises third-party APIs into one schema and hands the result to whatever model is calling. Its marketing claim is that the servers are "Optimized for Token Cost and Accuracy", which is a tool-design claim rather than a model claim.

**RevOps role**
A cheap way for a solo operator to put an agent in front of a CRM or ATS that has no first-party MCP server, without writing and maintaining the OAuth plumbing.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Knit-managed OAuth or SAML per connected application; the customer authorises each end application through Knit rather than holding its credentials directly. The endpoint pattern for an individual server was not published on any page that could be read on this date.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.getknit.dev/mcp-servers (catalogue; per-application server pages such as https://www.getknit.dev/mcp-servers/close-crm-mcp-server)

- [https://www.getknit.dev/mcp-servers](https://www.getknit.dev/mcp-servers)
- [https://www.getknit.dev/mcp-servers/close-crm-mcp-server](https://www.getknit.dev/mcp-servers/close-crm-mcp-server)

**What this server exposes**

What this server exposes is the customer's own workspace, not a fixed catalogue the vendor publishes. No tool list is the correct answer here rather than a gap, and the harvest recorded it as one.

Recorded by the harvest: a gateway that re-exposes many other vendors' MCP servers through one endpoint

The count below still carries this entry on the unmeasured side, because there is no list to record. That is a different thing from a server nobody has read, and both are published rather than blended.

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. The full roll up is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: knit-mcp
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-08

Install, as the source shows it:

```
pip install knit-mcp
```

quoted from [https://pypi.org/project/knit-mcp/](https://pypi.org/project/knit-mcp/) on 2026-09-08, via pypi, a third party source

Packages seen, with the version on 2026-09-08:

- [pypi: knit-mcp 0.1.1, third party](https://pypi.org/project/knit-mcp/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-08.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the MCP tab of the vendor's pricing page publishes a "Launchpad" tier at "Free", including "Knit's Remote MCP Servers", "Create your own MCP Server", "Upto 5 Servers" and "100 API Calls/ Month", then "Individual" at "$29/Month" adding "5K API Calls/ Month" and "Unlimited MCP Servers", with Enterprise routed to "Get in touch". Note that Knit's separate Unified API product is priced very differently, starting at $499/month.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to getknit.dev with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

2 candidate accounts seen and rejected by the evidence rules: getknit, getknitt-com. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.getknit.dev/mcp-servers](https://www.getknit.dev/mcp-servers)
- [https://www.getknit.dev/pricing](https://www.getknit.dev/pricing)

2 source URLs. Raw sources field, verbatim:

https://www.getknit.dev/mcp-servers, https://www.getknit.dev/pricing

**Notes, verbatim from the file**
Verified 2026-09-07 from the vendor's own catalogue and pricing pages. NO ENDPOINT WAS CAPTURED and none is claimed: the catalogue lists servers per application but the per-server connection URL sits behind the app, so this entry records where to read about the servers rather than where to reach one, and no liveness probe was run. The GTM-relevant slice of the catalogue is thin next to the HR and recruiting side: CRM servers listed include Close CRM, HubSpot and Salesforce, while the bulk of the 100-plus entries are HRIS and ATS. The pricing split is the finding worth carrying: the same vendor charges $0 to $29 a month for the MCP surface and from $499 a month for the unified REST API over broadly the same connectors, which is the first case in this file of MCP being priced as the cheap on-ramp rather than the premium tier. Knit also advertises adding a requested application within 7 days, which is a coverage claim, not a verified fact.

**Provenance**

- **Entry id**: 07-knit-mcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 292

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
