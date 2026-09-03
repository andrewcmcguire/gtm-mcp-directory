# Video Prospecting tools with MCP servers: 9 of 14, counted

> 9 of the 14 video prospecting tools in The GTM MCP Directory have an MCP server: 3 official and 6 community. The server URL, auth model and access gate for each. Counted 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / Video Prospecting tools with an MCP server

**List · 9 of 293**

## Video Prospecting tools with an MCP server

Personalized video for outbound - a rep records one clip, and the tool inserts the prospect's name, company, or website into it (either simple templated overlay or genuine AI voice-clone/avatar generation), then tracks opens inside an email or sequence. MCP maturity here is close to zero: the only two official servers found (Tavus, HeyGen) belong to general-purpose AI-avatar platforms that happen to have a sales use case, not the dedicated video-prospecting vendors, which have shipped nothing publishable yet - several rely on generic Zapier MCP gateways instead of a first-party server. 9 of 14 entries in this category are reachable by an agent: 3 through a server the vendor maintains and 6 through one somebody else built. The category is tagged most often with Create and send a prospecting video. [See the full category page](../categories/video-prospecting.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Tavus](../tools/tavus.md)
tavus.io | [Official MCP](../mcp/official.md) | [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp) +3 more | OAuth or an API key
OAuth 2.0 browser-based flow; the exchange mints a per-user API key server-side, nothing... | [Free to start](../gates/free.md) |
| [HeyGen](../tools/heygen.md)
heygen.com | [Official MCP](../mcp/official.md) | [https://mcp.heygen.com/mcp/v1/](https://mcp.heygen.com/mcp/v1/) +2 more | OAuth
OAuth - vendor states "connect your HeyGen account, no API key required"; generation... | [Paid, self-serve](../gates/paid.md) |
| [Trumpet](../tools/trumpet.md)
sendtrumpet.com | [Official MCP](../mcp/official.md) | [https://trumpet.app/api/mcp](https://trumpet.app/api/mcp) +2 more | OAuth
OAuth 2.0 - vendor help-center doc confirms "Authenticate via trumpet (OAuth 2.0)"; setup... | [Gate unknown](../gates/unknown.md) |
| [Loom](../tools/loom.md)
loom.com | [Community MCP](../mcp/community.md) | [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom) +2 more | API key
karbassi/mcp-loom uses Loom's undocumented internal GraphQL API via a browser session... | [Free to start](../gates/free.md) |
| [Bonjoro](../tools/bonjoro.md)
bonjoro.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/bonjoro](https://zapier.com/mcp/bonjoro) | OAuth
Rides a Zapier account connection (OAuth to Zapier, which holds the Bonjoro-side... | [Paid, self-serve](../gates/paid.md) |
| [Sendspark](../tools/sendspark.md)
sendspark.com | [Community MCP](../mcp/community.md) | [https://composio.dev/toolkits/sendspark](https://composio.dev/toolkits/sendspark) | Third party platform auth
API-key based - Composio's page states Sendspark requires the user's own API key, which... | [Paid, self-serve](../gates/paid.md) |
| [Vidyard](../tools/vidyard.md)
vidyard.com | [Community MCP](../mcp/community.md) | [https://viasocket.com/mcp/vidyard](https://viasocket.com/mcp/vidyard) | Third party platform auth
Not documented in technical detail on the viaSocket listing ("built-in authentication").... | [Paid, self-serve](../gates/paid.md) |
| [Weezly](../tools/weezly.md)
weezly.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/weezly](https://zapier.com/mcp/weezly) | Third party platform auth
Zapier-mediated connection. | [Paid, self-serve](../gates/paid.md) |
| [BombBomb](../tools/bombbomb.md)
bombbomb.com | [Community MCP](../mcp/community.md) | [https://zapier.com/mcp/bombbombcom](https://zapier.com/mcp/bombbombcom) | OAuth or an API key
Rides Zapier's own OAuth/API-key connection to BombBomb; not a native BombBomb MCP auth... | [Enterprise only](../gates/enterprise-only.md) |

### The other 5 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [Covideo](../tools/covideo.md)
covideo.com | [MCP unknown](../mcp/unknown.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-08-24 |
| [Dubb](../tools/dubb.md)
dubb.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-08-24 |
| [Hippo Video](../tools/hippo-video.md)
hippovideo.io | [No MCP found](../mcp/none-found.md) | [Enterprise leaning](../gates/enterprise-leaning.md) | 2026-08-24 |
| [Potion](../tools/potion.md)
sendpotion.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-08-24 |
| [Quickpage](../tools/quickpage.md)
quickpage.io | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-08-24 |

### What this category is asked for

The jobs most often tagged on the 14 tagged entries in this category.

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)
- [Book a meeting](../jobs/book-a-meeting.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Create a digital sales room](../jobs/create-digital-sales-room.md)

Counted 2026-09-02 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
