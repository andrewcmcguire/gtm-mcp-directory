# MCP Layer tools with MCP servers: 14 of 19, counted

> 14 of the 19 mcp layer tools in The GTM MCP Directory have an MCP server: 14 official and 0 community. The server URL, auth model and access gate for each. Counted 2026-09-11.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / MCP Layer tools with an MCP server

**List · 14 of 336**

## MCP Layer tools with an MCP server

The layer that sits between an AI agent and the hundred SaaS apps a GTM team actually runs on: registries that just list servers, and aggregators that host/broker them. The load-bearing question for every entry below is who holds the OAuth tokens when you connect - read `notes` before you wire anything into a production agent. 14 of 19 entries in this category are reachable by an agent: 14 through a server the vendor maintains and 0 through one somebody else built. The category is tagged most often with Proxy tool calls to SaaS apps. [See the full category page](../categories/mcp-infrastructure.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Apideck](../tools/apideck.md)
apideck.com | [Official MCP](../mcp/official.md) | [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp) +1 more | OAuth or an API key
Managed OAuth via Apideck Vault on the hosted endpoint, or x-apideck-api-key plus... | [Free to start](../gates/free.md) |
| [Composio](../tools/composio.md)
composio.dev | [Official MCP](../mcp/official.md) | [https://connect.composio.dev/mcp](https://connect.composio.dev/mcp) +2 more | OAuth or an API key
Composio brokers OAuth for each connected toolkit (HubSpot, Gmail, Slack, etc.) on the... | [Free to start](../gates/free.md) |
| [Knit MCP](../tools/knit-mcp.md)
getknit.dev | [Official MCP](../mcp/official.md) | [https://www.getknit.dev/mcp-servers](https://www.getknit.dev/mcp-servers) +1 more | OAuth
Knit-managed OAuth or SAML per connected application; the customer authorises each end... | [Free to start](../gates/free.md) |
| [Merge Agent Handler](../tools/merge-agent-handler.md)
merge.dev | [Official MCP](../mcp/official.md) | [https://github.com/merge-api/merge-mcp](https://github.com/merge-api/merge-mcp) +3 more | OAuth or an API key
api key in an Authorization Bearer header, alongside the identity encoded in the URL... | [Free to start](../gates/free.md) |
| [Model Context Protocol - official servers repo](../tools/model-context-protocol-official-servers-repo.md)
github.com | [Official MCP](../mcp/official.md) | [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | API key
Per-server - individual servers take credentials (e.g. API tokens) via environment... | [Free to start](../gates/free.md) |
| [Pipeworx](../tools/pipeworx.md)
pipeworx.io | [Official MCP](../mcp/official.md) | [https://gateway.pipeworx.io/mcp](https://gateway.pipeworx.io/mcp) +4 more | Auth not recorded
none required for the free tiers. The vendor states "No API keys" and that an anonymous... | [Free to start](../gates/free.md) |
| [StackOne](../tools/stackone.md)
stackone.com | [Official MCP](../mcp/official.md) | [https://mcp.stackone.com/mcp](https://mcp.stackone.com/mcp) +2 more | OAuth or an API key
Basic authentication plus a per-account identifier, with StackOne brokering OAuth, API... | [Free to start](../gates/free.md) |
| [usefulapi.io](../tools/usefulapi-io.md)
usefulapi.io | [Official MCP](../mcp/official.md) | [https://pipedrive.usefulapi.io/mcp](https://pipedrive.usefulapi.io/mcp) +3 more | OAuth or an API key
per-application OAuth. The setup instructions add the subdomain as a custom connector and... | [Free to start](../gates/free.md) |
| [Zapier MCP](../tools/zapier-mcp.md)
zapier.com | [Official MCP](../mcp/official.md) | [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect) +3 more | OAuth
Uses Zapier's existing decade-old app-connection/OAuth infrastructure - you authorize... | [Free to start](../gates/free.md) |
| [Metorial](../tools/metorial.md)
metorial.com | [Official MCP](../mcp/official.md) | [https://github.com/metorial/metorial](https://github.com/metorial/metorial) +1 more | OAuth or an API key
Fully custodial - Metorial stores and centrally manages OAuth tokens for every connected... | [Paid, self-serve](../gates/paid.md) |
| [Pipedream MCP](../tools/pipedream-mcp.md)
pipedream.com | [Official MCP](../mcp/official.md) | [https://mcp.pipedream.com](https://mcp.pipedream.com) | OAuth or an API key
OAuth/API-key credentials for each underlying app are stored by Pipedream and isolated... | [Paid, self-serve](../gates/paid.md) |
| [Paragon (ActionKit MCP)](../tools/paragon.md)
useparagon.com | [Official MCP](../mcp/official.md) | [https://github.com/useparagon/paragon-mcp](https://github.com/useparagon/paragon-mcp) +1 more | OAuth
Paragon user token plus Connect Portal OAuth. The distinguishing feature is that the... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md)
turbomcp.ai | [Official MCP](../mcp/official.md) | [https://github.com/dylibso/mcp.run-servlets](https://github.com/dylibso/mcp.run-servlets) +1 more | OAuth
Integrates with a team's own OIDC-compatible identity provider; handles OAuth and Dynamic... | [Enterprise only](../gates/enterprise-only.md) |
| [Klavis AI](../tools/klavis-ai.md)
klavis.ai | [Official MCP](../mcp/official.md) | [https://www.klavis.ai/docs/concepts/strata.md](https://www.klavis.ai/docs/concepts/strata.md) +2 more | OAuth or an API key
Klavis API key as an HTTP Bearer token on the management API that creates a per-user... | [Gate unknown](../gates/unknown.md) |

### The other 5 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [mcp.so](../tools/mcp-so.md)
mcp.so | [MCP unknown](../mcp/unknown.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |
| [Claude / Anthropic MCP Connector Directory](../tools/claude-anthropic-mcp-connector-directory.md)
claude.com | [MCP not applicable](../mcp/n-a.md) | [Free to start](../gates/free.md) | 2026-08-24 |
| [PulseMCP](../tools/pulsemcp.md)
pulsemcp.com | [MCP not applicable](../mcp/n-a.md) | [Free to start](../gates/free.md) | 2026-08-24 |
| [Smithery](../tools/smithery.md)
smithery.ai | [MCP not applicable](../mcp/n-a.md) | [Free to start](../gates/free.md) | 2026-08-24 |
| [Glama (MCP directory)](../tools/glama.md)
glama.ai | [MCP not applicable](../mcp/n-a.md) | [Gate unknown](../gates/unknown.md) | 2026-08-24 |

### What this category is asked for

The jobs most often tagged on the 10 tagged entries in this category.

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)
- [Discover MCP servers](../jobs/discover-mcp-servers.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

Counted 2026-09-11 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 336 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
