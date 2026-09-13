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
CLI: trigify

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

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 380 entries that record an official or community MCP server carry a harvested tool list. The other 261 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: trigify
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g @trigify/cli
```

quoted from [https://www.npmjs.com/package/@trigify/cli](https://www.npmjs.com/package/@trigify/cli) on 2026-09-12, via npm

Packages seen, with the version on 2026-09-12:

- [npm: @trigify/cli 1.1.0](https://www.npmjs.com/package/@trigify/cli)
- [npm: trigify-cli 0.2.0, third party](https://www.npmjs.com/package/trigify-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

528 of 784 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/bcharleson/trigify-cli](https://github.com/bcharleson/trigify-cli)

**On GitHub**

[github.com/trigify](https://github.com/trigify) tied to the vendor by rule 3, account website https://trigify.io has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-04-01

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [skills](https://github.com/trigify/skills) | other | Agentic Skills | 0 | 2026-04-01 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Monitor social and community mentions](../jobs/monitor-social-mentions.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 784 entries carry at least one tag; 849 tags are assigned in total.

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

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
