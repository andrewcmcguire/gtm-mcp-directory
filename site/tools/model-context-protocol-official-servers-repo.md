# Model Context Protocol - official servers repo: MCP server status, API access gate and what it does

> The official reference-implementation repository for MCP, "managed by Anthropic, but built together with the... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

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

Vendor: [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) · entry id 07-model-context-protocol-official-servers-repo · source 07-mcp-infrastructure.md line 183

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
- **Docs URL**: [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/modelcontextprotocol/servers

- [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

**What this server exposes**

- **Tools named**: 24
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-11
- **Repo read**: modelcontextprotocol/servers
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **add_observations** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_directory** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_entities** No description was recorded with the name. evidence: in the server source · calling it reads

- **create_relations** No description was recorded with the name. evidence: in the server source · calling it reads

- **delete_entities** No description was recorded with the name. evidence: in the server source · calling it reads

- **delete_observations** No description was recorded with the name. evidence: in the server source · calling it reads

- **delete_relations** No description was recorded with the name. evidence: in the server source · calling it reads

- **directory_tree** No description was recorded with the name. evidence: in the server source · calling it reads

- **edit_file** No description was recorded with the name. evidence: in the server source · calling it reads

- **get_file_info** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_allowed_directories** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_directory** No description was recorded with the name. evidence: in the server source · calling it reads

- **list_directory_with_sizes** No description was recorded with the name. evidence: in the server source · calling it reads

- **move_file** No description was recorded with the name. evidence: in the server source · calling it reads

- **open_nodes** No description was recorded with the name. evidence: in the server source · calling it reads

- **read_file** No description was recorded with the name. evidence: in the server source · calling it reads

- **read_graph** No description was recorded with the name. evidence: in the server source · calling it reads

- **read_media_file** No description was recorded with the name. evidence: in the server source · calling it reads

- **read_multiple_files** No description was recorded with the name. evidence: in the server source · calling it reads

- **read_text_file** No description was recorded with the name. evidence: in the server source · calling it reads

- **search_files** No description was recorded with the name. evidence: in the server source · calling it reads

- **search_nodes** No description was recorded with the name. evidence: in the server source · calling it reads

- **sequentialthinking** No description was recorded with the name. evidence: in the server source · calling it reads

- **write_file** No description was recorded with the name. evidence: in the server source · calling it reads

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (open source; dual-licensed Apache 2.0 for new contributions, MIT for existing code)

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

**On GitHub**

[github.com/modelcontextprotocol](https://github.com/modelcontextprotocol) tied to the vendor by rule 1, the directory already classed this repo first-party and its owner is an Organization, confidence strong

- **Public repositories**: 42, forks excluded, as read on 2026-09-08
- **Mention MCP**: 35 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk) | MCP server | The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft. | 4,521 | 2026-09-08 | v2.2.0 |
| [ext-apps](https://github.com/modelcontextprotocol/ext-apps) | SDK | Official repo for spec & SDK of MCP Apps protocol - standard for UIs embedded AI chatbots, served by MCP servers | 2,804 | 2026-09-08 | v1.7.5 |
| [rust-sdk](https://github.com/modelcontextprotocol/rust-sdk) | MCP server | The official Rust SDK for the Model Context Protocol | 3,897 | 2026-09-08 | rmcp-v3.2.0 |
| [kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk) | MCP server | The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains | 1,450 | 2026-09-08 | 0.15.0 |
| [java-sdk](https://github.com/modelcontextprotocol/java-sdk) | MCP server | The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI | 3,685 | 2026-09-08 | v2.0.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: no-job-fits. The official reference-servers repo. It is the spec's canonical reference, not a registry an agent queries and not a SaaS proxy.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 13 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://github.com/modelcontextprotocol/servers

**Notes, verbatim from the file**
Worth flagging plainly for anyone assuming this repo is a live GTM connector catalog - it isn't anymore. The maintained set is down to seven small reference servers; real-world integrations have moved to community repos or vendor-hosted official servers (Salesforce, HubSpot, Attio, etc. - see 06-revops-infra.md).

**Provenance**

- **Entry id**: 07-model-context-protocol-official-servers-repo

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 183

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
