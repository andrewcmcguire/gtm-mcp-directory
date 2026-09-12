# SigParser: MCP server status, API access gate and what it does

> A relationship-intelligence and contact-capture product that scans connected mailboxes, calendars and address... Official MCP, Enterprise leaning. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
SigParser

# SigParser

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [sigparser.com](https://sigparser.com) · entry id 01-sigparser · source 01-data-enrichment.md line 834

**What it does**
A relationship-intelligence and contact-capture product that scans connected mailboxes, calendars and address books, parses email signatures, and turns the result into contact and company records with who-knows-who relationship scores, exportable to a CRM, a spreadsheet or a data warehouse.

**AI features, separated from automation with an AI label on it**
Genuine and narrow: the vendor states custom AI models extract structured fields (full name, title, location, phone number, LinkedIn profile) from free-text email signatures. The rest is deterministic scanning, deduplication and relationship scoring.

**RevOps role**
Turns a company's own email and calendar history into a first-party contact graph, which is a different supply than any purchased database in this file; used for warm-intro discovery, CRM hygiene and relationship handover when a rep leaves.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown. The endpoint answers HTTP 401 to an unauthenticated MCP initialize but no first-party page documents the scheme; SigParser's REST API, served from the same ipaas.sigparser.com host, uses an API key.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official (endpoint-only; no vendor MCP documentation page found)

mcp_url, verbatim from the file:

https://ipaas.sigparser.com/api/mcp

- [https://ipaas.sigparser.com/api/mcp](https://ipaas.sigparser.com/api/mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 106 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning - the vendor's pricing page lists "Access API Endpoints" only under the Enterprise tier, prices that tier at $499 per month billed annually, and gives it a "Schedule a Demo" button, while the three tiers below it (Individual $19, Team $49, Professional $299) carry "Start Free Trial". A price is published, but the only tier that carries the API is the one routed through sales.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/DragnetTech](https://github.com/DragnetTech) tied to the vendor by rule 3, account website https://sigparser.com has the vendor's domain, confidence strong

- **Public repositories**: 2, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2023-02-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [ApiDataFetcher](https://github.com/DragnetTech/ApiDataFetcher) | CLI | Fetch data from the SigParser APIs with this CLI tool. | 0 | 2023-02-08 | v1.1.10 |
| [SigParserDotNetApis](https://github.com/DragnetTech/SigParserDotNetApis) | other | SigParser API access code for .NET developers to use to call the SigParser APIs | 1 | 2023-02-08 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.sigparser.com/pricing](https://www.sigparser.com/pricing)
- [https://www.sigparser.com/developers](https://www.sigparser.com/developers)
- [https://www.sigparser.com/how-to-category/ai-and-mcp](https://www.sigparser.com/how-to-category/ai-and-mcp)
- [https://ipaas.sigparser.com/api/mcp](https://ipaas.sigparser.com/api/mcp)

4 source URLs. Raw sources field, verbatim:

https://www.sigparser.com/pricing, https://www.sigparser.com/developers, https://www.sigparser.com/how-to-category/ai-and-mcp, https://ipaas.sigparser.com/api/mcp

**Notes, verbatim from the file**
READ THE mcp_status QUALIFIER BEFORE CITING THIS ENTRY. Verified 2026-09-07: POST of an MCP initialize to https://ipaas.sigparser.com/api/mcp returned HTTP 401 and a GET returned HTTP 405, exactly how a live auth-gated MCP endpoint behaves, and that host is first-party (SigParser's own API documentation prints pagination URLs on ipaas.sigparser.com). What is missing is any vendor page describing the server: sigparser.com/mcp and sigparser.com/developers/mcp both return 404, sigparser.com/llms.txt returns 404, the developers page never mentions MCP, and the site's own sitemap declares a content category at /how-to-category/ai-and-mcp which renders "No items found". The official call here therefore rests entirely on a first-party endpoint that answers as an MCP server, with zero first-party prose about it. That is weaker evidence than every other official entry in this file and is flagged rather than smoothed over; re-check for a published docs page before this is used on camera. Note also the mismatch between the gate and the product: the API tier is $499/month and sales-routed, while the underlying value (contacts mined from mailboxes the buyer already owns) is exactly what a solo operator would most want to automate. 2026-09-07: Official MCP registry carries com.sigparser/sigparser (DNS-verified sigparser.com namespace) with remote https://ipaas.sigparser.com/api/mcp; that URL returned 401 to an MCP initialize (https://ipaas.sigparser.com/api/mcp).

**Provenance**

- **Entry id**: 01-sigparser

- **Source file**: 01-data-enrichment.md

- **Source line**: 834

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
