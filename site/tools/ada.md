# Ada: MCP server status, API access gate and what it does

> Enterprise AI customer-experience platform (voice, chat, email) that automates inbound support and sales... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Ada

# Ada

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [ada.cx](https://ada.cx) · entry id 14-ada · source 14-inbound-plg-chat.md line 65

**What it does**
Enterprise AI customer-experience platform (voice, chat, email) that automates inbound support and sales conversations end-to-end.

**AI features, separated from automation with an AI label on it**
Vendor claims multi-LLM orchestration, generative AI for complex resolution, and "Playbooks" for automating SOPs with agentic AI, citing an 84% automated resolution rate and 357% ROI - all vendor-stated figures, not independently verified.

**RevOps role**
Enterprise inbound AI agent platform for CX teams; notable in this category for having a real but narrow MCP server.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: none documented - connects over HTTP with no credential requirement described in the docs.

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official (docs-only)

mcp_url, verbatim from the file:

https://docs.ada.cx/_mcp/server

- [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (/pricing is a demo-booking landing page with no tiers or prices; docs.ada.cx publishes a public API reference but states no plan or package requirement for access)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.ada.cx](https://www.ada.cx)
- [https://docs.ada.cx](https://docs.ada.cx)
- [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server)
- [https://www.ada.cx/pricing/](https://www.ada.cx/pricing/)

4 source URLs. Raw sources field, verbatim:

https://www.ada.cx, https://docs.ada.cx, https://docs.ada.cx/_mcp/server, https://www.ada.cx/pricing/

**Notes, verbatim from the file**
IMPORTANT CAVEAT - Ada's MCP server exposes exactly one tool ("AI-powered search over the documentation") and only lets an AI client search Ada's own help docs; it is not an MCP for querying or acting on a customer's live Ada account data (conversations, contacts, etc.). Listed as official because the URL is real and vendor-hosted, but do not conflate this with a full product-data MCP like Intercom's or Pylon's. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.ada.cx/pricing/): /pricing is a demo-booking landing page with no tiers or prices; docs.ada.cx publishes a public API reference but states no plan or package requirement for access.

**Provenance**

- **Entry id**: 14-ada

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 65

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
