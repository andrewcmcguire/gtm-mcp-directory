# GTM MCP servers that use an API key: 44 tools, counted

> 44 of the 165 GTM tools with an MCP server use an API key. The verbatim auth field for each one is printed beside it. Counted 2026-08-28.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers that use an API key

**List · 44 of 293**

## GTM MCP servers that use an API key

The server authenticates with a key or token the operator generates and pastes in. Simple to wire, and the key is as powerful as whatever the vendor scoped it to. The bucket is a keyword match over the mcp_auth field, run at build time, and the verbatim field ships in the row beside it so you can check the parse yourself. Where the two disagree, the verbatim field is the fact and the bucket is the convenience.

| Tool | MCP status | Server URL | mcp_auth, verbatim | Gate |
|---|---|---|---|---|
| [Autobound](../tools/autobound.md)
autobound.ai | [Official MCP](../mcp/official.md) | [https://www.autobound.ai/integrations/mcp](https://www.autobound.ai/integrations/mcp) +1 more | api key via an AUTOBOUND_API_KEY environment variable in the MCP client config. | [Free to start](../gates/free.md) |
| [Census (now operates as "Fivetran Activations")](../tools/census.md)
getcensus.com | [Official MCP](../mcp/official.md) | [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) | API key + secret via env vars (FIVETRAN_API_KEY, FIVETRAN_API_SECRET). | [Free to start](../gates/free.md) |
| [Diffbot](../tools/diffbot.md)
diffbot.com | [Official MCP](../mcp/official.md) | [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp) | api key (free Diffbot token required to use the MCP tools) | [Free to start](../gates/free.md) |
| [Enrow](../tools/enrow.md)
enrow.io | [Official MCP](../mcp/official.md) | [https://github.com/EnrowAPI/enrow-mcp](https://github.com/EnrowAPI/enrow-mcp) +1 more | api key. ENROW_API_KEY env var for stdio, or an Authorization Bearer / x-enrow-api-key header for remote HTTP. | [Free to start](../gates/free.md) |
| [Exa](../tools/exa.md)
exa.ai | [Official MCP](../mcp/official.md) | [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) +1 more | api key (issued via dashboard.exa.ai) | [Free to start](../gates/free.md) |
| [Fivetran](../tools/fivetran.md)
fivetran.com | [Official MCP](../mcp/official.md) | [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) | API key + API secret via env vars, generated from the Fivetran dashboard. Scoped permission tiers (read / read-write / read-write-delete) with a... | [Free to start](../gates/free.md) |
| [Hunter.io](../tools/hunter-io.md)
hunter.io | [Official MCP](../mcp/official.md) | [https://hunter.io/api-documentation#mcp](https://hunter.io/api-documentation#mcp) | api key (HUNTER_API_KEY) | [Free to start](../gates/free.md) |
| [Lusha](../tools/lusha.md)
lusha.com | [Official MCP](../mcp/official.md) | [https://github.com/lusha-oss/lusha-public-api-mcp](https://github.com/lusha-oss/lusha-public-api-mcp) +2 more | api key (LUSHA_API_KEY) | [Free to start](../gates/free.md) |
| [Model Context Protocol - official servers repo](../tools/model-context-protocol-official-servers-repo.md)
github.com | [Official MCP](../mcp/official.md) | [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Per-server - individual servers take credentials (e.g. API tokens) via environment variables or CLI args where needed; the repo itself has no central... | [Free to start](../gates/free.md) |
| [n8n](../tools/n8n.md)
n8n.io | [Official MCP](../mcp/official.md) | [https://docs.n8n.io/integrations/builtin/core-nodes/...](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger) +1 more | MCP Server Trigger supports Bearer or Header auth to secure the exposed endpoint; supports SSE and streamable-HTTP transport with separate... | [Free to start](../gates/free.md) |
| [PredictLeads](../tools/predictleads.md)
predictleads.com | [Official MCP](../mcp/official.md) | [https://mcp.predictleads.com/](https://mcp.predictleads.com/) | api key (same API key/token used for REST API calls, per vendor blog) | [Free to start](../gates/free.md) |
| [TheirStack](../tools/theirstack.md)
theirstack.com | [Official MCP](../mcp/official.md) | [https://theirstack.com/en/docs/mcp](https://theirstack.com/en/docs/mcp) +2 more | api key (same credentials as the REST API) | [Free to start](../gates/free.md) |
| [Airspeed (formerly Glyphic)](../tools/airspeed.md)
goairspeed.com | [Official MCP](../mcp/official.md) | [https://api.glyphic.ai/mcp](https://api.glyphic.ai/mcp) +1 more | Airspeed API key passed as an X-API-Key header. | [Paid, self-serve](../gates/paid.md) |
| [Avoma](../tools/avoma.md)
avoma.com | [Official MCP](../mcp/official.md) | [https://help.avoma.com/admins-add-avoma-mcp-connecto...](https://help.avoma.com/admins-add-avoma-mcp-connector-in-claude) | API key pair (CLIENT_KEY:CLIENT_SECRET) generated at Settings → Organization → Developer. | [Paid, self-serve](../gates/paid.md) |
| [Bright Data](../tools/bright-data.md)
brightdata.com | [Official MCP](../mcp/official.md) | [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | api key (Bright Data API token) | [Paid, self-serve](../gates/paid.md) |
| [Clay](../tools/clay.md)
clay.com | [Official MCP](../mcp/official.md) | [https://www.clay.com/mcp](https://www.clay.com/mcp) +1 more | Session cookie - the same token used to log into app.clay.com in-browser, which grants full account access (tables, records, enrichments, CRM... | [Paid, self-serve](../gates/paid.md) |
| [Crustdata](../tools/crustdata.md)
crustdata.com | [Official MCP](../mcp/official.md) | [https://docs.crustdata.com/for-agents/mcp.md](https://docs.crustdata.com/for-agents/mcp.md) +1 more | api key (free sandbox key available) | [Paid, self-serve](../gates/paid.md) |
| [CUFinder](../tools/cufinder.md)
cufinder.io | [Official MCP](../mcp/official.md) | [https://mcp.cufinder.io/mcp](https://mcp.cufinder.io/mcp) +1 more | api key from the CUFinder dashboard under Account Settings then API Dashboard. Streamable HTTP transport, explicitly stated by the vendor. | [Paid, self-serve](../gates/paid.md) |
| [Explorium](../tools/explorium.md)
explorium.ai | [Official MCP](../mcp/official.md) | [https://www.explorium.ai/mcp/](https://www.explorium.ai/mcp/) +1 more | api key | [Paid, self-serve](../gates/paid.md) |
| [Factors.ai](../tools/factors-ai.md)
factors.ai | [Official MCP](../mcp/official.md) | [https://help.factors.ai/en/articles/14705206-factors...](https://help.factors.ai/en/articles/14705206-factors-mcp) | Personal access token (generated in Settings > AI Features), used via Claude custom connector or a local Python 3.11+ package. | [Paid, self-serve](../gates/paid.md) |
| [HighLevel (GoHighLevel)](../tools/highlevel.md)
gohighlevel.com | [Official MCP](../mcp/official.md) | [https://services.leadconnectorhq.com/mcp/](https://services.leadconnectorhq.com/mcp/) +1 more | A Private Integration Token passed as a bearer token, plus a locationId header. Tool availability follows the scopes granted to the token. | [Paid, self-serve](../gates/paid.md) |
| [Infraforge](../tools/infraforge.md)
infraforge.ai | [Official MCP](../mcp/official.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) | API key, generated from the Infraforge/Salesforge dashboard. | [Paid, self-serve](../gates/paid.md) |
| [Instantly](../tools/instantly.md)
instantly.ai | [Official MCP](../mcp/official.md) | [https://mcp.instantly.ai/mcp](https://mcp.instantly.ai/mcp) +1 more | api key (generated in Instantly Settings > Integrations > API Keys) | [Paid, self-serve](../gates/paid.md) |
| [Lead411](../tools/lead411.md)
lead411.com | [Official MCP](../mcp/official.md) | [https://mcp.lead411.com/mcp](https://mcp.lead411.com/mcp) +3 more | api key via X-API-KEY header. TRANSPORT IS DISPUTED: the official registry record says SSE, PulseMCP says Streamable HTTP. Verify at connect time. | [Paid, self-serve](../gates/paid.md) |
| [Mailforge](../tools/mailforge.md)
mailforge.ai | [Official MCP](../mcp/official.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) | API key, generated from the Mailforge dashboard. | [Paid, self-serve](../gates/paid.md) |
| [Ocean.io](../tools/ocean-io.md)
ocean.io | [Official MCP](../mcp/official.md) | [https://app.ocean.io/docs/getting-started/mcp](https://app.ocean.io/docs/getting-started/mcp) +1 more | api key (api-token passed as a URL parameter to the hosted MCP endpoint) | [Paid, self-serve](../gates/paid.md) |
| [RB2B](../tools/rb2b.md)
rb2b.com | [Official MCP](../mcp/official.md) | [https://registry.npmjs.org/@rb2b/rb2b-apis-mcp](https://registry.npmjs.org/@rb2b/rb2b-apis-mcp) | api key | [Paid, self-serve](../gates/paid.md) |
| [Reply.io](../tools/reply-io.md)
reply.io | [Official MCP](../mcp/official.md) | [https://reply.io/mcp/](https://reply.io/mcp/) | api key (personal API key over HTTPS, included in free trial) | [Paid, self-serve](../gates/paid.md) |
| [Salesforge](../tools/salesforge.md)
salesforge.ai | [Official MCP](../mcp/official.md) | [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp) | api key via HTTP header (X-Salesforge-Key) | [Paid, self-serve](../gates/paid.md) |
| [Super Send](../tools/super-send.md)
supersend.io | [Official MCP](../mcp/official.md) | [https://docs.supersend.io/docs/mcp-server](https://docs.supersend.io/docs/mcp-server) | api key, Streamable HTTP transport | [Paid, self-serve](../gates/paid.md) |
| [tl;dv](../tools/tl-dv.md)
tldv.io | [Official MCP](../mcp/official.md) | [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server) +1 more | API key generated at Settings → Personal Settings → API keys. | [Paid, self-serve](../gates/paid.md) |
| [HG Insights (Phoenix platform)](../tools/hg-insights.md)
hginsights.com | [Official MCP](../mcp/official.md) | [https://learn.microsoft.com/en-us/connectors/hginsig...](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/) | api key (`x-api-key` header; throttled to 100 calls/60 seconds per connection) | [Enterprise only](../gates/enterprise-only.md) |
| [Surfe](../tools/surfe.md)
surfe.com | [Official MCP](../mcp/official.md) | [https://mcp.eu.surfe.com/mcp](https://mcp.eu.surfe.com/mcp) +1 more | Surfe API key, with a browser sign-in flow that exchanges the key for a managed token so it is entered once, or the key passed directly per call.... | [Enterprise only](../gates/enterprise-only.md) |
| [RevenueHero](../tools/revenuehero.md)
revenuehero.io | [Official MCP](../mcp/official.md) | [https://www.revenuehero.io/resources/tales-of-ops](https://www.revenuehero.io/resources/tales-of-ops) | Per-customer router token over an SSE endpoint, manually provisioned by RevenueHero - not a self-serve API-key flow. | [Gate unknown](../gates/unknown.md) |
| [Fathom](../tools/fathom.md)
fathom.video | [Community MCP](../mcp/community.md) | [https://github.com/trevorwelch/fathom-video-mcp](https://github.com/trevorwelch/fathom-video-mcp) +2 more | Community servers authenticate with a Fathom API key (FATHOM_API_KEY environment variable). | [Free to start](../gates/free.md) |
| [Loom](../tools/loom.md)
loom.com | [Community MCP](../mcp/community.md) | [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom) +2 more | karbassi/mcp-loom uses Loom's undocumented internal GraphQL API via a browser session cookie (connect.sid) manually extracted from a logged-in... | [Free to start](../gates/free.md) |
| [People Data Labs](../tools/people-data-labs.md)
peopledatalabs.com | [Community MCP](../mcp/community.md) | [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp) | api key (PDL_API_KEY environment variable) | [Free to start](../gates/free.md) |
| [Motion](../tools/motion.md)
usemotion.com | [Community MCP](../mcp/community.md) | [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp) | API key (MOTION_API_KEY from Motion Settings -> API), per community repos. Rate limits reported at 12 req/min for individual accounts, 120 req/min... | [Paid, self-serve](../gates/paid.md) |
| [Overloop](../tools/overloop.md)
overloop.com | [Community MCP](../mcp/community.md) | [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp) | api key via OVERLOOP_API_KEY environment variable | [Paid, self-serve](../gates/paid.md) |
| [SavvyCal](../tools/savvycal.md)
savvycal.com | [Community MCP](../mcp/community.md) | [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server) | API key (SAVVYCAL_API_KEY env var, a personal access token from SavvyCal's Developer Settings). MIT-licensed repo, not explicitly disclaiming... | [Paid, self-serve](../gates/paid.md) |
| [Smartlead](../tools/smartlead.md)
smartlead.ai | [Community MCP](../mcp/community.md) | [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server) +1 more | api key | [Paid, self-serve](../gates/paid.md) |
| [Syften](../tools/syften.md)
syften.com | [Community MCP](../mcp/community.md) | [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening) | Community server presumably authenticates with a Syften API key (matching Syften's own API auth model); not independently confirmed for this specific... | [Paid, self-serve](../gates/paid.md) |
| [Trigify (Trigify.io)](../tools/trigify.md)
trigify.io | [Community MCP](../mcp/community.md) | [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli) | api key (from app.trigify.io/settings; via `trigify login --api-key`, env var TRIGIFY_API_KEY, or a per-command flag) | [Paid, self-serve](../gates/paid.md) |
| [Copy.ai (GTM AI Platform)](../tools/copy-ai.md)
copy.ai | [Community MCP](../mcp/community.md) | [https://github.com/anhuaxiang/copy-ai-mcp](https://github.com/anhuaxiang/copy-ai-mcp) | API key via COPY_AI_API_KEY environment variable | [Enterprise only](../gates/enterprise-only.md) |

Counted 2026-08-28 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
