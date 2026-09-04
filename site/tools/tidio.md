# Tidio: MCP server status, API access gate and what it does

> Customer-service platform combining live chat, a help desk, and an AI agent ("Lyro") that resolves routine... Official MCP, Free to start. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Tidio

# Tidio

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [tidio.com](https://tidio.com) · entry id 14-tidio · source 14-inbound-plg-chat.md line 237

**What it does**
Customer-service platform combining live chat, a help desk, and an AI agent ("Lyro") that resolves routine support/sales questions automatically.

**AI features, separated from automation with an AI label on it**
Lyro AI Agent is marketed to resolve "up to 90%" of low-level questions with an "80% resolution rate across 10,000 chats a month," answering in the brand's voice with context awareness - vendor-stated figures, not independently verified.

**RevOps role**
Widely deployed (300,000+ businesses per vendor) SMB-friendly inbound chat/support layer.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth: the tidio_connect tool opens a browser to Tidio's login page, then stores access and refresh tokens locally in ~/.tidio-mcp/credentials.json.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/TidioPoland/tidio-mcp-connector](https://github.com/TidioPoland/tidio-mcp-connector)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/TidioPoland/tidio-mcp-connector (https://tid.io/mcp 301-redirects here)

- [https://github.com/TidioPoland/tidio-mcp-connector](https://github.com/TidioPoland/tidio-mcp-connector)
- [https://tid.io/mcp](https://tid.io/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited). Self-serve, no-card-required free tier exists; a "Premium Plan" and enterprise options are directed to sales for pricing.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/TidioPoland/tidio-mcp-connector](https://github.com/TidioPoland/tidio-mcp-connector)

**Jobs it can do**

- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.tidio.com](https://www.tidio.com)
- [https://github.com/TidioPoland/tidio-mcp-connector](https://github.com/TidioPoland/tidio-mcp-connector)
- [https://tid.io/mcp](https://tid.io/mcp)
- [https://www.tidio.com/ai-agent/build-and-integrate/](https://www.tidio.com/ai-agent/build-and-integrate/)

4 source URLs. Raw sources field, verbatim:

https://www.tidio.com, https://github.com/TidioPoland/tidio-mcp-connector, https://tid.io/mcp, https://www.tidio.com/ai-agent/build-and-integrate/

**Notes, verbatim from the file**
Tidio's own marketing copy lists "REST APIs, webhooks, JS actions, or Model Context Protocol (MCP)" as supported integration methods, but no dedicated MCP docs page, repo, or listing could be located on tidio.com, PulseMCP, mcp.so, or glama.ai during this research pass - per this directory's law that an MCP claim requires a URL in hand, this is logged as none-found rather than official/community despite the vendor's own claim. Re-check before the next pass. 2026-09-02: mcp_status none-found -> official, narrowly. Tidio's short domain https://tid.io/mcp 301-redirects to github.com/TidioPoland/tidio-mcp-connector, a repo under the TidioPoland GitHub organisation (whose profile links tidio.com), and mcpservers.org lists it with an official badge. It is a small setup connector: three tools (tidio_connect, tidio_status, tidio_disconnect) plus embed-code generation so an AI assistant or Lovable can wire Tidio onto a site; it does not expose conversations, contacts or Lyro data. Separately, https://www.tidio.com/ai-agent/build-and-integrate/ describes Lyro consuming MCP servers (Shopify, Guru, Stripe), which makes Lyro an MCP client. The community server github.com/adrmrn/tidio-mcp wraps the Tidio REST API. The "no dedicated MCP docs page, repo, or listing" sentence above is superseded.

**Provenance**

- **Entry id**: 14-tidio

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 237

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
