# GTM MCP servers that accept OAuth or an API key: 68 tools, counted

> 68 of the 437 GTM tools with an MCP server use OAuth or an API key. The verbatim auth field for each one is printed beside it. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers that accept OAuth or an API key

**List · 68 of 934**

## GTM MCP servers that accept OAuth or an API key

Both paths are documented. Usually OAuth for a hosted server and a key for the self hosted or legacy endpoint. The bucket is a keyword match over the mcp_auth field, run at build time, and the verbatim field ships in the row beside it so you can check the parse yourself. Where the two disagree, the verbatim field is the fact and the bucket is the convenience.

| Tool | MCP status | Server URL | mcp_auth, verbatim | Gate |
|---|---|---|---|---|
| [Airbyte](../tools/airbyte.md)
airbyte.com | [Official MCP](../mcp/official.md) | [https://mcp.airbyte.ai/mcp](https://mcp.airbyte.ai/mcp) +1 more | Two-layer OAuth 2.0 - OAuth into the Airbyte account/org for the MCP server itself, plus separate OAuth or API-key auth per connected third-party... | [Free to start](../gates/free.md) |
| [Anymail Finder](../tools/anymail-finder.md)
anymailfinder.com | [Official MCP](../mcp/official.md) | [https://api.anymailfinder.com/mcp](https://api.anymailfinder.com/mcp) +1 more | Browser-based OAuth-style sign-in and approval for Claude, ChatGPT and Cursor, with an API key fallback for clients that cannot do browser sign-in. | [Free to start](../gates/free.md) |
| [Apideck](../tools/apideck.md)
apideck.com | [Official MCP](../mcp/official.md) | [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp) +1 more | Managed OAuth via Apideck Vault on the hosted endpoint, or x-apideck-api-key plus x-apideck-app-id plus x-apideck-consumer-id headers for direct use. | [Free to start](../gates/free.md) |
| [Apify](../tools/apify.md)
apify.com | [Official MCP](../mcp/official.md) | [https://mcp.apify.com](https://mcp.apify.com) +1 more | oauth (recommended, browser sign-in) or an Apify API token as an Authorization Bearer header. The docs state "The Apify MCP server accepts requests... | [Free to start](../gates/free.md) |
| [Cal.com](../tools/cal-com.md)
cal.com | [Official MCP](../mcp/official.md) | [https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp) +1 more | Two paths. Hosted server (mcp.cal.com) uses OAuth 2.1 - "your client handles the authorization flow automatically," no API key needed.... | [Free to start](../gates/free.md) |
| [Calendly](../tools/calendly.md)
calendly.com | [Official MCP](../mcp/official.md) | [https://mcp.calendly.com](https://mcp.calendly.com) +3 more | OAuth 2.1 Authorization Code + PKCE (S256) with Dynamic Client Registration (RFC 7591). Personal access tokens are not supported. Fully hosted by... | [Free to start](../gates/free.md) |
| [Composio](../tools/composio.md)
composio.dev | [Official MCP](../mcp/official.md) | [https://connect.composio.dev/mcp](https://connect.composio.dev/mcp) +2 more | Composio brokers OAuth for each connected toolkit (HubSpot, Gmail, Slack, etc.) on the user's behalf, then gates the MCP endpoint itself with an... | [Free to start](../gates/free.md) |
| [Fathom](../tools/fathom.md)
fathom.video | [Official MCP](../mcp/official.md) | [https://developers.fathom.ai/mcp-docs](https://developers.fathom.ai/mcp-docs) +4 more | In-client authorization: the docs say to add the server URL "then authenticate to access your meeting data", via the Fathom connector in Claude... | [Free to start](../gates/free.md) |
| [Firecrawl](../tools/firecrawl.md)
firecrawl.dev | [Official MCP](../mcp/official.md) | [https://mcp.firecrawl.dev/v2/mcp](https://mcp.firecrawl.dev/v2/mcp) +4 more | api key as an Authorization Bearer header, or browser sign-in via the /v2/mcp-oauth variant, or keyless with daily limits. The vendor docs state... | [Free to start](../gates/free.md) |
| [Fireflies.ai](../tools/fireflies-ai.md)
fireflies.ai | [Official MCP](../mcp/official.md) | [https://api.fireflies.ai/mcp](https://api.fireflies.ai/mcp) +1 more | OAuth (Google/Microsoft, recommended) or manual API key for Claude Desktop and other MCP clients. | [Free to start](../gates/free.md) |
| [Google BigQuery](../tools/google-bigquery.md)
cloud.google.com | [Official MCP](../mcp/official.md) | [https://bigquery.googleapis.com/mcp](https://bigquery.googleapis.com/mcp) +1 more | oauth. The docs state the server uses the "OAuth 2.0 protocol with IAM for authentication and authorization", supports "all Google Cloud identities"... | [Free to start](../gates/free.md) |
| [Jotform](../tools/jotform.md)
jotform.com | [Official MCP](../mcp/official.md) | [https://mcp.jotform.com](https://mcp.jotform.com) +2 more | oauth only. The vendor's MCP page states "Bearer-token access is not supported; OAuth 2.0 is required for all connections." Rate limits by plan: "60... | [Free to start](../gates/free.md) |
| [LeadMagic](../tools/leadmagic.md)
leadmagic.io | [Official MCP](../mcp/official.md) | [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp) +1 more | api key for local/self-hosted install (LEADMAGIC_API_KEY env var); OAuth Bearer token (Clerk-issued) for the hosted remote MCP - hosted version does... | [Free to start](../gates/free.md) |
| [MeetGeek](../tools/meetgeek.md)
meetgeek.ai | [Official MCP](../mcp/official.md) | [https://mcp.meetgeek.ai/mcp](https://mcp.meetgeek.ai/mcp) +2 more | Two paths. The cloud server uses OAuth 2.0 with Google or Microsoft sign-in and no API key. The self-hosted server runs locally on Node.js and... | [Free to start](../gates/free.md) |
| [Merge Agent Handler](../tools/merge-agent-handler.md)
merge.dev | [Official MCP](../mcp/official.md) | [https://github.com/merge-api/merge-mcp](https://github.com/merge-api/merge-mcp) +3 more | api key in an Authorization Bearer header, alongside the identity encoded in the URL itself. The docs are explicit that three values are needed on... | [Free to start](../gates/free.md) |
| [monday.com (monday CRM)](../tools/monday-com.md)
monday.com | [Official MCP](../mcp/official.md) | [https://mcp.monday.com/mcp](https://mcp.monday.com/mcp) +3 more | oauth for the remote server. The vendor states "monday MCP remote server connects via the secure OAuth protocol" and that an admin must first install... | [Free to start](../gates/free.md) |
| [Prospeo](../tools/prospeo.md)
prospeo.io | [Official MCP](../mcp/official.md) | [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server) | OAuth 2.0 for the hosted server (auto-handled by Claude.ai/Desktop via the MCP directory); local/self-hosted setup uses an API key via... | [Free to start](../gates/free.md) |
| [StackOne](../tools/stackone.md)
stackone.com | [Official MCP](../mcp/official.md) | [https://mcp.stackone.com/mcp](https://mcp.stackone.com/mcp) +2 more | Basic authentication plus a per-account identifier, with StackOne brokering OAuth, API keys and token refresh to each connected application on the... | [Free to start](../gates/free.md) |
| [Tally](../tools/tally.md)
tally.so | [Official MCP](../mcp/official.md) | [https://api.tally.so/mcp](https://api.tally.so/mcp) +2 more | oauth or api key. The help page states "The easiest way to connect is through OAuth, just click 'Connect' and follow the prompts. If you prefer, you... | [Free to start](../gates/free.md) |
| [Tavily](../tools/tavily.md)
tavily.com | [Official MCP](../mcp/official.md) | [https://mcp.tavily.com/mcp/](https://mcp.tavily.com/mcp/) +1 more | api key as a tavilyApiKey query parameter or in the Authorization header, or OAuth. The docs state "OAuth authentication is optional, you can still... | [Free to start](../gates/free.md) |
| [Tavus](../tools/tavus.md)
tavus.io | [Official MCP](../mcp/official.md) | [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp) +3 more | OAuth 2.0 browser-based flow; the exchange mints a per-user API key server-side, nothing stored in client config. | [Free to start](../gates/free.md) |
| [usefulapi.io](../tools/usefulapi-io.md)
usefulapi.io | [Official MCP](../mcp/official.md) | [https://pipedrive.usefulapi.io/mcp](https://pipedrive.usefulapi.io/mcp) +3 more | per-application OAuth. The setup instructions add the subdomain as a custom connector and the user then authenticates with the wrapped vendor when... | [Free to start](../gates/free.md) |
| [Warmly](../tools/warmly.md)
warmly.ai | [Official MCP](../mcp/official.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | OAuth for the MCP connector; API key for the REST API | [Free to start](../gates/free.md) |
| [Warmly (Warmly.ai)](../tools/warmly.md)
warmly.ai | [Official MCP](../mcp/official.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | MCP uses OAuth-based login (no manual key management); the separate REST API (opps-api.getwarmly.com) uses a per-organization API key. | [Free to start](../gates/free.md) |
| [Wistia](../tools/wistia.md)
wistia.com | [Official MCP](../mcp/official.md) | [https://api.wistia.com/mcp/api](https://api.wistia.com/mcp/api) +1 more | oauth or an access token as an Authorization Bearer header. The docs state "If you use an access token you need to add the Authorization: Bearer... | [Free to start](../gates/free.md) |
| [Zapier](../tools/zapier.md)
zapier.com | [Official MCP](../mcp/official.md) | [https://mcp.zapier.com/api/v1/connect](https://mcp.zapier.com/api/v1/connect) +3 more | Reuses Zapier's existing 13+ year credential infrastructure - connect an AI client (Claude, ChatGPT, Cursor) through a guided ~5-minute flow that... | [Free to start](../gates/free.md) |
| [Affinity](../tools/affinity.md)
affinity.co | [Official MCP](../mcp/official.md) | [https://mcp.affinity.co/mcp](https://mcp.affinity.co/mcp) +1 more | OAuth where the client supports it, otherwise an API key. Local deployment is API key only. All MCP queries inherit the connecting user's existing... | [Paid, self-serve](../gates/paid.md) |
| [Attention](../tools/attention.md)
attention.com | [Official MCP](../mcp/official.md) | [https://docs.attention.com/mcp/overview](https://docs.attention.com/mcp/overview) +1 more | oauth for end users, api key for programmatic access, per https://docs.attention.com/mcp/authentication read 2026-08-28. | [Paid, self-serve](../gates/paid.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Official MCP](../mcp/official.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper Edge API key, generated by an admin in Command Center and... | [Paid, self-serve](../gates/paid.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Official MCP](../mcp/official.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper Edge API key, generated by an admin in Command Center and... | [Paid, self-serve](../gates/paid.md) |
| [Clari Copilot](../tools/clari-copilot.md)
clari.com | [Official MCP](../mcp/official.md) | [https://mcp.clari.com/mcp](https://mcp.clari.com/mcp) +2 more | Scalekit-hosted connector uses per-user delegated OAuth-style authorization in Scalekit's own token vault. The underlying Clari Copilot REST API... | [Paid, self-serve](../gates/paid.md) |
| [Close (Close CRM)](../tools/close.md)
close.com | [Official MCP](../mcp/official.md) | [https://mcp.close.com/mcp](https://mcp.close.com/mcp) +1 more | Dual - OAuth 2.0 with Dynamic Client Registration (recommended; used by Claude, ChatGPT, Cursor) or API-key auth via custom headers (Close-API-Key,... | [Paid, self-serve](../gates/paid.md) |
| [dbt (dbt platform remote MCP)](../tools/dbt.md)
getdbt.com | [Official MCP](../mcp/official.md) | [https://YOUR_DBT_HOST_URL/api/ai/v1/mcp](https://YOUR_DBT_HOST_URL/api/ai/v1/mcp) +3 more | oauth (beta) or token. The docs state "OAuth lets you connect to the remote MCP server without copying API tokens into your MCP client" and limit... | [Paid, self-serve](../gates/paid.md) |
| [Dropcontact](../tools/dropcontact.md)
dropcontact.com | [Official MCP](../mcp/official.md) | [https://mcp.dropcontact.com/mcp](https://mcp.dropcontact.com/mcp) +1 more | Hosted server at mcp.dropcontact.com/mcp/, supporting OAuth (recommended, browser-based) or a Dropcontact API token/key passed via headers; also... | [Paid, self-serve](../gates/paid.md) |
| [Fiber AI](../tools/fiber-ai.md)
fiber.ai | [Official MCP](../mcp/official.md) | [https://mcp.fiber.ai/mcp/v3](https://mcp.fiber.ai/mcp/v3) +2 more | OAuth via Clerk on the v3 endpoint; x-api-key header on the v2 and legacy endpoints. | [Paid, self-serve](../gates/paid.md) |
| [HeyReach](../tools/heyreach.md)
heyreach.io | [Official MCP](../mcp/official.md) | [https://mcp.heyreach.io/mcp](https://mcp.heyreach.io/mcp) +2 more | workspace-scoped "MCP key" + connection URL (API-key-style, not OAuth) | [Paid, self-serve](../gates/paid.md) |
| [Intercom (Fin)](../tools/intercom.md)
intercom.com | [Official MCP](../mcp/official.md) | [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp) +2 more | OAuth (browser-based, recommended) or a Bearer token using an Intercom API token; Streamable HTTP transport, 13 exposed tools covering conversations,... | [Paid, self-serve](../gates/paid.md) |
| [Keyplay](../tools/keyplay.md)
keyplay.io | [Official MCP](../mcp/official.md) | [https://api.keyplay.io/mcp](https://api.keyplay.io/mcp) +1 more | OAuth for Claude.ai and Claude Desktop, API key for Claude Code, per the vendor's docs | [Paid, self-serve](../gates/paid.md) |
| [lemlist](../tools/lemlist.md)
lemlist.com | [Official MCP](../mcp/official.md) | [https://app.lemlist.com/mcp](https://app.lemlist.com/mcp) +1 more | OAuth (browser-based PKCE flow, recommended) or API key via X-API-Key header | [Paid, self-serve](../gates/paid.md) |
| [Make](../tools/make.md)
make.com | [Official MCP](../mcp/official.md) | [https://mcp.make.com](https://mcp.make.com) +2 more | Two supported methods - OAuth via Make's cloud (endpoint mcp.make.com) or an MCP Token generated from the user's Make profile, sent as a Bearer token... | [Paid, self-serve](../gates/paid.md) |
| [Metorial](../tools/metorial.md)
metorial.com | [Official MCP](../mcp/official.md) | [https://github.com/metorial/metorial](https://github.com/metorial/metorial) +1 more | Fully custodial - Metorial stores and centrally manages OAuth tokens for every connected integration ("no tokens to manage" for the end user), with... | [Paid, self-serve](../gates/paid.md) |
| [Octave](../tools/octave.md)
octavehq.com | [Official MCP](../mcp/official.md) | [https://docs.octavehq.com/mcp/overview](https://docs.octavehq.com/mcp/overview) +3 more | Browser OAuth. Per the vendor's Claude Code setup doc you add the server with "claude mcp add octave-myWorkspace --transport http... | [Paid, self-serve](../gates/paid.md) |
| [Pipedream MCP](../tools/pipedream-mcp.md)
pipedream.com | [Official MCP](../mcp/official.md) | [https://mcp.pipedream.com](https://mcp.pipedream.com) | OAuth/API-key credentials for each underlying app are stored by Pipedream and isolated per end user; Pipedream states credentials are "never exposed... | [Paid, self-serve](../gates/paid.md) |
| [Reply.io (Jason AI)](../tools/reply-io.md)
reply.io | [Official MCP](../mcp/official.md) | [https://reply.io/mcp/](https://reply.io/mcp/) +2 more | Personal API key (vendor-recommended, sent as a Bearer token, scoped to the permissions the key allows) or OAuth (used by the Claude connector;... | [Paid, self-serve](../gates/paid.md) |
| [Saleshandy](../tools/saleshandy.md)
saleshandy.com | [Official MCP](../mcp/official.md) | [https://mcp.saleshandy.com/mcp](https://mcp.saleshandy.com/mcp) +3 more | oauth, with an api key fallback. The developer docs state "Saleshandy MCP uses OAuth for authentication - no API key needed for most clients" and... | [Paid, self-serve](../gates/paid.md) |
| [SalesQL](../tools/salesql.md)
salesql.com | [Official MCP](../mcp/official.md) | [https://mcp.salesql.com/mcp](https://mcp.salesql.com/mcp) +2 more | oauth. The vendor's docs record "Auth OAuth 2.1" with an MCP key as the fallback for clients that cannot carry the OAuth flow. | [Paid, self-serve](../gates/paid.md) |
| [Skyp.ai](../tools/skyp-ai.md)
skyp.ai | [Official MCP](../mcp/official.md) | [https://api.skyp.ai/mcp](https://api.skyp.ai/mcp) +3 more | api key (X-API-Key or Authorization Bearer header) or OAuth. The endpoint's own 401 body reads "Missing credentials. Use X-API-Key or Authorization:... | [Paid, self-serve](../gates/paid.md) |
| [The Swarm](../tools/the-swarm.md)
theswarm.com | [Official MCP](../mcp/official.md) | [https://bee.theswarm.com/mcp](https://bee.theswarm.com/mcp) +1 more | OAuth via personal Swarm login (native Claude and ChatGPT app connectors) or team API key via x-api-key header for any MCP client supporting custom... | [Paid, self-serve](../gates/paid.md) |
| [Vayne](../tools/vayne.md)
vayne.io | [Official MCP](../mcp/official.md) | [https://mcp.vayne.io/mcp](https://mcp.vayne.io/mcp) +1 more | oauth or api key. The vendor's docs state OAuth is the default for Claude Desktop, Claude.ai, Claude Code and Cursor (server URL only, no token... | [Paid, self-serve](../gates/paid.md) |
| [Waalaxy](../tools/waalaxy.md)
waalaxy.com | [Official MCP](../mcp/official.md) | [https://docs.waalaxy.com/mcp-server](https://docs.waalaxy.com/mcp-server) +1 more | user-based OAuth 2.1 via magic-link sign-in; vendor docs explicitly state bearer API keys are NOT supported by the MCP server (differs from the... | [Paid, self-serve](../gates/paid.md) |
| [Wiza](../tools/wiza.md)
wiza.co | [Official MCP](../mcp/official.md) | [https://mcp.wiza.co/mcp](https://mcp.wiza.co/mcp) +2 more | OAuth 2.1 with PKCE for clients that support it, otherwise a static bearer token in the Authorization header using a Wiza API key. Streamable HTTP... | [Paid, self-serve](../gates/paid.md) |
| [Woodpecker](../tools/woodpecker.md)
woodpecker.co | [Official MCP](../mcp/official.md) | [https://github.com/Woodpeckerco/woodpecker-mcp-serve...](https://github.com/Woodpeckerco/woodpecker-mcp-server) +2 more | hosted OAuth-style flow (Claude-specific) or self-hosted Docker setup using a Woodpecker API key | [Paid, self-serve](../gates/paid.md) |
| [Harmonic](../tools/harmonic.md)
harmonic.ai | [Official MCP](../mcp/official.md) | [https://mcp.api.harmonic.ai](https://mcp.api.harmonic.ai) +1 more | oauth. The server publishes OAuth protected-resource metadata at https://mcp.api.harmonic.ai/.well-known/oauth-protected-resource declaring itself as... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Anaplan (PlanIQ / Anaplan Forecaster)](../tools/anaplan.md)
anaplan.com | [Official MCP](../mcp/official.md) | [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/) +1 more | unknown - described only as a "governed MCP connection" with permission/audit controls; the specific credential mechanism (API key vs. OAuth) is not... | [Enterprise only](../gates/enterprise-only.md) |
| [Meltwater](../tools/meltwater.md)
meltwater.com | [Official MCP](../mcp/official.md) | [https://developer.meltwater.com/guides/meltwater-mcp...](https://developer.meltwater.com/guides/meltwater-mcp/overview/) +1 more | Meltwater API token today, "with OAuth 2.0 planned for later this year" per the vendor docs; access requires a Meltwater MCP package in the... | [Enterprise only](../gates/enterprise-only.md) |
| [Seamless.AI](../tools/seamless-ai.md)
seamless.ai | [Official MCP](../mcp/official.md) | [https://mcp.seamless.ai/mcp](https://mcp.seamless.ai/mcp) +1 more | OAuth 2.1 or API key; docs state "MCP access must be enabled on your account" - i.e. gated per-account, contact admin/support to turn on | [Enterprise only](../gates/enterprise-only.md) |
| [Seismic](../tools/seismic.md)
seismic.com | [Official MCP](../mcp/official.md) | [https://mcp.seismic.com/](https://mcp.seismic.com/) +1 more | Streamable HTTP transport per Seismic's MCP documentation; the specific credential type (API key vs. OAuth) was not confirmed in the sources reviewed. | [Enterprise only](../gates/enterprise-only.md) |
| [Similarweb](../tools/similarweb.md)
similarweb.com | [Official MCP](../mcp/official.md) | [https://mcp.similarweb.com](https://mcp.similarweb.com) +3 more | CONFLICTING VENDOR STATEMENTS, flagged rather than resolved. Both Similarweb developer docs pages state an active Similarweb API key from Account... | [Enterprise only](../gates/enterprise-only.md) |
| [Syncari](../tools/syncari.md)
syncari.com | [Official MCP](../mcp/official.md) | [https://mcp.syncari.com/mcp](https://mcp.syncari.com/mcp) +1 more | unknown - the MCP server page describes real-time, entity/field-level access control and audit logging but does not state whether connection auth is... | [Enterprise only](../gates/enterprise-only.md) |
| [UserGems](../tools/usergems.md)
usergems.com | [Official MCP](../mcp/official.md) | [https://www.usergems.com/product/mcp](https://www.usergems.com/product/mcp) | unknown - connects inside Claude/ChatGPT per the product page, but the exact auth mechanism (OAuth vs. API key) isn't disclosed publicly. | [Enterprise only](../gates/enterprise-only.md) |
| [Endgame](../tools/endgame.md)
endgame.io | [Official MCP](../mcp/official.md) | [https://app.endgame.io/api/v1/mcp](https://app.endgame.io/api/v1/mcp) +1 more | OAuth (browser-based) for individual users via Claude/ChatGPT/Claude Code/Codex connectors; Bearer-token service-account API keys (issued at... | [Gate unknown](../gates/unknown.md) |
| [Klavis AI](../tools/klavis-ai.md)
klavis.ai | [Official MCP](../mcp/official.md) | [https://www.klavis.ai/docs/concepts/strata.md](https://www.klavis.ai/docs/concepts/strata.md) +2 more | Klavis API key as an HTTP Bearer token on the management API that creates a per-user Strata server... | [Gate unknown](../gates/unknown.md) |
| [Reclaim.ai](../tools/reclaim-ai.md)
reclaim.ai | [Official MCP](../mcp/official.md) | [https://mcp.reclaim.ai](https://mcp.reclaim.ai) | OAuth (official hosted server). A separate unofficial/community server also exists (github.com/universalamateur/reclaim-mcp-server, explicitly marked... | [Gate unknown](../gates/unknown.md) |
| [Zoom Revenue Accelerator](../tools/zoom-revenue-accelerator.md)
zoom.com | [Official MCP](../mcp/official.md) | [https://news.zoom.com/zoom-revenue-accelerator-mcp-c...](https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/) +1 more | OAuth - Zoom user-level OAuth access token (env var ZOOM_REVENUE_ACCELERATOR_MCP_ACCESS_TOKEN), plus an OpenAI Codex plugin variant. | [Gate unknown](../gates/unknown.md) |
| [Aircall](../tools/aircall.md)
aircall.io | [Community MCP](../mcp/community.md) | [https://github.com/themobilefirstco/aircall-mcp-serv...](https://github.com/themobilefirstco/aircall-mcp-server) +1 more | api key. The community server takes an Aircall API ID and API token, which the public API checks as HTTP Basic auth ("The api_id is the username and... | [Paid, self-serve](../gates/paid.md) |
| [UpLead](../tools/uplead.md)
uplead.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/uplead](https://zapier.com/mcp/uplead) +1 more | Handled through the Zapier/Pipedream platform's own connector auth (API key entered into that third-party platform), not a UpLead-native OAuth or... | [Paid, self-serve](../gates/paid.md) |
| [BombBomb](../tools/bombbomb.md)
bombbomb.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom) | Rides Zapier's own OAuth/API-key connection to BombBomb; not a native BombBomb MCP auth flow. | [Enterprise only](../gates/enterprise-only.md) |
| [Jiminny](../tools/jiminny.md)
jiminny.com | [Community MCP](../mcp/community.md) | [https://mcp.jiminny.com/mcp](https://mcp.jiminny.com/mcp) +3 more | Community server: JIMINNY_TOKEN API token. Zapier's hosted connector uses Zapier's own OAuth layer. | [Enterprise only](../gates/enterprise-only.md) |

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 934 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
