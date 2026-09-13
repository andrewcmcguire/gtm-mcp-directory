# GTM MCP servers with no auth model recorded: 67 tools, counted

> 67 of the 264 GTM tools with an MCP server use an auth model that is not recorded. The verbatim auth field for each one is printed beside it. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / GTM MCP servers with no auth model recorded

**List · 67 of 514**

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
| [Anyquery](../tools/anyquery.md)
anyquery.dev | [Community MCP](../mcp/community.md) | [https://github.com/julien040/anyquery](https://github.com/julien040/anyquery) | blank | [Gate unknown](../gates/unknown.md) |
| [Apex Log MCP by Certinia](../tools/apex-log-mcp-by-certinia.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://github.com/certinia/debug-log-analyzer-mcp](https://github.com/certinia/debug-log-analyzer-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Apex MCP SDK by bfmvsa](../tools/apex-mcp-sdk-by-bfmvsa.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/bfmvsa/mcp-apex-sdk](https://github.com/bfmvsa/mcp-apex-sdk) | blank | [Gate unknown](../gates/unknown.md) |
| [Capsule CRM MCP by soil-dev](../tools/capsule-crm-mcp-by-soil-dev.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | blank | [Gate unknown](../gates/unknown.md) |
| [Coldstart](../tools/coldstart.md)
coldstart.so | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | blank | [Gate unknown](../gates/unknown.md) |
| [Conduyt](../tools/conduyt.md)
conduyt.app | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Flipfactory CRM MCP](../tools/flipfactory-crm-mcp.md)
npmjs.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [HubSpot MCP by baryhuang](../tools/hubspot-mcp-by-baryhuang.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/baryhuang/mcp-hubspot](https://github.com/baryhuang/mcp-hubspot) | blank | [Gate unknown](../gates/unknown.md) |
| [IN2 Agent MCP](../tools/in2-agent-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp-server%20salesfor...](https://www.npmjs.com/search?q=mcp-server%20salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Insaight](../tools/insaight.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/spirosbax/insaight](https://github.com/spirosbax/insaight) | blank | [Gate unknown](../gates/unknown.md) |
| [LinkedGrow](../tools/linkedgrow.md)
linkedgrow.ai | [Community MCP](../mcp/community.md) | [https://github.com/DigiHold/LinkedGrow](https://github.com/DigiHold/LinkedGrow) | blank | [Gate unknown](../gates/unknown.md) |
| [MCP Force by RapidoCloud](../tools/mcp-force-by-rapidocloud.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/RapidoCloud/mcp-force](https://github.com/RapidoCloud/mcp-force) | blank | [Gate unknown](../gates/unknown.md) |
| [MCP-Salesforce by smn2gnt](../tools/mcp-salesforce-by-smn2gnt.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/smn2gnt/MCP-Salesforce](https://github.com/smn2gnt/MCP-Salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Mesh](../tools/mesh.md)
me.sh | [Community MCP](../mcp/community.md) | [https://github.com/mesh/mesh-mcp](https://github.com/mesh/mesh-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Morphed](../tools/morphed.md)
morphed.io | [Community MCP](../mcp/community.md) | [https://morphed.io/mcp](https://morphed.io/mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Munin](../tools/munin.md)
getmunin.com | [Community MCP](../mcp/community.md) | [https://github.com/getmunin/munin](https://github.com/getmunin/munin) | blank | [Gate unknown](../gates/unknown.md) |
| [Nimbus](../tools/nimbus.md)
testnimbus.dev | [Community MCP](../mcp/community.md) | [https://github.com/nimbus-solution/nimbus](https://github.com/nimbus-solution/nimbus) | blank | [Gate unknown](../gates/unknown.md) |
| [Pipedrive MCP by comma-compliance](../tools/pipedrive-mcp-by-comma-compliance.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/comma-compliance/pipedrive-mcp](https://github.com/comma-compliance/pipedrive-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [S.C.A.L.A.](../tools/s-c-a-l-a.md)
get-scala.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20crm](https://www.npmjs.com/search?q=mcp%20crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Sales Enablement Plugin by jbalbu01](../tools/sales-enablement-plugin-by-jbalbu01.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jbalbu01/sales-enablement-plugin](https://github.com/jbalbu01/sales-enablement-plugin) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce CLI MCP](../tools/salesforce-cli-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/salesforcecli/mcp](https://github.com/salesforcecli/mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Docs MCP by Sanket](../tools/salesforce-docs-mcp-by-sanket.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SalesforceDiariesBySanket/salesfo...](https://github.com/SalesforceDiariesBySanket/salesforce-docs-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce Marketing Cloud MCP by salesforcebob](../tools/salesforce-marketing-cloud-mcp-by-salesforcebob.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/salesforcebob/Salesforce-Marketin...](https://github.com/salesforcebob/Salesforce-Marketing-Cloud-Engagement-MCP) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by advancedcommunities](../tools/salesforce-mcp-by-advancedcommunities.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/advancedcommunities/salesforce-mc...](https://github.com/advancedcommunities/salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by AiondaDotCom](../tools/salesforce-mcp-by-aiondadotcom.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/AiondaDotCom/mcp-salesforce](https://github.com/AiondaDotCom/mcp-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by jaworjar95](../tools/salesforce-mcp-by-jaworjar95.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/jaworjar95/salesforce-mcp-server](https://github.com/jaworjar95/salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by kablewy](../tools/salesforce-mcp-by-kablewy.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/kablewy/salesforce-mcp-server](https://github.com/kablewy/salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by SurajAdsul](../tools/salesforce-mcp-by-surajadsul.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SurajAdsul/mcp-server-salesforce](https://github.com/SurajAdsul/mcp-server-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by timescale](../tools/salesforce-mcp-by-timescale.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/timescale/tiger-salesforce-mcp-se...](https://github.com/timescale/tiger-salesforce-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP by tsmztech](../tools/salesforce-mcp-by-tsmztech.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/tsmztech/mcp-server-salesforce](https://github.com/tsmztech/mcp-server-salesforce) | blank | [Gate unknown](../gates/unknown.md) |
| [Salesforce MCP Lib by Damecek](../tools/salesforce-mcp-lib-by-damecek.md)
context7.com | [Community MCP](../mcp/community.md) | [https://github.com/Damecek/salesforce-mcp-lib](https://github.com/Damecek/salesforce-mcp-lib) | blank | [Gate unknown](../gates/unknown.md) |
| [SIMOSphere](../tools/simosphere.md)
simosphereai.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | blank | [Gate unknown](../gates/unknown.md) |
| [Tomba](../tools/tomba.md)
tomba.io | [Community MCP](../mcp/community.md) | [https://github.com/tomba-io/tomba-mcp-server](https://github.com/tomba-io/tomba-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Twenty CRM MCP](../tools/twenty-crm-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mhenry3164/twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server) | blank | [Gate unknown](../gates/unknown.md) |
| [Vibe Prospecting MCP](../tools/vibe-prospecting-mcp.md)
vibeprospecting.ai | [Community MCP](../mcp/community.md) | [https://github.com/explorium-ai/vibeprospecting-mcp](https://github.com/explorium-ai/vibeprospecting-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [WarmySender](../tools/warmysender.md)
warmysender.com | [Community MCP](../mcp/community.md) | [https://warmysender.com](https://warmysender.com) | blank | [Gate unknown](../gates/unknown.md) |
| [Wokelo](../tools/wokelo.md)
wokelo.ai | [Community MCP](../mcp/community.md) | [https://github.com/Wokelo-AI/Wokelo-MCP-Server](https://github.com/Wokelo-AI/Wokelo-MCP-Server) | blank | [Gate unknown](../gates/unknown.md) |
| [YG3](../tools/yg3.md)
yg3.ai | [Community MCP](../mcp/community.md) | [https://github.com/YG3-ai/yg3-mcp](https://github.com/YG3-ai/yg3-mcp) | blank | [Gate unknown](../gates/unknown.md) |
| [Zetadeck](../tools/zetadeck.md)
zetadeck.com | [Community MCP](../mcp/community.md) | [https://zetadeck.com](https://zetadeck.com) | blank | [Gate unknown](../gates/unknown.md) |

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 514 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
