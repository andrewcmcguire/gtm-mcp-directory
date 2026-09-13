# Showpad: MCP server status, API access gate and what it does

> Revenue effectiveness platform combining sales content management, buyer engagement tracking, and AI-driven... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Enablement & Coaching](../categories/enablement-coaching.md) /
Showpad

# Showpad

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Enablement & Coaching](../categories/enablement-coaching.md)
RESEARCHED
Checked 2026-09-07
CLI: showpad

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.showpad.com/mcp/v1 ; https://developer.showpad.com/docs/integrations/platform-independent/mcp (first-party docs; remote endpoints https://mcp.showpad.com/mcp/v1 or per-tenant https://yourcompany.showpad.biz/mcp/v1)

- [https://mcp.showpad.com/mcp/v1](https://mcp.showpad.com/mcp/v1)
- [https://developer.showpad.com/docs/integrations/platform-independent/mcp](https://developer.showpad.com/docs/integrations/platform-independent/mcp)
- [https://yourcompany.showpad.biz/mcp/v1](https://yourcompany.showpad.biz/mcp/v1)

**What this server exposes**

- **Tools named**: 12
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **fetch** Retrieves an asset's content by ID: text transcription, page content, or a URL. evidence: in the vendor docs · calling it reads · required: id

- **search** Finds Showpad assets by name, type, description, or content. Returns results with webapp URLs. evidence: in the vendor docs · calling it reads

- **showpad_ask_a_question** Returns an AI-generated answer with cited sources, drawn from the user's Showpad content. evidence: in the vendor docs · calling it reads

- **showpad_browse** An interactive asset browser with thumbnails, metadata, and content-type filters. Listed by the vendor as an MCP App rather than a text tool. evidence: in the vendor docs · calling it reads

- **showpad_browse_filter** The same asset browser, populated by a ShowQL filter instead of free text. Listed by the vendor as an MCP App rather than a text tool. evidence: in the vendor docs · calling it reads

- **showpad_shared_space_card** A visual card for one shared space showing metadata, sharing settings, engagement KPI tiles. Listed by the vendor as an MCP App rather than a text tool. evidence: in the vendor docs · calling it reads

- **showpad_shared_spaces_get** Returns full details for one shared space by ID. evidence: in the vendor docs · calling it reads · required: id

- **showpad_shared_spaces_get_engagement** Returns engagement insights for one shared space. evidence: in the vendor docs · calling it reads

- **showpad_shared_spaces_list** Lists the shared spaces the user owns or participates in. evidence: in the vendor docs · calling it reads

- **showpad_showql_filter** Filters assets by structured metadata: type, tags, dates, size, language, share flags, and engagement. evidence: in the vendor docs · calling it reads

- **showpad_showql_guide** Returns the ShowQL syntax reference for building structured filter queries. evidence: in the vendor docs · calling it reads

- **showpad_whoami** Returns the current user's identity: name, email, and account type. evidence: in the vendor docs · calling it reads

119 of the 415 entries that record an official or community MCP server carry a harvested tool list. The other 296 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: showpad
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @showpad/cli
```

quoted from [https://www.npmjs.com/package/@showpad/cli](https://www.npmjs.com/package/@showpad/cli) on 2026-09-12, via npm

```
npm install -g @showpad/experience-app-cli
```

quoted from [https://www.npmjs.com/package/@showpad/experience-app-cli](https://www.npmjs.com/package/@showpad/experience-app-cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @showpad/cli 1.0.7](https://www.npmjs.com/package/@showpad/cli)
- [npm: @showpad/experience-app-cli 3.1.1](https://www.npmjs.com/package/@showpad/experience-app-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (the Developer Bundle (API/SDK, webhooks, reporting API) is bundled into the mid-tier Advanced plan and the Expert tier adds a remote MCP server, but all three tiers are quote-only with no published price and no self-serve purchase)

**API documentation**

No documentation URL recorded.

582 of 884 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/showpad](https://github.com/showpad) tied to the vendor by rule 3, account website https://showpad.com has the vendor's domain, confidence strong

- **Public repositories**: 0, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: not recorded

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Retrieve sales content](../jobs/retrieve-sales-content.md)
- [Score rep performance](../jobs/score-rep-performance.md)
- [Run a sales roleplay practice](../jobs/run-sales-roleplay-practice.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 884 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.showpad.com](https://www.showpad.com)
- [https://developer.showpad.com](https://developer.showpad.com)
- [https://www.showpad.com/pricing/](https://www.showpad.com/pricing/)
- [https://developer.showpad.com/docs/integrations/platform-independent/mcp](https://developer.showpad.com/docs/integrations/platform-independent/mcp)
- [https://developer.showpad.com/news/mcp-tools](https://developer.showpad.com/news/mcp-tools)
- [https://mcp.showpad.com/mcp/v1](https://mcp.showpad.com/mcp/v1)

6 source URLs. Raw sources field, verbatim:

https://www.showpad.com, https://developer.showpad.com, https://www.showpad.com/pricing/, https://developer.showpad.com/docs/integrations/platform-independent/mcp, https://developer.showpad.com/news/mcp-tools, https://mcp.showpad.com/mcp/v1

**Notes, verbatim from the file**
No MCP server found at developer.showpad.com or on GitHub, mcp.so, glama.ai, or pulsemcp.com - the developer portal exists but nothing MCP-specific was found there in this pass. developer.showpad.com returned an HTTP 403 to an automated fetch during this research pass; worth checking by hand directly in a browser. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.showpad.com/pricing/): the Developer Bundle (API/SDK, webhooks, reporting API) is bundled into the mid-tier Advanced plan and the Expert tier adds a remote MCP server, but all three tiers are quote-only with no published price and no self-serve purchase. 2026-09-02: mcp_status none-found -> official. developer.showpad.com loaded without the earlier 403, its homepage says "connect AI assistants with Showpad MCP", and its sitemap lists https://developer.showpad.com/docs/integrations/platform-independent/mcp, a first-party docs page for a remotely hosted Showpad MCP: endpoints https://mcp.showpad.com/mcp/v1 or per-tenant https://yourcompany.showpad.biz/mcp/v1, OAuth per end user with Showpad permissions enforced, 8 text tools (search, fetch, showpad_showql_guide, showpad_showql_filter, showpad_ask_a_question, showpad_whoami, showpad_shared_spaces_list, showpad_shared_spaces_get, showpad_shared_spaces_get_engagement) plus 3 MCP Apps widgets, with Claude Code and ChatGPT named as clients. The docs call it beta and route access via "Contact your Account Manager"; a July 2026 news item (https://developer.showpad.com/news/mcp-tools) says the article now carries the full tool reference. The "no MCP server found" sentence above is superseded. 2026-09-07: https://mcp.showpad.com/mcp/v1 returned 401 to an MCP initialize POST, as did the per-tenant form https://<tenant>.showpad.biz/mcp/v1 (https://mcp.showpad.com/mcp/v1).

**Provenance**

- **Entry id**: 11-showpad

- **Source file**: 11-enablement-coaching.md

- **Source line**: 216

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
