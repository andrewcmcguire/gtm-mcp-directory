# HeyReach: MCP server status, API access gate and what it does

> Cloud-based LinkedIn outreach automation platform for agencies/sales teams running multi-account connection,... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
HeyReach

# HeyReach

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [heyreach.io](https://heyreach.io) · entry id 02-heyreach · source 02-engagement-outbound.md line 350

**What it does**
Cloud-based LinkedIn outreach automation platform for agencies/sales teams running multi-account connection, messaging, and inbox campaigns from unlimited LinkedIn accounts.

**AI features, separated from automation with an AI label on it**
AI filters, message personalization, and message-optimization suggestions bundled in the paid plan - applied LLM copy generation/scoring layered on top of rule-based sequencing, not a novel capability.

**RevOps role**
LinkedIn multi-account outbound execution layer, downstream of list-building/enrichment tools and upstream of CRM via API/webhooks.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: workspace-scoped "MCP key" + connection URL (API-key-style, not OAuth)

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.heyreach.io/mcp ; setup docs at https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools

- [https://www.heyreach.io/mcp](https://www.heyreach.io/mcp)
- [https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools](https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.heyreach.io/pricing](https://www.heyreach.io/pricing)
- [https://www.heyreach.io/mcp](https://www.heyreach.io/mcp)
- [https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools](https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools)
- [https://www.heyreach.io/blog/campaign-api](https://www.heyreach.io/blog/campaign-api)

4 source URLs. Raw sources field, verbatim:

https://www.heyreach.io/pricing, https://www.heyreach.io/mcp, https://help.heyreach.io/en/articles/12117291-how-does-heyreach-mcp-work-with-popular-tools, https://www.heyreach.io/blog/campaign-api

**Notes, verbatim from the file**
No permanent free tier (14-day trial only); cheapest paid plan is Growth at $79/mo/sender, with API and MCP included. A third-party/unofficial MCP repo (github.com/bcharleson/heyreach-mcp) predates and duplicates the official one - don't conflate them. Like all LinkedIn automation tools, this operates against LinkedIn's User Agreement, which prohibits third-party bots/automation (linkedin.com/help/linkedin/answer/a1341387).

**Provenance**

- **Entry id**: 02-heyreach

- **Source file**: 02-engagement-outbound.md

- **Source line**: 350

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
