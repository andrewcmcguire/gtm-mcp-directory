# Artisan AI (Ava): MCP server status, API access gate and what it does

> An AI agent ("Ava") that finds and enriches B2B leads, writes and sends personalized outreach, handles... Official MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
Artisan AI (Ava)

# Artisan AI (Ava)

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.artisan.co](https://www.artisan.co) · entry id 04-artisan-ai · source 04-ai-sdr-agents.md line 30

**What it does**
An AI agent ("Ava") that finds and enriches B2B leads, writes and sends personalized outreach, handles replies, and books meetings - marketed as running outbound "end to end."

**AI features, separated from automation with an AI label on it**
Lead research/enrichment and message personalization are AI-driven per vendor copy; reply-handling and end-to-end autonomy claims ("runs outbound end to end") could not be independently verified - treat as vendor-copy-only until bench-tested.

**RevOps role**
Full-funnel outbound replacement layer - positioned to replace an entire SDR hire, not just a sequencing tool.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: none required - a JSON-RPC initialize POST to the endpoint with no credentials answered HTTP 200 on 2026-09-02 (serverInfo name "artisan-content", title "Artisan Content MCP", version 1.0.0)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: answered as an MCP server
- **Endpoint URL[https://www.artisan.co/mcp](https://www.artisan.co/mcp)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official (content-only)

mcp_url, verbatim from the file:

https://www.artisan.co/mcp

- [https://www.artisan.co/mcp](https://www.artisan.co/mcp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (all three tiers show no dollar amounts and route to talk-to-sales, no tier lists API access, and the only public developer artefact is a read-only MCP server over Artisan's marketing content)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)
- [Book a meeting](../jobs/book-a-meeting.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.artisan.co](https://www.artisan.co)
- [https://www.artisan.co/pricing](https://www.artisan.co/pricing)
- [https://www.artisan.co/llms.txt](https://www.artisan.co/llms.txt)
- [https://www.artisan.co/mcp](https://www.artisan.co/mcp)

4 source URLs. Raw sources field, verbatim:

https://www.artisan.co, https://www.artisan.co/pricing, https://www.artisan.co/llms.txt, https://www.artisan.co/mcp

**Notes, verbatim from the file**
Famous for its 2024 "stop hiring humans" billboard campaign - a marketing stance worth noting since it signals how aggressively the vendor copy should be discounted. Good bench-test candidate precisely because the claims are so strong. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.artisan.co/pricing): all three tiers show no dollar amounts and route to talk-to-sales, no tier lists API access, and the only public developer artefact is a read-only MCP server over Artisan's marketing content. 2026-09-02: mcp_status none-found -> official (content-only). https://www.artisan.co/llms.txt lists a "Model Context Protocol server (Streamable HTTP, revision 2025-06-18) exposing Artisan's public pages and blog as read-only tools" at https://www.artisan.co/mcp, and that endpoint answered an initialize request today with the instructions "Read-only access to Artisan's public marketing pages and blog. Use list_pages / get_page for site content and search_blog / get_blog_post for articles." A first-party endpoint that answers clears law 1, but this is a marketing-content reader in the Ada mould, not an MCP over Ava or any customer data; do not present it as an AI SDR MCP.

**Provenance**

- **Entry id**: 04-artisan-ai

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 30

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
