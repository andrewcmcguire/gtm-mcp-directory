# Browserbase: MCP server status, API access gate and what it does

> A hosted headless-browser service (sessions, proxies, stealth, session recording) with Stagehand, its... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Browserbase

# Browserbase

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [browserbase.com](https://browserbase.com) · entry id 01-browserbase · source 01-data-enrichment.md line 930

**What it does**
A hosted headless-browser service (sessions, proxies, stealth, session recording) with Stagehand, its natural-language browser automation layer, so agents can navigate, act on and extract from web pages that plain HTTP fetching cannot reach.

**AI features, separated from automation with an AI label on it**
The browser hosting is infrastructure. Stagehand's act, observe and extract tools take natural-language instructions and use a model to pick page elements and pull data; the MCP setup docs expose a model flag ("The model to use for Stagehand"), so the AI is a configurable layer on top of the browser.

**RevOps role**
The browser layer under an enrichment or research agent for pages behind logins, JavaScript rendering or anti-bot walls; the step after Firecrawl or Tavily fail on a target site.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key passed as a browserbaseApiKey query parameter on the endpoint URL; the docs list it as "Required for tool calls". Six tools: navigate, act, observe, extract, start, end, each taking an optional sessionId.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.browserbase.com/mcp (docs: https://docs.browserbase.com/integrations/mcp/setup)

- [https://mcp.browserbase.com/mcp](https://mcp.browserbase.com/mcp)
- [https://docs.browserbase.com/integrations/mcp/setup](https://docs.browserbase.com/integrations/mcp/setup)

**What this server exposes**

- **Tools named**: 6
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-08
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **act** Perform an action on the page evidence: answered tools/list · calling it reads · required: action

- **end** Close the current Browserbase session evidence: answered tools/list · calling it reads

- **extract** Extract data from the page evidence: answered tools/list · calling it reads

- **navigate** Navigate to a URL evidence: answered tools/list · calling it reads · required: url

- **observe** Observe actionable elements on the page evidence: answered tools/list · calling it reads · required: instruction

- **start** Create or reuse a Browserbase session evidence: answered tools/list · calling it writes

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the pricing page lists Free at $0/mo with "1 browser hour", 3 concurrent browsers, "15 minutes /session", "1,000 Search calls" and "1,000 Fetch calls"; Developer $20/mo ("100 browser hours then $0.12/browser hr"), Startup $99/mo ("500 browser hours then $0.10/browser hr"), Scale custom.

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

- [https://docs.browserbase.com/integrations/mcp/setup](https://docs.browserbase.com/integrations/mcp/setup)
- [https://www.browserbase.com/pricing](https://www.browserbase.com/pricing)
- [https://mcp.browserbase.com/mcp](https://mcp.browserbase.com/mcp)

3 source URLs. Raw sources field, verbatim:

https://docs.browserbase.com/integrations/mcp/setup, https://www.browserbase.com/pricing, https://mcp.browserbase.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.browserbase.com/mcp with no key returned HTTP 200 with a JSON-RPC result, serverInfo name "stagehand-api" (protocolVersion 2025-03-26); the control POST to /zzz-not-a-route returned 404. Initialize succeeds keyless and, per the docs, the key is enforced at tool-call time. The candidate row's proposed alternative category was mcp-infrastructure; it lands here because its GTM use is data collection, the same reasoning as Bright Data. One browser hour a month on Free is a demo allowance, not a working allowance. 2026-09-07: https://mcp.browserbase.com/mcp returned 200 with a JSON-RPC initialize result to an MCP initialize POST (https://mcp.browserbase.com/mcp).

**Provenance**

- **Entry id**: 01-browserbase

- **Source file**: 01-data-enrichment.md

- **Source line**: 930

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
