# 6sense: MCP server status, API access gate and what it does

> Detects B2B buying intent by combining IP-based website deanonymization, a proprietary third-party... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
6sense

# 6sense

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://6sense.com](https://6sense.com) · entry id 05-6sense · source 05-signals-intent-abm.md line 14

**What it does**
Detects B2B buying intent by combining IP-based website deanonymization, a proprietary third-party intent/content-consumption network ("Signalverse"), and first-party CRM/MAP/product data to flag in-market accounts and identify individual buyers researching a purchase.

**AI features, separated from automation with an AI label on it**
The core account/buying-stage scoring is a proprietary ML model trained on ~13 years of behavioral data - a genuine ML claim. "RevvyAI" is an LLM chat layer for querying already-computed scores, not a new signal source; treat it as an interface, not discovery.

**RevOps role**
Top-of-funnel account prioritization and predictive scoring engine feeding CRM/MAP and ad platforms.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth using existing 6sense platform login (no separate API key setup per vendor docs)

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://6sense.com/platform/mcp-server/ ; https://support.6sense.com/docs/6sense-model-context-protocol-mcp-1

- [https://6sense.com/platform/mcp-server/](https://6sense.com/platform/mcp-server/)
- [https://support.6sense.com/docs/6sense-model-context-protocol-mcp-1](https://support.6sense.com/docs/6sense-model-context-protocol-mcp-1)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

120 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 105 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-11 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/6si](https://github.com/6si) tied to the vendor by rule 3, account website https://6sense.com has the vendor's domain, confidence strong

- **Public repositories**: 7, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2024-10-11

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [rules_cloud_files](https://github.com/6si/rules_cloud_files) | other | | 1 | 2024-10-11 | v1.0.0 |
| [rules_wheel](https://github.com/6si/rules_wheel) | other | | 0 | 2024-08-08 | v0.2.1 |
| [changed-files](https://github.com/6si/changed-files) | other | Mirror of tj-actions/changed-files | 0 | 2023-09-04 | v19 |
| [shipwright](https://github.com/6si/shipwright) | infrastructure | Shipwright / The right way to build, tag and ship Docker containers. | 117 | 2023-04-15 | |
| [docker-utf8](https://github.com/6si/docker-utf8) | infrastructure | Ubuntu en_US.UTF-8 to workaround the fact CircleCI can't run locale-gen under docker | 0 | 2014-11-09 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Build a target account list](../jobs/build-target-account-list.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://6sense.com/platform/mcp-server/](https://6sense.com/platform/mcp-server/)
- [https://support.6sense.com/docs/6sense-model-context-protocol-mcp-1](https://support.6sense.com/docs/6sense-model-context-protocol-mcp-1)
- [https://6sense.com/blog/apis-and-mcp/](https://6sense.com/blog/apis-and-mcp/)
- [https://6sense.com/newsroom/6sense-launches-mcp-server-bringing-proprietary-gtm-intelligence-into-any-ai-agent/](https://6sense.com/newsroom/6sense-launches-mcp-server-bringing-proprietary-gtm-intelligence-into-any-ai-agent/)
- [https://support.6sense.com/docs/api-credits-api-tokens](https://support.6sense.com/docs/api-credits-api-tokens)

5 source URLs. Raw sources field, verbatim:

https://6sense.com/platform/mcp-server/, https://support.6sense.com/docs/6sense-model-context-protocol-mcp-1, https://6sense.com/blog/apis-and-mcp/, https://6sense.com/newsroom/6sense-launches-mcp-server-bringing-proprietary-gtm-intelligence-into-any-ai-agent/, https://support.6sense.com/docs/api-credits-api-tokens

**Notes, verbatim from the file**
MCP launched in open beta ~July 2026. No published pricing or self-serve signup found - homepage offers "Book a Demo" only. API credit pools (Company ID, Enrichment) are purchased separately from platform seats through a CSM.

**Provenance**

- **Entry id**: 05-6sense

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 14

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
