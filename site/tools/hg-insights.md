# HG Insights (Phoenix platform): MCP server status, API access gate and what it does

> Aggregates B2B technographic data (software/tech a company runs, sourced from job postings, web crawling,... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
HG Insights (Phoenix platform)

# HG Insights (Phoenix platform)

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://hginsights.com](https://hginsights.com) · entry id 05-hg-insights · source 05-signals-intent-abm.md line 235

**What it does**
Aggregates B2B technographic data (software/tech a company runs, sourced from job postings, web crawling, public filings, partner feeds), firmographics, IT spend estimates, and third-party intent (via TrustRadius review/research activity) into a unified company profile.

**AI features, separated from automation with an AI label on it**
Long-standing data-aggregation/technographics business that predates the "AI" framing. Newer "RGI Agent Builder" and MCP layer expose existing structured data to AI agents - infrastructure for AI, not AI-derived data itself; skeptical of "AI-ready infrastructure" marketing beyond that.

**RevOps role**
Firmographic/technographic enrichment and account intelligence, feeding ICP fit-scoring and territory/account prioritization upstream of outbound.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (`x-api-key` header; throttled to 100 calls/60 seconds per connection)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://learn.microsoft.com/en-us/connectors/hginsightsmcp/](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://learn.microsoft.com/en-us/connectors/hginsightsmcp/ (Microsoft-certified connector, publisher HG Insights)

- [https://learn.microsoft.com/en-us/connectors/hginsightsmcp/](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/)

**What this server exposes**

- **Tools named**: 43
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **company_ai_maturity** Company AI Maturity evidence: in the vendor docs · calling it reads

- **company_cloud_spend** Company Cloud Spend evidence: in the vendor docs · calling it reads

- **company_contracts** Company Contracts evidence: in the vendor docs · calling it reads

- **company_fai** FAI Scores evidence: in the vendor docs · calling it reads

- **company_firmographic** Company Firmographics evidence: in the vendor docs · calling it reads

- **company_gov_opportunities** Company Gov Opportunities evidence: in the vendor docs · calling it reads

- **company_gov_relationships** Company Gov Relationships evidence: in the vendor docs · calling it reads

- **company_install_time_series** Company Install Time Series evidence: in the vendor docs · calling it reads

- **company_intent** Company Intent evidence: in the vendor docs · calling it reads

- **company_operating_signals** Company Operating Signals evidence: in the vendor docs · calling it reads

- **company_research** Company Research evidence: in the vendor docs · calling it reads

- **company_spend** Company Spend evidence: in the vendor docs · calling it reads

- **company_technographic** Company Technographics evidence: in the vendor docs · calling it reads

- **contact_enrich** Contact Enrich evidence: in the vendor docs · calling it reads

- **contact_search** Contact Search evidence: in the vendor docs · calling it reads

- **customer_data_explore** Customer Data Explore evidence: in the vendor docs · calling it reads

- **customer_data_query** Customer Data Query evidence: in the vendor docs · calling it reads

- **get_company_hierarchy** Company Hierarchy evidence: in the vendor docs · calling it reads

- **get_product_attribute** Get Product Attribute evidence: in the vendor docs · calling it reads

- **get_product_category** Get Product Category evidence: in the vendor docs · calling it reads

- **get_product_information** Product Information evidence: in the vendor docs · calling it reads

- **get_product_reviews** Product Reviews evidence: in the vendor docs · calling it reads

- **get_vendor_information** Vendor Information evidence: in the vendor docs · calling it reads

- **hg_catalog** HG Data Catalog evidence: in the vendor docs · calling it reads

- **hg_data_query** HG Data Query evidence: in the vendor docs · calling it reads

- **hg_query** HG Query (NL to SQL) evidence: in the vendor docs · calling it reads

- **intent_category** Intent Category evidence: in the vendor docs · calling it reads

- **list_fai_departments** FAI Departments evidence: in the vendor docs · calling it reads

- **list_intent_topics** Intent Topics evidence: in the vendor docs · calling it reads

- **phoenix_get_artifact** Get Artifact evidence: in the vendor docs · calling it reads

- **phoenix_get_run_status** Get Run Status evidence: in the vendor docs · calling it reads

- **phoenix_invoke_agent** Invoke Agent evidence: in the vendor docs · calling it reads

- **phoenix_list_agents** List Agents evidence: in the vendor docs · calling it reads

- **phoenix_list_artifacts** List Artifacts evidence: in the vendor docs · calling it reads

- **phoenix_onboarding** Guided Onboarding evidence: in the vendor docs · calling it reads

- **product_search_and_enrich** Product Search and Enrich evidence: in the vendor docs · calling it reads

- **search_companies** Company Search evidence: in the vendor docs · calling it reads

- **search_federal_contracts** Search Federal Contracts evidence: in the vendor docs · calling it reads

- **search_gov_opportunities** Search Gov Opportunities evidence: in the vendor docs · calling it reads

- **search_industries_naics_sic** Industry Search (NAICS/SIC) evidence: in the vendor docs · calling it reads

- **sec_filing_section** SEC Filing Section evidence: in the vendor docs · calling it reads

- **sec_full_text_search** SEC Full Text Search evidence: in the vendor docs · calling it reads

- **web_search** Web Search evidence: in the vendor docs · calling it reads

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/HGData](https://github.com/HGData) tied to the vendor by rule 3, account website http://www.hginsights.com has the vendor's domain, confidence strong

- **Public repositories**: 27, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-02-20

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [action-setup-elixir](https://github.com/HGData/action-setup-elixir) | SDK | Checks out the code, configures Elixir, fetches dependencies, and manages build caching | 0 | 2026-02-20 | v1.0.6 |
| [mk-developers](https://github.com/HGData/mk-developers) | other | | 2 | 2024-09-12 | |
| [mk-node-mixpanel-export](https://github.com/HGData/mk-node-mixpanel-export) | other | | 0 | 2024-07-09 | |
| [mk-node-marketo](https://github.com/HGData/mk-node-marketo) | other | REST Client for Marketo API | 50 | 2024-02-05 | 0.7.8 |
| [mk-node-eloqua](https://github.com/HGData/mk-node-eloqua) | other | | 4 | 2024-01-03 | 1.3.5 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 649 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://hginsights.com/gtm-data-insights/gtm-infrastructure/](https://hginsights.com/gtm-data-insights/gtm-infrastructure/)
- [https://hginsights.com/solutions-use-case/gtm-infrastructure-for-ai-agents/](https://hginsights.com/solutions-use-case/gtm-infrastructure-for-ai-agents/)
- [https://learn.microsoft.com/en-us/connectors/hginsightsmcp/](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/)
- [https://data-docs.hginsights.com/v2/guides/overview](https://data-docs.hginsights.com/v2/guides/overview)
- [https://phoenix.hginsights.com/features](https://phoenix.hginsights.com/features)

5 source URLs. Raw sources field, verbatim:

https://hginsights.com/gtm-data-insights/gtm-infrastructure/, https://hginsights.com/solutions-use-case/gtm-infrastructure-for-ai-agents/, https://learn.microsoft.com/en-us/connectors/hginsightsmcp/, https://data-docs.hginsights.com/v2/guides/overview, https://phoenix.hginsights.com/features

**Notes, verbatim from the file**
The AI-agent/MCP product is described as "early access request" only, no self-serve signup found, consistent with HG Insights' historical enterprise-contract business model. Note: madkudu.com now 301-redirects to hginsights.com, indicating MadKudu (predictive PQL scoring) has been folded into HG Insights - see Sweep notes. 2026-09-07: LAW 1 FLAG, NOT DOWNGRADED. What the official claim actually rests on: a Microsoft-certified Power Platform connector, which is a Microsoft-hosted wrapper, not a first-party repo or endpoint. The finder searched GitHub ("HG Insights mcp", owners hginsights and HGInsights), npm, PyPI and the official registry and probed https://mcp.hginsights.com/mcp with no result. A human should decide whether official survives law 1.

**Provenance**

- **Entry id**: 05-hg-insights

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 235

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
