# MadKudu: MCP server status, API access gate and what it does

> Historically a lead-scoring/qualification product; the vendor domain now redirects to HG Insights, and... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
MadKudu

# MadKudu

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-09-07
CLI: mct-vulnerator

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.madkudu.com (redirects to https://hginsights.com)](https://www.madkudu.com (redirects to https://hginsights.com)) · entry id 04-madkudu · source 04-ai-sdr-agents.md line 277

**What it does**
Historically a lead-scoring/qualification product; the vendor domain now redirects to HG Insights, and MadKudu appears folded into HG Insights' "HG Sales Copilot" (AI-automated scoring, account research, playbooks, personalized outreach sequences, signal-based engagement) at msi.madkudu.com.

**AI features, separated from automation with an AI label on it**
Could not independently verify current-state agentic depth beyond the HG Insights marketing description found via the redirect; the original standalone MadKudu lead-scoring product no longer appears to exist as an independent entity.

**RevOps role**
Formerly a lead-scoring layer between marketing/sales handoff; now positioned inside HG Insights' broader revenue-intelligence suite.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: MadKudu API key embedded in the endpoint path; the portal states "Please contact HG Insights or your account manager if you're interested in the MadKudu API".

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min](https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min (endpoints https://mcp.madkudu.com/YOUR_API_KEY/mcp for Streamable HTTP and https://mcp.madkudu.com/YOUR_API_KEY/sse for SSE clients such as Claude)

- [https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min](https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min)
- [https://mcp.madkudu.com/YOUR_API_KEY/mcp](https://mcp.madkudu.com/YOUR_API_KEY/mcp)
- [https://mcp.madkudu.com/YOUR_API_KEY/sse](https://mcp.madkudu.com/YOUR_API_KEY/sse)

**What this server exposes**

- **Tools named**: 16
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **madkudu-account-activities** Retrieve account activity history including events, timestamps, activity types, and associated person details with advanced filtering, search, and sorting capabilities. evidence: answered tools/list · calling it reads · required: domain

- **madkudu-account-brief-instructions** Generate comprehensive account sales brief instructions for a target domain. This tool provides a structured prompt that guides through account research using various MadKudu tools to create an actionable sales strategy. These instructions evidence: answered tools/list · calling it reads · required: domain

- **madkudu-account-details** Retrieve comprehensive account profile including company information, geographic location, social media presence, MadKudu scoring metrics, and activity data. evidence: answered tools/list · calling it reads · required: domain

- **madkudu-account-news-deep-search** Execute comprehensive news research across multiple AI-optimized search queries, returning news information with relevance scoring. IMPORTANT: This tool has higher cost than other tools - only use when explicitly requested by the user or sp evidence: answered tools/list · calling it reads · required: domain

- **madkudu-account-top-persons** Retrieve key people from an account including contact information, job titles, location data, social profiles, MadKudu scoring metrics, and activity levels. evidence: answered tools/list · calling it reads · required: domain

- **madkudu-account-top-users** Lists the top users from the account based on activity volume evidence: in the vendor docs · calling it reads

- **madkudu-discover-persons** Discover persons and retrieve contact information from external data providers using provider-specific filters. Each provider (Apollo, ZoomInfo, Cognism) has different filter capabilities and comprehensive filtering options. IMPORTANT: Alwa evidence: answered tools/list · calling it reads · required: provider

- **madkudu-enrich-person** Enrich person records with additional contact information including email and phone numbers using provider-specific identifiers obtained from madkudu-discover-persons tool results. IMPORTANT: Always call madkudu-sourcing-providers first to evidence: answered tools/list · calling it reads · required: provider, provider_id

- **madkudu-enrich-persons** Finds contact details like email and phone numbers for people discovered evidence: in the vendor docs · calling it reads

- **madkudu-person-activities** Retrieve person activity history including events, timestamps, activity types, and associated account details with advanced filtering, search, and sorting capabilities. evidence: answered tools/list · calling it reads

- **madkudu-person-details** Retrieve comprehensive person profile including contact information, job details, location, social profiles, MadKudu scoring metrics, and activity aggregations. evidence: answered tools/list · calling it reads

- **madkudu-search-accounts** Search for accounts across your database with advanced filtering, text search, and sorting capabilities. Use typed filters restricted to account-specific fields. evidence: answered tools/list · calling it reads

- **madkudu-search-job-postings** Search for job postings by domain with advanced filtering, sorting, and pagination capabilities. This tool helps identify hiring activity and job openings at specific companies. evidence: answered tools/list · calling it reads · required: domain

- **madkudu-search-persons** Search for persons across your database with advanced filtering, text search, and sorting capabilities. Use typed filters restricted to person-specific fields. evidence: answered tools/list · calling it reads

- **madkudu-sourcing-providers** Retrieve list of available external sourcing data providers and their connection status to determine which providers can be used for person discovery and enrichment. evidence: answered tools/list · calling it reads

- **madkudu-value-prop** Retrieve tenant-specific value propositions and persona-based messaging for sales and marketing outreach customization. evidence: answered tools/list · calling it reads

119 of the 337 entries that record an official or community MCP server carry a harvested tool list. The other 218 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: mct-vulnerator
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @madkudu-core-tools/vulnerator
```

quoted from [https://www.npmjs.com/package/@madkudu-core-tools/vulnerator](https://www.npmjs.com/package/@madkudu-core-tools/vulnerator) on 2026-09-12, via npm

```
npm install -g @madkudu-core-tools/split
```

quoted from [https://www.npmjs.com/package/@madkudu-core-tools/split](https://www.npmjs.com/package/@madkudu-core-tools/split) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @madkudu-core-tools/vulnerator 2.1.0](https://www.npmjs.com/package/@madkudu-core-tools/vulnerator)
- [npm: @madkudu-core-tools/split 1.2.0](https://www.npmjs.com/package/@madkudu-core-tools/split)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (madkudu.com/pricing 301s to hginsights.com after the HG Insights acquisition and HG publishes no prices - platform and data-fabric pricing is by data consumption, seats and credits on quote, with no self-serve purchase path)

**API documentation**

No documentation URL recorded.

494 of 694 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/MadKudu](https://github.com/MadKudu) tied to the vendor by rule 3, account website http://www.madkudu.com has the vendor's domain, confidence strong

- **Public repositories**: 0, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: not recorded

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 694 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.madkudu.com](https://www.madkudu.com)
- [https://hginsights.com](https://hginsights.com)
- [https://hginsights.com/pricing](https://hginsights.com/pricing)
- [https://developers.madkudu.com/](https://developers.madkudu.com/)
- [https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min](https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min)

5 source URLs. Raw sources field, verbatim:

https://www.madkudu.com, https://hginsights.com, https://hginsights.com/pricing, https://developers.madkudu.com/, https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min

**Notes, verbatim from the file**
SWEEP FLAG - www.madkudu.com now 301-redirects to hginsights.com, and the login link is labeled "HG Sales Copilot" at msi.madkudu.com. Strong signal of an acquisition/absorption; could not find a dedicated public announcement confirming deal terms or date in this pass. Treat MadKudu as effectively discontinued as a standalone product. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://hginsights.com/pricing): madkudu.com/pricing 301s to hginsights.com after the HG Insights acquisition and HG publishes no prices - platform and data-fabric pricing is by data consumption, seats and credits on quote, with no self-serve purchase path. 2026-09-02: mcp_status none-found -> official. https://developers.madkudu.com/ ("HG Platform API", shorthand MadAPI and MadMCP) has a MadKudu MCP section (What is MadKudu MCP, First time using MCP, Install in AI platforms in 2min, MadMCP tools, Building AI Agents powered by MadKudu) and states "MCP is a new protocol to connect to AI tools like ChatGPT, Claude, Cursor, Dust, or your own GPT agents... The MCP server translates that into API calls to MadKudu." The install page gives the mcp.madkudu.com endpoints above. The key is gated behind HG Insights sales, so api_gate stays enterprise-only. hginsights.com/llms.txt has no MCP mention; the receipt lives on the MadKudu developer subdomain, which still operates under the MadKudu name post-acquisition. 2026-09-07: https://mcp.madkudu.com/YOUR_API_KEY/mcp answered an MCP initialize with HTTP 200 and a jsonrpc result (the key is a path segment). npm publishes @madkudu/mcp under the vendor scope (https://mcp.madkudu.com/<API_KEY>/mcp).

**Provenance**

- **Entry id**: 04-madkudu

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 277

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
