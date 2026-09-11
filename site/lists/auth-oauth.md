# GTM MCP servers that use OAuth: 69 tools, counted

> 69 of the 225 GTM tools with an MCP server use OAuth. The verbatim auth field for each one is printed beside it. Counted 2026-09-11.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers that use OAuth

**List · 69 of 336**

## GTM MCP servers that use OAuth

The server takes the user through a browser sign in and holds a scoped token. Nothing is pasted into a config file, and access can be revoked from the vendor side without touching the agent. The bucket is a keyword match over the mcp_auth field, run at build time, and the verbatim field ships in the row beside it so you can check the parse yourself. Where the two disagree, the verbatim field is the fact and the bucket is the convenience.

| Tool | MCP status | Server URL | mcp_auth, verbatim | Gate |
|---|---|---|---|---|
| [Attio](../tools/attio.md)
attio.com | [Official MCP](../mcp/official.md) | [https://mcp.attio.com/mcp](https://mcp.attio.com/mcp) +1 more | OAuth - one-time login as the user's own Attio account, no API key needed. Reads auto-approve; writes require confirmation. Permissions mirror... | [Free to start](../gates/free.md) |
| [Cargo](../tools/cargo.md)
getcargo.ai | [Official MCP](../mcp/official.md) | [https://docs.getcargo.ai/](https://docs.getcargo.ai/) | unknown for the MCP layer specifically - docs confirm the capability but not its auth mechanism. Cargo's separate REST API (api.getcargo.io/v1) uses... | [Free to start](../gates/free.md) |
| [FullEnrich](../tools/fullenrich.md)
fullenrich.com | [Official MCP](../mcp/official.md) | [https://mcp.fullenrich.com/mcp](https://mcp.fullenrich.com/mcp) +1 more | oauth (browser sign-in to FullEnrich account; no manual API key needed) | [Free to start](../gates/free.md) |
| [HubSpot](../tools/hubspot.md)
hubspot.com | [Official MCP](../mcp/official.md) | [https://developers.hubspot.com/ai-tools/mcp](https://developers.hubspot.com/ai-tools/mcp) | OAuth 2.0 for the hosted Remote MCP Server (migrating to OAuth 2.1 with PKCE + refresh-token rotation), explicitly excluding custom Sensitive Data... | [Free to start](../gates/free.md) |
| [Knit MCP](../tools/knit-mcp.md)
getknit.dev | [Official MCP](../mcp/official.md) | [https://www.getknit.dev/mcp-servers](https://www.getknit.dev/mcp-servers) +1 more | Knit-managed OAuth or SAML per connected application; the customer authorises each end application through Knit rather than holding its credentials... | [Free to start](../gates/free.md) |
| [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md)
leadfeeder.com | [Official MCP](../mcp/official.md) | [https://www.leadfeeder.com/features/mcp-server/](https://www.leadfeeder.com/features/mcp-server/) +1 more | OAuth - user signs in with their own Leadfeeder account; vendor states "No keys pasted in." | [Free to start](../gates/free.md) |
| [Metricool](../tools/metricool.md)
metricool.com | [Official MCP](../mcp/official.md) | [https://ai.metricool.com/mcp](https://ai.metricool.com/mcp) +3 more | oauth (browser authorisation in clients that support remote OAuth MCP) or a METRICOOL_USER_TOKEN plus METRICOOL_USER_ID header pair from account... | [Free to start](../gates/free.md) |
| [PandaDoc](../tools/pandadoc.md)
pandadoc.com | [Official MCP](../mcp/official.md) | [https://mcp.pandadoc.com/v1/mcp](https://mcp.pandadoc.com/v1/mcp) +2 more | OAuth - remote hosted server, add the server URL to an MCP client (Claude Desktop, Claude Code, Cursor, VS Code, Gemini, etc.) and authenticate via... | [Free to start](../gates/free.md) |
| [Pipedrive](../tools/pipedrive.md)
pipedrive.com | [Official MCP](../mcp/official.md) | [https://mcp.pipedrive.com/mcp](https://mcp.pipedrive.com/mcp) +1 more | OAuth - "Connect in minutes through secure OAuth. No coding, no API development, no developer required." AI assistants can only see/edit what the... | [Free to start](../gates/free.md) |
| [Relevance AI](../tools/relevance-ai.md)
relevanceai.com | [Official MCP](../mcp/official.md) | [https://mcp.relevanceai.com/](https://mcp.relevanceai.com/) +1 more | OAuth (tokens may expire after inactivity; re-auth via login flow); Viewer/Chat project roles get restricted read-only access automatically | [Free to start](../gates/free.md) |
| [Retool](../tools/retool.md)
retool.com | [Official MCP](../mcp/official.md) | [https://mcp.retool.com/mcp](https://mcp.retool.com/mcp) +1 more | OAuth 2.0. Endpoint pattern https:///mcp over HTTP. | [Free to start](../gates/free.md) |
| [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md)
snowflake.com | [Official MCP](../mcp/official.md) | [https://docs.snowflake.com/en/user-guide/snowflake-c...](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp) +1 more | Snowflake OAuth 2.0 by default, or External OAuth (Okta, Microsoft Entra ID); hardcoded PATs/tokens are explicitly discouraged. Exposes Cortex Agent,... | [Free to start](../gates/free.md) |
| [Tidio](../tools/tidio.md)
tidio.com | [Official MCP](../mcp/official.md) | [https://github.com/TidioPoland/tidio-mcp-connector](https://github.com/TidioPoland/tidio-mcp-connector) +1 more | OAuth: the tidio_connect tool opens a browser to Tidio's login page, then stores access and refresh tokens locally in ~/.tidio-mcp/credentials.json. | [Free to start](../gates/free.md) |
| [Trumpet (sendtrumpet.com)](../tools/trumpet.md)
sendtrumpet.com | [Official MCP](../mcp/official.md) | [https://www.sendtrumpet.com/blog-posts/introducing-t...](https://www.sendtrumpet.com/blog-posts/introducing-trumpet-mcp) | unknown - vendor states it is "installable in five minutes with no engineering required," implying a simple hosted-connector flow, but the specific... | [Free to start](../gates/free.md) |
| [Zapier MCP](../tools/zapier-mcp.md)
zapier.com | [Official MCP](../mcp/official.md) | [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect) +3 more | Uses Zapier's existing decade-old app-connection/OAuth infrastructure - you authorize apps the same way you would for a normal Zap, then expose... | [Free to start](../gates/free.md) |
| [ZoomInfo](../tools/zoominfo.md)
zoominfo.com | [Official MCP](../mcp/official.md) | [https://mcp.zoominfo.com/mcp](https://mcp.zoominfo.com/mcp) +2 more | OAuth for user-level access, or client credentials for service accounts; no API keys stored by the client. A local mcp-remote bridge is used for... | [Free to start](../gates/free.md) |
| [Allegrow](../tools/allegrow.md)
allegrow.co | [Official MCP](../mcp/official.md) | [https://mcp.allegrow.co/mcp](https://mcp.allegrow.co/mcp) +1 more | OAuth - connects through Claude's standard connector authorization flow; user logs into their Allegrow account and grants access explicitly (no... | [Paid, self-serve](../gates/paid.md) |
| [Apollo.io](../tools/apollo-io.md)
apollo.io | [Official MCP](../mcp/official.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | OAuth (Apollo.io sign-in/authorization flow in the client) | [Paid, self-serve](../gates/paid.md) |
| [Brand24](../tools/brand24.md)
brand24.com | [Official MCP](../mcp/official.md) | [https://mcp.brand24.com/v1/mcp](https://mcp.brand24.com/v1/mcp) +1 more | OAuth; the help article states "MCP access is available to Brand24 subscribers. The data available in MCP reflects what's in your active projects." | [Paid, self-serve](../gates/paid.md) |
| [CatchIntent](../tools/catchintent.md)
catchintent.com | [Official MCP](../mcp/official.md) | [https://engine.catchintent.com/mcp](https://engine.catchintent.com/mcp) +2 more | oauth. The vendor's MCP page states "One-time OAuth 2.1 authorization. Your MCP client opens a browser, you sign into CatchIntent, pick the... | [Paid, self-serve](../gates/paid.md) |
| [Circleback](../tools/circleback.md)
circleback.ai | [Official MCP](../mcp/official.md) | [https://circleback.ai/api/mcp](https://circleback.ai/api/mcp) +2 more | OAuth with dynamic client registration, compliant with the authenticated remote MCP spec. Centrally hosted and managed by Circleback. | [Paid, self-serve](../gates/paid.md) |
| [Coresignal](../tools/coresignal.md)
coresignal.com | [Official MCP](../mcp/official.md) | [https://mcp.coresignal.com/mcp/v2](https://mcp.coresignal.com/mcp/v2) +2 more | OAuth 2.1 - per docs, the data key is fetched live with every request and never stored, allowing instant revocation | [Paid, self-serve](../gates/paid.md) |
| [Cube Software](../tools/cube-software.md)
cubesoftware.com | [Official MCP](../mcp/official.md) | [https://mcp.cubesoftware.com/](https://mcp.cubesoftware.com/) +2 more | OAuth - no manual API key management. | [Paid, self-serve](../gates/paid.md) |
| [DocuSign](../tools/docusign.md)
docusign.com | [Official MCP](../mcp/official.md) | [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/) +2 more | OAuth - Streamable HTTP transport; first connection opens a browser window to sign in and authorize, then reuses credentials. | [Paid, self-serve](../gates/paid.md) |
| [Fellow](../tools/fellow.md)
fellow.ai | [Official MCP](../mcp/official.md) | [https://fellow.app/mcp](https://fellow.app/mcp) +1 more | OAuth, with OAuth 2.0 dynamic discovery supported. | [Paid, self-serve](../gates/paid.md) |
| [Front](../tools/front.md)
front.com | [Official MCP](../mcp/official.md) | [https://mcp.frontapp.com/mcp](https://mcp.frontapp.com/mcp) +1 more | OAuth 2.1 with PKCE, per teammate. Front's docs state the server does not support Dynamic Client Registration, so the AI client must be able to send... | [Paid, self-serve](../gates/paid.md) |
| [Grain](../tools/grain.md)
grain.com | [Official MCP](../mcp/official.md) | [https://api.grain.com/_/mcp](https://api.grain.com/_/mcp) +1 more | OAuth via the native Claude integration, or manual server-URL setup for other MCP clients. Deal and coaching-feedback tools specifically require a... | [Paid, self-serve](../gates/paid.md) |
| [Granola](../tools/granola.md)
granola.ai | [Official MCP](../mcp/official.md) | [https://www.pulsemcp.com/servers/granola](https://www.pulsemcp.com/servers/granola) +2 more | OAuth - no manual API key required. | [Paid, self-serve](../gates/paid.md) |
| [Help Scout](../tools/help-scout.md)
helpscout.com | [Official MCP](../mcp/official.md) | [https://mcp.helpscout.net/mcp](https://mcp.helpscout.net/mcp) +1 more | oauth. The vendor's article states the connector registers itself, so the OAuth client ID and secret fields in the AI client are left empty, and... | [Paid, self-serve](../gates/paid.md) |
| [Hex](../tools/hex.md)
hex.tech | [Official MCP](../mcp/official.md) | [https://app.hex.tech/mcp](https://app.hex.tech/mcp) +1 more | oauth. The docs state "Complete the OAuth flow to authorize access to your Hex workspace"; no token path is documented. "Hex MCP server is currently... | [Paid, self-serve](../gates/paid.md) |
| [HeyGen](../tools/heygen.md)
heygen.com | [Official MCP](../mcp/official.md) | [https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/) +2 more | OAuth - vendor states "connect your HeyGen account, no API key required"; generation draws down the premium credits already in the user's HeyGen plan... | [Paid, self-serve](../gates/paid.md) |
| [Hootsuite (Social OS)](../tools/hootsuite.md)
hootsuite.com | [Official MCP](../mcp/official.md) | [https://mcp.hootsuite.com/perch](https://mcp.hootsuite.com/perch) +4 more | oauth. The vendor's setup steps end with "Sign in with your Hootsuite workspace when prompted. Authorization is one-time." | [Paid, self-serve](../gates/paid.md) |
| [La Growth Machine](../tools/la-growth-machine.md)
lagrowthmachine.com | [Official MCP](../mcp/official.md) | [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system) +1 more | OAuth - no API key needed; first use opens a browser sign-in directly to the user's La Growth Machine account. | [Paid, self-serve](../gates/paid.md) |
| [LeadIQ](../tools/leadiq.md)
leadiq.com | [Official MCP](../mcp/official.md) | [https://mcp.leadiq.com/mcp](https://mcp.leadiq.com/mcp) +1 more | oauth. The vendor's page states the connector is added from the AI client's connector directory and the user then signs in with LeadIQ credentials to... | [Paid, self-serve](../gates/paid.md) |
| [Mixmax](../tools/mixmax.md)
mixmax.com | [Official MCP](../mcp/official.md) | [https://mcp.mixmax.com/mcp](https://mcp.mixmax.com/mcp) +2 more | OAuth 2.0 authorization code flow, scoped to the connecting user's account. Read-only. | [Paid, self-serve](../gates/paid.md) |
| [Nutshell CRM](../tools/nutshell-crm.md)
nutshell.com | [Official MCP](../mcp/official.md) | [https://app.nutshell.com/mcp](https://app.nutshell.com/mcp) +1 more | oauth. The vendor's article instructs the user to add the server URL as a custom connector, then log in to Nutshell and approve access on a consent... | [Paid, self-serve](../gates/paid.md) |
| [PhantomBuster](../tools/phantombuster.md)
phantombuster.com | [Official MCP](../mcp/official.md) | [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server) +1 more | OAuth - first connection redirects to PhantomBuster sign-in/authorization, then workspace selection. | [Paid, self-serve](../gates/paid.md) |
| [RingCentral App Connect MCP](../tools/ringcentral-app-connect-mcp.md)
ringcentral.com | [Official MCP](../mcp/official.md) | [https://unified-crm-extension.labs.ringcentral.com/m...](https://unified-crm-extension.labs.ringcentral.com/mcp) +3 more | oauth plus a second, separate CRM link. The docs describe a two-layer model: RingCentral identity via OAuth 2.0 or SSO established when the server is... | [Paid, self-serve](../gates/paid.md) |
| [RocketReach](../tools/rocketreach.md)
rocketreach.co | [Official MCP](../mcp/official.md) | [https://rocketreach.co/resources/products/mcp/](https://rocketreach.co/resources/products/mcp/) +1 more | OAuth 2.1, browser-based; ties to your existing RocketReach account and shares its credit pool (no separate API key needed for the official connector) | [Paid, self-serve](../gates/paid.md) |
| [Snov.io](../tools/snov-io.md)
snov.io | [Official MCP](../mcp/official.md) | [https://mcp.snov.io/mcp](https://mcp.snov.io/mcp) +1 more | OAuth - user reviews and approves the connection through their Snov.io account; no raw API key is shared with the AI assistant | [Paid, self-serve](../gates/paid.md) |
| [SparkToro](../tools/sparktoro.md)
sparktoro.com | [Official MCP](../mcp/official.md) | [https://sparktoro.com/mcp](https://sparktoro.com/mcp) +1 more | OAuth (one-click sign-in with an existing SparkToro account); documented to work with Claude Desktop, Claude Code, Cursor, and ChatGPT. | [Paid, self-serve](../gates/paid.md) |
| [Superblocks](../tools/superblocks.md)
superblocks.com | [Official MCP](../mcp/official.md) | [https://api.superblocks.com/mcp](https://api.superblocks.com/mcp) +1 more | unknown - the announcement doesn't specify the auth method; the feature is Enterprise-only, implying an admin/OAuth-gated setup, but this isn't... | [Paid, self-serve](../gates/paid.md) |
| [Typeform](../tools/typeform.md)
typeform.com | [Official MCP](../mcp/official.md) | [https://api.typeform.com/mcp](https://api.typeform.com/mcp) +2 more | oauth. The docs state "Authorization is OAuth 2.0, and your client is prompted on first connect." EU-hosted accounts use different endpoints, and a... | [Paid, self-serve](../gates/paid.md) |
| [Vainu](../tools/vainu.md)
vainu.com | [Official MCP](../mcp/official.md) | [https://mcp.vainu.ai/mcp](https://mcp.vainu.ai/mcp) +2 more | OAuth 2.0 with PKCE, scoped to existing Vainu permissions, but NOT enabled by default. The vendor help centre says it "isn't automatically available... | [Paid, self-serve](../gates/paid.md) |
| [Versium REACH](../tools/versium-reach.md)
versium.com | [Official MCP](../mcp/official.md) | [https://app.versium.com/mcp/reach](https://app.versium.com/mcp/reach) +2 more | OAuth, and the client must support dynamic client registration. | [Paid, self-serve](../gates/paid.md) |
| [Zoho CRM](../tools/zoho-crm.md)
zoho.com | [Official MCP](../mcp/official.md) | [https://www.zoho.com/crm/developer/mcp.html](https://www.zoho.com/crm/developer/mcp.html) | oauth. The vendor's page describes a four-step setup ending in "Authenticate via OAuth. Connect your Zoho CRM account. Your agent inherits your... | [Paid, self-serve](../gates/paid.md) |
| [Amplemarket](../tools/amplemarket.md)
amplemarket.com | [Official MCP](../mcp/official.md) | [https://mcp.amplemarket.com/mcp](https://mcp.amplemarket.com/mcp) +2 more | OAuth 2.0 sign-in with the Amplemarket account in the browser; the knowledge article says no API keys are needed. Rate limit 100 requests per minute... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Dialpad](../tools/dialpad.md)
dialpad.com | [Official MCP](../mcp/official.md) | [https://mcp-public.us.karehq.com/mcp](https://mcp-public.us.karehq.com/mcp) +3 more | oauth. The docs state the server is hosted by Dialpad, supports Dynamic Client Registration so clients register themselves on first connect, acts on... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Paragon (ActionKit MCP)](../tools/paragon.md)
useparagon.com | [Official MCP](../mcp/official.md) | [https://github.com/useparagon/paragon-mcp](https://github.com/useparagon/paragon-mcp) +1 more | Paragon user token plus Connect Portal OAuth. The distinguishing feature is that the authorisation prompt is embedded in the calling product's own... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Sybill](../tools/sybill.md)
sybill.ai | [Official MCP](../mcp/official.md) | [https://mcp.sybill.ai/mcp](https://mcp.sybill.ai/mcp) +1 more | Browser-based sign-in / OAuth on first connection from an MCP client such as Claude Desktop. | [Enterprise leaning](../gates/enterprise-leaning.md) |
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
| [Crunchbase](../tools/crunchbase.md)
crunchbase.com | [Official MCP](../mcp/official.md) | [https://mcp.crunchbase.com](https://mcp.crunchbase.com) +2 more | OAuth 2.1. The user signs in with their normal Crunchbase account in the AI client's browser flow; Crunchbase then checks that the account holds an... | [Enterprise only](../gates/enterprise-only.md) |
| [G2 Buyer Intent](../tools/g2-buyer-intent.md)
g2.com | [Official MCP](../mcp/official.md) | [https://mcp.g2.com/mcp](https://mcp.g2.com/mcp) +2 more | OAuth 2.0 Authorization Code with PKCE. You register an OAuth app in the G2 Developer Dashboard at https://my.g2.com/developers to get a client_id... | [Enterprise only](../gates/enterprise-only.md) |
| [Looker](../tools/looker.md)
cloud.google.com | [Official MCP](../mcp/official.md) | [https://docs.cloud.google.com/looker/docs/mcp](https://docs.cloud.google.com/looker/docs/mcp) +3 more | The managed server uses OAuth 2.1 and an admin "must manually register AI agents as OAuth clients via the API Explorer"; all tools are "disabled by... | [Enterprise only](../gates/enterprise-only.md) |
| [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md)
turbomcp.ai | [Official MCP](../mcp/official.md) | [https://github.com/dylibso/mcp.run-servlets](https://github.com/dylibso/mcp.run-servlets) +1 more | Integrates with a team's own OIDC-compatible identity provider; handles OAuth and Dynamic Client Registration for the servers it fronts. | [Enterprise only](../gates/enterprise-only.md) |
| [Nooks](../tools/nooks.md)
nooks.ai | [Official MCP](../mcp/official.md) | [https://mcp.nooks.in/mcp](https://mcp.nooks.in/mcp) +1 more | OAuth 2.0 authorization code with PKCE (S256), issuer https://oauth.nooks.in, per the server's own /.well-known/oauth-authorization-server metadata;... | [Enterprise only](../gates/enterprise-only.md) |
| [Outreach](../tools/outreach.md)
outreach.ai | [Official MCP](../mcp/official.md) | [https://api.outreach.io/mcp/](https://api.outreach.io/mcp/) +1 more | OAuth 2.1 with Dynamic Client Registration; also requires the org-level "Amplify" add-on to be enabled and admin-toggled - not available to every... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md)
salesforce.com | [Official MCP](../mcp/official.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) +2 more | OAuth + PKCE via an External Client App (scopes mcp_api, refresh_token); every MCP call runs under the authenticated user's own permissions... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesloft](../tools/salesloft.md)
salesloft.com | [Official MCP](../mcp/official.md) | [https://mcp.salesloft.com/mcp](https://mcp.salesloft.com/mcp) +2 more | unknown exact flow - vendor press material describes it as natively listed in Claude's connector directory "with no custom setup required," implying... | [Enterprise only](../gates/enterprise-only.md) |
| [Showpad](../tools/showpad.md)
showpad.com | [Official MCP](../mcp/official.md) | [https://mcp.showpad.com/mcp/v1](https://mcp.showpad.com/mcp/v1) +2 more | OAuth; the docs say each end user authenticates with their own Showpad credentials and can only search and retrieve content they are already... | [Enterprise only](../gates/enterprise-only.md) |
| [Actively](../tools/actively.md)
actively.ai | [Official MCP](../mcp/official.md) | [https://app.actively.ai/docs/mcp](https://app.actively.ai/docs/mcp) +2 more | oauth. The vendor docs state "MCP access uses OAuth 2.1 with WorkOS." Tools are read-only: "Public tools are read-only, non-destructive, idempotent,... | [Gate unknown](../gates/unknown.md) |
| [Pylon](../tools/pylon.md)
usepylon.com | [Official MCP](../mcp/official.md) | [https://mcp.usepylon.com](https://mcp.usepylon.com) +1 more | OAuth 2.0 over stateless streamable HTTP; access is permission-scoped so a connected AI tool can only see/change what the authenticated user could... | [Gate unknown](../gates/unknown.md) |
| [Trumpet](../tools/trumpet.md)
sendtrumpet.com | [Official MCP](../mcp/official.md) | [https://trumpet.app/api/mcp](https://trumpet.app/api/mcp) +2 more | OAuth 2.0 - vendor help-center doc confirms "Authenticate via trumpet (OAuth 2.0)"; setup flow is add-custom-connector → paste MCP server URL →... | [Gate unknown](../gates/unknown.md) |
| [Bonjoro](../tools/bonjoro.md)
bonjoro.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro) | Rides a Zapier account connection (OAuth to Zapier, which holds the Bonjoro-side connection). | [Paid, self-serve](../gates/paid.md) |
| [Loopio](../tools/loopio.md)
loopio.com | [Community MCP](../mcp/community.md) | [https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp) | OAuth2 client credentials (Client ID and Secret from the Loopio admin panel) against the Loopio Data API v2, per the repo README; runs locally over... | [Enterprise only](../gates/enterprise-only.md) |

Counted 2026-09-11 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 336 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
