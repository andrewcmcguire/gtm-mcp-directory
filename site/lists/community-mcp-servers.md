# Community MCP servers: 103 GTM tools with a third party server

> Go to market tools where a working MCP server exists but somebody other than the vendor built it. Counted 2026-09-12 across 604 directory entries.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / The 103 GTM tools with a community MCP server

**List · 103 of 604**

## The 103 GTM tools with a community MCP server

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
| [abm.dev](../tools/abm-dev.md)
abm.dev | [Signals & Intent](../categories/signals-intent-abm.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=sales) | Auth not recorded
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
| [Apollo MCP by louis030195](../tools/apollo-mcp-by-louis030195.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Attio MCP by hmk](../tools/attio-mcp-by-hmk.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by MonadsAG](../tools/capsule-crm-mcp-by-monadsag.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by soil-dev](../tools/capsule-crm-mcp-by-soil-dev.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Clay MCP by shanefirek](../tools/clay-mcp-by-shanefirek.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/shanefirek/clay-mcp-public](https://github.com/shanefirek/clay-mcp-public) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Codex Data MCP](../tools/codex-data-mcp.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Coldstart](../tools/coldstart.md)
coldstart.so | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Conduyt](../tools/conduyt.md)
conduyt.app | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Emelia](../tools/emelia.md)
emelia.io | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/emelia-io/claude-outreach](https://github.com/emelia-io/claude-outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [FavCRM](../tools/favcrm.md)
favcrm.io | [MCP Layer](../categories/mcp-infrastructure.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Flipfactory CRM MCP](../tools/flipfactory-crm-mcp.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GTM Alpha MCP](../tools/gtm-alpha-mcp.md)
gtmalpha.netlify.app | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20gtm](https://www.npmjs.com/search?q=mcp%20gtm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by baryhuang](../tools/hubspot-mcp-by-baryhuang.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/baryhuang/mcp-hubspot](https://github.com/baryhuang/mcp-hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by rfoxes](../tools/hubspot-mcp-by-rfoxes.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20hubspot](https://www.npmjs.com/search?q=mcp-server%20hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [IN2 Agent MCP](../tools/in2-agent-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Insaight](../tools/insaight.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/spirosbax/insaight](https://github.com/spirosbax/insaight) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [JobDataLake MCP](../tools/jobdatalake-mcp.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Keepsake MCP by nicolascroce](../tools/keepsake-mcp-by-nicolascroce.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedGrow](../tools/linkedgrow.md)
linkedgrow.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://github.com/DigiHold/LinkedGrow](https://github.com/DigiHold/LinkedGrow) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Little Green Light MCP](../tools/little-green-light-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/WillHeadlee/Little-Green-Light-MC...](https://github.com/WillHeadlee/Little-Green-Light-MCP-Server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCP Force by RapidoCloud](../tools/mcp-force-by-rapidocloud.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/RapidoCloud/mcp-force](https://github.com/RapidoCloud/mcp-force) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCP-Salesforce by smn2gnt](../tools/mcp-salesforce-by-smn2gnt.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mesh](../tools/mesh.md)
me.sh | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/mesh/mesh-mcp](https://github.com/mesh/mesh-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Morphed](../tools/morphed.md)
morphed.io | [RevOps Infra](../categories/revops-infra.md) | [https://morphed.io/mcp](https://morphed.io/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Munin](../tools/munin.md)
getmunin.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/getmunin/munin](https://github.com/getmunin/munin) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nimbus](../tools/nimbus.md)
testnimbus.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/nimbus-solution/nimbus](https://github.com/nimbus-solution/nimbus) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nuph](../tools/nuph.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/teslaeas/nuph-mcp-server](https://github.com/teslaeas/nuph-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Outreacher](../tools/outreacher.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/technicallypete/outreacher](https://github.com/technicallypete/outreacher) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Pipedrive MCP by comma-compliance](../tools/pipedrive-mcp-by-comma-compliance.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/comma-compliance/pipedrive-mcp](https://github.com/comma-compliance/pipedrive-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Potarix Enricher](../tools/potarix-enricher.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/Potarix/potarix-mcp](https://github.com/Potarix/potarix-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Prism Enrichment](../tools/prism-enrichment.md)
enrich.gocreativeai.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://enrich.gocreativeai.com](https://enrich.gocreativeai.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Relm CRM](../tools/relm-crm.md)
relmcrm.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://relmcrm.com](https://relmcrm.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RepScale](../tools/repscale.md)
repscale.ai | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://repscale.ai](https://repscale.ai) | Auth not recorded
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
| [Salesforce CLI MCP](../tools/salesforce-cli-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Commerce Cloud MCP by brinzl](../tools/salesforce-commerce-cloud-mcp-by-brinzl.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/brinzl/commercecloud-mcp-server](https://github.com/brinzl/commercecloud-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Commerce Cloud MCP by vinkius-labs](../tools/salesforce-commerce-cloud-mcp-by-vinkius-labs.md)
vinkius.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/vinkius-labs/salesforce-commerce-...](https://github.com/vinkius-labs/salesforce-commerce-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Docs MCP by Sanket](../tools/salesforce-docs-mcp-by-sanket.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/SalesforceDiariesBySanket/salesfo...](https://github.com/SalesforceDiariesBySanket/salesforce-docs-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Hosted Custom MCP by Sanket](../tools/salesforce-hosted-custom-mcp-by-sanket.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/SalesforceDiariesBySanket/Salesfo...](https://github.com/SalesforceDiariesBySanket/Salesforce-Hosted-Custom-Mcp-Server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by salesforcebob](../tools/salesforce-marketing-cloud-mcp-by-salesforcebob.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/salesforcebob/Salesforce-Marketin...](https://github.com/salesforcebob/Salesforce-Marketing-Cloud-Engagement-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by vinkius-labs](../tools/salesforce-marketing-cloud-mcp-by-vinkius-labs.md)
vinkius.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/vinkius-labs/salesforce-marketing...](https://github.com/vinkius-labs/salesforce-marketing-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by advancedcommunities](../tools/salesforce-mcp-by-advancedcommunities.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/advancedcommunities/salesforce-mc...](https://github.com/advancedcommunities/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by AiondaDotCom](../tools/salesforce-mcp-by-aiondadotcom.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/AiondaDotCom/mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by jaworjar95](../tools/salesforce-mcp-by-jaworjar95.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/jaworjar95/salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by kablewy](../tools/salesforce-mcp-by-kablewy.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/kablewy/salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by rohithvemulapally](../tools/salesforce-mcp-by-rohithvemulapally.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by starcatmeow](../tools/salesforce-mcp-by-starcatmeow.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | Auth not recorded
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
| [SeldonFrame](../tools/seldonframe.md)
seldonframe.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ServiceAgent](../tools/serviceagent.md)
serviceagent.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://serviceagent.ai](https://serviceagent.ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Siftable](../tools/siftable.md)
npmjs.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SIMOSphere](../tools/simosphere.md)
simosphereai.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Social Profile Enrichment API](../tools/social-profile-enrichment-api.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/Br0ski777/social-profile-x402](https://github.com/Br0ski777/social-profile-x402) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Technology Stack Detection API](../tools/technology-stack-detection-api.md)
github.com | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/Br0ski777/tech-enrichment-x402](https://github.com/Br0ski777/tech-enrichment-x402) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Tomba](../tools/tomba.md)
tomba.io | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/tomba-io/tomba-mcp-server](https://github.com/tomba-io/tomba-mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Twenty CRM MCP](../tools/twenty-crm-mcp.md)
github.com | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | Auth not recorded
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
| [WarmySender](../tools/warmysender.md)
warmysender.com | [Engagement & Outbound](../categories/engagement-outbound.md) | [https://warmysender.com](https://warmysender.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Whatcanido](../tools/whatcanido.md)
whatcanido.dev | [MCP Layer](../categories/mcp-infrastructure.md) | [https://whatcanido.dev/agents](https://whatcanido.dev/agents) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Wokelo](../tools/wokelo.md)
wokelo.ai | [Data & Enrichment](../categories/data-enrichment.md) | [https://github.com/Wokelo-AI/Wokelo-MCP-Server](https://github.com/Wokelo-AI/Wokelo-MCP-Server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [YG3](../tools/yg3.md)
yg3.ai | [MCP Layer](../categories/mcp-infrastructure.md) | [https://github.com/YG3-ai/yg3-mcp](https://github.com/YG3-ai/yg3-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Zetadeck](../tools/zetadeck.md)
zetadeck.com | [RevOps Infra](../categories/revops-infra.md) | [https://zetadeck.com](https://zetadeck.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ZOOQ](../tools/zooq.md)
zooq.dev | [Data & Enrichment](../categories/data-enrichment.md) | [https://registry.smithery.ai/servers?q=enrich](https://registry.smithery.ai/servers?q=enrich) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 604 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
