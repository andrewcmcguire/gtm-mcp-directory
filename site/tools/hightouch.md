# Hightouch: MCP server status, API access gate and what it does

> A CDP/reverse-ETL platform that syncs warehouse data (Snowflake, BigQuery, Databricks, Redshift) to 300+... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

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

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [hightouch.com](https://hightouch.com) · entry id 06-hightouch · source 06-revops-infra.md line 311

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
- **Docs URL**: [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (gated)

mcp_url, verbatim from the file:

https://hightouch.com/docs/ai-integrations/mcp

- [https://hightouch.com/docs/ai-integrations/mcp](https://hightouch.com/docs/ai-integrations/mcp)

**What this server exposes**

- **Tools named**: 2
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **read_doc** Returns the full markdown content of a documentation page by path. Use paths from search_docs results. evidence: in the vendor docs · calling it reads · required: path

- **search_docs** Full-text search across all public docs with per-heading granularity. Returns matching sections with title, URL, content snippet, and section hierarchy. evidence: in the vendor docs · calling it reads

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the REST API is open to all Hightouch users (bearer-token API key), available even on the free Basic Reverse ETL tier (up to 2 active syncs, unlimited destinations/seats, no sales conversation required for the API itself).

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/hightouchio](https://github.com/hightouchio) tied to the vendor by rule 3, account website https://hightouch.com has the vendor's domain, confidence strong

- **Public repositories**: 16, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-07-29

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [design-team](https://github.com/hightouchio/design-team) | other | This is a test of the new design team site. | 0 | 2026-07-29 | |
| [tfc-agent](https://github.com/hightouchio/tfc-agent) | infrastructure | Terraform Cloud Agent with some customizations | 0 | 2026-06-11 | |
| [airflow-provider-hightouch](https://github.com/hightouchio/airflow-provider-hightouch) | infrastructure | Airflow operators, hooks, and sensors for interacting with the Hightouch API | 16 | 2026-04-24 | 5.0.0 |
| [passage](https://github.com/hightouchio/passage) | other | Secure private tunnels as a service :closed_lock_with_key: | 46 | 2025-10-03 | v0.3.6 |
| [bottlerocket-bootstrap-storage](https://github.com/hightouchio/bottlerocket-bootstrap-storage) | other | Bootstrap container to configure storage on Bottlerocket instances | 0 | 2025-02-21 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Sync records between systems](../jobs/sync-records-between-systems.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 559 entries carry at least one tag; 849 tags are assigned in total.

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

- **Source line**: 311

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
