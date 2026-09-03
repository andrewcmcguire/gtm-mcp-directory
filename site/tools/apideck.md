# Apideck: MCP server status, API access gate and what it does

> A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint... Official MCP, Free to start. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Apideck

# Apideck

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [apideck.com](https://apideck.com) · entry id 07-apideck · source 07-mcp-infrastructure.md line 266

**What it does**
A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint covering CRM, accounting, HRIS, ATS, file storage and issue tracking.

**AI features, separated from automation with an AI label on it**
A dynamic mode that exposes only four meta-tools so the agent discovers and executes tools on demand instead of loading every schema up front, cutting the context cost to roughly 1,300 tokens. That is a genuine agent-design feature rather than an AI claim.

**RevOps role**
One integration layer so an agent can read and write across every CRM in a portfolio without wiring each vendor separately; the multi-CRM abstraction a GTM agent needs when it cannot assume which CRM it will meet.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Managed OAuth via Apideck Vault on the hosted endpoint, or x-apideck-api-key plus x-apideck-app-id plus x-apideck-consumer-id headers for direct use.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/apideck-libraries/mcp (docs: https://developers.apideck.com/mcp; hosted endpoint: see the caveat in notes)

- [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp)
- [https://developers.apideck.com/mcp](https://developers.apideck.com/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

[https://developers.apideck.com/mcp](https://developers.apideck.com/mcp)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp)

**Jobs it can do**

- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developers.apideck.com/mcp](https://developers.apideck.com/mcp)
- [https://www.apideck.com/mcp-server](https://www.apideck.com/mcp-server)
- [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp)

3 source URLs. Raw sources field, verbatim:

https://developers.apideck.com/mcp, https://www.apideck.com/mcp-server, https://github.com/apideck-libraries/mcp

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. CAVEAT ON THE ENDPOINT: two different hosted endpoints appear in the vendor's own material, mcp.apideck.com in the developer docs and mcp.apideck.dev on the marketing page. Confirm which is current before wiring it up; the GitHub repo is cited as mcp_url because it is the one unambiguous vendor-owned artifact. Signup is self-serve and free to start, but the paid tier thresholds are not published, so "free" here means free-to-start, not free-at-volume. The four-meta-tool dynamic mode is the same design problem the Salesforce Hosted MCP entry (06) solves with Discover/Describe/Dispatch, and the two make a natural pair for a segment on how not to dump 3,000 tools on an agent.

**Provenance**

- **Entry id**: 07-apideck

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 266

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
