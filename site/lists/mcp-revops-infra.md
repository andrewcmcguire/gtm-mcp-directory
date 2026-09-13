# RevOps infrastructure tools with MCP servers: 31 of 52, counted

> 31 of the 52 revops infra tools in The GTM MCP Directory have an MCP server: 29 official and 2 community. The server URL, auth model and access gate for each. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / RevOps infrastructure tools with an MCP server

**List · 31 of 514**

## RevOps infrastructure tools with an MCP server

The systems of record, the pipes between them, and the low-code layer a GTM engineer builds on top. Most of category has genuine AI now in one specific corner of the product - Agentforce, Breeze, AI Agent nodes - bolted onto a much larger base of plain rules-based automation. This file tries to draw that line honestly for each one. 31 of 52 entries in this category are reachable by an agent: 29 through a server the vendor maintains and 2 through one somebody else built. The category is tagged most often with Run an automation workflow. [See the full category page](../categories/revops-infra.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Airbyte](../tools/airbyte.md)
airbyte.com | [Official MCP](../mcp/official.md) | [https://mcp.airbyte.ai/mcp](https://mcp.airbyte.ai/mcp) +1 more | OAuth or an API key
Two-layer OAuth 2.0 - OAuth into the Airbyte account/org for the MCP server itself, plus... | [Free to start](../gates/free.md) |
| [Attio](../tools/attio.md)
attio.com | [Official MCP](../mcp/official.md) | [https://mcp.attio.com/mcp](https://mcp.attio.com/mcp) +1 more | OAuth
OAuth - one-time login as the user's own Attio account, no API key needed. Reads... | [Free to start](../gates/free.md) |
| [Cargo](../tools/cargo.md)
getcargo.ai | [Official MCP](../mcp/official.md) | [https://docs.getcargo.ai/](https://docs.getcargo.ai/) | OAuth
unknown for the MCP layer specifically - docs confirm the capability but not its auth... | [Free to start](../gates/free.md) |
| [Census (now operates as "Fivetran Activations")](../tools/census.md)
getcensus.com | [Official MCP](../mcp/official.md) | [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) | API key
API key + secret via env vars (FIVETRAN_API_KEY, FIVETRAN_API_SECRET). | [Free to start](../gates/free.md) |
| [Fivetran](../tools/fivetran.md)
fivetran.com | [Official MCP](../mcp/official.md) | [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) | API key
API key + API secret via env vars, generated from the Fivetran dashboard. Scoped... | [Free to start](../gates/free.md) |
| [Google BigQuery](../tools/google-bigquery.md)
cloud.google.com | [Official MCP](../mcp/official.md) | [https://bigquery.googleapis.com/mcp](https://bigquery.googleapis.com/mcp) +1 more | OAuth or an API key
oauth. The docs state the server uses the "OAuth 2.0 protocol with IAM for authentication... | [Free to start](../gates/free.md) |
| [Hightouch](../tools/hightouch.md)
hightouch.com | [Official MCP](../mcp/official.md) | [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp) | Auth not recorded
Existing Hightouch workspace auth with role-based access control; however the MCP server... | [Free to start](../gates/free.md) |
| [HubSpot](../tools/hubspot.md)
hubspot.com | [Official MCP](../mcp/official.md) | [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp) | OAuth
OAuth 2.0 for the hosted Remote MCP Server (migrating to OAuth 2.1 with PKCE +... | [Free to start](../gates/free.md) |
| [monday.com (monday CRM)](../tools/monday-com.md)
monday.com | [Official MCP](../mcp/official.md) | [https://mcp.monday.com/mcp](https://mcp.monday.com/mcp) +3 more | OAuth or an API key
oauth for the remote server. The vendor states "monday MCP remote server connects via the... | [Free to start](../gates/free.md) |
| [n8n](../tools/n8n.md)
n8n.io | [Official MCP](../mcp/official.md) | [https://github.com/n8n-io/n8n](https://github.com/n8n-io/n8n) +2 more | API key
MCP Server Trigger supports Bearer or Header auth to secure the exposed endpoint;... | [Free to start](../gates/free.md) |
| [Pipedrive](../tools/pipedrive.md)
pipedrive.com | [Official MCP](../mcp/official.md) | [https://mcp.pipedrive.com/mcp](https://mcp.pipedrive.com/mcp) +1 more | OAuth
OAuth - "Connect in minutes through secure OAuth. No coding, no API development, no... | [Free to start](../gates/free.md) |
| [Retool](../tools/retool.md)
retool.com | [Official MCP](../mcp/official.md) | [https://mcp.retool.com/mcp](https://mcp.retool.com/mcp) +2 more | OAuth
OAuth 2.0. Endpoint pattern https:///mcp over HTTP. | [Free to start](../gates/free.md) |
| [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md)
snowflake.com | [Official MCP](../mcp/official.md) | [https://docs.snowflake.com/en/user-guide/snowflake-c...](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) +1 more | OAuth
Snowflake OAuth 2.0 by default, or External OAuth (Okta, Microsoft Entra ID); hardcoded... | [Free to start](../gates/free.md) |
| [Zapier](../tools/zapier.md)
zapier.com | [Official MCP](../mcp/official.md) | [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect) +3 more | OAuth or an API key
Reuses Zapier's existing 13+ year credential infrastructure - connect an AI client... | [Free to start](../gates/free.md) |
| [Affinity](../tools/affinity.md)
affinity.co | [Official MCP](../mcp/official.md) | [https://mcp.affinity.co/mcp](https://mcp.affinity.co/mcp) +1 more | OAuth or an API key
OAuth where the client supports it, otherwise an API key. Local deployment is API key... | [Paid, self-serve](../gates/paid.md) |
| [Close (Close CRM)](../tools/close.md)
close.com | [Official MCP](../mcp/official.md) | [https://mcp.close.com/mcp](https://mcp.close.com/mcp) +1 more | OAuth or an API key
Dual - OAuth 2.0 with Dynamic Client Registration (recommended; used by Claude, ChatGPT,... | [Paid, self-serve](../gates/paid.md) |
| [dbt (dbt platform remote MCP)](../tools/dbt.md)
getdbt.com | [Official MCP](../mcp/official.md) | [https://YOUR_DBT_HOST_URL/api/ai/v1/mcp](https://YOUR_DBT_HOST_URL/api/ai/v1/mcp) +3 more | OAuth or an API key
oauth (beta) or token. The docs state "OAuth lets you connect to the remote MCP server... | [Paid, self-serve](../gates/paid.md) |
| [Hex](../tools/hex.md)
hex.tech | [Official MCP](../mcp/official.md) | [https://app.hex.tech/mcp](https://app.hex.tech/mcp) +1 more | OAuth
oauth. The docs state "Complete the OAuth flow to authorize access to your Hex... | [Paid, self-serve](../gates/paid.md) |
| [HighLevel (GoHighLevel)](../tools/highlevel.md)
gohighlevel.com | [Official MCP](../mcp/official.md) | [https://services.leadconnectorhq.com/mcp/](https://services.leadconnectorhq.com/mcp/) +1 more | API key
A Private Integration Token passed as a bearer token, plus a locationId header. Tool... | [Paid, self-serve](../gates/paid.md) |
| [Make](../tools/make.md)
make.com | [Official MCP](../mcp/official.md) | [https://mcp.make.com](https://mcp.make.com) +2 more | OAuth or an API key
Two supported methods - OAuth via Make's cloud (endpoint mcp.make.com) or an MCP Token... | [Paid, self-serve](../gates/paid.md) |
| [Microsoft Dynamics 365 Sales](../tools/microsoft-dynamics-365-sales.md)
microsoft.com | [Official MCP](../mcp/official.md) | [https://agent365.svc.cloud.microsoft/mcp/environment...](https://agent365.svc.cloud.microsoft/mcp/environments/) +1 more | Auth not recorded
enterprise gate. Microsoft Entra identity; the documented prerequisites are admin... | [Paid, self-serve](../gates/paid.md) |
| [Nutshell CRM](../tools/nutshell-crm.md)
nutshell.com | [Official MCP](../mcp/official.md) | [https://app.nutshell.com/mcp](https://app.nutshell.com/mcp) +1 more | OAuth
oauth. The vendor's article instructs the user to add the server URL as a custom... | [Paid, self-serve](../gates/paid.md) |
| [Octave](../tools/octave.md)
octavehq.com | [Official MCP](../mcp/official.md) | [https://docs.octavehq.com/mcp/overview](https://docs.octavehq.com/mcp/overview) +3 more | OAuth or an API key
Browser OAuth. Per the vendor's Claude Code setup doc you add the server with "claude mcp... | [Paid, self-serve](../gates/paid.md) |
| [Ortto](../tools/ortto.md)
ortto.com | [Official MCP](../mcp/official.md) | [https://mcp-api-us.ortto.app/mcp](https://mcp-api-us.ortto.app/mcp) +1 more | Auth not recorded
A scoped JWT key created as an MCP data source inside the Ortto account, passed as a... | [Paid, self-serve](../gates/paid.md) |
| [Superblocks](../tools/superblocks.md)
superblocks.com | [Official MCP](../mcp/official.md) | [https://api.superblocks.com/mcp](https://api.superblocks.com/mcp) +1 more | OAuth
unknown - the announcement doesn't specify the auth method; the feature is... | [Paid, self-serve](../gates/paid.md) |
| [Zoho CRM](../tools/zoho-crm.md)
zoho.com | [Official MCP](../mcp/official.md) | [https://www.zoho.com/crm/developer/mcp.html](https://www.zoho.com/crm/developer/mcp.html) | OAuth
oauth. The vendor's page describes a four-step setup ending in "Authenticate via OAuth.... | [Paid, self-serve](../gates/paid.md) |
| [Looker](../tools/looker.md)
cloud.google.com | [Official MCP](../mcp/official.md) | [https://docs.cloud.google.com/looker/docs/mcp](https://docs.cloud.google.com/looker/docs/mcp) +3 more | OAuth
The managed server uses OAuth 2.1 and an admin "must manually register AI agents as OAuth... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)
salesforce.com | [Official MCP](../mcp/official.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) +2 more | OAuth
OAuth + PKCE via an External Client App (scopes mcp_api, refresh_token); every MCP call... | [Enterprise only](../gates/enterprise-only.md) |
| [Syncari](../tools/syncari.md)
syncari.com | [Official MCP](../mcp/official.md) | [https://mcp.syncari.com/mcp](https://mcp.syncari.com/mcp) +1 more | OAuth or an API key
unknown - the MCP server page describes real-time, entity/field-level access control and... | [Enterprise only](../gates/enterprise-only.md) |
| [Morphed](../tools/morphed.md)
morphed.io | [Community MCP](../mcp/community.md) | [https://morphed.io/mcp](https://morphed.io/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Zetadeck](../tools/zetadeck.md)
zetadeck.com | [Community MCP](../mcp/community.md) | [https://zetadeck.com](https://zetadeck.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |

### The other 21 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [Default](../tools/default.md)
default.com | [MCP unknown](../mcp/unknown.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Openprise](../tools/openprise.md)
openprisetech.com | [No MCP found](../mcp/none-found.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Apsona](../tools/apsona.md)
apsona.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Boomi](../tools/boomi.md)
boomi.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [CloudFiles](../tools/cloudfiles.md)
cloudfiles.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Databox](../tools/databox.md)
databox.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Dust](../tools/dust.md)
dust.tt | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Glean](../tools/glean.md)
glean.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [GoLinks](../tools/golinks.md)
golinks.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Introw](../tools/introw.md)
introw.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [LinkPoint Connect](../tools/linkpoint-connect.md)
linkpoint360.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [PartnerOS](../tools/partneros.md)
partneros.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Relate](../tools/relate.md)
relate.so | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Skyvern](../tools/skyvern.md)
skyvern.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Streak](../tools/streak.md)
streak.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Suger](../tools/suger.md)
suger.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Superglue](../tools/superglue.md)
superglue.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Torchlite](../tools/torchlite.md)
torchlite.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Tray.ai](../tools/tray-ai.md)
tray.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Vertify](../tools/vertify.md)
vertify.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Workato](../tools/workato.md)
workato.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |

### What this category is asked for

The jobs most often tagged on the 21 tagged entries in this category.

- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 514 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
