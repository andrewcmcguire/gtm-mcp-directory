# Trainual: MCP server status, API access gate and what it does

> SOP and process-documentation platform for onboarding and training, positioned more broadly at operations/HR... Official MCP, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Enablement & Coaching](../categories/enablement-coaching.md) /
Trainual

# Trainual

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Enablement & Coaching](../categories/enablement-coaching.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [trainual.com](https://trainual.com) · entry id 11-trainual · source 11-enablement-coaching.md line 235

**What it does**
SOP and process-documentation platform for onboarding and training, positioned more broadly at operations/HR than sales-specific enablement, with AI-assisted SOP drafting.

**AI features, separated from automation with an AI label on it**
AI SOP generator drafts a first-pass standard operating procedure from a manager's plain-language description; AI-assisted documentation and AI knowledge search are included across paid tiers. This is generative content-drafting and retrieval AI over the org's own SOP library - not conversational roleplay or buyer simulation, and not sales-specific.

**RevOps role**
General SOP/onboarding documentation tool that sales orgs use for process content rather than a purpose-built sales-enablement or roleplay platform - included here as an adjacent, AI-relevant onboarding tool per the research brief.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Bearer MCP token in the Authorization header; the help article states "Only those with an Admin+ permission level can create MCP tokens" and "The Trainual MCP is available under Premium and Enterprise plans."

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://help.trainual.com/en/the-trainual-mcp-server](https://help.trainual.com/en/the-trainual-mcp-server)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://help.trainual.com/en/the-trainual-mcp-server (endpoint https://mcp.trainual.com, remote MCP server)

- [https://help.trainual.com/en/the-trainual-mcp-server](https://help.trainual.com/en/the-trainual-mcp-server)
- [https://mcp.trainual.com](https://mcp.trainual.com)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - Trainual's Grow (top/custom-priced) tier explicitly includes API access and custom integration support; some third-party breakdowns describe the mid Scale tier ($299/mo) as including API access too, so the exact tier boundary should be reconfirmed directly on trainual.com/pricing.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/trainual/tiptap-collaboration-mcp](https://github.com/trainual/tiptap-collaboration-mcp)

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: no-job-fits. SOP and process documentation, explicitly described as not sales-specific.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://trainual.com/pricing](https://trainual.com/pricing)
- [https://operandio.com/trainual-pricing/](https://operandio.com/trainual-pricing/)
- [https://github.com/trainual/tiptap-collaboration-mcp](https://github.com/trainual/tiptap-collaboration-mcp)
- [https://trainual.com/product-updates/connect-trainual-integrations](https://trainual.com/product-updates/connect-trainual-integrations)
- [https://help.trainual.com/en/the-trainual-mcp-server](https://help.trainual.com/en/the-trainual-mcp-server)
- [https://zapier.com/mcp/trainual](https://zapier.com/mcp/trainual)

6 source URLs. Raw sources field, verbatim:

https://trainual.com/pricing, https://operandio.com/trainual-pricing/, https://github.com/trainual/tiptap-collaboration-mcp, https://trainual.com/product-updates/connect-trainual-integrations, https://help.trainual.com/en/the-trainual-mcp-server, https://zapier.com/mcp/trainual

**Notes, verbatim from the file**
A public GitHub repo at github.com/trainual/tiptap-collaboration-mcp is real and maintained by Trainual's own GitHub org, but per its README it is an MCP server for Tiptap's collaboration/document service (Trainual's underlying editor infrastructure) - it does not expose Trainual's own product/training data. Do not cite it as a "Trainual product MCP"; mcp_status is none-found for Trainual-the-product on that basis. 2026-09-02: mcp_status none-found -> official. Trainual's own help center article https://help.trainual.com/en/the-trainual-mcp-server documents a remote MCP server at https://mcp.trainual.com, configured in Claude Desktop, Cursor or Windsurf with an Authorization: Bearer <your-mcp-token> header, tokens created by Admin+ users, gated to the Premium and Enterprise plans; the 2026-07-14 product update https://trainual.com/product-updates/connect-trainual-integrations announces it ("Connect them to Trainual's Model Context Protocol (MCP) server"). Zapier and viaSocket also host third-party Trainual connectors (https://zapier.com/mcp/trainual: 5 triggers, 7 write actions), which are now secondary. trainual.com has no llms.txt and the official MCP registry has no trainual entry, which is why the 2026-08-24 pass found only the unrelated tiptap-collaboration-mcp repo; that caveat about the Tiptap repo still stands, but it no longer decides mcp_status. api_gate is left as recorded because it describes API access; the MCP plan gate is stated above.

**Provenance**

- **Entry id**: 11-trainual

- **Source file**: 11-enablement-coaching.md

- **Source line**: 235

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
