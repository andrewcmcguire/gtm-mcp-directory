# Official MCP servers list: 144 GTM tools, with links

> The full list of 144 go to market tools whose vendor ships and maintains its own MCP server, with the server URL, the auth model and the access gate for each. Counted 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / The 144 GTM tools with an official MCP server

**List · 144 of 293**

## The 144 GTM tools with an official MCP server

Official means first party. The vendor ships and maintains the server itself, and a wrapper built by Zapier, viaSocket, Composio or any other third party does not count no matter how well it works. 143 of these 144 entries carry a parseable URL in the mcp_url field; the rest claim a server in prose without one, which is recorded as a risk on the [methodology page](../methodology.md) rather than cleaned up quietly.

| Tool | Category | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Airbyte](../tools/airbyte.md)
airbyte.com | [RevOps Infra](../categories/revops-infra.md) | [https://docs.airbyte.com/ai-agents/interfaces/mcp](https://docs.airbyte.com/ai-agents/interfaces/mcp) | OAuth or an API key
Two-layer OAuth 2.0 - OAuth into the Airbyte account/org for the MCP server itself, plus... | [Free to start](../gates/free.md) |
| [Anymail Finder](../tools/anymail-finder.md)
anymailfinder.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://api.anymailfinder.com/mcp](https://api.anymailfinder.com/mcp) +1 more | OAuth or an API key
Browser-based OAuth-style sign-in and approval for Claude, ChatGPT and Cursor, with an... | [Free to start](../gates/free.md) |
| [Apideck](../tools/apideck.md)
apideck.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp) +1 more | OAuth or an API key
Managed OAuth via Apideck Vault on the hosted endpoint, or x-apideck-api-key plus... | [Free to start](../gates/free.md) |
| [Attio](../tools/attio.md)
attio.com | [RevOps Infra](../categories/revops-infra.md) | [https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview) +1 more | OAuth
OAuth - one-time login as the user's own Attio account, no API key needed. Reads... | [Free to start](../gates/free.md) |
| [Autobound](../tools/autobound.md)
autobound.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://www.autobound.ai/integrations/mcp](https://www.autobound.ai/integrations/mcp) +1 more | API key
api key via an AUTOBOUND_API_KEY environment variable in the MCP client config. | [Free to start](../gates/free.md) |
| [Cal.com](../tools/cal-com.md)
cal.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp) +1 more | OAuth or an API key
Two paths. Hosted server (mcp.cal.com) uses OAuth 2.1 - "your client handles the... | [Free to start](../gates/free.md) |
| [Calendly](../tools/calendly.md)
calendly.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://developer.calendly.com/calendly-mcp-server](https://developer.calendly.com/calendly-mcp-server) +3 more | OAuth or an API key
OAuth 2.1 Authorization Code + PKCE (S256) with Dynamic Client Registration (RFC 7591).... | [Free to start](../gates/free.md) |
| [Cargo](../tools/cargo.md)
getcargo.ai | [RevOps Infra](../categories/revops-infra.md) | [https://docs.getcargo.ai/](https://docs.getcargo.ai/) | OAuth
unknown for the MCP layer specifically - docs confirm the capability but not its auth... | [Free to start](../gates/free.md) |
| [Census (now operates as "Fivetran Activations")](../tools/census.md)
getcensus.com | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) | API key
API key + secret via env vars (FIVETRAN_API_KEY, FIVETRAN_API_SECRET). | [Free to start](../gates/free.md) |
| [Common Paper](../tools/common-paper.md)
commonpaper.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://commonpaper.com/release-notes/common-paper-m...](https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/) +1 more | Auth not recorded
unknown - not detailed in the release-notes excerpt reviewed. | [Free to start](../gates/free.md) |
| [Composio](../tools/composio.md)
composio.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://docs.composio.dev/mcp/overview](https://docs.composio.dev/mcp/overview) | OAuth or an API key
Composio brokers OAuth for each connected toolkit (HubSpot, Gmail, Slack, etc.) on the... | [Free to start](../gates/free.md) |
| [Diffbot](../tools/diffbot.md)
diffbot.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/diffbot/diffbot-mcp](https://github.com/diffbot/diffbot-mcp) | API key
api key (free Diffbot token required to use the MCP tools) | [Free to start](../gates/free.md) |
| [Enrow](../tools/enrow.md)
enrow.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/EnrowAPI/enrow-mcp](https://github.com/EnrowAPI/enrow-mcp) +1 more | API key
api key. ENROW_API_KEY env var for stdio, or an Authorization Bearer / x-enrow-api-key... | [Free to start](../gates/free.md) |
| [Exa](../tools/exa.md)
exa.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) +1 more | API key
api key (issued via dashboard.exa.ai) | [Free to start](../gates/free.md) |
| [Fireflies.ai](../tools/fireflies-ai.md)
fireflies.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://guide.fireflies.ai/articles/8272956938-learn...](https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol) +1 more | OAuth or an API key
OAuth (Google/Microsoft, recommended) or manual API key for Claude Desktop and other MCP... | [Free to start](../gates/free.md) |
| [Fivetran](../tools/fivetran.md)
fivetran.com | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/fivetran/fivetran-mcp](https://github.com/fivetran/fivetran-mcp) | API key
API key + API secret via env vars, generated from the Fivetran dashboard. Scoped... | [Free to start](../gates/free.md) |
| [FullEnrich](../tools/fullenrich.md)
fullenrich.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.fullenrich.com/mcp](https://mcp.fullenrich.com/mcp) +1 more | OAuth
oauth (browser sign-in to FullEnrich account; no manual API key needed) | [Free to start](../gates/free.md) |
| [Hightouch](../tools/hightouch.md)
hightouch.com | [RevOps Infra](../categories/revops-infra.md) | [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp) | Auth not recorded
Existing Hightouch workspace auth with role-based access control; however the MCP server... | [Free to start](../gates/free.md) |
| [HubSpot](../tools/hubspot.md)
hubspot.com | [RevOps Infra](../categories/revops-infra.md) | [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp) | OAuth
OAuth 2.0 for the hosted Remote MCP Server (migrating to OAuth 2.1 with PKCE +... | [Free to start](../gates/free.md) |
| [Hunter.io](../tools/hunter-io.md)
hunter.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://hunter.io/api-documentation#mcp](https://hunter.io/api-documentation#mcp) | API key
api key (HUNTER_API_KEY) | [Free to start](../gates/free.md) |
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
| [Model Context Protocol - official servers repo](../tools/model-context-protocol-official-servers-repo.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | API key
Per-server - individual servers take credentials (e.g. API tokens) via environment... | [Free to start](../gates/free.md) |
| [n8n](../tools/n8n.md)
n8n.io | [RevOps Infra](../categories/revops-infra.md) | [https://docs.n8n.io/integrations/builtin/core-nodes/...](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger) +1 more | API key
MCP Server Trigger supports Bearer or Header auth to secure the exposed endpoint;... | [Free to start](../gates/free.md) |
| [PandaDoc](../tools/pandadoc.md)
pandadoc.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://developers.pandadoc.com/docs/how-to-use-the-...](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server) +1 more | OAuth
OAuth - remote hosted server, add the server URL to an MCP client (Claude Desktop,... | [Free to start](../gates/free.md) |
| [Pipedrive](../tools/pipedrive.md)
pipedrive.com | [RevOps Infra](../categories/revops-infra.md) | [https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server) | OAuth
OAuth - "Connect in minutes through secure OAuth. No coding, no API development, no... | [Free to start](../gates/free.md) |
| [PredictLeads](../tools/predictleads.md)
predictleads.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://mcp.predictleads.com/](https://mcp.predictleads.com/) | API key
api key (same API key/token used for REST API calls, per vendor blog) | [Free to start](../gates/free.md) |
| [Prospeo](../tools/prospeo.md)
prospeo.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server) | OAuth or an API key
OAuth 2.0 for the hosted server (auto-handled by Claude.ai/Desktop via the MCP... | [Free to start](../gates/free.md) |
| [Relevance AI](../tools/relevance-ai.md)
relevanceai.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://relevanceai.com/docs/integrations/mcp/progra...](https://relevanceai.com/docs/integrations/mcp/programmatic-gtm/introduction) | OAuth
OAuth (tokens may expire after inactivity; re-auth via login flow); Viewer/Chat project... | [Free to start](../gates/free.md) |
| [Retool](../tools/retool.md)
retool.com | [RevOps Infra](../categories/revops-infra.md) | [https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server) | OAuth
OAuth 2.0. Endpoint pattern https:///mcp over HTTP. | [Free to start](../gates/free.md) |
| [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md)
snowflake.com | [RevOps Infra](../categories/revops-infra.md) | [https://docs.snowflake.com/en/user-guide/snowflake-c...](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) | OAuth
Snowflake OAuth 2.0 by default, or External OAuth (Okta, Microsoft Entra ID); hardcoded... | [Free to start](../gates/free.md) |
| [Tavus](../tools/tavus.md)
tavus.io | [Video Prospecting](../categories/video-prospecting.md) | [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp) +3 more | OAuth or an API key
OAuth 2.0 browser-based flow; the exchange mints a per-user API key server-side, nothing... | [Free to start](../gates/free.md) |
| [TheirStack](../tools/theirstack.md)
theirstack.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://theirstack.com/en/docs/mcp](https://theirstack.com/en/docs/mcp) +2 more | API key
api key (same credentials as the REST API) | [Free to start](../gates/free.md) |
| [TheirStack](../tools/theirstack.md)
theirstack.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp) | Auth not recorded
unknown - page references a "How does authentication work?" FAQ but the answer wasn't... | [Free to start](../gates/free.md) |
| [Trumpet (sendtrumpet.com)](../tools/trumpet.md)
sendtrumpet.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://www.sendtrumpet.com/blog-posts/introducing-t...](https://www.sendtrumpet.com/blog-posts/introducing-trumpet-mcp) | OAuth
unknown - vendor states it is "installable in five minutes with no engineering... | [Free to start](../gates/free.md) |
| [Warmly](../tools/warmly.md)
warmly.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | OAuth or an API key
OAuth for the MCP connector; API key for the REST API | [Free to start](../gates/free.md) |
| [Warmly (Warmly.ai)](../tools/warmly.md)
warmly.ai | [Signals & Intent](../categories/signals-intent-abm.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | OAuth or an API key
MCP uses OAuth-based login (no manual key management); the separate REST API... | [Free to start](../gates/free.md) |
| [Zapier](../tools/zapier.md)
zapier.com | [RevOps Infra](../categories/revops-infra.md) | [https://zapier.com/mcp](https://zapier.com/mcp) +1 more | OAuth or an API key
Reuses Zapier's existing 13+ year credential infrastructure - connect an AI client... | [Free to start](../gates/free.md) |
| [Zapier MCP](../tools/zapier-mcp.md)
zapier.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://mcp.zapier.com](https://mcp.zapier.com) | OAuth
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
allegrow.co | [Email Deliverability](../categories/email-deliverability.md) | [https://www.allegrow.co/knowledge-base/claude-email-...](https://www.allegrow.co/knowledge-base/claude-email-mcp) | OAuth
OAuth - connects through Claude's standard connector authorization flow; user logs into... | [Paid, self-serve](../gates/paid.md) |
| [Amplemarket (Duo Copilot)](../tools/amplemarket.md)
amplemarket.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://knowledge.amplemarket.com/articles/802268531...](https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server) | Auth not recorded
Account sign-in (no API key needed) - "sign in with your Amplemarket account when... | [Paid, self-serve](../gates/paid.md) |
| [Apollo.io](../tools/apollo-io.md)
apollo.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | OAuth
OAuth (Apollo.io sign-in/authorization flow in the client) | [Paid, self-serve](../gates/paid.md) |
| [Arphie](../tools/arphie.md)
arphie.ai | [Proposals & Deals](../categories/proposals-deals.md) | referenced via pricing/product pages describing an "Arphie... | Auth not recorded
unknown | [Paid, self-serve](../gates/paid.md) |
| [Attention](../tools/attention.md)
attention.com | [Conversation Intel](../categories/conversation-intel.md) | [https://docs.attention.com/attention-mcp-server](https://docs.attention.com/attention-mcp-server) +1 more | Auth not recorded
unknown - not confirmed in the sources reviewed. | [Paid, self-serve](../gates/paid.md) |
| [Avoma](../tools/avoma.md)
avoma.com | [Conversation Intel](../categories/conversation-intel.md) | [https://help.avoma.com/avoma-mcp-server-user-guide](https://help.avoma.com/avoma-mcp-server-user-guide) | API key
API key pair (CLIENT_KEY:CLIENT_SECRET) generated at Settings → Organization → Developer. | [Paid, self-serve](../gates/paid.md) |
| [Bright Data](../tools/bright-data.md)
brightdata.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) | API key
api key (Bright Data API token) | [Paid, self-serve](../gates/paid.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | OAuth or an API key
Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper... | [Paid, self-serve](../gates/paid.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | OAuth or an API key
Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper... | [Paid, self-serve](../gates/paid.md) |
| [Circleback](../tools/circleback.md)
circleback.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://circleback.ai/api/mcp](https://circleback.ai/api/mcp) +2 more | OAuth
OAuth with dynamic client registration, compliant with the authenticated remote MCP spec.... | [Paid, self-serve](../gates/paid.md) |
| [Clay](../tools/clay.md)
clay.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.clay.com/mcp](https://www.clay.com/mcp) +1 more | API key
Session cookie - the same token used to log into app.clay.com in-browser, which grants... | [Paid, self-serve](../gates/paid.md) |
| [Close (Close CRM)](../tools/close.md)
close.com | [RevOps Infra](../categories/revops-infra.md) | [https://help.close.com/docs/mcp-server](https://help.close.com/docs/mcp-server) +1 more | OAuth or an API key
Dual - OAuth 2.0 with Dynamic Client Registration (recommended; used by Claude, ChatGPT,... | [Paid, self-serve](../gates/paid.md) |
| [Coresignal](../tools/coresignal.md)
coresignal.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://coresignal.com/mcp-server/](https://coresignal.com/mcp-server/) | OAuth
OAuth 2.1 - per docs, the data key is fetched live with every request and never stored,... | [Paid, self-serve](../gates/paid.md) |
| [Crustdata](../tools/crustdata.md)
crustdata.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://docs.crustdata.com/for-agents/mcp.md](https://docs.crustdata.com/for-agents/mcp.md) +1 more | API key
api key (free sandbox key available) | [Paid, self-serve](../gates/paid.md) |
| [Cube Software](../tools/cube-software.md)
cubesoftware.com | [Forecasting & Revenue](../categories/forecasting-revenue.md) | [https://www.cubesoftware.com/mcp](https://www.cubesoftware.com/mcp) +1 more | OAuth
OAuth - no manual API key management. | [Paid, self-serve](../gates/paid.md) |
| [CUFinder](../tools/cufinder.md)
cufinder.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.cufinder.io/mcp](https://mcp.cufinder.io/mcp) +1 more | API key
api key from the CUFinder dashboard under Account Settings then API Dashboard. Streamable... | [Paid, self-serve](../gates/paid.md) |
| [DocuSign](../tools/docusign.md)
docusign.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/) +2 more | OAuth
OAuth - Streamable HTTP transport; first connection opens a browser window to sign in... | [Paid, self-serve](../gates/paid.md) |
| [Dropcontact](../tools/dropcontact.md)
dropcontact.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.dropcontact.com/mcp-dropcontact](https://www.dropcontact.com/mcp-dropcontact) | OAuth or an API key
Hosted server at mcp.dropcontact.com/mcp/, supporting OAuth (recommended, browser-based)... | [Paid, self-serve](../gates/paid.md) |
| [Factors.ai](../tools/factors-ai.md)
factors.ai | [Signals & Intent](../categories/signals-intent-abm.md) | [https://help.factors.ai/en/articles/14705206-factors...](https://help.factors.ai/en/articles/14705206-factors-mcp) | API key
Personal access token (generated in Settings > AI Features), used via Claude custom... | [Paid, self-serve](../gates/paid.md) |
| [Fiber AI](../tools/fiber-ai.md)
fiber.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.fiber.ai/mcp/v3](https://mcp.fiber.ai/mcp/v3) +2 more | OAuth or an API key
OAuth via Clerk on the v3 endpoint; x-api-key header on the v2 and legacy endpoints. | [Paid, self-serve](../gates/paid.md) |
| [Grain](../tools/grain.md)
grain.com | [Conversation Intel](../categories/conversation-intel.md) | [https://developers.grain.com/mcp](https://developers.grain.com/mcp) +1 more | OAuth
OAuth via the native Claude integration, or manual server-URL setup for other MCP... | [Paid, self-serve](../gates/paid.md) |
| [HeyGen](../tools/heygen.md)
heygen.com | [Video Prospecting](../categories/video-prospecting.md) | [https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/) +2 more | OAuth
OAuth - vendor states "connect your HeyGen account, no API key required"; generation... | [Paid, self-serve](../gates/paid.md) |
| [HeyReach](../tools/heyreach.md)
heyreach.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://www.heyreach.io/mcp](https://www.heyreach.io/mcp) +1 more | OAuth or an API key
workspace-scoped "MCP key" + connection URL (API-key-style, not OAuth) | [Paid, self-serve](../gates/paid.md) |
| [HighLevel (GoHighLevel)](../tools/highlevel.md)
gohighlevel.com | [RevOps Infra](../categories/revops-infra.md) | [https://services.leadconnectorhq.com/mcp/](https://services.leadconnectorhq.com/mcp/) +1 more | API key
A Private Integration Token passed as a bearer token, plus a locationId header. Tool... | [Paid, self-serve](../gates/paid.md) |
| [Infraforge](../tools/infraforge.md)
infraforge.ai | [Email Deliverability](../categories/email-deliverability.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) | API key
API key, generated from the Infraforge/Salesforge dashboard. | [Paid, self-serve](../gates/paid.md) |
| [Instantly](../tools/instantly.md)
instantly.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.instantly.ai/mcp](https://mcp.instantly.ai/mcp) +1 more | API key
api key (generated in Instantly Settings > Integrations > API Keys) | [Paid, self-serve](../gates/paid.md) |
| [Intercom (Fin)](../tools/intercom.md)
intercom.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp) +2 more | OAuth or an API key
OAuth (browser-based, recommended) or a Bearer token using an Intercom API token;... | [Paid, self-serve](../gates/paid.md) |
| [La Growth Machine](../tools/la-growth-machine.md)
lagrowthmachine.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system) +1 more | OAuth
OAuth - no API key needed; first use opens a browser sign-in directly to the user's La... | [Paid, self-serve](../gates/paid.md) |
| [Lead411](../tools/lead411.md)
lead411.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.lead411.com/mcp](https://mcp.lead411.com/mcp) +3 more | API key
api key via X-API-KEY header. TRANSPORT IS DISPUTED: the official registry record says... | [Paid, self-serve](../gates/paid.md) |
| [lemlist](../tools/lemlist.md)
lemlist.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://developer.lemlist.com/mcp/setup](https://developer.lemlist.com/mcp/setup) +1 more | OAuth or an API key
OAuth (browser-based PKCE flow, recommended) or API key via X-API-Key header | [Paid, self-serve](../gates/paid.md) |
| [Maildoso](../tools/maildoso.md)
maildoso.ai | [Email Deliverability](../categories/email-deliverability.md) | [https://maildoso.ai/](https://maildoso.ai/) | Auth not recorded
unknown - described only as "API and MCP access" bundled into every plan, without a... | [Paid, self-serve](../gates/paid.md) |
| [Mailforge](../tools/mailforge.md)
mailforge.ai | [Email Deliverability](../categories/email-deliverability.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) | API key
API key, generated from the Mailforge dashboard. | [Paid, self-serve](../gates/paid.md) |
| [Make](../tools/make.md)
make.com | [RevOps Infra](../categories/revops-infra.md) | [https://developers.make.com/mcp-server](https://developers.make.com/mcp-server) | OAuth or an API key
Two supported methods - OAuth via Make's cloud (endpoint mcp.make.com) or an MCP Token... | [Paid, self-serve](../gates/paid.md) |
| [Metorial](../tools/metorial.md)
metorial.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://metorial.com](https://metorial.com) | OAuth or an API key
Fully custodial - Metorial stores and centrally manages OAuth tokens for every connected... | [Paid, self-serve](../gates/paid.md) |
| [Mixmax](../tools/mixmax.md)
mixmax.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://mcp.mixmax.com/mcp](https://mcp.mixmax.com/mcp) +2 more | OAuth
OAuth 2.0 authorization code flow, scoped to the connecting user's account. Read-only. | [Paid, self-serve](../gates/paid.md) |
| [Ocean.io](../tools/ocean-io.md)
ocean.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://app.ocean.io/docs/getting-started/mcp](https://app.ocean.io/docs/getting-started/mcp) +1 more | API key
api key (api-token passed as a URL parameter to the hosted MCP endpoint) | [Paid, self-serve](../gates/paid.md) |
| [Octave](../tools/octave.md)
octavehq.com | [RevOps Infra](../categories/revops-infra.md) | [https://docs.octavehq.com/mcp/overview](https://docs.octavehq.com/mcp/overview) +3 more | OAuth or an API key
Browser OAuth. Per the vendor's Claude Code setup doc you add the server with "claude mcp... | [Paid, self-serve](../gates/paid.md) |
| [Ortto](../tools/ortto.md)
ortto.com | [RevOps Infra](../categories/revops-infra.md) | [https://mcp-api-us.ortto.app/mcp](https://mcp-api-us.ortto.app/mcp) +1 more | Auth not recorded
A scoped JWT key created as an MCP data source inside the Ortto account, passed as a... | [Paid, self-serve](../gates/paid.md) |
| [PhantomBuster](../tools/phantombuster.md)
phantombuster.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server) +1 more | OAuth
OAuth - first connection redirects to PhantomBuster sign-in/authorization, then... | [Paid, self-serve](../gates/paid.md) |
| [Pipedream MCP](../tools/pipedream-mcp.md)
pipedream.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://mcp.pipedream.com](https://mcp.pipedream.com) | OAuth or an API key
OAuth/API-key credentials for each underlying app are stored by Pipedream and isolated... | [Paid, self-serve](../gates/paid.md) |
| [RB2B](../tools/rb2b.md)
rb2b.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://github.com/robbclarke/RB2B-APIs-MCP](https://github.com/robbclarke/RB2B-APIs-MCP) | API key
api key | [Paid, self-serve](../gates/paid.md) |
| [Reply.io](../tools/reply-io.md)
reply.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://reply.io/mcp/](https://reply.io/mcp/) | API key
api key (personal API key over HTTPS, included in free trial) | [Paid, self-serve](../gates/paid.md) |
| [Responsive (formerly RFPIO)](../tools/responsive.md)
responsive.io | [Proposals & Deals](../categories/proposals-deals.md) | [https://www.responsive.io/capability/mcp-server](https://www.responsive.io/capability/mcp-server) +2 more | Auth not recorded
unknown - not detailed in the sources reviewed. | [Paid, self-serve](../gates/paid.md) |
| [RocketReach](../tools/rocketreach.md)
rocketreach.co | [Data & Enrichment](../categories/data-enrichment.md) | [https://rocketreach.co/resources/products/mcp/](https://rocketreach.co/resources/products/mcp/) +1 more | OAuth
OAuth 2.1, browser-based; ties to your existing RocketReach account and shares its credit... | [Paid, self-serve](../gates/paid.md) |
| [Salesforge](../tools/salesforge.md)
salesforge.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp) | API key
api key via HTTP header (X-Salesforge-Key) | [Paid, self-serve](../gates/paid.md) |
| [Salesforge (Agent Frank)](../tools/salesforge.md)
salesforge.ai | [AI SDRs](../categories/ai-sdr-agents.md) | [https://help.salesforge.ai/en/articles/10333582-sale...](https://help.salesforge.ai/en/articles/10333582-salesforge-mcp-server-connect-with-ai-assistants) | Auth not recorded
unknown specifics (help article confirms an official MCP server "to connect with AI... | [Paid, self-serve](../gates/paid.md) |
| [Snitcher](../tools/snitcher.md)
snitcher.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://www.snitcher.com/changelog/point-claude-at-s...](https://www.snitcher.com/changelog/point-claude-at-snitcher/) | Auth not recorded
unknown - vendor changelog points to docs.snitcher.com for authentication specifics, not... | [Paid, self-serve](../gates/paid.md) |
| [Snov.io](../tools/snov-io.md)
snov.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.snov.io/mcp](https://mcp.snov.io/mcp) +1 more | OAuth
OAuth - user reviews and approves the connection through their Snov.io account; no raw... | [Paid, self-serve](../gates/paid.md) |
| [SparkToro](../tools/sparktoro.md)
sparktoro.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://sparktoro.com/mcp](https://sparktoro.com/mcp) +1 more | OAuth
OAuth (one-click sign-in with an existing SparkToro account); documented to work with... | [Paid, self-serve](../gates/paid.md) |
| [Sumble](../tools/sumble.md)
sumble.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://docs.sumble.com/pages/KLH6XuEHsUssUZW6C1i4](https://docs.sumble.com/pages/KLH6XuEHsUssUZW6C1i4) | Auth not recorded
unknown - not disclosed in the public docs excerpt available | [Paid, self-serve](../gates/paid.md) |
| [Super Send](../tools/super-send.md)
supersend.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://docs.supersend.io/docs/mcp-server](https://docs.supersend.io/docs/mcp-server) | API key
api key, Streamable HTTP transport | [Paid, self-serve](../gates/paid.md) |
| [Superblocks](../tools/superblocks.md)
superblocks.com | [RevOps Infra](../categories/revops-infra.md) | [https://superblocks.com/blog/superblocks-mcp](https://superblocks.com/blog/superblocks-mcp) | OAuth
unknown - the announcement doesn't specify the auth method; the feature is... | [Paid, self-serve](../gates/paid.md) |
| [The Swarm](../tools/the-swarm.md)
theswarm.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://bee.theswarm.com/mcp](https://bee.theswarm.com/mcp) +1 more | OAuth or an API key
OAuth via personal Swarm login (native Claude and ChatGPT app connectors) or team API key... | [Paid, self-serve](../gates/paid.md) |
| [tl;dv](../tools/tl-dv.md)
tldv.io | [Conversation Intel](../categories/conversation-intel.md) | [https://github.com/tldv-public/tldv-mcp-server](https://github.com/tldv-public/tldv-mcp-server) +1 more | API key
API key generated at Settings → Personal Settings → API keys. | [Paid, self-serve](../gates/paid.md) |
| [Vainu](../tools/vainu.md)
vainu.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.vainu.ai/mcp](https://mcp.vainu.ai/mcp) +2 more | OAuth
OAuth 2.0 with PKCE, scoped to existing Vainu permissions, but NOT enabled by default.... | [Paid, self-serve](../gates/paid.md) |
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
woodpecker.co | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/) +1 more | OAuth or an API key
hosted OAuth-style flow (Claude-specific) or self-hosted Docker setup using a Woodpecker... | [Paid, self-serve](../gates/paid.md) |
| [Clari](../tools/clari.md)
clari.com | [Conversation Intel](../categories/conversation-intel.md) | [https://www.clari.com/press/clari-salesloft-forecast...](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/) | Auth not recorded
unknown / not disclosed publicly | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [6sense](../tools/6sense.md)
6sense.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://6sense.com/platform/mcp-server/](https://6sense.com/platform/mcp-server/) +1 more | OAuth
OAuth using existing 6sense platform login (no separate API key setup per vendor docs) | [Enterprise only](../gates/enterprise-only.md) |
| [Apollo.io Sequences (Emailer Campaigns)](../tools/apollo-io-sequences.md)
apollo.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) +1 more | OAuth
OAuth (Apollo.io sign-in/authorization flow; no API key required for this MCP) | [Enterprise only](../gates/enterprise-only.md) |
| [Clari (+ Salesloft agents)](../tools/clari.md)
clari.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://www.clari.com/press/clari-salesloft-forecast...](https://www.clari.com/press/clari-salesloft-forecasting-execution-mcp-server/) | Auth not recorded
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
highspot.com | [Conversation Intel](../categories/conversation-intel.md) | [https://www.highspot.com/product/mcp-server/](https://www.highspot.com/product/mcp-server/) | Auth not recorded
unknown - product page describes agent-to-agent access via OpenAI, Anthropic, and... | [Enterprise only](../gates/enterprise-only.md) |
| [Ironclad](../tools/ironclad.md)
ironcladapp.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://support.ironcladapp.com/hc/en-us/articles/39...](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server) +1 more | Auth not recorded
unknown - a single, static MCP endpoint per the support article; specific credential... | [Enterprise only](../gates/enterprise-only.md) |
| [Otter.ai](../tools/otter-ai.md)
otter.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://help.otter.ai/hc/en-us/articles/352876075696...](https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server) +2 more | Auth not recorded
unknown - exact auth mechanism not confirmed in public sources; framed under "Otter for... | [Enterprise only](../gates/enterprise-only.md) |
| [Pigment](../tools/pigment.md)
pigment.com | [Forecasting & Revenue](../categories/forecasting-revenue.md) | [https://www.pigment.com/ai/mcp-server](https://www.pigment.com/ai/mcp-server) +1 more | Auth not recorded
A workspace admin enables MCP under Settings > Integrations, generating a per-workspace... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)
salesforce.com | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) +2 more | OAuth
OAuth + PKCE via an External Client App (scopes mcp_api, refresh_token); every MCP call... | [Enterprise only](../gates/enterprise-only.md) |
| [Seamless.AI](../tools/seamless-ai.md)
seamless.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://docs.seamless.ai/mcp-docs](https://docs.seamless.ai/mcp-docs) +1 more | OAuth or an API key
OAuth 2.1 or API key; docs state "MCP access must be enabled on your account" - i.e.... | [Enterprise only](../gates/enterprise-only.md) |
| [Seismic](../tools/seismic.md)
seismic.com | [Conversation Intel](../categories/conversation-intel.md) | [https://developer.seismic.com/seismicsoftware/docs/s...](https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server) | OAuth or an API key
Streamable HTTP transport per Seismic's MCP documentation; the specific credential type... | [Enterprise only](../gates/enterprise-only.md) |
| [Similarweb](../tools/similarweb.md)
similarweb.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://mcp.similarweb.com](https://mcp.similarweb.com) +3 more | OAuth or an API key
CONFLICTING VENDOR STATEMENTS, flagged rather than resolved. Both Similarweb developer... | [Enterprise only](../gates/enterprise-only.md) |
| [Surfe](../tools/surfe.md)
surfe.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://mcp.eu.surfe.com/mcp](https://mcp.eu.surfe.com/mcp) +1 more | API key
Surfe API key, with a browser sign-in flow that exchanges the key for a managed token so... | [Enterprise only](../gates/enterprise-only.md) |
| [Syncari](../tools/syncari.md)
syncari.com | [RevOps Infra](../categories/revops-infra.md) | [https://syncari.com/mcp-server/](https://syncari.com/mcp-server/) | OAuth or an API key
unknown - the MCP server page describes real-time, entity/field-level access control and... | [Enterprise only](../gates/enterprise-only.md) |
| [UserGems](../tools/usergems.md)
usergems.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://www.usergems.com/product/mcp](https://www.usergems.com/product/mcp) | OAuth or an API key
unknown - connects inside Claude/ChatGPT per the product page, but the exact auth... | [Enterprise only](../gates/enterprise-only.md) |
| [Ada](../tools/ada.md)
ada.cx | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server) | Auth not recorded
none documented - connects over HTTP with no credential requirement described in the... | [Gate unknown](../gates/unknown.md) |
| [Allego](../tools/allego.md)
allego.com | [Enablement & Coaching](../categories/enablement-coaching.md) | [https://www.allego.com/platform/integrations/](https://www.allego.com/platform/integrations/) | Auth not recorded
unknown - vendor material states the MCP server connects to Salesforce Einstein,... | [Gate unknown](../gates/unknown.md) |
| [Anaplan (PlanIQ / Anaplan Forecaster)](../tools/anaplan.md)
anaplan.com | [Forecasting & Revenue](../categories/forecasting-revenue.md) | [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/) | OAuth or an API key
unknown - described only as a "governed MCP connection" with permission/audit controls;... | [Gate unknown](../gates/unknown.md) |
| [Crustdata](../tools/crustdata.md)
crustdata.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://crustdata.com/](https://crustdata.com/) | Auth not recorded
unknown | [Gate unknown](../gates/unknown.md) |
| [Default](../tools/default.md)
default.com | [RevOps Infra](../categories/revops-infra.md) | [https://www.default.com](https://www.default.com) | Auth not recorded
unknown - not documented anywhere found (checked default.com, default.com/product,... | [Gate unknown](../gates/unknown.md) |
| [Default](../tools/default.md)
default.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://www.default.com/product/platform](https://www.default.com/product/platform) | OAuth or an API key
unknown - not specified on the public page (plausibly API key or OAuth given CRM-grade... | [Gate unknown](../gates/unknown.md) |
| [Endgame](../tools/endgame.md)
endgame.io | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://docs.endgame.io/features/mcp-server](https://docs.endgame.io/features/mcp-server) +1 more | OAuth or an API key
OAuth (browser-based) for individual users via Claude/ChatGPT/Claude Code/Codex... | [Gate unknown](../gates/unknown.md) |
| [Explorium](../tools/explorium.md)
explorium.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.explorium.ai/mcp/](https://www.explorium.ai/mcp/) +1 more | API key
api key | [Gate unknown](../gates/unknown.md) |
| [Fellow](../tools/fellow.md)
fellow.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://fellow.app/mcp](https://fellow.app/mcp) +1 more | OAuth
OAuth, with OAuth 2.0 dynamic discovery supported. | [Gate unknown](../gates/unknown.md) |
| [Granola](../tools/granola.md)
granola.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://www.pulsemcp.com/servers/granola](https://www.pulsemcp.com/servers/granola) +2 more | OAuth
OAuth - no manual API key required. | [Gate unknown](../gates/unknown.md) |
| [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md)
turbomcp.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://turbomcp.ai](https://turbomcp.ai) | OAuth
Integrates with a team's own OIDC-compatible identity provider; handles OAuth and Dynamic... | [Gate unknown](../gates/unknown.md) |
| [Outreach](../tools/outreach.md)
outreach.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://api.outreach.io/mcp/](https://api.outreach.io/mcp/) +1 more | OAuth
OAuth 2.1 with Dynamic Client Registration; also requires the org-level "Amplify" add-on... | [Gate unknown](../gates/unknown.md) |
| [Pylon](../tools/pylon.md)
usepylon.com | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://mcp.usepylon.com](https://mcp.usepylon.com) +1 more | OAuth
OAuth 2.0 over stateless streamable HTTP; access is permission-scoped so a connected AI... | [Gate unknown](../gates/unknown.md) |
| [Reclaim.ai](../tools/reclaim-ai.md)
reclaim.ai | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://mcp.reclaim.ai](https://mcp.reclaim.ai) | OAuth or an API key
OAuth (official hosted server). A separate unofficial/community server also exists... | [Gate unknown](../gates/unknown.md) |
| [RevenueHero](../tools/revenuehero.md)
revenuehero.io | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://www.revenuehero.io/resources/tales-of-ops](https://www.revenuehero.io/resources/tales-of-ops) | API key
Per-customer router token over an SSE endpoint, manually provisioned by RevenueHero -... | [Gate unknown](../gates/unknown.md) |
| [Salesloft](../tools/salesloft.md)
salesloft.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://www.salesloft.com/company/newsroom/clari-sal...](https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server) +1 more | OAuth
unknown exact flow - vendor press material describes it as natively listed in Claude's... | [Gate unknown](../gates/unknown.md) |
| [Sybill](../tools/sybill.md)
sybill.ai | [Conversation Intel](../categories/conversation-intel.md) | [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html) +1 more | OAuth
Browser-based sign-in / OAuth on first connection from an MCP client such as Claude... | [Gate unknown](../gates/unknown.md) |
| [Trumpet](../tools/trumpet.md)
sendtrumpet.com | [Video Prospecting](../categories/video-prospecting.md) | [https://trumpet.app/api/mcp](https://trumpet.app/api/mcp) +2 more | OAuth
OAuth 2.0 - vendor help-center doc confirms "Authenticate via trumpet (OAuth 2.0)";... | [Gate unknown](../gates/unknown.md) |
| [Zoom Revenue Accelerator](../tools/zoom-revenue-accelerator.md)
zoom.com | [Conversation Intel](../categories/conversation-intel.md) | [https://news.zoom.com/zoom-revenue-accelerator-mcp-c...](https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/) +1 more | OAuth or an API key
OAuth - Zoom user-level OAuth access token (env var... | [Gate unknown](../gates/unknown.md) |

Counted 2026-08-25 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
