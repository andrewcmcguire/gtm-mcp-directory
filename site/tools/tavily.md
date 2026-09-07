# Tavily: MCP server status, API access gate and what it does

> A web search and page-extraction API built for LLM agents that returns ranked, cleaned results and extracted... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Tavily

# Tavily

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [tavily.com](https://tavily.com) · entry id 01-tavily · source 01-data-enrichment.md line 911

**What it does**
A web search and page-extraction API built for LLM agents that returns ranked, cleaned results and extracted page content rather than a list of links.

**AI features, separated from automation with an AI label on it**
The search ranking and content extraction are tuned for agent consumption, which is the vendor's pitch, but the product is an API a model calls; the AI is the caller. The MCP server exposes two tools, tavily-search and tavily-extract.

**RevOps role**
The live-research leg of an account-research agent, the same job Exa does in this file, with a search-plus-extract pair sized for a solo operator on the free tier.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key as a tavilyApiKey query parameter or in the Authorization header, or OAuth. The docs state "OAuth authentication is optional, you can still use API key authentication at any time by including your Tavily API key in the URL query parameter (?tavilyApiKey=...) or by setting it in the Authorization header."

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.tavily.com/mcp/ (docs: https://docs.tavily.com/documentation/mcp)

- [https://mcp.tavily.com/mcp/](https://mcp.tavily.com/mcp/)
- [https://docs.tavily.com/documentation/mcp](https://docs.tavily.com/documentation/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the pricing page lists a Researcher tier at $0/month with "1,000 API credits / month" and "No credit card required", pay as you go at "$0.008 / credit", a Project plan from "4,000 API credits / month", and Enterprise at "Custom".

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://docs.tavily.com/documentation/mcp](https://docs.tavily.com/documentation/mcp)
- [https://www.tavily.com/pricing](https://www.tavily.com/pricing)
- [https://mcp.tavily.com/mcp/](https://mcp.tavily.com/mcp/)

3 source URLs. Raw sources field, verbatim:

https://docs.tavily.com/documentation/mcp, https://www.tavily.com/pricing, https://mcp.tavily.com/mcp/

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.tavily.com/mcp/ returned HTTP 401 with an empty body; the control POST to /zzz-not-a-route returned 404 "Not Found". Live first-party auth-gated server. The docs put the API key in the URL query string as the primary example; a key in a URL ends up in client logs and config files, which is worth saying before anyone pastes it on camera. The endpoint carries a trailing slash. 2026-09-07: https://mcp.tavily.com/mcp/ returned 401 to an MCP initialize POST (https://mcp.tavily.com/mcp/).

**Provenance**

- **Entry id**: 01-tavily

- **Source file**: 01-data-enrichment.md

- **Source line**: 911

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
