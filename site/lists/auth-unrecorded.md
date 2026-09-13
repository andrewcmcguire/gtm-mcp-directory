# GTM MCP servers with no auth model recorded: 324 tools, counted

> 324 of the 521 GTM tools with an MCP server use an auth model that is not recorded. The verbatim auth field for each one is printed beside it. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers with no auth model recorded

**List · 324 of 1,032**

## GTM MCP servers with no auth model recorded

The mcp_auth field on the entry is blank, or says unknown. Published as blank rather than guessed. The bucket is a keyword match over the mcp_auth field, run at build time, and the verbatim field ships in the row beside it so you can check the parse yourself. Where the two disagree, the verbatim field is the fact and the bucket is the convenience.

| Tool | MCP status | Server URL | mcp_auth, verbatim | Gate |
|---|---|---|---|---|
| [Common Paper](../tools/common-paper.md)
commonpaper.com | [Official MCP](../mcp/official.md) | [https://api.commonpaper.com/mcp](https://api.commonpaper.com/mcp) +2 more | unknown - not detailed in the release-notes excerpt reviewed. | [Free to start](../gates/free.md) |
| [Crustdata](../tools/crustdata.md)
crustdata.com | [Official MCP](../mcp/official.md) | [https://install.crustdata.com/mcp](https://install.crustdata.com/mcp) +1 more | unknown | [Free to start](../gates/free.md) |
| [Hightouch](../tools/hightouch.md)
hightouch.com | [Official MCP](../mcp/official.md) | [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp) | Existing Hightouch workspace auth with role-based access control; however the MCP server itself "must be enabled by Hightouch - contact us to turn it... | [Free to start](../gates/free.md) |
| [Pipeworx](../tools/pipeworx.md)
pipeworx.io | [Official MCP](../mcp/official.md) | [https://gateway.pipeworx.io/mcp](https://gateway.pipeworx.io/mcp) +4 more | none required for the free tiers. The vendor states "No API keys" and that an anonymous client gets 50 tool calls a day on the full catalogue; a free... | [Free to start](../gates/free.md) |
| [TheirStack](../tools/theirstack.md)
theirstack.com | [Official MCP](../mcp/official.md) | [https://api.theirstack.com/mcp/](https://api.theirstack.com/mcp/) +1 more | unknown - page references a "How does authentication work?" FAQ but the answer wasn't visible in the fetched content; requires free signup/login to... | [Free to start](../gates/free.md) |
| [Amplemarket (Duo Copilot)](../tools/amplemarket.md)
amplemarket.com | [Official MCP](../mcp/official.md) | [https://mcp.amplemarket.com/mcp](https://mcp.amplemarket.com/mcp) +2 more | Account sign-in (no API key needed) - "sign in with your Amplemarket account when prompted" | [Paid, self-serve](../gates/paid.md) |
| [Arphie](../tools/arphie.md)
arphie.ai | [Official MCP](../mcp/official.md) | referenced via pricing/product pages describing an "Arphie... | unknown | [Paid, self-serve](../gates/paid.md) |
| [Maildoso](../tools/maildoso.md)
maildoso.ai | [Official MCP](../mcp/official.md) | [https://maildoso.ai/](https://maildoso.ai/) | unknown - described only as "API and MCP access" bundled into every plan, without a documented auth mechanism in sourced pages. | [Paid, self-serve](../gates/paid.md) |
| [Microsoft Dynamics 365 Sales](../tools/microsoft-dynamics-365-sales.md)
microsoft.com | [Official MCP](../mcp/official.md) | [https://agent365.svc.cloud.microsoft/mcp/environment...](https://agent365.svc.cloud.microsoft/mcp/environments/) +1 more | enterprise gate. Microsoft Entra identity; the documented prerequisites are admin permissions in Dynamics 365 Sales, admin permissions in Copilot... | [Paid, self-serve](../gates/paid.md) |
| [Ortto](../tools/ortto.md)
ortto.com | [Official MCP](../mcp/official.md) | [https://mcp-api-us.ortto.app/mcp](https://mcp-api-us.ortto.app/mcp) +1 more | A scoped JWT key created as an MCP data source inside the Ortto account, passed as a "jwt" query parameter on the URL. | [Paid, self-serve](../gates/paid.md) |
| [Responsive (formerly RFPIO)](../tools/responsive.md)
responsive.io | [Official MCP](../mcp/official.md) | [https://www.responsive.io/capability/mcp-server](https://www.responsive.io/capability/mcp-server) +2 more | unknown - not detailed in the sources reviewed. | [Paid, self-serve](../gates/paid.md) |
| [Salesforge (Agent Frank)](../tools/salesforge.md)
salesforge.ai | [Official MCP](../mcp/official.md) | [https://mcp.salesforge.ai/mcp](https://mcp.salesforge.ai/mcp) +2 more | unknown specifics (help article confirms an official MCP server "to connect with AI assistants" alongside API and CLI access, but exact auth flow not... | [Paid, self-serve](../gates/paid.md) |
| [Snitcher](../tools/snitcher.md)
snitcher.com | [Official MCP](../mcp/official.md) | [https://app.snitcher.com/mcp/snitcher](https://app.snitcher.com/mcp/snitcher) +1 more | unknown - vendor changelog points to docs.snitcher.com for authentication specifics, not independently confirmed. | [Paid, self-serve](../gates/paid.md) |
| [Sumble](../tools/sumble.md)
sumble.com | [Official MCP](../mcp/official.md) | [https://mcp.sumble.com/](https://mcp.sumble.com/) +3 more | unknown - the MCP overview page documents one-click install from the Claude and ChatGPT app directories and a custom MCP connection for Cursor,... | [Paid, self-serve](../gates/paid.md) |
| [Clari](../tools/clari.md)
clari.com | [Official MCP](../mcp/official.md) | [https://mcp.clari.com/mcp](https://mcp.clari.com/mcp) +1 more | unknown / not disclosed publicly | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Ada](../tools/ada.md)
ada.cx | [Official MCP](../mcp/official.md) | [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server) +1 more | none documented - connects over HTTP with no credential requirement described in the docs. | [Enterprise only](../gates/enterprise-only.md) |
| [Artisan AI (Ava)](../tools/artisan-ai.md)
artisan.co | [Official MCP](../mcp/official.md) | [https://www.artisan.co/mcp](https://www.artisan.co/mcp) | none required - a JSON-RPC initialize POST to the endpoint with no credentials answered HTTP 200 on 2026-09-02 (serverInfo name "artisan-content",... | [Enterprise only](../gates/enterprise-only.md) |
| [Clari (+ Salesloft agents)](../tools/clari.md)
clari.com | [Official MCP](../mcp/official.md) | [https://mcp.clari.com/mcp](https://mcp.clari.com/mcp) +1 more | unknown - announcement confirms an official MCP server (works with Claude, ChatGPT, Microsoft Copilot, Gemini, and Salesforce Agentforce) but does... | [Enterprise only](../gates/enterprise-only.md) |
| [Demandbase (Demandbase One)](../tools/demandbase.md)
demandbase.com | [Official MCP](../mcp/official.md) | [https://developer.demandbase.com/docs/mcp](https://developer.demandbase.com/docs/mcp) +1 more | unknown - the account-team-gated support article that likely covers this returned HTTP 403 and could not be read; docs confirm the MCP is read-only... | [Enterprise only](../gates/enterprise-only.md) |
| [Gong](../tools/gong.md)
gong.io | [Official MCP](../mcp/official.md) | [https://help.gong.io/docs/about-gong-mcp](https://help.gong.io/docs/about-gong-mcp) +2 more | Official MCP client+server ships as part of Gong's enterprise agent stack (used to connect Microsoft 365 Copilot, Salesforce, etc.); community... | [Enterprise only](../gates/enterprise-only.md) |
| [Highspot](../tools/highspot.md)
highspot.com | [Official MCP](../mcp/official.md) | [https://mcp.highspot.com/mcp](https://mcp.highspot.com/mcp) +1 more | unknown - product page describes agent-to-agent access via OpenAI, Anthropic, and Microsoft Copilot integrations but does not detail the underlying... | [Enterprise only](../gates/enterprise-only.md) |
| [Ironclad](../tools/ironclad.md)
ironcladapp.com | [Official MCP](../mcp/official.md) | [https://support.ironcladapp.com/hc/en-us/articles/39...](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server) +1 more | unknown - a single, static MCP endpoint per the support article; specific credential mechanism not detailed in the sources reviewed. | [Enterprise only](../gates/enterprise-only.md) |
| [Otter.ai](../tools/otter-ai.md)
otter.ai | [Official MCP](../mcp/official.md) | [https://mcp.otter.ai/mcp](https://mcp.otter.ai/mcp) +3 more | unknown - exact auth mechanism not confirmed in public sources; framed under "Otter for Enterprise" with a demo-request CTA. | [Enterprise only](../gates/enterprise-only.md) |
| [Pigment](../tools/pigment.md)
pigment.com | [Official MCP](../mcp/official.md) | [https://www.pigment.com/ai/mcp-server](https://www.pigment.com/ai/mcp-server) +2 more | A workspace admin enables MCP under Settings > Integrations, generating a per-workspace endpoint; individual users then connect with their existing... | [Enterprise only](../gates/enterprise-only.md) |
| [Talkwalker (rebranded: Lumen by Talkwalker)](../tools/talkwalker.md)
talkwalker.com | [Official MCP](../mcp/official.md) | [https://mcp.hootsuite.com/lumen](https://mcp.hootsuite.com/lumen) +1 more | Sign in with a Hootsuite workspace when prompted; the Hootsuite MCP page says authorization is one-time. | [Enterprise only](../gates/enterprise-only.md) |
| [Unify](../tools/unify.md)
unifygtm.com | [Community MCP](../mcp/community.md) | [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp) | Auth0 browser sign-in (auth.unifygtm.com); MCP caches the session cookie (~30-day life) rather than a refresh token - no password or key ever passed... | [Paid, self-serve](../gates/paid.md) |
| [Brandwatch](../tools/brandwatch.md)
brandwatch.com | [Community MCP](../mcp/community.md) | [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch) | unknown - the third-party server's description states it interfaces with "the Brandwatch Consumer Research, Data Upload and Analysis APIs," hosted on... | [Enterprise only](../gates/enterprise-only.md) |
| [DealHub (DealHub AI)](../tools/dealhub.md)
dealhub.io | [Community MCP](../mcp/community.md) | [https://www.pulsemcp.com/servers/vishvick-dealhub-ad...](https://www.pulsemcp.com/servers/vishvick-dealhub-admin) | unknown - stdio transport run locally against the customer's own DealHub instance per the npm description; credential mechanism not read | [Enterprise only](../gates/enterprise-only.md) |
| [0nmcp](../tools/0nmcp.md)
0nmcp.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [abm.dev](../tools/abm-dev.md)
abm.dev | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=sales) | blank | [Gate unknown](../gates/unknown.md) |
| [Accelo MCP by Selerity](../tools/accelo-mcp-by-selerity.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Selerity/accelo-mcp](https://github.com/Selerity/accelo-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [ActiveCampaign MCP by pipeworx](../tools/activecampaign-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-activecampaign](https://github.com/pipeworx-io/mcp-activecampaign) | blank | [Gate unknown](../gates/unknown.md) |
| [Adrata](../tools/adrata.md)
adrata.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Agentled](../tools/agentled.md)
agentled.app | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | blank | [Gate unknown](../gates/unknown.md) |
| [amoCRM MCP by theYahia](../tools/amocrm-mcp-by-theyahia.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/theYahia/amocrm-mcp](https://github.com/theYahia/amocrm-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [AmpUp GTM Chat](../tools/ampup-gtm-chat.md)
chat.ampup.ai | [Community MCP](../mcp/community.md) | [https://github.com/A79-ai/gtm-agentic-chat](https://github.com/A79-ai/gtm-agentic-chat) | blank | [Gate unknown](../gates/unknown.md) |
| [Anyquery](../tools/anyquery.md)
anyquery.dev | [Community MCP](../mcp/community.md) | [https://github.com/julien040/anyquery](https://github.com/julien040/anyquery) | blank | [Gate unknown](../gates/unknown.md) |
| [Apex Log MCP by Certinia](../tools/apex-log-mcp-by-certinia.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://github.com/certinia/debug-log-analyzer-mcp](https://github.com/certinia/debug-log-analyzer-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Apex MCP SDK by bfmvsa](../tools/apex-mcp-sdk-by-bfmvsa.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/bfmvsa/mcp-apex-sdk](https://github.com/bfmvsa/mcp-apex-sdk) | blank | [Gate unknown](../gates/unknown.md) |
| [Apify Actors MCP](../tools/apify-actors-mcp.md)
mcp.apify.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo Agent CLI by bcharleson](../tools/apollo-agent-cli-by-bcharleson.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/bcharleson/apollo-agent-cli](https://github.com/bcharleson/apollo-agent-cli) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by AgenTeam](../tools/apollo-mcp-by-agenteam.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/AgenTeam-AI-2026/mcp-apollo](https://github.com/AgenTeam-AI-2026/mcp-apollo) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by BlockchainRev](../tools/apollo-mcp-by-blockchainrev.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/BlockchainRev/apollo-mcp-server](https://github.com/BlockchainRev/apollo-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by Eden-Anthony](../tools/apollo-mcp-by-eden-anthony.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Eden-Anthony/apollo-mcp](https://github.com/Eden-Anthony/apollo-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by fuzzylabs](../tools/apollo-mcp-by-fuzzylabs.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/fuzzylabs/apollo-mcp](https://github.com/fuzzylabs/apollo-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by Inferensys](../tools/apollo-mcp-by-inferensys.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Inferensys/apollo-io-mcp](https://github.com/Inferensys/apollo-io-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by kingler](../tools/apollo-mcp-by-kingler.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/kingler/apollo-io-mcp-server](https://github.com/kingler/apollo-io-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by louis030195](../tools/apollo-mcp-by-louis030195.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by maxmulvey](../tools/apollo-mcp-by-maxmulvey.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/maxmulvey/apollo-mcp](https://github.com/maxmulvey/apollo-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by mayanksingh09](../tools/apollo-mcp-by-mayanksingh09.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mayanksingh09/apollo-io-mcp-serve...](https://github.com/mayanksingh09/apollo-io-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by shariqriazz](../tools/apollo-mcp-by-shariqriazz.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/shariqriazz/apollo-io-mcp-server](https://github.com/shariqriazz/apollo-io-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by wmarceau](../tools/apollo-mcp-by-wmarceau.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/MarceauSolutions/dev-sandbox](https://github.com/MarceauSolutions/dev-sandbox) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP Plugin by apolloio](../tools/apollo-mcp-plugin-by-apolloio.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | blank | [Gate unknown](../gates/unknown.md) |
| [Apollo.io CLI by dipankar](../tools/apollo-io-cli-by-dipankar.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/dipankar/apollo-io-cli](https://github.com/dipankar/apollo-io-cli) | blank | [Gate unknown](../gates/unknown.md) |
| [Artefact MCP](../tools/artefact-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/artefactventures/artefact-mcp-ser...](https://github.com/artefactventures/artefact-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [AstroFabric MCP](../tools/astrofabric-mcp.md)
astrofabric.ai | [Community MCP](../mcp/community.md) | [https://github.com/sam1siam/astrofabric-mcp](https://github.com/sam1siam/astrofabric-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Attio MCP by Arkel-ai](../tools/attio-mcp-by-arkel-ai.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Arkel-ai/attio-mcp-server](https://github.com/Arkel-ai/attio-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Attio MCP by hmk](../tools/attio-mcp-by-hmk.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [AU BizIntel MCP](../tools/au-bizintel-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/ljdigital/au-bizintel-mcp](https://github.com/ljdigital/au-bizintel-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [B2B Enrichment MCP by Aleksey-Panf](../tools/b2b-enrichment-mcp-by-aleksey-panf.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Bavlio](../tools/bavlio.md)
bavlio.com | [Community MCP](../mcp/community.md) | [https://github.com/Bavlio/bavlio-mcp](https://github.com/Bavlio/bavlio-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [BD Desk MCP by iaj6](../tools/bd-desk-mcp-by-iaj6.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/iaj6/bd-desk](https://github.com/iaj6/bd-desk) | blank | [Gate unknown](../gates/unknown.md) |
| [Bitrix24 MCP by john7ross](../tools/bitrix24-mcp-by-john7ross.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/john7ross/BitrixMCP](https://github.com/john7ross/BitrixMCP) | blank | [Gate unknown](../gates/unknown.md) |
| [Bitrix24 MCP by theYahia](../tools/bitrix24-mcp-by-theyahia.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/theYahia/bitrix24-mcp](https://github.com/theYahia/bitrix24-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Blitz API Open Source](../tools/blitz-api-open-source.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/malharlakdawala/blitzapi-opensour...](https://github.com/malharlakdawala/blitzapi-opensource) | blank | [Gate unknown](../gates/unknown.md) |
| [BNI MCP by alexaltovate](../tools/bni-mcp-by-alexaltovate.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/alexaltovate/bni-mcp](https://github.com/alexaltovate/bni-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Brand Intel MCP](../tools/brand-intel-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/FoundryNet/brand-intel-mcp](https://github.com/FoundryNet/brand-intel-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Bytemine MCP](../tools/bytemine-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/kzarov/bytemine-bytemine-mcp](https://github.com/kzarov/bytemine-bytemine-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by MonadsAG](../tools/capsule-crm-mcp-by-monadsag.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by soil-dev](../tools/capsule-crm-mcp-by-soil-dev.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Chatflow](../tools/chatflow.md)
chatflow.biz | [Community MCP](../mcp/community.md) | [https://github.com/Yersat/chatflow-mcp](https://github.com/Yersat/chatflow-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [CiviCRM MCP by YogiAdhik](../tools/civicrm-mcp-by-yogiadhik.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/YogiAdhik/civicrm-mcp](https://github.com/YogiAdhik/civicrm-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Clay MCP by bpw-civic](../tools/clay-mcp-by-bpw-civic.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/bpw-civic/clay-mcp-server](https://github.com/bpw-civic/clay-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Clay MCP by shanefirek](../tools/clay-mcp-by-shanefirek.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/shanefirek/clay-mcp-public](https://github.com/shanefirek/clay-mcp-public) | blank | [Gate unknown](../gates/unknown.md) |
| [Clay to Instantly/Smartlead MCP](../tools/clay-to-instantly-smartlead-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mambalabsdev/mcp-clay-to-instantl...](https://github.com/mambalabsdev/mcp-clay-to-instantly-smartlead-push) | blank | [Gate unknown](../gates/unknown.md) |
| [Clint CRM MCP by Franky-Neto](../tools/clint-crm-mcp-by-franky-neto.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Franky-Neto/mcp-clint-crm](https://github.com/Franky-Neto/mcp-clint-crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Close CRM MCP by pipeworx](../tools/close-crm-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-close-crm](https://github.com/pipeworx-io/mcp-close-crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Codex Data MCP](../tools/codex-data-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Cognis Coldforge MCP](../tools/cognis-coldforge-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/cognis-digital/coldforge](https://github.com/cognis-digital/coldforge) | blank | [Gate unknown](../gates/unknown.md) |
| [Cognis CRM Sync MCP](../tools/cognis-crm-sync-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/cognis-digital/crmsync](https://github.com/cognis-digital/crmsync) | blank | [Gate unknown](../gates/unknown.md) |
| [Cognis Dealflow MCP](../tools/cognis-dealflow-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/cognis-digital/dealflow](https://github.com/cognis-digital/dealflow) | blank | [Gate unknown](../gates/unknown.md) |
| [Cognis Enrichr MCP](../tools/cognis-enrichr-mcp.md)
cognis.digital | [Community MCP](../mcp/community.md) | [https://github.com/cognis-digital/enrichr](https://github.com/cognis-digital/enrichr) | blank | [Gate unknown](../gates/unknown.md) |
| [Cognis Leadforge MCP](../tools/cognis-leadforge-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/cognis-digital/leadforge](https://github.com/cognis-digital/leadforge) | blank | [Gate unknown](../gates/unknown.md) |
| [Coldforge](../tools/coldforge.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Makeph/coldforge](https://github.com/Makeph/coldforge) | blank | [Gate unknown](../gates/unknown.md) |
| [Coldstart](../tools/coldstart.md)
coldstart.so | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | blank | [Gate unknown](../gates/unknown.md) |
| [Commercient Data Lake](../tools/commercient-data-lake.md)
commercient.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20hubspot](https://www.npmjs.com/search?q=mcp%20hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [Company Enrichment MCP by sercanmetalore](../tools/company-enrichment-mcp-by-sercanmetalore.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/sercanmetalore/API-MCP](https://github.com/sercanmetalore/API-MCP) | blank | [Gate unknown](../gates/unknown.md) |
| [CompCode MCP](../tools/compcode-mcp.md)
compcode.ai | [Community MCP](../mcp/community.md) | [https://github.com/compcode-ai/mcp](https://github.com/compcode-ai/mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Conduyt](../tools/conduyt.md)
conduyt.app | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Crevideo Reach](../tools/crevideo-reach.md)
crevideo.com | [Community MCP](../mcp/community.md) | [https://github.com/crevideo/crevideo-reach](https://github.com/crevideo/crevideo-reach) | blank | [Gate unknown](../gates/unknown.md) |
| [CrispHive MCP](../tools/crisphive-mcp.md)
docs.crisphive.com | [Community MCP](../mcp/community.md) | [https://github.com/crisphive/crisphive-mcp](https://github.com/crisphive/crisphive-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [CRM AI MCP by MEOK](../tools/crm-ai-mcp-by-meok.md)
meok.ai | [Community MCP](../mcp/community.md) | [https://github.com/CSOAI-ORG/crm-ai-mcp](https://github.com/CSOAI-ORG/crm-ai-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [CRM Bridge MCP](../tools/crm-bridge-mcp.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [CRM Solid MCP](../tools/crm-solid-mcp.md)
docs.crmsolid.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Crustdata MCP](../tools/crustdata-mcp.md)
crustdata.com | [Community MCP](../mcp/community.md) | [https://crustdata.com](https://crustdata.com) | blank | [Gate unknown](../gates/unknown.md) |
| [Curtis LinkedIn MCP](../tools/curtis-linkedin-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/matteolegrottaglie/curtis](https://github.com/matteolegrottaglie/curtis) | blank | [Gate unknown](../gates/unknown.md) |
| [Customer Intelligence Hub](../tools/customer-intelligence-hub.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Gabrielm3/customer-intelligence-h...](https://github.com/Gabrielm3/customer-intelligence-hub) | blank | [Gate unknown](../gates/unknown.md) |
| [DataLayer.sh MCP](../tools/datalayer-sh-mcp.md)
datalayer.sh | [Community MCP](../mcp/community.md) | [https://github.com/datalayer-sh/mcp](https://github.com/datalayer-sh/mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Decern CRM MCP](../tools/decern-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/statwonk/decern](https://github.com/statwonk/decern) | blank | [Gate unknown](../gates/unknown.md) |
| [Diffbot MCP by pipeworx](../tools/diffbot-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-diffbot](https://github.com/pipeworx-io/mcp-diffbot) | blank | [Gate unknown](../gates/unknown.md) |
| [Dolibarr MCP by sachitha7](../tools/dolibarr-mcp-by-sachitha7.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/sachitha7/mcp-server-dolibarr](https://github.com/sachitha7/mcp-server-dolibarr) | blank | [Gate unknown](../gates/unknown.md) |
| [Elizabeth AI Agent](../tools/elizabeth-ai-agent.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/gcarreno-dev/elizabeth-ai-agent](https://github.com/gcarreno-dev/elizabeth-ai-agent) | blank | [Gate unknown](../gates/unknown.md) |
| [Emelia](../tools/emelia.md)
emelia.io | [Community MCP](../mcp/community.md) | [https://github.com/emelia-io/claude-outreach](https://github.com/emelia-io/claude-outreach) | blank | [Gate unknown](../gates/unknown.md) |
| [Entity Enricher MCP](../tools/entity-enricher-mcp.md)
entityenricher.ai | [Community MCP](../mcp/community.md) | [https://github.com/TOT-Concept/mcp-server-entity-enr...](https://github.com/TOT-Concept/mcp-server-entity-enricher) | blank | [Gate unknown](../gates/unknown.md) |
| [Everything Civi MCP](../tools/everything-civi-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/ananda-callhub/everything-civi](https://github.com/ananda-callhub/everything-civi) | blank | [Gate unknown](../gates/unknown.md) |
| [EZ@Work MCP](../tools/ez-work-mcp.md)
ezatwork.com | [Community MCP](../mcp/community.md) | [https://github.com/eranfinish/ezatwork-mcp](https://github.com/eranfinish/ezatwork-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [FavCRM](../tools/favcrm.md)
favcrm.io | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Flipfactory CRM MCP](../tools/flipfactory-crm-mcp.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Fluent MCP Servers](../tools/fluent-mcp-servers.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Dominotypist3077/fluent-mcp-serve...](https://github.com/Dominotypist3077/fluent-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Follow Up Boss MCP](../tools/follow-up-boss-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/theperrygroup/Follow-Up-Boss-MCP](https://github.com/theperrygroup/Follow-Up-Boss-MCP) | blank | [Gate unknown](../gates/unknown.md) |
| [FounderStack CRM](../tools/founderstack-crm.md)
crm-landing-three.vercel.app | [Community MCP](../mcp/community.md) | [https://github.com/Othunderlight/FounderStackCRM-ope...](https://github.com/Othunderlight/FounderStackCRM-open) | blank | [Gate unknown](../gates/unknown.md) |
| [FullEnrich Skills](../tools/fullenrich-skills.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/FullEnrich/fullenrich-skills](https://github.com/FullEnrich/fullenrich-skills) | blank | [Gate unknown](../gates/unknown.md) |
| [Fundz Agent Examples](../tools/fundz-agent-examples.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Fund-z/agent-examples](https://github.com/Fund-z/agent-examples) | blank | [Gate unknown](../gates/unknown.md) |
| [GenPark B2B Lead Waterfall Skill](../tools/genpark-b2b-lead-waterfall-skill.md)
genpark.ai | [Community MCP](../mcp/community.md) | [https://github.com/alphaparkinc/genpark-b2b-lead-wat...](https://github.com/alphaparkinc/genpark-b2b-lead-waterfall-enrichment-cascade-skill) | blank | [Gate unknown](../gates/unknown.md) |
| [GenPark Deal Velocity Skill](../tools/genpark-deal-velocity-skill.md)
genpark.ai | [Community MCP](../mcp/community.md) | [https://github.com/alphaparkinc/genpark-conversation...](https://github.com/alphaparkinc/genpark-conversational-b2b-deal-velocity-scoring-engine-skill) | blank | [Gate unknown](../gates/unknown.md) |
| [GenPark Lead Scoring Skill](../tools/genpark-lead-scoring-skill.md)
genpark.ai | [Community MCP](../mcp/community.md) | [https://github.com/alphaparkinc/genpark-lead-scoring...](https://github.com/alphaparkinc/genpark-lead-scoring-intent-data-enricher-skill) | blank | [Gate unknown](../gates/unknown.md) |
| [GenPark Leads Enrichment Skill](../tools/genpark-leads-enrichment-skill.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/alphaparkinc/genpark-automated-le...](https://github.com/alphaparkinc/genpark-automated-leads-enrichment-skill) | blank | [Gate unknown](../gates/unknown.md) |
| [GenPark Sales Agent MCP](../tools/genpark-sales-agent-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/alphaparkinc/genpark-sales-agent](https://github.com/alphaparkinc/genpark-sales-agent) | blank | [Gate unknown](../gates/unknown.md) |
| [GenPark Waterfall Intent Scoring Skill](../tools/genpark-waterfall-intent-scoring-skill.md)
genpark.ai | [Community MCP](../mcp/community.md) | [https://github.com/alphaparkinc/genpark-waterfall-b2...](https://github.com/alphaparkinc/genpark-waterfall-b2b-lead-enrichment-intent-scoring-skill) | blank | [Gate unknown](../gates/unknown.md) |
| [GlobalSearchData Enrich MCP](../tools/globalsearchdata-enrich-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/globalsearchdata/enrich-mcp-plugi...](https://github.com/globalsearchdata/enrich-mcp-plugin) | blank | [Gate unknown](../gates/unknown.md) |
| [Gmail Outreach MCP by brandononchain](../tools/gmail-outreach-mcp-by-brandononchain.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/brandononchain/gmail-mcp-agent](https://github.com/brandononchain/gmail-mcp-agent) | blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by elitedcs](../tools/gohighlevel-mcp-by-elitedcs.md)
elitedcs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by NightSquawk](../tools/gohighlevel-mcp-by-nightsquawk.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/NightSquawk/gohighlevel-mcp-serve...](https://github.com/NightSquawk/gohighlevel-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by northrosetech](../tools/gohighlevel-mcp-by-northrosetech.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/northrosetech/ghl-mcp-server](https://github.com/northrosetech/ghl-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by rockurbusinesscs](../tools/gohighlevel-mcp-by-rockurbusinesscs.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/rockurbusinesscs-ship-it/gohighle...](https://github.com/rockurbusinesscs-ship-it/gohighlevel-mcp-starter) | blank | [Gate unknown](../gates/unknown.md) |
| [Google Maps Email Extractor MCP](../tools/google-maps-email-extractor-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/the-ai-entrepreneur-ai-hub/google...](https://github.com/the-ai-entrepreneur-ai-hub/google-maps-email-extractor) | blank | [Gate unknown](../gates/unknown.md) |
| [Google Maps Extractor MCP by dppalukuri](../tools/google-maps-extractor-mcp-by-dppalukuri.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/dppalukuri/mcp-google-maps-extrac...](https://github.com/dppalukuri/mcp-google-maps-extractor) | blank | [Gate unknown](../gates/unknown.md) |
| [GTM Alpha MCP](../tools/gtm-alpha-mcp.md)
gtmalpha.netlify.app | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | blank | [Gate unknown](../gates/unknown.md) |
| [GTM Copilot by archanakrishnan](../tools/gtm-copilot-by-archanakrishnan.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/archanakrishnan094-max/AI-GTM-Cop...](https://github.com/archanakrishnan094-max/AI-GTM-Copilot-End-to-End-GTM-Intelligence-CRM-Automation) | blank | [Gate unknown](../gates/unknown.md) |
| [GTM MCP by aleprieto790](../tools/gtm-mcp-by-aleprieto790.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/aleprieto790-alt/gtm-mcp](https://github.com/aleprieto790-alt/gtm-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [GTMos MCP by Kai8karma](../tools/gtmos-mcp-by-kai8karma.md)
kai8karma.github.io | [Community MCP](../mcp/community.md) | [https://github.com/Kai8karma/gtmos-mcp](https://github.com/Kai8karma/gtmos-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Guapu](../tools/guapu.md)
guapu.io | [Community MCP](../mcp/community.md) | [https://guapu.io/conecta-tu-ia](https://guapu.io/conecta-tu-ia) | blank | [Gate unknown](../gates/unknown.md) |
| [Helm AI](../tools/helm-ai.md)
gethelm.ai | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [HireSignal MCP](../tools/hiresignal-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/iusmuchandra/hiresignal-mcp](https://github.com/iusmuchandra/hiresignal-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by amin-ale](../tools/hubspot-mcp-by-amin-ale.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/amin-ale/hubspot-mcp-server](https://github.com/amin-ale/hubspot-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by baryhuang](../tools/hubspot-mcp-by-baryhuang.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/baryhuang/mcp-hubspot](https://github.com/baryhuang/mcp-hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by Devart](../tools/hubspot-mcp-by-devart.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by djmoore-projects](../tools/hubspot-mcp-by-djmoore-projects.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/djmoore-projects/hubspot-mcp-serv...](https://github.com/djmoore-projects/hubspot-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by mindstone-engineering](../tools/hubspot-mcp-by-mindstone-engineering.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by pipeworx](../tools/hubspot-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-hubspot](https://github.com/pipeworx-io/mcp-hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by rfoxes](../tools/hubspot-mcp-by-rfoxes.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [Hunter MCP by scalably](../tools/hunter-mcp-by-scalably.md)
scalably.io | [Community MCP](../mcp/community.md) | [https://github.com/scalably-io/hunter-mcp](https://github.com/scalably-io/hunter-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [IN2 Agent MCP](../tools/in2-agent-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Indraft](../tools/indraft.md)
indraft.io | [Community MCP](../mcp/community.md) | [https://indraft.io](https://indraft.io) | blank | [Gate unknown](../gates/unknown.md) |
| [Infona](../tools/infona.md)
infona.ai | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20enrichment](https://www.npmjs.com/search?q=mcp%20enrichment) | blank | [Gate unknown](../gates/unknown.md) |
| [Infosys AI CRM by ffred1962](../tools/infosys-ai-crm-by-ffred1962.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/ffred1962/infosys](https://github.com/ffred1962/infosys) | blank | [Gate unknown](../gates/unknown.md) |
| [Insaight](../tools/insaight.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/spirosbax/insaight](https://github.com/spirosbax/insaight) | blank | [Gate unknown](../gates/unknown.md) |
| [Intent Outreach](../tools/intent-outreach.md)
demos.intentsolutions.io | [Community MCP](../mcp/community.md) | [https://github.com/jeremylongshore/intent-outreach](https://github.com/jeremylongshore/intent-outreach) | blank | [Gate unknown](../gates/unknown.md) |
| [Iridium LinkedIn Agent](../tools/iridium-linkedin-agent.md)
iridiumhqmcp.com | [Community MCP](../mcp/community.md) | [https://github.com/nikhilkulkarni1755/iridium-linked...](https://github.com/nikhilkulkarni1755/iridium-linkedin-agent) | blank | [Gate unknown](../gates/unknown.md) |
| [JobDataLake MCP](../tools/jobdatalake-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Kaanha AI](../tools/kaanha-ai.md)
kaanha.ai | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Keepsake MCP by nicolascroce](../tools/keepsake-mcp-by-nicolascroce.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Kenva](../tools/kenva.md)
kenva.app | [Community MCP](../mcp/community.md) | [https://kenva.app](https://kenva.app) | blank | [Gate unknown](../gates/unknown.md) |
| [Kordic CRM](../tools/kordic-crm.md)
kordic.io | [Community MCP](../mcp/community.md) | [https://github.com/meelad-diggit/kordic-modelcontext...](https://github.com/meelad-diggit/kordic-modelcontextprotocol.git) | blank | [Gate unknown](../gates/unknown.md) |
| [Lead Enrich MCP by carsonlabs](../tools/lead-enrich-mcp-by-carsonlabs.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/carsonlabs/leadenrich-mcp](https://github.com/carsonlabs/leadenrich-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Lead Radar](../tools/lead-radar.md)
lead-radar.fr | [Community MCP](../mcp/community.md) | [https://lead-radar.fr](https://lead-radar.fr) | blank | [Gate unknown](../gates/unknown.md) |
| [Lead411 MCP](../tools/lead411-mcp.md)
lead411.com | [Community MCP](../mcp/community.md) | [https://lead411.com](https://lead411.com) | blank | [Gate unknown](../gates/unknown.md) |
| [LeadConnector MCP by pipeworx](../tools/leadconnector-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-leadconnector](https://github.com/pipeworx-io/mcp-leadconnector) | blank | [Gate unknown](../gates/unknown.md) |
| [Leadcraft MCP](../tools/leadcraft-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Lakshya330-sudo/leadcraft](https://github.com/Lakshya330-sudo/leadcraft) | blank | [Gate unknown](../gates/unknown.md) |
| [Leadgen MCP by koolninad](../tools/leadgen-mcp-by-koolninad.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/koolninad/leadgen-mcp](https://github.com/koolninad/leadgen-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Leadhound API](../tools/leadhound-api.md)
leadhoundapi.com | [Community MCP](../mcp/community.md) | [https://leadhoundapi.com](https://leadhoundapi.com) | blank | [Gate unknown](../gates/unknown.md) |
| [LeadMagic MCP](../tools/leadmagic-mcp.md)
leadmagic.io | [Community MCP](../mcp/community.md) | [https://github.com/LeadMagic/leadmagic-mcp](https://github.com/LeadMagic/leadmagic-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [LeadOracle MCP](../tools/leadoracle-mcp.md)
tooloracle.io | [Community MCP](../mcp/community.md) | [https://github.com/ToolOracle/leadoracle](https://github.com/ToolOracle/leadoracle) | blank | [Gate unknown](../gates/unknown.md) |
| [Leadpipe MCP](../tools/leadpipe-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/automatiabcn/leadpipe-mcp](https://github.com/automatiabcn/leadpipe-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [LeadScout MCP](../tools/leadscout-mcp.md)
chenagent.dev | [Community MCP](../mcp/community.md) | [https://github.com/alexchenai/leadscout-mcp](https://github.com/alexchenai/leadscout-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Leadzaar](../tools/leadzaar.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Techthos/leadzaar](https://github.com/Techthos/leadzaar) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedGrow](../tools/linkedgrow.md)
linkedgrow.ai | [Community MCP](../mcp/community.md) | [https://github.com/DigiHold/LinkedGrow](https://github.com/DigiHold/LinkedGrow) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn ICP Discovery MCP](../tools/linkedin-icp-discovery-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jpeslar1/linkedin-mcp-icp-discove...](https://github.com/jpeslar1/linkedin-mcp-icp-discovery) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Job Change MCP by jpeslar1](../tools/linkedin-job-change-mcp-by-jpeslar1.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jpeslar1/linkedin-mcp-job-change-...](https://github.com/jpeslar1/linkedin-mcp-job-change-trigger) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Marketing MCP by 1036007003-wq](../tools/linkedin-marketing-mcp-by-1036007003-wq.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/1036007003-wq/linkedin-marketing-...](https://github.com/1036007003-wq/linkedin-marketing-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn MCP by gtm-api](../tools/linkedin-mcp-by-gtm-api.md)
gtm-api.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Outreach MCP by hfarazul](../tools/linkedin-outreach-mcp-by-hfarazul.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/hfarazul/linkedin-outreach-mcp](https://github.com/hfarazul/linkedin-outreach-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Outreach MCP by MEOK](../tools/linkedin-outreach-mcp-by-meok.md)
meok.ai | [Community MCP](../mcp/community.md) | [https://github.com/CSOAI-ORG/linkedin-outreach-mcp](https://github.com/CSOAI-ORG/linkedin-outreach-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedNav](../tools/linkednav.md)
linkednav.com | [Community MCP](../mcp/community.md) | [https://github.com/linglistack/linkednav-mcp](https://github.com/linglistack/linkednav-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkMCP](../tools/linkmcp.md)
app.linkmcp.io | [Community MCP](../mcp/community.md) | [https://github.com/linkmcp-io/linkmcp](https://github.com/linkmcp-io/linkmcp) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkupAPI LinkedIn Skills](../tools/linkupapi-linkedin-skills.md)
linkupapi.com | [Community MCP](../mcp/community.md) | [https://github.com/claude-dev-code/claude-skills-lin...](https://github.com/claude-dev-code/claude-skills-linkedin) | blank | [Gate unknown](../gates/unknown.md) |
| [ListSignal MCP](../tools/listsignal-mcp.md)
listsignal.com | [Community MCP](../mcp/community.md) | [https://github.com/giushansen/listsignal-mcp](https://github.com/giushansen/listsignal-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Little Green Light MCP](../tools/little-green-light-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/WillHeadlee/Little-Green-Light-MC...](https://github.com/WillHeadlee/Little-Green-Light-MCP-Server) | blank | [Gate unknown](../gates/unknown.md) |
| [Livespace CRM MCP](../tools/livespace-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/proAutomator/livespace-crm-mcp](https://github.com/proAutomator/livespace-crm-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Local MCP CRM](../tools/local-mcp-crm.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/bhairavaa/local-mcp-crm](https://github.com/bhairavaa/local-mcp-crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Lookaberry GTM MCP](../tools/lookaberry-gtm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/lucasmartins-ai/lookaberry](https://github.com/lucasmartins-ai/lookaberry) | blank | [Gate unknown](../gates/unknown.md) |
| [Maasy](../tools/maasy.md)
maasy.co | [Community MCP](../mcp/community.md) | [https://github.com/Jbelieve/mcp-server](https://github.com/Jbelieve/mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Magellan MCP by sorrek](../tools/magellan-mcp-by-sorrek.md)
magellandata.io | [Community MCP](../mcp/community.md) | [https://github.com/sorrek/mcp](https://github.com/sorrek/mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Magpipe](../tools/magpipe.md)
magpipe.ai | [Community MCP](../mcp/community.md) | [https://github.com/elagerway/magpipe](https://github.com/elagerway/magpipe) | blank | [Gate unknown](../gates/unknown.md) |
| [Mamba Domain Deliverability MCP](../tools/mamba-domain-deliverability-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mambalabsdev/mcp-domain-deliverab...](https://github.com/mambalabsdev/mcp-domain-deliverability-checker) | blank | [Gate unknown](../gates/unknown.md) |
| [Mamba Firmographic Enricher MCP](../tools/mamba-firmographic-enricher-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Mamba GTM Hiring Signal MCP](../tools/mamba-gtm-hiring-signal-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Mamba GTM Job Discovery MCP](../tools/mamba-gtm-job-discovery-mcp.md)
mambabuilt.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | blank | [Gate unknown](../gates/unknown.md) |
| [Mamba GTM Suite MCP](../tools/mamba-gtm-suite-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Mamba Tech Stack Signal MCP](../tools/mamba-tech-stack-signal-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mambalabsdev/mcp-gtm-tech-stack-s...](https://github.com/mambalabsdev/mcp-gtm-tech-stack-signal-scraper) | blank | [Gate unknown](../gates/unknown.md) |
| [Max MCP by Digital Crew](../tools/max-mcp-by-digital-crew.md)
max-mcp-server.vercel.app | [Community MCP](../mcp/community.md) | [https://github.com/Digital-Crew-Technologies/max-mcp...](https://github.com/Digital-Crew-Technologies/max-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [MCP Force by RapidoCloud](../tools/mcp-force-by-rapidocloud.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/RapidoCloud/mcp-force](https://github.com/RapidoCloud/mcp-force) | blank | [Gate unknown](../gates/unknown.md) |
| [MCP-Salesforce by smn2gnt](../tools/mcp-salesforce-by-smn2gnt.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [MCPCloud CLI](../tools/mcpcloud-cli.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20enrichment](https://www.npmjs.com/search?q=mcp%20enrichment) | blank | [Gate unknown](../gates/unknown.md) |
| [Mesh](../tools/mesh.md)
me.sh | [Community MCP](../mcp/community.md) | [https://github.com/mesh/mesh-mcp](https://github.com/mesh/mesh-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Method CRM MCP](../tools/method-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/avisangle/method-crm-mcp-workers](https://github.com/avisangle/method-crm-mcp-workers) | blank | [Gate unknown](../gates/unknown.md) |
| [Misarreach](../tools/misarreach.md)
misarreach.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | blank | [Gate unknown](../gates/unknown.md) |
| [Morphed](../tools/morphed.md)
morphed.io | [Community MCP](../mcp/community.md) | [https://morphed.io/mcp](https://morphed.io/mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Munin](../tools/munin.md)
getmunin.com | [Community MCP](../mcp/community.md) | [https://github.com/getmunin/munin](https://github.com/getmunin/munin) | blank | [Gate unknown](../gates/unknown.md) |
| [myOPC](../tools/myopc.md)
myopc.io | [Community MCP](../mcp/community.md) | [https://github.com/Steveser1989/Main-MY-OPC-System](https://github.com/Steveser1989/Main-MY-OPC-System) | blank | [Gate unknown](../gates/unknown.md) |
| [n47vc MCP Suite](../tools/n47vc-mcp-suite.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/n47vc/mcp](https://github.com/n47vc/mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Nevent MCP](../tools/nevent-mcp.md)
nevent.ai | [Community MCP](../mcp/community.md) | [https://github.com/nevent-dev/mcp-nevent](https://github.com/nevent-dev/mcp-nevent) | blank | [Gate unknown](../gates/unknown.md) |
| [Nex MCP](../tools/nex-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/nex-crm/nex-as-a-skill](https://github.com/nex-crm/nex-as-a-skill) | blank | [Gate unknown](../gates/unknown.md) |
| [Nimbus](../tools/nimbus.md)
testnimbus.dev | [Community MCP](../mcp/community.md) | [https://github.com/nimbus-solution/nimbus](https://github.com/nimbus-solution/nimbus) | blank | [Gate unknown](../gates/unknown.md) |
| [NirmahGTM](../tools/nirmahgtm.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/AnjaliPPal/NirmahGTM](https://github.com/AnjaliPPal/NirmahGTM) | blank | [Gate unknown](../gates/unknown.md) |
| [Nuph](../tools/nuph.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/teslaeas/nuph-mcp-server](https://github.com/teslaeas/nuph-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Nynch MCP](../tools/nynch-mcp.md)
nynch.com | [Community MCP](../mcp/community.md) | [https://github.com/peterod99/nynch-mcp-server](https://github.com/peterod99/nynch-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Ocean.io Agent CLI](../tools/ocean-io-agent-cli.md)
ocean.io | [Community MCP](../mcp/community.md) | [https://github.com/bcharleson/ocean-agent-cli](https://github.com/bcharleson/ocean-agent-cli) | blank | [Gate unknown](../gates/unknown.md) |
| [Odoo MCP by pipeworx](../tools/odoo-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-odoo](https://github.com/pipeworx-io/mcp-odoo) | blank | [Gate unknown](../gates/unknown.md) |
| [Oisha OS](../tools/oisha-os.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/baxtiyorjongaziyev/oisha-os](https://github.com/baxtiyorjongaziyev/oisha-os) | blank | [Gate unknown](../gates/unknown.md) |
| [Opafex MCP Suite](../tools/opafex-mcp-suite.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Opafex/opafex-mcps](https://github.com/Opafex/opafex-mcps) | blank | [Gate unknown](../gates/unknown.md) |
| [Open Sales Stack MCP by ekas](../tools/open-sales-stack-mcp-by-ekas.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [OpenDirectories MCP](../tools/opendirectories-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/BigJai/opendirectories-mcp](https://github.com/BigJai/opendirectories-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [OpsDoctor](../tools/opsdoctor.md)
opsdoctor.app | [Community MCP](../mcp/community.md) | [https://github.com/jhicks935-lab/resolution-ai](https://github.com/jhicks935-lab/resolution-ai) | blank | [Gate unknown](../gates/unknown.md) |
| [Outbound Engine MCP by closermethod](../tools/outbound-engine-mcp-by-closermethod.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/closermethod/outbound-engine-mcp](https://github.com/closermethod/outbound-engine-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Outreach Deliverability MCP by closermethod](../tools/outreach-deliverability-mcp-by-closermethod.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/closermethod/outreach-deliverabil...](https://github.com/closermethod/outreach-deliverability-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Outreach MCP by CData](../tools/outreach-mcp-by-cdata.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/CDataSoftware/outreach.io-mcp-ser...](https://github.com/CDataSoftware/outreach.io-mcp-server-by-cdata) | blank | [Gate unknown](../gates/unknown.md) |
| [Outreach MCP by mindstone-engineering](../tools/outreach-mcp-by-mindstone-engineering.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20outreach](https://www.npmjs.com/search?q=mcp-server%20outreach) | blank | [Gate unknown](../gates/unknown.md) |
| [Outreacher](../tools/outreacher.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/technicallypete/outreacher](https://github.com/technicallypete/outreacher) | blank | [Gate unknown](../gates/unknown.md) |
| [PaidSync MCP](../tools/paidsync-mcp.md)
paidsync.ai | [Community MCP](../mcp/community.md) | [https://github.com/PaidSync/paidsync-mcp](https://github.com/PaidSync/paidsync-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [People Data Labs MCP by pipeworx](../tools/people-data-labs-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-peopledatalabs](https://github.com/pipeworx-io/mcp-peopledatalabs) | blank | [Gate unknown](../gates/unknown.md) |
| [Perfex CRM MCP](../tools/perfex-crm-mcp.md)
themesic.com | [Community MCP](../mcp/community.md) | [https://github.com/themesic/perfex-rest-api-examples](https://github.com/themesic/perfex-rest-api-examples) | blank | [Gate unknown](../gates/unknown.md) |
| [PersuadioAI](../tools/persuadioai.md)
persuadioai.com | [Community MCP](../mcp/community.md) | [https://github.com/mannyfernandezvc/persuadioai-plat...](https://github.com/mannyfernandezvc/persuadioai-platform) | blank | [Gate unknown](../gates/unknown.md) |
| [Pipedrive MCP by comma-compliance](../tools/pipedrive-mcp-by-comma-compliance.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/comma-compliance/pipedrive-mcp](https://github.com/comma-compliance/pipedrive-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Pipedrive MCP by Teapot-Agency](../tools/pipedrive-mcp-by-teapot-agency.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) | blank | [Gate unknown](../gates/unknown.md) |
| [Planhat MCP by da-troll](../tools/planhat-mcp-by-da-troll.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/da-troll/Planhat-MCP](https://github.com/da-troll/Planhat-MCP) | blank | [Gate unknown](../gates/unknown.md) |
| [Plixana](../tools/plixana.md)
plixana.com | [Community MCP](../mcp/community.md) | [https://plixana.com/conecta-tu-ia](https://plixana.com/conecta-tu-ia) | blank | [Gate unknown](../gates/unknown.md) |
| [Ploomes MCP by victorbenazzi](../tools/ploomes-mcp-by-victorbenazzi.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/victorbenazzi/ploomes-mcp-server](https://github.com/victorbenazzi/ploomes-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Podcast Guest CRM](../tools/podcast-guest-crm.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/RudrenduPaul/podcast-guest-crm](https://github.com/RudrenduPaul/podcast-guest-crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Potarix Enricher](../tools/potarix-enricher.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Potarix/potarix-mcp](https://github.com/Potarix/potarix-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Prism Enrichment](../tools/prism-enrichment.md)
enrich.gocreativeai.com | [Community MCP](../mcp/community.md) | [https://enrich.gocreativeai.com](https://enrich.gocreativeai.com) | blank | [Gate unknown](../gates/unknown.md) |
| [Prospecting Agent by B-Kirb](../tools/prospecting-agent-by-b-kirb.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/B-Kirb/prospecting-agent](https://github.com/B-Kirb/prospecting-agent) | blank | [Gate unknown](../gates/unknown.md) |
| [Prospector MCP by dremnik](../tools/prospector-mcp-by-dremnik.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/dremnik/prospector](https://github.com/dremnik/prospector) | blank | [Gate unknown](../gates/unknown.md) |
| [PulseAgent MCP](../tools/pulseagent-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/iPythoning/pulseagent-mcp-server](https://github.com/iPythoning/pulseagent-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [RapidStart CRM MCP](../tools/rapidstart-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/forceworks/rapidstart-mcp-server](https://github.com/forceworks/rapidstart-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Relm CRM](../tools/relm-crm.md)
relmcrm.com | [Community MCP](../mcp/community.md) | [https://relmcrm.com](https://relmcrm.com) | blank | [Gate unknown](../gates/unknown.md) |
| [RepScale](../tools/repscale.md)
repscale.ai | [Community MCP](../mcp/community.md) | [https://repscale.ai](https://repscale.ai) | blank | [Gate unknown](../gates/unknown.md) |
| [RetailCRM MCP](../tools/retailcrm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/theYahia/retailcrm-mcp](https://github.com/theYahia/retailcrm-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [RevOps Eval](../tools/revops-eval.md)
revopseval.com | [Community MCP](../mcp/community.md) | [https://github.com/elijeangilles/revops-skills](https://github.com/elijeangilles/revops-skills) | blank | [Gate unknown](../gates/unknown.md) |
| [S.C.A.L.A.](../tools/s-c-a-l-a.md)
get-scala.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Sales Enablement Plugin by jbalbu01](../tools/sales-enablement-plugin-by-jbalbu01.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jbalbu01/sales-enablement-plugin](https://github.com/jbalbu01/sales-enablement-plugin) | blank | [Gate unknown](../gates/unknown.md) |
| [Sales Intelligence MCP by Aria Agentworks](../tools/sales-intelligence-mcp-by-aria-agentworks.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/aria-agentworks/sales-intelligenc...](https://github.com/aria-agentworks/sales-intelligence-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesbot LinkedIn MCP](../tools/salesbot-linkedin-mcp.md)
salesbot.cz | [Community MCP](../mcp/community.md) | [https://github.com/Kubis010/linkedin-mcp-server-sale...](https://github.com/Kubis010/linkedin-mcp-server-salesbot) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce CLI MCP](../tools/salesforce-cli-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Cloud MCP by aaronsb](../tools/salesforce-cloud-mcp-by-aaronsb.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/aaronsb/salesforce-cloud](https://github.com/aaronsb/salesforce-cloud) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Commerce Cloud MCP by brinzl](../tools/salesforce-commerce-cloud-mcp-by-brinzl.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/brinzl/commercecloud-mcp-server](https://github.com/brinzl/commercecloud-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Commerce Cloud MCP by vinkius-labs](../tools/salesforce-commerce-cloud-mcp-by-vinkius-labs.md)
vinkius.com | [Community MCP](../mcp/community.md) | [https://github.com/vinkius-labs/salesforce-commerce-...](https://github.com/vinkius-labs/salesforce-commerce-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Data Cloud MCP by rishiganesh25](../tools/salesforce-data-cloud-mcp-by-rishiganesh25.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/rishiganesh25/data360-mcp](https://github.com/rishiganesh25/data360-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Docs MCP by Sanket](../tools/salesforce-docs-mcp-by-sanket.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SalesforceDiariesBySanket/salesfo...](https://github.com/SalesforceDiariesBySanket/salesforce-docs-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Hosted Custom MCP by Sanket](../tools/salesforce-hosted-custom-mcp-by-sanket.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SalesforceDiariesBySanket/Salesfo...](https://github.com/SalesforceDiariesBySanket/Salesforce-Hosted-Custom-Mcp-Server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Intelligence MCP](../tools/salesforce-intelligence-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/PranavNagrecha/Salesforce-Intelli...](https://github.com/PranavNagrecha/Salesforce-Intelligence) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by Devart](../tools/salesforce-marketing-cloud-mcp-by-devart.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-salesforce-marketing-cloud) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by salesforcebob](../tools/salesforce-marketing-cloud-mcp-by-salesforcebob.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/salesforcebob/Salesforce-Marketin...](https://github.com/salesforcebob/Salesforce-Marketing-Cloud-Engagement-MCP) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by vinkius-labs](../tools/salesforce-marketing-cloud-mcp-by-vinkius-labs.md)
vinkius.com | [Community MCP](../mcp/community.md) | [https://github.com/vinkius-labs/salesforce-marketing...](https://github.com/vinkius-labs/salesforce-marketing-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Auto Auth by kugamon](../tools/salesforce-mcp-auto-auth-by-kugamon.md)
pypi.org | [Community MCP](../mcp/community.md) | [https://github.com/kugamon/salesforce-mcp-auto-auth-...](https://github.com/kugamon/salesforce-mcp-auto-auth-chrome) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by aaron-pienza](../tools/salesforce-mcp-by-aaron-pienza.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by advancedcommunities](../tools/salesforce-mcp-by-advancedcommunities.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/advancedcommunities/salesforce-mc...](https://github.com/advancedcommunities/salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by AiondaDotCom](../tools/salesforce-mcp-by-aiondadotcom.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/AiondaDotCom/mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by alfe](../tools/salesforce-mcp-by-alfe.md)
alfe.ai | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20salesforce](https://www.npmjs.com/search?q=mcp%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by boejucci](../tools/salesforce-mcp-by-boejucci.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by Devart](../tools/salesforce-mcp-by-devart.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by imazhar101](../tools/salesforce-mcp-by-imazhar101.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by jaworjar95](../tools/salesforce-mcp-by-jaworjar95.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jaworjar95/salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by kablewy](../tools/salesforce-mcp-by-kablewy.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/kablewy/salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by KirtiJha](../tools/salesforce-mcp-by-kirtijha.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20salesforce](https://www.npmjs.com/search?q=mcp%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by LokiMCPUniverse](../tools/salesforce-mcp-by-lokimcpuniverse.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/LokiMCPUniverse/salesforce-mcp-se...](https://github.com/LokiMCPUniverse/salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by mindstone](../tools/salesforce-mcp-by-mindstone.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by pipeworx](../tools/salesforce-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-salesforce](https://github.com/pipeworx-io/mcp-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by rohithvemulapally](../tools/salesforce-mcp-by-rohithvemulapally.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by starcatmeow](../tools/salesforce-mcp-by-starcatmeow.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by suraj20028](../tools/salesforce-mcp-by-suraj20028.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/suraj20028/Salesforce-MCP](https://github.com/suraj20028/Salesforce-MCP) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by SurajAdsul](../tools/salesforce-mcp-by-surajadsul.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SurajAdsul/mcp-server-salesforce](https://github.com/SurajAdsul/mcp-server-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by timescale](../tools/salesforce-mcp-by-timescale.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/timescale/tiger-salesforce-mcp-se...](https://github.com/timescale/tiger-salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by tomnagengast](../tools/salesforce-mcp-by-tomnagengast.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/tomnagengast/mcp-server-salesforc...](https://github.com/tomnagengast/mcp-server-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by tsmztech](../tools/salesforce-mcp-by-tsmztech.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by vinkius-labs](../tools/salesforce-mcp-by-vinkius-labs.md)
vinkius.com | [Community MCP](../mcp/community.md) | [https://github.com/vinkius-labs/salesforce-mcp](https://github.com/vinkius-labs/salesforce-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Lib by Damecek](../tools/salesforce-mcp-lib-by-damecek.md)
context7.com | [Community MCP](../mcp/community.md) | [https://github.com/Damecek/salesforce-mcp-lib](https://github.com/Damecek/salesforce-mcp-lib) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Security Toolkit](../tools/salesforce-mcp-security-toolkit.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/ccmalcom/SFDC-MCP-Security-Toolki...](https://github.com/ccmalcom/SFDC-MCP-Security-Toolkit) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Metadata MCP by semwalajay83](../tools/salesforce-metadata-mcp-by-semwalajay83.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/semwalajay83-sem/salesforce-metad...](https://github.com/semwalajay83-sem/salesforce-metadata-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Pardot MCP by DaniilMai](../tools/salesforce-pardot-mcp-by-daniilmai.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/DaniilMai/salesforce-pardot-mcp](https://github.com/DaniilMai/salesforce-pardot-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Remote MCP by tsmztech](../tools/salesforce-remote-mcp-by-tsmztech.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/tsmztech/salesforce-remote-mcp-cl...](https://github.com/tsmztech/salesforce-remote-mcp-cloudflare) | blank | [Gate unknown](../gates/unknown.md) |
| [ScraperCity](../tools/scrapercity.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [SeldonFrame](../tools/seldonframe.md)
seldonframe.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [SeldonFrame MCP](../tools/seldonframe-mcp.md)
seldonframe.com | [Community MCP](../mcp/community.md) | [https://github.com/seldonframe/seldonframe](https://github.com/seldonframe/seldonframe) | blank | [Gate unknown](../gates/unknown.md) |
| [ServiceAgent](../tools/serviceagent.md)
serviceagent.ai | [Community MCP](../mcp/community.md) | [https://serviceagent.ai](https://serviceagent.ai) | blank | [Gate unknown](../gates/unknown.md) |
| [Setu Email MCP by gitmanhimanshu](../tools/setu-email-mcp-by-gitmanhimanshu.md)
setu.mimanasa.online | [Community MCP](../mcp/community.md) | [https://github.com/gitmanhimanshu/Email_automation](https://github.com/gitmanhimanshu/Email_automation) | blank | [Gate unknown](../gates/unknown.md) |
| [SFCC Dev MCP by taurgis](../tools/sfcc-dev-mcp-by-taurgis.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/taurgis/sfcc-dev-mcp](https://github.com/taurgis/sfcc-dev-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Siftable](../tools/siftable.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Signal Found Reddit MCP](../tools/signal-found-reddit-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/signal-found/sf-mcp](https://github.com/signal-found/sf-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [SIMOSphere](../tools/simosphere.md)
simosphereai.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Snov.io MCP by narkov](../tools/snov-io-mcp-by-narkov.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/narkov/snov-io-mcp-server](https://github.com/narkov/snov-io-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Social Profile Enrichment API](../tools/social-profile-enrichment-api.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Br0ski777/social-profile-x402](https://github.com/Br0ski777/social-profile-x402) | blank | [Gate unknown](../gates/unknown.md) |
| [Stacks AI](../tools/stacks-ai.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jentrix-au/stacks-ai](https://github.com/jentrix-au/stacks-ai) | blank | [Gate unknown](../gates/unknown.md) |
| [Studiomeyer CRM](../tools/studiomeyer-crm.md)
studiomeyer.io | [Community MCP](../mcp/community.md) | [https://github.com/studiomeyer-io/studiomeyer-crm](https://github.com/studiomeyer-io/studiomeyer-crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Synapse CRM MCP by NimbleBrain](../tools/synapse-crm-mcp-by-nimblebrain.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/NimbleBrainInc/synapse-crm](https://github.com/NimbleBrainInc/synapse-crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Teamleader MCP by BoostU](../tools/teamleader-mcp-by-boostu.md)
teamleader-mcp.boostu.be | [Community MCP](../mcp/community.md) | [https://github.com/boostuagency/boostu-teamleader-mc...](https://github.com/boostuagency/boostu-teamleader-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Technology Stack Detection API](../tools/technology-stack-detection-api.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Br0ski777/tech-enrichment-x402](https://github.com/Br0ski777/tech-enrichment-x402) | blank | [Gate unknown](../gates/unknown.md) |
| [Techtenstein LinkedIn MCP](../tools/techtenstein-linkedin-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/sathvic-kollu/techtenstein-linked...](https://github.com/sathvic-kollu/techtenstein-linkedin-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [TeloSignal](../tools/telosignal.md)
telosignal.com | [Community MCP](../mcp/community.md) | [https://github.com/patrick-creates/telosignal-workfl...](https://github.com/patrick-creates/telosignal-workflow-vault) | blank | [Gate unknown](../gates/unknown.md) |
| [Toflow](../tools/toflow.md)
toflow.ai | [Community MCP](../mcp/community.md) | [https://github.com/toflow-ai/toflow-mcp](https://github.com/toflow-ai/toflow-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Tomba](../tools/tomba.md)
tomba.io | [Community MCP](../mcp/community.md) | [https://github.com/tomba-io/tomba-mcp-server](https://github.com/tomba-io/tomba-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Twenty CRM MCP](../tools/twenty-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Twenty MCP Suite](../tools/twenty-mcp-suite.md)
andrewmarconi.github.io | [Community MCP](../mcp/community.md) | [https://github.com/andrewmarconi/twenty-mcp-suite](https://github.com/andrewmarconi/twenty-mcp-suite) | blank | [Gate unknown](../gates/unknown.md) |
| [UGC VZ MCP](../tools/ugc-vz-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/ugcvz/ugc-vz-mcp](https://github.com/ugcvz/ugc-vz-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Vesxo Connect](../tools/vesxo-connect.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Vibe Prospecting MCP](../tools/vibe-prospecting-mcp.md)
vibeprospecting.ai | [Community MCP](../mcp/community.md) | [https://github.com/explorium-ai/vibeprospecting-mcp](https://github.com/explorium-ai/vibeprospecting-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Vinkius Lead Gen Agents](../tools/vinkius-lead-gen-agents.md)
vinkius.com | [Community MCP](../mcp/community.md) | [https://github.com/vinkius-labs/crewai-mcp-lead-gen-...](https://github.com/vinkius-labs/crewai-mcp-lead-gen-agents) | blank | [Gate unknown](../gates/unknown.md) |
| [Voibe](../tools/voibe.md)
getvoibe.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=outreach](https://registry.smithery.ai/servers?q=outreach) | blank | [Gate unknown](../gates/unknown.md) |
| [Volanea](../tools/volanea.md)
volanea.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=2&pageSize...](https://registry.smithery.ai/servers?page=2&pageSize=100&q=crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Vruum](../tools/vruum.md)
vruum.ai | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | blank | [Gate unknown](../gates/unknown.md) |
| [Vsyble](../tools/vsyble.md)
vsyble.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20enrichment](https://www.npmjs.com/search?q=mcp%20enrichment) | blank | [Gate unknown](../gates/unknown.md) |
| [Wapiworld](../tools/wapiworld.md)
app.wapiworld.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=hubspot](https://registry.smithery.ai/servers?q=hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [WarmySender](../tools/warmysender.md)
warmysender.com | [Community MCP](../mcp/community.md) | [https://warmysender.com](https://warmysender.com) | blank | [Gate unknown](../gates/unknown.md) |
| [Well](../tools/well.md)
wellapp.ai | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Whatcanido](../tools/whatcanido.md)
whatcanido.dev | [Community MCP](../mcp/community.md) | [https://whatcanido.dev/agents](https://whatcanido.dev/agents) | blank | [Gate unknown](../gates/unknown.md) |
| [Wokelo](../tools/wokelo.md)
wokelo.ai | [Community MCP](../mcp/community.md) | [https://github.com/Wokelo-AI/Wokelo-MCP-Server](https://github.com/Wokelo-AI/Wokelo-MCP-Server) | blank | [Gate unknown](../gates/unknown.md) |
| [Xverum](../tools/xverum.md)
ask.xverum.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=enrich](https://registry.smithery.ai/servers?q=enrich) | blank | [Gate unknown](../gates/unknown.md) |
| [YG3](../tools/yg3.md)
yg3.ai | [Community MCP](../mcp/community.md) | [https://github.com/YG3-ai/yg3-mcp](https://github.com/YG3-ai/yg3-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [YourICP MCP](../tools/youricp-mcp.md)
app.youricp.com | [Community MCP](../mcp/community.md) | [https://github.com/YourICP/mcp-server](https://github.com/YourICP/mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [YouSpot](../tools/youspot.md)
youspot.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Zavora Sales Operations Skill](../tools/zavora-sales-operations-skill.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/zavora-ai/skill-sales-operations](https://github.com/zavora-ai/skill-sales-operations) | blank | [Gate unknown](../gates/unknown.md) |
| [Zetadeck](../tools/zetadeck.md)
zetadeck.com | [Community MCP](../mcp/community.md) | [https://zetadeck.com](https://zetadeck.com) | blank | [Gate unknown](../gates/unknown.md) |
| [Zoho CRM MCP by Devart](../tools/zoho-crm-mcp-by-devart.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-zoho-crm) | blank | [Gate unknown](../gates/unknown.md) |
| [ZOOQ](../tools/zooq.md)
zooq.dev | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=enrich](https://registry.smithery.ai/servers?q=enrich) | blank | [Gate unknown](../gates/unknown.md) |

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 1,032 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
