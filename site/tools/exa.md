# Exa: MCP server status, API access gate and what it does

> A search API that returns web pages and structured results ranked by semantic/meaning similarity to a query... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Exa

# Exa

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [exa.ai](https://exa.ai) · entry id 01-exa · source 01-data-enrichment.md line 293

**What it does**
A search API that returns web pages and structured results ranked by semantic/meaning similarity to a query (embeddings-based) rather than keyword matching, plus tools to fetch page contents and get LLM-generated answers with citations; used in GTM stacks (e.g., Clay) as a research layer to pull live company and person info off the open web.

**AI features, separated from automation with an AI label on it**
Core ranking genuinely uses transformer-based embeddings for semantic ("neural") search - that part is real ML, not marketing dressing. The "Answer" and "Agent"/deep-research endpoints layer an LLM on top to summarize/synthesize results with citations. It is not a proprietary contact database - it's search+summarization over the public web, so coverage/quality depends on what's crawlable and indexed, not a curated B2B dataset.

**RevOps role**
Web-research/enrichment layer used to supplement contact databases with live company or person context (news, funding signals, hiring, tech stack) - typically fed into Clay tables or agent workflows rather than used as a system of record.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (issued via dashboard.exa.ai)

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/exa-labs/exa-mcp-server (hosted endpoint https://mcp.exa.ai/mcp)

- [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
- [https://mcp.exa.ai/mcp](https://mcp.exa.ai/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)

**Jobs it can do**

- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
- [https://exa.ai/mcp](https://exa.ai/mcp)
- [https://exa.ai/pricing](https://exa.ai/pricing)
- [https://exa.ai/docs/reference/pricing](https://exa.ai/docs/reference/pricing)

4 source URLs. Raw sources field, verbatim:

https://github.com/exa-labs/exa-mcp-server, https://exa.ai/mcp, https://exa.ai/pricing, https://exa.ai/docs/reference/pricing

**Notes, verbatim from the file**
New accounts get $20 in free credits (~2,800 searches); free tier also adds $10/month in credits ongoing, then pay-as-you-go - no sales contact required for API access. Pricing is per-endpoint (roughly $7/1k requests for search, ~$1/1k pages for full content, ~$5/1k for the Answer endpoint). Unlike the other tools in this category, Exa has no phone/email verification or contact-database feature - it's general web search/research repurposed for GTM enrichment.

**Provenance**

- **Entry id**: 01-exa

- **Source file**: 01-data-enrichment.md

- **Source line**: 293

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
