# Showpad: MCP server status, API access gate and what it does

> Revenue effectiveness platform combining sales content management, buyer engagement tracking, and AI-driven... Official MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Enablement & Coaching](../categories/enablement-coaching.md) /
Showpad

# Showpad

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Enablement & Coaching](../categories/enablement-coaching.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [showpad.com](https://showpad.com) · entry id 11-showpad · source 11-enablement-coaching.md line 216

**What it does**
Revenue effectiveness platform combining sales content management, buyer engagement tracking, and AI-driven coaching/roleplay under a unified "Showpad Genie" AI layer.

**AI features, separated from automation with an AI label on it**
Genie Assistant (in-platform Q&A), Roleplay AI (practice conversations for seller training), Authoring AI (content-creation assist), and a "Field Seller Agent" - vendor describes Genie as "the platform's AI core that learns how your company wins," but no independent technical detail confirms whether Roleplay AI runs dynamic buyer personas (like Second Nature/Hyperbound) or more scripted practice flows.

**RevOps role**
Content-plus-coaching hub with a documented developer portal, positioned similarly to Allego/Bigtincan/Highspot as an enablement platform layering AI features onto a content-management core.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth; the docs say each end user authenticates with their own Showpad credentials and can only search and retrieve content they are already authorized to view. Access is beta and routed through the Account Manager; the pricing page lists Remote MCP Server under the Expert tier.

- **Parsed URLs**: 3 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-02 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developer.showpad.com/docs/integrations/platform-independent/mcp (first-party docs; remote endpoints https://mcp.showpad.com/mcp/v1 or per-tenant https://yourcompany.showpad.biz/mcp/v1)

- [https://developer.showpad.com/docs/integrations/platform-independent/mcp](https://developer.showpad.com/docs/integrations/platform-independent/mcp)
- [https://mcp.showpad.com/mcp/v1](https://mcp.showpad.com/mcp/v1)
- [https://yourcompany.showpad.biz/mcp/v1](https://yourcompany.showpad.biz/mcp/v1)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (the Developer Bundle (API/SDK, webhooks, reporting API) is bundled into the mid-tier Advanced plan and the Expert tier adds a remote MCP server, but all three tiers are quote-only with no published price and no self-serve purchase)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Retrieve sales content](../jobs/retrieve-sales-content.md)
- [Score rep performance](../jobs/score-rep-performance.md)
- [Run a sales roleplay practice](../jobs/run-sales-roleplay-practice.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.showpad.com](https://www.showpad.com)
- [https://developer.showpad.com](https://developer.showpad.com)
- [https://www.showpad.com/pricing/](https://www.showpad.com/pricing/)
- [https://developer.showpad.com/docs/integrations/platform-independent/mcp](https://developer.showpad.com/docs/integrations/platform-independent/mcp)
- [https://developer.showpad.com/news/mcp-tools](https://developer.showpad.com/news/mcp-tools)

5 source URLs. Raw sources field, verbatim:

https://www.showpad.com, https://developer.showpad.com, https://www.showpad.com/pricing/, https://developer.showpad.com/docs/integrations/platform-independent/mcp, https://developer.showpad.com/news/mcp-tools

**Notes, verbatim from the file**
No MCP server found at developer.showpad.com or on GitHub, mcp.so, glama.ai, or pulsemcp.com - the developer portal exists but nothing MCP-specific was found there in this pass. developer.showpad.com returned an HTTP 403 to an automated fetch during this research pass; worth checking by hand directly in a browser. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.showpad.com/pricing/): the Developer Bundle (API/SDK, webhooks, reporting API) is bundled into the mid-tier Advanced plan and the Expert tier adds a remote MCP server, but all three tiers are quote-only with no published price and no self-serve purchase. 2026-09-02: mcp_status none-found -> official. developer.showpad.com loaded without the earlier 403, its homepage says "connect AI assistants with Showpad MCP", and its sitemap lists https://developer.showpad.com/docs/integrations/platform-independent/mcp, a first-party docs page for a remotely hosted Showpad MCP: endpoints https://mcp.showpad.com/mcp/v1 or per-tenant https://yourcompany.showpad.biz/mcp/v1, OAuth per end user with Showpad permissions enforced, 8 text tools (search, fetch, showpad_showql_guide, showpad_showql_filter, showpad_ask_a_question, showpad_whoami, showpad_shared_spaces_list, showpad_shared_spaces_get, showpad_shared_spaces_get_engagement) plus 3 MCP Apps widgets, with Claude Code and ChatGPT named as clients. The docs call it beta and route access via "Contact your Account Manager"; a July 2026 news item (https://developer.showpad.com/news/mcp-tools) says the article now carries the full tool reference. The "no MCP server found" sentence above is superseded.

**Provenance**

- **Entry id**: 11-showpad

- **Source file**: 11-enablement-coaching.md

- **Source line**: 216

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-02

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
