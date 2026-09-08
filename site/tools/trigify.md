# Trigify (Trigify.io): MCP server status, API access gate and what it does

> Monitors LinkedIn, X/Twitter, Reddit, YouTube, and podcasts for keyword mentions and engagement (likes,... Community MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Trigify (Trigify.io)

# Trigify (Trigify.io)

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://www.trigify.io](https://www.trigify.io) · entry id 05-trigify · source 05-signals-intent-abm.md line 211

**What it does**
Monitors LinkedIn, X/Twitter, Reddit, YouTube, and podcasts for keyword mentions and engagement (likes, comments, shares, job changes), mapping who engaged with that content into an "engagement graph" filtered by ICP criteria.

**AI features, separated from automation with an AI label on it**
Marketed as "GTM Signal Intelligence" but the mechanism is keyword monitoring plus engagement scraping and rules-based filtering across 30+ signal types - data aggregation and matching, not predictive ML or LLM analysis as documented. The "AI agents" framing refers to agents consuming the data via API/MCP, not Trigify generating it via AI.

**RevOps role**
Social/engagement-signal-based prospecting, surfacing warm leads from real-time social activity, feeding outbound sequencing tools.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: api key (from app.trigify.io/settings; via `trigify login --api-key`, env var TRIGIFY_API_KEY, or a per-command flag)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/bcharleson/trigify-cli

- [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli)

**What this server exposes**

- **Tools named**: 3
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-08
- **Repo read**: bcharleson/trigify-cli
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **Endpoint** Method evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **Layer** What you get evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **Operation** Cost evidence: in a README table · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli)

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.trigify.io/](https://www.trigify.io/)
- [https://www.trigify.io/pricing](https://www.trigify.io/pricing)
- [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli)
- [https://libraries.io/npm/trigify-cli](https://libraries.io/npm/trigify-cli)
- [https://instantly.ai/marketplace/trigify](https://instantly.ai/marketplace/trigify)

5 source URLs. Raw sources field, verbatim:

https://www.trigify.io/, https://www.trigify.io/pricing, https://github.com/bcharleson/trigify-cli, https://libraries.io/npm/trigify-cli, https://instantly.ai/marketplace/trigify

**Notes, verbatim from the file**
Trigify's own site claims "Every Trigify signal, search and workflow is available to AI agents through a REST API, an MCP server and a CLI," implying a first-party MCP exists, but no distinct official repo/URL was found (zero results on PulseMCP; none on mcp.so/glama.ai either) - so mcp_status is set to community, backed only by the concrete third-party repo in hand. Unusually solo-operator-friendly pricing: self-serve, 14-day free trial, Starter $40/mo includes API access.

**Provenance**

- **Entry id**: 05-trigify

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 211

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
