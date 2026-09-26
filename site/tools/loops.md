# Loops: MCP server status, API access gate and what it does

> Loops is email marketing software for SaaS teams to send marketing, lifecycle, and transactional email from... No MCP found, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Loops

# Loops

[No MCP found](../mcp/none-found.md)
[Gate unknown](../gates/unknown.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-12
CLI: loops

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [loops.so](https://loops.so) · entry id 02-loops · source 02-engagement-outbound.md line 1957

**What it does**
Loops is email marketing software for SaaS teams to send marketing, lifecycle, and transactional email from one product. Free to start.

**AI features, separated from automation with an AI label on it**
Not evidenced from fetched pages this pass; no AI feature claims recorded without a source URL.

**RevOps role**
Outbound engagement, sequencing, or messaging layer used by sales teams

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: not recorded

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-12.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 417 of 1252 entries are.

**Command line**

- **Binary**: loops
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-26

Install, as the source shows it:

```
brew install loops-so/tap/loops
```

quoted from [https://loops.so/docs/cli](https://loops.so/docs/cli) on 2026-09-26, via brew

```
curl -fsSL https://install.loops.so/cli | sh
```

quoted from [https://loops.so/docs/cli](https://loops.so/docs/cli) on 2026-09-26, via shell

```
curl -fsSL https://install.loops.so/wizard | sh
```

quoted from [https://loops.so/docs/cli](https://loops.so/docs/cli) on 2026-09-26, via shell

```
go install github.com/loops-so/cli/cmd/loops@latest
```

quoted from [https://loops.so/docs/cli](https://loops.so/docs/cli) on 2026-09-26, via go

Login or key hint seen on the page:

loops auth

Subcommands seen with the binary:

agent-context, api-key, auth, dedicated-sending-ips, skill

Where it was documented:

- [https://loops.so/docs/cli](https://loops.so/docs/cli) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-26.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

[https://loops.so/docs](https://loops.so/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to loops.so with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://loops.so](https://loops.so)
- [https://loops.so/docs](https://loops.so/docs)
- [https://yc-oss.github.io/api/industries/marketing.json](https://yc-oss.github.io/api/industries/marketing.json)

3 source URLs. Raw sources field, verbatim:

https://loops.so, https://loops.so/docs, https://yc-oss.github.io/api/industries/marketing.json

**Notes, verbatim from the file**
mcp_status none-found with dated probe 2026-09-12; no first-party MCP URL confirmed from fetched pages. No official MCP invented. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Category corrected from data-enrichment to engagement-outbound.

**Provenance**

- **Entry id**: 02-loops

- **Source file**: 02-engagement-outbound.md

- **Source line**: 1957

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-26

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
