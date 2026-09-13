# FavCRM: MCP server status, API access gate and what it does

> FavCRM 是為香港服務業而設的 CRM：預約系統、會員系統、客戶管理、WhatsApp 跟進與收款放喺同一處。AI 幫你整理同草擬，重要動作由你審批。 Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
FavCRM

# FavCRM

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-12

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [favcrm.io](https://favcrm.io) · entry id 07-favcrm · source 07-mcp-infrastructure.md line 1301

**What it does**
FavCRM 是為香港服務業而設的 CRM：預約系統、會員系統、客戶管理、WhatsApp 跟進與收款放喺同一處。AI 幫你整理同草擬，重要動作由你審批。

**AI features, separated from automation with an AI label on it**
Homepage copy mentions AI/ML-related terms; specific AI feature list not independently verified beyond that mention this pass. See sources.

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

https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm

- [https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 521 entries that record an official or community MCP server carry a harvested tool list. The other 402 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

The CLI layer has not been measured on this build.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

729 of 1032 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

635 of 1032 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

The GitHub organisation layer has not been measured on this build.

**Jobs it can do**

No job tag on this entry.

761 of 1,032 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://favcrm.io/zh-hk/](https://favcrm.io/zh-hk/)
- [https://favcrm.io/llms.txt](https://favcrm.io/llms.txt)
- [https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm)

3 source URLs. Raw sources field, verbatim:

https://favcrm.io/zh-hk/, https://favcrm.io/llms.txt, https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm

**Notes, verbatim from the file**
API mentioned on https://favcrm.io/llms.txt; pricing/gate not inferred from presence alone. mcp_status=community from smithery listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave E 2026-09-12: canonical name FavCRM (draft listed as FavCRM - Agentic CRM).

**Provenance**

- **Entry id**: 07-favcrm

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 1301

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
