# GTM Tools MCP: MCP server status, API access gate and what it does

> A read-only verified record of agent-operable GTM tools: search, fetch, compare, track changes. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
GTM Tools MCP

# GTM Tools MCP

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-12

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://gcwmjfotygqnlsyfhiyq.supabase.co/functions/v1/mcp](https://gcwmjfotygqnlsyfhiyq.supabase.co/functions/v1/mcp) · entry id 07-gtm-tools-mcp · source 07-mcp-infrastructure.md line 4624

**What it does**
A read-only verified record of agent-operable GTM tools: search, fetch, compare, track changes.

**AI features, separated from automation with an AI label on it**
Not evidenced from fetched pages this pass; no AI feature claims recorded without a source URL.

**RevOps role**
MCP server/client or agent-tooling infrastructure

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://gcwmjfotygqnlsyfhiyq.supabase.co/functions/v1/mcp

- [https://gcwmjfotygqnlsyfhiyq.supabase.co/functions/v1/mcp](https://gcwmjfotygqnlsyfhiyq.supabase.co/functions/v1/mcp)

**What this server exposes**

- **Tools named**: 4
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-15
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **compare_tools** Compare two GTM tools head-to-head. Returns both full records plus a per-axis diff (overall score, API quality, GTM relevance, curation score, ease of use, free tier) naming the winning slug or 'tie'. evidence: answered tools/list · calling it reads · required: a, b

- **get_tool** Get one GTM tool by name or slug, with verified status (real last_checked_at), curation, product signals, adoption, and verified review themes. evidence: answered tools/list · calling it reads · required: name_or_slug

- **list_changes** Recent detected changes to tracked tools (pricing, reachability, free-tier, deprecation), newest first. Optionally filter by kind. evidence: answered tools/list · calling it reads

- **search_tools** Search the verified GTM-tools directory. Filter by keyword, category, tier (BADGE|listed|DEMOTE), verifiedOnly, or mcpOnly; sort by score (default), name, or g2. Returns ranked slim results. Use category + sort=score for 'best in category'. evidence: answered tools/list · calling it reads

138 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 603 are unmeasured, which is not the same as empty. Harvest last run 2026-09-15. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-15 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

727 of 1252 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to gcwmjfotygqnlsyfhiyq.supabase.co with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://gcwmjfotygqnlsyfhiyq.supabase.co/functions/v1/mcp](https://gcwmjfotygqnlsyfhiyq.supabase.co/functions/v1/mcp)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 100 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://gcwmjfotygqnlsyfhiyq.supabase.co/functions/v1/mcp

**Notes, verbatim from the file**
what_it_does used staging desc because homepage meta description was empty. mcp_status=community from official-mcp-registry listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave Q 2026-09-12: canonical name GTM Tools MCP (draft listed as dev.gtmtools/gtm-tools).

**Provenance**

- **Entry id**: 07-gtm-tools-mcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 4624

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-15

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
