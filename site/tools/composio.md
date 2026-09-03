# Composio: MCP server status, API access gate and what it does

> A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Composio

# Composio

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [composio.dev](https://composio.dev) · entry id 07-composio · source 07-mcp-infrastructure.md line 11

**What it does**
A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps (HubSpot, Slack, Gmail, GitHub, Notion, Stripe, and others) through Composio-managed OAuth.

**AI features, separated from automation with an AI label on it**
none in Composio itself - it is tool/auth plumbing that any LLM or agent framework (Claude, GPT, LangChain, CrewAI, or a raw MCP client) calls into. The "AI" is whichever agent is on the other end, not something Composio adds.

**RevOps role**
The connector layer a solo RevOps engineer reaches for instead of hand-building OAuth + API wrappers for a dozen GTM tools one at a time.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Composio brokers OAuth for each connected toolkit (HubSpot, Gmail, Slack, etc.) on the user's behalf, then gates the MCP endpoint itself with an x-api-key header (required by default for new orgs). MCP endpoint pattern is https://backend.composio.dev/v3/mcp/{server_id}?user_id={user_id}.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://docs.composio.dev/mcp/overview](https://docs.composio.dev/mcp/overview)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.composio.dev/docs/single-toolkit-mcp (redirect correction 2026-08-28: the address previously recorded here, docs.composio.dev/mcp/overview, 308s to this one and this one returns 200)

- [https://docs.composio.dev/docs/single-toolkit-mcp](https://docs.composio.dev/docs/single-toolkit-mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (100K tool calls/mo, 50K trigger events/mo, unlimited connections on the Free plan, no credit card)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://composio.dev](https://composio.dev)
- [https://composio.dev/pricing](https://composio.dev/pricing)
- [https://docs.composio.dev/docs/single-toolkit-mcp](https://docs.composio.dev/docs/single-toolkit-mcp)

3 source URLs. Raw sources field, verbatim:

https://composio.dev, https://composio.dev/pricing, https://docs.composio.dev/docs/single-toolkit-mcp

**Notes, verbatim from the file**
Composio holds the OAuth tokens for every connected toolkit - it is a custodial broker, not a pass-through. Pro tier ($29/mo) adds pay-as-you-scale overage at $0.0003/tool call; Enterprise adds SSO/SCIM and a KMS proxy for teams that don't want Composio holding raw tokens.

**Provenance**

- **Entry id**: 07-composio

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 11

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
