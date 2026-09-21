# DataMerge MCP: MCP server status, API access gate and what it does

> B2B data enrichment for 375M+ companies: legal entities, corporate hierarchies, and contacts. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
DataMerge MCP

# DataMerge MCP

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-12

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [mcp.datamerge.ai](https://mcp.datamerge.ai) · entry id 01-datamerge-mcp · source 01-data-enrichment.md line 4216

**What it does**
B2B data enrichment for 375M+ companies: legal entities, corporate hierarchies, and contacts.

**AI features, separated from automation with an AI label on it**
Not evidenced from fetched pages this pass; no AI feature claims recorded without a source URL.

**RevOps role**
Upstream contact/company data or enrichment utility feeding CRM and outbound tooling

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://mcp.datamerge.ai

- [https://mcp.datamerge.ai](https://mcp.datamerge.ai)

**What this server exposes**

- **Tools named**: 23
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-18
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **configure_datamerge** Configure DataMerge API authentication (required before using other tools if DATAMERGE_API_KEY is not set). evidence: answered tools/list · calling it reads

- **contact_enrich** POST /v1/contact/enrich. Enrich specific contacts by LinkedIn URL or name+domain. Returns a job_id (async, 202). evidence: answered tools/list · calling it writes · required: contacts, enrich_fields

- **contact_search** POST /v1/contact/search. Search for contacts at specified companies. Returns a job_id (async, 202). enrich_fields required (at least one of contact.emails or contact.phones). Use company_list (slug) instead of domains to search a saved list evidence: answered tools/list · calling it writes · required: enrich_fields

- **contact_search_unenriched** POST /v1/contact/search/unenriched. Find contacts without running email/phone enrichment. Returns a job_id; contacts are created in `unconfirmed` status with stable ids. BETA: requires the `contact_search_unenriched` flag on the account. evidence: answered tools/list · calling it writes

- **create_list** POST /v1/lists. Body: name, object_type (company or contact). evidence: answered tools/list · calling it writes · required: name, object_type

- **delete_list** DELETE /v1/lists/{object_type}/{list_slug}. System lists cannot be deleted. evidence: answered tools/list · calling it writes · required: object_type, list_slug

- **get_company** Get a single company record. GET /v1/company/get?datamerge_id={id} or ?record_id={uuid}. Provide either datamerge_id (charges 1 credit) or record_id (free). Not both. Optional: add_to_list - list slug to add the company to (only with... evidence: answered tools/list · calling it reads

- **get_company_enrichment_result** GET /v1/company/enrich/{job_id}/status. Poll until status is "completed" or "failed". Response includes record_ids. Status values: queued · processing · completed · failed. evidence: answered tools/list · calling it reads · required: job_id

- **get_company_hierarchy** Get all entities in the same global ultimate hierarchy. GET /v1/company/hierarchy?datamerge_id={id}. Parameters: include_names (bool, charges 1 credit), include_branches (bool), only_subsidiaries (bool), max_level (int), country_code (array evidence: answered tools/list · calling it reads · required: datamerge_id

- **get_contact** GET /v1/contact/get?record_id={uuid}. Retrieve a specific contact by record UUID. Never charges credits. evidence: answered tools/list · calling it reads · required: record_id

- **get_contact_enrich_status** GET /v1/contact/enrich/{job_id}/status. Poll until status is "completed" or "failed". Response includes record_ids. evidence: answered tools/list · calling it reads · required: job_id

- **get_contact_search_status** GET /v1/contact/search/{job_id}/status. Poll until status is "completed" or "failed". Response includes record_ids. evidence: answered tools/list · calling it reads · required: job_id

- **get_credits_balance** GET /v1/credits/balance. Returns credits_balance and balances (one_off, recurring, rollover, total). evidence: answered tools/list · calling it reads

- **get_list_items** GET /v1/lists/{object_type}/{list_slug}. object_type: company or contact. list_slug: e.g. target-accounts. Parameters: page, page_size (max 100), sort_by, sort_order (asc/desc). evidence: answered tools/list · calling it reads · required: object_type, list_slug

- **health_check** Check if the DataMerge API client is configured and can connect. Uses /auth/info. evidence: answered tools/list · calling it reads

- **list_lists** GET /v1/lists. Optional: object_type=company or object_type=contact. evidence: answered tools/list · calling it reads

- **remove_list_item** DELETE /v1/lists/{object_type}/{list_slug}/{item_id}. evidence: answered tools/list · calling it writes · required: object_type, list_slug, item_id

- **run_company_enrichment** Agent-friendly company enrichment. On the first call provide enrichment params (domain, domains, company_name, country_code, etc.); the server starts the job and polls internally for up to ~25s. If the job is still running, the response wil evidence: answered tools/list · calling it reads

- **run_contact_enrich** Agent-friendly contact enrichment. On the first call provide contacts and enrich_fields; the server starts the job and polls internally for up to ~25s. If still running, returns {status:"pending", continuation_token, attempt, elapsed_second evidence: answered tools/list · calling it reads

- **run_contact_search** Agent-friendly contact search. On the first call provide domains and enrich_fields; the server starts the job and polls internally for up to ~25s. If still running, returns {status:"pending", continuation_token, attempt, elapsed_seconds} - evidence: answered tools/list · calling it reads

- **run_contact_search_unenriched** POST /v1/contact/search/unenriched/sync. Synchronous unenriched contact search - returns contacts inline (no polling). Requires the `contact_search_unenriched` beta flag. Limits: 10 domains and max_results_per_company ≤ 10. Response... evidence: answered tools/list · calling it writes · required: domains

- **start_company_enrichment** POST /v1/company/enrich. Enrich one or more companies by domain. Returns a job_id (async). Single: domain. Batch: domains, country_code, global_ultimate, list, skip_if_exists. evidence: answered tools/list · calling it writes

- **start_company_enrichment_and_wait** POST /v1/company/enrich then poll GET /v1/company/enrich/{job_id}/status until status is "completed" or "failed" or timeout. Same params as start_company_enrichment plus poll_interval_seconds and timeout_seconds. evidence: answered tools/list · calling it writes

140 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 601 are unmeasured, which is not the same as empty. Harvest last run 2026-09-18. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-18 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

727 of 1252 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to mcp.datamerge.ai with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://mcp.datamerge.ai](https://mcp.datamerge.ai)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 100 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://mcp.datamerge.ai

**Notes, verbatim from the file**
Homepage fetch failed (HTTPError 400); what_it_does used staging desc. mcp_status=community from official-mcp-registry listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave Q 2026-09-12.

**Provenance**

- **Entry id**: 01-datamerge-mcp

- **Source file**: 01-data-enrichment.md

- **Source line**: 4216

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-20

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
