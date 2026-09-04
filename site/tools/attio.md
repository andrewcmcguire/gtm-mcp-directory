# Attio: MCP server status, API access gate and what it does

> A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Attio

# Attio

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [attio.com](https://attio.com) · entry id 06-attio · source 06-revops-infra.md line 57

**What it does**
A CRM built around a flexible, user-defined data model (not fixed contact/company/deal objects) with real-time sync and an API-first architecture.

**AI features, separated from automation with an AI label on it**
Confirmed AI surface is thin in what's publicly documented - automatic data enrichment and meeting-intelligence tooling are mentioned as part of the MCP tool surface, but no distinct named AI-agent product on the scale of Agentforce or Breeze was found; treated as unconfirmed rather than asserted.

**RevOps role**
A newer, flexible-schema CRM competing for data-team/startup RevOps stacks that want customizable record objects; one of the cleaner "log in with your own account, no API key" MCP implementations found in this research.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - one-time login as the user's own Attio account, no API key needed. Reads auto-approve; writes require confirmation. Permissions mirror whatever the logged-in user already has in the workspace.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.attio.com/mcp/overview (endpoint: https://mcp.attio.com/mcp)

- [https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview)
- [https://mcp.attio.com/mcp](https://mcp.attio.com/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the Free plan (up to 3 seats) includes API access, rate-limited (~1,000 calls/hour). Paid tiers: Plus $29/user/mo, Pro $69/user/mo, Enterprise custom.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview)
- [https://mcp.attio.com/](https://mcp.attio.com/)
- [https://attio.com/pricing](https://attio.com/pricing)

3 source URLs. Raw sources field, verbatim:

https://docs.attio.com/mcp/overview, https://mcp.attio.com/, https://attio.com/pricing

**Notes, verbatim from the file**
Community/unofficial Attio MCP servers also exist (e.g. kesslerio/attio-mcp-server) and are separate from the official mcp.attio.com hosted server linked above.

**Provenance**

- **Entry id**: 06-attio

- **Source file**: 06-revops-infra.md

- **Source line**: 57

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
