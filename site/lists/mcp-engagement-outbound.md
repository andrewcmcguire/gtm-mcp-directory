# Engagement & Outbound tools with MCP servers: 17 of 27, counted

> 17 of the 27 engagement & outbound tools in The GTM MCP Directory have an MCP server: 15 official and 2 community. The server URL, auth model and access gate for each. Counted 2026-08-28.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / Engagement & Outbound tools with an MCP server

**List · 17 of 293**

## Engagement & Outbound tools with an MCP server

The execution layer - sequencers, parallel dialers, and LinkedIn automation tools that actually put messages and calls in front of prospects. MCP maturity here is split sharply: the big sales-engagement platforms (Salesloft, Outreach, lemlist) and several LinkedIn tools have shipped real official servers in 2026, while most parallel dialers and mid-market cold-email tools have none. 17 of 27 entries in this category are reachable by an agent: 15 through a server the vendor maintains and 2 through one somebody else built. The category is tagged most often with Run an email sequence. [See the full category page](../categories/engagement-outbound.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Autobound](../tools/autobound.md)
autobound.ai | [Official MCP](../mcp/official.md) | [https://www.autobound.ai/integrations/mcp](https://www.autobound.ai/integrations/mcp) +1 more | API key
api key via an AUTOBOUND_API_KEY environment variable in the MCP client config. | [Free to start](../gates/free.md) |
| [HeyReach](../tools/heyreach.md)
heyreach.io | [Official MCP](../mcp/official.md) | [https://www.heyreach.io/mcp](https://www.heyreach.io/mcp) +1 more | OAuth or an API key
workspace-scoped "MCP key" + connection URL (API-key-style, not OAuth) | [Paid, self-serve](../gates/paid.md) |
| [Instantly](../tools/instantly.md)
instantly.ai | [Official MCP](../mcp/official.md) | [https://mcp.instantly.ai/mcp](https://mcp.instantly.ai/mcp) +1 more | API key
api key (generated in Instantly Settings > Integrations > API Keys) | [Paid, self-serve](../gates/paid.md) |
| [La Growth Machine](../tools/la-growth-machine.md)
lagrowthmachine.com | [Official MCP](../mcp/official.md) | [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system) +1 more | OAuth
OAuth - no API key needed; first use opens a browser sign-in directly to the user's La... | [Paid, self-serve](../gates/paid.md) |
| [lemlist](../tools/lemlist.md)
lemlist.com | [Official MCP](../mcp/official.md) | [https://developer.lemlist.com/mcp/setup](https://developer.lemlist.com/mcp/setup) +1 more | OAuth or an API key
OAuth (browser-based PKCE flow, recommended) or API key via X-API-Key header | [Paid, self-serve](../gates/paid.md) |
| [Mixmax](../tools/mixmax.md)
mixmax.com | [Official MCP](../mcp/official.md) | [https://mcp.mixmax.com/mcp](https://mcp.mixmax.com/mcp) +2 more | OAuth
OAuth 2.0 authorization code flow, scoped to the connecting user's account. Read-only. | [Paid, self-serve](../gates/paid.md) |
| [PhantomBuster](../tools/phantombuster.md)
phantombuster.com | [Official MCP](../mcp/official.md) | [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server) +1 more | OAuth
OAuth - first connection redirects to PhantomBuster sign-in/authorization, then workspace... | [Paid, self-serve](../gates/paid.md) |
| [Reply.io](../tools/reply-io.md)
reply.io | [Official MCP](../mcp/official.md) | [https://reply.io/mcp/](https://reply.io/mcp/) | API key
api key (personal API key over HTTPS, included in free trial) | [Paid, self-serve](../gates/paid.md) |
| [Salesforge](../tools/salesforge.md)
salesforge.ai | [Official MCP](../mcp/official.md) | [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp) | API key
api key via HTTP header (X-Salesforge-Key) | [Paid, self-serve](../gates/paid.md) |
| [Super Send](../tools/super-send.md)
supersend.io | [Official MCP](../mcp/official.md) | [https://docs.supersend.io/docs/mcp-server](https://docs.supersend.io/docs/mcp-server) | API key
api key, Streamable HTTP transport | [Paid, self-serve](../gates/paid.md) |
| [Waalaxy](../tools/waalaxy.md)
waalaxy.com | [Official MCP](../mcp/official.md) | [https://docs.waalaxy.com/mcp-server](https://docs.waalaxy.com/mcp-server) +1 more | OAuth or an API key
user-based OAuth 2.1 via magic-link sign-in; vendor docs explicitly state bearer API keys... | [Paid, self-serve](../gates/paid.md) |
| [Woodpecker](../tools/woodpecker.md)
woodpecker.co | [Official MCP](../mcp/official.md) | [https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/) +1 more | OAuth or an API key
hosted OAuth-style flow (Claude-specific) or self-hosted Docker setup using a Woodpecker... | [Paid, self-serve](../gates/paid.md) |
| [Apollo.io Sequences (Emailer Campaigns)](../tools/apollo-io-sequences.md)
apollo.io | [Official MCP](../mcp/official.md) | [https://github.com/apolloio/apollo-mcp-plugin](https://github.com/apolloio/apollo-mcp-plugin) +1 more | OAuth
OAuth (Apollo.io sign-in/authorization flow; no API key required for this MCP) | [Enterprise only](../gates/enterprise-only.md) |
| [Outreach](../tools/outreach.md)
outreach.io | [Official MCP](../mcp/official.md) | [https://api.outreach.io/mcp/](https://api.outreach.io/mcp/) +1 more | OAuth
OAuth 2.1 with Dynamic Client Registration; also requires the org-level "Amplify" add-on... | [Enterprise only](../gates/enterprise-only.md) |
| [Salesloft](../tools/salesloft.md)
salesloft.com | [Official MCP](../mcp/official.md) | [https://www.salesloft.com/company/newsroom/clari-sal...](https://www.salesloft.com/company/newsroom/clari-salesloft-forecasting-execution-mcp-server) +1 more | OAuth
unknown exact flow - vendor press material describes it as natively listed in Claude's... | [Enterprise only](../gates/enterprise-only.md) |
| [Overloop](../tools/overloop.md)
overloop.com | [Community MCP](../mcp/community.md) | [https://github.com/sortlist/overloop-mcp](https://github.com/sortlist/overloop-mcp) | API key
api key via OVERLOOP_API_KEY environment variable | [Paid, self-serve](../gates/paid.md) |
| [Smartlead](../tools/smartlead.md)
smartlead.ai | [Community MCP](../mcp/community.md) | [https://github.com/LeadMagic/smartlead-mcp-server](https://github.com/LeadMagic/smartlead-mcp-server) +1 more | API key
api key | [Paid, self-serve](../gates/paid.md) |

### The other 10 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [Groove](../tools/groove.md)
groove.co | [MCP unknown](../mcp/unknown.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-08-24 |
| [Expandi](../tools/expandi.md)
expandi.io | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-08-24 |
| [Kixie](../tools/kixie.md)
kixie.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-08-24 |
| [Klenty](../tools/klenty.md)
klenty.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-08-24 |
| [Mailshake](../tools/mailshake.md)
mailshake.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-08-24 |
| [QuickMail](../tools/quickmail.md)
quickmail.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-08-24 |
| [Amplemarket](../tools/amplemarket.md)
amplemarket.com | [No MCP found](../mcp/none-found.md) | [Enterprise leaning](../gates/enterprise-leaning.md) | 2026-08-24 |
| [Nooks](../tools/nooks.md)
nooks.ai | [No MCP found](../mcp/none-found.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-08-25 |
| [Orum](../tools/orum.md)
orum.com | [No MCP found](../mcp/none-found.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-08-24 |
| [Outplay](../tools/outplay.md)
outplay.ai | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-08-24 |

### What this category is asked for

The jobs most often tagged on the 27 tagged entries in this category.

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)
- [Search people by criteria](../jobs/search-people-by-criteria.md)

Counted 2026-08-28 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
