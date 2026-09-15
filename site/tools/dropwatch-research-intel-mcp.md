# Dropwatch Research Intel MCP: MCP server status, API access gate and what it does

> Research GTM triggers: new NIH grants by PI/institution and new clinical trials by sponsor/phase. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Dropwatch Research Intel MCP

# Dropwatch Research Intel MCP

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-12

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://research.dropwatchhq.com/mcp](https://research.dropwatchhq.com/mcp) · entry id 05-dropwatch-research-intel-mcp · source 05-signals-intent-abm.md line 1660

**What it does**
Research GTM triggers: new NIH grants by PI/institution and new clinical trials by sponsor/phase.

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

https://research.dropwatchhq.com/mcp

- [https://research.dropwatchhq.com/mcp](https://research.dropwatchhq.com/mcp)

**What this server exposes**

- **Tools named**: 5
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-15
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **delta_digest** New grants + new trials in a filter over the last N days (the weekly-digest payload). Best for BD teams. evidence: answered tools/list · calling it reads

- **entity_watch** Recent funding/trial events for one institution, PI, sponsor, or topic. Use to enrich an account or check a competitor. evidence: answered tools/list · calling it reads · required: type, value

- **new_funding** THE GTM-trigger tool. Return the newest NIH grants and newly-registered clinical trials in a territory - the highest-intent buying signal in life-sciences sales (a newly-funded lab has budget and is choosing vendors now). Filter by... evidence: answered tools/list · calling it reads

- **search_records** Ad-hoc search/enrichment over snapshotted grants + trials by any filter (keyword, sponsorClass, topic, $ range). evidence: answered tools/list · calling it reads

- **whats_changed_since** Return grants/trials that are NEW or MODIFIED since a cursor token (cursor = your bookmark / CRM-sync point). Pass the cursor from a prior call to get only changes since then. Same filters as new_funding. evidence: answered tools/list · calling it reads

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

[https://research.dropwatchhq.com/docs](https://research.dropwatchhq.com/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to research.dropwatchhq.com with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://research.dropwatchhq.com/mcp](https://research.dropwatchhq.com/mcp)
- [https://research.dropwatchhq.com/docs](https://research.dropwatchhq.com/docs)
- [https://research.dropwatchhq.com/developers](https://research.dropwatchhq.com/developers)

3 source URLs. Raw sources field, verbatim:

https://research.dropwatchhq.com/mcp, https://research.dropwatchhq.com/docs, https://research.dropwatchhq.com/developers

**Notes, verbatim from the file**
what_it_does used staging desc because homepage meta description was empty. API mentioned on https://research.dropwatchhq.com/docs; pricing/gate not inferred from presence alone. API mentioned on https://research.dropwatchhq.com/developers; pricing/gate not inferred from presence alone. mcp_status=community from official-mcp-registry listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave P 2026-09-12: canonical name Dropwatch Research Intel MCP (draft listed as com.dropwatchhq/research-intel).

**Provenance**

- **Entry id**: 05-dropwatch-research-intel-mcp

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 1660

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-15

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
