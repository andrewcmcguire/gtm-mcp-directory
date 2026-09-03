# Model Context Protocol - official servers repo: MCP server status, API access gate and what it does

> The official reference-implementation repository for MCP, "managed by Anthropic, but built together with the... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Model Context Protocol - official servers repo

# Model Context Protocol - official servers repo

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) · entry id 07-model-context-protocol-official-servers-repo · source 07-mcp-infrastructure.md line 178

**What it does**
The official reference-implementation repository for MCP, "managed by Anthropic, but built together with the community" - ships a small set of maintained example servers (Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time) intended as educational references, not production integrations.

**AI features, separated from automation with an AI label on it**
none - reference server code, not an AI product.

**RevOps role**
Not a GTM connector layer directly - the major third-party integration servers (GitHub, Slack, Google Drive, etc.) that once lived here have been archived out to a separate, community/externally-maintained repo. Relevant mainly as the canonical spec reference, not a place to find Salesforce/HubSpot servers.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Per-server - individual servers take credentials (e.g. API tokens) via environment variables or CLI args where needed; the repo itself has no central auth layer.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL[https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)Probed**: 2026-09-03, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/modelcontextprotocol/servers

- [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (open source; dual-licensed Apache 2.0 for new contributions, MIT for existing code)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: no-job-fits. The official reference-servers repo. It is the spec's canonical reference, not a registry an agent queries and not a SaaS proxy.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 14 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://github.com/modelcontextprotocol/servers

**Notes, verbatim from the file**
Worth flagging plainly for anyone assuming this repo is a live GTM connector catalog - it isn't anymore. The maintained set is down to seven small reference servers; real-world integrations have moved to community repos or vendor-hosted official servers (Salesforce, HubSpot, Attio, etc. - see 06-revops-infra.md).

**Provenance**

- **Entry id**: 07-model-context-protocol-official-servers-repo

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 178

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
