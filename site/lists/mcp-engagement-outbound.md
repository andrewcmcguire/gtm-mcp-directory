# Engagement & Outbound tools with MCP servers: 81 of 173, counted

> 81 of the 173 engagement & outbound tools in The GTM MCP Directory have an MCP server: 23 official and 58 community. The server URL, auth model and access gate for each. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / Engagement & Outbound tools with an MCP server

**List · 81 of 1,251**

## Engagement & Outbound tools with an MCP server

The execution layer - sequencers, parallel dialers, and LinkedIn automation tools that actually put messages and calls in front of prospects. MCP maturity here is split sharply: the big sales-engagement platforms (Salesloft, Outreach, lemlist) and several LinkedIn tools have shipped real official servers in 2026, while most parallel dialers and mid-market cold-email tools have none. 81 of 173 entries in this category are reachable by an agent: 23 through a server the vendor maintains and 58 through one somebody else built. The category is tagged most often with Run an email sequence. [See the full category page](../categories/engagement-outbound.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Autobound](../tools/autobound.md)
autobound.ai | [Official MCP](../mcp/official.md) | [https://www.autobound.ai/integrations/mcp](https://www.autobound.ai/integrations/mcp) +1 more | API key
api key via an AUTOBOUND_API_KEY environment variable in the MCP client config. | [Free to start](../gates/free.md) |
| [HeyReach](../tools/heyreach.md)
heyreach.io | [Official MCP](../mcp/official.md) | [https://mcp.heyreach.io/mcp](https://mcp.heyreach.io/mcp) +2 more | OAuth or an API key
workspace-scoped "MCP key" + connection URL (API-key-style, not OAuth) | [Paid, self-serve](../gates/paid.md) |
| [Instantly](../tools/instantly.md)
instantly.ai | [Official MCP](../mcp/official.md) | [https://mcp.instantly.ai/mcp](https://mcp.instantly.ai/mcp) +1 more | API key
api key (generated in Instantly Settings > Integrations > API Keys) | [Paid, self-serve](../gates/paid.md) |
| [JustCall](../tools/justcall.md)
justcall.io | [Official MCP](../mcp/official.md) | [https://mcp.justcall.host/mcp](https://mcp.justcall.host/mcp) +2 more | API key
api key. The vendor's docs show an Authorization header of the form "Bearer... | [Paid, self-serve](../gates/paid.md) |
| [La Growth Machine](../tools/la-growth-machine.md)
lagrowthmachine.com | [Official MCP](../mcp/official.md) | [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system) +1 more | OAuth
OAuth - no API key needed; first use opens a browser sign-in directly to the user's La... | [Paid, self-serve](../gates/paid.md) |
| [lemlist](../tools/lemlist.md)
lemlist.com | [Official MCP](../mcp/official.md) | [https://app.lemlist.com/mcp](https://app.lemlist.com/mcp) +1 more | OAuth or an API key
OAuth (browser-based PKCE flow, recommended) or API key via X-API-Key header | [Paid, self-serve](../gates/paid.md) |
| [Mixmax](../tools/mixmax.md)
mixmax.com | [Official MCP](../mcp/official.md) | [https://mcp.mixmax.com/mcp](https://mcp.mixmax.com/mcp) +2 more | OAuth
OAuth 2.0 authorization code flow, scoped to the connecting user's account. Read-only. | [Paid, self-serve](../gates/paid.md) |
| [PhantomBuster](../tools/phantombuster.md)
phantombuster.com | [Official MCP](../mcp/official.md) | [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server) +1 more | OAuth
OAuth - first connection redirects to PhantomBuster sign-in/authorization, then workspace... | [Paid, self-serve](../gates/paid.md) |
| [Reply.io](../tools/reply-io.md)
reply.io | [Official MCP](../mcp/official.md) | [https://reply.io/mcp/](https://reply.io/mcp/) +1 more | API key
api key (personal API key over HTTPS, included in free trial) | [Paid, self-serve](../gates/paid.md) |
| [RingCentral App Connect MCP](../tools/ringcentral-app-connect-mcp.md)
ringcentral.com | [Official MCP](../mcp/official.md) | [https://unified-crm-extension.labs.ringcentral.com/m...](https://unified-crm-extension.labs.ringcentral.com/mcp) +3 more | OAuth
oauth plus a second, separate CRM link. The docs describe a two-layer model: RingCentral... | [Paid, self-serve](../gates/paid.md) |
| [Salesforge](../tools/salesforge.md)
salesforge.ai | [Official MCP](../mcp/official.md) | [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp) | API key
api key via HTTP header (X-Salesforge-Key) | [Paid, self-serve](../gates/paid.md) |
| [Saleshandy](../tools/saleshandy.md)
saleshandy.com | [Official MCP](../mcp/official.md) | [https://mcp.saleshandy.com/mcp](https://mcp.saleshandy.com/mcp) +3 more | OAuth or an API key
oauth, with an api key fallback. The developer docs state "Saleshandy MCP uses OAuth for... | [Paid, self-serve](../gates/paid.md) |
| [Skyp.ai](../tools/skyp-ai.md)
skyp.ai | [Official MCP](../mcp/official.md) | [https://api.skyp.ai/mcp](https://api.skyp.ai/mcp) +3 more | OAuth or an API key
api key (X-API-Key or Authorization Bearer header) or OAuth. The endpoint's own 401 body... | [Paid, self-serve](../gates/paid.md) |
| [Smartlead](../tools/smartlead.md)
smartlead.ai | [Official MCP](../mcp/official.md) | [https://helpcenter.smartlead.ai/en/articles/300-smar...](https://helpcenter.smartlead.ai/en/articles/300-smartlead-mcp-server) +3 more | API key
api key, passed as the user_api_key query parameter on the SSE endpoint URL; SSE... | [Paid, self-serve](../gates/paid.md) |
| [Super Send](../tools/super-send.md)
supersend.io | [Official MCP](../mcp/official.md) | [https://mcp.supersend.io/mcp](https://mcp.supersend.io/mcp) +1 more | API key
api key, Streamable HTTP transport | [Paid, self-serve](../gates/paid.md) |
| [Waalaxy](../tools/waalaxy.md)
waalaxy.com | [Official MCP](../mcp/official.md) | [https://docs.waalaxy.com/mcp-server](https://docs.waalaxy.com/mcp-server) +1 more | OAuth or an API key
user-based OAuth 2.1 via magic-link sign-in; vendor docs explicitly state bearer API keys... | [Paid, self-serve](../gates/paid.md) |
| [Woodpecker](../tools/woodpecker.md)
woodpecker.co | [Official MCP](../mcp/official.md) | [https://github.com/Woodpeckerco/woodpecker-mcp-serve...](https://github.com/Woodpeckerco/woodpecker-mcp-server) +2 more | OAuth or an API key
hosted OAuth-style flow (Claude-specific) or self-hosted Docker setup using a Woodpecker... | [Paid, self-serve](../gates/paid.md) |
| [Amplemarket](../tools/amplemarket.md)
amplemarket.com | [Official MCP](../mcp/official.md) | [https://mcp.amplemarket.com/mcp](https://mcp.amplemarket.com/mcp) +3 more | OAuth
OAuth 2.0 sign-in with the Amplemarket account in the browser; the knowledge article says... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Dialpad](../tools/dialpad.md)
dialpad.com | [Official MCP](../mcp/official.md) | [https://mcp-public.us.karehq.com/mcp](https://mcp-public.us.karehq.com/mcp) +3 more | OAuth
oauth. The docs state the server is hosted by Dialpad, supports Dynamic Client... | [Enterprise leaning](../gates/enterprise-leaning.md) |
| [Apollo.io Sequences (Emailer Campaigns)](../tools/apollo-io-sequences.md)
apollo.io | [Official MCP](../mcp/official.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) +1 more | OAuth
OAuth (Apollo.io sign-in/authorization flow; no API key required for this MCP) | [Enterprise only](../gates/enterprise-only.md) |
| [Nooks](../tools/nooks.md)
nooks.ai | [Official MCP](../mcp/official.md) | [https://mcp.nooks.in/mcp](https://mcp.nooks.in/mcp) +1 more | OAuth
OAuth 2.0 authorization code with PKCE (S256), issuer https://oauth.nooks.in, per the... | [Enterprise only](../gates/enterprise-only.md) |
| [Outreach](../tools/outreach.md)
outreach.ai | [Official MCP](../mcp/official.md) | [https://api.outreach.io/mcp/](https://api.outreach.io/mcp/) +1 more | OAuth
OAuth 2.1 with Dynamic Client Registration; also requires the org-level "Amplify" add-on... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesloft](../tools/salesloft.md)
salesloft.com | [Official MCP](../mcp/official.md) | [https://mcp.salesloft.com/mcp](https://mcp.salesloft.com/mcp) +2 more | OAuth
unknown exact flow - vendor press material describes it as natively listed in Claude's... | [Enterprise only](../gates/enterprise-only.md) |
| [Aircall](../tools/aircall.md)
aircall.io | [Community MCP](../mcp/community.md) | [https://github.com/themobilefirstco/aircall-mcp-serv...](https://github.com/themobilefirstco/aircall-mcp-server) +1 more | OAuth or an API key
api key. The community server takes an Aircall API ID and API token, which the public API... | [Paid, self-serve](../gates/paid.md) |
| [Overloop](../tools/overloop.md)
overloop.com | [Community MCP](../mcp/community.md) | [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp) | API key
api key via OVERLOOP_API_KEY environment variable | [Paid, self-serve](../gates/paid.md) |
| [ACA Automated Client Acquisition](../tools/aca-automated-client-acquisition.md)
automatedclientacquisition.com | [Community MCP](../mcp/community.md) | [https://github.com/seguelaCedric/screenshot-perfect](https://github.com/seguelaCedric/screenshot-perfect) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Agent Cold Email MCP (Coldrig)](../tools/agent-cold-email-mcp.md)
coldrig.dev | [Community MCP](../mcp/community.md) | [https://github.com/YS-projectcalc/agent-cold-email](https://github.com/YS-projectcalc/agent-cold-email) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Bavlio](../tools/bavlio.md)
bavlio.com | [Community MCP](../mcp/community.md) | [https://github.com/Bavlio/bavlio-mcp](https://github.com/Bavlio/bavlio-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Bird MCP by UsefulAPI](../tools/bird-mcp-by-usefulapi.md)
bird.usefulapi.io | [Community MCP](../mcp/community.md) | [https://github.com/m190/usefulapi-mcp](https://github.com/m190/usefulapi-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [CampaignStack](../tools/campaignstack.md)
campaignstack.io | [Community MCP](../mcp/community.md) | [https://campaignstack.io](https://campaignstack.io) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ContentStudio](../tools/contentstudio.md)
contentstudio.io | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=hubspot](https://registry.smithery.ai/servers?q=hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Crevideo Reach](../tools/crevideo-reach.md)
crevideo.com | [Community MCP](../mcp/community.md) | [https://github.com/crevideo/crevideo-reach](https://github.com/crevideo/crevideo-reach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Email Outreach by OpenHelm](../tools/email-outreach-by-openhelm.md)
openhelm.ai | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=sales) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Emelia](../tools/emelia.md)
emelia.io | [Community MCP](../mcp/community.md) | [https://github.com/emelia-io/claude-outreach](https://github.com/emelia-io/claude-outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Fintalio LinkedIn MCP](../tools/fintalio-linkedin-mcp.md)
fintalio.com | [Community MCP](../mcp/community.md) | [https://github.com/saybil-lab/mnareach](https://github.com/saybil-lab/mnareach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [FirstTouch](../tools/firsttouch.md)
firsttouch.com | [Community MCP](../mcp/community.md) | [https://github.com/First-Touch-Inc/mcp](https://github.com/First-Touch-Inc/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GetDialer](../tools/getdialer.md)
getdialer.app | [Community MCP](../mcp/community.md) | [https://getdialer.app/mcp](https://getdialer.app/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [GramClaw](../tools/gramclaw.md)
gramclaw.com | [Community MCP](../mcp/community.md) | [https://github.com/liquiden/grmcw](https://github.com/liquiden/grmcw) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [HeyLead - Autonomous LinkedIn SDR](../tools/heylead-autonomous-linkedin-sdr.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/D4umak/heylead](https://github.com/D4umak/heylead) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [ICT Dialer MCP](../tools/ict-dialer-mcp.md)
ictdialer.com | [Community MCP](../mcp/community.md) | [https://github.com/ictinnovations/ictdialer-mcp](https://github.com/ictinnovations/ictdialer-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Intent Outreach](../tools/intent-outreach.md)
demos.intentsolutions.io | [Community MCP](../mcp/community.md) | [https://github.com/jeremylongshore/intent-outreach](https://github.com/jeremylongshore/intent-outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Kairon](../tools/kairon.md)
heykairon.com | [Community MCP](../mcp/community.md) | [https://heykairon.com/mcp](https://heykairon.com/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LeadSleuth MCP](../tools/leadsleuth-mcp.md)
leads.zalize.com | [Community MCP](../mcp/community.md) | [https://github.com/wookat/leadsleuth](https://github.com/wookat/leadsleuth) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LeadSmarts](../tools/leadsmarts.md)
bjmsxprjidjdyquiroxy.supabase.co | [Community MCP](../mcp/community.md) | [https://bjmsxprjidjdyquiroxy.supabase.co/functions/v...](https://bjmsxprjidjdyquiroxy.supabase.co/functions/v1/mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedGrow](../tools/linkedgrow.md)
linkedgrow.ai | [Community MCP](../mcp/community.md) | [https://github.com/DigiHold/LinkedGrow](https://github.com/DigiHold/LinkedGrow) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedNav](../tools/linkednav.md)
linkednav.com | [Community MCP](../mcp/community.md) | [https://github.com/linglistack/linkednav-mcp](https://github.com/linglistack/linkednav-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Linkly](../tools/linkly.md)
linklyhq.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=hubspot](https://registry.smithery.ai/servers?q=hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LoomaScale for Google Ads](../tools/loomascale-for-google-ads.md)
ai.loomascale.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=gtm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MachFive Cold Email MCP](../tools/machfive-cold-email-mcp.md)
help.machfive.io | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=outreach](https://registry.smithery.ai/servers?q=outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MailerLite MCP by UsefulAPI](../tools/mailerlite-mcp-by-usefulapi.md)
mailerlite.usefulapi.io | [Community MCP](../mcp/community.md) | [https://github.com/m190/usefulapi-mcp](https://github.com/m190/usefulapi-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mailrith](../tools/mailrith.md)
mailrith.com | [Community MCP](../mcp/community.md) | [https://github.com/anrawool/mailrith-agent-platform](https://github.com/anrawool/mailrith-agent-platform) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Mamba Clay to Instantly/Smartlead Push MCP](../tools/mamba-clay-to-instantly-smartlead-push-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/mambalabsdev/mcp-clay-to-instantl...](https://github.com/mambalabsdev/mcp-clay-to-instantly-smartlead-push) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Marvenn MCP](../tools/marvenn-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/marvennai/mcp-server](https://github.com/marvennai/mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MCP Emails](../tools/mcp-emails.md)
mcpemails.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=2&pageSize...](https://registry.smithery.ai/servers?page=2&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MentionAgent](../tools/mentionagent.md)
mentionagent.ai | [Community MCP](../mcp/community.md) | [https://github.com/BuildsbyMatt/mentionagent-claude-...](https://github.com/BuildsbyMatt/mentionagent-claude-skill) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MisarMail MCP](../tools/misarmail-mcp.md)
misarmail.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Misarreach](../tools/misarreach.md)
misarreach.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Moltline Outbound](../tools/moltline-outbound.md)
moltlinestudio.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=sales) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [MuntuAI MCP](../tools/muntuai-mcp.md)
api.muntuai.com | [Community MCP](../mcp/community.md) | [https://github.com/design-smith/MuntuAI-MCP](https://github.com/design-smith/MuntuAI-MCP) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Nitrosend](../tools/nitrosend.md)
nitrosend.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Omnflow](../tools/omnflow.md)
omnflow.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=enrich](https://registry.smithery.ai/servers?q=enrich) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Onsa](../tools/onsa.md)
api.onsa.ai | [Community MCP](../mcp/community.md) | [https://api.onsa.ai/api/mcp](https://api.onsa.ai/api/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [OpenHelm Email Outreach MCP](../tools/openhelm-email-outreach-mcp.md)
mcp.openhelm.ai | [Community MCP](../mcp/community.md) | [https://mcp.openhelm.ai/email/mcp](https://mcp.openhelm.ai/email/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PersuadioAI](../tools/persuadioai.md)
persuadioai.com | [Community MCP](../mcp/community.md) | [https://github.com/mannyfernandezvc/persuadioai-plat...](https://github.com/mannyfernandezvc/persuadioai-platform) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Phos Sales Engine](../tools/phos-sales-engine.md)
se.phos.nz | [Community MCP](../mcp/community.md) | [https://se.phos.nz/mcp](https://se.phos.nz/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Phos Sales Engine MCP](../tools/phos-sales-engine-mcp.md)
sales.phos.nz | [Community MCP](../mcp/community.md) | [https://github.com/albermm/sales-engine](https://github.com/albermm/sales-engine) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PitchPilot Outreach](../tools/pitchpilot-outreach.md)
aioutreachkit.surge.sh | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=enrich](https://registry.smithery.ai/servers?q=enrich) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PLOTT](../tools/plott.md)
plott.uk | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=outreach](https://registry.smithery.ai/servers?q=outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Podcast Guest CRM](../tools/podcast-guest-crm.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/RudrenduPaul/podcast-guest-crm](https://github.com/RudrenduPaul/podcast-guest-crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Pro Reach](../tools/pro-reach.md)
proreach.ai | [Community MCP](../mcp/community.md) | [https://proreach.ai/api/mcp](https://proreach.ai/api/mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RD Station Marketing MCP](../tools/rd-station-marketing-mcp.md)
mcp.ai | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Reach MCP](../tools/reach-mcp.md)
reachmcp.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?q=hubspot](https://registry.smithery.ai/servers?q=hubspot) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RepScale](../tools/repscale.md)
repscale.ai | [Community MCP](../mcp/community.md) | [https://repscale.ai](https://repscale.ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SalesEQ Plugins](../tools/saleseq-plugins.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/SalesEQ/plugins](https://github.com/SalesEQ/plugins) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SalesTouch](../tools/salestouch.md)
salestouch.io | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=1&pageSize...](https://registry.smithery.ai/servers?page=1&pageSize=100&q=sales) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SendPulse](../tools/sendpulse.md)
sendpulse.com | [Community MCP](../mcp/community.md) | [https://github.com/sendpulse/mcp-server](https://github.com/sendpulse/mcp-server) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Sequenzy MCP](../tools/sequenzy-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Signal Found Reddit MCP](../tools/signal-found-reddit-mcp.md)
github.com | [Community MCP](../mcp/community.md) | [https://github.com/signal-found/sf-mcp](https://github.com/signal-found/sf-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [SoundGTM](../tools/soundgtm.md)
soundgtm.com | [Community MCP](../mcp/community.md) | [https://registry.smithery.ai/servers?page=2&pageSize...](https://registry.smithery.ai/servers?page=2&pageSize=100&q=crm) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Toflow](../tools/toflow.md)
toflow.ai | [Community MCP](../mcp/community.md) | [https://github.com/toflow-ai/toflow-mcp](https://github.com/toflow-ai/toflow-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [WarmySender](../tools/warmysender.md)
warmysender.com | [Community MCP](../mcp/community.md) | [https://warmysender.com](https://warmysender.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |

### The other 92 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [Expandi](../tools/expandi.md)
expandi.io | [MCP unknown](../mcp/unknown.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Groove](../tools/groove.md)
groove.co | [MCP unknown](../mcp/unknown.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Kixie](../tools/kixie.md)
kixie.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Klenty](../tools/klenty.md)
klenty.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Mailshake](../tools/mailshake.md)
mailshake.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [QuickMail](../tools/quickmail.md)
quickmail.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Orum](../tools/orum.md)
orum.com | [No MCP found](../mcp/none-found.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Act-On](../tools/act-on.md)
act-on.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [ActiveCampaign](../tools/activecampaign.md)
activecampaign.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [AgentMail](../tools/agentmail.md)
agentmail.to | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Alyce](../tools/alyce.md)
alyce.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Atlog](../tools/atlog.md)
atlog.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Banabo](../tools/banabo.md)
banabo.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Birdie](../tools/birdie.md)
getbirdie.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Blaze](../tools/blaze.md)
withblaze.app | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Bluebirds](../tools/bluebirds.md)
bluebirds.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Brevo](../tools/brevo.md)
brevo.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [CallHippo](../tools/callhippo.md)
callhippo.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Castled.io](../tools/castled-io.md)
castled.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [CIENCE](../tools/cience.md)
cience.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [CoffeeAI](../tools/coffeeai.md)
get-coffee.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Cohesive](../tools/cohesive.md)
getcohesiveai.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [ConnectAndSell](../tools/connectandsell.md)
connectandsell.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Copyfactory](../tools/copyfactory.md)
copyfactory.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Dreach](../tools/dreach.md)
dreach.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Dyspatch](../tools/dyspatch.md)
dyspatch.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [EmailBison](../tools/emailbison.md)
emailbison.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Emailchaser](../tools/emailchaser.md)
emailchaser.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [FrontSpin](../tools/frontspin.md)
frontspin.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Fuse AI](../tools/fuse-ai.md)
fuseai.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Hatch](../tools/hatch.md)
usehatch.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Hilos](../tools/hilos.md)
hilos.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Hive](../tools/hive.md)
hive.co | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Imagine AI](../tools/imagine-ai.md)
imagineai.me | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [InstaAgent](../tools/instaagent.md)
instaagent.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [JustAI](../tools/justai.md)
getjust.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [KrispCall](../tools/krispcall.md)
krispcall.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Kular](../tools/kular.md)
kular.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Kuli](../tools/kuli.md)
kuli.one | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [LemonLime](../tools/lemonlime.md)
lemonlime.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Lob](../tools/lob.md)
lob.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Locent](../tools/locent.md)
locent.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Loops](../tools/loops.md)
loops.so | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Mailchimp](../tools/mailchimp.md)
mailchimp.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Mailmodo](../tools/mailmodo.md)
mailmodo.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Meticulate](../tools/meticulate.md)
meticulate.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Mogli](../tools/mogli.md)
mogli.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Natterbox](../tools/natterbox.md)
natterbox.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Naytev](../tools/naytev.md)
naytev.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [OneLocal](../tools/onelocal.md)
onelocal.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [OneSignal](../tools/onesignal.md)
onesignal.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Origami](../tools/origami.md)
origami.chat | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Outplay](../tools/outplay.md)
outplay.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |
| [OwnLocal](../tools/ownlocal.md)
ownlocal.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Pavoot](../tools/pavoot.md)
pavoot.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Persana AI](../tools/persana-ai.md)
persana.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [PhoneBurner](../tools/phoneburner.md)
phoneburner.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [PhoneSys](../tools/phonesys.md)
pingm.net | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Pinnacle](../tools/pinnacle.md)
pinnacle.sh | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Plai](../tools/plai.md)
plai.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [PlayAbly](../tools/playably.md)
playably.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Popsy](../tools/popsy.md)
popsy.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Postal](../tools/postal.md)
postal.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Postscript](../tools/postscript.md)
postscript.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Quo](../tools/quo.md)
quo.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Ranla](../tools/ranla.md)
ranla.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Reachdesk](../tools/reachdesk.md)
reachdesk.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [ReachInbox](../tools/reachinbox.md)
reachinbox.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Resquared](../tools/resquared.md)
re2.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Ringover](../tools/ringover.md)
ringover.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Salesgraph](../tools/salesgraph.md)
salesgraph.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Scribeless](../tools/scribeless.md)
scribeless.co | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Sendblue](../tools/sendblue.md)
sendblue.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Sendoff](../tools/sendoff.md)
github.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Sendoso](../tools/sendoso.md)
sendoso.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [SharpSpring](../tools/sharpspring.md)
sharpspring.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Slik](../tools/slik.md)
slik.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Smobi](../tools/smobi.md)
smobi.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [SMS-Magic](../tools/sms-magic.md)
sms-magic.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Sprites](../tools/sprites.md)
sprites.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Superhuman](../tools/superhuman.md)
superhuman.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [SureConnect](../tools/sureconnect.md)
sureconnect.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Surface](../tools/surface.md)
withsurface.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Synthio Labs](../tools/synthio-labs.md)
synthiolabs.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [throxy](../tools/throxy.md)
throxy.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [TimelinesAI](../tools/timelinesai.md)
timelines.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Treble](../tools/treble.md)
treble.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Twain](../tools/twain.md)
twain.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Upcall](../tools/upcall.md)
upcall.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Venta AI](../tools/venta-ai.md)
getventa.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [WhatsApp Business](../tools/whatsapp-business.md)
business.whatsapp.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Zaymo](../tools/zaymo.md)
zaymo.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |

### What this category is asked for

The jobs most often tagged on the 27 tagged entries in this category.

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Search people by criteria](../jobs/search-people-by-criteria.md)

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 1,251 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
