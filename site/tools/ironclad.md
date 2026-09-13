# Ironclad: MCP server status, API access gate and what it does

> Contract lifecycle management (CLM) platform for drafting, negotiating, and managing contracts with workflow... Official MCP, Enterprise only. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
Ironclad

# Ironclad

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [ironcladapp.com](https://ironcladapp.com) · entry id 13-ironclad · source 13-proposals-deals.md line 166

**What it does**
Contract lifecycle management (CLM) platform for drafting, negotiating, and managing contracts with workflow automation across legal, sales, and procurement teams - sales-adjacent rather than a sales tool proper.

**AI features, separated from automation with an AI label on it**
"AI Assist" is marketed as a distinct paid add-on for contract analysis/drafting assistance; specific model/methodology details not independently verified.

**RevOps role**
Legal-ops-owned CLM system that GTM engineers touch mainly for contract-velocity/cycle-time visibility, not a sales tool a solo operator would independently purchase.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - a single, static MCP endpoint per the support article; specific credential mechanism not detailed in the sources reviewed.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server ; also referenced at https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md

- [https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server)
- [https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md](https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-13. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-13 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only. Ironclad has no published list pricing; typical mid-market/enterprise deployments run $50K-$200K+/yr per third-party trackers, with AI Assist as a separate $50,000-$200,000/yr add-on. Public API access requires an enterprise contract and an account rep - not self-serve at any tier.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md](https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md)

**On GitHub**

[github.com/Ironclad](https://github.com/Ironclad) tied to the vendor by rule 3, account website ironcladapp.com has the vendor's domain, confidence strong

- **Public repositories**: 4, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-26

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [rivet](https://github.com/Ironclad/rivet) | other | The open-source visual AI programming environment and TypeScript library | 4,688 | 2026-08-26 | app-v1.11.3 |
| [openapi](https://github.com/Ironclad/openapi) | docs or examples | This repository is deprecated. The most up-to-date version of the Ironclad public API OpenAPI specifications can be... | 6 | 2025-10-20 | |
| [rivet-example](https://github.com/Ironclad/rivet-example) | docs or examples | | 87 | 2024-03-26 | |
| [ea-servicenow-guide](https://github.com/Ironclad/ea-servicenow-guide) | other | ServiceNow assets for EA solution guide | 1 | 2023-02-15 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Read contract terms](../jobs/read-contract-terms.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server)
- [https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md](https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md)
- [https://www.vaquill.ai/blog/ironclad-pricing](https://www.vaquill.ai/blog/ironclad-pricing)
- [https://ironcladapp.com/pricing](https://ironcladapp.com/pricing)

4 source URLs. Raw sources field, verbatim:

https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server, https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md, https://www.vaquill.ai/blog/ironclad-pricing, https://ironcladapp.com/pricing

**Notes, verbatim from the file**
Included per the seed list's "sales-adjacent" framing - Ironclad is legal-ops-first, but its MCP server and contract-velocity data are genuinely relevant to a GTM engineer tracking deal-to-close friction.

**Provenance**

- **Entry id**: 13-ironclad

- **Source file**: 13-proposals-deals.md

- **Source line**: 166

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-13

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
