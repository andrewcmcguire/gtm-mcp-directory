# Smartlead: MCP server status, API access gate and what it does

> Cold email outreach platform for managing campaigns across many mailboxes, with built-in deliverability... Official MCP, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Smartlead

# Smartlead

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [smartlead.ai](https://smartlead.ai) · entry id 02-smartlead · source 02-engagement-outbound.md line 141

**What it does**
Cold email outreach platform for managing campaigns across many mailboxes, with built-in deliverability infrastructure and a unified reply inbox.

**AI features, separated from automation with an AI label on it**
"SmartAgents"/"SmartAI Bot" claim to research leads and draft persona-specific copy via generative AI - genuinely LLM-based per vendor description. "AI-powered" warmup is mostly scripted open/read/reply simulation, borderline as "AI." Sender rotation, DNS setup, and verification are plain automation.

**RevOps role**
Outbound email sequencing/deliverability layer with agent-style lead research and reply-triage add-ons.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key, passed as the user_api_key query parameter on the SSE endpoint URL; SSE transport only (the help article says streamable HTTP is not supported), and the vendor FAQ says only Claude Desktop is supported for now

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server (first-party; endpoint https://mcp.smartlead.ai/sse?user_api_key=YOUR_API_KEY. Community alternative: https://github.com/LeadMagic/smartlead-mcp-server, listed at https://www.pulsemcp.com/servers/leadmagic-smartlead)

- [https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server)
- [https://mcp.smartlead.ai/sse?user_api_key=YOUR_API_KEY](https://mcp.smartlead.ai/sse?user_api_key=YOUR_API_KEY)
- [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server)
- [https://www.pulsemcp.com/servers/leadmagic-smartlead](https://www.pulsemcp.com/servers/leadmagic-smartlead)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server)

**Jobs it can do**

- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.smartlead.ai/pricing](https://www.smartlead.ai/pricing)
- [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server)
- [https://www.pulsemcp.com/servers/leadmagic-smartlead](https://www.pulsemcp.com/servers/leadmagic-smartlead)
- [https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server)

4 source URLs. Raw sources field, verbatim:

https://www.smartlead.ai/pricing, https://github.com/LeadMagic/smartlead-mcp-server, https://www.pulsemcp.com/servers/leadmagic-smartlead, https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server

**Notes, verbatim from the file**
API/webhooks/CRM integration require the Pro plan ($94/mo) or higher, not the base Base plan ($39/mo). No official first-party MCP found - several overlapping community implementations exist with varying maintenance; verify before adopting. 2026-09-02: mcp_status community -> official. Smartlead's own help center now documents a first-party server at https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server: endpoint mcp.smartlead.ai/sse with the API key in the URL, SSE only, Claude Desktop only per the vendor FAQ, covering campaign data, diagnostics and lead retrieval. The earlier "no official MCP" sentence is superseded. The LeadMagic community server stays listed as the alternative for clients that need stdio or streamable HTTP.

**Provenance**

- **Entry id**: 02-smartlead

- **Source file**: 02-engagement-outbound.md

- **Source line**: 141

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
