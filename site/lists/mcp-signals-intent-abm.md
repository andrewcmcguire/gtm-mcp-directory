# Signals & Intent tools with MCP servers: 19 of 28, counted

> 19 of the 28 signals & intent tools in The GTM MCP Directory have an MCP server: 18 official and 1 community. The server URL, auth model and access gate for each. Counted 2026-09-04.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The lists](index.md) / Signals & Intent tools with an MCP server

**List · 19 of 293**

## Signals & Intent tools with an MCP server

Tools that try to answer "who is about to buy, and how do you know." The category splits cleanly into two eras: the legacy enterprise intent-data incumbents (6sense, Demandbase, Bombora, HG Insights) sold on annual contracts with no self-serve path, and a newer wave of visitor-ID/job-change/ API-first tools (RB2B, Warmly, Crustdata, TheirStack, PredictLeads) built for solo operators with free tiers and documented MCP servers. 19 of 28 entries in this category are reachable by an agent: 18 through a server the vendor maintains and 1 through one somebody else built. The category is tagged most often with Fetch buyer intent signals. [See the full category page](../categories/signals-intent-abm.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Crustdata](../tools/crustdata.md)
crustdata.com | [Official MCP](../mcp/official.md) | [https://docs.crustdata.com/for-agents/mcp.md](https://docs.crustdata.com/for-agents/mcp.md) +1 more | API key
api key (free sandbox key available) | [Free to start](../gates/free.md) |
| [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md)
leadfeeder.com | [Official MCP](../mcp/official.md) | [https://www.leadfeeder.com/features/mcp-server/](https://www.leadfeeder.com/features/mcp-server/) +1 more | OAuth
OAuth - user signs in with their own Leadfeeder account; vendor states "No keys pasted... | [Free to start](../gates/free.md) |
| [PredictLeads](../tools/predictleads.md)
predictleads.com | [Official MCP](../mcp/official.md) | [https://mcp.predictleads.com/](https://mcp.predictleads.com/) | API key
api key (same API key/token used for REST API calls, per vendor blog) | [Free to start](../gates/free.md) |
| [TheirStack](../tools/theirstack.md)
theirstack.com | [Official MCP](../mcp/official.md) | [https://theirstack.com/en/job-posting-mcp](https://theirstack.com/en/job-posting-mcp) | Auth not recorded
unknown - page references a "How does authentication work?" FAQ but the answer wasn't... | [Free to start](../gates/free.md) |
| [Warmly (Warmly.ai)](../tools/warmly.md)
warmly.ai | [Official MCP](../mcp/official.md) | [https://www.warmly.ai/launches/warmly-mcp-and-api-ar...](https://www.warmly.ai/launches/warmly-mcp-and-api-are-live) | OAuth or an API key
MCP uses OAuth-based login (no manual key management); the separate REST API... | [Free to start](../gates/free.md) |
| [Factors.ai](../tools/factors-ai.md)
factors.ai | [Official MCP](../mcp/official.md) | [https://help.factors.ai/en/articles/14705206-factors...](https://help.factors.ai/en/articles/14705206-factors-mcp) | API key
Personal access token (generated in Settings > AI Features), used via Claude custom... | [Paid, self-serve](../gates/paid.md) |
| [Keyplay](../tools/keyplay.md)
keyplay.io | [Official MCP](../mcp/official.md) | [https://docs.keyplay.io/en/articles/13643214-keyplay...](https://docs.keyplay.io/en/articles/13643214-keyplay-mcp) +1 more | OAuth or an API key
OAuth for Claude.ai and Claude Desktop, API key for Claude Code, per the vendor's docs | [Paid, self-serve](../gates/paid.md) |
| [RB2B](../tools/rb2b.md)
rb2b.com | [Official MCP](../mcp/official.md) | [https://registry.npmjs.org/@rb2b/rb2b-apis-mcp](https://registry.npmjs.org/@rb2b/rb2b-apis-mcp) | API key
api key | [Paid, self-serve](../gates/paid.md) |
| [Snitcher](../tools/snitcher.md)
snitcher.com | [Official MCP](../mcp/official.md) | [https://www.snitcher.com/changelog/point-claude-at-s...](https://www.snitcher.com/changelog/point-claude-at-snitcher/) | Auth not recorded
unknown - vendor changelog points to docs.snitcher.com for authentication specifics, not... | [Paid, self-serve](../gates/paid.md) |
| [Sumble](../tools/sumble.md)
sumble.com | [Official MCP](../mcp/official.md) | [https://docs.sumble.com/api/mcp](https://docs.sumble.com/api/mcp) +1 more | Auth not recorded
unknown - the MCP overview page documents one-click install from the Claude and ChatGPT... | [Paid, self-serve](../gates/paid.md) |
| [6sense](../tools/6sense.md)
6sense.com | [Official MCP](../mcp/official.md) | [https://6sense.com/platform/mcp-server/](https://6sense.com/platform/mcp-server/) +1 more | OAuth
OAuth using existing 6sense platform login (no separate API key setup per vendor docs) | [Enterprise only](../gates/enterprise-only.md) |
| [Common Room](../tools/common-room.md)
commonroom.io | [Official MCP](../mcp/official.md) | [https://www.commonroom.io/docs/using-common-room/mcp...](https://www.commonroom.io/docs/using-common-room/mcp-server/) +1 more | OAuth
oauth (OAuth 2.1, browser-based, tokens scoped to the user's own Common Room permissions) | [Enterprise only](../gates/enterprise-only.md) |
| [Crossbeam](../tools/crossbeam.md)
crossbeam.com | [Official MCP](../mcp/official.md) | [https://mcp.crossbeam.com/mcp](https://mcp.crossbeam.com/mcp) +1 more | OAuth
OAuth with Crossbeam login credentials, with a permission consent screen at connect time. | [Enterprise only](../gates/enterprise-only.md) |
| [Demandbase (Demandbase One)](../tools/demandbase.md)
demandbase.com | [Official MCP](../mcp/official.md) | [https://developer.demandbase.com/docs/mcp](https://developer.demandbase.com/docs/mcp) +1 more | Auth not recorded
unknown - the account-team-gated support article that likely covers this returned HTTP... | [Enterprise only](../gates/enterprise-only.md) |
| [G2 Buyer Intent](../tools/g2-buyer-intent.md)
g2.com | [Official MCP](../mcp/official.md) | [https://mcp.g2.com/mcp](https://mcp.g2.com/mcp) +2 more | OAuth
OAuth 2.0 Authorization Code with PKCE. You register an OAuth app in the G2 Developer... | [Enterprise only](../gates/enterprise-only.md) |
| [HG Insights (Phoenix platform)](../tools/hg-insights.md)
hginsights.com | [Official MCP](../mcp/official.md) | [https://learn.microsoft.com/en-us/connectors/hginsig...](https://learn.microsoft.com/en-us/connectors/hginsightsmcp/) | API key
api key (`x-api-key` header; throttled to 100 calls/60 seconds per connection) | [Enterprise only](../gates/enterprise-only.md) |
| [Similarweb](../tools/similarweb.md)
similarweb.com | [Official MCP](../mcp/official.md) | [https://mcp.similarweb.com](https://mcp.similarweb.com) +3 more | OAuth or an API key
CONFLICTING VENDOR STATEMENTS, flagged rather than resolved. Both Similarweb developer... | [Enterprise only](../gates/enterprise-only.md) |
| [UserGems](../tools/usergems.md)
usergems.com | [Official MCP](../mcp/official.md) | [https://www.usergems.com/product/mcp](https://www.usergems.com/product/mcp) | OAuth or an API key
unknown - connects inside Claude/ChatGPT per the product page, but the exact auth... | [Enterprise only](../gates/enterprise-only.md) |
| [Trigify (Trigify.io)](../tools/trigify.md)
trigify.io | [Community MCP](../mcp/community.md) | [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli) | API key
api key (from app.trigify.io/settings; via `trigify login --api-key`, env var... | [Paid, self-serve](../gates/paid.md) |

### The other 9 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [Centralize](../tools/centralize.md)
usecentralize.com | [MCP unknown](../mcp/unknown.md) | [Free to start](../gates/free.md) | 2026-09-02 |
| [Vector (vector.co)](../tools/vector.md)
vector.co | [MCP unknown](../mcp/unknown.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Koala](../tools/koala.md)
getkoala.com | [MCP not applicable](../mcp/n-a.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Albacross](../tools/albacross.md)
albacross.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Clearbit Reveal (rebranded: HubSpot Breeze Intelligence)](../tools/clearbit-reveal.md)
clearbit.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Intently (getintently.com)](../tools/intently.md)
getintently.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Live Data Technologies](../tools/live-data-technologies.md)
livedatatechnologies.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Bombora (Company Surge)](../tools/bombora.md)
bombora.com | [No MCP found](../mcp/none-found.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Champify](../tools/champify.md)
champify.io | [No MCP found](../mcp/none-found.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |

### What this category is asked for

The jobs most often tagged on the 27 tagged entries in this category.

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Find a work email address](../jobs/find-work-email.md)

Counted 2026-09-04 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
