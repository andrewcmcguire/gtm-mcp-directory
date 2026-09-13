# Vayne: MCP server status, API access gate and what it does

> A LinkedIn data platform that runs Sales Navigator lead and account scraping, single-URL and batch profile... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Vayne

# Vayne

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07
CLI: vayne

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [vayne.io](https://vayne.io) · entry id 01-vayne · source 01-data-enrichment.md line 853

**What it does**
A LinkedIn data platform that runs Sales Navigator lead and account scraping, single-URL and batch profile and company scraping, job scraping and job search, post-engagement scraping, reverse email to LinkedIn lookup, and email and phone enrichment, all of it exposed as MCP tools as well as a REST API.

**AI features, separated from automation with an AI label on it**
None claimed in the data layer. Vayne is a scraping and enrichment engine and the AI is whichever agent calls it. The MCP server is the AI surface, and the vendor publishes its whole agent guide as a single markdown page specifically so an assistant can be handed it as context.

**RevOps role**
The LinkedIn-data leg of a GTM stack: list building from Sales Navigator, enrichment of a known profile, and engagement scraping for signal work, feeding a CRM or a sequencer downstream.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth or api key. The vendor's docs state OAuth is the default for Claude Desktop, Claude.ai, Claude Code and Cursor (server URL only, no token stored on the machine), and every other client sends a Vayne API token as an Authorization Bearer header.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.vayne.io/mcp (docs: https://www.vayne.io/en/mcp-documentation)

- [https://mcp.vayne.io/mcp](https://mcp.vayne.io/mcp)
- [https://www.vayne.io/en/mcp-documentation](https://www.vayne.io/en/mcp-documentation)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 319 entries that record an official or community MCP server carry a harvested tool list. The other 200 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: vayne
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @vayne/cli
```

quoted from [https://www.npmjs.com/package/@vayne/cli](https://www.npmjs.com/package/@vayne/cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: vayne 0.0.27, third party](https://www.npmjs.com/package/vayne)
- [npm: @vayne/cli 1.1.1](https://www.npmjs.com/package/@vayne/cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's MCP documentation states "Using the MCP requires a plan with API access (Starter and above), OAuth connections included: on a lower plan the connector still authorizes, but every tool call comes back with 'Plan does not include API access'." Starter is $49/month or $490/year on the published pricing page; a Free plan (200 leads/month) and a $29/month Freelance plan sit below it and do not carry API access.

**API documentation**

No documentation URL recorded.

471 of 649 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to vayne.io with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: VaynerMedia-NewYork, vaynerx, VaynerMedia-London, vaynejs, vaynermedia. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

No job tag on this entry.

378 of 649 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.vayne.io/en/mcp-documentation](https://www.vayne.io/en/mcp-documentation)
- [https://www.vayne.io/en/pricing](https://www.vayne.io/en/pricing)
- [https://mcp.vayne.io/mcp](https://mcp.vayne.io/mcp)

3 source URLs. Raw sources field, verbatim:

https://www.vayne.io/en/mcp-documentation, https://www.vayne.io/en/pricing, https://mcp.vayne.io/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.vayne.io/mcp returned HTTP 401 with a JSON-RPC error reading "Missing or invalid Authorization header. Provide your Vayne API token (or an OAuth access token) as a Bearer token.", which confirms a live auth-gated server and confirms both auth paths in one response. The failure mode the docs describe is the useful and unusual detail: on an under-tier plan the OAuth connection succeeds and only the tool calls fail, with the message "Plan does not include API access", so a buyer can appear connected and still get nothing back. The vendor publishes a copyable agent guide (tool catalogue, credit model, webhooks, export column glossary) as one markdown page, which is the llms.txt idea applied to a tool catalogue and is worth naming as a pattern. STANDING CATEGORY RISK applies in full: LinkedIn's User Agreement prohibits automation and every Sales Navigator scraping tool in this directory carries account-ban risk. The vendor's own site banner on this date advertised a waiting list for a "cookie less Sales Navigator scraper", which is a direct acknowledgement that the current method depends on a logged-in session. 2026-09-07: https://mcp.vayne.io/mcp returned 401 to an MCP initialize POST (https://mcp.vayne.io/mcp).

**Provenance**

- **Entry id**: 01-vayne

- **Source file**: 01-data-enrichment.md

- **Source line**: 853

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
