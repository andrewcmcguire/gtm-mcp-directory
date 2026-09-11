# Similarweb: MCP server status, API access gate and what it does

> Web, app and market intelligence platform that estimates traffic, audience, keyword and competitive metrics... Official MCP, Enterprise only. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Similarweb

# Similarweb

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-25
CLI: similarweb (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [similarweb.com](https://similarweb.com) · entry id 05-similarweb · source 05-signals-intent-abm.md line 647

**What it does**
Web, app and market intelligence platform that estimates traffic, audience, keyword and competitive metrics for any domain, used in sales as an account-prioritisation and account-research signal.

**AI features, separated from automation with an AI label on it**
The core estimation models are statistical panel and clickstream modelling rather than generative AI. The AI surface is the MCP server and natural-language querying over the same metrics, so treat "AI" here as an access layer, not a new capability.

**RevOps role**
Account-sizing, competitor-displacement and territory-prioritisation signal, and the standard source for "is this account actually growing" checks during account research.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: CONFLICTING VENDOR STATEMENTS, flagged rather than resolved. Both Similarweb developer docs pages state an active Similarweb API key from Account Settings is required and passed via the MCP client config. A third-party setup guide (mcpservers.org) describes an OAuth browser flow on first connect. The vendor docs are the stronger source, so treat it as api key until Similarweb documents OAuth itself.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: auth wall at every path, not proven a server
- **Endpoint URL**: [https://mcp.similarweb.com](https://mcp.similarweb.com)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-04 the recorded URL answered an auth challenge, but so did a path on that host which cannot exist, so the challenge proves a wall rather than a running MCP server.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.similarweb.com (docs: https://developers.similarweb.com/docs/similarweb-mcp and https://docs.similarweb.com/api-v5/similarweb-mcp/mcp-setup; announcement: https://www.similarweb.com/blog/updates/announcements/mcp-server-launch/)

- [https://mcp.similarweb.com](https://mcp.similarweb.com)
- [https://developers.similarweb.com/docs/similarweb-mcp](https://developers.similarweb.com/docs/similarweb-mcp)
- [https://docs.similarweb.com/api-v5/similarweb-mcp/mcp-setup](https://docs.similarweb.com/api-v5/similarweb-mcp/mcp-setup)
- [https://www.similarweb.com/blog/updates/announcements/mcp-server-launch/](https://www.similarweb.com/blog/updates/announcements/mcp-server-launch/)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. The full roll up is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: similarweb
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-11

Install, as the source shows it:

```
npm install -g similarweb
```

quoted from [https://www.npmjs.com/package/similarweb](https://www.npmjs.com/package/similarweb) on 2026-09-11, via npm, a third party source

```
npm install -g similarweb-cli
```

quoted from [https://www.npmjs.com/package/similarweb-cli](https://www.npmjs.com/package/similarweb-cli) on 2026-09-11, via npm, a third party source

Packages seen, with the version on 2026-09-11:

- [npm: similarweb 0.1.0, third party](https://www.npmjs.com/package/similarweb)
- [npm: similarweb-cli 0.0.1, third party](https://www.npmjs.com/package/similarweb-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-11.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

[https://developers.similarweb.com/](https://developers.similarweb.com/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/similarweb](https://github.com/similarweb) tied to the vendor by rule 3, account website http://www.similarweb.com has the vendor's domain, confidence strong

- **Public repositories**: 32, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [Movie-Trivia-Day-2-](https://github.com/similarweb/Movie-Trivia-Day-2-) | other | | 0 | 2026-09-08 | |
| [Movie-Trivia-day-1](https://github.com/similarweb/Movie-Trivia-day-1) | other | | 0 | 2026-09-07 | |
| [Emoji-Movie-Trivia](https://github.com/similarweb/Emoji-Movie-Trivia) | other | | 0 | 2026-09-07 | |
| [Host-side-](https://github.com/similarweb/Host-side-) | other | | 0 | 2026-08-30 | |
| [linq2fb](https://github.com/similarweb/linq2fb) | other | LinqToDB adapter for Firebolt | 6 | 2026-08-12 | v6.0.0-rc.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://developers.similarweb.com/docs/similarweb-mcp](https://developers.similarweb.com/docs/similarweb-mcp)
- [https://docs.similarweb.com/api-v5/similarweb-mcp/mcp-setup](https://docs.similarweb.com/api-v5/similarweb-mcp/mcp-setup)
- [https://www.similarweb.com/corp/ai/mcp/](https://www.similarweb.com/corp/ai/mcp/)
- [https://www.similarweb.com/blog/updates/announcements/mcp-server-launch/](https://www.similarweb.com/blog/updates/announcements/mcp-server-launch/)
- [https://www.similarweb.com/corp/pricing/](https://www.similarweb.com/corp/pricing/)
- [https://mcpservers.org/remote-mcp-servers/similarweb](https://mcpservers.org/remote-mcp-servers/similarweb)

6 source URLs. Raw sources field, verbatim:

https://developers.similarweb.com/docs/similarweb-mcp, https://docs.similarweb.com/api-v5/similarweb-mcp/mcp-setup, https://www.similarweb.com/corp/ai/mcp/, https://www.similarweb.com/blog/updates/announcements/mcp-server-launch/, https://www.similarweb.com/corp/pricing/, https://mcpservers.org/remote-mcp-servers/similarweb

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. 21 tools across three groups: Web Metrics (16 tools covering traffic, referrals, similar sites, demographics, technology detection), Search Metrics (2 tools for SERP and keyword click trends), App Metrics (3 tools for install penetration, store rankings, app details). IMPORTANT COST MECHANIC, and the sharpest practical warning in this file: MCP calls consume the same data credits as regular API calls, and consumption varies with query complexity, so an agent looping over an account list can burn a credit budget fast with no natural stopping point. api_gate is enterprise-only despite a naming quirk worth explaining: the developer docs say MCP requires a subscription on the "API-only, Business, or Enterprise" plans with API access enabled, but Similarweb's corporate pricing page publishes no prices at all, splits into self-service "Entrepreneurs" packages versus sales-contact "Businesses and Enterprises," and its FAQ states plainly that "API is available as part of our customized packages for Businesses." So the "API-only" plan has no published price and no self-serve path. BEWARE the Apify "Similarweb scraper" MCP servers in search results; those are third-party scrapers, one explicitly marked DEPRECATED, and are not Similarweb.

**Provenance**

- **Entry id**: 05-similarweb

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 647

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-11

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
