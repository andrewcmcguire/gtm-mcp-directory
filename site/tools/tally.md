# Tally: MCP server status, API access gate and what it does

> A free-first online form builder (unlimited forms and submissions on the free plan, conditional logic,... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Tally

# Tally

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-07
CLI: tally-cli (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [tally.so](https://tally.so) · entry id 14-tally · source 14-inbound-plg-chat.md line 371

**What it does**
A free-first online form builder (unlimited forms and submissions on the free plan, conditional logic, payments, signatures, file uploads) with a REST API, webhooks and a hosted MCP server.

**AI features, separated from automation with an AI label on it**
None in the form engine. The vendor's MCP help page describes AI-assisted use through the server (build forms in natural language, "run sentiment analysis", "qualitative analysis at scale" on submissions), which is the connected model's work over Tally data, not a Tally feature.

**RevOps role**
The lowest-cost intake form under an inbound flow; the MCP gives an agent form building and submission reading on a plan that costs nothing.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth or api key. The help page states "The easiest way to connect is through OAuth, just click 'Connect' and follow the prompts. If you prefer, you can also authenticate using an API key." API keys go in an "Authorization: Bearer tly-xxxx" header.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.tally.so/mcp (docs: https://tally.so/help/mcp and https://developers.tally.so/api-reference/mcp)

- [https://api.tally.so/mcp](https://api.tally.so/mcp)
- [https://tally.so/help/mcp](https://tally.so/help/mcp)
- [https://developers.tally.so/api-reference/mcp](https://developers.tally.so/api-reference/mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 521 entries that record an official or community MCP server carry a harvested tool list. The other 402 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: tally-cli
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
pip install tally-cli
```

quoted from [https://pypi.org/project/tally-cli/](https://pypi.org/project/tally-cli/) on 2026-09-12, via pypi, a third party source

Packages seen, with the version on 2026-09-12:

- [pypi: tally-cli 0.45.0, third party](https://pypi.org/project/tally-cli/)
- [pypi: tally-cli 0.45.0, third party](https://pypi.org/project/tally-cli/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the help centre states "Tally's MCP server is free to use on all plans, including the free plan. There's no separate add-on or upgrade required." and "the Tally API is free for all Tally users, including the free plan." The pricing page lists Free ("Unlimited forms and submissions, completely free, as long as you stay within our fair usage guidelines"), Pro $24/month and Business $74/month.

**API documentation**

No documentation URL recorded.

635 of 1032 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/tallyforms](https://github.com/tallyforms) tied to the vendor by rule 3, account website https://tally.so has the vendor's domain, confidence strong

- **Public repositories**: 2, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-05-11

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [n8n-nodes-tallyforms](https://github.com/tallyforms/n8n-nodes-tallyforms) | plugin or integration | n8n trigger for Tally form submissions | 6 | 2026-05-11 | v1.3.3 |
| [framer-plugin](https://github.com/tallyforms/framer-plugin) | plugin or integration | The Tally plugin for Framer makes it effortless to embed any published Tally form directly into your Framer projects. | 3 | 2025-12-12 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

761 of 1,032 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://tally.so/help/mcp](https://tally.so/help/mcp)
- [https://developers.tally.so/api-reference/mcp](https://developers.tally.so/api-reference/mcp)
- [https://tally.so/help/api](https://tally.so/help/api)
- [https://tally.so/pricing](https://tally.so/pricing)
- [https://api.tally.so/mcp](https://api.tally.so/mcp)

5 source URLs. Raw sources field, verbatim:

https://tally.so/help/mcp, https://developers.tally.so/api-reference/mcp, https://tally.so/help/api, https://tally.so/pricing, https://api.tally.so/mcp

**Notes, verbatim from the file**
Probed 2026-09-07: POST of an MCP initialize to https://api.tally.so/mcp returned HTTP 401 with the text "Unauthorized"; the control POST to /zzz-not-a-route on api.tally.so returned the same 401 "Unauthorized". A 401 on both paths is an auth wall across the API host, not proof that /mcp is an MCP server; the vendor's two documentation pages naming the URL are the evidence. Of the three form builders added to this file on 2026-09-07 (Typeform, Jotform, Tally), Tally is the only one whose vendor states that both the API and the MCP are free on the free plan. 2026-09-07: https://api.tally.so/mcp returned 401 to an MCP initialize POST (https://api.tally.so/mcp).

**Provenance**

- **Entry id**: 14-tally

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 371

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
