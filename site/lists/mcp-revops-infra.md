# RevOps infrastructure tools with MCP servers: 21 of 23, counted

> 21 of the 23 revops infra tools in The GTM MCP Directory have an MCP server: 21 official and 0 community. The server URL, auth model and access gate for each. Counted 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / RevOps infrastructure tools with an MCP server

**List · 21 of 293**

## RevOps infrastructure tools with an MCP server

The systems of record, the pipes between them, and the low-code layer a GTM engineer builds on top. Most of category has genuine AI now in one specific corner of the product - Agentforce, Breeze, AI Agent nodes - bolted onto a much larger base of plain rules-based automation. This file tries to draw that line honestly for each one. 21 of 23 entries in this category are reachable by an agent: 21 through a server the vendor maintains and 0 through one somebody else built. The category is tagged most often with Run an automation workflow. [See the full category page](../categories/revops-infra.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Airbyte](../tools/airbyte.md)
airbyte.com | [Official MCP](../mcp/official.md) | [https://docs.airbyte.com/ai-agents/interfaces/mcp](https://docs.airbyte.com/ai-agents/interfaces/mcp) | OAuth or an API key
Two-layer OAuth 2.0 - OAuth into the Airbyte account/org for the MCP server itself, plus... | [Free to start](../gates/free.md) |
| [Attio](../tools/attio.md)
attio.com | [Official MCP](../mcp/official.md) | [https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview) +1 more | OAuth
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
| [Hightouch](../tools/hightouch.md)
hightouch.com | [Official MCP](../mcp/official.md) | [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp) | Auth not recorded
Existing Hightouch workspace auth with role-based access control; however the MCP server... | [Free to start](../gates/free.md) |
| [HubSpot](../tools/hubspot.md)
hubspot.com | [Official MCP](../mcp/official.md) | [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp) | OAuth
OAuth 2.0 for the hosted Remote MCP Server (migrating to OAuth 2.1 with PKCE +... | [Free to start](../gates/free.md) |
| [n8n](../tools/n8n.md)
n8n.io | [Official MCP](../mcp/official.md) | [https://docs.n8n.io/integrations/builtin/core-nodes/...](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger) +1 more | API key
MCP Server Trigger supports Bearer or Header auth to secure the exposed endpoint;... | [Free to start](../gates/free.md) |
| [Pipedrive](../tools/pipedrive.md)
pipedrive.com | [Official MCP](../mcp/official.md) | [https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server) | OAuth
OAuth - "Connect in minutes through secure OAuth. No coding, no API development, no... | [Free to start](../gates/free.md) |
| [Retool](../tools/retool.md)
retool.com | [Official MCP](../mcp/official.md) | [https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server) | OAuth
OAuth 2.0. Endpoint pattern https:///mcp over HTTP. | [Free to start](../gates/free.md) |
| [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md)
snowflake.com | [Official MCP](../mcp/official.md) | [https://docs.snowflake.com/en/user-guide/snowflake-c...](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) | OAuth
Snowflake OAuth 2.0 by default, or External OAuth (Okta, Microsoft Entra ID); hardcoded... | [Free to start](../gates/free.md) |
| [Zapier](../tools/zapier.md)
zapier.com | [Official MCP](../mcp/official.md) | [https://zapier.com/mcp](https://zapier.com/mcp) +1 more | OAuth or an API key
Reuses Zapier's existing 13+ year credential infrastructure - connect an AI client... | [Free to start](../gates/free.md) |
| [Affinity](../tools/affinity.md)
affinity.co | [Official MCP](../mcp/official.md) | [https://mcp.affinity.co/mcp](https://mcp.affinity.co/mcp) +1 more | OAuth or an API key
OAuth where the client supports it, otherwise an API key. Local deployment is API key... | [Paid, self-serve](../gates/paid.md) |
| [Close (Close CRM)](../tools/close.md)
close.com | [Official MCP](../mcp/official.md) | [https://help.close.com/integrations/close-mcp-server](https://help.close.com/integrations/close-mcp-server) +1 more | OAuth or an API key
Dual - OAuth 2.0 with Dynamic Client Registration (recommended; used by Claude, ChatGPT,... | [Paid, self-serve](../gates/paid.md) |
| [HighLevel (GoHighLevel)](../tools/highlevel.md)
gohighlevel.com | [Official MCP](../mcp/official.md) | [https://services.leadconnectorhq.com/mcp/](https://services.leadconnectorhq.com/mcp/) +1 more | API key
A Private Integration Token passed as a bearer token, plus a locationId header. Tool... | [Paid, self-serve](../gates/paid.md) |
| [Make](../tools/make.md)
make.com | [Official MCP](../mcp/official.md) | [https://developers.make.com/mcp-server](https://developers.make.com/mcp-server) | OAuth or an API key
Two supported methods - OAuth via Make's cloud (endpoint mcp.make.com) or an MCP Token... | [Paid, self-serve](../gates/paid.md) |
| [Octave](../tools/octave.md)
octavehq.com | [Official MCP](../mcp/official.md) | [https://docs.octavehq.com/mcp/overview](https://docs.octavehq.com/mcp/overview) +3 more | OAuth or an API key
Browser OAuth. Per the vendor's Claude Code setup doc you add the server with "claude mcp... | [Paid, self-serve](../gates/paid.md) |
| [Ortto](../tools/ortto.md)
ortto.com | [Official MCP](../mcp/official.md) | [https://mcp-api-us.ortto.app/mcp](https://mcp-api-us.ortto.app/mcp) +1 more | Auth not recorded
A scoped JWT key created as an MCP data source inside the Ortto account, passed as a... | [Paid, self-serve](../gates/paid.md) |
| [Superblocks](../tools/superblocks.md)
superblocks.com | [Official MCP](../mcp/official.md) | [https://superblocks.com/blog/superblocks-mcp](https://superblocks.com/blog/superblocks-mcp) | OAuth
unknown - the announcement doesn't specify the auth method; the feature is... | [Paid, self-serve](../gates/paid.md) |
| [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)
salesforce.com | [Official MCP](../mcp/official.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) +2 more | OAuth
OAuth + PKCE via an External Client App (scopes mcp_api, refresh_token); every MCP call... | [Enterprise only](../gates/enterprise-only.md) |
| [Syncari](../tools/syncari.md)
syncari.com | [Official MCP](../mcp/official.md) | [https://syncari.com/mcp-server/](https://syncari.com/mcp-server/) | OAuth or an API key
unknown - the MCP server page describes real-time, entity/field-level access control and... | [Enterprise only](../gates/enterprise-only.md) |

### The other 2 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [Default](../tools/default.md)
default.com | [MCP unknown](../mcp/unknown.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Openprise](../tools/openprise.md)
openprisetech.com | [No MCP found](../mcp/none-found.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-08-24 |

### What this category is asked for

The jobs most often tagged on the 21 tagged entries in this category.

- [Run an automation workflow](../jobs/run-automation-workflow.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)

Counted 2026-09-03 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
