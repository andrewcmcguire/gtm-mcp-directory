# Versium REACH: MCP server status, API access gate and what it does

> An identity-graph append service that turns partial contact records into enriched B2B and B2C profiles, plus... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Versium REACH

# Versium REACH

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [versium.com](https://versium.com) · entry id 01-versium-reach · source 01-data-enrichment.md line 579

**What it does**
An identity-graph append service that turns partial contact records into enriched B2B and B2C profiles, plus audience sizing and real-time email validation.

**AI features, separated from automation with an AI label on it**
The MCP layer translates natural language into REACH API calls. The underlying identity resolution is deterministic graph matching, not AI. This is a clean example of an "AI" surface bolted onto a non-AI core, and the entry says so.

**RevOps role**
Identity resolution and append step between raw lead capture and CRM or ad-platform activation.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth, and the client must support dynamic client registration.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL**: [https://app.versium.com/mcp/reach](https://app.versium.com/mcp/reach)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://app.versium.com/mcp/reach (docs: https://reach-help.versium.com/docs/mcp-overview; announcement: https://versium.com/blog/versium-launches-versium-reach-mcp-server/)

- [https://app.versium.com/mcp/reach](https://app.versium.com/mcp/reach)
- [https://reach-help.versium.com/docs/mcp-overview](https://reach-help.versium.com/docs/mcp-overview)
- [https://versium.com/blog/versium-launches-versium-reach-mcp-server/](https://versium.com/blog/versium-launches-versium-reach-mcp-server/)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 359 entries that record an official or community MCP server carry a harvested tool list. The other 240 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://reach-help.versium.com/docs/mcp-overview](https://reach-help.versium.com/docs/mcp-overview)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/VersiumAnalytics](https://github.com/VersiumAnalytics) tied to the vendor by rule 3, account website https://versium.com has the vendor's domain, confidence strong

- **Public repositories**: 7, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2025-10-01

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [reach-api-sdk-node](https://github.com/VersiumAnalytics/reach-api-sdk-node) | SDK | Node.js client library for accessing the Versium REACH API | 5 | 2025-10-01 | v1.1.1 |
| [offline-file-hasher](https://github.com/VersiumAnalytics/offline-file-hasher) | other | This javascript hashes a file on your computer, then saves the hashed output. This process is 100% offline and... | 2 | 2023-07-14 | |
| [reach-api-php-sdk](https://github.com/VersiumAnalytics/reach-api-php-sdk) | SDK | A PHP client library for accessing the REACH APIs | 1 | 2023-06-21 | v0.4.0 |
| [reach-api-python-sdk](https://github.com/VersiumAnalytics/reach-api-python-sdk) | SDK | | 3 | 2023-05-24 | v1.1.0 |
| [versium-modeling](https://github.com/VersiumAnalytics/versium-modeling) | other | Tools for appending data and creating lead scoring models | 5 | 2022-10-06 | v0.1.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 739 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://versium.com/blog/versium-launches-versium-reach-mcp-server/](https://versium.com/blog/versium-launches-versium-reach-mcp-server/)
- [https://versium.com/versium-reach-mcp/](https://versium.com/versium-reach-mcp/)
- [https://reach-help.versium.com/docs/mcp-overview](https://reach-help.versium.com/docs/mcp-overview)
- [https://www.pulsemcp.com/servers/versium-reach](https://www.pulsemcp.com/servers/versium-reach)

4 source URLs. Raw sources field, verbatim:

https://versium.com/blog/versium-launches-versium-reach-mcp-server/, https://versium.com/versium-reach-mcp/, https://reach-help.versium.com/docs/mcp-overview, https://www.pulsemcp.com/servers/versium-reach

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. Launched February 2026. Tool surface covers contact, demographic and firmographic appends, C2B and IP-to-domain resolution, a consumer audience builder, B2B list estimates, and email hygiene. Requires an existing REACH account, so a solo operator needs a paid seat before the MCP is usable. The dynamic-client-registration requirement is a real compatibility constraint: clients that do not implement DCR cannot connect at all.

**Provenance**

- **Entry id**: 01-versium-reach

- **Source file**: 01-data-enrichment.md

- **Source line**: 579

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
