# Exa: MCP server status, API access gate and what it does

> A search API that returns web pages and structured results ranked by semantic/meaning similarity to a query... Official MCP, Free to start. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Exa

# Exa

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
BENCH-TESTED
Checked 2026-09-03
CLI: exa-cli (community)

> **BENCH-TESTED** Andrew personally ran it on a stated date. Cannot be bought. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [exa.ai](https://exa.ai) · entry id 01-exa · source 01-data-enrichment.md line 293

**What it does**
A search API that returns web pages and structured results ranked by semantic/meaning similarity to a query (embeddings-based) rather than keyword matching, plus tools to fetch page contents and get LLM-generated answers with citations; used in GTM stacks (e.g., Clay) as a research layer to pull live company and person info off the open web.

**AI features, separated from automation with an AI label on it**
Core ranking genuinely uses transformer-based embeddings for semantic ("neural") search - that part is real ML, not marketing dressing. The "Answer" and "Agent"/deep-research endpoints layer an LLM on top to summarize/synthesize results with citations. It is not a proprietary contact database - it's search+summarization over the public web, so coverage/quality depends on what's crawlable and indexed, not a curated B2B dataset.

**RevOps role**
Web-research/enrichment layer used to supplement contact databases with live company or person context (news, funding signals, hiring, tech stack) - typically fed into Clay tables or agent workflows rather than used as a system of record.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (issued via dashboard.exa.ai) for the self-hosted server and for quota. CORRECTED 2026-09-03 by bench test: the hosted endpoint https://mcp.exa.ai/mcp completed a full MCP session and served live results from both tools with NO credential sent - no Authorization header, no exaApiKey argument, no account. Measured, not inferred. See the bench notes below.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/exa-labs/exa-mcp-server (hosted endpoint https://mcp.exa.ai/mcp)

- [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
- [https://mcp.exa.ai/mcp](https://mcp.exa.ai/mcp)

**What this server exposes**

- **Tools named**: 11
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-12
- **Repo read**: exa-labs/exa-mcp-server
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **agent_run** Start or resume an Exa Agent run; runs may take several minutes. Retain the returned run ID and resume with runId when the tool reports the run is still running. An interrupted tool call is not an explicit cancellation request. evidence: in the server source · calling it writes

- **company_research_exa** [Deprecated: Use web_search_advanced_exa instead] Research any company to get business information, news, and insights. Best for: Learning about a company evidence: in the server source · calling it reads

- **deep_researcher_check** [Deprecated] Check status and get results from a deep research task. Best for: Getting the research report after calling deep_researcher_start. Returns: Research report when complete, or status update if still running. Important: Keep call evidence: in the server source · calling it reads

- **deep_researcher_start** [Deprecated] Start an AI research agent that searches, reads, and writes a detailed report. Takes 15 seconds to 2 minutes. Best for: Complex research questions needing deep analysis and synthesis. Returns: Research ID - use deep_researcher evidence: in the server source · calling it writes

- **deep_search_exa** [Deprecated: Use web_search_advanced_exa instead] Deep search with automatic query expansion for thorough research. Generates multiple search variations to find results from multiple angles, then synthesizes a short answer with citations. evidence: in the server source · calling it reads

- **get_code_context_exa** Find code examples, documentation, and programming solutions. Best for: Any programming question - API usage, library examples, code snippets, debugging help. Returns: Relevant code and documentation. Query tips: describe what you evidence: in the server source · calling it reads

- **linkedin_search_exa** ⚠️ DEPRECATED: This tool is deprecated. Please use evidence: in the server source · calling it reads

- **people_search_exa** [Deprecated: Use web_search_advanced_exa instead] Find people and their professional profiles. Best for: Finding professionals, executives, or anyone with a public profile. Returns: Profile information and links. evidence: in the server source · calling it reads

- **web_fetch_exa** Read a webpage's full content as clean markdown. Use after web_search_exa when highlights are insufficient or to read any URL. Best for: Extracting full content from known URLs. Batch multiple URLs in one call. Returns: Clean text content evidence: answered tools/list · calling it reads · required: urls

- **web_search_advanced_exa** Advanced web search with full control over filters, domains, dates, and content options. Best for: When you need specific filters like date ranges, domain restrictions, or category filters. Not recommended for: Simple searches - use web_se evidence: in the server source · calling it reads

- **web_search_exa** Search the web for any topic and get clean, ready-to-use content. Best for: Finding current information, news, facts, people, companies, or answering questions about any topic. Returns: Clean text content from top search result evidence: answered tools/list · calling it reads · required: query, objective

119 of the 740 entries that record an official or community MCP server carry a harvested tool list. The other 621 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: exa-cli
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
pip install exa-cli
```

quoted from [https://pypi.org/project/exa-cli/](https://pypi.org/project/exa-cli/) on 2026-09-12, via pypi, a third party source

Packages seen, with the version on 2026-09-12:

- [pypi: exa-cli 0.1.0, third party](https://pypi.org/project/exa-cli/)
- [pypi: exa-cli 0.1.0, third party](https://pypi.org/project/exa-cli/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

727 of 1251 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)

**On GitHub**

[github.com/exa-labs](https://github.com/exa-labs) tied to the vendor by rule 1, account website https://exa.ai has the vendor's domain, confidence strong

- **Public repositories**: 50, forks excluded, as read on 2026-09-08
- **Mention MCP**: 3 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [agent-skills](https://github.com/exa-labs/agent-skills) | other | Official skills for the Exa API. | 46 | 2026-09-03 | |
| [exa-js](https://github.com/exa-labs/exa-js) | SDK | The Official Exa Javascript SDK | 130 | 2026-09-03 | v2.20.0 |
| [exa-py](https://github.com/exa-labs/exa-py) | SDK | The Official Exa Python Package | 233 | 2026-09-03 | v2.20.0 |
| [exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) | MCP server | Exa MCP for web search and web crawling! | 4,987 | 2026-08-21 | |
| [company-researcher](https://github.com/exa-labs/company-researcher) | other | Company Researcher tool helps you instantly understand any company inside out. | 1,494 | 2026-08-08 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 1,251 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
- [https://exa.ai/mcp](https://exa.ai/mcp)
- [https://exa.ai/pricing](https://exa.ai/pricing)
- [https://exa.ai/docs/reference/pricing](https://exa.ai/docs/reference/pricing)
- H:/amcg-content/directory/BENCH_2026-09-03.md
- H:/amcg-content/directory/bench_history.jsonl

4 source URLs. Raw sources field, verbatim:

https://github.com/exa-labs/exa-mcp-server, https://exa.ai/mcp, https://exa.ai/pricing, https://exa.ai/docs/reference/pricing, H:/amcg-content/directory/BENCH_2026-09-03.md, H:/amcg-content/directory/bench_history.jsonl

**Notes, verbatim from the file**
New accounts get $20 in free credits (~2,800 searches); free tier also adds $10/month in credits ongoing, then pay-as-you-go - no sales contact required for API access. Pricing is per-endpoint (roughly $7/1k requests for search, ~$1/1k pages for full content, ~$5/1k for the Answer endpoint). Unlike the other tools in this category, Exa has no phone/email verification or contact-database feature - it's general web search/research repurposed for GTM enrichment. BENCH TEST 2026-09-03, the first in this directory, at $0 with no credential and no account, harness directory/bench_exa.py, full log directory/BENCH_2026-09-03.md, wire log directory/bench_history.jsonl record exa-2026-09-03. THE EXACT CALLS - POST https://mcp.exa.ai/mcp initialize (protocolVersion 2025-06-18) returned HTTP 200 in 92 ms with serverInfo exa-search-server 3.2.1 and a session id; tools/list returned HTTP 200 and exactly two tools, web_search_exa and web_fetch_exa (the GitHub repo named first in mcp_url is a locally installed server and a different surface, not run here); tools/call web_search_exa {"query":"category:people <person> <company> (<domain>)","numResults":5} was run once for each of three VENDOR founders. WHAT CAME BACK - Kareem Amin at Clay HTTP 200 in 1139 ms, 11009 chars, result 1 https://www.linkedin.com/in/kareemamin; Amit Bendov at Gong HTTP 200 in 1330 ms, 11457 chars, result 1 https://www.linkedin.com/in/amitbendov; Manny Medina at Outreach HTTP 200 in 1301 ms, 17396 chars, result 1 https://www.linkedin.com/in/medinism. 3 of 3 correct in position 1, judged by the role-and-company line carried in the same payload, which is a self-consistency check and not an independent one; three calls is a sample of three, not a hit rate. The call-prep chain also ran end to end - web_search_exa returned 35014 chars on a vendor account query and web_fetch_exa on https://www.clay.com/pricing returned HTTP 200 in 124 ms with 1568 chars of markdown. linkedin.com was never fetched; the only page fetches went to vendor domains. FAILURE MODES MEASURED - there is no null result: an invented person at an invented company returned HTTP 200 and a confident, unrelated LinkedIn profile, and a re-run returned a DIFFERENT wrong profile, so a caller must verify the returned profile's company against the input itself; results 2 to 5 were unrelated people on all three subjects, so only result 1 is usable; the default Python urllib user agent is rejected at the edge with HTTP 403 Cloudflare 1010 browser_signature_banned before any MCP traffic, a failure that looks nothing like an auth failure; an unknown tool name returns HTTP 200 with isError true and "MCP error -32602: Tool ... not found" in the body; a 2-URL batch fetch returns partial success inside one HTTP 200, with the failed URL's error as an inline string (CRAWL_LIVECRAWL_TIMEOUT); maxCharacters 1500 returned 1568 chars, so the cap is a target and not a truncation. Net: HTTP status cannot be used to detect failure on this server. This bench licenses nothing about any other entry and no Leaderboard score, and it is a snapshot of 2026-09-03 - the keyless endpoint is what answered that day, not a promise it stays keyless.

**Provenance**

- **Entry id**: 01-exa

- **Source file**: 01-data-enrichment.md

- **Source line**: 293

- **Tier**: BENCH-TESTED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
