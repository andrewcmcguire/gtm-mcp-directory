# HighLevel (GoHighLevel): MCP server status, API access gate and what it does

> An all-in-one agency CRM covering contacts, pipelines, conversations, calendars, payments and campaign... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
HighLevel (GoHighLevel)

# HighLevel (GoHighLevel)

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-25
CLI: gohighlevel (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [gohighlevel.com](https://gohighlevel.com) · entry id 06-highlevel · source 06-revops-infra.md line 489

**What it does**
An all-in-one agency CRM covering contacts, pipelines, conversations, calendars, payments and campaign automation across many client sub-accounts from one place.

**AI features, separated from automation with an AI label on it**
The MCP itself is a plain tool surface, so the AI is whatever client is attached. HighLevel ships its own conversation AI separately, and that is not what the MCP exposes.

**RevOps role**
Consolidated CRM and marketing-automation stack for agencies and SMB GTM, with one endpoint reaching every sub-account object.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: A Private Integration Token passed as a bearer token, plus a locationId header. Tool availability follows the scopes granted to the token.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL**: [https://services.leadconnectorhq.com/mcp/](https://services.leadconnectorhq.com/mcp/)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://services.leadconnectorhq.com/mcp/ (docs: https://marketplace.gohighlevel.com/docs/other/mcp/)

- [https://services.leadconnectorhq.com/mcp/](https://services.leadconnectorhq.com/mcp/)
- [https://marketplace.gohighlevel.com/docs/other/mcp/](https://marketplace.gohighlevel.com/docs/other/mcp/)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. The full roll up is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: gohighlevel
- **Status**: community CLI, third party
- **Strongest evidence**: github
- **Harvested**: 2026-09-08

No install command was quoted by the harvest. The status rests on the package or page linked below.

Subcommands seen with the binary:

calendars, contacts, conversations, metadata, opportunities

Where it was documented:

- [https://github.com/deanmikan/gohighlevel-cli](https://github.com/deanmikan/gohighlevel-cli) (the repository that documented it)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-08.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://marketplace.gohighlevel.com/docs/other/mcp/](https://marketplace.gohighlevel.com/docs/other/mcp/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/GoHighLevel](https://github.com/GoHighLevel) tied to the vendor by rule 3, account website http://gohighlevel.com has the vendor's domain, confidence strong

- **Public repositories**: 18, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [marketplace-cli](https://github.com/GoHighLevel/marketplace-cli) | CLI | | 0 | 2026-09-08 | |
| [highlevel-api-sdk](https://github.com/GoHighLevel/highlevel-api-sdk) | SDK | Official SDK for HighLevel Public APIs | 29 | 2026-09-03 | v3.1.0 |
| [highlevel-api-docs](https://github.com/GoHighLevel/highlevel-api-docs) | docs or examples | This repo is our public documentation for API v2. | 144 | 2026-08-25 | |
| [ghl-sdk-examples](https://github.com/GoHighLevel/ghl-sdk-examples) | docs or examples | Examples for how to use HighLevel SDK | 12 | 2026-06-25 | |
| [highlevel-api-python](https://github.com/GoHighLevel/highlevel-api-python) | SDK | Python library for the HighLevel API. | 4 | 2026-06-25 | v3.0.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Book a meeting](../jobs/book-a-meeting.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://help.gohighlevel.com/support/solutions/articles/155000005741-how-to-setup-and-use-the-highlevel-mcp-server](https://help.gohighlevel.com/support/solutions/articles/155000005741-how-to-setup-and-use-the-highlevel-mcp-server)
- [https://marketplace.gohighlevel.com/docs/other/mcp/](https://marketplace.gohighlevel.com/docs/other/mcp/)
- [https://ideas.gohighlevel.com/highlevel-mcp](https://ideas.gohighlevel.com/highlevel-mcp)

3 source URLs. Raw sources field, verbatim:

https://help.gohighlevel.com/support/solutions/articles/155000005741-how-to-setup-and-use-the-highlevel-mcp-server, https://marketplace.gohighlevel.com/docs/other/mcp/, https://ideas.gohighlevel.com/highlevel-mcp

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. 36 native tools at time of check, across contacts, conversations, opportunities, calendars, payments, locations, blogs, email templates and social posting. No additional charge beyond an existing HighLevel subscription. DISCOVERY HAZARD: a large community MCP ecosystem has grown around HighLevel (mastanley13, uxieee with 413 endpoints, drjerryrelth with 212 tools), and those unofficial forks rank above the vendor's own server in most searches, so a buyer searching "gohighlevel mcp" will hit a community fork first. Scoping note: this is the SMB and agency end of the market rather than the enterprise B2B motion most of this directory covers.

**Provenance**

- **Entry id**: 06-highlevel

- **Source file**: 06-revops-infra.md

- **Source line**: 489

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
