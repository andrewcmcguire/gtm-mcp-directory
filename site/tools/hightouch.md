# Hightouch: MCP server status, API access gate and what it does

> A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Hightouch

# Hightouch

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [hightouch.com](https://hightouch.com) · entry id 06-hightouch · source 06-revops-infra.md line 300

**What it does**
A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+ downstream tools (ad platforms, CRMs, marketing automation) for audience activation and personalization.

**AI features, separated from automation with an AI label on it**
More AI-forward than most peers - "AI Decisioning" (reinforcement-learning-based 1:1 personalization, per their own docs - the specific "reinforcement learning" framing is vendor-stated and not independently verified beyond marketing language), "Proactive Insights" (agents surfacing signals across data/market/competitors), and AI content generation for Lifecycle Studio (email/SMS) and Ad Studio (ad creative).

**RevOps role**
Sits between the warehouse and GTM execution tools - the activation layer that turns modeled/scored data into audiences, syncs, and now AI-generated campaign content.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Existing Hightouch workspace auth with role-based access control; however the MCP server itself "must be enabled by Hightouch - contact us to turn it on," so it is not self-serve activatable even though the auth mechanism itself is standard.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (gated)

mcp_url, verbatim from the file:

https://hightouch.com/docs/ai-integrations/mcp

- [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the REST API is open to all Hightouch users (bearer-token API key), available even on the free Basic Reverse ETL tier (up to 2 active syncs, unlimited destinations/seats, no sales conversation required for the API itself).

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.hightouch.com/](https://www.hightouch.com/)
- [https://hightouch.com/pricing](https://hightouch.com/pricing)
- [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp)
- [https://hightouch.com/docs/developer-tools/api-guide](https://hightouch.com/docs/developer-tools/api-guide)

4 source URLs. Raw sources field, verbatim:

https://www.hightouch.com/, https://hightouch.com/pricing, https://hightouch.com/docs/ai-integrations/mcp, https://hightouch.com/docs/developer-tools/api-guide

**Notes, verbatim from the file**
The MCP capability itself is read-write and functionally broad (create audiences, manage syncs, design journeys, generate email/ad content) - one of the more substantive MCP implementations researched for this file, but a solo operator can't self-serve turn it on; it requires contacting Hightouch first.

**Provenance**

- **Entry id**: 06-hightouch

- **Source file**: 06-revops-infra.md

- **Source line**: 300

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
