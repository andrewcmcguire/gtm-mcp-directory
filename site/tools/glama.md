# Glama (MCP directory): MCP server status, API access gate and what it does

> A large searchable registry/catalog of open-source MCP servers (77,000+ listed as of this check), filterable... MCP not applicable, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Glama (MCP directory)

# Glama (MCP directory)

[MCP not applicable](../mcp/n-a.md)
[Gate unknown](../gates/unknown.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [glama.ai](https://glama.ai) · entry id 07-glama · source 07-mcp-infrastructure.md line 116

**What it does**
A large searchable registry/catalog of open-source MCP servers (77,000+ listed as of this check), filterable by language, hosting type (remote/local/hybrid), capability, and category; also offers separate hosting services.

**AI features, separated from automation with an AI label on it**
none - a catalog/search layer, not an AI product.

**RevOps role**
Useful as a discovery/search tool for finding a self-hosted or community MCP server for a niche need; mainstream GTM/CRM platforms (Salesforce, HubSpot, Slack, Gmail) were not prominently featured in what was surfaced - the catalog skews toward databases, dev tools, and self-hosted/local-first servers.

**MCP server**

- **Status bucket**: MCP not applicable

- **Auth**: Varies per listed server; Glama promotes several "no API key required" servers but does not itself broker auth for the catalog as a whole the way Smithery's agent.pw does.

- **Parsed URLs**: 1 found in the mcp_url field

An MCP server is not a meaningful question for this entry. The status was established on 2026-08-24.

mcp_status, verbatim from the file:

n/a (Glama is the directory itself)

mcp_url, verbatim from the file:

https://glama.ai/mcp/servers

- [https://glama.ai/mcp/servers](https://glama.ai/mcp/servers)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown (pricing page referenced but not disclosed in the fetched content)

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Discover MCP servers](../jobs/discover-mcp-servers.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://glama.ai/mcp/servers](https://glama.ai/mcp/servers)
- [https://glama.ai/api/mcp/openapi.json](https://glama.ai/api/mcp/openapi.json)

2 source URLs. Raw sources field, verbatim:

https://glama.ai/mcp/servers, https://glama.ai/api/mcp/openapi.json

**Notes, verbatim from the file**
Glama's emphasis on local-first/self-hosted servers makes it a better fit for privacy-conscious infra teams than for someone looking for one-click hosted GTM connectors. [api_gate 2026-08-25] Re-checked and left unknown, honestly: plans are cheap and self-serve (free for open-source MCP servers, then $9/mo Starter, $26/mo Pro, $80/mo Business) and a REST directory API exists whose OpenAPI spec requires bearerAuth on every endpoint, but no loadable Glama page states which plan issues that token; the API reference page is client-rendered and returns nothing to a plain fetch. Checked against https://glama.ai/api/mcp/openapi.json.

**Provenance**

- **Entry id**: 07-glama

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 116

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
