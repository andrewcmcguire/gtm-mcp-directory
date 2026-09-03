# Scheduling & Routing tools with MCP servers: 7 of 14, counted

> 7 of the 14 scheduling & routing tools in The GTM MCP Directory have an MCP server: 5 official and 2 community. The server URL, auth model and access gate for each. Counted 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / Scheduling & Routing tools with an MCP server

**List · 7 of 293**

## Scheduling & Routing tools with an MCP server

The last mile of a GTM motion: turning a qualified lead into a meeting on a rep's calendar, instantly and to the right person, then keeping that rep's own calendar sane. Three sub-lanes live in this file - prospect-facing booking pages (Calendly, Cal.com, SavvyCal), inbound lead-routing/handoff engines (Chili Piper, Default, RevenueHero, Kronologic, LeanData), and personal calendar-intelligence tools for reps/AEs (Motion, Reclaim.ai, Clockwise, Trevor AI) - plus two adjacent discovery finds (Clara, Doodle). MCP maturity here splits the same way category-06 does: the open-source/API-first booking tools (Cal.com, Calendly) shipped clean official servers, while most routing engines and personal-calendar apps have none or only community ones. 7 of 14 entries in this category are reachable by an agent: 5 through a server the vendor maintains and 2 through one somebody else built. The category is tagged most often with Read calendar availability. [See the full category page](../categories/scheduling-routing.md).

| Tool | MCP status | Server URL | Auth | Gate |
|---|---|---|---|---|
| [Cal.com](../tools/cal-com.md)
cal.com | [Official MCP](../mcp/official.md) | [https://github.com/calcom/cal-mcp](https://github.com/calcom/cal-mcp) +1 more | OAuth or an API key
Two paths. Hosted server (mcp.cal.com) uses OAuth 2.1 - "your client handles the... | [Free to start](../gates/free.md) |
| [Calendly](../tools/calendly.md)
calendly.com | [Official MCP](../mcp/official.md) | [https://developer.calendly.com/calendly-mcp-server](https://developer.calendly.com/calendly-mcp-server) +3 more | OAuth or an API key
OAuth 2.1 Authorization Code + PKCE (S256) with Dynamic Client Registration (RFC 7591).... | [Free to start](../gates/free.md) |
| [Chili Piper](../tools/chili-piper.md)
chilipiper.com | [Official MCP](../mcp/official.md) | [https://www.chilipiper.com/products/mcp](https://www.chilipiper.com/products/mcp) +3 more | OAuth or an API key
Two supported paths, both vendor-documented. Option A (vendor-recommended): a Chili Piper... | [Paid, self-serve](../gates/paid.md) |
| [Reclaim.ai](../tools/reclaim-ai.md)
reclaim.ai | [Official MCP](../mcp/official.md) | [https://mcp.reclaim.ai](https://mcp.reclaim.ai) | OAuth or an API key
OAuth (official hosted server). A separate unofficial/community server also exists... | [Gate unknown](../gates/unknown.md) |
| [RevenueHero](../tools/revenuehero.md)
revenuehero.io | [Official MCP](../mcp/official.md) | [https://www.revenuehero.io/resources/tales-of-ops](https://www.revenuehero.io/resources/tales-of-ops) | API key
Per-customer router token over an SSE endpoint, manually provisioned by RevenueHero - not... | [Gate unknown](../gates/unknown.md) |
| [Motion](../tools/motion.md)
usemotion.com | [Community MCP](../mcp/community.md) | [https://github.com/RF-D/motion-mcp](https://github.com/RF-D/motion-mcp) | API key
API key (MOTION_API_KEY from Motion Settings -> API), per community repos. Rate limits... | [Paid, self-serve](../gates/paid.md) |
| [SavvyCal](../tools/savvycal.md)
savvycal.com | [Community MCP](../mcp/community.md) | [https://github.com/arturkoter/savvycal-mcp-server](https://github.com/arturkoter/savvycal-mcp-server) | API key
API key (SAVVYCAL_API_KEY env var, a personal access token from SavvyCal's Developer... | [Paid, self-serve](../gates/paid.md) |

### The other 7 in this category

No server found, or the check could not settle it. Same category, not reachable by an agent today.

| Tool | MCP status | Gate | Checked |
|---|---|---|---|
| [Default](../tools/default.md)
default.com | [MCP unknown](../mcp/unknown.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [LeanData](../tools/leandata.md)
leandata.com | [MCP unknown](../mcp/unknown.md) | [Enterprise only](../gates/enterprise-only.md) | 2026-09-02 |
| [Clockwise](../tools/clockwise.md)
getclockwise.com | [MCP not applicable](../mcp/n-a.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |
| [Clara (Clara Labs)](../tools/clara.md)
claralabs.com | [No MCP found](../mcp/none-found.md) | [Paid, self-serve](../gates/paid.md) | 2026-09-02 |
| [Doodle](../tools/doodle.md)
doodle.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |
| [Kronologic](../tools/kronologic.md)
kronologic.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |
| [Trevor AI](../tools/trevor-ai.md)
trevorai.com | [No MCP found](../mcp/none-found.md) | [Gate unknown](../gates/unknown.md) | 2026-09-02 |

### What this category is asked for

The jobs most often tagged on the 13 tagged entries in this category.

- [Read calendar availability](../jobs/read-calendar-availability.md)
- [Book a meeting](../jobs/book-a-meeting.md)
- [Route an inbound lead](../jobs/route-inbound-lead.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)

Counted 2026-09-03 from directory.json and reconciled against tools_recount.py. Nothing on this page is hand maintained: it is a filter over the same 293 entries the rest of the site is built from. Ordered by the published rule: official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.
