# Affinity: MCP server status, API access gate and what it does

> A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Affinity

# Affinity

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [affinity.co](https://affinity.co) · entry id 06-affinity · source 06-revops-infra.md line 456

**What it does**
A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar activity and scores relationship strength, rather than relying on reps to log activity.

**AI features, separated from automation with an AI label on it**
Semantic search across companies and people, relationship-strength scoring, and meeting-transcript retrieval. The contact-graph construction itself is automation over mail and calendar metadata, not AI.

**RevOps role**
System of record for relationship-driven pipelines, primarily private capital, with warm-path discovery layered on top of the CRM itself.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth where the client supports it, otherwise an API key. Local deployment is API key only. All MCP queries inherit the connecting user's existing Affinity permissions.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-03, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-03 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.affinity.co/mcp (docs: https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP)

- [https://mcp.affinity.co/mcp](https://mcp.affinity.co/mcp)
- [https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP](https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP](https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Discover warm intro paths](../jobs/discover-warm-intro-paths.md)
- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP](https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP)
- [https://www.affinity.co/blog/affinity-is-building-the-best-mcp-for-private-capital](https://www.affinity.co/blog/affinity-is-building-the-best-mcp-for-private-capital)
- [https://www.affinity.co/product/crm](https://www.affinity.co/product/crm)

3 source URLs. Raw sources field, verbatim:

https://support.affinity.co/s/article/Getting-started-with-Affinity-MCP, https://www.affinity.co/blog/affinity-is-building-the-best-mcp-for-private-capital, https://www.affinity.co/product/crm

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. API and MCP access are restricted to the Scale, Advanced and Enterprise tiers; lower tiers cannot use it at all. Launched in beta in 2026 with roughly 33 read and write tools. TRANSFERABILITY CAVEAT: Affinity is aimed at VC, PE and investment banking rather than classic B2B SaaS sales, so the relationship-strength model is tuned for a different motion than most of this directory. Included because the auto-built relationship graph is the same job Centralize (05) and The Swarm (01) do, approached from a third direction, and the three together are a coherent lane.

**Provenance**

- **Entry id**: 06-affinity

- **Source file**: 06-revops-infra.md

- **Source line**: 456

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
