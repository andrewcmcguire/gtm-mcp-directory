# Apideck: MCP server status, API access gate and what it does

> A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint... Official MCP, Free to start. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Apideck

# Apideck

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-08-25
CLI: apideck

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [apideck.com](https://apideck.com) · entry id 07-apideck · source 07-mcp-infrastructure.md line 273

**What it does**
A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint covering CRM, accounting, HRIS, ATS, file storage and issue tracking.

**AI features, separated from automation with an AI label on it**
A dynamic mode that exposes only four meta-tools so the agent discovers and executes tools on demand instead of loading every schema up front, cutting the context cost to roughly 1,300 tokens. That is a genuine agent-design feature rather than an AI claim.

**RevOps role**
One integration layer so an agent can read and write across every CRM in a portfolio without wiring each vendor separately; the multi-CRM abstraction a GTM agent needs when it cannot assume which CRM it will meet.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Managed OAuth via Apideck Vault on the hosted endpoint, or x-apideck-api-key plus x-apideck-app-id plus x-apideck-consumer-id headers for direct use.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/apideck-libraries/mcp (docs: https://developers.apideck.com/mcp; hosted endpoint: see the caveat in notes)

- [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp)
- [https://developers.apideck.com/mcp](https://developers.apideck.com/mcp)

**What this server exposes**

- **Tools named**: 25
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-13
- **Repo read**: apideck-libraries/mcp
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **API** Tools evidence: in a README table · calling it reads

- **ATS** 15 evidence: in a README table · calling it reads

- **Accounting** 143 evidence: in a README table · calling it reads

- **CRM** 50 evidence: in a README table · calling it reads

- **Connector** 8 evidence: in a README table · calling it reads

- **Ecommerce** 7 evidence: in a README table · calling it reads

- **HRIS** 25 evidence: in a README table · calling it reads

- **Header** Description evidence: in a README table · calling it reads

- **Mode** Tools exposed evidence: in a README table · calling it reads

- **Proxy** 6 evidence: in a README table · calling it reads

- **Scope** HTTP methods evidence: in a README table · calling it reads

- **Vault** 23 evidence: in a README table · calling it reads

- **Webhook** 6 evidence: in a README table · calling it reads

- **apideck-month-end-close-check** Fans out aged-creditors, aged-debtors, balance-sheet, and P&L in parallel. Returns a partial result when some reports aren't supported by the connector. evidence: in a README table · calling it reads

- **code** `apideck_search` + `apideck_run` evidence: in a README table · calling it reads

- **destructive** DELETE evidence: in a README table · calling it writes

- **get_doc** Return the full markdown of a documentation page by path, or a single section of it. Use search_docs or list_docs to find paths. evidence: answered tools/list · calling it reads · required: path

- **list_docs** List documentation pages with their path, title, description and last-modified date. Useful to browse the structure before searching or to find pages under a prefix. evidence: answered tools/list · calling it reads

- **read** GET, HEAD evidence: in a README table · calling it reads

- **search_docs** Full-text search over the documentation. Returns matching sections with a snippet, the page path and heading anchor. Call get_doc with a returned path to read the full page or a single section. evidence: answered tools/list · calling it reads · required: query

- **static** All 330 tools evidence: in a README table · calling it reads

- **write** POST, PUT, PATCH evidence: in a README table · calling it writes

- **x-apideck-api-key** Your Apideck API key evidence: in a README table · calling it reads

- **x-apideck-app-id** Your Apideck application ID evidence: in a README table · calling it reads

- **x-apideck-consumer-id** The end-user / customer ID in your app (**optional** - see below) evidence: in a README table · calling it reads

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-13. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: apideck
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-13

Install, as the source shows it:

```
brew install apideck-libraries/tap/apideck
```

quoted from [https://www.apideck.com/cli](https://www.apideck.com/cli) on 2026-09-13, via brew

```
go install github.com/apideck-libraries/cli/cmd/apideck@latest
```

quoted from [https://developers.apideck.com/cli](https://developers.apideck.com/cli) on 2026-09-13, via go

```
docker run apideck/cli
```

quoted from [https://developers.apideck.com/cli](https://developers.apideck.com/cli) on 2026-09-13, via docker

Login or key hint seen on the page:

apideck auth

Subcommands seen with the binary:

accounting, agent-prompt, auth, crm, explore, skill

Where it was documented:

- [https://www.apideck.com/cli](https://www.apideck.com/cli) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-13.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

[https://developers.apideck.com/mcp](https://developers.apideck.com/mcp)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp)

**On GitHub**

[github.com/apideck-libraries](https://github.com/apideck-libraries) tied to the vendor by rule 1, account website https://www.apideck.com/ has the vendor's domain, confidence strong

- **Public repositories**: 36, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 2 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [sdk-java](https://github.com/apideck-libraries/sdk-java) | SDK | | 1 | 2026-09-08 | v0.40.0 |
| [sdk-csharp](https://github.com/apideck-libraries/sdk-csharp) | SDK | | 4 | 2026-09-08 | v0.32.0 |
| [sdk-go](https://github.com/apideck-libraries/sdk-go) | SDK | | 1 | 2026-09-08 | v0.34.0 |
| [sdk-typescript](https://github.com/apideck-libraries/sdk-typescript) | SDK | | 3 | 2026-09-08 | v0.48.0 |
| [sdk-php](https://github.com/apideck-libraries/sdk-php) | SDK | | 2 | 2026-09-08 | v0.25.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developers.apideck.com/mcp](https://developers.apideck.com/mcp)
- [https://www.apideck.com/mcp-server](https://www.apideck.com/mcp-server)
- [https://github.com/apideck-libraries/mcp](https://github.com/apideck-libraries/mcp)

3 source URLs. Raw sources field, verbatim:

https://developers.apideck.com/mcp, https://www.apideck.com/mcp-server, https://github.com/apideck-libraries/mcp

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. CAVEAT ON THE ENDPOINT: two different hosted endpoints appear in the vendor's own material, mcp.apideck.com in the developer docs and mcp.apideck.dev on the marketing page. Confirm which is current before wiring it up; the GitHub repo is cited as mcp_url because it is the one unambiguous vendor-owned artifact. Signup is self-serve and free to start, but the paid tier thresholds are not published, so "free" here means free-to-start, not free-at-volume. The four-meta-tool dynamic mode is the same design problem the Salesforce Hosted MCP entry (06) solves with Discover/Describe/Dispatch, and the two make a natural pair for a segment on how not to dump 3,000 tools on an agent.

**Provenance**

- **Entry id**: 07-apideck

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 273

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-13

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
