# GTM MCP servers that accept OAuth or an API key: 45 tools, counted

> 45 of the 165 GTM tools with an MCP server use OAuth or an API key. The verbatim auth field for each one is printed beside it. Counted 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers that accept OAuth or an API key

**List · 45 of 293**

## GTM MCP servers that accept OAuth or an API key

Both paths are documented. Usually OAuth for a hosted server and a key for the self hosted or legacy endpoint. The bucket is a keyword match over the mcp_auth field, run at build time, and the verbatim field ships in the row beside it so you can check the parse yourself. Where the two disagree, the verbatim field is the fact and the bucket is the convenience.

| Tool | MCP status | Server URL | mcp_auth, verbatim | Gate |
|---|---|---|---|---|
| [Airbyte](../tools/airbyte.md)
airbyte.com | [Official MCP](../mcp/official.md) | [https://docs.airbyte.com/ai-agents/interfaces/mcp](https://docs.airbyte.com/ai-agents/interfaces/mcp) | Two-layer OAuth 2.0 - OAuth into the Airbyte account/org for the MCP server itself, plus separate OAuth or API-key auth per connected third-party... | [Free to start](../gates/free.md) |
| [Anymail Finder](../tools/anymail-finder.md)
anymailfinder.com | [Official MCP](../mcp/official.md) | [https://api.anymailfinder.com/mcp](https://api.anymailfinder.com/mcp) +1 more | Browser-based OAuth-style sign-in and approval for Claude, ChatGPT and Cursor, with an API key fallback for clients that cannot do browser sign-in. | [Free to start](../gates/free.md) |
| [Apideck](../tools/apideck.md)
apideck.com | [Official MCP](../mcp/official.md) | [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp) +1 more | Managed OAuth via Apideck Vault on the hosted endpoint, or x-apideck-api-key plus x-apideck-app-id plus x-apideck-consumer-id headers for direct use. | [Free to start](../gates/free.md) |
| [Cal.com](../tools/cal-com.md)
cal.com | [Official MCP](../mcp/official.md) | [https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp) +1 more | Two paths. Hosted server (mcp.cal.com) uses OAuth 2.1 - "your client handles the authorization flow automatically," no API key needed.... | [Free to start](../gates/free.md) |
| [Calendly](../tools/calendly.md)
calendly.com | [Official MCP](../mcp/official.md) | [https://developer.calendly.com/calendly-mcp-server](https://developer.calendly.com/calendly-mcp-server) +3 more | OAuth 2.1 Authorization Code + PKCE (S256) with Dynamic Client Registration (RFC 7591). Personal access tokens are not supported. Fully hosted by... | [Free to start](../gates/free.md) |
| [Composio](../tools/composio.md)
composio.dev | [Official MCP](../mcp/official.md) | [https://docs.composio.dev/mcp/overview](https://docs.composio.dev/mcp/overview) | Composio brokers OAuth for each connected toolkit (HubSpot, Gmail, Slack, etc.) on the user's behalf, then gates the MCP endpoint itself with an... | [Free to start](../gates/free.md) |
| [Fireflies.ai](../tools/fireflies-ai.md)
fireflies.ai | [Official MCP](../mcp/official.md) | [https://guide.fireflies.ai/articles/8272956938-learn...](https://guide.fireflies.ai/articles/8272956938-learn-about-the-fireflies-mcp-server-model-context-protocol) +1 more | OAuth (Google/Microsoft, recommended) or manual API key for Claude Desktop and other MCP clients. | [Free to start](../gates/free.md) |
| [LeadMagic](../tools/leadmagic.md)
leadmagic.io | [Official MCP](../mcp/official.md) | [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp) +1 more | api key for local/self-hosted install (LEADMAGIC_API_KEY env var); OAuth Bearer token (Clerk-issued) for the hosted remote MCP - hosted version does... | [Free to start](../gates/free.md) |
| [MeetGeek](../tools/meetgeek.md)
meetgeek.ai | [Official MCP](../mcp/official.md) | [https://mcp.meetgeek.ai/mcp](https://mcp.meetgeek.ai/mcp) +2 more | Two paths. The cloud server uses OAuth 2.0 with Google or Microsoft sign-in and no API key. The self-hosted server runs locally on Node.js and... | [Free to start](../gates/free.md) |
| [Prospeo](../tools/prospeo.md)
prospeo.io | [Official MCP](../mcp/official.md) | [https://github.com/prospeo-v2/prospeo-mcp-server](https://github.com/prospeo-v2/prospeo-mcp-server) | OAuth 2.0 for the hosted server (auto-handled by Claude.ai/Desktop via the MCP directory); local/self-hosted setup uses an API key via... | [Free to start](../gates/free.md) |
| [Tavus](../tools/tavus.md)
tavus.io | [Official MCP](../mcp/official.md) | [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp) +3 more | OAuth 2.0 browser-based flow; the exchange mints a per-user API key server-side, nothing stored in client config. | [Free to start](../gates/free.md) |
| [Warmly](../tools/warmly.md)
warmly.ai | [Official MCP](../mcp/official.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | OAuth for the MCP connector; API key for the REST API | [Free to start](../gates/free.md) |
| [Warmly (Warmly.ai)](../tools/warmly.md)
warmly.ai | [Official MCP](../mcp/official.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | MCP uses OAuth-based login (no manual key management); the separate REST API (opps-api.getwarmly.com) uses a per-organization API key. | [Free to start](../gates/free.md) |
| [Zapier](../tools/zapier.md)
zapier.com | [Official MCP](../mcp/official.md) | [https://zapier.com/mcp](https://zapier.com/mcp) +1 more | Reuses Zapier's existing 13+ year credential infrastructure - connect an AI client (Claude, ChatGPT, Cursor) through a guided ~5-minute flow that... | [Free to start](../gates/free.md) |
| [Affinity](../tools/affinity.md)
affinity.co | [Official MCP](../mcp/official.md) | [https://mcp.affinity.co/mcp](https://mcp.affinity.co/mcp) +1 more | OAuth where the client supports it, otherwise an API key. Local deployment is API key only. All MCP queries inherit the connecting user's existing... | [Paid, self-serve](../gates/paid.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Official MCP](../mcp/official.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper Edge API key, generated by an admin in Command Center and... | [Paid, self-serve](../gates/paid.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Official MCP](../mcp/official.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper Edge API key, generated by an admin in Command Center and... | [Paid, self-serve](../gates/paid.md) |
| [Close (Close CRM)](../tools/close.md)
close.com | [Official MCP](../mcp/official.md) | [https://help.close.com/docs/mcp-server](https://help.close.com/docs/mcp-server) +1 more | Dual - OAuth 2.0 with Dynamic Client Registration (recommended; used by Claude, ChatGPT, Cursor) or API-key auth via custom headers (Close-API-Key,... | [Paid, self-serve](../gates/paid.md) |
| [Dropcontact](../tools/dropcontact.md)
dropcontact.com | [Official MCP](../mcp/official.md) | [https://www.dropcontact.com/mcp-dropcontact](https://www.dropcontact.com/mcp-dropcontact) | Hosted server at mcp.dropcontact.com/mcp/, supporting OAuth (recommended, browser-based) or a Dropcontact API token/key passed via headers; also... | [Paid, self-serve](../gates/paid.md) |
| [Fiber AI](../tools/fiber-ai.md)
fiber.ai | [Official MCP](../mcp/official.md) | [https://mcp.fiber.ai/mcp/v3](https://mcp.fiber.ai/mcp/v3) +2 more | OAuth via Clerk on the v3 endpoint; x-api-key header on the v2 and legacy endpoints. | [Paid, self-serve](../gates/paid.md) |
| [HeyReach](../tools/heyreach.md)
heyreach.io | [Official MCP](../mcp/official.md) | [https://www.heyreach.io/mcp](https://www.heyreach.io/mcp) +1 more | workspace-scoped "MCP key" + connection URL (API-key-style, not OAuth) | [Paid, self-serve](../gates/paid.md) |
| [Intercom (Fin)](../tools/intercom.md)
intercom.com | [Official MCP](../mcp/official.md) | [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp) +2 more | OAuth (browser-based, recommended) or a Bearer token using an Intercom API token; Streamable HTTP transport, 13 exposed tools covering conversations,... | [Paid, self-serve](../gates/paid.md) |
| [lemlist](../tools/lemlist.md)
lemlist.com | [Official MCP](../mcp/official.md) | [https://developer.lemlist.com/mcp/setup](https://developer.lemlist.com/mcp/setup) +1 more | OAuth (browser-based PKCE flow, recommended) or API key via X-API-Key header | [Paid, self-serve](../gates/paid.md) |
| [Make](../tools/make.md)
make.com | [Official MCP](../mcp/official.md) | [https://developers.make.com/mcp-server](https://developers.make.com/mcp-server) | Two supported methods - OAuth via Make's cloud (endpoint mcp.make.com) or an MCP Token generated from the user's Make profile, sent as a Bearer token... | [Paid, self-serve](../gates/paid.md) |
| [Metorial](../tools/metorial.md)
metorial.com | [Official MCP](../mcp/official.md) | [https://metorial.com](https://metorial.com) | Fully custodial - Metorial stores and centrally manages OAuth tokens for every connected integration ("no tokens to manage" for the end user), with... | [Paid, self-serve](../gates/paid.md) |
| [Octave](../tools/octave.md)
octavehq.com | [Official MCP](../mcp/official.md) | [https://docs.octavehq.com/mcp/overview](https://docs.octavehq.com/mcp/overview) +3 more | Browser OAuth. Per the vendor's Claude Code setup doc you add the server with "claude mcp add octave-myWorkspace --transport http... | [Paid, self-serve](../gates/paid.md) |
| [Pipedream MCP](../tools/pipedream-mcp.md)
pipedream.com | [Official MCP](../mcp/official.md) | [https://mcp.pipedream.com](https://mcp.pipedream.com) | OAuth/API-key credentials for each underlying app are stored by Pipedream and isolated per end user; Pipedream states credentials are "never exposed... | [Paid, self-serve](../gates/paid.md) |
| [The Swarm](../tools/the-swarm.md)
theswarm.com | [Official MCP](../mcp/official.md) | [https://bee.theswarm.com/mcp](https://bee.theswarm.com/mcp) +1 more | OAuth via personal Swarm login (native Claude and ChatGPT app connectors) or team API key via x-api-key header for any MCP client supporting custom... | [Paid, self-serve](../gates/paid.md) |
| [Waalaxy](../tools/waalaxy.md)
waalaxy.com | [Official MCP](../mcp/official.md) | [https://docs.waalaxy.com/mcp-server](https://docs.waalaxy.com/mcp-server) +1 more | user-based OAuth 2.1 via magic-link sign-in; vendor docs explicitly state bearer API keys are NOT supported by the MCP server (differs from the... | [Paid, self-serve](../gates/paid.md) |
| [Wiza](../tools/wiza.md)
wiza.co | [Official MCP](../mcp/official.md) | [https://mcp.wiza.co/mcp](https://mcp.wiza.co/mcp) +2 more | OAuth 2.1 with PKCE for clients that support it, otherwise a static bearer token in the Authorization header using a Wiza API key. Streamable HTTP... | [Paid, self-serve](../gates/paid.md) |
| [Woodpecker](../tools/woodpecker.md)
woodpecker.co | [Official MCP](../mcp/official.md) | [https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/) +1 more | hosted OAuth-style flow (Claude-specific) or self-hosted Docker setup using a Woodpecker API key | [Paid, self-serve](../gates/paid.md) |
| [Anaplan (PlanIQ / Anaplan Forecaster)](../tools/anaplan.md)
anaplan.com | [Official MCP](../mcp/official.md) | [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/) | unknown - described only as a "governed MCP connection" with permission/audit controls; the specific credential mechanism (API key vs. OAuth) is not... | [Enterprise only](../gates/enterprise-only.md) |
| [Default](../tools/default.md)
default.com | [Official MCP](../mcp/official.md) | [https://www.default.com/product/platform](https://www.default.com/product/platform) | unknown - not specified on the public page (plausibly API key or OAuth given CRM-grade data access, but unconfirmed) | [Enterprise only](../gates/enterprise-only.md) |
| [Seamless.AI](../tools/seamless-ai.md)
seamless.ai | [Official MCP](../mcp/official.md) | [https://docs.seamless.ai/mcp-docs](https://docs.seamless.ai/mcp-docs) +1 more | OAuth 2.1 or API key; docs state "MCP access must be enabled on your account" - i.e. gated per-account, contact admin/support to turn on | [Enterprise only](../gates/enterprise-only.md) |
| [Seismic](../tools/seismic.md)
seismic.com | [Official MCP](../mcp/official.md) | [https://developer.seismic.com/seismicsoftware/docs/s...](https://developer.seismic.com/seismicsoftware/docs/seismic-mcp-server) | Streamable HTTP transport per Seismic's MCP documentation; the specific credential type (API key vs. OAuth) was not confirmed in the sources reviewed. | [Enterprise only](../gates/enterprise-only.md) |
| [Similarweb](../tools/similarweb.md)
similarweb.com | [Official MCP](../mcp/official.md) | [https://mcp.similarweb.com](https://mcp.similarweb.com) +3 more | CONFLICTING VENDOR STATEMENTS, flagged rather than resolved. Both Similarweb developer docs pages state an active Similarweb API key from Account... | [Enterprise only](../gates/enterprise-only.md) |
| [Syncari](../tools/syncari.md)
syncari.com | [Official MCP](../mcp/official.md) | [https://syncari.com/mcp-server/](https://syncari.com/mcp-server/) | unknown - the MCP server page describes real-time, entity/field-level access control and audit logging but does not state whether connection auth is... | [Enterprise only](../gates/enterprise-only.md) |
| [UserGems](../tools/usergems.md)
usergems.com | [Official MCP](../mcp/official.md) | [https://www.usergems.com/product/mcp](https://www.usergems.com/product/mcp) | unknown - connects inside Claude/ChatGPT per the product page, but the exact auth mechanism (OAuth vs. API key) isn't disclosed publicly. | [Enterprise only](../gates/enterprise-only.md) |
| [Endgame](../tools/endgame.md)
endgame.io | [Official MCP](../mcp/official.md) | [https://docs.endgame.io/features/mcp-server](https://docs.endgame.io/features/mcp-server) +1 more | OAuth (browser-based) for individual users via Claude/ChatGPT/Claude Code/Codex connectors; Bearer-token service-account API keys (issued at... | [Gate unknown](../gates/unknown.md) |
| [Reclaim.ai](../tools/reclaim-ai.md)
reclaim.ai | [Official MCP](../mcp/official.md) | [https://mcp.reclaim.ai](https://mcp.reclaim.ai) | OAuth (official hosted server). A separate unofficial/community server also exists (github.com/universalamateur/reclaim-mcp-server, explicitly marked... | [Gate unknown](../gates/unknown.md) |
| [Zoom Revenue Accelerator](../tools/zoom-revenue-accelerator.md)
zoom.com | [Official MCP](../mcp/official.md) | [https://news.zoom.com/zoom-revenue-accelerator-mcp-c...](https://news.zoom.com/zoom-revenue-accelerator-mcp-connector/) +1 more | OAuth - Zoom user-level OAuth access token (env var ZOOM_REVENUE_ACCELERATOR_MCP_ACCESS_TOKEN), plus an OpenAI Codex plugin variant. | [Gate unknown](../gates/unknown.md) |
| [Clari Copilot](../tools/clari-copilot.md)
clari.com | [Community MCP](../mcp/community.md) | [https://www.scalekit.com/connectors/claricopilot](https://www.scalekit.com/connectors/claricopilot) +1 more | Scalekit-hosted connector uses per-user delegated OAuth-style authorization in Scalekit's own token vault. The underlying Clari Copilot REST API... | [Paid, self-serve](../gates/paid.md) |
| [UpLead](../tools/uplead.md)
uplead.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/uplead](https://zapier.com/mcp/uplead) +1 more | Handled through the Zapier/Pipedream platform's own connector auth (API key entered into that third-party platform), not a UpLead-native OAuth or... | [Paid, self-serve](../gates/paid.md) |
| [BombBomb](../tools/bombbomb.md)
bombbomb.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom) | Rides Zapier's own OAuth/API-key connection to BombBomb; not a native BombBomb MCP auth flow. | [Enterprise only](../gates/enterprise-only.md) |
| [Jiminny](../tools/jiminny.md)
jiminny.com | [Community MCP](../mcp/community.md) | [https://glama.ai/mcp/servers/@fzheng0222/jiminny-mcp](https://glama.ai/mcp/servers/@fzheng0222/jiminny-mcp) +1 more | Community server: JIMINNY_TOKEN API token. Zapier's hosted connector uses Zapier's own OAuth layer. | [Enterprise only](../gates/enterprise-only.md) |

Counted 2026-08-25 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
