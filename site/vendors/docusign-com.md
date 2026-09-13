# DocuSign: products, MCP servers and connect URLs, one vendor page

> DocuSign (docusign.com): 1 product in The GTM MCP Directory, 1 with an official MCP server, 0 answering a live handshake, 4 tools catalogued. Data baked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Vendors](../vendors/index.md) /
DocuSign

# DocuSign

1 product in the directory
1 official MCP server
0 live handshakes
Data baked 2026-09-12

Vendor domain: [docusign.com](https://docusign.com) · [Public company brief (DOCU)](https://andrewcmcguire.com/companies/docusign/) · vendor page id docusign-com

**The rollup**

- **Products**: 1, facts checked by hand 2026-08-24

- **Official MCP servers**: 1 of 1, as recorded on 2026-08-24

- **Community MCP servers**: 0 of 1

- **Live handshake**: 0 of 1 answered an MCP initialize, 1 probed, 2026-09-04

- **Repo local**: 0 of 1: a server you install and run yourself

- **Docs only**: 1 of 1: the recorded URL is a page about the server, not the server

- **Tools catalogued**: 4 named across 1 measured server, harvested 2026-09-12

- **Bench tested**: 0 of 1 here, 1 of 834 across the directory

- **Ships a CLI**: 1 of 1 official, 0 community only, 0 none found, harvested 2026-09-12

- **GitHub organisation**: [github.com/docusign](https://github.com/docusign), tied to the domain with evidence 2026-09-08

A live handshake means the URL answered an MCP initialize as a server on the probe date. It is liveness and nothing more: nobody has run its tools. A tool being catalogued means a server names it, by answering tools/list, in its own source, or in the vendor's documentation. None of them has been called. A tool count of 0 means not measured, never zero tools.

**Products, 1**

### [DocuSign](../tools/docusign.md)

E-signature and Intelligent Agreement Management (IAM) platform; the CLM/AI side covered here is agreement creation, status tracking, and AI-assisted querying/analysis of agreement data via MCP, distinct from plain e-signature.

[Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED

- **Endpoint probe**: docs page, not an endpoint, 2026-09-04

- **Connect URL**: [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/) (docs page)

- **Tools catalogued**: 4 named, harvested 2026-09-12, catalogue fixed

- **last_checked**: 2026-08-24

**The gates, in plain words**

1 of 1 paid and self serve, API access by paying, no sales call.

The gate is the api_gate field on each product entry, established by hand on the last_checked date shown above. It records whether a solo operator can get API access without a contract. Money is not tracked.

**Jobs the vendor says its products do**

- [Send a document for signature](../jobs/send-document-for-signature.md)
- [Read contract terms](../jobs/read-contract-terms.md)

2 distinct job labels, the union across 1 product, tagged 2026-08-25. A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

**Connect URLs**

- [https://developers.docusign.com/platform/mcp-server/](https://developers.docusign.com/platform/mcp-server/) (DocuSign, docs page, probed 2026-09-04)

An endpoint is where an agent connects. A docs page is where a person reads about connecting. Both are published because both are what the probe found; an agent needs the first.

**Command line**

### [DocuSign](../tools/docusign.md) docusign official CLI

```
npm install -g @docusign/cli
```

quoted from [https://www.npmjs.com/package/@docusign/cli](https://www.npmjs.com/package/@docusign/cli) on 2026-09-12, via npm

2 more install commands, harvested 2026-09-12, all on the [tool page](../tools/docusign.md).

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it.

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

**What this page does not claim**

A job tag is a vendor claim: it means the vendor says the product does this, and it is not a test result. A listed tool has not been run: the catalogue says what an agent could try, not what works. 1 of 834 directory entries are bench tested, meaning somebody personally ran the tool on a stated date, and 0 of this vendor's 1 product are among them. There is no verdict here on whether this vendor is better than another.

Vendor pages group the directory's canonical product entries by vendor_domain. The vendor name is the product display name that matches the domain when several products share it; nothing on this page is typed by hand. Data baked 2026-09-12 by build_directory.py (phase 1).
