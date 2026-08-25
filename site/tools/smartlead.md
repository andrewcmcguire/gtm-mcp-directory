# Smartlead: MCP server status, API access gate and what it does

> Cold email outreach platform for managing campaigns across many mailboxes, with built-in deliverability... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Smartlead

# Smartlead

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [smartlead.ai](https://smartlead.ai) · entry id 02-smartlead · source 02-engagement-outbound.md line 141

**What it does**
Cold email outreach platform for managing campaigns across many mailboxes, with built-in deliverability infrastructure and a unified reply inbox.

**AI features, separated from automation with an AI label on it**
"SmartAgents"/"SmartAI Bot" claim to research leads and draft persona-specific copy via generative AI - genuinely LLM-based per vendor description. "AI-powered" warmup is mostly scripted open/read/reply simulation, borderline as "AI." Sender rotation, DNS setup, and verification are plain automation.

**RevOps role**
Outbound email sequencing/deliverability layer with agent-style lead research and reply-triage add-ons.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: api key

- **Parsed URLs**: 2 found in the mcp_url field

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/LeadMagic/smartlead-mcp-server (also multiple other community implementations); listed at https://www.pulsemcp.com/servers/leadmagic-smartlead

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

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.smartlead.ai/pricing](https://www.smartlead.ai/pricing)
- [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server)
- [https://www.pulsemcp.com/servers/leadmagic-smartlead](https://www.pulsemcp.com/servers/leadmagic-smartlead)

3 source URLs. Raw sources field, verbatim:

https://www.smartlead.ai/pricing, https://github.com/LeadMagic/smartlead-mcp-server, https://www.pulsemcp.com/servers/leadmagic-smartlead

**Notes, verbatim from the file**
API/webhooks/CRM integration require the Pro plan ($94/mo) or higher, not the base Base plan ($39/mo). No official first-party MCP found - several overlapping community implementations exist with varying maintenance; verify before adopting.

**Provenance**

- **Entry id**: 02-smartlead

- **Source file**: 02-engagement-outbound.md

- **Source line**: 141

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
