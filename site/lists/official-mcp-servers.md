# Official MCP servers list: 200 GTM tools, with links

> The full list of 200 go to market tools whose vendor ships and maintains its own MCP server, with the server URL, the auth model and the access gate for each. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / The 200 GTM tools with an official MCP server

**List · 200 of 468**

## The 200 GTM tools with an official MCP server

Official means first party. The vendor ships and maintains the server itself, and a wrapper built by Zapier, viaSocket, Composio or any other third party does not count no matter how well it works. 199 of these 200 entries carry a parseable URL in the mcp_url field; the rest claim a server in prose without one, which is recorded as a risk on the [methodology page](../methodology.md) rather than cleaned up quietly. Probed live on 2026-09-04: 27 of the official entries record a URL that answered as an MCP server, and 88 record a documentation page rather than an endpoint. Each tool page says which.

| Tool | Category | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Airbyte](../tools/airbyte.md)
airbyte.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.airbyte.ai/mcp](https://mcp.airbyte.ai/mcp) +1 more | OAuth or an API key
Two-layer OAuth 2.0 - OAuth into the Airbyte account/org for the MCP server itself, plus... | [Free to start](../gates/free.md) |
| [Anymail Finder](../tools/anymail-finder.md)
anymailfinder.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://api.anymailfinder.com/mcp](https://api.anymailfinder.com/mcp) +1 more | OAuth or an API key
Browser-based OAuth-style sign-in and approval for Claude, ChatGPT and Cursor, with an... | [Free to start](../gates/free.md) |
| [Apideck](../tools/apideck.md)
apideck.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp) +1 more | OAuth or an API key
Managed OAuth via Apideck Vault on the hosted endpoint, or x-apideck-api-key plus... | [Free to start](../gates/free.md) |
| [Apify](../tools/apify.md)
apify.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.apify.com](https://mcp.apify.com) +1 more | OAuth or an API key
oauth (recommended, browser sign-in) or an Apify API token as an Authorization Bearer... | [Free to start](../gates/free.md) |
| [Attio](../tools/attio.md)
attio.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.attio.com/mcp](https://mcp.attio.com/mcp) +1 more | OAuth
OAuth - one-time login as the user's own Attio account, no API key needed. Reads... | [Free to start](../gates/free.md) |
| [Autobound](../tools/autobound.md)
autobound.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://www.autobound.ai/integrations/mcp](https://www.autobound.ai/integrations/mcp) +1 more | API key
api key via an AUTOBOUND_API_KEY environment variable in the MCP client config. | [Free to start](../gates/free.md) |
| [Browserbase](../tools/browserbase.md)
browserbase.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.browserbase.com/mcp](https://mcp.browserbase.com/mcp) +1 more | API key
api key passed as a browserbaseApiKey query parameter on the endpoint URL; the docs list... | [Free to start](../gates/free.md) |
| [Buffer](../tools/buffer.md)
buffer.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://mcp.buffer.com/mcp](https://mcp.buffer.com/mcp) +1 more | API key
api key. The vendor's guide instructs the user to generate an API key from the developer... | [Free to start](../gates/free.md) |
| [Cal.com](../tools/cal-com.md)
cal.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp) +1 more | OAuth or an API key
Two paths. Hosted server (mcp.cal.com) uses OAuth 2.1 - "your client handles the... | [Free to start](../gates/free.md) |
| [Calendly](../tools/calendly.md)
calendly.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://mcp.calendly.com](https://mcp.calendly.com) +3 more | OAuth or an API key
OAuth 2.1 Authorization Code + PKCE (S256) with Dynamic Client Registration (RFC 7591).... | [Free to start](../gates/free.md) |
| [Cargo](../tools/cargo.md)
getcargo.ai | [RevOps Infra](../categories/revops-infra.md) | [https://docs.getcargo.ai/](https://docs.getcargo.ai/) | OAuth
unknown for the MCP layer specifically - docs confirm the capability but not its auth... | [Free to start](../gates/free.md) |
| [Census (now operates as "Fivetran Activations")](../tools/census.md)
getcensus.com | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) | API key
API key + secret via env vars (FIVETRAN_API_KEY, FIVETRAN_API_SECRET). | [Free to start](../gates/free.md) |
| [Common Paper](../tools/common-paper.md)
commonpaper.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://api.commonpaper.com/mcp](https://api.commonpaper.com/mcp) +2 more | Auth not recorded
unknown - not detailed in the release-notes excerpt reviewed. | [Free to start](../gates/free.md) |
| [Composio](../tools/composio.md)
composio.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://connect.composio.dev/mcp](https://connect.composio.dev/mcp) +2 more | OAuth or an API key
Composio brokers OAuth for each connected toolkit (HubSpot, Gmail, Slack, etc.) on the... | [Free to start](../gates/free.md) |
| [Crustdata](../tools/crustdata.md)
crustdata.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://install.crustdata.com/mcp](https://install.crustdata.com/mcp) +1 more | Auth not recorded
unknown | [Free to start](../gates/free.md) |
| [Crustdata](../tools/crustdata.md)
crustdata.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://install.crustdata.com/mcp](https://install.crustdata.com/mcp) +2 more | API key
api key (free sandbox key available) | [Free to start](../gates/free.md) |
| [Diffbot](../tools/diffbot.md)
diffbot.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp) | API key
api key (free Diffbot token required to use the MCP tools) | [Free to start](../gates/free.md) |
| [Enrow](../tools/enrow.md)
enrow.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/EnrowAPI/enrow-mcp](https://github.com/EnrowAPI/enrow-mcp) +1 more | API key
api key. ENROW_API_KEY env var for stdio, or an Authorization Bearer / x-enrow-api-key... | [Free to start](../gates/free.md) |
| [Exa](../tools/exa.md)
exa.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) +1 more | API key
api key (issued via dashboard.exa.ai) for the self-hosted server and for quota. CORRECTED... | [Free to start](../gates/free.md) |
| [Fathom](../tools/fathom.md)
fathom.video | [Conversation Intel](../categories/conversation-intel.md) | [https://developers.fathom.ai/mcp-docs](https://developers.fathom.ai/mcp-docs) +4 more | OAuth or an API key
In-client authorization: the docs say to add the server URL "then authenticate to access... | [Free to start](../gates/free.md) |
| [Firecrawl](../tools/firecrawl.md)
firecrawl.dev | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.firecrawl.dev/v2/mcp](https://mcp.firecrawl.dev/v2/mcp) +4 more | OAuth or an API key
api key as an Authorization Bearer header, or browser sign-in via the /v2/mcp-oauth... | [Free to start](../gates/free.md) |
| [Fireflies.ai](../tools/fireflies-ai.md)
fireflies.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://api.fireflies.ai/mcp](https://api.fireflies.ai/mcp) +1 more | OAuth or an API key
OAuth (Google/Microsoft, recommended) or manual API key for Claude Desktop and other MCP... | [Free to start](../gates/free.md) |
| [Fivetran](../tools/fivetran.md)
fivetran.com | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) | API key
API key + API secret via env vars, generated from the Fivetran dashboard. Scoped... | [Free to start](../gates/free.md) |
| [FullEnrich](../tools/fullenrich.md)
fullenrich.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.fullenrich.com/mcp](https://mcp.fullenrich.com/mcp) +1 more | OAuth
oauth (browser sign-in to FullEnrich account; no manual API key needed) | [Free to start](../gates/free.md) |
| [Google BigQuery](../tools/google-bigquery.md)
cloud.google.com | [RevOps Infra](../categories/revops-infra.md) | [https://bigquery.googleapis.com/mcp](https://bigquery.googleapis.com/mcp) +1 more | OAuth or an API key
oauth. The docs state the server uses the "OAuth 2.0 protocol with IAM for authentication... | [Free to start](../gates/free.md) |
| [Hightouch](../tools/hightouch.md)
hightouch.com | [RevOps Infra](../categories/revops-infra.md) | [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp) | Auth not recorded
Existing Hightouch workspace auth with role-based access control; however the MCP server... | [Free to start](../gates/free.md) |
| [HubSpot](../tools/hubspot.md)
hubspot.com | [RevOps Infra](../categories/revops-infra.md) | [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp) | OAuth
OAuth 2.0 for the hosted Remote MCP Server (migrating to OAuth 2.1 with PKCE +... | [Free to start](../gates/free.md) |
| [Hunter.io](../tools/hunter-io.md)
hunter.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://hunter.io/api-documentation#mcp](https://hunter.io/api-documentation#mcp) | API key
api key (HUNTER_API_KEY) | [Free to start](../gates/free.md) |
| [Jotform](../tools/jotform.md)
jotform.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://mcp.jotform.com](https://mcp.jotform.com) +2 more | OAuth or an API key
oauth only. The vendor's MCP page states "Bearer-token access is not supported; OAuth 2.0... | [Free to start](../gates/free.md) |
| [Knit MCP](../tools/knit-mcp.md)
getknit.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.getknit.dev/mcp-servers](https://www.getknit.dev/mcp-servers) +1 more | OAuth
Knit-managed OAuth or SAML per connected application; the customer authorises each end... | [Free to start](../gates/free.md) |
| [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md)
leadfeeder.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://www.leadfeeder.com/features/mcp-server/](https://www.leadfeeder.com/features/mcp-server/) +1 more | OAuth
OAuth - user signs in with their own Leadfeeder account; vendor states "No keys pasted... | [Free to start](../gates/free.md) |
| [LeadMagic](../tools/leadmagic.md)
leadmagic.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp) +1 more | OAuth or an API key
api key for local/self-hosted install (LEADMAGIC_API_KEY env var); OAuth Bearer token... | [Free to start](../gates/free.md) |
| [Lusha](../tools/lusha.md)
lusha.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/lusha-oss/lusha-public-api-mcp](https://github.com/lusha-oss/lusha-public-api-mcp) +2 more | API key
api key (LUSHA_API_KEY) | [Free to start](../gates/free.md) |
| [MeetGeek](../tools/meetgeek.md)
meetgeek.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.meetgeek.ai/mcp](https://mcp.meetgeek.ai/mcp) +2 more | OAuth or an API key
Two paths. The cloud server uses OAuth 2.0 with Google or Microsoft sign-in and no API... | [Free to start](../gates/free.md) |
| [Merge Agent Handler](../tools/merge-agent-handler.md)
merge.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/merge-api/merge-mcp](https://github.com/merge-api/merge-mcp) +3 more | OAuth or an API key
api key in an Authorization Bearer header, alongside the identity encoded in the URL... | [Free to start](../gates/free.md) |
| [Metricool](../tools/metricool.md)
metricool.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://ai.metricool.com/mcp](https://ai.metricool.com/mcp) +3 more | OAuth
oauth (browser authorisation in clients that support remote OAuth MCP) or a... | [Free to start](../gates/free.md) |
| [Model Context Protocol - official servers repo](../tools/model-context-protocol-official-servers-repo.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | API key
Per-server - individual servers take credentials (e.g. API tokens) via environment... | [Free to start](../gates/free.md) |
| [monday.com (monday CRM)](../tools/monday-com.md)
monday.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.monday.com/mcp](https://mcp.monday.com/mcp) +3 more | OAuth or an API key
oauth for the remote server. The vendor states "monday MCP remote server connects via the... | [Free to start](../gates/free.md) |
| [n8n](../tools/n8n.md)
n8n.io | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/n8n-io/n8n](https://github.com/n8n-io/n8n) +2 more | API key
MCP Server Trigger supports Bearer or Header auth to secure the exposed endpoint;... | [Free to start](../gates/free.md) |
| [PandaDoc](../tools/pandadoc.md)
pandadoc.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://mcp.pandadoc.com/v1/mcp](https://mcp.pandadoc.com/v1/mcp) +2 more | OAuth
OAuth - remote hosted server, add the server URL to an MCP client (Claude Desktop, Claude... | [Free to start](../gates/free.md) |
| [Pipedrive](../tools/pipedrive.md)
pipedrive.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.pipedrive.com/mcp](https://mcp.pipedrive.com/mcp) +1 more | OAuth
OAuth - "Connect in minutes through secure OAuth. No coding, no API development, no... | [Free to start](../gates/free.md) |
| [Pipeworx](../tools/pipeworx.md)
pipeworx.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://gateway.pipeworx.io/mcp](https://gateway.pipeworx.io/mcp) +4 more | Auth not recorded
none required for the free tiers. The vendor states "No API keys" and that an anonymous... | [Free to start](../gates/free.md) |
| [PredictLeads](../tools/predictleads.md)
predictleads.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://mcp.predictleads.com/](https://mcp.predictleads.com/) | API key
api key (same API key/token used for REST API calls, per vendor blog) | [Free to start](../gates/free.md) |
| [Prospeo](../tools/prospeo.md)
prospeo.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server) | OAuth or an API key
OAuth 2.0 for the hosted server (auto-handled by Claude.ai/Desktop via the MCP... | [Free to start](../gates/free.md) |
| [Relevance AI](../tools/relevance-ai.md)
relevanceai.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://mcp.relevanceai.com/](https://mcp.relevanceai.com/) +1 more | OAuth
OAuth (tokens may expire after inactivity; re-auth via login flow); Viewer/Chat project... | [Free to start](../gates/free.md) |
| [Retool](../tools/retool.md)
retool.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.retool.com/mcp](https://mcp.retool.com/mcp) +2 more | OAuth
OAuth 2.0. Endpoint pattern https:///mcp over HTTP. | [Free to start](../gates/free.md) |
| [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md)
snowflake.com | [RevOps Infra](../categories/revops-infra.md) | [https://docs.snowflake.com/en/user-guide/snowflake-c...](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) +1 more | OAuth
Snowflake OAuth 2.0 by default, or External OAuth (Okta, Microsoft Entra ID); hardcoded... | [Free to start](../gates/free.md) |
| [StackOne](../tools/stackone.md)
stackone.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://mcp.stackone.com/mcp](https://mcp.stackone.com/mcp) +2 more | OAuth or an API key
Basic authentication plus a per-account identifier, with StackOne brokering OAuth, API... | [Free to start](../gates/free.md) |
| [Tally](../tools/tally.md)
tally.so | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://api.tally.so/mcp](https://api.tally.so/mcp) +2 more | OAuth or an API key
oauth or api key. The help page states "The easiest way to connect is through OAuth, just... | [Free to start](../gates/free.md) |
| [Tavily](../tools/tavily.md)
tavily.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.tavily.com/mcp/](https://mcp.tavily.com/mcp/) +1 more | OAuth or an API key
api key as a tavilyApiKey query parameter or in the Authorization header, or OAuth. The... | [Free to start](../gates/free.md) |
| [Tavus](../tools/tavus.md)
tavus.io | [Video Prospecting](../categories/video-prospecting.md) | [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp) +3 more | OAuth or an API key
OAuth 2.0 browser-based flow; the exchange mints a per-user API key server-side, nothing... | [Free to start](../gates/free.md) |
| [TheirStack](../tools/theirstack.md)
theirstack.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://api.theirstack.com/mcp/](https://api.theirstack.com/mcp/) +3 more | API key
api key (same credentials as the REST API) | [Free to start](../gates/free.md) |
| [TheirStack](../tools/theirstack.md)
theirstack.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://api.theirstack.com/mcp/](https://api.theirstack.com/mcp/) +1 more | Auth not recorded
unknown - page references a "How does authentication work?" FAQ but the answer wasn't... | [Free to start](../gates/free.md) |
| [Tidio](../tools/tidio.md)
tidio.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://github.com/TidioPoland/tidio-mcp-connector](https://github.com/TidioPoland/tidio-mcp-connector) +1 more | OAuth
OAuth: the tidio_connect tool opens a browser to Tidio's login page, then stores access... | [Free to start](../gates/free.md) |
| [Trumpet (sendtrumpet.com)](../tools/trumpet.md)
sendtrumpet.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://www.sendtrumpet.com/blog-posts/introducing-t...](https://www.sendtrumpet.com/blog-posts/introducing-trumpet-mcp) | OAuth
unknown - vendor states it is "installable in five minutes with no engineering required,"... | [Free to start](../gates/free.md) |
| [usefulapi.io](../tools/usefulapi-io.md)
usefulapi.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://pipedrive.usefulapi.io/mcp](https://pipedrive.usefulapi.io/mcp) +3 more | OAuth or an API key
per-application OAuth. The setup instructions add the subdomain as a custom connector and... | [Free to start](../gates/free.md) |
| [Warmly](../tools/warmly.md)
warmly.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | OAuth or an API key
OAuth for the MCP connector; API key for the REST API | [Free to start](../gates/free.md) |
| [Warmly (Warmly.ai)](../tools/warmly.md)
warmly.ai | [Signals & Intent](../categories/signals-intent-abm.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | OAuth or an API key
MCP uses OAuth-based login (no manual key management); the separate REST API... | [Free to start](../gates/free.md) |
| [Wistia](../tools/wistia.md)
wistia.com | [Video Prospecting](../categories/video-prospecting.md) | [https://api.wistia.com/mcp/api](https://api.wistia.com/mcp/api) +1 more | OAuth or an API key
oauth or an access token as an Authorization Bearer header. The docs state "If you use an... | [Free to start](../gates/free.md) |
| [Zapier](../tools/zapier.md)
zapier.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect) +3 more | OAuth or an API key
Reuses Zapier's existing 13+ year credential infrastructure - connect an AI client... | [Free to start](../gates/free.md) |
| [Zapier MCP](../tools/zapier-mcp.md)
zapier.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect) +3 more | OAuth
Uses Zapier's existing decade-old app-connection/OAuth infrastructure - you authorize... | [Free to start](../gates/free.md) |
| [ZoomInfo](../tools/zoominfo.md)
zoominfo.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp) +2 more | OAuth
OAuth for user-level access, or client credentials for service accounts; no API keys... | [Free to start](../gates/free.md) |
| [Affinity](../tools/affinity.md)
affinity.co | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.affinity.co/mcp](https://mcp.affinity.co/mcp) +1 more | OAuth or an API key
OAuth where the client supports it, otherwise an API key. Local deployment is API key... | [Paid, self-serve](../gates/paid.md) |
| [Airspeed (formerly Glyphic)](../tools/airspeed.md)
goairspeed.com | [Conversation Intel](../categories/conversation-intel.md) | [https://api.glyphic.ai/mcp](https://api.glyphic.ai/mcp) +1 more | API key
Airspeed API key passed as an X-API-Key header. | [Paid, self-serve](../gates/paid.md) |
| [Allegrow](../tools/allegrow.md)
allegrow.co | [Email Deliverability](../categories/email-deliverability.md) | [https://mcp.allegrow.co/mcp](https://mcp.allegrow.co/mcp) +1 more | OAuth
OAuth - connects through Claude's standard connector authorization flow; user logs into... | [Paid, self-serve](../gates/paid.md) |
| [Amplemarket (Duo Copilot)](../tools/amplemarket.md)
amplemarket.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://mcp.amplemarket.com/mcp](https://mcp.amplemarket.com/mcp) +2 more | Auth not recorded
Account sign-in (no API key needed) - "sign in with your Amplemarket account when... | [Paid, self-serve](../gates/paid.md) |
| [Apollo.io](../tools/apollo-io.md)
apollo.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | OAuth
OAuth (Apollo.io sign-in/authorization flow in the client) | [Paid, self-serve](../gates/paid.md) |
| [Arphie](../tools/arphie.md)
arphie.ai | [Proposals & Deals](../categories/proposals-deals.md) | referenced via pricing/product pages describing an "Arphie... | Auth not recorded
unknown | [Paid, self-serve](../gates/paid.md) |
| [Attention](../tools/attention.md)
attention.com | [Conversation Intel](../categories/conversation-intel.md) | [https://docs.attention.com/mcp/overview](https://docs.attention.com/mcp/overview) +1 more | OAuth or an API key
oauth for end users, api key for programmatic access, per... | [Paid, self-serve](../gates/paid.md) |
| [Avoma](../tools/avoma.md)
avoma.com | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.avoma.com/mcp](https://mcp.avoma.com/mcp) +1 more | API key
API key pair (CLIENT_KEY:CLIENT_SECRET) generated at Settings → Organization → Developer. | [Paid, self-serve](../gates/paid.md) |
| [Brand24](../tools/brand24.md)
brand24.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://mcp.brand24.com/v1/mcp](https://mcp.brand24.com/v1/mcp) +1 more | OAuth
OAuth; the help article states "MCP access is available to Brand24 subscribers. The data... | [Paid, self-serve](../gates/paid.md) |
| [Bright Data](../tools/bright-data.md)
brightdata.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | API key
api key (Bright Data API token) | [Paid, self-serve](../gates/paid.md) |
| [CatchIntent](../tools/catchintent.md)
catchintent.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://engine.catchintent.com/mcp](https://engine.catchintent.com/mcp) +3 more | OAuth
oauth. The vendor's MCP page states "One-time OAuth 2.1 authorization. Your MCP client... | [Paid, self-serve](../gates/paid.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | OAuth or an API key
Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper... | [Paid, self-serve](../gates/paid.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | OAuth or an API key
Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper... | [Paid, self-serve](../gates/paid.md) |
| [Circleback](../tools/circleback.md)
circleback.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://circleback.ai/api/mcp](https://circleback.ai/api/mcp) +2 more | OAuth
OAuth with dynamic client registration, compliant with the authenticated remote MCP spec.... | [Paid, self-serve](../gates/paid.md) |
| [Clari Copilot](../tools/clari-copilot.md)
clari.com | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.clari.com/mcp](https://mcp.clari.com/mcp) +2 more | OAuth or an API key
Scalekit-hosted connector uses per-user delegated OAuth-style authorization in Scalekit's... | [Paid, self-serve](../gates/paid.md) |
| [Clay](../tools/clay.md)
clay.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.clay.com/mcp](https://www.clay.com/mcp) +1 more | API key
Session cookie - the same token used to log into app.clay.com in-browser, which grants... | [Paid, self-serve](../gates/paid.md) |
| [Close (Close CRM)](../tools/close.md)
close.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.close.com/mcp](https://mcp.close.com/mcp) +1 more | OAuth or an API key
Dual - OAuth 2.0 with Dynamic Client Registration (recommended; used by Claude, ChatGPT,... | [Paid, self-serve](../gates/paid.md) |
| [Coresignal](../tools/coresignal.md)
coresignal.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.coresignal.com/mcp/v2](https://mcp.coresignal.com/mcp/v2) +2 more | OAuth
OAuth 2.1 - per docs, the data key is fetched live with every request and never stored,... | [Paid, self-serve](../gates/paid.md) |
| [Cube Software](../tools/cube-software.md)
cubesoftware.com | [Forecasting & Revenue](../categories/forecasting-revenue.md) | [https://mcp.cubesoftware.com/](https://mcp.cubesoftware.com/) +2 more | OAuth
OAuth - no manual API key management. | [Paid, self-serve](../gates/paid.md) |
| [CUFinder](../tools/cufinder.md)
cufinder.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.cufinder.io/mcp](https://mcp.cufinder.io/mcp) +1 more | API key
api key from the CUFinder dashboard under Account Settings then API Dashboard. Streamable... | [Paid, self-serve](../gates/paid.md) |
| [dbt (dbt platform remote MCP)](../tools/dbt.md)
getdbt.com | [RevOps Infra](../categories/revops-infra.md) | [https://YOUR_DBT_HOST_URL/api/ai/v1/mcp](https://YOUR_DBT_HOST_URL/api/ai/v1/mcp) +3 more | OAuth or an API key
oauth (beta) or token. The docs state "OAuth lets you connect to the remote MCP server... | [Paid, self-serve](../gates/paid.md) |
| [Derrick](../tools/derrick.md)
derrick-app.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://app1.derrick-app.com/mcp](https://app1.derrick-app.com/mcp) +2 more | API key
api key. The vendor's page states the MCP installs without credentials but every tool... | [Paid, self-serve](../gates/paid.md) |
| [DocuSign](../tools/docusign.md)
docusign.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/) +2 more | OAuth
OAuth - Streamable HTTP transport; first connection opens a browser window to sign in and... | [Paid, self-serve](../gates/paid.md) |
| [Dropcontact](../tools/dropcontact.md)
dropcontact.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.dropcontact.com/mcp](https://mcp.dropcontact.com/mcp) +1 more | OAuth or an API key
Hosted server at mcp.dropcontact.com/mcp/, supporting OAuth (recommended, browser-based)... | [Paid, self-serve](../gates/paid.md) |
| [Explorium](../tools/explorium.md)
explorium.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp-github-registry.explorium.ai/mcp](https://mcp-github-registry.explorium.ai/mcp) +3 more | API key
api key | [Paid, self-serve](../gates/paid.md) |
| [Factors.ai](../tools/factors-ai.md)
factors.ai | [Signals & Intent](../categories/signals-intent-abm.md) | [https://mcp.factors.ai/mcp](https://mcp.factors.ai/mcp) +1 more | API key
Personal access token (generated in Settings > AI Features), used via Claude custom... | [Paid, self-serve](../gates/paid.md) |
| [Fellow](../tools/fellow.md)
fellow.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://fellow.app/mcp](https://fellow.app/mcp) +1 more | OAuth
OAuth, with OAuth 2.0 dynamic discovery supported. | [Paid, self-serve](../gates/paid.md) |
| [Fiber AI](../tools/fiber-ai.md)
fiber.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.fiber.ai/mcp/v3](https://mcp.fiber.ai/mcp/v3) +2 more | OAuth or an API key
OAuth via Clerk on the v3 endpoint; x-api-key header on the v2 and legacy endpoints. | [Paid, self-serve](../gates/paid.md) |
| [Front](../tools/front.md)
front.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://mcp.frontapp.com/mcp](https://mcp.frontapp.com/mcp) +1 more | OAuth
OAuth 2.1 with PKCE, per teammate. Front's docs state the server does not support Dynamic... | [Paid, self-serve](../gates/paid.md) |
| [Grain](../tools/grain.md)
grain.com | [Conversation Intel](../categories/conversation-intel.md) | [https://api.grain.com/_/mcp](https://api.grain.com/_/mcp) +2 more | OAuth
OAuth via the native Claude integration, or manual server-URL setup for other MCP... | [Paid, self-serve](../gates/paid.md) |
| [Granola](../tools/granola.md)
granola.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://www.pulsemcp.com/servers/granola](https://www.pulsemcp.com/servers/granola) +2 more | OAuth
OAuth - no manual API key required. | [Paid, self-serve](../gates/paid.md) |
| [Help Scout](../tools/help-scout.md)
helpscout.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://mcp.helpscout.net/mcp](https://mcp.helpscout.net/mcp) +1 more | OAuth
oauth. The vendor's article states the connector registers itself, so the OAuth client ID... | [Paid, self-serve](../gates/paid.md) |
| [Hex](../tools/hex.md)
hex.tech | [RevOps Infra](../categories/revops-infra.md) | [https://app.hex.tech/mcp](https://app.hex.tech/mcp) +1 more | OAuth
oauth. The docs state "Complete the OAuth flow to authorize access to your Hex... | [Paid, self-serve](../gates/paid.md) |
| [HeyGen](../tools/heygen.md)
heygen.com | [Video Prospecting](../categories/video-prospecting.md) | [https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/) +2 more | OAuth
OAuth - vendor states "connect your HeyGen account, no API key required"; generation... | [Paid, self-serve](../gates/paid.md) |
| [HeyReach](../tools/heyreach.md)
heyreach.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.heyreach.io/mcp](https://mcp.heyreach.io/mcp) +2 more | OAuth or an API key
workspace-scoped "MCP key" + connection URL (API-key-style, not OAuth) | [Paid, self-serve](../gates/paid.md) |
| [HighLevel (GoHighLevel)](../tools/highlevel.md)
gohighlevel.com | [RevOps Infra](../categories/revops-infra.md) | [https://services.leadconnectorhq.com/mcp/](https://services.leadconnectorhq.com/mcp/) +1 more | API key
A Private Integration Token passed as a bearer token, plus a locationId header. Tool... | [Paid, self-serve](../gates/paid.md) |
| [Hootsuite (Social OS)](../tools/hootsuite.md)
hootsuite.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://mcp.hootsuite.com/perch](https://mcp.hootsuite.com/perch) +4 more | OAuth
oauth. The vendor's setup steps end with "Sign in with your Hootsuite workspace when... | [Paid, self-serve](../gates/paid.md) |
| [Infraforge](../tools/infraforge.md)
infraforge.ai | [Email Deliverability](../categories/email-deliverability.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) | API key
API key, generated from the Infraforge/Salesforge dashboard. | [Paid, self-serve](../gates/paid.md) |
| [Instantly](../tools/instantly.md)
instantly.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.instantly.ai/mcp](https://mcp.instantly.ai/mcp) +1 more | API key
api key (generated in Instantly Settings > Integrations > API Keys) | [Paid, self-serve](../gates/paid.md) |
| [Intercom (Fin)](../tools/intercom.md)
intercom.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp) +2 more | OAuth or an API key
OAuth (browser-based, recommended) or a Bearer token using an Intercom API token;... | [Paid, self-serve](../gates/paid.md) |
| [JustCall](../tools/justcall.md)
justcall.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.justcall.host/mcp](https://mcp.justcall.host/mcp) +2 more | API key
api key. The vendor's docs show an Authorization header of the form "Bearer... | [Paid, self-serve](../gates/paid.md) |
| [Keyplay](../tools/keyplay.md)
keyplay.io | [Signals & Intent](../categories/signals-intent-abm.md) | [https://api.keyplay.io/mcp](https://api.keyplay.io/mcp) +1 more | OAuth or an API key
OAuth for Claude.ai and Claude Desktop, API key for Claude Code, per the vendor's docs | [Paid, self-serve](../gates/paid.md) |
| [Klenty](../tools/klenty.md)
klenty.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://api.klenty.com/mcp](https://api.klenty.com/mcp) +2 more | Third party platform auth
Rides Zapier's hosted-connector auth at mcp.zapier.com (and Runbear's for the Slack... | [Paid, self-serve](../gates/paid.md) |
| [La Growth Machine](../tools/la-growth-machine.md)
lagrowthmachine.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system) +1 more | OAuth
OAuth - no API key needed; first use opens a browser sign-in directly to the user's La... | [Paid, self-serve](../gates/paid.md) |
| [Lead411](../tools/lead411.md)
lead411.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.lead411.com/mcp](https://mcp.lead411.com/mcp) +3 more | API key
api key via X-API-KEY header. TRANSPORT IS DISPUTED: the official registry record says... | [Paid, self-serve](../gates/paid.md) |
| [LeadIQ](../tools/leadiq.md)
leadiq.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.leadiq.com/mcp](https://mcp.leadiq.com/mcp) +1 more | OAuth
oauth. The vendor's page states the connector is added from the AI client's connector... | [Paid, self-serve](../gates/paid.md) |
| [lemlist](../tools/lemlist.md)
lemlist.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://app.lemlist.com/mcp](https://app.lemlist.com/mcp) +1 more | OAuth or an API key
OAuth (browser-based PKCE flow, recommended) or API key via X-API-Key header | [Paid, self-serve](../gates/paid.md) |
| [Maildoso](../tools/maildoso.md)
maildoso.ai | [Email Deliverability](../categories/email-deliverability.md) | [https://maildoso.ai/](https://maildoso.ai/) | Auth not recorded
unknown - described only as "API and MCP access" bundled into every plan, without a... | [Paid, self-serve](../gates/paid.md) |
| [Mailforge](../tools/mailforge.md)
mailforge.ai | [Email Deliverability](../categories/email-deliverability.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) | API key
API key, generated from the Mailforge dashboard. | [Paid, self-serve](../gates/paid.md) |
| [Make](../tools/make.md)
make.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.make.com](https://mcp.make.com) +2 more | OAuth or an API key
Two supported methods - OAuth via Make's cloud (endpoint mcp.make.com) or an MCP Token... | [Paid, self-serve](../gates/paid.md) |
| [Metorial](../tools/metorial.md)
metorial.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/metorial/metorial](https://github.com/metorial/metorial) +1 more | OAuth or an API key
Fully custodial - Metorial stores and centrally manages OAuth tokens for every connected... | [Paid, self-serve](../gates/paid.md) |
| [Microsoft Dynamics 365 Sales](../tools/microsoft-dynamics-365-sales.md)
microsoft.com | [RevOps Infra](../categories/revops-infra.md) | [https://agent365.svc.cloud.microsoft/mcp/environment...](https://agent365.svc.cloud.microsoft/mcp/environments/) +1 more | Auth not recorded
enterprise gate. Microsoft Entra identity; the documented prerequisites are admin... | [Paid, self-serve](../gates/paid.md) |
| [Mixmax](../tools/mixmax.md)
mixmax.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.mixmax.com/mcp](https://mcp.mixmax.com/mcp) +2 more | OAuth
OAuth 2.0 authorization code flow, scoped to the connecting user's account. Read-only. | [Paid, self-serve](../gates/paid.md) |
| [Nutshell CRM](../tools/nutshell-crm.md)
nutshell.com | [RevOps Infra](../categories/revops-infra.md) | [https://app.nutshell.com/mcp](https://app.nutshell.com/mcp) +1 more | OAuth
oauth. The vendor's article instructs the user to add the server URL as a custom... | [Paid, self-serve](../gates/paid.md) |
| [Ocean.io](../tools/ocean-io.md)
ocean.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://app.ocean.io/docs/getting-started/mcp](https://app.ocean.io/docs/getting-started/mcp) +1 more | API key
api key (api-token passed as a URL parameter to the hosted MCP endpoint) | [Paid, self-serve](../gates/paid.md) |
| [Octave](../tools/octave.md)
octavehq.com | [RevOps Infra](../categories/revops-infra.md) | [https://docs.octavehq.com/mcp/overview](https://docs.octavehq.com/mcp/overview) +3 more | OAuth or an API key
Browser OAuth. Per the vendor's Claude Code setup doc you add the server with "claude mcp... | [Paid, self-serve](../gates/paid.md) |
| [Offorte](../tools/offorte.md)
offorte.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://github.com/offorte/offorte-mcp-server](https://github.com/offorte/offorte-mcp-server) +2 more | API key
api key. The repo README lists an "Offorte API Key (see Authentication Section of the... | [Paid, self-serve](../gates/paid.md) |
| [Ortto](../tools/ortto.md)
ortto.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp-api-us.ortto.app/mcp](https://mcp-api-us.ortto.app/mcp) +1 more | Auth not recorded
A scoped JWT key created as an MCP data source inside the Ortto account, passed as a... | [Paid, self-serve](../gates/paid.md) |
| [PhantomBuster](../tools/phantombuster.md)
phantombuster.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server) +1 more | OAuth
OAuth - first connection redirects to PhantomBuster sign-in/authorization, then workspace... | [Paid, self-serve](../gates/paid.md) |
| [Pipedream MCP](../tools/pipedream-mcp.md)
pipedream.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://mcp.pipedream.com](https://mcp.pipedream.com) | OAuth or an API key
OAuth/API-key credentials for each underlying app are stored by Pipedream and isolated... | [Paid, self-serve](../gates/paid.md) |
| [RB2B](../tools/rb2b.md)
rb2b.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://registry.npmjs.org/@rb2b/rb2b-apis-mcp](https://registry.npmjs.org/@rb2b/rb2b-apis-mcp) | API key
api key | [Paid, self-serve](../gates/paid.md) |
| [Reply.io](../tools/reply-io.md)
reply.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://reply.io/mcp/](https://reply.io/mcp/) +1 more | API key
api key (personal API key over HTTPS, included in free trial) | [Paid, self-serve](../gates/paid.md) |
| [Reply.io (Jason AI)](../tools/reply-io.md)
reply.io | [AI SDRs](../categories/ai-sdr-agents.md) | [https://reply.io/mcp/](https://reply.io/mcp/) +2 more | OAuth or an API key
Personal API key (vendor-recommended, sent as a Bearer token, scoped to the permissions... | [Paid, self-serve](../gates/paid.md) |
| [Responsive (formerly RFPIO)](../tools/responsive.md)
responsive.io | [Proposals & Deals](../categories/proposals-deals.md) | [https://www.responsive.io/capability/mcp-server](https://www.responsive.io/capability/mcp-server) +2 more | Auth not recorded
unknown - not detailed in the sources reviewed. | [Paid, self-serve](../gates/paid.md) |
| [RingCentral App Connect MCP](../tools/ringcentral-app-connect-mcp.md)
ringcentral.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://unified-crm-extension.labs.ringcentral.com/m...](https://unified-crm-extension.labs.ringcentral.com/mcp) +3 more | OAuth
oauth plus a second, separate CRM link. The docs describe a two-layer model: RingCentral... | [Paid, self-serve](../gates/paid.md) |
| [RocketReach](../tools/rocketreach.md)
rocketreach.co | [Data & Enrichment](../categories/data-enrichment.md) | [https://rocketreach.co/resources/products/mcp/](https://rocketreach.co/resources/products/mcp/) +1 more | OAuth
OAuth 2.1, browser-based; ties to your existing RocketReach account and shares its credit... | [Paid, self-serve](../gates/paid.md) |
| [Salesforge](../tools/salesforge.md)
salesforge.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp) | API key
api key via HTTP header (X-Salesforge-Key) | [Paid, self-serve](../gates/paid.md) |
| [Salesforge (Agent Frank)](../tools/salesforge.md)
salesforge.ai | [AI SDRs](../categories/ai-sdr-agents.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) +2 more | Auth not recorded
unknown specifics (help article confirms an official MCP server "to connect with AI... | [Paid, self-serve](../gates/paid.md) |
| [Saleshandy](../tools/saleshandy.md)
saleshandy.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.saleshandy.com/mcp](https://mcp.saleshandy.com/mcp) +3 more | OAuth or an API key
oauth, with an api key fallback. The developer docs state "Saleshandy MCP uses OAuth for... | [Paid, self-serve](../gates/paid.md) |
| [SalesQL](../tools/salesql.md)
salesql.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.salesql.com/mcp](https://mcp.salesql.com/mcp) +2 more | OAuth or an API key
oauth. The vendor's docs record "Auth OAuth 2.1" with an MCP key as the fallback for... | [Paid, self-serve](../gates/paid.md) |
| [Skyp.ai](../tools/skyp-ai.md)
skyp.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://api.skyp.ai/mcp](https://api.skyp.ai/mcp) +3 more | OAuth or an API key
api key (X-API-Key or Authorization Bearer header) or OAuth. The endpoint's own 401 body... | [Paid, self-serve](../gates/paid.md) |
| [Smartlead](../tools/smartlead.md)
smartlead.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://helpcenter.smartlead.ai/en/articles/300-smar...](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server) +3 more | API key
api key, passed as the user_api_key query parameter on the SSE endpoint URL; SSE... | [Paid, self-serve](../gates/paid.md) |
| [Snitcher](../tools/snitcher.md)
snitcher.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://app.snitcher.com/mcp/snitcher](https://app.snitcher.com/mcp/snitcher) +1 more | Auth not recorded
unknown - vendor changelog points to docs.snitcher.com for authentication specifics, not... | [Paid, self-serve](../gates/paid.md) |
| [Snov.io](../tools/snov-io.md)
snov.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.snov.io/mcp](https://mcp.snov.io/mcp) +1 more | OAuth
OAuth - user reviews and approves the connection through their Snov.io account; no raw... | [Paid, self-serve](../gates/paid.md) |
| [SparkToro](../tools/sparktoro.md)
sparktoro.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://sparktoro.com/mcp](https://sparktoro.com/mcp) +1 more | OAuth
OAuth (one-click sign-in with an existing SparkToro account); documented to work with... | [Paid, self-serve](../gates/paid.md) |
| [Sumble](../tools/sumble.md)
sumble.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://mcp.sumble.com/](https://mcp.sumble.com/) +3 more | Auth not recorded
unknown - the MCP overview page documents one-click install from the Claude and ChatGPT... | [Paid, self-serve](../gates/paid.md) |
| [Super Send](../tools/super-send.md)
supersend.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.supersend.io/mcp](https://mcp.supersend.io/mcp) +1 more | API key
api key, Streamable HTTP transport | [Paid, self-serve](../gates/paid.md) |
| [Superblocks](../tools/superblocks.md)
superblocks.com | [RevOps Infra](../categories/revops-infra.md) | [https://api.superblocks.com/mcp](https://api.superblocks.com/mcp) +1 more | OAuth
unknown - the announcement doesn't specify the auth method; the feature is... | [Paid, self-serve](../gates/paid.md) |
| [The Swarm](../tools/the-swarm.md)
theswarm.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://bee.theswarm.com/mcp](https://bee.theswarm.com/mcp) +1 more | OAuth or an API key
OAuth via personal Swarm login (native Claude and ChatGPT app connectors) or team API key... | [Paid, self-serve](../gates/paid.md) |
| [tl;dv](../tools/tl-dv.md)
tldv.io | [Conversation Intel](../categories/conversation-intel.md) | [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server) +1 more | API key
API key generated at Settings → Personal Settings → API keys. | [Paid, self-serve](../gates/paid.md) |
| [Trainual](../tools/trainual.md)
trainual.com | [Enablement & Coaching](../categories/enablement-coaching.md) | [https://help.trainual.com/en/the-trainual-mcp-server](https://help.trainual.com/en/the-trainual-mcp-server) +1 more | API key
Bearer MCP token in the Authorization header; the help article states "Only those with an... | [Paid, self-serve](../gates/paid.md) |
| [Typeform](../tools/typeform.md)
typeform.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://api.typeform.com/mcp](https://api.typeform.com/mcp) +2 more | OAuth
oauth. The docs state "Authorization is OAuth 2.0, and your client is prompted on first... | [Paid, self-serve](../gates/paid.md) |
| [Vainu](../tools/vainu.md)
vainu.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.vainu.ai/mcp](https://mcp.vainu.ai/mcp) +2 more | OAuth
OAuth 2.0 with PKCE, scoped to existing Vainu permissions, but NOT enabled by default.... | [Paid, self-serve](../gates/paid.md) |
| [Vayne](../tools/vayne.md)
vayne.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.vayne.io/mcp](https://mcp.vayne.io/mcp) +1 more | OAuth or an API key
oauth or api key. The vendor's docs state OAuth is the default for Claude Desktop,... | [Paid, self-serve](../gates/paid.md) |
| [Versium REACH](../tools/versium-reach.md)
versium.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://app.versium.com/mcp/reach](https://app.versium.com/mcp/reach) +2 more | OAuth
OAuth, and the client must support dynamic client registration. | [Paid, self-serve](../gates/paid.md) |
| [Waalaxy](../tools/waalaxy.md)
waalaxy.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://docs.waalaxy.com/mcp-server](https://docs.waalaxy.com/mcp-server) +1 more | OAuth or an API key
user-based OAuth 2.1 via magic-link sign-in; vendor docs explicitly state bearer API keys... | [Paid, self-serve](../gates/paid.md) |
| [Wiza](../tools/wiza.md)
wiza.co | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.wiza.co/mcp](https://mcp.wiza.co/mcp) +2 more | OAuth or an API key
OAuth 2.1 with PKCE for clients that support it, otherwise a static bearer token in the... | [Paid, self-serve](../gates/paid.md) |
| [Woodpecker](../tools/woodpecker.md)
woodpecker.co | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/Woodpeckerco/woodpecker-mcp-serve...](https://github.com/Woodpeckerco/woodpecker-mcp-server) +2 more | OAuth or an API key
hosted OAuth-style flow (Claude-specific) or self-hosted Docker setup using a Woodpecker... | [Paid, self-serve](../gates/paid.md) |
| [Zoho CRM](../tools/zoho-crm.md)
zoho.com | [RevOps Infra](../categories/revops-infra.md) | [https://www.zoho.com/crm/developer/mcp.html](https://www.zoho.com/crm/developer/mcp.html) | OAuth
oauth. The vendor's page describes a four-step setup ending in "Authenticate via OAuth.... | [Paid, self-serve](../gates/paid.md) |
| [Amplemarket](../tools/amplemarket.md)
amplemarket.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.amplemarket.com/mcp](https://mcp.amplemarket.com/mcp) +3 more | OAuth
OAuth 2.0 sign-in with the Amplemarket account in the browser; the knowledge article says... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Clari](../tools/clari.md)
clari.com | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.clari.com/mcp](https://mcp.clari.com/mcp) +1 more | Auth not recorded
unknown / not disclosed publicly | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Dialpad](../tools/dialpad.md)
dialpad.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp-public.us.karehq.com/mcp](https://mcp-public.us.karehq.com/mcp) +3 more | OAuth
oauth. The docs state the server is hosted by Dialpad, supports Dynamic Client... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Harmonic](../tools/harmonic.md)
harmonic.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.api.harmonic.ai](https://mcp.api.harmonic.ai) +1 more | OAuth or an API key
oauth. The server publishes OAuth protected-resource metadata at... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Paragon (ActionKit MCP)](../tools/paragon.md)
useparagon.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/useparagon/paragon-mcp](https://github.com/useparagon/paragon-mcp) +1 more | OAuth
Paragon user token plus Connect Portal OAuth. The distinguishing feature is that the... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [SigParser](../tools/sigparser.md)
sigparser.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://ipaas.sigparser.com/api/mcp](https://ipaas.sigparser.com/api/mcp) | API key
unknown. The endpoint answers HTTP 401 to an unauthenticated MCP initialize but no... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Sybill](../tools/sybill.md)
sybill.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.sybill.ai/mcp](https://mcp.sybill.ai/mcp) +1 more | OAuth
Browser-based sign-in / OAuth on first connection from an MCP client such as Claude... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [6sense](../tools/6sense.md)
6sense.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://6sense.com/platform/mcp-server/](https://6sense.com/platform/mcp-server/) +1 more | OAuth
OAuth using existing 6sense platform login (no separate API key setup per vendor docs) | [Enterprise only](../gates/enterprise-only.md) |
| [Ada](../tools/ada.md)
ada.cx | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server) +1 more | Auth not recorded
none documented - connects over HTTP with no credential requirement described in the docs. | [Enterprise only](../gates/enterprise-only.md) |
| [Anaplan (PlanIQ / Anaplan Forecaster)](../tools/anaplan.md)
anaplan.com | [Forecasting & Revenue](../categories/forecasting-revenue.md) | [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/) +1 more | OAuth or an API key
unknown - described only as a "governed MCP connection" with permission/audit controls;... | [Enterprise only](../gates/enterprise-only.md) |
| [Apollo.io Sequences (Emailer Campaigns)](../tools/apollo-io-sequences.md)
apollo.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) +1 more | OAuth
OAuth (Apollo.io sign-in/authorization flow; no API key required for this MCP) | [Enterprise only](../gates/enterprise-only.md) |
| [Artisan AI (Ava)](../tools/artisan-ai.md)
artisan.co | [AI SDRs](../categories/ai-sdr-agents.md) | [https://www.artisan.co/mcp](https://www.artisan.co/mcp) | Auth not recorded
none required - a JSON-RPC initialize POST to the endpoint with no credentials answered... | [Enterprise only](../gates/enterprise-only.md) |
| [Clari (+ Salesloft agents)](../tools/clari.md)
clari.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://mcp.clari.com/mcp](https://mcp.clari.com/mcp) +1 more | Auth not recorded
unknown - announcement confirms an official MCP server (works with Claude, ChatGPT,... | [Enterprise only](../gates/enterprise-only.md) |
| [Common Room](../tools/common-room.md)
commonroom.io | [Signals & Intent](../categories/signals-intent-abm.md) | [https://www.commonroom.io/docs/using-common-room/mcp...](https://www.commonroom.io/docs/using-common-room/mcp-server/) +1 more | OAuth
oauth (OAuth 2.1, browser-based, tokens scoped to the user's own Common Room permissions) | [Enterprise only](../gates/enterprise-only.md) |
| [Common Room](../tools/common-room.md)
commonroom.io | [Community & Dark Social](../categories/community-dark-social.md) | [https://www.commonroom.io/docs/using-common-room/mcp...](https://www.commonroom.io/docs/using-common-room/mcp-server/) +1 more | OAuth
oauth (OAuth 2.1, browser-based, tokens scoped to the user's own Common Room permissions) | [Enterprise only](../gates/enterprise-only.md) |
| [Crossbeam](../tools/crossbeam.md)
crossbeam.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://mcp.crossbeam.com/mcp](https://mcp.crossbeam.com/mcp) +1 more | OAuth
OAuth with Crossbeam login credentials, with a permission consent screen at connect time. | [Enterprise only](../gates/enterprise-only.md) |
| [Crunchbase](../tools/crunchbase.md)
crunchbase.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.crunchbase.com](https://mcp.crunchbase.com) +2 more | OAuth
OAuth 2.1. The user signs in with their normal Crunchbase account in the AI client's... | [Enterprise only](../gates/enterprise-only.md) |
| [Demandbase (Demandbase One)](../tools/demandbase.md)
demandbase.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://developer.demandbase.com/docs/mcp](https://developer.demandbase.com/docs/mcp) +1 more | Auth not recorded
unknown - the account-team-gated support article that likely covers this returned HTTP... | [Enterprise only](../gates/enterprise-only.md) |
| [G2 Buyer Intent](../tools/g2-buyer-intent.md)
g2.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://mcp.g2.com/mcp](https://mcp.g2.com/mcp) +2 more | OAuth
OAuth 2.0 Authorization Code with PKCE. You register an OAuth app in the G2 Developer... | [Enterprise only](../gates/enterprise-only.md) |
| [Gong](../tools/gong.md)
gong.io | [Conversation Intel](../categories/conversation-intel.md) | [https://help.gong.io/docs/about-gong-mcp](https://help.gong.io/docs/about-gong-mcp) +2 more | Auth not recorded
Official MCP client+server ships as part of Gong's enterprise agent stack (used to... | [Enterprise only](../gates/enterprise-only.md) |
| [HG Insights (Phoenix platform)](../tools/hg-insights.md)
hginsights.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://learn.microsoft.com/en-us/connectors/hginsig...](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/) | API key
api key (`x-api-key` header; throttled to 100 calls/60 seconds per connection) | [Enterprise only](../gates/enterprise-only.md) |
| [Highspot](../tools/highspot.md)
highspot.com | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.highspot.com/mcp](https://mcp.highspot.com/mcp) +1 more | Auth not recorded
unknown - product page describes agent-to-agent access via OpenAI, Anthropic, and... | [Enterprise only](../gates/enterprise-only.md) |
| [Ironclad](../tools/ironclad.md)
ironcladapp.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://support.ironcladapp.com/hc/en-us/articles/39...](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server) +1 more | Auth not recorded
unknown - a single, static MCP endpoint per the support article; specific credential... | [Enterprise only](../gates/enterprise-only.md) |
| [Looker](../tools/looker.md)
cloud.google.com | [RevOps Infra](../categories/revops-infra.md) | [https://docs.cloud.google.com/looker/docs/mcp](https://docs.cloud.google.com/looker/docs/mcp) +3 more | OAuth
The managed server uses OAuth 2.1 and an admin "must manually register AI agents as OAuth... | [Enterprise only](../gates/enterprise-only.md) |
| [MadKudu](../tools/madkudu.md)
madkudu.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://developers.madkudu.com/madkudu-mcp/install-i...](https://developers.madkudu.com/madkudu-mcp/install-in-ai-platforms-in-2min) +2 more | API key
MadKudu API key embedded in the endpoint path; the portal states "Please contact HG... | [Enterprise only](../gates/enterprise-only.md) |
| [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md)
turbomcp.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/dylibso/mcp.run-servlets](https://github.com/dylibso/mcp.run-servlets) +1 more | OAuth
Integrates with a team's own OIDC-compatible identity provider; handles OAuth and Dynamic... | [Enterprise only](../gates/enterprise-only.md) |
| [Meltwater](../tools/meltwater.md)
meltwater.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://developer.meltwater.com/guides/meltwater-mcp...](https://developer.meltwater.com/guides/meltwater-mcp/overview/) +1 more | OAuth or an API key
Meltwater API token today, "with OAuth 2.0 planned for later this year" per the vendor... | [Enterprise only](../gates/enterprise-only.md) |
| [Nooks](../tools/nooks.md)
nooks.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.nooks.in/mcp](https://mcp.nooks.in/mcp) +1 more | OAuth
OAuth 2.0 authorization code with PKCE (S256), issuer https://oauth.nooks.in, per the... | [Enterprise only](../gates/enterprise-only.md) |
| [Otter.ai](../tools/otter-ai.md)
otter.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.otter.ai/mcp](https://mcp.otter.ai/mcp) +3 more | Auth not recorded
unknown - exact auth mechanism not confirmed in public sources; framed under "Otter for... | [Enterprise only](../gates/enterprise-only.md) |
| [Outreach](../tools/outreach.md)
outreach.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://api.outreach.io/mcp/](https://api.outreach.io/mcp/) +1 more | OAuth
OAuth 2.1 with Dynamic Client Registration; also requires the org-level "Amplify" add-on... | [Enterprise only](../gates/enterprise-only.md) |
| [Pigment](../tools/pigment.md)
pigment.com | [Forecasting & Revenue](../categories/forecasting-revenue.md) | [https://www.pigment.com/ai/mcp-server](https://www.pigment.com/ai/mcp-server) +2 more | Auth not recorded
A workspace admin enables MCP under Settings > Integrations, generating a per-workspace... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)
salesforce.com | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) +2 more | OAuth
OAuth + PKCE via an External Client App (scopes mcp_api, refresh_token); every MCP call... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesloft](../tools/salesloft.md)
salesloft.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.salesloft.com/mcp](https://mcp.salesloft.com/mcp) +2 more | OAuth
unknown exact flow - vendor press material describes it as natively listed in Claude's... | [Enterprise only](../gates/enterprise-only.md) |
| [Seamless.AI](../tools/seamless-ai.md)
seamless.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.seamless.ai/mcp](https://mcp.seamless.ai/mcp) +1 more | OAuth or an API key
OAuth 2.1 or API key; docs state "MCP access must be enabled on your account" - i.e.... | [Enterprise only](../gates/enterprise-only.md) |
| [Seismic](../tools/seismic.md)
seismic.com | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.seismic.com/](https://mcp.seismic.com/) +1 more | OAuth or an API key
Streamable HTTP transport per Seismic's MCP documentation; the specific credential type... | [Enterprise only](../gates/enterprise-only.md) |
| [Showpad](../tools/showpad.md)
showpad.com | [Enablement & Coaching](../categories/enablement-coaching.md) | [https://mcp.showpad.com/mcp/v1](https://mcp.showpad.com/mcp/v1) +2 more | OAuth
OAuth; the docs say each end user authenticates with their own Showpad credentials and... | [Enterprise only](../gates/enterprise-only.md) |
| [Similarweb](../tools/similarweb.md)
similarweb.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://mcp.similarweb.com](https://mcp.similarweb.com) +3 more | OAuth or an API key
CONFLICTING VENDOR STATEMENTS, flagged rather than resolved. Both Similarweb developer... | [Enterprise only](../gates/enterprise-only.md) |
| [Surfe](../tools/surfe.md)
surfe.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.eu.surfe.com/mcp](https://mcp.eu.surfe.com/mcp) +1 more | API key
Surfe API key, with a browser sign-in flow that exchanges the key for a managed token so... | [Enterprise only](../gates/enterprise-only.md) |
| [Syncari](../tools/syncari.md)
syncari.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp.syncari.com/mcp](https://mcp.syncari.com/mcp) +1 more | OAuth or an API key
unknown - the MCP server page describes real-time, entity/field-level access control and... | [Enterprise only](../gates/enterprise-only.md) |
| [Talkwalker (rebranded: Lumen by Talkwalker)](../tools/talkwalker.md)
talkwalker.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://mcp.hootsuite.com/lumen](https://mcp.hootsuite.com/lumen) +1 more | Auth not recorded
Sign in with a Hootsuite workspace when prompted; the Hootsuite MCP page says... | [Enterprise only](../gates/enterprise-only.md) |
| [UserGems](../tools/usergems.md)
usergems.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://www.usergems.com/product/mcp](https://www.usergems.com/product/mcp) | OAuth or an API key
unknown - connects inside Claude/ChatGPT per the product page, but the exact auth... | [Enterprise only](../gates/enterprise-only.md) |
| [Actively](../tools/actively.md)
actively.ai | [Signals & Intent](../categories/signals-intent-abm.md) | [https://app.actively.ai/docs/mcp](https://app.actively.ai/docs/mcp) +2 more | OAuth
oauth. The vendor docs state "MCP access uses OAuth 2.1 with WorkOS." Tools are... | [Gate unknown](../gates/unknown.md) |
| [Endgame](../tools/endgame.md)
endgame.io | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://app.endgame.io/api/v1/mcp](https://app.endgame.io/api/v1/mcp) +1 more | OAuth or an API key
OAuth (browser-based) for individual users via Claude/ChatGPT/Claude Code/Codex... | [Gate unknown](../gates/unknown.md) |
| [Klavis AI](../tools/klavis-ai.md)
klavis.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.klavis.ai/docs/concepts/strata.md](https://www.klavis.ai/docs/concepts/strata.md) +2 more | OAuth or an API key
Klavis API key as an HTTP Bearer token on the management API that creates a per-user... | [Gate unknown](../gates/unknown.md) |
| [Pylon](../tools/pylon.md)
usepylon.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://mcp.usepylon.com](https://mcp.usepylon.com) +1 more | OAuth
OAuth 2.0 over stateless streamable HTTP; access is permission-scoped so a connected AI... | [Gate unknown](../gates/unknown.md) |
| [Reclaim.ai](../tools/reclaim-ai.md)
reclaim.ai | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://mcp.reclaim.ai](https://mcp.reclaim.ai) | OAuth or an API key
OAuth (official hosted server). A separate unofficial/community server also exists... | [Gate unknown](../gates/unknown.md) |
| [RevenueHero](../tools/revenuehero.md)
revenuehero.io | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://www.revenuehero.io/resources/tales-of-ops](https://www.revenuehero.io/resources/tales-of-ops) | API key
Per-customer router token over an SSE endpoint, manually provisioned by RevenueHero - not... | [Gate unknown](../gates/unknown.md) |
| [Trumpet](../tools/trumpet.md)
sendtrumpet.com | [Video Prospecting](../categories/video-prospecting.md) | [https://trumpet.app/api/mcp](https://trumpet.app/api/mcp) +2 more | OAuth
OAuth 2.0 - vendor help-center doc confirms "Authenticate via trumpet (OAuth 2.0)"; setup... | [Gate unknown](../gates/unknown.md) |
| [Zoom Revenue Accelerator](../tools/zoom-revenue-accelerator.md)
zoom.com | [Conversation Intel](../categories/conversation-intel.md) | [https://news.zoom.com/zoom-revenue-accelerator-mcp-c...](https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/) +1 more | OAuth or an API key
OAuth - Zoom user-level OAuth access token (env var... | [Gate unknown](../gates/unknown.md) |

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 468 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
