# Relevance AI: MCP server status, API access gate and what it does

> A platform for building and deploying specialist AI agents (research/enrichment, outbound prospecting,... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[AI SDRs](../categories/ai-sdr-agents.md) /
Relevance AI

# Relevance AI

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[AI SDRs](../categories/ai-sdr-agents.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://relevanceai.com](https://relevanceai.com) · entry id 04-relevance-ai · source 04-ai-sdr-agents.md line 163

**What it does**
A platform for building and deploying specialist AI agents (research/enrichment, outbound prospecting, meeting scheduling, deal review, proposal building) that teams configure and progress toward autonomous ("L3 Autopilot") operation.

**AI features, separated from automation with an AI label on it**
Genuinely a build-your-own-agent platform rather than a single packaged persona - the agentic depth depends entirely on what the operator configures; the "96.4% eval pass rate" and "L3 Autopilot" framing are vendor-reported metrics, not independently verified.

**RevOps role**
Agent-building layer that can sit anywhere in the stack depending on configuration - closer to infrastructure than a packaged point solution.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (tokens may expire after inactivity; re-auth via login flow); Viewer/Chat project roles get restricted read-only access automatically

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins](https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins (redirect correction 2026-08-28: the address previously recorded here, relevanceai.com/docs/integrations/mcp/programmatic-gtm/introduction, 308s to this one and this one returns 200)

- [https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins](https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the MCP server and Claude Code plugin are free to connect; usage (agent runs, tool executions) bills against the operator's Relevance AI plan

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: thin. Tagged nothing. It is a build-your-own-agent platform and the entry says the agentic depth depends entirely on what the operator configures. Its listed specialist agents (prospecting, scheduling, deal review, proposal building) would each be a tag, but tagging a builder with its example templates would inflate the supply count for six jobs at once.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://relevanceai.com](https://relevanceai.com)
- [https://marketplace.relevanceai.com/](https://marketplace.relevanceai.com/)
- [https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins](https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins)

3 source URLs. Raw sources field, verbatim:

https://relevanceai.com, https://marketplace.relevanceai.com/, https://relevanceai.com/docs/get-started/core-concepts/mcp-plugins

**Notes, verbatim from the file**
The seed list named this tool's SDR agent "Bosh" - that name could not be found anywhere on the current site or marketplace (agent templates found instead: "Outbound Prospector," "Sales Researcher," "Perfect 5 Leads," etc.). Either renamed, deprecated, or misremembered - flag as unconfirmed. This is one of the very few tools in this category with a confirmed, solo-operator-accessible official MCP - a strong bench-test candidate.

**Provenance**

- **Entry id**: 04-relevance-ai

- **Source file**: 04-ai-sdr-agents.md

- **Source line**: 163

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
