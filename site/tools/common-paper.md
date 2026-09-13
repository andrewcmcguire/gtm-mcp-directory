# Common Paper: MCP server status, API access gate and what it does

> Contract system built for startups - standardized, mutually-agreeable contract templates (MSAs, DPAs, order... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
Common Paper

# Common Paper

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/](https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.commonpaper.com/mcp ; https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/ ; REST API docs at https://api.commonpaper.com/docs

- [https://api.commonpaper.com/mcp](https://api.commonpaper.com/mcp)
- [https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/](https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/)
- [https://api.commonpaper.com/docs](https://api.commonpaper.com/docs)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited) to paid. Pricing tiers found: a Free tier, a $50/user/month standard tier, and a $100/user/month premium tier, with the API and notification webhooks described as available across plans (exact per-tier API scope not itemized).

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/CommonPaper](https://github.com/CommonPaper) tied to the vendor by rule 3, account website https://commonpaper.com has the vendor's domain, confidence strong

- **Public repositories**: 14, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-05

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [claude-skill](https://github.com/CommonPaper/claude-skill) | other | Official Common Paper skill for Claude and other agents | 7 | 2026-09-05 | |
| [Design-Partner-Agreement](https://github.com/CommonPaper/Design-Partner-Agreement) | other | Common Paper standard Design Partner Agreement | 23 | 2026-08-04 | 1.3 |
| [AI-Addendum](https://github.com/CommonPaper/AI-Addendum) | other | Common Paper Standard AI Addendum | 3 | 2025-08-07 | 1.0 |
| [Pilot-Agreement](https://github.com/CommonPaper/Pilot-Agreement) | other | Common Paper standard Pilot Agreement | 3 | 2025-07-22 | 1.1 |
| [PSA](https://github.com/CommonPaper/PSA) | other | Common Paper standard Professional Services Agreement | 14 | 2025-05-23 | 1.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Send a document for signature](../jobs/send-document-for-signature.md)
- [Read contract terms](../jobs/read-contract-terms.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 559 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/](https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/)
- [https://commonpaper.com/pricing/](https://commonpaper.com/pricing/)
- [https://api.commonpaper.com/docs](https://api.commonpaper.com/docs)
- [https://api.commonpaper.com/mcp](https://api.commonpaper.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://commonpaper.com/release-notes/common-paper-mcp-model-context-protocol-integration/, https://commonpaper.com/pricing/, https://api.commonpaper.com/docs, https://api.commonpaper.com/mcp

**Notes, verbatim from the file**
The main commonpaper.com homepage returned an HTTP 403 to automated fetching during this research; facts above are drawn from search-indexed pricing and release-notes pages instead of a direct homepage read - worth a manual re-check. 2026-09-07: https://api.commonpaper.com/mcp returned 401 "Bearer token required" while the control path https://api.commonpaper.com/zzznotamcp returned a 404 problem-JSON, so /mcp is a real registered route on the vendor API, not a blanket auth wall (https://api.commonpaper.com/mcp).

**Provenance**

- **Entry id**: 13-common-paper

- **Source file**: 13-proposals-deals.md

- **Source line**: 185

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
