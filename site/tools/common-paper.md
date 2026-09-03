# Common Paper: MCP server status, API access gate and what it does

> Contract system built for startups - standardized, mutually-agreeable contract templates (MSAs, DPAs, order... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
Common Paper

# Common Paper

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [commonpaper.com](https://commonpaper.com) · entry id 13-common-paper · source 13-proposals-deals.md line 185

**What it does**
Contract system built for startups - standardized, mutually-agreeable contract templates (MSAs, DPAs, order forms) plus a workflow/e-signature layer, positioned as a faster, less lawyer-heavy alternative to a full CLM for early-stage companies.

**AI features, separated from automation with an AI label on it**
MCP integration is framed as bringing "contract intelligence" into AI tools (query agreements, analyze contract terms, generate insights) - a genuine data-access/analysis layer over real contract data; underlying AI methodology not independently verified beyond that framing.

**RevOps role**
Lightweight, standardized contracting layer aimed at startups closing deals faster without a full legal-ops build-out - the closest thing in this file to a solo-operator-friendly CLM.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - not detailed in the release-notes excerpt reviewed.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/](https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/)Probed**: 2026-08-25, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-08-25 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/ ; REST API docs at https://api.commonpaper.com/docs

- [https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/](https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/)
- [https://api.commonpaper.com/docs](https://api.commonpaper.com/docs)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited) to paid. Pricing tiers found: a Free tier, a $50/user/month standard tier, and a $100/user/month premium tier, with the API and notification webhooks described as available across plans (exact per-tier API scope not itemized).

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Send a document for signature](../jobs/send-document-for-signature.md)
- [Read contract terms](../jobs/read-contract-terms.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/](https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/)
- [https://commonpaper.com/pricing/](https://commonpaper.com/pricing/)
- [https://api.commonpaper.com/docs](https://api.commonpaper.com/docs)

3 source URLs. Raw sources field, verbatim:

https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/, https://commonpaper.com/pricing/, https://api.commonpaper.com/docs

**Notes, verbatim from the file**
The main commonpaper.com homepage returned an HTTP 403 to automated fetching during this research; facts above are drawn from search-indexed pricing and release-notes pages instead of a direct homepage read - worth a manual re-check.

**Provenance**

- **Entry id**: 13-common-paper

- **Source file**: 13-proposals-deals.md

- **Source line**: 185

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
