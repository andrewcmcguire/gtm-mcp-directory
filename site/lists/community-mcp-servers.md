# Community MCP servers: 271 GTM tools with a third party server

> Go to market tools where a working MCP server exists but somebody other than the vendor built it. Counted 2026-09-12 across 982 directory entries.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / The 271 GTM tools with a community MCP server

**List · 271 of 982**

## The 271 GTM tools with a community MCP server

A community server is a real server. It is also a server that can be abandoned without the vendor noticing, which is the single most useful thing to know before you write one into a workflow. The repo health rail that would date stamp each one has not been run, so no staleness claim is made here.

| Tool | Category | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Landbot](../tools/landbot.md)
landbot.io | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://composio.dev/toolkits/landbot](https://composio.dev/toolkits/landbot) +1 more | Third party platform auth
The operator's own Landbot API key stored with Composio; the Zapier connector rides... | [Free to start](../gates/free.md) |
| [Loom](../tools/loom.md)
loom.com | [Video Prospecting](../categories/video-prospecting.md) | [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom) +2 more | API key
karbassi/mcp-loom uses Loom's undocumented internal GraphQL API via a browser session... | [Free to start](../gates/free.md) |
| [People Data Labs](../tools/people-data-labs.md)
peopledatalabs.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/phxdev1/peopledatalabs-mcp](https://github.com/phxdev1/peopledatalabs-mcp) | API key
api key (PDL_API_KEY environment variable) | [Free to start](../gates/free.md) |
| [Aircall](../tools/aircall.md)
aircall.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/themobilefirstco/aircall-mcp-serv...](https://github.com/themobilefirstco/aircall-mcp-server) +1 more | OAuth or an API key
api key. The community server takes an Aircall API ID and API token, which the public API... | [Paid, self-serve](../gates/paid.md) |
| [Bonjoro](../tools/bonjoro.md)
bonjoro.com | [Video Prospecting](../categories/video-prospecting.md) | [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro) | OAuth
Rides a Zapier account connection (OAuth to Zapier, which holds the Bonjoro-side... | [Paid, self-serve](../gates/paid.md) |
| [Chatbase](../tools/chatbase.md)
chatbase.co | [Inbound & PLG Chat](../categories/inbound-plg-chat.md) | [https://zapier.com/mcp/chatbase](https://zapier.com/mcp/chatbase) | Third party platform auth
Rides Zapier's hosted-connector auth at mcp.zapier.com, not a Chatbase-issued MCP... | [Paid, self-serve](../gates/paid.md) |
| [Mention](../tools/mention.md)
mention.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://github.com/MaelitoP/mention-mcp-server](https://github.com/MaelitoP/mention-mcp-server) | API key
Mention API key via the MCP_MENTION_API_KEY environment variable | [Paid, self-serve](../gates/paid.md) |
| [Motion](../tools/motion.md)
usemotion.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp) | API key
API key (MOTION_API_KEY from Motion Settings -> API), per community repos. Rate limits... | [Paid, self-serve](../gates/paid.md) |
| [Overloop](../tools/overloop.md)
overloop.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp) | API key
api key via OVERLOOP_API_KEY environment variable | [Paid, self-serve](../gates/paid.md) |
| [SavvyCal](../tools/savvycal.md)
savvycal.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server) | API key
API key (SAVVYCAL_API_KEY env var, a personal access token from SavvyCal's Developer... | [Paid, self-serve](../gates/paid.md) |
| [Sendspark](../tools/sendspark.md)
sendspark.com | [Video Prospecting](../categories/video-prospecting.md) | [https://composio.dev/toolkits/sendspark](https://composio.dev/toolkits/sendspark) | Third party platform auth
API-key based - Composio's page states Sendspark requires the user's own API key, which... | [Paid, self-serve](../gates/paid.md) |
| [Syften](../tools/syften.md)
syften.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://github.com/syntax-syndicate/social-listening](https://github.com/syntax-syndicate/social-listening) | API key
Community server presumably authenticates with a Syften API key (matching Syften's own... | [Paid, self-serve](../gates/paid.md) |
| [Trigify (Trigify.io)](../tools/trigify.md)
trigify.io | [Signals & Intent](../categories/signals-intent-abm.md) | [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli) | API key
api key (from app.trigify.io/settings; via `trigify login --api-key`, env var... | [Paid, self-serve](../gates/paid.md) |
| [Unify](../tools/unify.md)
unifygtm.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://github.com/footcarts/unify-mcp](https://github.com/footcarts/unify-mcp) | Auth not recorded
Auth0 browser sign-in (auth.unifygtm.com); MCP caches the session cookie (~30-day life)... | [Paid, self-serve](../gates/paid.md) |
| [UpLead](../tools/uplead.md)
uplead.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://zapier.com/mcp/uplead](https://zapier.com/mcp/uplead) +1 more | OAuth or an API key
Handled through the Zapier/Pipedream platform's own connector auth (API key entered into... | [Paid, self-serve](../gates/paid.md) |
| [Vidyard](../tools/vidyard.md)
vidyard.com | [Video Prospecting](../categories/video-prospecting.md) | [https://viasocket.com/mcp/vidyard](https://viasocket.com/mcp/vidyard) | Third party platform auth
Not documented in technical detail on the viaSocket listing ("built-in authentication").... | [Paid, self-serve](../gates/paid.md) |
| [Weezly](../tools/weezly.md)
weezly.com | [Video Prospecting](../categories/video-prospecting.md) | [https://zapier.com/mcp/weezly](https://zapier.com/mcp/weezly) | Third party platform auth
Zapier-mediated connection. | [Paid, self-serve](../gates/paid.md) |
| [BombBomb](../tools/bombbomb.md)
bombbomb.com | [Video Prospecting](../categories/video-prospecting.md) | [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom) | OAuth or an API key
Rides Zapier's own OAuth/API-key connection to BombBomb; not a native BombBomb MCP auth... | [Enterprise only](../gates/enterprise-only.md) |
| [Brandwatch](../tools/brandwatch.md)
brandwatch.com | [Community & Dark Social](../categories/community-dark-social.md) | [https://github.com/ambo-sk/mcp-brandwatch](https://github.com/ambo-sk/mcp-brandwatch) | Auth not recorded
unknown - the third-party server's description states it interfaces with "the Brandwatch... | [Enterprise only](../gates/enterprise-only.md) |
| [Chorus](../tools/chorus.md)
zoominfo.com | [Conversation Intel](../categories/conversation-intel.md) | [https://github.com/opensourceops/chorus-mcp-server](https://github.com/opensourceops/chorus-mcp-server) | API key
Community server: Chorus API key in the CHORUS_API_KEY environment variable (stdio via... | [Enterprise only](../gates/enterprise-only.md) |
| [Copy.ai (GTM AI Platform)](../tools/copy-ai.md)
copy.ai | [AI SDRs](../categories/ai-sdr-agents.md) | [https://github.com/anhuaxiang/copy-ai-mcp](https://github.com/anhuaxiang/copy-ai-mcp) | API key
API key via COPY_AI_API_KEY environment variable | [Enterprise only](../gates/enterprise-only.md) |
| [DealHub (DealHub AI)](../tools/dealhub.md)
dealhub.io | [Proposals & Deals](../categories/proposals-deals.md) | [https://www.pulsemcp.com/servers/vishvick-dealhub-ad...](https://www.pulsemcp.com/servers/vishvick-dealhub-admin) | Auth not recorded
unknown - stdio transport run locally against the customer's own DealHub instance per the... | [Enterprise only](../gates/enterprise-only.md) |
| [Jiminny](../tools/jiminny.md)
jiminny.com | [Conversation Intel](../categories/conversation-intel.md) | [https://mcp.jiminny.com/mcp](https://mcp.jiminny.com/mcp) +3 more | OAuth or an API key
Community server: JIMINNY_TOKEN API token. Zapier's hosted connector uses Zapier's own... | [Enterprise only](../gates/enterprise-only.md) |
| [Loopio](../tools/loopio.md)
loopio.com | [Proposals & Deals](../categories/proposals-deals.md) | [https://github.com/fredericboyer/loopio-mcp](https://github.com/fredericboyer/loopio-mcp) | OAuth
OAuth2 client credentials (Client ID and Secret from the Loopio admin panel) against the... | [Enterprise only](../gates/enterprise-only.md) |
| [WorkRamp](../tools/workramp.md)
workramp.com | [Enablement & Coaching](../categories/enablement-coaching.md) | [https://app.workramp.com/mcp](https://app.workramp.com/mcp) +3 more | Third party platform auth
Rides Zapier's/viaSocket's own hosted-connector auth (their MCP gateway at... | [Enterprise only](../gates/enterprise-only.md) |
| [0nmcp](../tools/0nmcp.md)
0nmcp.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [abm.dev](../tools/abm-dev.md)
abm.dev | [Signals & Intent](../categories/signals-intent-abm.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=sales) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Accelo MCP by Selerity](../tools/accelo-mcp-by-selerity.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Selerity/accelo-mcp](https://github.com/Selerity/accelo-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ActiveCampaign MCP by pipeworx](../tools/activecampaign-mcp-by-pipeworx.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/pipeworx-io/mcp-activecampaign](https://github.com/pipeworx-io/mcp-activecampaign) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Adrata](../tools/adrata.md)
adrata.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Agentled](../tools/agentled.md)
agentled.app | [RevOps Infra](../categories/revops-infra.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [AmpUp GTM Chat](../tools/ampup-gtm-chat.md)
chat.ampup.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/A79-ai/gtm-agentic-chat](https://github.com/A79-ai/gtm-agentic-chat) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Anyquery](../tools/anyquery.md)
anyquery.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/julien040/anyquery](https://github.com/julien040/anyquery) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apex Log MCP by Certinia](../tools/apex-log-mcp-by-certinia.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/certinia/debug-log-analyzer-mcp](https://github.com/certinia/debug-log-analyzer-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apex MCP SDK by bfmvsa](../tools/apex-mcp-sdk-by-bfmvsa.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/bfmvsa/mcp-apex-sdk](https://github.com/bfmvsa/mcp-apex-sdk) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apify Actors MCP](../tools/apify-actors-mcp.md)
mcp.apify.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo Agent CLI by bcharleson](../tools/apollo-agent-cli-by-bcharleson.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/bcharleson/apollo-agent-cli](https://github.com/bcharleson/apollo-agent-cli) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by BlockchainRev](../tools/apollo-mcp-by-blockchainrev.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/BlockchainRev/apollo-mcp-server](https://github.com/BlockchainRev/apollo-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by Eden-Anthony](../tools/apollo-mcp-by-eden-anthony.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Eden-Anthony/apollo-mcp](https://github.com/Eden-Anthony/apollo-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by fuzzylabs](../tools/apollo-mcp-by-fuzzylabs.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/fuzzylabs/apollo-mcp](https://github.com/fuzzylabs/apollo-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by Inferensys](../tools/apollo-mcp-by-inferensys.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Inferensys/apollo-io-mcp](https://github.com/Inferensys/apollo-io-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by kingler](../tools/apollo-mcp-by-kingler.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/kingler/apollo-io-mcp-server](https://github.com/kingler/apollo-io-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by louis030195](../tools/apollo-mcp-by-louis030195.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by maxmulvey](../tools/apollo-mcp-by-maxmulvey.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/maxmulvey/apollo-mcp](https://github.com/maxmulvey/apollo-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by mayanksingh09](../tools/apollo-mcp-by-mayanksingh09.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/mayanksingh09/apollo-io-mcp-serve...](https://github.com/mayanksingh09/apollo-io-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by shariqriazz](../tools/apollo-mcp-by-shariqriazz.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/shariqriazz/apollo-io-mcp-server](https://github.com/shariqriazz/apollo-io-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP by wmarceau](../tools/apollo-mcp-by-wmarceau.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/MarceauSolutions/dev-sandbox](https://github.com/MarceauSolutions/dev-sandbox) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo MCP Plugin by apolloio](../tools/apollo-mcp-plugin-by-apolloio.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Apollo.io CLI by dipankar](../tools/apollo-io-cli-by-dipankar.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/dipankar/apollo-io-cli](https://github.com/dipankar/apollo-io-cli) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Artefact MCP](../tools/artefact-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/artefactventures/artefact-mcp-ser...](https://github.com/artefactventures/artefact-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Attio MCP by Arkel-ai](../tools/attio-mcp-by-arkel-ai.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Arkel-ai/attio-mcp-server](https://github.com/Arkel-ai/attio-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Attio MCP by hmk](../tools/attio-mcp-by-hmk.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [B2B Enrichment MCP by Aleksey-Panf](../tools/b2b-enrichment-mcp-by-aleksey-panf.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [BD Desk MCP by iaj6](../tools/bd-desk-mcp-by-iaj6.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/iaj6/bd-desk](https://github.com/iaj6/bd-desk) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Bitrix24 MCP by john7ross](../tools/bitrix24-mcp-by-john7ross.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/john7ross/BitrixMCP](https://github.com/john7ross/BitrixMCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Blitz API Open Source](../tools/blitz-api-open-source.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/malharlakdawala/blitzapi-opensour...](https://github.com/malharlakdawala/blitzapi-opensource) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [BNI MCP by alexaltovate](../tools/bni-mcp-by-alexaltovate.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/alexaltovate/bni-mcp](https://github.com/alexaltovate/bni-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by MonadsAG](../tools/capsule-crm-mcp-by-monadsag.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by soil-dev](../tools/capsule-crm-mcp-by-soil-dev.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Chatflow](../tools/chatflow.md)
chatflow.biz | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Yersat/chatflow-mcp](https://github.com/Yersat/chatflow-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CiviCRM MCP by YogiAdhik](../tools/civicrm-mcp-by-yogiadhik.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/YogiAdhik/civicrm-mcp](https://github.com/YogiAdhik/civicrm-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Clay MCP by bpw-civic](../tools/clay-mcp-by-bpw-civic.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/bpw-civic/clay-mcp-server](https://github.com/bpw-civic/clay-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Clay MCP by shanefirek](../tools/clay-mcp-by-shanefirek.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/shanefirek/clay-mcp-public](https://github.com/shanefirek/clay-mcp-public) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Clay to Instantly/Smartlead MCP](../tools/clay-to-instantly-smartlead-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/mambalabsdev/mcp-clay-to-instantl...](https://github.com/mambalabsdev/mcp-clay-to-instantly-smartlead-push) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Clint CRM MCP by Franky-Neto](../tools/clint-crm-mcp-by-franky-neto.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Franky-Neto/mcp-clint-crm](https://github.com/Franky-Neto/mcp-clint-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Close CRM MCP by pipeworx](../tools/close-crm-mcp-by-pipeworx.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/pipeworx-io/mcp-close-crm](https://github.com/pipeworx-io/mcp-close-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Codex Data MCP](../tools/codex-data-mcp.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Cognis Coldforge MCP](../tools/cognis-coldforge-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/cognis-digital/coldforge](https://github.com/cognis-digital/coldforge) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Cognis CRM Sync MCP](../tools/cognis-crm-sync-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/cognis-digital/crmsync](https://github.com/cognis-digital/crmsync) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Cognis Dealflow MCP](../tools/cognis-dealflow-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/cognis-digital/dealflow](https://github.com/cognis-digital/dealflow) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Cognis Leadforge MCP](../tools/cognis-leadforge-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/cognis-digital/leadforge](https://github.com/cognis-digital/leadforge) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Coldforge](../tools/coldforge.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Makeph/coldforge](https://github.com/Makeph/coldforge) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Coldstart](../tools/coldstart.md)
coldstart.so | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Commercient Data Lake](../tools/commercient-data-lake.md)
commercient.com | [RevOps Infra](../categories/revops-infra.md) | [https://www.npmjs.com/search?q=mcp%20hubspot](https://www.npmjs.com/search?q=mcp%20hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CompCode MCP](../tools/compcode-mcp.md)
compcode.ai | [Forecasting & Revenue](../categories/forecasting-revenue.md) | [https://github.com/compcode-ai/mcp](https://github.com/compcode-ai/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Conduyt](../tools/conduyt.md)
conduyt.app | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Crevideo Reach](../tools/crevideo-reach.md)
crevideo.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/crevideo/crevideo-reach](https://github.com/crevideo/crevideo-reach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CrispHive MCP](../tools/crisphive-mcp.md)
docs.crisphive.com | [Scheduling & Routing](../categories/scheduling-routing.md) | [https://github.com/crisphive/crisphive-mcp](https://github.com/crisphive/crisphive-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CRM AI MCP by MEOK](../tools/crm-ai-mcp-by-meok.md)
meok.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/CSOAI-ORG/crm-ai-mcp](https://github.com/CSOAI-ORG/crm-ai-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CRM Bridge MCP](../tools/crm-bridge-mcp.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CRM Solid MCP](../tools/crm-solid-mcp.md)
docs.crmsolid.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Curtis LinkedIn MCP](../tools/curtis-linkedin-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/matteolegrottaglie/curtis](https://github.com/matteolegrottaglie/curtis) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Customer Intelligence Hub](../tools/customer-intelligence-hub.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Gabrielm3/customer-intelligence-h...](https://github.com/Gabrielm3/customer-intelligence-hub) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Dolibarr MCP by sachitha7](../tools/dolibarr-mcp-by-sachitha7.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/sachitha7/mcp-server-dolibarr](https://github.com/sachitha7/mcp-server-dolibarr) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Elizabeth AI Agent](../tools/elizabeth-ai-agent.md)
github.com | [AI SDRs](../categories/ai-sdr-agents.md) | [https://github.com/gcarreno-dev/elizabeth-ai-agent](https://github.com/gcarreno-dev/elizabeth-ai-agent) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Emelia](../tools/emelia.md)
emelia.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/emelia-io/claude-outreach](https://github.com/emelia-io/claude-outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Everything Civi MCP](../tools/everything-civi-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/ananda-callhub/everything-civi](https://github.com/ananda-callhub/everything-civi) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [EZ@Work MCP](../tools/ez-work-mcp.md)
ezatwork.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/eranfinish/ezatwork-mcp](https://github.com/eranfinish/ezatwork-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [FavCRM](../tools/favcrm.md)
favcrm.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Flipfactory CRM MCP](../tools/flipfactory-crm-mcp.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Fluent MCP Servers](../tools/fluent-mcp-servers.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Dominotypist3077/fluent-mcp-serve...](https://github.com/Dominotypist3077/fluent-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Follow Up Boss MCP](../tools/follow-up-boss-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/theperrygroup/Follow-Up-Boss-MCP](https://github.com/theperrygroup/Follow-Up-Boss-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [FounderStack CRM](../tools/founderstack-crm.md)
crm-landing-three.vercel.app | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/Othunderlight/FounderStackCRM-ope...](https://github.com/Othunderlight/FounderStackCRM-open) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Fundz Agent Examples](../tools/fundz-agent-examples.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Fund-z/agent-examples](https://github.com/Fund-z/agent-examples) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Gmail Outreach MCP by brandononchain](../tools/gmail-outreach-mcp-by-brandononchain.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/brandononchain/gmail-mcp-agent](https://github.com/brandononchain/gmail-mcp-agent) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by elitedcs](../tools/gohighlevel-mcp-by-elitedcs.md)
elitedcs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by NightSquawk](../tools/gohighlevel-mcp-by-nightsquawk.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/NightSquawk/gohighlevel-mcp-serve...](https://github.com/NightSquawk/gohighlevel-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GoHighLevel MCP by rockurbusinesscs](../tools/gohighlevel-mcp-by-rockurbusinesscs.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/rockurbusinesscs-ship-it/gohighle...](https://github.com/rockurbusinesscs-ship-it/gohighlevel-mcp-starter) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GTM Alpha MCP](../tools/gtm-alpha-mcp.md)
gtmalpha.netlify.app | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GTM Copilot by archanakrishnan](../tools/gtm-copilot-by-archanakrishnan.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/archanakrishnan094-max/AI-GTM-Cop...](https://github.com/archanakrishnan094-max/AI-GTM-Copilot-End-to-End-GTM-Intelligence-CRM-Automation) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GTM MCP by aleprieto790](../tools/gtm-mcp-by-aleprieto790.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/aleprieto790-alt/gtm-mcp](https://github.com/aleprieto790-alt/gtm-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GTMos MCP by Kai8karma](../tools/gtmos-mcp-by-kai8karma.md)
kai8karma.github.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Kai8karma/gtmos-mcp](https://github.com/Kai8karma/gtmos-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Guapu](../tools/guapu.md)
guapu.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://guapu.io/conecta-tu-ia](https://guapu.io/conecta-tu-ia) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Helm AI](../tools/helm-ai.md)
gethelm.ai | [RevOps Infra](../categories/revops-infra.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HireSignal MCP](../tools/hiresignal-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/iusmuchandra/hiresignal-mcp](https://github.com/iusmuchandra/hiresignal-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by amin-ale](../tools/hubspot-mcp-by-amin-ale.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/amin-ale/hubspot-mcp-server](https://github.com/amin-ale/hubspot-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by baryhuang](../tools/hubspot-mcp-by-baryhuang.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/baryhuang/mcp-hubspot](https://github.com/baryhuang/mcp-hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by Devart](../tools/hubspot-mcp-by-devart.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by djmoore-projects](../tools/hubspot-mcp-by-djmoore-projects.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/djmoore-projects/hubspot-mcp-serv...](https://github.com/djmoore-projects/hubspot-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by mindstone-engineering](../tools/hubspot-mcp-by-mindstone-engineering.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by pipeworx](../tools/hubspot-mcp-by-pipeworx.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/pipeworx-io/mcp-hubspot](https://github.com/pipeworx-io/mcp-hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by rfoxes](../tools/hubspot-mcp-by-rfoxes.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [IN2 Agent MCP](../tools/in2-agent-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Indraft](../tools/indraft.md)
indraft.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://indraft.io](https://indraft.io) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Infona](../tools/infona.md)
infona.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.npmjs.com/search?q=mcp%20enrichment](https://www.npmjs.com/search?q=mcp%20enrichment) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Infosys AI CRM by ffred1962](../tools/infosys-ai-crm-by-ffred1962.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/ffred1962/infosys](https://github.com/ffred1962/infosys) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Insaight](../tools/insaight.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/spirosbax/insaight](https://github.com/spirosbax/insaight) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Intent Outreach](../tools/intent-outreach.md)
demos.intentsolutions.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/jeremylongshore/intent-outreach](https://github.com/jeremylongshore/intent-outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Iridium LinkedIn Agent](../tools/iridium-linkedin-agent.md)
iridiumhqmcp.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/nikhilkulkarni1755/iridium-linked...](https://github.com/nikhilkulkarni1755/iridium-linkedin-agent) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [JobDataLake MCP](../tools/jobdatalake-mcp.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Kaanha AI](../tools/kaanha-ai.md)
kaanha.ai | [RevOps Infra](../categories/revops-infra.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Keepsake MCP by nicolascroce](../tools/keepsake-mcp-by-nicolascroce.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Kenva](../tools/kenva.md)
kenva.app | [RevOps Infra](../categories/revops-infra.md) | [https://kenva.app](https://kenva.app) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Kordic CRM](../tools/kordic-crm.md)
kordic.io | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/meelad-diggit/kordic-modelcontext...](https://github.com/meelad-diggit/kordic-modelcontextprotocol.git) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Lead Enrich MCP by carsonlabs](../tools/lead-enrich-mcp-by-carsonlabs.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/carsonlabs/leadenrich-mcp](https://github.com/carsonlabs/leadenrich-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Lead Radar](../tools/lead-radar.md)
lead-radar.fr | [Data & Enrichment](../categories/data-enrichment.md) | [https://lead-radar.fr](https://lead-radar.fr) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LeadConnector MCP by pipeworx](../tools/leadconnector-mcp-by-pipeworx.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/pipeworx-io/mcp-leadconnector](https://github.com/pipeworx-io/mcp-leadconnector) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Leadcraft MCP](../tools/leadcraft-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Lakshya330-sudo/leadcraft](https://github.com/Lakshya330-sudo/leadcraft) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Leadgen MCP by koolninad](../tools/leadgen-mcp-by-koolninad.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/koolninad/leadgen-mcp](https://github.com/koolninad/leadgen-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Leadhound API](../tools/leadhound-api.md)
leadhoundapi.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://leadhoundapi.com](https://leadhoundapi.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Leadpipe MCP](../tools/leadpipe-mcp.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/automatiabcn/leadpipe-mcp](https://github.com/automatiabcn/leadpipe-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Leadzaar](../tools/leadzaar.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Techthos/leadzaar](https://github.com/Techthos/leadzaar) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedGrow](../tools/linkedgrow.md)
linkedgrow.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/DigiHold/LinkedGrow](https://github.com/DigiHold/LinkedGrow) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn ICP Discovery MCP](../tools/linkedin-icp-discovery-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/jpeslar1/linkedin-mcp-icp-discove...](https://github.com/jpeslar1/linkedin-mcp-icp-discovery) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Job Change MCP by jpeslar1](../tools/linkedin-job-change-mcp-by-jpeslar1.md)
github.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://github.com/jpeslar1/linkedin-mcp-job-change-...](https://github.com/jpeslar1/linkedin-mcp-job-change-trigger) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn MCP by gtm-api](../tools/linkedin-mcp-by-gtm-api.md)
gtm-api.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Outreach MCP by hfarazul](../tools/linkedin-outreach-mcp-by-hfarazul.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/hfarazul/linkedin-outreach-mcp](https://github.com/hfarazul/linkedin-outreach-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedIn Outreach MCP by MEOK](../tools/linkedin-outreach-mcp-by-meok.md)
meok.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/CSOAI-ORG/linkedin-outreach-mcp](https://github.com/CSOAI-ORG/linkedin-outreach-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedNav](../tools/linkednav.md)
linkednav.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/linglistack/linkednav-mcp](https://github.com/linglistack/linkednav-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkupAPI LinkedIn Skills](../tools/linkupapi-linkedin-skills.md)
linkupapi.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/claude-dev-code/claude-skills-lin...](https://github.com/claude-dev-code/claude-skills-linkedin) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Little Green Light MCP](../tools/little-green-light-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/WillHeadlee/Little-Green-Light-MC...](https://github.com/WillHeadlee/Little-Green-Light-MCP-Server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Livespace CRM MCP](../tools/livespace-crm-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/proAutomator/livespace-crm-mcp](https://github.com/proAutomator/livespace-crm-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Local MCP CRM](../tools/local-mcp-crm.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/bhairavaa/local-mcp-crm](https://github.com/bhairavaa/local-mcp-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Lookaberry GTM MCP](../tools/lookaberry-gtm-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/lucasmartins-ai/lookaberry](https://github.com/lucasmartins-ai/lookaberry) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Maasy](../tools/maasy.md)
maasy.co | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Jbelieve/mcp-server](https://github.com/Jbelieve/mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Magellan MCP by sorrek](../tools/magellan-mcp-by-sorrek.md)
magellandata.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/sorrek/mcp](https://github.com/sorrek/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Magpipe](../tools/magpipe.md)
magpipe.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/elagerway/magpipe](https://github.com/elagerway/magpipe) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mamba Domain Deliverability MCP](../tools/mamba-domain-deliverability-mcp.md)
github.com | [Email Deliverability](../categories/email-deliverability.md) | [https://github.com/mambalabsdev/mcp-domain-deliverab...](https://github.com/mambalabsdev/mcp-domain-deliverability-checker) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mamba Firmographic Enricher MCP](../tools/mamba-firmographic-enricher-mcp.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mamba GTM Hiring Signal MCP](../tools/mamba-gtm-hiring-signal-mcp.md)
github.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mamba GTM Job Discovery MCP](../tools/mamba-gtm-job-discovery-mcp.md)
mambabuilt.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mamba GTM Suite MCP](../tools/mamba-gtm-suite-mcp.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mamba Tech Stack Signal MCP](../tools/mamba-tech-stack-signal-mcp.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/mambalabsdev/mcp-gtm-tech-stack-s...](https://github.com/mambalabsdev/mcp-gtm-tech-stack-signal-scraper) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Max MCP by Digital Crew](../tools/max-mcp-by-digital-crew.md)
max-mcp-server.vercel.app | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Digital-Crew-Technologies/max-mcp...](https://github.com/Digital-Crew-Technologies/max-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCP Force by RapidoCloud](../tools/mcp-force-by-rapidocloud.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/RapidoCloud/mcp-force](https://github.com/RapidoCloud/mcp-force) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCP-Salesforce by smn2gnt](../tools/mcp-salesforce-by-smn2gnt.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCPCloud CLI](../tools/mcpcloud-cli.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20enrichment](https://www.npmjs.com/search?q=mcp%20enrichment) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mesh](../tools/mesh.md)
me.sh | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/mesh/mesh-mcp](https://github.com/mesh/mesh-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Method CRM MCP](../tools/method-crm-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/avisangle/method-crm-mcp-workers](https://github.com/avisangle/method-crm-mcp-workers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Misarreach](../tools/misarreach.md)
misarreach.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Morphed](../tools/morphed.md)
morphed.io | [RevOps Infra](../categories/revops-infra.md) | [https://morphed.io/mcp](https://morphed.io/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Munin](../tools/munin.md)
getmunin.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/getmunin/munin](https://github.com/getmunin/munin) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [n47vc MCP Suite](../tools/n47vc-mcp-suite.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/n47vc/mcp](https://github.com/n47vc/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nevent MCP](../tools/nevent-mcp.md)
nevent.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/nevent-dev/mcp-nevent](https://github.com/nevent-dev/mcp-nevent) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nimbus](../tools/nimbus.md)
testnimbus.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/nimbus-solution/nimbus](https://github.com/nimbus-solution/nimbus) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [NirmahGTM](../tools/nirmahgtm.md)
github.com | [Signals & Intent](../categories/signals-intent-abm.md) | [https://github.com/AnjaliPPal/NirmahGTM](https://github.com/AnjaliPPal/NirmahGTM) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nuph](../tools/nuph.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/teslaeas/nuph-mcp-server](https://github.com/teslaeas/nuph-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nynch MCP](../tools/nynch-mcp.md)
nynch.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/peterod99/nynch-mcp-server](https://github.com/peterod99/nynch-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Ocean.io Agent CLI](../tools/ocean-io-agent-cli.md)
ocean.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/bcharleson/ocean-agent-cli](https://github.com/bcharleson/ocean-agent-cli) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Odoo MCP by pipeworx](../tools/odoo-mcp-by-pipeworx.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/pipeworx-io/mcp-odoo](https://github.com/pipeworx-io/mcp-odoo) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Oisha OS](../tools/oisha-os.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/baxtiyorjongaziyev/oisha-os](https://github.com/baxtiyorjongaziyev/oisha-os) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Open Sales Stack MCP by ekas](../tools/open-sales-stack-mcp-by-ekas.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [OpsDoctor](../tools/opsdoctor.md)
opsdoctor.app | [RevOps Infra](../categories/revops-infra.md) | [https://github.com/jhicks935-lab/resolution-ai](https://github.com/jhicks935-lab/resolution-ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outbound Engine MCP by closermethod](../tools/outbound-engine-mcp-by-closermethod.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/closermethod/outbound-engine-mcp](https://github.com/closermethod/outbound-engine-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outreach Deliverability MCP by closermethod](../tools/outreach-deliverability-mcp-by-closermethod.md)
github.com | [Email Deliverability](../categories/email-deliverability.md) | [https://github.com/closermethod/outreach-deliverabil...](https://github.com/closermethod/outreach-deliverability-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outreach MCP by CData](../tools/outreach-mcp-by-cdata.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/CDataSoftware/outreach.io-mcp-ser...](https://github.com/CDataSoftware/outreach.io-mcp-server-by-cdata) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outreach MCP by mindstone-engineering](../tools/outreach-mcp-by-mindstone-engineering.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20outreach](https://www.npmjs.com/search?q=mcp-server%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outreacher](../tools/outreacher.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/technicallypete/outreacher](https://github.com/technicallypete/outreacher) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PaidSync MCP](../tools/paidsync-mcp.md)
paidsync.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/PaidSync/paidsync-mcp](https://github.com/PaidSync/paidsync-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Perfex CRM MCP](../tools/perfex-crm-mcp.md)
themesic.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/themesic/perfex-rest-api-examples](https://github.com/themesic/perfex-rest-api-examples) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PersuadioAI](../tools/persuadioai.md)
persuadioai.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/mannyfernandezvc/persuadioai-plat...](https://github.com/mannyfernandezvc/persuadioai-platform) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Pipedrive MCP by comma-compliance](../tools/pipedrive-mcp-by-comma-compliance.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/comma-compliance/pipedrive-mcp](https://github.com/comma-compliance/pipedrive-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Pipedrive MCP by Teapot-Agency](../tools/pipedrive-mcp-by-teapot-agency.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Teapot-Agency/mcp_pipedrive](https://github.com/Teapot-Agency/mcp_pipedrive) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Planhat MCP by da-troll](../tools/planhat-mcp-by-da-troll.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/da-troll/Planhat-MCP](https://github.com/da-troll/Planhat-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Plixana](../tools/plixana.md)
plixana.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://plixana.com/conecta-tu-ia](https://plixana.com/conecta-tu-ia) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Ploomes MCP by victorbenazzi](../tools/ploomes-mcp-by-victorbenazzi.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/victorbenazzi/ploomes-mcp-server](https://github.com/victorbenazzi/ploomes-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Potarix Enricher](../tools/potarix-enricher.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/Potarix/potarix-mcp](https://github.com/Potarix/potarix-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Prism Enrichment](../tools/prism-enrichment.md)
enrich.gocreativeai.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://enrich.gocreativeai.com](https://enrich.gocreativeai.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Prospecting Agent by B-Kirb](../tools/prospecting-agent-by-b-kirb.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/B-Kirb/prospecting-agent](https://github.com/B-Kirb/prospecting-agent) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Prospector MCP by dremnik](../tools/prospector-mcp-by-dremnik.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/dremnik/prospector](https://github.com/dremnik/prospector) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PulseAgent MCP](../tools/pulseagent-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/iPythoning/pulseagent-mcp-server](https://github.com/iPythoning/pulseagent-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RapidStart CRM MCP](../tools/rapidstart-crm-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/forceworks/rapidstart-mcp-server](https://github.com/forceworks/rapidstart-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Relm CRM](../tools/relm-crm.md)
relmcrm.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://relmcrm.com](https://relmcrm.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RepScale](../tools/repscale.md)
repscale.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://repscale.ai](https://repscale.ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RetailCRM MCP](../tools/retailcrm-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/theYahia/retailcrm-mcp](https://github.com/theYahia/retailcrm-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RevOps Eval](../tools/revops-eval.md)
revopseval.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/elijeangilles/revops-skills](https://github.com/elijeangilles/revops-skills) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [S.C.A.L.A.](../tools/s-c-a-l-a.md)
get-scala.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Sales Enablement Plugin by jbalbu01](../tools/sales-enablement-plugin-by-jbalbu01.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/jbalbu01/sales-enablement-plugin](https://github.com/jbalbu01/sales-enablement-plugin) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Sales Intelligence MCP by Aria Agentworks](../tools/sales-intelligence-mcp-by-aria-agentworks.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/aria-agentworks/sales-intelligenc...](https://github.com/aria-agentworks/sales-intelligence-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesbot LinkedIn MCP](../tools/salesbot-linkedin-mcp.md)
salesbot.cz | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Kubis010/linkedin-mcp-server-sale...](https://github.com/Kubis010/linkedin-mcp-server-salesbot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce CLI MCP](../tools/salesforce-cli-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Cloud MCP by aaronsb](../tools/salesforce-cloud-mcp-by-aaronsb.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/aaronsb/salesforce-cloud](https://github.com/aaronsb/salesforce-cloud) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Commerce Cloud MCP by brinzl](../tools/salesforce-commerce-cloud-mcp-by-brinzl.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/brinzl/commercecloud-mcp-server](https://github.com/brinzl/commercecloud-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Commerce Cloud MCP by vinkius-labs](../tools/salesforce-commerce-cloud-mcp-by-vinkius-labs.md)
vinkius.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/vinkius-labs/salesforce-commerce-...](https://github.com/vinkius-labs/salesforce-commerce-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Data Cloud MCP by rishiganesh25](../tools/salesforce-data-cloud-mcp-by-rishiganesh25.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/rishiganesh25/data360-mcp](https://github.com/rishiganesh25/data360-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Docs MCP by Sanket](../tools/salesforce-docs-mcp-by-sanket.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/SalesforceDiariesBySanket/salesfo...](https://github.com/SalesforceDiariesBySanket/salesforce-docs-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Hosted Custom MCP by Sanket](../tools/salesforce-hosted-custom-mcp-by-sanket.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/SalesforceDiariesBySanket/Salesfo...](https://github.com/SalesforceDiariesBySanket/Salesforce-Hosted-Custom-Mcp-Server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by Devart](../tools/salesforce-marketing-cloud-mcp-by-devart.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-salesforce-marketing-cloud) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by salesforcebob](../tools/salesforce-marketing-cloud-mcp-by-salesforcebob.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/salesforcebob/Salesforce-Marketin...](https://github.com/salesforcebob/Salesforce-Marketing-Cloud-Engagement-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by vinkius-labs](../tools/salesforce-marketing-cloud-mcp-by-vinkius-labs.md)
vinkius.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/vinkius-labs/salesforce-marketing...](https://github.com/vinkius-labs/salesforce-marketing-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Auto Auth by kugamon](../tools/salesforce-mcp-auto-auth-by-kugamon.md)
pypi.org | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/kugamon/salesforce-mcp-auto-auth-...](https://github.com/kugamon/salesforce-mcp-auto-auth-chrome) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by aaron-pienza](../tools/salesforce-mcp-by-aaron-pienza.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by advancedcommunities](../tools/salesforce-mcp-by-advancedcommunities.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/advancedcommunities/salesforce-mc...](https://github.com/advancedcommunities/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by AiondaDotCom](../tools/salesforce-mcp-by-aiondadotcom.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/AiondaDotCom/mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by alfe](../tools/salesforce-mcp-by-alfe.md)
alfe.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20salesforce](https://www.npmjs.com/search?q=mcp%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by boejucci](../tools/salesforce-mcp-by-boejucci.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by Devart](../tools/salesforce-mcp-by-devart.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by imazhar101](../tools/salesforce-mcp-by-imazhar101.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by jaworjar95](../tools/salesforce-mcp-by-jaworjar95.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/jaworjar95/salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by kablewy](../tools/salesforce-mcp-by-kablewy.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/kablewy/salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by KirtiJha](../tools/salesforce-mcp-by-kirtijha.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20salesforce](https://www.npmjs.com/search?q=mcp%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by LokiMCPUniverse](../tools/salesforce-mcp-by-lokimcpuniverse.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/LokiMCPUniverse/salesforce-mcp-se...](https://github.com/LokiMCPUniverse/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by mindstone](../tools/salesforce-mcp-by-mindstone.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by pipeworx](../tools/salesforce-mcp-by-pipeworx.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/pipeworx-io/mcp-salesforce](https://github.com/pipeworx-io/mcp-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by rohithvemulapally](../tools/salesforce-mcp-by-rohithvemulapally.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by starcatmeow](../tools/salesforce-mcp-by-starcatmeow.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by suraj20028](../tools/salesforce-mcp-by-suraj20028.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/suraj20028/Salesforce-MCP](https://github.com/suraj20028/Salesforce-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by SurajAdsul](../tools/salesforce-mcp-by-surajadsul.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/SurajAdsul/mcp-server-salesforce](https://github.com/SurajAdsul/mcp-server-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by timescale](../tools/salesforce-mcp-by-timescale.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/timescale/tiger-salesforce-mcp-se...](https://github.com/timescale/tiger-salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by tomnagengast](../tools/salesforce-mcp-by-tomnagengast.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/tomnagengast/mcp-server-salesforc...](https://github.com/tomnagengast/mcp-server-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by tsmztech](../tools/salesforce-mcp-by-tsmztech.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by vinkius-labs](../tools/salesforce-mcp-by-vinkius-labs.md)
vinkius.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/vinkius-labs/salesforce-mcp](https://github.com/vinkius-labs/salesforce-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Lib by Damecek](../tools/salesforce-mcp-lib-by-damecek.md)
context7.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/Damecek/salesforce-mcp-lib](https://github.com/Damecek/salesforce-mcp-lib) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Security Toolkit](../tools/salesforce-mcp-security-toolkit.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/ccmalcom/SFDC-MCP-Security-Toolki...](https://github.com/ccmalcom/SFDC-MCP-Security-Toolkit) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Pardot MCP by DaniilMai](../tools/salesforce-pardot-mcp-by-daniilmai.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/DaniilMai/salesforce-pardot-mcp](https://github.com/DaniilMai/salesforce-pardot-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Remote MCP by tsmztech](../tools/salesforce-remote-mcp-by-tsmztech.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/tsmztech/salesforce-remote-mcp-cl...](https://github.com/tsmztech/salesforce-remote-mcp-cloudflare) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ScraperCity](../tools/scrapercity.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SeldonFrame](../tools/seldonframe.md)
seldonframe.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ServiceAgent](../tools/serviceagent.md)
serviceagent.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://serviceagent.ai](https://serviceagent.ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Setu Email MCP by gitmanhimanshu](../tools/setu-email-mcp-by-gitmanhimanshu.md)
setu.mimanasa.online | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/gitmanhimanshu/Email_automation](https://github.com/gitmanhimanshu/Email_automation) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Siftable](../tools/siftable.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SIMOSphere](../tools/simosphere.md)
simosphereai.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Snov.io MCP by narkov](../tools/snov-io-mcp-by-narkov.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/narkov/snov-io-mcp-server](https://github.com/narkov/snov-io-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Social Profile Enrichment API](../tools/social-profile-enrichment-api.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/Br0ski777/social-profile-x402](https://github.com/Br0ski777/social-profile-x402) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Stacks AI](../tools/stacks-ai.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/jentrix-au/stacks-ai](https://github.com/jentrix-au/stacks-ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Studiomeyer CRM](../tools/studiomeyer-crm.md)
studiomeyer.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/studiomeyer-io/studiomeyer-crm](https://github.com/studiomeyer-io/studiomeyer-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Synapse CRM MCP by NimbleBrain](../tools/synapse-crm-mcp-by-nimblebrain.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/NimbleBrainInc/synapse-crm](https://github.com/NimbleBrainInc/synapse-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Teamleader MCP by BoostU](../tools/teamleader-mcp-by-boostu.md)
teamleader-mcp.boostu.be | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/boostuagency/boostu-teamleader-mc...](https://github.com/boostuagency/boostu-teamleader-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Technology Stack Detection API](../tools/technology-stack-detection-api.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/Br0ski777/tech-enrichment-x402](https://github.com/Br0ski777/tech-enrichment-x402) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Toflow](../tools/toflow.md)
toflow.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/toflow-ai/toflow-mcp](https://github.com/toflow-ai/toflow-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Tomba](../tools/tomba.md)
tomba.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/tomba-io/tomba-mcp-server](https://github.com/tomba-io/tomba-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Twenty CRM MCP](../tools/twenty-crm-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Twenty MCP Suite](../tools/twenty-mcp-suite.md)
andrewmarconi.github.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/andrewmarconi/twenty-mcp-suite](https://github.com/andrewmarconi/twenty-mcp-suite) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [UGC VZ MCP](../tools/ugc-vz-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/ugcvz/ugc-vz-mcp](https://github.com/ugcvz/ugc-vz-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Vesxo Connect](../tools/vesxo-connect.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Vibe Prospecting MCP](../tools/vibe-prospecting-mcp.md)
vibeprospecting.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/explorium-ai/vibeprospecting-mcp](https://github.com/explorium-ai/vibeprospecting-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Vinkius Lead Gen Agents](../tools/vinkius-lead-gen-agents.md)
vinkius.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/vinkius-labs/crewai-mcp-lead-gen-...](https://github.com/vinkius-labs/crewai-mcp-lead-gen-agents) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Vruum](../tools/vruum.md)
vruum.ai | [AI SDRs](../categories/ai-sdr-agents.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Vsyble](../tools/vsyble.md)
vsyble.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://www.npmjs.com/search?q=mcp%20enrichment](https://www.npmjs.com/search?q=mcp%20enrichment) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Wapiworld](../tools/wapiworld.md)
app.wapiworld.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://registry.smithery.ai/servers?q=hubspot](https://registry.smithery.ai/servers?q=hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [WarmySender](../tools/warmysender.md)
warmysender.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://warmysender.com](https://warmysender.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Well](../tools/well.md)
wellapp.ai | [RevOps Infra](../categories/revops-infra.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Whatcanido](../tools/whatcanido.md)
whatcanido.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://whatcanido.dev/agents](https://whatcanido.dev/agents) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Wokelo](../tools/wokelo.md)
wokelo.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/Wokelo-AI/Wokelo-MCP-Server](https://github.com/Wokelo-AI/Wokelo-MCP-Server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Xverum](../tools/xverum.md)
ask.xverum.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://registry.smithery.ai/servers?q=enrich](https://registry.smithery.ai/servers?q=enrich) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [YG3](../tools/yg3.md)
yg3.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/YG3-ai/yg3-mcp](https://github.com/YG3-ai/yg3-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [YouSpot](../tools/youspot.md)
youspot.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Zavora Sales Operations Skill](../tools/zavora-sales-operations-skill.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/zavora-ai/skill-sales-operations](https://github.com/zavora-ai/skill-sales-operations) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Zetadeck](../tools/zetadeck.md)
zetadeck.com | [RevOps Infra](../categories/revops-infra.md) | [https://zetadeck.com](https://zetadeck.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Zoho CRM MCP by Devart](../tools/zoho-crm-mcp-by-devart.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/devart-ai-connectivity/devart-mcp...](https://github.com/devart-ai-connectivity/devart-mcp-server-zoho-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ZOOQ](../tools/zooq.md)
zooq.dev | [Data & Enrichment](../categories/data-enrichment.md) | [https://registry.smithery.ai/servers?q=enrich](https://registry.smithery.ai/servers?q=enrich) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 982 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
