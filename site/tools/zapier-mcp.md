# Zapier MCP: MCP server status, API access gate and what it does

> Zapier's own MCP endpoint, letting Claude, ChatGPT, Cursor, and other MCP clients trigger the same 9,000+ app... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Zapier MCP

# Zapier MCP

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [zapier.com/mcp](https://zapier.com/mcp) · entry id 07-zapier-mcp · source 07-mcp-infrastructure.md line 54

**What it does**
Zapier's own MCP endpoint, letting Claude, ChatGPT, Cursor, and other MCP clients trigger the same 9,000+ app actions Zapier already exposes to its classic trigger-action Zaps.

**AI features, separated from automation with an AI label on it**
none in the MCP layer itself - it reuses Zapier's existing (non-AI) action library. Zapier's separate "Zapier Agents" product is where genuine LLM-driven autonomous behavior lives; MCP is a new door into the same rules-based action catalog.

**RevOps role**
The broadest reach-into-anything connector for a RevOps stack already standardized on Zapier - claims 9,000+ connectable apps including Salesforce, HubSpot, Gmail, and Slack.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Uses Zapier's existing decade-old app-connection/OAuth infrastructure - you authorize apps the same way you would for a normal Zap, then expose selected actions to the MCP client.

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.zapier.com/login?redirectTo=%2Fmcp (redirect correction 2026-08-28: the bare address previously recorded here, mcp.zapier.com, 307s to /mcp and then to this signed-in console URL, which returns 200. It is an auth wall, not documentation; the public documentation for the same server is https://zapier.com/mcp)

- [https://mcp.zapier.com/login?redirectTo=%2Fmcp](https://mcp.zapier.com/login?redirectTo=%2Fmcp)
- [https://zapier.com/mcp](https://zapier.com/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (bundled into existing Zapier plans; each MCP tool call consumes 2 tasks from the account's standard task quota - no separate SKU)

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

- [https://zapier.com/mcp](https://zapier.com/mcp)
- [https://mcp.zapier.com/login?redirectTo=%2Fmcp](https://mcp.zapier.com/login?redirectTo=%2Fmcp)

2 source URLs. Raw sources field, verbatim:

https://zapier.com/mcp, https://mcp.zapier.com/login?redirectTo=%2Fmcp

**Notes, verbatim from the file**
Because MCP calls draw from the same task pool as regular Zaps, a chatty agent can burn a plan's task quota fast - worth watching before pointing a high-frequency agent at it.

**Provenance**

- **Entry id**: 07-zapier-mcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 54

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
