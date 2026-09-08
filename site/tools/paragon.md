# Paragon (ActionKit MCP): MCP server status, API access gate and what it does

> An embedded integration platform for SaaS products, whose ActionKit product exposes a stated 1,000-plus... Official MCP, Enterprise leaning. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Paragon (ActionKit MCP)

# Paragon (ActionKit MCP)

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [useparagon.com](https://useparagon.com) · entry id 07-paragon · source 07-mcp-infrastructure.md line 337

**What it does**
An embedded integration platform for SaaS products, whose ActionKit product exposes a stated 1,000-plus actions across 130-plus third-party applications through one API and one MCP server, with Paragon handling the OAuth prompts inside the customer's own product.

**AI features, separated from automation with an AI label on it**
None of its own. The differentiator relevant to agents is a Dynamic Proxy Actions feature, in beta, that lets an agent write and execute raw HTTP requests against a third-party API using the model's own knowledge of that API rather than a pre-built connector, which is a genuinely different design from a fixed tool list.

**RevOps role**
Integration infrastructure for a team that is shipping an agent inside its own product rather than wiring up its own stack, which makes it the odd one out among the gateways in this file and closer to Merge than to Composio.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Paragon user token plus Connect Portal OAuth. The distinguishing feature is that the authorisation prompt is embedded in the calling product's own chat surface, so an end user authorises a third-party application at query time without leaving the app.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official (open-source adapter you host)

mcp_url, verbatim from the file:

https://github.com/useparagon/paragon-mcp (product page: https://www.useparagon.com/mcp)

- [https://github.com/useparagon/paragon-mcp](https://github.com/useparagon/paragon-mcp)
- [https://www.useparagon.com/mcp](https://www.useparagon.com/mcp)

**What this server exposes**

- **Tools named**: 1
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-08
- **Repo read**: useparagon/paragon-mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **CALL_API_REQUEST** Call an API if no tool is available for an integration that matches the user evidence: in the server source · calling it reads

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning - Paragon publishes no prices. Its pricing page prices by "Connected Users", stating "Usage costs scale based on the number of tenants (customer orgs) you have using integrations", offers a "Start free trial" on each of the three products (Managed Sync, ActionKit, Workflows), and routes SSO, priority support and professional services to "Talk to sales". A solo operator can start without a call but cannot learn the price without one.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/useparagon/paragon-mcp](https://github.com/useparagon/paragon-mcp)

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.useparagon.com/mcp](https://www.useparagon.com/mcp)
- [https://www.useparagon.com/pricing](https://www.useparagon.com/pricing)
- [https://github.com/useparagon/paragon-mcp](https://github.com/useparagon/paragon-mcp)

3 source URLs. Raw sources field, verbatim:

https://www.useparagon.com/mcp, https://www.useparagon.com/pricing, https://github.com/useparagon/paragon-mcp

**Notes, verbatim from the file**
Verified 2026-09-07 from the vendor's own MCP page. NOT A HOSTED ENDPOINT: unlike every other entry in this group, Paragon ships an open-source adapter the customer runs, so there is nothing to probe and none is claimed; the vendor's page offers "Book a demo" and "View GitHub repo" and no server URL. GTM connectors named on the page include Salesforce, HubSpot, Pipedrive, Gong, Salesloft, Apollo, Outreach, Marketo, Mailchimp and Microsoft Dynamics, which is the densest GTM coverage of the six unified-API layers reviewed in this pass. The multi-tenant framing is the practical divider between this and a Composio or a Zapier MCP: Paragon assumes the buyer has end users of their own who each need to authorise their own accounts, so a single operator wiring up one stack is not the target customer and will find the pricing model an awkward fit.

**Provenance**

- **Entry id**: 07-paragon

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 337

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
