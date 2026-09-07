# Merge Agent Handler: MCP server status, API access gate and what it does

> Merge's tool-calling platform for AI agents: it wraps hundreds of third-party SaaS applications as pre-built... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Merge Agent Handler

# Merge Agent Handler

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [merge.dev](https://merge.dev) · entry id 07-merge-agent-handler · source 07-mcp-infrastructure.md line 307

**What it does**
Merge's tool-calling platform for AI agents: it wraps hundreds of third-party SaaS applications as pre-built MCP-ready connectors, bundles them into scoped "tool packs" per agent, brokers per-end-user authentication, and puts a security gateway, redaction rules and an audit log in front of every tool call.

**AI features, separated from automation with an AI label on it**
None of its own by design. The product is governance and plumbing around somebody else's agent, and the features it sells (tool scoping, data-loss prevention, tool-call logs, audit trail) are controls rather than intelligence.

**RevOps role**
The governed alternative to handing an agent a dozen raw vendor MCP servers: one endpoint per user per tool pack, with the audit trail a security review will ask for, which is the difference between a demo and something a RevOps team can put in front of customer data.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key in an Authorization Bearer header, alongside the identity encoded in the URL itself. The docs are explicit that three values are needed on every connection: the tool pack (what tools), the registered user (whose credentials), and the access key (authorisation). Per-end-user OAuth to each connected application is brokered separately through Merge Link.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.merge.dev/api/v1/tool-packs//registered-users//mcp (docs: https://docs.merge.dev/merge-agent-handler/build/connecting-agents/mcp-integration and https://docs.merge.dev/merge-agent-handler/overview)

- [https://api.merge.dev/api/v1/tool-packs/](https://api.merge.dev/api/v1/tool-packs/)
- [https://docs.merge.dev/merge-agent-handler/build/connecting-agents/mcp-integration](https://docs.merge.dev/merge-agent-handler/build/connecting-agents/mcp-integration)
- [https://docs.merge.dev/merge-agent-handler/overview](https://docs.merge.dev/merge-agent-handler/overview)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the Agent Handler pricing tab publishes a Free tier at "$0 / month" that "Get started for free with 2,000 monthly credits", with unlimited registered users and unlimited tool packs, then Launch, Pro and Professional tiers, with Enterprise routed to "Contact sales". Credits are consumed per tool call.

**API documentation**

No documentation URL recorded.

289 of 318 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

47 of 318 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.merge.dev/merge-agent-handler/build/connecting-agents/mcp-integration](https://docs.merge.dev/merge-agent-handler/build/connecting-agents/mcp-integration)
- [https://docs.merge.dev/merge-agent-handler/overview](https://docs.merge.dev/merge-agent-handler/overview)
- [https://www.merge.dev/merge-agent-handler](https://www.merge.dev/merge-agent-handler)
- [https://www.merge.dev/pricing/agent-handler](https://www.merge.dev/pricing/agent-handler)

4 source URLs. Raw sources field, verbatim:

https://docs.merge.dev/merge-agent-handler/build/connecting-agents/mcp-integration, https://docs.merge.dev/merge-agent-handler/overview, https://www.merge.dev/merge-agent-handler, https://www.merge.dev/pricing/agent-handler

**Notes, verbatim from the file**
CORRECTION TO THE CANDIDATE ROW, and it matters: the address carried in CANDIDATES.md pointed at ah-api-develop.merge.dev, a development host. Merge's own documentation gives the production pattern as https://api.merge.dev/api/v1/tool-packs/{TOOL_PACK_ID}/registered-users/{REGISTERED_USER_ID}/mcp, and that is what is recorded above. Verified 2026-09-07 from the docs; no liveness probe result is recorded because the URL is per-tenant and cannot be constructed without a tool pack and a registered user. The docs also document a simplified URL for the "Agent Handler for Employees" setup, plus custom MCP servers and custom headers, so a buyer can front their own servers with the same gateway. Merge's own troubleshooting page names the two failure modes worth knowing before a bench test: a 401 on every call usually means the Bearer prefix is missing or the key belongs to the wrong environment, and session-ID mismatches require capturing and reusing the Mcp-Session-Id header. Merge sells three separate products on one brand (Unified, Agent Handler, Gateway) with three separate price lists; only Agent Handler is the MCP product and the $650/month figure that appears in Merge coverage belongs to the Unified API, not to this.

**Provenance**

- **Entry id**: 07-merge-agent-handler

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 307

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
