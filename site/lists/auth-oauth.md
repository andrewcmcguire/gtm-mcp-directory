# GTM MCP servers that use OAuth: 46 tools, counted

> 46 of the 165 GTM tools with an MCP server use OAuth. The verbatim auth field for each one is printed beside it. Counted 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers that use OAuth

**List · 46 of 293**

## GTM MCP servers that use OAuth

The server takes the user through a browser sign in and holds a scoped token. Nothing is pasted into a config file, and access can be revoked from the vendor side without touching the agent. The bucket is a keyword match over the mcp_auth field, run at build time, and the verbatim field ships in the row beside it so you can check the parse yourself. Where the two disagree, the verbatim field is the fact and the bucket is the convenience.

| Tool | MCP status | Server URL | mcp_auth, verbatim | Gate |
|---|---|---|---|---|
| [Attio](../tools/attio.md)
attio.com | [Official MCP](../mcp/official.md) | [https://docs.attio.com/mcp/overview](https://docs.attio.com/mcp/overview) +1 more | OAuth - one-time login as the user's own Attio account, no API key needed. Reads auto-approve; writes require confirmation. Permissions mirror... | [Free to start](../gates/free.md) |
| [Cargo](../tools/cargo.md)
getcargo.ai | [Official MCP](../mcp/official.md) | [https://docs.getcargo.ai/](https://docs.getcargo.ai/) | unknown for the MCP layer specifically - docs confirm the capability but not its auth mechanism. Cargo's separate REST API (api.getcargo.io/v1) uses... | [Free to start](../gates/free.md) |
| [FullEnrich](../tools/fullenrich.md)
fullenrich.com | [Official MCP](../mcp/official.md) | [https://mcp.fullenrich.com/mcp](https://mcp.fullenrich.com/mcp) +1 more | oauth (browser sign-in to FullEnrich account; no manual API key needed) | [Free to start](../gates/free.md) |
| [HubSpot](../tools/hubspot.md)
hubspot.com | [Official MCP](../mcp/official.md) | [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp) | OAuth 2.0 for the hosted Remote MCP Server (migrating to OAuth 2.1 with PKCE + refresh-token rotation), explicitly excluding custom Sensitive Data... | [Free to start](../gates/free.md) |
| [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md)
leadfeeder.com | [Official MCP](../mcp/official.md) | [https://www.leadfeeder.com/features/mcp-server/](https://www.leadfeeder.com/features/mcp-server/) +1 more | OAuth - user signs in with their own Leadfeeder account; vendor states "No keys pasted in." | [Free to start](../gates/free.md) |
| [PandaDoc](../tools/pandadoc.md)
pandadoc.com | [Official MCP](../mcp/official.md) | [https://developers.pandadoc.com/docs/how-to-use-the-...](https://developers.pandadoc.com/docs/how-to-use-the-pandadoc-mcp-server) +1 more | OAuth - remote hosted server, add the server URL to an MCP client (Claude Desktop, Claude Code, Cursor, VS Code, Gemini, etc.) and authenticate via... | [Free to start](../gates/free.md) |
| [Pipedrive](../tools/pipedrive.md)
pipedrive.com | [Official MCP](../mcp/official.md) | [https://www.pipedrive.com/en/features/mcp-server](https://www.pipedrive.com/en/features/mcp-server) | OAuth - "Connect in minutes through secure OAuth. No coding, no API development, no developer required." AI assistants can only see/edit what the... | [Free to start](../gates/free.md) |
| [Relevance AI](../tools/relevance-ai.md)
relevanceai.com | [Official MCP](../mcp/official.md) | [https://relevanceai.com/docs/integrations/mcp/progra...](https://relevanceai.com/docs/integrations/mcp/programmatic-gtm/introduction) | OAuth (tokens may expire after inactivity; re-auth via login flow); Viewer/Chat project roles get restricted read-only access automatically | [Free to start](../gates/free.md) |
| [Retool](../tools/retool.md)
retool.com | [Official MCP](../mcp/official.md) | [https://retool.com/blog/retool-mcp-server](https://retool.com/blog/retool-mcp-server) | OAuth 2.0. Endpoint pattern https:///mcp over HTTP. | [Free to start](../gates/free.md) |
| [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md)
snowflake.com | [Official MCP](../mcp/official.md) | [https://docs.snowflake.com/en/user-guide/snowflake-c...](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) | Snowflake OAuth 2.0 by default, or External OAuth (Okta, Microsoft Entra ID); hardcoded PATs/tokens are explicitly discouraged. Exposes Cortex Agent,... | [Free to start](../gates/free.md) |
| [Trumpet (sendtrumpet.com)](../tools/trumpet.md)
sendtrumpet.com | [Official MCP](../mcp/official.md) | [https://www.sendtrumpet.com/blog-posts/introducing-t...](https://www.sendtrumpet.com/blog-posts/introducing-trumpet-mcp) | unknown - vendor states it is "installable in five minutes with no engineering required," implying a simple hosted-connector flow, but the specific... | [Free to start](../gates/free.md) |
| [Zapier MCP](../tools/zapier-mcp.md)
zapier.com | [Official MCP](../mcp/official.md) | [https://mcp.zapier.com](https://mcp.zapier.com) | Uses Zapier's existing decade-old app-connection/OAuth infrastructure - you authorize apps the same way you would for a normal Zap, then expose... | [Free to start](../gates/free.md) |
| [ZoomInfo](../tools/zoominfo.md)
zoominfo.com | [Official MCP](../mcp/official.md) | [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp) +2 more | OAuth for user-level access, or client credentials for service accounts; no API keys stored by the client. A local mcp-remote bridge is used for... | [Free to start](../gates/free.md) |
| [Allegrow](../tools/allegrow.md)
allegrow.co | [Official MCP](../mcp/official.md) | [https://www.allegrow.co/knowledge-base/claude-email-...](https://www.allegrow.co/knowledge-base/claude-email-mcp) | OAuth - connects through Claude's standard connector authorization flow; user logs into their Allegrow account and grants access explicitly (no... | [Paid, self-serve](../gates/paid.md) |
| [Apollo.io](../tools/apollo-io.md)
apollo.io | [Official MCP](../mcp/official.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | OAuth (Apollo.io sign-in/authorization flow in the client) | [Paid, self-serve](../gates/paid.md) |
| [Circleback](../tools/circleback.md)
circleback.ai | [Official MCP](../mcp/official.md) | [https://circleback.ai/api/mcp](https://circleback.ai/api/mcp) +2 more | OAuth with dynamic client registration, compliant with the authenticated remote MCP spec. Centrally hosted and managed by Circleback. | [Paid, self-serve](../gates/paid.md) |
| [Coresignal](../tools/coresignal.md)
coresignal.com | [Official MCP](../mcp/official.md) | [https://coresignal.com/mcp-server/](https://coresignal.com/mcp-server/) | OAuth 2.1 - per docs, the data key is fetched live with every request and never stored, allowing instant revocation | [Paid, self-serve](../gates/paid.md) |
| [Cube Software](../tools/cube-software.md)
cubesoftware.com | [Official MCP](../mcp/official.md) | [https://www.cubesoftware.com/mcp](https://www.cubesoftware.com/mcp) +1 more | OAuth - no manual API key management. | [Paid, self-serve](../gates/paid.md) |
| [DocuSign](../tools/docusign.md)
docusign.com | [Official MCP](../mcp/official.md) | [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/) +2 more | OAuth - Streamable HTTP transport; first connection opens a browser window to sign in and authorize, then reuses credentials. | [Paid, self-serve](../gates/paid.md) |
| [Grain](../tools/grain.md)
grain.com | [Official MCP](../mcp/official.md) | [https://developers.grain.com/mcp](https://developers.grain.com/mcp) +1 more | OAuth via the native Claude integration, or manual server-URL setup for other MCP clients. Deal and coaching-feedback tools specifically require a... | [Paid, self-serve](../gates/paid.md) |
| [HeyGen](../tools/heygen.md)
heygen.com | [Official MCP](../mcp/official.md) | [https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/) +2 more | OAuth - vendor states "connect your HeyGen account, no API key required"; generation draws down the premium credits already in the user's HeyGen... | [Paid, self-serve](../gates/paid.md) |
| [La Growth Machine](../tools/la-growth-machine.md)
lagrowthmachine.com | [Official MCP](../mcp/official.md) | [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system) +1 more | OAuth - no API key needed; first use opens a browser sign-in directly to the user's La Growth Machine account. | [Paid, self-serve](../gates/paid.md) |
| [Mixmax](../tools/mixmax.md)
mixmax.com | [Official MCP](../mcp/official.md) | [https://mcp.mixmax.com/mcp](https://mcp.mixmax.com/mcp) +2 more | OAuth 2.0 authorization code flow, scoped to the connecting user's account. Read-only. | [Paid, self-serve](../gates/paid.md) |
| [PhantomBuster](../tools/phantombuster.md)
phantombuster.com | [Official MCP](../mcp/official.md) | [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server) +1 more | OAuth - first connection redirects to PhantomBuster sign-in/authorization, then workspace selection. | [Paid, self-serve](../gates/paid.md) |
| [RocketReach](../tools/rocketreach.md)
rocketreach.co | [Official MCP](../mcp/official.md) | [https://rocketreach.co/resources/products/mcp/](https://rocketreach.co/resources/products/mcp/) +1 more | OAuth 2.1, browser-based; ties to your existing RocketReach account and shares its credit pool (no separate API key needed for the official connector) | [Paid, self-serve](../gates/paid.md) |
| [Snov.io](../tools/snov-io.md)
snov.io | [Official MCP](../mcp/official.md) | [https://mcp.snov.io/mcp](https://mcp.snov.io/mcp) +1 more | OAuth - user reviews and approves the connection through their Snov.io account; no raw API key is shared with the AI assistant | [Paid, self-serve](../gates/paid.md) |
| [SparkToro](../tools/sparktoro.md)
sparktoro.com | [Official MCP](../mcp/official.md) | [https://sparktoro.com/mcp](https://sparktoro.com/mcp) +1 more | OAuth (one-click sign-in with an existing SparkToro account); documented to work with Claude Desktop, Claude Code, Cursor, and ChatGPT. | [Paid, self-serve](../gates/paid.md) |
| [Superblocks](../tools/superblocks.md)
superblocks.com | [Official MCP](../mcp/official.md) | [https://superblocks.com/blog/superblocks-mcp](https://superblocks.com/blog/superblocks-mcp) | unknown - the announcement doesn't specify the auth method; the feature is Enterprise-only, implying an admin/OAuth-gated setup, but this isn't... | [Paid, self-serve](../gates/paid.md) |
| [Vainu](../tools/vainu.md)
vainu.com | [Official MCP](../mcp/official.md) | [https://mcp.vainu.ai/mcp](https://mcp.vainu.ai/mcp) +2 more | OAuth 2.0 with PKCE, scoped to existing Vainu permissions, but NOT enabled by default. The vendor help centre says it "isn't automatically available... | [Paid, self-serve](../gates/paid.md) |
| [Versium REACH](../tools/versium-reach.md)
versium.com | [Official MCP](../mcp/official.md) | [https://app.versium.com/mcp/reach](https://app.versium.com/mcp/reach) +2 more | OAuth, and the client must support dynamic client registration. | [Paid, self-serve](../gates/paid.md) |
| [6sense](../tools/6sense.md)
6sense.com | [Official MCP](../mcp/official.md) | [https://6sense.com/platform/mcp-server/](https://6sense.com/platform/mcp-server/) +1 more | OAuth using existing 6sense platform login (no separate API key setup per vendor docs) | [Enterprise only](../gates/enterprise-only.md) |
| [Apollo.io Sequences (Emailer Campaigns)](../tools/apollo-io-sequences.md)
apollo.io | [Official MCP](../mcp/official.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) +1 more | OAuth (Apollo.io sign-in/authorization flow; no API key required for this MCP) | [Enterprise only](../gates/enterprise-only.md) |
| [Common Room](../tools/common-room.md)
commonroom.io | [Official MCP](../mcp/official.md) | [https://www.commonroom.io/docs/using-common-room/mcp...](https://www.commonroom.io/docs/using-common-room/mcp-server/) +1 more | oauth (OAuth 2.1, browser-based, tokens scoped to the user's own Common Room permissions) | [Enterprise only](../gates/enterprise-only.md) |
| [Common Room](../tools/common-room.md)
commonroom.io | [Official MCP](../mcp/official.md) | [https://www.commonroom.io/docs/using-common-room/mcp...](https://www.commonroom.io/docs/using-common-room/mcp-server/) +1 more | oauth (OAuth 2.1, browser-based, tokens scoped to the user's own Common Room permissions) | [Enterprise only](../gates/enterprise-only.md) |
| [Crossbeam](../tools/crossbeam.md)
crossbeam.com | [Official MCP](../mcp/official.md) | [https://mcp.crossbeam.com/mcp](https://mcp.crossbeam.com/mcp) +1 more | OAuth with Crossbeam login credentials, with a permission consent screen at connect time. | [Enterprise only](../gates/enterprise-only.md) |
| [G2 Buyer Intent](../tools/g2-buyer-intent.md)
g2.com | [Official MCP](../mcp/official.md) | [https://mcp.g2.com/mcp](https://mcp.g2.com/mcp) +2 more | OAuth 2.0 Authorization Code with PKCE. You register an OAuth app in the G2 Developer Dashboard at https://my.g2.com/developers to get a client_id... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)
salesforce.com | [Official MCP](../mcp/official.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) +2 more | OAuth + PKCE via an External Client App (scopes mcp_api, refresh_token); every MCP call runs under the authenticated user's own permissions... | [Enterprise only](../gates/enterprise-only.md) |
| [Fellow](../tools/fellow.md)
fellow.ai | [Official MCP](../mcp/official.md) | [https://fellow.app/mcp](https://fellow.app/mcp) +1 more | OAuth, with OAuth 2.0 dynamic discovery supported. | [Gate unknown](../gates/unknown.md) |
| [Granola](../tools/granola.md)
granola.ai | [Official MCP](../mcp/official.md) | [https://www.pulsemcp.com/servers/granola](https://www.pulsemcp.com/servers/granola) +2 more | OAuth - no manual API key required. | [Gate unknown](../gates/unknown.md) |
| [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md)
turbomcp.ai | [Official MCP](../mcp/official.md) | [https://turbomcp.ai](https://turbomcp.ai) | Integrates with a team's own OIDC-compatible identity provider; handles OAuth and Dynamic Client Registration for the servers it fronts. | [Gate unknown](../gates/unknown.md) |
| [Outreach](../tools/outreach.md)
outreach.io | [Official MCP](../mcp/official.md) | [https://api.outreach.io/mcp/](https://api.outreach.io/mcp/) +1 more | OAuth 2.1 with Dynamic Client Registration; also requires the org-level "Amplify" add-on to be enabled and admin-toggled - not available to every... | [Gate unknown](../gates/unknown.md) |
| [Pylon](../tools/pylon.md)
usepylon.com | [Official MCP](../mcp/official.md) | [https://mcp.usepylon.com](https://mcp.usepylon.com) +1 more | OAuth 2.0 over stateless streamable HTTP; access is permission-scoped so a connected AI tool can only see/change what the authenticated user could... | [Gate unknown](../gates/unknown.md) |
| [Salesloft](../tools/salesloft.md)
salesloft.com | [Official MCP](../mcp/official.md) | [https://www.salesloft.com/company/newsroom/clari-sal...](https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server) +1 more | unknown exact flow - vendor press material describes it as natively listed in Claude's connector directory "with no custom setup required," implying... | [Gate unknown](../gates/unknown.md) |
| [Sybill](../tools/sybill.md)
sybill.ai | [Official MCP](../mcp/official.md) | [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html) +1 more | Browser-based sign-in / OAuth on first connection from an MCP client such as Claude Desktop. | [Gate unknown](../gates/unknown.md) |
| [Trumpet](../tools/trumpet.md)
sendtrumpet.com | [Official MCP](../mcp/official.md) | [https://trumpet.app/api/mcp](https://trumpet.app/api/mcp) +2 more | OAuth 2.0 - vendor help-center doc confirms "Authenticate via trumpet (OAuth 2.0)"; setup flow is add-custom-connector → paste MCP server URL →... | [Gate unknown](../gates/unknown.md) |
| [Bonjoro](../tools/bonjoro.md)
bonjoro.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro) | Rides a Zapier account connection (OAuth to Zapier, which holds the Bonjoro-side connection). | [Paid, self-serve](../gates/paid.md) |

Counted 2026-08-25 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
