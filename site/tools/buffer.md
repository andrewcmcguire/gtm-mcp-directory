# Buffer: MCP server status, API access gate and what it does

> A social-media scheduling and publishing tool covering channels, a posting queue, drafts, ideas and per-post... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Buffer

# Buffer

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [buffer.com](https://buffer.com) · entry id 15-buffer · source 15-community-dark-social.md line 311

**What it does**
A social-media scheduling and publishing tool covering channels, a posting queue, drafts, ideas and per-post analytics, with a remote MCP server that lets an AI assistant read channels, browse the queue and drafts, schedule and edit posts, capture ideas and pull analytics.

**AI features, separated from automation with an AI label on it**
An AI Assistant for drafting and repurposing post copy is included from the Free plan upward. The MCP server itself adds no intelligence; it makes the queue and the analytics addressable by whichever model the operator already uses.

**RevOps role**
The publishing arm of a founder-led or community-led motion: the place a distribution calendar actually executes, and, via MCP, the point where an agent can queue and adjust posts without a human opening the app.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key. The vendor's guide instructs the user to generate an API key from the developer site and send it as "Authorization: Bearer YOUR_API_KEY" against the server URL; the same key is shared with Buffer's API Explorer.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.buffer.com/mcp (docs: https://developers.buffer.com/guides/integrations/mcp.html)

- [https://mcp.buffer.com/mcp](https://mcp.buffer.com/mcp)
- [https://developers.buffer.com/guides/integrations/mcp.html](https://developers.buffer.com/guides/integrations/mcp.html)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - Buffer's pricing page publishes a Free plan, "Free forever", connecting up to 3 channels, whose included feature list carries "API access" with "1 API key" and "3,000 requests/month". Paid tiers are Essentials at $5 per channel per month and Team at $10 per channel per month, raising the allowance to 3 keys and 7,500 requests and 5 keys and 15,000 requests respectively.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/bufferapp](https://github.com/bufferapp) tied to the vendor by rule 3, account website https://overflow.buffer.com has the vendor's domain, confidence strong

- **Public repositories**: 129, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-02

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [vpat](https://github.com/bufferapp/vpat) | other | Contains VPAT document for Buffer | 1 | 2026-09-02 | |
| [buffer-n8n](https://github.com/bufferapp/buffer-n8n) | plugin or integration | The official Buffer integration for n8n | 0 | 2026-08-27 | v3.8.1 |
| [smart-tag](https://github.com/bufferapp/smart-tag) | other | | 0 | 2026-05-13 | |
| [js-bufflog](https://github.com/bufferapp/js-bufflog) | other | logger for all javascript and typescript Buffer services | 0 | 2026-05-13 | |
| [go-base-worker](https://github.com/bufferapp/go-base-worker) | other | Golang packages needed to build a consumers | 3 | 2026-03-23 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://developers.buffer.com/guides/integrations/mcp.html](https://developers.buffer.com/guides/integrations/mcp.html)
- [https://buffer.com/pricing](https://buffer.com/pricing)
- [https://mcp.buffer.com/mcp](https://mcp.buffer.com/mcp)

3 source URLs. Raw sources field, verbatim:

https://developers.buffer.com/guides/integrations/mcp.html, https://buffer.com/pricing, https://mcp.buffer.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.buffer.com/mcp returned HTTP 401 with {"error":"Authorization header is required","httpCode":401}, confirming a live auth-gated server, and the endpoint is printed verbatim in Buffer's own developer guide. THIS IS THE CHEAPEST OFFICIAL MCP SERVER FOUND IN THIS CATEGORY: a genuine free-forever plan carries a working API key and 3,000 requests a month, in a category where 12 of 16 prior entries had no MCP server at all and the ones that did were paid. That makes Buffer the natural bench-test candidate for this file. Rate limits are the thing to watch rather than the price: the guide states MCP calls "count against the same rate limits as any other client", on rolling 15-minute, 24-hour and 30-day windows, per client and shared across every request rather than counted per tool, so one chatty conversation that lists posts, reads several and edits one can spend a noticeable share of a free monthly allowance. Write access is in scope (schedule and edit posts), so an agent connected here can publish to real audiences. 2026-09-07: https://mcp.buffer.com/mcp returned 401 to an MCP initialize POST (https://mcp.buffer.com/mcp).

**Provenance**

- **Entry id**: 15-buffer

- **Source file**: 15-community-dark-social.md

- **Source line**: 311

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
