# DocuSign: MCP server status, API access gate and what it does

> E-signature and Intelligent Agreement Management (IAM) platform; the CLM/AI side covered here is agreement... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
DocuSign

# DocuSign

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-08-24
CLI: docusign

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [docusign.com](https://docusign.com) · entry id 13-docusign · source 13-proposals-deals.md line 33

**What it does**
E-signature and Intelligent Agreement Management (IAM) platform; the CLM/AI side covered here is agreement creation, status tracking, and AI-assisted querying/analysis of agreement data via MCP, distinct from plain e-signature.

**AI features, separated from automation with an AI label on it**
MCP tools let an AI client query and analyze agreement data conversationally (find documents, check status, move signing workflows forward from chat) - this is an AI-agent access layer over DocuSign's IAM platform; DocuSign also markets separate "Intelligent Agreement Management" AI analysis features not independently verified in this research.

**RevOps role**
E-signature and agreement-management system of record; the MCP server is a genuinely new, low-friction AI-agent entry point into a platform that otherwise gates by envelope volume and dollar tier.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - Streamable HTTP transport; first connection opens a browser window to sign in and authorize, then reuses credentials.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (Open Beta)

mcp_url, verbatim from the file:

https://developers.docusign.com/platform/mcp-server/ ; hosted endpoint https://mcp.docusign.com/mcp ; announcement/community thread: https://community.docusign.com/general-74/building-with-ai-just-got-easier-introducing-the-docusign-mcp-server-25912

- [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/)
- [https://mcp.docusign.com/mcp](https://mcp.docusign.com/mcp)
- [https://community.docusign.com/general-74/building-with-ai-just-got-easier-introducing-the-docusign-mcp-server-25912](https://community.docusign.com/general-74/building-with-ai-just-got-easier-introducing-the-docusign-mcp-server-25912)

**What this server exposes**

- **Tools named**: 4
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **getAgreementDetails** Pull structured metadata for a specific agreement. evidence: in the vendor docs · calling it reads

- **getAllAgreements** Retrieve a filtered list of agreements by counterparty, agreement type, or date range. evidence: in the vendor docs · calling it reads

- **getWorkflowTriggerRequirements** Retrieve the trigger requirements for the target workflow. evidence: in the vendor docs · calling it reads

- **triggerWorkflow** Initiate the process for a preconfigured workflow. evidence: in the vendor docs · calling it reads

119 of the 337 entries that record an official or community MCP server carry a harvested tool list. The other 218 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: docusign
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @docusign/cli
```

quoted from [https://www.npmjs.com/package/@docusign/cli](https://www.npmjs.com/package/@docusign/cli) on 2026-09-12, via npm

```
npm install -g @docusign/agreement-cli
```

quoted from [https://www.npmjs.com/package/@docusign/agreement-cli](https://www.npmjs.com/package/@docusign/agreement-cli) on 2026-09-12, via npm

```
npm install -g @docusign-it/sfpds
```

quoted from [https://www.npmjs.com/package/@docusign-it/sfpds](https://www.npmjs.com/package/@docusign-it/sfpds) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @docusign/cli 1.1.0-rc](https://www.npmjs.com/package/@docusign/cli)
- [npm: @docusign/agreement-cli 1.2.1-beta](https://www.npmjs.com/package/@docusign/agreement-cli)
- [npm: @docusign-it/sfpds 25.6.1](https://www.npmjs.com/package/@docusign-it/sfpds)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid, tiered by envelope volume. DocuSign's Developer API plans run Starter ($50/mo or $600/yr, 40 envelopes/mo) through Intermediate ($300/mo, 100 envelopes/mo) to Advanced ($480/mo, unlocks Bulk Send/PowerForms/Connect webhooks) and Enterprise (custom); a free developer sandbox account exists for prototyping but is explicitly not production-usable. The MCP Server itself is described as available to both developer and production accounts in Open Beta with "no intake form or approval required," which is a notably low-friction access point relative to the metered envelope API underneath it.

**API documentation**

No documentation URL recorded.

494 of 694 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/docusign](https://github.com/docusign) tied to the vendor by rule 3, account website https://developers.docusign.com/ has the vendor's domain, confidence strong

- **Public repositories**: 145, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-04

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [PSA](https://github.com/docusign/PSA) | other | Repo for all PSA assets | 1 | 2026-09-04 | workshop-kit-v1 |
| [community-code-along](https://github.com/docusign/community-code-along) | other | | 1 | 2026-09-04 | |
| [code-examples-csharp](https://github.com/docusign/code-examples-csharp) | docs or examples | Docusign C# code examples and launcher | 64 | 2026-09-03 | v2018.12.18-1 |
| [docusign-monitor-python-client](https://github.com/docusign/docusign-monitor-python-client) | SDK | | 2 | 2026-09-03 | v1.2.0 |
| [docusign-monitor-csharp-client](https://github.com/docusign/docusign-monitor-csharp-client) | SDK | The Official DocuSign Charp Library used to interact with the Monitor REST API. | 0 | 2026-09-03 | v2.0.2 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Send a document for signature](../jobs/send-document-for-signature.md)
- [Read contract terms](../jobs/read-contract-terms.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 694 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/)
- [https://mcpservers.org/remote-mcp-servers/docusign](https://mcpservers.org/remote-mcp-servers/docusign)
- [https://www.pulsemcp.com/servers/docusign](https://www.pulsemcp.com/servers/docusign)
- [https://www.docusign.com/blog/developers/claude-docusign-mcp-connector-guide](https://www.docusign.com/blog/developers/claude-docusign-mcp-connector-guide)
- [https://ecom.docusign.com/plans-and-pricing/developer](https://ecom.docusign.com/plans-and-pricing/developer)

5 source URLs. Raw sources field, verbatim:

https://developers.docusign.com/platform/mcp-server/, https://mcpservers.org/remote-mcp-servers/docusign, https://www.pulsemcp.com/servers/docusign, https://www.docusign.com/blog/developers/claude-docusign-mcp-connector-guide, https://ecom.docusign.com/plans-and-pricing/developer

**Notes, verbatim from the file**
This entry deliberately covers the CLM/AI/MCP side per the seed list's instruction, not DocuSign's base e-signature product as a whole. The MCP Server being open to both developer AND production accounts with no approval gate is unusual for an incumbent this large - worth flagging as a genuinely low-friction access point.

**Provenance**

- **Entry id**: 13-docusign

- **Source file**: 13-proposals-deals.md

- **Source line**: 33

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
