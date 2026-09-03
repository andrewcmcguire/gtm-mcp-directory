# Inbound & PLG Chat tools with MCP servers: 8 of 15, counted

> 8 of the 15 inbound & plg chat tools in The GTM MCP Directory have an MCP server: 6 official and 2 community. The server URL, auth model and access gate for each. Counted 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / Inbound & PLG Chat tools with an MCP server

**List · 8 of 293**

## Inbound & PLG Chat tools with an MCP server

Tools that sit on the receiving end of demand - website chat that qualifies and books a visitor before a human ever joins, in-app signal tools that turn free-trial usage into a sales-ready account, and the newer wave of AI-SDR-for-inbound entrants trying to do both. The defining tension: this category has an unusually high mortality rate. Of the ten seed tools researched for this file, three (Pocus, Correlated, Toplyne) are confirmed dead or absorbed and two more (Drift, Ultimate.ai) are folded into an acquirer's platform rather than sold standalone - suggesting "PLG signal tool" and "chat widget" were never durable categories on their own, just features that bigger platforms eventually swallowed. 8 of 15 entries in this category are reachable by an agent: 6 through a server the vendor maintains and 2 through one somebody else built. The category is tagged most often with Answer an inbound chat or call. [See the full category page](../categories/inbound-plg-chat.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Tidio](../tools/tidio.md)
tidio.com | [Official MCP](../mcp/official.md) | [https://github.com/TidioPoland/tidio-mcp-connector](https://github.com/TidioPoland/tidio-mcp-connector) +1 more | OAuth
OAuth: the tidio_connect tool opens a browser to Tidio's login page, then stores access... | [Free to start](../gates/free.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Official MCP](../mcp/official.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | OAuth or an API key
Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper... | [Paid, self-serve](../gates/paid.md) |
| [Intercom (Fin)](../tools/intercom.md)
intercom.com | [Official MCP](../mcp/official.md) | [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp) +2 more | OAuth or an API key
OAuth (browser-based, recommended) or a Bearer token using an Intercom API token;... | [Paid, self-serve](../gates/paid.md) |
| [Ada](../tools/ada.md)
ada.cx | [Official MCP](../mcp/official.md) | [https://docs.ada.cx/_mcp/server](https://docs.ada.cx/_mcp/server) | Auth not recorded
none documented - connects over HTTP with no credential requirement described in the docs. | [Enterprise only](../gates/enterprise-only.md) |
| [Endgame](../tools/endgame.md)
endgame.io | [Official MCP](../mcp/official.md) | [https://docs.endgame.io/features/mcp-server](https://docs.endgame.io/features/mcp-server) +1 more | OAuth or an API key
OAuth (browser-based) for individual users via Claude/ChatGPT/Claude Code/Codex... | [Gate unknown](../gates/unknown.md) |
| [Pylon](../tools/pylon.md)
usepylon.com | [Official MCP](../mcp/official.md) | [https://mcp.usepylon.com](https://mcp.usepylon.com) +1 more | OAuth
OAuth 2.0 over stateless streamable HTTP; access is permission-scoped so a connected AI... | [Gate unknown](../gates/unknown.md) |
| [Landbot](../tools/landbot.md)
landbot.io | [Community MCP](../mcp/community.md) | [https://composio.dev/toolkits/landbot](https://composio.dev/toolkits/landbot) +1 more | Third party platform auth
The operator's own Landbot API key stored with Composio; the Zapier connector rides... | [Free to start](../gates/free.md) |
| [Chatbase](../tools/chatbase.md)
chatbase.co | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/chatbase](https://zapier.com/mcp/chatbase) | Third party platform auth
Rides Zapier's hosted-connector auth at mcp.zapier.com, not a Chatbase-issued MCP... | [Paid, self-serve](../gates/paid.md) |

### The other 7 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [Forethought (now "Forethought AI Agents by Zendesk")](../tools/forethought.md)
forethought.ai | [MCP unknown](../mcp/unknown.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Pocus](../tools/pocus.md)
pocus.com | [MCP not applicable](../mcp/n-a.md) | [Gate not applicable](../gates/n-a.md) | 2026-09-02 |
| [Qualified](../tools/qualified.md)
qualified.com | [No MCP found](../mcp/none-found.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Drift](../tools/drift.md)
drift.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |
| [Correlated](../tools/correlated.md)
correlated.ai | [No MCP found](../mcp/none-found.md) | [Gate not applicable](../gates/n-a.md) | 2026-09-02 |
| [Toplyne](../tools/toplyne.md)
toplyne.io | [No MCP found](../mcp/none-found.md) | [Gate not applicable](../gates/n-a.md) | 2026-09-02 |
| [Ultimate.ai (Ultimate)](../tools/ultimate-ai.md)
getultimate.ai | [No MCP found](../mcp/none-found.md) | [Gate not applicable](../gates/n-a.md) | 2026-09-02 |

### What this category is asked for

The jobs most often tagged on the 10 tagged entries in this category.

- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Book a meeting](../jobs/book-a-meeting.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

Counted 2026-09-03 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
