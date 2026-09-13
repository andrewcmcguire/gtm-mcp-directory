# Sumble: MCP server status, API access gate and what it does

> Builds an account-intelligence knowledge graph by continuously scanning tens of millions of public sources... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Sumble

# Sumble

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://sumble.com](https://sumble.com) · entry id 05-sumble · source 05-signals-intent-abm.md line 472

**What it does**
Builds an account-intelligence knowledge graph by continuously scanning tens of millions of public sources (job boards, company sites, social media, regulatory filings) to map org structure, tech stack, and initiatives like cloud migrations or GenAI projects per company.

**AI features, separated from automation with an AI label on it**
Genuinely AI-driven - pairs a knowledge graph with an LLM to synthesize disparate signals into coherent account narratives, per vendor and TechCrunch coverage. Founded by Kaggle co-founders (Anthony Goldbloom, Ben Hamner), which lends some credibility, though the specifics remain vendor-described.

**RevOps role**
Account research / call-prep layer - LLM-driven account intelligence for reps prepping outbound or discovery calls.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - the MCP overview page documents one-click install from the Claude and ChatGPT app directories and a custom MCP connection for Cursor, Claude Code and Gemini CLI, but does not name the credential type on that page. Read 2026-08-28.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.sumble.com/api/mcp](https://docs.sumble.com/api/mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.sumble.com/ ; https://docs.sumble.com/api/mcp (re-verified 200 on 2026-08-28; corrected that day off a dead receipt, see notes. Product overview at https://sumble.com/mcp) ; repo https://github.com/SumbleData/sumble-mcp

- [https://mcp.sumble.com/](https://mcp.sumble.com/)
- [https://docs.sumble.com/api/mcp](https://docs.sumble.com/api/mcp)
- [https://sumble.com/mcp](https://sumble.com/mcp)
- [https://github.com/SumbleData/sumble-mcp](https://github.com/SumbleData/sumble-mcp)

**What this server exposes**

- **Tools named**: 34
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **AddContactsToList** Adds people to an existing contact list evidence: in the vendor docs · calling it reads · required: list id, person ids

- **AddOrganizationsToList** Adds organizations to an existing list evidence: in the vendor docs · calling it reads · required: list id or slug, organization ids

- **CreateContactList** Creates a new empty contact list evidence: in the vendor docs · calling it reads

- **CreateOrganizationList** Creates a new empty organization list evidence: in the vendor docs · calling it reads

- **FindMatchAndEnrichJobs** Find, look up, and enrich job postings in one call evidence: in the vendor docs · calling it reads

- **FindMatchAndEnrichOrganizations** Find, match, and enrich organizations in one call, search by advanced query or resolve a list of names/URLs/IDs evidence: in the vendor docs · calling it reads

- **FindMatchAndEnrichPeople** Find, match, and enrich people in one call evidence: in the vendor docs · calling it reads

- **GetAccountInformation** Checks credit balance and plan info evidence: in the vendor docs · calling it reads

- **GetContactList** Retrieves one contact list and its people evidence: in the vendor docs · calling it reads · required: list id

- **GetDocumentationPage** Reads a documentation page evidence: in the vendor docs · calling it reads · required: path

- **GetIntelligenceBrief** LLM-generated sales intelligence brief synthesized from structured data evidence: in the vendor docs · calling it reads · required: organization id

- **GetMyCompanyProfile** Retrieves company profile and intelligence data evidence: in the vendor docs · calling it reads

- **GetOrganizationList** Retrieves one organization list and its organizations evidence: in the vendor docs · calling it reads · required: list id

- **GetOrganizationSignals** Get recent sales signals (notable changes) for one organization by ID evidence: in the vendor docs · calling it reads · required: organization id

- **GetOrganizationTechStack** Get an organization's CONFIRMED-USED technology stack, grouped by business function evidence: in the vendor docs · calling it reads · required: organization id

- **ListContactLists** Lists saved contact lists with metadata evidence: in the vendor docs · calling it reads

- **ListDocumentation** Lists all documentation pages evidence: in the vendor docs · calling it reads

- **ListOrganizationLists** Lists saved organization lists with metadata evidence: in the vendor docs · calling it reads

- **ListSignalConfigs** Lists active standing rules for signal delivery evidence: in the vendor docs · calling it reads

- **ListTables** Lists all tables and columns in the database evidence: in the vendor docs · calling it reads

- **LookupJobTitles** Resolves job titles to canonical job function and level evidence: in the vendor docs · calling it reads · required: job titles

- **LookupProjects** Resolves project names or slugs to canonical data evidence: in the vendor docs · calling it reads · required: projects

- **LookupTechnologies** Resolves technology names or slugs to canonical data evidence: in the vendor docs · calling it reads · required: technologies

- **LookupTechnologyCategories** Resolves category slugs or names to canonical data evidence: in the vendor docs · calling it reads · required: categories

- **RenameOrganizationList** Renames an existing organization list evidence: in the vendor docs · calling it reads

- **ReportDataQualityIssue** Reports data quality or coverage issues evidence: in the vendor docs · calling it reads

- **RunSqlQuery** Runs read-only SQL against DuckDB evidence: in the vendor docs · calling it reads · required: query

- **SearchPrioritySignals** Searches Priority Signals digest items evidence: in the vendor docs · calling it reads

- **SearchSignals** Searches Sumble Signals by IDs, organizations, people, technologies evidence: in the vendor docs · calling it reads

- **SearchTechnologies** Looks up technology names and slugs evidence: in the vendor docs · calling it reads · required: query

- **SetOrganizationListDeleted** Soft-deletes or restores an organization list evidence: in the vendor docs · calling it reads

- **SetOrganizationListSignals** Includes or excludes a list from Signals delivery evidence: in the vendor docs · calling it reads

- **SubmitSupportRequest** Submits general support requests evidence: in the vendor docs · calling it reads

- **UpdatePrioritySignalRelevance** Marks a priority signal relevant or not evidence: in the vendor docs · calling it reads · required: signal id, is_relevant

119 of the 471 entries that record an official or community MCP server carry a harvested tool list. The other 352 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

629 of 982 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/SumbleData/sumble-mcp](https://github.com/SumbleData/sumble-mcp)

**On GitHub**

No GitHub organisation could be tied to sumble.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

3 candidate accounts seen and rejected by the evidence rules: SumbleData, sumble-data, Sumble-Guys. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 982 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://techcrunch.com/2025/10/22/sumble-emerges-from-stealth-with-38-5m-to-bring-ai-powered-context-to-sales-intelligence/](https://techcrunch.com/2025/10/22/sumble-emerges-from-stealth-with-38-5m-to-bring-ai-powered-context-to-sales-intelligence/)
- [https://sumble.com/](https://sumble.com/)
- [https://docs.sumble.com/api/mcp](https://docs.sumble.com/api/mcp)
- [https://sumble.com/llms.txt](https://sumble.com/llms.txt)
- [https://sumble.com/mcp](https://sumble.com/mcp)
- [https://mcp.sumble.com/](https://mcp.sumble.com/)

6 source URLs. Raw sources field, verbatim:

https://techcrunch.com/2025/10/22/sumble-emerges-from-stealth-with-38-5m-to-bring-ai-powered-context-to-sales-intelligence/, https://sumble.com/, https://docs.sumble.com/api/mcp, https://sumble.com/llms.txt, https://sumble.com/mcp, https://mcp.sumble.com/

**Notes, verbatim from the file**
2026-08-28 link-rot correction, and the lead paid off. The mcp_url published until today, docs.sumble.com/pages/KLH6XuEHsUssUZW6C1i4, 404d when re-checked on 2026-08-27. It is named here rather than left in the mcp_url field so the published page does not carry a link to a 404. https://sumble.com/llms.txt names the real current surface under a "For AI agents" heading, and both https://sumble.com/mcp and https://docs.sumble.com/api/mcp return 200. The server is alive and first-party, so mcp_status stays official rather than being downgraded. Emerged from stealth October 2025 with a $38.5M raise; knowledge graph covers ~2.6M companies. Self-serve 30-day free trial, no credit card required; specific paid pricing tiers not published. 2026-09-07: https://mcp.sumble.com/ returned 401 {"error": "invalid_token", "error_description": "Authentication required"} to an MCP initialize POST (https://mcp.sumble.com/). 2026-09-12 (P6-04 repo sweep): first-party repository recorded at https://github.com/SumbleData/sumble-mcp - first-party agent skill for the Sumble MCP (README: "Sumble MCP Skill", installed with npx skills add SumbleData/sumble-mcp), NOT the server source. Evidence: the vendor's own docs page https://docs.sumble.com/api/mcp names github.com/SumbleData, which is the domain evidence the 2026-09-09 pass could not find on the org profile. The exact URL that page prints, github.com/SumbleData/sumble, returned 404 on 2026-09-12; the live repository in that same org is sumble-mcp, last pushed 2026-04-14.

**Provenance**

- **Entry id**: 05-sumble

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 472

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
