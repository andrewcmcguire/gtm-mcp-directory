# Clockwise: MCP server status, API access gate and what it does

> Historical - team-calendar optimization app that auto-scheduled/rescheduled meetings across a team, defended... No MCP found, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Clockwise

# Clockwise

[No MCP found](../mcp/none-found.md)
[Gate unknown](../gates/unknown.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [getclockwise.com](https://getclockwise.com) · entry id 10-clockwise · source 10-scheduling-routing.md line 160

**What it does**
Historical - team-calendar optimization app that auto-scheduled/rescheduled meetings across a team, defended Focus Time, and blocked task time factoring in each person's working hours/preferences. THE PRODUCT IS SHUT DOWN - see notes.

**AI features, separated from automation with an AI label on it**
Historical - multi-party meeting-conflict resolution and rescheduling, Focus Time optimization, "smart holds": classic scheduling-optimization algorithms marketed as AI-driven ("scheduling intelligence"). No independently verified LLM-specific feature (e.g. generative summary/chat) was documented before shutdown.

**RevOps role**
Formerly filled the same team-calendar-optimization niche as Reclaim/Motion for reps and AEs. No longer usable.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a (was OAuth, per historical PulseMCP listing and Clockwise's own support docs)

- **Parsed URLs**: 1 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a (was https://mcp.getclockwise.com - endpoint no longer resolves; historical announcement was at getclockwise.com/blog/introducing-clockwise-mcp, no longer live)

- [https://mcp.getclockwise.com](https://mcp.getclockwise.com)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown/moot - product discontinued, no live API to gate

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: dead. Entry says THE PRODUCT IS SHUT DOWN. It did book-a-meeting and read-calendar-availability; tagging a dead endpoint as supply is exactly the failure INDEX.md finding 5 warns about.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.getclockwise.com](https://www.getclockwise.com)
- [https://aiforautomation.io/news/2026-03-20-clockwise-ai-scheduling-salesforce-acquires-shuts-down](https://aiforautomation.io/news/2026-03-20-clockwise-ai-scheduling-salesforce-acquires-shuts-down)
- [https://thedailyclaws.com/blog/2026-03-20-news-clockwise-shutdown-salesforce/](https://thedailyclaws.com/blog/2026-03-20-news-clockwise-shutdown-salesforce/)
- [https://www.usecarly.com/blog/is-clockwise-shutting-down/](https://www.usecarly.com/blog/is-clockwise-shutting-down/)
- [https://finance.yahoo.com/sectors/technology/articles/salesforce-recuits-team-behind-calendar-app-clockwise-103000806.html](https://finance.yahoo.com/sectors/technology/articles/salesforce-recuits-team-behind-calendar-app-clockwise-103000806.html)
- [https://vantagepoint.io/blog/sf/clockwise-salesforce-agentic-ai-acquihire-crm-strategy](https://vantagepoint.io/blog/sf/clockwise-salesforce-agentic-ai-acquihire-crm-strategy)
- [https://www.pulsemcp.com/servers/clockwise](https://www.pulsemcp.com/servers/clockwise)

7 source URLs. Raw sources field, verbatim:

https://www.getclockwise.com, https://aiforautomation.io/news/2026-03-20-clockwise-ai-scheduling-salesforce-acquires-shuts-down, https://thedailyclaws.com/blog/2026-03-20-news-clockwise-shutdown-salesforce/, https://www.usecarly.com/blog/is-clockwise-shutting-down/, https://finance.yahoo.com/sectors/technology/articles/salesforce-recuits-team-behind-calendar-app-clockwise-103000806.html, https://vantagepoint.io/blog/sf/clockwise-salesforce-agentic-ai-acquihire-crm-strategy, https://www.pulsemcp.com/servers/clockwise

**Notes, verbatim from the file**
CLOCKWISE IS SHUT DOWN. Salesforce acqui-hired the Clockwise team in late 2025 (folded into Agentforce/agentic-AI effort - people, not the standalone product). getclockwise.com now shows a static wind-down notice stating the product "will no longer be available starting on March 27, 2026" - a date already passed as of this file's last_checked. support.getclockwise.com and mcp.getclockwise.com no longer resolve (confirmed via direct fetch during this research pass). Clockwise officially recommended Reclaim.ai as the migration path for departing customers, with a price-match guarantee cited by third-party sources. Kept in this file as a discontinued/historical entry on purpose - this kind of quiet mid-category death is exactly what INDEX.md's "quiet deaths and rebrands" section exists to catch. Do not present this as a live, usable tool in any published content. [api_gate 2026-08-25] Re-checked and left unknown, honestly: DEAD PRODUCT, confirmed 2026-08-25. getclockwise.com still resolves but every path, including /pricing, now serves a shutdown notice: the Clockwise team is joining Salesforce and the product shut down on 27 March 2026. Clockwise-managed calendar events and Scheduling Links stopped working, user data is deleted rather than transferred, prorated refunds were issued, and the page points customers to Reclaim with a price-match migration offer. This confirms and escalates the DYING flag raised in the 2026-08 sweep (INDEX.md finding 5). The entry needs a human decision on tombstoning versus delisting before the next republish; api_gate is left unknown because there is no longer a product to gate. Checked against https://www.getclockwise.com/.

**Provenance**

- **Entry id**: 10-clockwise

- **Source file**: 10-scheduling-routing.md

- **Source line**: 160

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
