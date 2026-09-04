# Pipedream MCP: MCP server status, API access gate and what it does

> Pipedream's existing workflow/integration platform re-exposed as hosted MCP servers, giving an MCP client... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Pipedream MCP

# Pipedream MCP

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [pipedream.com](https://pipedream.com) · entry id 07-pipedream-mcp · source 07-mcp-infrastructure.md line 33

**What it does**
Pipedream's existing workflow/integration platform re-exposed as hosted MCP servers, giving an MCP client access to 3,000+ connected apps and 10,000+ pre-built tools via Pipedream Connect.

**AI features, separated from automation with an AI label on it**
none in Pipedream itself - same pattern as Composio, it is connector infrastructure an external LLM/agent calls into, not a model or agent of its own.

**RevOps role**
Same slot as Composio - a hosted connector layer, notable for breadth (3,000+ apps) rather than GTM-specific depth.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth/API-key credentials for each underlying app are stored by Pipedream and isolated per end user; Pipedream states credentials are "never exposed to AI models or client-side code" and all calls route server-side through its infrastructure.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://mcp.pipedream.com](https://mcp.pipedream.com)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.pipedream.com

- [https://mcp.pipedream.com](https://mcp.pipedream.com)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (free for personal use and development; a paid plan is required once you deploy to production)

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://mcp.pipedream.com](https://mcp.pipedream.com)
- [https://pipedream.com/docs/connect/mcp](https://pipedream.com/docs/connect/mcp)

2 source URLs. Raw sources field, verbatim:

https://mcp.pipedream.com, https://pipedream.com/docs/connect/mcp

**Notes, verbatim from the file**
Pipedream is custodial like Composio - it stores end-user credentials server-side rather than passing them through. Could not confirm exact production-tier pricing numbers in this pass (pricing docs page 404'd); marked unknown rather than guessed. GTM apps (Salesforce, HubSpot) were not explicitly named in the fetched docs, only implied by the "3,000+ apps" breadth claim.

**Provenance**

- **Entry id**: 07-pipedream-mcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 33

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
