# Pipeworx: MCP server status, API access gate and what it does

> A single MCP gateway that fronts a stated 1,532 live data sources as 5,871 tools behind one URL, weighted... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Pipeworx

# Pipeworx

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [pipeworx.io](https://pipeworx.io) · entry id 07-pipeworx · source 07-mcp-infrastructure.md line 352

**What it does**
A single MCP gateway that fronts a stated 1,532 live data sources as 5,871 tools behind one URL, weighted toward public and regulatory data (SEC EDGAR, FDA, the Federal Reserve, ClinicalTrials, USPTO, EPA, EU procurement), with per-application wrapper paths for common SaaS APIs alongside them.

**AI features, separated from automation with an AI label on it**
None as a model, but several agent-native design features that are genuinely unusual: it ships all three MCP primitives (Tools, Resources and Prompts) rather than tools alone, and adds gateway meta-tools including ask_pipeworx, discover_tools, resolve_entity, compare_entities, entity_profile, recent_changes and a remember, recall and forget memory triple, which the vendor says collapse five to fifteen agent round trips into one call.

**RevOps role**
The public-and-regulatory-data leg of a research agent, sitting alongside rather than inside the GTM stack: filings, patents, tenders, approvals and rates that no CRM or enrichment vendor supplies, reachable without a key.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: none required for the free tiers. The vendor states "No API keys" and that an anonymous client gets 50 tool calls a day on the full catalogue; a free GitHub signup raises that to 200 a day and adds persistent memory and a usage dashboard, and paid usage is metered in credits.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://gateway.pipeworx.io/mcp for the whole gateway, with per-application paths of the form https://gateway.pipeworx.io//mcp (docs: https://pipeworx.io/docs/; directory: https://pipeworx.io/directory)

- [https://gateway.pipeworx.io/mcp](https://gateway.pipeworx.io/mcp)
- [https://gateway.pipeworx.io/](https://gateway.pipeworx.io/)
- [https://pipeworx.io/docs/](https://pipeworx.io/docs/)
- [https://pipeworx.io/directory](https://pipeworx.io/directory)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the pricing page publishes an "Anonymous" tier, "Free forever", at "50 tool calls / day" with "All 5,871 tools" and no API keys, and a "Registered (Free)" tier at "200 tool calls / day" with GitHub signup. Paid usage is priced in credits at 1 credit = $0.0001, with per-category rates and optional $49/month and $99/month subscriptions that lock a lower rate card and are credited against usage rather than charged on top.

**API documentation**

No documentation URL recorded.

289 of 318 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

47 of 318 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://pipeworx.io/](https://pipeworx.io/)
- [https://pipeworx.io/pricing](https://pipeworx.io/pricing)
- [https://pipeworx.io/docs/](https://pipeworx.io/docs/)
- [https://gateway.pipeworx.io/mcp](https://gateway.pipeworx.io/mcp)

4 source URLs. Raw sources field, verbatim:

https://pipeworx.io/, https://pipeworx.io/pricing, https://pipeworx.io/docs/, https://gateway.pipeworx.io/mcp

**Notes, verbatim from the file**
Verified 2026-09-07 and this is the strongest liveness result in this group: POST of an MCP initialize to https://gateway.pipeworx.io/mcp returned HTTP 200 over SSE with a full initialize result, serverInfo name "pipeworx-gateway" version 0.1.0, protocol 2025-06-18, advertising tools, resources and prompts. A per-application path, https://gateway.pipeworx.io/hubspot/mcp, returned the same server identity, which confirms the per-app URLs in the candidate research are routes on one gateway rather than separate servers. RECLASSIFIED FROM THE CANDIDATE ROW: the research filed this as a "third-party wrapper (community)" because its per-app routes wrap other vendors' REST APIs. That is true of the wrapper routes and is a real caveat for anyone connecting the HubSpot or Salesforce path, since neither vendor endorses it. But the entry here is for Pipeworx as a product, and the gateway is Pipeworx's own first-party server, which is the same treatment Composio, Pipedream and Zapier MCP already get in this file, so mcp_status is official. Vendor claims recorded as claims, not findings: 1.7M+ requests/month, and a benchmark asserting frontier models were "100% correct with Pipeworx, 63% with web search" across 188 questions. The self-reported reliability figures are unusually candid and worth quoting in any coverage: the vendor says agent tool calls fail 25 to 30 percent of the time against typical MCP servers and that one instrumentation pass in May 2026 took its own error rate from 27.6% to 6.9%.

**Provenance**

- **Entry id**: 07-pipeworx

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 352

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
