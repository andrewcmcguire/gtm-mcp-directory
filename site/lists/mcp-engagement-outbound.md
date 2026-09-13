# Engagement & Outbound tools with MCP servers: 33 of 98, counted

> 33 of the 98 engagement & outbound tools in The GTM MCP Directory have an MCP server: 23 official and 10 community. The server URL, auth model and access gate for each. Counted 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / Engagement & Outbound tools with an MCP server

**List · 33 of 739**

## Engagement & Outbound tools with an MCP server

The execution layer - sequencers, parallel dialers, and LinkedIn automation tools that actually put messages and calls in front of prospects. MCP maturity here is split sharply: the big sales-engagement platforms (Salesloft, Outreach, lemlist) and several LinkedIn tools have shipped real official servers in 2026, while most parallel dialers and mid-market cold-email tools have none. 33 of 98 entries in this category are reachable by an agent: 23 through a server the vendor maintains and 10 through one somebody else built. The category is tagged most often with Run an email sequence. [See the full category page](../categories/engagement-outbound.md).

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
| [Emelia](../tools/emelia.md)
emelia.io | [Community MCP](../mcp/community.md) | [https://github.com/emelia-io/claude-outreach](https://github.com/emelia-io/claude-outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Intent Outreach](../tools/intent-outreach.md)
demos.intentsolutions.io | [Community MCP](../mcp/community.md) | [https://github.com/jeremylongshore/intent-outreach](https://github.com/jeremylongshore/intent-outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [LinkedGrow](../tools/linkedgrow.md)
linkedgrow.ai | [Community MCP](../mcp/community.md) | [https://github.com/DigiHold/LinkedGrow](https://github.com/DigiHold/LinkedGrow) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Misarreach](../tools/misarreach.md)
misarreach.com | [Community MCP](../mcp/community.md) | [https://www.npmjs.com/search?q=mcp%20outreach](https://www.npmjs.com/search?q=mcp%20outreach) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [PersuadioAI](../tools/persuadioai.md)
persuadioai.com | [Community MCP](../mcp/community.md) | [https://github.com/mannyfernandezvc/persuadioai-plat...](https://github.com/mannyfernandezvc/persuadioai-platform) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [RepScale](../tools/repscale.md)
repscale.ai | [Community MCP](../mcp/community.md) | [https://repscale.ai](https://repscale.ai) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [Toflow](../tools/toflow.md)
toflow.ai | [Community MCP](../mcp/community.md) | [https://github.com/toflow-ai/toflow-mcp](https://github.com/toflow-ai/toflow-mcp) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |
| [WarmySender](../tools/warmysender.md)
warmysender.com | [Community MCP](../mcp/community.md) | [https://warmysender.com](https://warmysender.com) | Auth not recorded
blank | [Gate unknown](../gates/unknown.md) |

### The other 65 in this category

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
| [Atlog](../tools/atlog.md)
atlog.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Banabo](../tools/banabo.md)
banabo.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Birdie](../tools/birdie.md)
getbirdie.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Blaze](../tools/blaze.md)
withblaze.app | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Brevo](../tools/brevo.md)
brevo.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Cohesive](../tools/cohesive.md)
getcohesiveai.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [EmailBison](../tools/emailbison.md)
emailbison.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Emailchaser](../tools/emailchaser.md)
emailchaser.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [FrontSpin](../tools/frontspin.md)
frontspin.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Fuse AI](../tools/fuse-ai.md)
fuseai.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
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
| [Mailchimp](../tools/mailchimp.md)
mailchimp.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Meticulate](../tools/meticulate.md)
meticulate.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Mogli](../tools/mogli.md)
mogli.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Natterbox](../tools/natterbox.md)
natterbox.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [OneLocal](../tools/onelocal.md)
onelocal.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Origami](../tools/origami.md)
origami.chat | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [Outplay](../tools/outplay.md)
outplay.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |
| [OwnLocal](../tools/ownlocal.md)
ownlocal.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [PhoneBurner](../tools/phoneburner.md)
phoneburner.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
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
| [Sendoso](../tools/sendoso.md)
sendoso.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
| [SharpSpring](../tools/sharpspring.md)
sharpspring.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-12 |
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

Counted 2026-09-12 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 739 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
