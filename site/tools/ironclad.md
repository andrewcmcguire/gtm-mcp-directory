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
- **Probed**: 2026-09-03, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server ; also referenced at https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md

- [https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server](https://support.ironcladapp.com/hc/en-us/articles/39887091143319-Ironclad-MCP-Server)
- [https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md](https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only. Ironclad has no published list pricing; typical mid-market/enterprise deployments run $50K-$200K+/yr per third-party trackers, with AI Assist as a separate $50,000-$200,000/yr add-on. Public API access requires an enterprise contract and an account rep - not self-serve at any tier.

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md](https://github.com/ever-works/awesome-mcp-servers/blob/master/details/ironclad-mcp-server.md)

**Jobs it can do**

- [Read contract terms](../jobs/read-contract-terms.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
