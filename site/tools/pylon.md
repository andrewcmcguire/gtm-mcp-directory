# Pylon: MCP server status, API access gate and what it does

> "Agentic" B2B customer support platform (Slack, Teams, email, chat, SMS, WhatsApp, phone) where AI agents and... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Pylon

# Pylon

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [usepylon.com](https://usepylon.com) · entry id 14-pylon · source 14-inbound-plg-chat.md line 179

**What it does**
"Agentic" B2B customer support platform (Slack, Teams, email, chat, SMS, WhatsApp, phone) where AI agents and humans jointly investigate, resolve, and act on support signals.

**AI features, separated from automation with an AI label on it**
Multiple purpose-built agents (Assist Agent for investigation/task delegation, Background Agent for automated skill execution, Slack Agent, Support Agent for automated resolution) plus reusable "Skills" - a genuinely agentic architecture per vendor description; depth not independently verified.

**RevOps role**
CATEGORY-FIT NOTE - Pylon is fundamentally a B2B support/ticketing platform, not an inbound-chat-qualification or PLG-signal tool. Included here because its AI agents work the same "inbound signal -> route/resolve" motion this category covers and it has one of the cleanest official MCP servers in the set; a future pass may be better served moving it to conversation-intel or a dedicated support-ops category if one is added.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 over stateless streamable HTTP; access is permission-scoped so a connected AI tool can only see/change what the authenticated user could already see in the Pylon dashboard.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.usepylon.com](https://mcp.usepylon.com)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.usepylon.com ; https://www.pulsemcp.com/servers/pylon (a separate community server by Justin Beckwith also exists)

- [https://mcp.usepylon.com](https://mcp.usepylon.com)
- [https://www.pulsemcp.com/servers/pylon](https://www.pulsemcp.com/servers/pylon)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown. No public pricing page was found; the pricing route is a demo-booking form ("Schedule a personalized 30-minute demo"), consistent with a sales-led model, but no explicit enterprise-only statement was found either.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://usepylon.com](https://usepylon.com)
- [https://usepylon.com/mcp](https://usepylon.com/mcp)
- [https://usepylon.com/pricing](https://usepylon.com/pricing)
- [https://www.pulsemcp.com/servers/pylon](https://www.pulsemcp.com/servers/pylon)
- [https://docs.usepylon.com/pylon-docs/developer/api](https://docs.usepylon.com/pylon-docs/developer/api)

5 source URLs. Raw sources field, verbatim:

https://usepylon.com, https://usepylon.com/mcp, https://usepylon.com/pricing, https://www.pulsemcp.com/servers/pylon, https://docs.usepylon.com/pylon-docs/developer/api

**Notes, verbatim from the file**
None. [api_gate 2026-08-25] Re-checked and left unknown, honestly: usepylon.com/pricing is a demo-booking page with no tiers or prices and no pricing link exists in nav or footer; the public API reference states only that admin users can create API tokens, with no plan requirement. Checked against https://docs.usepylon.com/pylon-docs/developer/api.

**Provenance**

- **Entry id**: 14-pylon

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 179

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
