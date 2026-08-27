# Smithery: MCP server status, API access gate and what it does

> A registry and distribution marketplace for MCP servers - "publish once, install anywhere" - that indexes and... MCP not applicable, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Smithery

# Smithery

[MCP not applicable](../mcp/n-a.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [smithery.ai](https://smithery.ai) · entry id 07-smithery · source 07-mcp-infrastructure.md line 96

**What it does**
A registry and distribution marketplace for MCP servers - "publish once, install anywhere" - that indexes and distributes third-party servers rather than hosting them itself, plus an integrated OAuth/credential layer.

**AI features, separated from automation with an AI label on it**
none - a directory and connection-management layer, not an AI product.

**RevOps role**
A discovery and one-click-install layer for MCP servers; useful for finding tools but CRM-grade GTM servers (Salesforce, HubSpot, Slack, Gmail) were not prominent in what was surfaced during this research.

**MCP server**

- **Status bucket**: MCP not applicable

- **Auth**: For the servers listed, auth runs through "agent.pw," described as Smithery's own open-source agent credential vault - Smithery "handles OAuth flows, credential injection, and retries automatically," with connections persisting across chats/harnesses.

- **Parsed URLs**: 1 found in the mcp_url field

An MCP server is not a meaningful question for this entry. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

n/a (Smithery is the registry itself, not a vendor's own product MCP)

mcp_url, verbatim from the file:

https://smithery.ai

- [https://smithery.ai](https://smithery.ai)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free to browse; some individual listed servers charge per-call (e.g. one listed server at $0.01-$0.05/call) while others are free/open-source - pricing is per-server, not a single Smithery tier.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Discover MCP servers](../jobs/discover-mcp-servers.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://smithery.ai](https://smithery.ai)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 17 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://smithery.ai

**Notes, verbatim from the file**
Smithery lists 17,000+ MCP servers by its own count. Because Smithery's agent.pw vault handles OAuth and "credential injection" for listed servers, using it to connect a GTM app means trusting that vault with the resulting tokens - worth confirming per-server before connecting anything with write access.

**Provenance**

- **Entry id**: 07-smithery

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 96

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
