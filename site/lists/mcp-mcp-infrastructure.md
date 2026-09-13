# MCP Layer tools with MCP servers: 173 of 178, counted

> 173 of the 178 mcp layer tools in The GTM MCP Directory have an MCP server: 14 official and 159 community. The server URL, auth model and access gate for each. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / MCP Layer tools with an MCP server

**List · 173 of 934**

## MCP Layer tools with an MCP server

The layer that sits between an AI agent and the hundred SaaS apps a GTM team actually runs on: registries that just list servers, and aggregators that host/broker them. The load-bearing question for every entry below is who holds the OAuth tokens when you connect - read `notes` before you wire anything into a production agent. 173 of 178 entries in this category are reachable by an agent: 14 through a server the vendor maintains and 159 through one somebody else built. The category is tagged most often with Proxy tool calls to SaaS apps. [See the full category page](../categories/mcp-infrastructure.md).

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
| [0nmcp](../tools/0nmcp.md)
0nmcp.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Accelo MCP by Selerity](../tools/accelo-mcp-by-selerity.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Selerity/accelo-mcp](https://github.com/Selerity/accelo-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ActiveCampaign MCP by pipeworx](../tools/activecampaign-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-activecampaign](https://github.com/pipeworx-io/mcp-activecampaign) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Adrata](../tools/adrata.md)
adrata.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [AmpUp GTM Chat](../tools/ampup-gtm-chat.md)
chat.ampup.ai | [Community MCP](../mcp/community.md) | [https://github.com/A79-ai/gtm-agentic-chat](https://github.com/A79-ai/gtm-agentic-chat) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Anyquery](../tools/anyquery.md)
anyquery.dev | [Community MCP](../mcp/community.md) | [https://github.com/julien040/anyquery](https://github.com/julien040/anyquery) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apex Log MCP by Certinia](../tools/apex-log-mcp-by-certinia.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://github.com/certinia/debug-log-analyzer-mcp](https://github.com/certinia/debug-log-analyzer-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apex MCP SDK by bfmvsa](../tools/apex-mcp-sdk-by-bfmvsa.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/bfmvsa/mcp-apex-sdk](https://github.com/bfmvsa/mcp-apex-sdk) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apify Actors MCP](../tools/apify-actors-mcp.md)
mcp.apify.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by BlockchainRev](../tools/apollo-mcp-by-blockchainrev.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/BlockchainRev/apollo-mcp-server](https://github.com/BlockchainRev/apollo-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by Eden-Anthony](../tools/apollo-mcp-by-eden-anthony.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Eden-Anthony/apollo-mcp](https://github.com/Eden-Anthony/apollo-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by Inferensys](../tools/apollo-mcp-by-inferensys.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Inferensys/apollo-io-mcp](https://github.com/Inferensys/apollo-io-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by kingler](../tools/apollo-mcp-by-kingler.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/kingler/apollo-io-mcp-server](https://github.com/kingler/apollo-io-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by maxmulvey](../tools/apollo-mcp-by-maxmulvey.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/maxmulvey/apollo-mcp](https://github.com/maxmulvey/apollo-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by shariqriazz](../tools/apollo-mcp-by-shariqriazz.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/shariqriazz/apollo-io-mcp-server](https://github.com/shariqriazz/apollo-io-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP Plugin by apolloio](../tools/apollo-mcp-plugin-by-apolloio.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Attio MCP by hmk](../tools/attio-mcp-by-hmk.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [BD Desk MCP by iaj6](../tools/bd-desk-mcp-by-iaj6.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/iaj6/bd-desk](https://github.com/iaj6/bd-desk) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Bitrix24 MCP by john7ross](../tools/bitrix24-mcp-by-john7ross.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/john7ross/BitrixMCP](https://github.com/john7ross/BitrixMCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Blitz API Open Source](../tools/blitz-api-open-source.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/malharlakdawala/blitzapi-opensour...](https://github.com/malharlakdawala/blitzapi-opensource) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [BNI MCP by alexaltovate](../tools/bni-mcp-by-alexaltovate.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/alexaltovate/bni-mcp](https://github.com/alexaltovate/bni-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by MonadsAG](../tools/capsule-crm-mcp-by-monadsag.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by soil-dev](../tools/capsule-crm-mcp-by-soil-dev.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CiviCRM MCP by YogiAdhik](../tools/civicrm-mcp-by-yogiadhik.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/YogiAdhik/civicrm-mcp](https://github.com/YogiAdhik/civicrm-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Clay to Instantly/Smartlead MCP](../tools/clay-to-instantly-smartlead-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mambalabsdev/mcp-clay-to-instantl...](https://github.com/mambalabsdev/mcp-clay-to-instantly-smartlead-push) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Clint CRM MCP by Franky-Neto](../tools/clint-crm-mcp-by-franky-neto.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Franky-Neto/mcp-clint-crm](https://github.com/Franky-Neto/mcp-clint-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Close CRM MCP by pipeworx](../tools/close-crm-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-close-crm](https://github.com/pipeworx-io/mcp-close-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Coldforge](../tools/coldforge.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Makeph/coldforge](https://github.com/Makeph/coldforge) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Coldstart](../tools/coldstart.md)
coldstart.so | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Conduyt](../tools/conduyt.md)
conduyt.app | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CRM AI MCP by MEOK](../tools/crm-ai-mcp-by-meok.md)
meok.ai | [Community MCP](../mcp/community.md) | [https://github.com/CSOAI-ORG/crm-ai-mcp](https://github.com/CSOAI-ORG/crm-ai-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CRM Bridge MCP](../tools/crm-bridge-mcp.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CRM Solid MCP](../tools/crm-solid-mcp.md)
docs.crmsolid.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Curtis LinkedIn MCP](../tools/curtis-linkedin-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/matteolegrottaglie/curtis](https://github.com/matteolegrottaglie/curtis) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Customer Intelligence Hub](../tools/customer-intelligence-hub.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Gabrielm3/customer-intelligence-h...](https://github.com/Gabrielm3/customer-intelligence-hub) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Dolibarr MCP by sachitha7](../tools/dolibarr-mcp-by-sachitha7.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/sachitha7/mcp-server-dolibarr](https://github.com/sachitha7/mcp-server-dolibarr) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [EZ@Work MCP](../tools/ez-work-mcp.md)
ezatwork.com | [Community MCP](../mcp/community.md) | [https://github.com/eranfinish/ezatwork-mcp](https://github.com/eranfinish/ezatwork-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [FavCRM](../tools/favcrm.md)
favcrm.io | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Flipfactory CRM MCP](../tools/flipfactory-crm-mcp.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Fluent MCP Servers](../tools/fluent-mcp-servers.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Dominotypist3077/fluent-mcp-serve...](https://github.com/Dominotypist3077/fluent-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Follow Up Boss MCP](../tools/follow-up-boss-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/theperrygroup/Follow-Up-Boss-MCP](https://github.com/theperrygroup/Follow-Up-Boss-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Fundz Agent Examples](../tools/fundz-agent-examples.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Fund-z/agent-examples](https://github.com/Fund-z/agent-examples) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by elitedcs](../tools/gohighlevel-mcp-by-elitedcs.md)
elitedcs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by NightSquawk](../tools/gohighlevel-mcp-by-nightsquawk.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/NightSquawk/gohighlevel-mcp-serve...](https://github.com/NightSquawk/gohighlevel-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by rockurbusinesscs](../tools/gohighlevel-mcp-by-rockurbusinesscs.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/rockurbusinesscs-ship-it/gohighle...](https://github.com/rockurbusinesscs-ship-it/gohighlevel-mcp-starter) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GTM Alpha MCP](../tools/gtm-alpha-mcp.md)
gtmalpha.netlify.app | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GTM Copilot by archanakrishnan](../tools/gtm-copilot-by-archanakrishnan.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/archanakrishnan094-max/AI-GTM-Cop...](https://github.com/archanakrishnan094-max/AI-GTM-Copilot-End-to-End-GTM-Intelligence-CRM-Automation) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GTMos MCP by Kai8karma](../tools/gtmos-mcp-by-kai8karma.md)
kai8karma.github.io | [Community MCP](../mcp/community.md) | [https://github.com/Kai8karma/gtmos-mcp](https://github.com/Kai8karma/gtmos-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Guapu](../tools/guapu.md)
guapu.io | [Community MCP](../mcp/community.md) | [https://guapu.io/conecta-tu-ia](https://guapu.io/conecta-tu-ia) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HireSignal MCP](../tools/hiresignal-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/iusmuchandra/hiresignal-mcp](https://github.com/iusmuchandra/hiresignal-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by baryhuang](../tools/hubspot-mcp-by-baryhuang.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/baryhuang/mcp-hubspot](https://github.com/baryhuang/mcp-hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by Devart](../tools/hubspot-mcp-by-devart.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by djmoore-projects](../tools/hubspot-mcp-by-djmoore-projects.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/djmoore-projects/hubspot-mcp-serv...](https://github.com/djmoore-projects/hubspot-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by mindstone-engineering](../tools/hubspot-mcp-by-mindstone-engineering.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by pipeworx](../tools/hubspot-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-hubspot](https://github.com/pipeworx-io/mcp-hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by rfoxes](../tools/hubspot-mcp-by-rfoxes.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [IN2 Agent MCP](../tools/in2-agent-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Indraft](../tools/indraft.md)
indraft.io | [Community MCP](../mcp/community.md) | [https://indraft.io](https://indraft.io) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Infosys AI CRM by ffred1962](../tools/infosys-ai-crm-by-ffred1962.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/ffred1962/infosys](https://github.com/ffred1962/infosys) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Insaight](../tools/insaight.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/spirosbax/insaight](https://github.com/spirosbax/insaight) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Iridium LinkedIn Agent](../tools/iridium-linkedin-agent.md)
iridiumhqmcp.com | [Community MCP](../mcp/community.md) | [https://github.com/nikhilkulkarni1755/iridium-linked...](https://github.com/nikhilkulkarni1755/iridium-linkedin-agent) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Keepsake MCP by nicolascroce](../tools/keepsake-mcp-by-nicolascroce.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LeadConnector MCP by pipeworx](../tools/leadconnector-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-leadconnector](https://github.com/pipeworx-io/mcp-leadconnector) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Leadcraft MCP](../tools/leadcraft-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Lakshya330-sudo/leadcraft](https://github.com/Lakshya330-sudo/leadcraft) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Leadgen MCP by koolninad](../tools/leadgen-mcp-by-koolninad.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/koolninad/leadgen-mcp](https://github.com/koolninad/leadgen-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Leadzaar](../tools/leadzaar.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Techthos/leadzaar](https://github.com/Techthos/leadzaar) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn ICP Discovery MCP](../tools/linkedin-icp-discovery-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jpeslar1/linkedin-mcp-icp-discove...](https://github.com/jpeslar1/linkedin-mcp-icp-discovery) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Outreach MCP by hfarazul](../tools/linkedin-outreach-mcp-by-hfarazul.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/hfarazul/linkedin-outreach-mcp](https://github.com/hfarazul/linkedin-outreach-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Outreach MCP by MEOK](../tools/linkedin-outreach-mcp-by-meok.md)
meok.ai | [Community MCP](../mcp/community.md) | [https://github.com/CSOAI-ORG/linkedin-outreach-mcp](https://github.com/CSOAI-ORG/linkedin-outreach-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Little Green Light MCP](../tools/little-green-light-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/WillHeadlee/Little-Green-Light-MC...](https://github.com/WillHeadlee/Little-Green-Light-MCP-Server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Livespace CRM MCP](../tools/livespace-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/proAutomator/livespace-crm-mcp](https://github.com/proAutomator/livespace-crm-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Lookaberry GTM MCP](../tools/lookaberry-gtm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/lucasmartins-ai/lookaberry](https://github.com/lucasmartins-ai/lookaberry) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Maasy](../tools/maasy.md)
maasy.co | [Community MCP](../mcp/community.md) | [https://github.com/Jbelieve/mcp-server](https://github.com/Jbelieve/mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Magellan MCP by sorrek](../tools/magellan-mcp-by-sorrek.md)
magellandata.io | [Community MCP](../mcp/community.md) | [https://github.com/sorrek/mcp](https://github.com/sorrek/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Magpipe](../tools/magpipe.md)
magpipe.ai | [Community MCP](../mcp/community.md) | [https://github.com/elagerway/magpipe](https://github.com/elagerway/magpipe) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Max MCP by Digital Crew](../tools/max-mcp-by-digital-crew.md)
max-mcp-server.vercel.app | [Community MCP](../mcp/community.md) | [https://github.com/Digital-Crew-Technologies/max-mcp...](https://github.com/Digital-Crew-Technologies/max-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCP Force by RapidoCloud](../tools/mcp-force-by-rapidocloud.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/RapidoCloud/mcp-force](https://github.com/RapidoCloud/mcp-force) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCP-Salesforce by smn2gnt](../tools/mcp-salesforce-by-smn2gnt.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCPCloud CLI](../tools/mcpcloud-cli.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20enrichment](https://www.npmjs.com/search?q=mcp%20enrichment) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mesh](../tools/mesh.md)
me.sh | [Community MCP](../mcp/community.md) | [https://github.com/mesh/mesh-mcp](https://github.com/mesh/mesh-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Munin](../tools/munin.md)
getmunin.com | [Community MCP](../mcp/community.md) | [https://github.com/getmunin/munin](https://github.com/getmunin/munin) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [n47vc MCP Suite](../tools/n47vc-mcp-suite.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/n47vc/mcp](https://github.com/n47vc/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nevent MCP](../tools/nevent-mcp.md)
nevent.ai | [Community MCP](../mcp/community.md) | [https://github.com/nevent-dev/mcp-nevent](https://github.com/nevent-dev/mcp-nevent) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nimbus](../tools/nimbus.md)
testnimbus.dev | [Community MCP](../mcp/community.md) | [https://github.com/nimbus-solution/nimbus](https://github.com/nimbus-solution/nimbus) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nuph](../tools/nuph.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/teslaeas/nuph-mcp-server](https://github.com/teslaeas/nuph-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nynch MCP](../tools/nynch-mcp.md)
nynch.com | [Community MCP](../mcp/community.md) | [https://github.com/peterod99/nynch-mcp-server](https://github.com/peterod99/nynch-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Odoo MCP by pipeworx](../tools/odoo-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-odoo](https://github.com/pipeworx-io/mcp-odoo) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Open Sales Stack MCP by ekas](../tools/open-sales-stack-mcp-by-ekas.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outreach MCP by CData](../tools/outreach-mcp-by-cdata.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/CDataSoftware/outreach.io-mcp-ser...](https://github.com/CDataSoftware/outreach.io-mcp-server-by-cdata) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outreach MCP by mindstone-engineering](../tools/outreach-mcp-by-mindstone-engineering.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20outreach](https://www.npmjs.com/search?q=mcp-server%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outreacher](../tools/outreacher.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/technicallypete/outreacher](https://github.com/technicallypete/outreacher) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PaidSync MCP](../tools/paidsync-mcp.md)
paidsync.ai | [Community MCP](../mcp/community.md) | [https://github.com/PaidSync/paidsync-mcp](https://github.com/PaidSync/paidsync-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Perfex CRM MCP](../tools/perfex-crm-mcp.md)
themesic.com | [Community MCP](../mcp/community.md) | [https://github.com/themesic/perfex-rest-api-examples](https://github.com/themesic/perfex-rest-api-examples) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Pipedrive MCP by comma-compliance](../tools/pipedrive-mcp-by-comma-compliance.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/comma-compliance/pipedrive-mcp](https://github.com/comma-compliance/pipedrive-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Pipedrive MCP by Teapot-Agency](../tools/pipedrive-mcp-by-teapot-agency.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Planhat MCP by da-troll](../tools/planhat-mcp-by-da-troll.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/da-troll/Planhat-MCP](https://github.com/da-troll/Planhat-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Plixana](../tools/plixana.md)
plixana.com | [Community MCP](../mcp/community.md) | [https://plixana.com/conecta-tu-ia](https://plixana.com/conecta-tu-ia) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Ploomes MCP by victorbenazzi](../tools/ploomes-mcp-by-victorbenazzi.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/victorbenazzi/ploomes-mcp-server](https://github.com/victorbenazzi/ploomes-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Prospecting Agent by B-Kirb](../tools/prospecting-agent-by-b-kirb.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/B-Kirb/prospecting-agent](https://github.com/B-Kirb/prospecting-agent) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PulseAgent MCP](../tools/pulseagent-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/iPythoning/pulseagent-mcp-server](https://github.com/iPythoning/pulseagent-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RapidStart CRM MCP](../tools/rapidstart-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/forceworks/rapidstart-mcp-server](https://github.com/forceworks/rapidstart-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Relm CRM](../tools/relm-crm.md)
relmcrm.com | [Community MCP](../mcp/community.md) | [https://relmcrm.com](https://relmcrm.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RevOps Eval](../tools/revops-eval.md)
revopseval.com | [Community MCP](../mcp/community.md) | [https://github.com/elijeangilles/revops-skills](https://github.com/elijeangilles/revops-skills) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [S.C.A.L.A.](../tools/s-c-a-l-a.md)
get-scala.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Sales Enablement Plugin by jbalbu01](../tools/sales-enablement-plugin-by-jbalbu01.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jbalbu01/sales-enablement-plugin](https://github.com/jbalbu01/sales-enablement-plugin) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesbot LinkedIn MCP](../tools/salesbot-linkedin-mcp.md)
salesbot.cz | [Community MCP](../mcp/community.md) | [https://github.com/Kubis010/linkedin-mcp-server-sale...](https://github.com/Kubis010/linkedin-mcp-server-salesbot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce CLI MCP](../tools/salesforce-cli-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Cloud MCP by aaronsb](../tools/salesforce-cloud-mcp-by-aaronsb.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/aaronsb/salesforce-cloud](https://github.com/aaronsb/salesforce-cloud) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Commerce Cloud MCP by brinzl](../tools/salesforce-commerce-cloud-mcp-by-brinzl.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/brinzl/commercecloud-mcp-server](https://github.com/brinzl/commercecloud-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Commerce Cloud MCP by vinkius-labs](../tools/salesforce-commerce-cloud-mcp-by-vinkius-labs.md)
vinkius.com | [Community MCP](../mcp/community.md) | [https://github.com/vinkius-labs/salesforce-commerce-...](https://github.com/vinkius-labs/salesforce-commerce-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Data Cloud MCP by rishiganesh25](../tools/salesforce-data-cloud-mcp-by-rishiganesh25.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/rishiganesh25/data360-mcp](https://github.com/rishiganesh25/data360-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Docs MCP by Sanket](../tools/salesforce-docs-mcp-by-sanket.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SalesforceDiariesBySanket/salesfo...](https://github.com/SalesforceDiariesBySanket/salesforce-docs-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Hosted Custom MCP by Sanket](../tools/salesforce-hosted-custom-mcp-by-sanket.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SalesforceDiariesBySanket/Salesfo...](https://github.com/SalesforceDiariesBySanket/Salesforce-Hosted-Custom-Mcp-Server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by Devart](../tools/salesforce-marketing-cloud-mcp-by-devart.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-salesforce-marketing-cloud) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by salesforcebob](../tools/salesforce-marketing-cloud-mcp-by-salesforcebob.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/salesforcebob/Salesforce-Marketin...](https://github.com/salesforcebob/Salesforce-Marketing-Cloud-Engagement-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by vinkius-labs](../tools/salesforce-marketing-cloud-mcp-by-vinkius-labs.md)
vinkius.com | [Community MCP](../mcp/community.md) | [https://github.com/vinkius-labs/salesforce-marketing...](https://github.com/vinkius-labs/salesforce-marketing-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Auto Auth by kugamon](../tools/salesforce-mcp-auto-auth-by-kugamon.md)
pypi.org | [Community MCP](../mcp/community.md) | [https://github.com/kugamon/salesforce-mcp-auto-auth-...](https://github.com/kugamon/salesforce-mcp-auto-auth-chrome) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by aaron-pienza](../tools/salesforce-mcp-by-aaron-pienza.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by advancedcommunities](../tools/salesforce-mcp-by-advancedcommunities.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/advancedcommunities/salesforce-mc...](https://github.com/advancedcommunities/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by AiondaDotCom](../tools/salesforce-mcp-by-aiondadotcom.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/AiondaDotCom/mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by alfe](../tools/salesforce-mcp-by-alfe.md)
alfe.ai | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20salesforce](https://www.npmjs.com/search?q=mcp%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by boejucci](../tools/salesforce-mcp-by-boejucci.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by Devart](../tools/salesforce-mcp-by-devart.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by imazhar101](../tools/salesforce-mcp-by-imazhar101.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by jaworjar95](../tools/salesforce-mcp-by-jaworjar95.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jaworjar95/salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by kablewy](../tools/salesforce-mcp-by-kablewy.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/kablewy/salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by KirtiJha](../tools/salesforce-mcp-by-kirtijha.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20salesforce](https://www.npmjs.com/search?q=mcp%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by LokiMCPUniverse](../tools/salesforce-mcp-by-lokimcpuniverse.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/LokiMCPUniverse/salesforce-mcp-se...](https://github.com/LokiMCPUniverse/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by mindstone](../tools/salesforce-mcp-by-mindstone.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by pipeworx](../tools/salesforce-mcp-by-pipeworx.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/pipeworx-io/mcp-salesforce](https://github.com/pipeworx-io/mcp-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by rohithvemulapally](../tools/salesforce-mcp-by-rohithvemulapally.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by starcatmeow](../tools/salesforce-mcp-by-starcatmeow.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by suraj20028](../tools/salesforce-mcp-by-suraj20028.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/suraj20028/Salesforce-MCP](https://github.com/suraj20028/Salesforce-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by SurajAdsul](../tools/salesforce-mcp-by-surajadsul.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SurajAdsul/mcp-server-salesforce](https://github.com/SurajAdsul/mcp-server-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by timescale](../tools/salesforce-mcp-by-timescale.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/timescale/tiger-salesforce-mcp-se...](https://github.com/timescale/tiger-salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by tomnagengast](../tools/salesforce-mcp-by-tomnagengast.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/tomnagengast/mcp-server-salesforc...](https://github.com/tomnagengast/mcp-server-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by tsmztech](../tools/salesforce-mcp-by-tsmztech.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by vinkius-labs](../tools/salesforce-mcp-by-vinkius-labs.md)
vinkius.com | [Community MCP](../mcp/community.md) | [https://github.com/vinkius-labs/salesforce-mcp](https://github.com/vinkius-labs/salesforce-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Lib by Damecek](../tools/salesforce-mcp-lib-by-damecek.md)
context7.com | [Community MCP](../mcp/community.md) | [https://github.com/Damecek/salesforce-mcp-lib](https://github.com/Damecek/salesforce-mcp-lib) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Pardot MCP by DaniilMai](../tools/salesforce-pardot-mcp-by-daniilmai.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/DaniilMai/salesforce-pardot-mcp](https://github.com/DaniilMai/salesforce-pardot-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Remote MCP by tsmztech](../tools/salesforce-remote-mcp-by-tsmztech.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/tsmztech/salesforce-remote-mcp-cl...](https://github.com/tsmztech/salesforce-remote-mcp-cloudflare) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SeldonFrame](../tools/seldonframe.md)
seldonframe.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ServiceAgent](../tools/serviceagent.md)
serviceagent.ai | [Community MCP](../mcp/community.md) | [https://serviceagent.ai](https://serviceagent.ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Setu Email MCP by gitmanhimanshu](../tools/setu-email-mcp-by-gitmanhimanshu.md)
setu.mimanasa.online | [Community MCP](../mcp/community.md) | [https://github.com/gitmanhimanshu/Email_automation](https://github.com/gitmanhimanshu/Email_automation) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Siftable](../tools/siftable.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SIMOSphere](../tools/simosphere.md)
simosphereai.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Snov.io MCP by narkov](../tools/snov-io-mcp-by-narkov.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/narkov/snov-io-mcp-server](https://github.com/narkov/snov-io-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Stacks AI](../tools/stacks-ai.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jentrix-au/stacks-ai](https://github.com/jentrix-au/stacks-ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Studiomeyer CRM](../tools/studiomeyer-crm.md)
studiomeyer.io | [Community MCP](../mcp/community.md) | [https://github.com/studiomeyer-io/studiomeyer-crm](https://github.com/studiomeyer-io/studiomeyer-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Synapse CRM MCP by NimbleBrain](../tools/synapse-crm-mcp-by-nimblebrain.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/NimbleBrainInc/synapse-crm](https://github.com/NimbleBrainInc/synapse-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Twenty CRM MCP](../tools/twenty-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [UGC VZ MCP](../tools/ugc-vz-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/ugcvz/ugc-vz-mcp](https://github.com/ugcvz/ugc-vz-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Vesxo Connect](../tools/vesxo-connect.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Vibe Prospecting MCP](../tools/vibe-prospecting-mcp.md)
vibeprospecting.ai | [Community MCP](../mcp/community.md) | [https://github.com/explorium-ai/vibeprospecting-mcp](https://github.com/explorium-ai/vibeprospecting-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Whatcanido](../tools/whatcanido.md)
whatcanido.dev | [Community MCP](../mcp/community.md) | [https://whatcanido.dev/agents](https://whatcanido.dev/agents) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [YG3](../tools/yg3.md)
yg3.ai | [Community MCP](../mcp/community.md) | [https://github.com/YG3-ai/yg3-mcp](https://github.com/YG3-ai/yg3-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [YouSpot](../tools/youspot.md)
youspot.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Zavora Sales Operations Skill](../tools/zavora-sales-operations-skill.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/zavora-ai/skill-sales-operations](https://github.com/zavora-ai/skill-sales-operations) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Zoho CRM MCP by Devart](../tools/zoho-crm-mcp-by-devart.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-zoho-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |

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

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 934 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
