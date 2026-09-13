# Anaplan (PlanIQ / Anaplan Forecaster): MCP server status, API access gate and what it does

> Connected-planning platform whose AI forecasting engine - originally branded PlanIQ, now superseded by... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Forecasting & Revenue](../categories/forecasting-revenue.md) /
Anaplan (PlanIQ / Anaplan Forecaster)

# Anaplan (PlanIQ / Anaplan Forecaster)

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Forecasting & Revenue](../categories/forecasting-revenue.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [anaplan.com](https://anaplan.com) · entry id 12-anaplan · source 12-forecasting-revenue.md line 283

**What it does**
Connected-planning platform whose AI forecasting engine - originally branded PlanIQ, now superseded by "Anaplan Forecaster" (launched October 2025) - generates time-series demand/sales/revenue forecasts that feed directly into a customer's broader Anaplan models.

**AI features, separated from automation with an AI label on it**
Genuinely ML-based: the vendor names specific algorithms (DeepAR+, Prophet) combining statistical and machine-learning techniques on internal plus enriched external data to uncover patterns and correlations; Anaplan Forecaster is described as the next generation of PlanIQ with expanded ML algorithms and improved explainability. Separately, "CoModeler" (natural-language model building) and role-based AI agents are LLM-workflow features, not the forecasting engine itself.

**RevOps role**
Enterprise connected-planning platform where sales/demand forecasting is one module among many (finance, supply chain, workforce); the AI Gateway/MCP layer is Anaplan's play to make that planning data agent-accessible.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - described only as a "governed MCP connection" with permission/audit controls; the specific credential mechanism (API key vs. OAuth) is not disclosed on the page found.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.anaplan.com/platform/intelligence/ - the "Anaplan AI Gateway" feature page states: "Securely connect any LLM interface or enterprise agent to Anaplan through a governed MCP connection, with controls for permissions, auditability, consumption management, and rate limiting." No separate dedicated MCP docs/repo page was found beyond this feature description. The only resolving server URL found for Anaplan is third-party, not first-party: https://github.com/larasrinath/anaplan-mcp (individually owned, community at most).

- [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/)
- [https://github.com/larasrinath/anaplan-mcp](https://github.com/larasrinath/anaplan-mcp)

**What this server exposes**

- **Tools named**: 70
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: larasrinath/anaplan-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **add_list_items** Add new items to a list. Supports parent (hierarchy placement) and subsets (subset membership). Use show_lists to find listId. Item names must be unique. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **bulk_delete_models** Bulk delete closed models (WARNING: irreversible). Models must be closed first. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **cancel_task** Cancel a running task. taskId comes from the run_* response or show_tasks. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **close_model** Close (archive) a model. Requires workspace admin. Must be closed before bulk_delete_models. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_list_readrequest** Start a large volume list read (for lists too large for get_list_items). Lifecycle: create -> poll with get_list_readrequest -> download pages with get_list_readrequest_page -> cleanup with delete_list_readrequest. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_view_readrequest** Start a large volume view read (for views too large for read_cells). Lifecycle: create -> poll with get_view_readrequest -> download pages with get_view_readrequest_page -> cleanup with delete_view_readrequest. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_file** Delete a file from a model (WARNING: irreversible). Use show_files to find the fileId. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_list_items** Remove items from a list (WARNING: irreversible). Specify id or code for each item. Use get_list_items to find values. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_list_readrequest** Delete a large volume list read request to free server resources. Always call this after downloading all pages. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_view_readrequest** Delete a large volume view read request to free server resources. Always call this after downloading all pages. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **download_file** Download file content from a model. Text files are returned inline; for binary files, set saveToDownloads=true to preserve the exact bytes. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **download_importdump** Download error details from a failed import task as CSV. Data is ephemeral (~48 hours). Prerequisites: importId from show_imports, taskId from run_import response or show_tasks. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **download_optimizer_log** Download Optimizer solver log for a completed optimizer action. Logs are removed after 48 hours. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **download_processdump** Download error details from a failed process task as CSV. Data is ephemeral (~48 hours). Prerequisites: processId from show_processes, taskId from run_process response, objectId from the failed step. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_action_status** Check status of a running task. Poll until taskState is COMPLETE or FAILED. Use includeProcessDetails=true for step timing. taskId from run_* response. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_list_items** Get items in a list. Use includeAll=true for subsets, properties, and selective access details. Returns item IDs for write_cells. For >1M items, use create_list_readrequest. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_list_readrequest** Poll status of a large volume list read. When status is COMPLETE, use get_list_readrequest_page to download each page. requestId comes from create_list_readrequest response. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_list_readrequest_page** Download one page (CSV) from a completed large volume list read. Pages are 0-based. After all pages, use delete_list_readrequest. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_view_readrequest** Poll status of a large volume view read. When status is COMPLETE, use get_view_readrequest_page to download each page (0-based). requestId comes from create_view_readrequest response. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_view_readrequest_page** Download one page (CSV) from a completed large volume view read. Pages are 0-based. After downloading all pages, use delete_view_readrequest to free server resources. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **lookup_dimensionitems** Look up dimension items by name or code to get their IDs. Useful for resolving human-readable names to itemIds before write_cells. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **open_model** Open (wake up) a model. May return 202 if model is loading. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **preview_list** Preview up to 1000 records from a large list (CSV) before initiating a full large read request evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **read_cells** Read cell data from a module view. Use pages param to select specific page dimensions. For reports across ALL products/customers, use run_export instead -- do NOT call read_cells in a loop per item. viewId can be a saved view or moduleId (d evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **reset_list_index** Reset list item index numbering. Note: requires model ID and list ID (name resolution not supported for this tool). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **run_delete** Execute a delete action on a model. Use show_actions first to find the delete action ID. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **run_export** Execute an export and return the data inline. Best for bulk reports across all products/customers/regions -- prefer this over calling read_cells in a loop. Handles the full run-wait-download lifecycle. Use show_exports first. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **run_import** Upload CSV/JSON data to a file, then execute an import action. Use mappingParameters to target a specific dimension (e.g., import into evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **run_process** Execute a process (chain of imports/exports/deletes). Use mappingParameters to target a specific dimension at runtime. Use show_processes first. Monitor with get_action_status; download_processdump for failures. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **set_currentperiod** Set current period for a model (WARNING: may cause data loss if periods are removed). Use show_currentperiod to see the current value first. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **set_fiscalyear** Update fiscal year for model calendar (WARNING: may affect time ranges). Use show_modelcalendar to see the current value first. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **set_versionswitchover** Set version switchover date (WARNING: affects version boundaries). Use show_versions to find versionId. Note: requires model ID (name resolution not supported). evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_actiondetails** Get action definition metadata. Use run_delete to execute delete actions. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_actions** List available actions (including delete actions) in a model. Use run_delete to execute a delete action. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_alllineitems** List all line items in a model (cross-module). Note: requires model ID (name resolution not supported). Use includeAll=true for formulas and dimensions. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_allmodels** List all models across all workspaces. Filter by state param (PRODUCTION, UNLOCKED, etc). Use modelDetails=true for memory/dates. Returns IDs needed by ID-only tools. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_allviews** List all views in a model (cross-module, includes default and saved). Note: requires model ID (name resolution not supported). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_currentperiod** Get current period for a model. Use set_currentperiod to change it. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_currentuser** Get current authenticated user info evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_dimensionitems** List all items in a dimension. Returns itemId values needed for write_cells dimension coordinates. Note: requires model ID (name resolution not supported). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_exportdetails** Get export definition metadata including format and target. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_exports** List available export actions. Use run_export to execute and download data in one step. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_files** List files in a model. File IDs are needed for upload_file (before run_import) and download_file. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_importdetails** Get import definition metadata including source file and column mapping. Check this before run_import to understand the expected data format. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_imports** List available import actions in a model. Use show_importdetails to see source file and mapping, then run_import to execute. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_lineitem_dimensions** List dimensions for a line item. Returns dimensionId values needed by write_cells and show_dimensionitems. Note: requires model ID (name resolution not supported). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_lineitem_dimensions_items** List dimension items for a specific line item evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_lineitems** List line items in a module. Line item IDs are needed for write_cells. Use includeAll=true for formulas, formats, and dimensions. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_listmetadata** Get list metadata including properties, parent, and item count. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_lists** List all dimensions (lists) in a model. List IDs are needed for get_list_items, add/update/delete_list_items, and large volume list reads. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_modelcalendar** Get model calendar including fiscal year settings. Use set_fiscalyear to change the fiscal year. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_modeldetails** Get model details including status and workspace binding. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_models** List models in a workspace. Filter by state param (PRODUCTION, UNLOCKED, etc). Use modelDetails=true for memory/dates. Use show_modules next. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_modelstatus** Check model status including memory usage and export progress. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_moduledetails** Get module details with default view dimension metadata (rows, columns, pages). The default viewId equals the moduleId -- use it with read_cells directly. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_modules** List all modules in a model. Use show_lineitems to see a module evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_processdetails** Get process definition metadata including the chain of import/export actions. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_processes** List available processes (chained import/export actions). Use run_process to execute, then get_action_status to monitor. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_savedviews** List saved views in a module. Use includeSubsidiaryViews=true for unsaved subsidiary views. View IDs needed for read_cells. Tip: moduleId works as default viewId. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_tasks** List task history for an import, export, process, or action. Returns taskIds for use with get_action_status, cancel_task, or download_importdump/download_processdump. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_userdetails** Get user details by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_users** List all users in the tenant evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_versions** List version metadata (Current, Forecast, etc.) for a model. Version IDs are needed for set_versionswitchover. Note: requires model ID (name resolution not supported). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_viewdetails** Get view dimension layout (rows, columns, pages). Dimension IDs from here are needed for write_cells and show_viewdimensionitems. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_viewdimensionitems** List items in a dimension as filtered by a view. Useful for understanding what data a view includes. Note: requires model ID (name resolution not supported). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_workspacedetails** Get workspace details including size and active status. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **show_workspaces** List all accessible Anaplan workspaces. Use tenantDetails=true for size/quota info. Start here, then use show_models. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_list_items** Update existing items in a list. Use get_list_items to find item IDs. Important: if an item has a code value, you must include the code field in the update or Anaplan returns an error. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **upload_file** Upload CSV or text data to an Anaplan file (overwrites existing). Use compress=true for large files (>50MB). Typically followed by run_import. Use show_files for fileId. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **write_cells** Write values to specific cells. Supports both ID-based and name-based targeting: use lineItemName/dimensionName/itemName instead of IDs to skip the dimension resolution chain. For ID-based writes, use show_lineitem_dimensions then show_dime evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (/pricing resolves to a contact form promising an Anaplan expert will connect with you, with no pricing page and no developer or API portal link in nav or footer)

**API documentation**

No documentation URL recorded.

374 of 468 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/larasrinath/anaplan-mcp](https://github.com/larasrinath/anaplan-mcp)

**On GitHub**

No GitHub organisation could be tied to anaplan.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

6 candidate accounts seen and rejected by the evidence rules: larasrinath, anaplaninc, anaplan-engineering, AnaplanTestEnv, anaplan-gitops. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)
- [Model a revenue plan](../jobs/model-revenue-plan.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 468 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.anaplan.com/platform/anaplan-planiq/](https://www.anaplan.com/platform/anaplan-planiq/)
- [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/)
- [https://help.anaplan.com/drive-intelligent-forecasting-with-planiq-7333fab4-7118-45d9-8504-4137bc114e04](https://help.anaplan.com/drive-intelligent-forecasting-with-planiq-7333fab4-7118-45d9-8504-4137bc114e04)
- [https://www.globenewswire.com/news-release/2025/12/09/3202449/0/en/Anaplan-Introduces-Role-Based-AI-Agents-to-Advance-Industry-Leading-Enterprise-Scenario-Planning-and-Analysis-Platform.html](https://www.globenewswire.com/news-release/2025/12/09/3202449/0/en/Anaplan-Introduces-Role-Based-AI-Agents-to-Advance-Industry-Leading-Enterprise-Scenario-Planning-and-Analysis-Platform.html)
- [https://www.pulsemcp.com/servers?q=anaplan](https://www.pulsemcp.com/servers?q=anaplan)
- [https://www.anaplan.com/pricing/](https://www.anaplan.com/pricing/)
- [https://github.com/larasrinath/anaplan-mcp](https://github.com/larasrinath/anaplan-mcp)

7 source URLs. Raw sources field, verbatim:

https://www.anaplan.com/platform/anaplan-planiq/, https://www.anaplan.com/platform/intelligence/, https://help.anaplan.com/drive-intelligent-forecasting-with-planiq-7333fab4-7118-45d9-8504-4137bc114e04, https://www.globenewswire.com/news-release/2025/12/09/3202449/0/en/Anaplan-Introduces-Role-Based-AI-Agents-to-Advance-Industry-Leading-Enterprise-Scenario-Planning-and-Analysis-Platform.html, https://www.pulsemcp.com/servers?q=anaplan, https://www.anaplan.com/pricing/, https://github.com/larasrinath/anaplan-mcp

**Notes, verbatim from the file**
Marked official rather than none-found because Anaplan's own product page explicitly names MCP with a linkable URL, satisfying the schema's "URL required" law - the same judgment call made for the Default entry in 06-revops-infra.md - even though no dedicated MCP docs/repo page exists yet. Re-check as this matures; it currently reads as an early/generic capability statement rather than a documented integration. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.anaplan.com/pricing/): /pricing resolves to a contact form promising an Anaplan expert will connect with you, with no pricing page and no developer or API portal link in nav or footer. 2026-09-07: larasrinath/anaplan-mcp (7 stars) is a real server: src/server.ts plus src/tools/{bulk,exploration,transactional}.ts, README "MCP server for Anaplan Integration API v2." Owner is an individual, so third-party (https://github.com/larasrinath/anaplan-mcp). 2026-09-07: LAW 1 FLAG, NOT DOWNGRADED. What the official claim actually rests on: the "Anaplan AI Gateway" feature page at https://www.anaplan.com/platform/intelligence/, which describes a governed MCP connection but publishes no resolving server URL. The finder searched GitHub owner anaplan, npm, PyPI and the official registry and probed https://mcp.anaplan.com/mcp with no first-party result; the only real servers found (larasrinath/anaplan-mcp, VinzenzKlass/anaplan-mcp, FireEden/anaplan-mcp-model-management) are all third-party. A human should decide whether official survives law 1.

**Provenance**

- **Entry id**: 12-anaplan

- **Source file**: 12-forecasting-revenue.md

- **Source line**: 283

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
