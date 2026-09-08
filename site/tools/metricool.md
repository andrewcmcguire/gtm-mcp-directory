# Metricool: MCP server status, API access gate and what it does

> A social media management and analytics tool (scheduling, analytics, competitor tracking and ad-campaign... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Metricool

# Metricool

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-09-07
CLI: metricool (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [metricool.com](https://metricool.com) · entry id 15-metricool · source 15-community-dark-social.md line 350

**What it does**
A social media management and analytics tool (scheduling, analytics, competitor tracking and ad-campaign monitoring across Instagram, Facebook, X, LinkedIn, TikTok, YouTube and Meta, Google and TikTok Ads) for brands and agencies.

**AI features, separated from automation with an AI label on it**
The MCP server exposes 20 or more tools (get_analytics, get_metrics, post_schedule_post, update_schedule_post, get_network_competitors and per-network content reads) to whatever agent connects; the vendor's own AI copy assistance in the composer was not verified this pass. The analytics and scheduling core is not AI.

**RevOps role**
The social publishing and listening layer of dark-social GTM; an agent can read post and competitor analytics and schedule posts from the same connector.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth (browser authorisation in clients that support remote OAuth MCP) or a METRICOOL_USER_TOKEN plus METRICOOL_USER_ID header pair from account settings (used for n8n and the local Python package).

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://ai.metricool.com/mcp (docs: https://help.metricool.com/how-to-connect-metricools-mcp-eqp9h; FAQ: https://help.metricool.com/faqs-about-the-metricool-mcp-1i3w0; open-source local server: https://github.com/metricool/mcp-metricool)

- [https://ai.metricool.com/mcp](https://ai.metricool.com/mcp)
- [https://help.metricool.com/how-to-connect-metricools-mcp-eqp9h](https://help.metricool.com/how-to-connect-metricools-mcp-eqp9h)
- [https://help.metricool.com/faqs-about-the-metricool-mcp-1i3w0](https://help.metricool.com/faqs-about-the-metricool-mcp-1i3w0)
- [https://github.com/metricool/mcp-metricool](https://github.com/metricool/mcp-metricool)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. The full roll up is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: metricool
- **Status**: community CLI, third party
- **Strongest evidence**: github
- **Harvested**: 2026-09-08

No install command was quoted by the harvest. The status rests on the package or page linked below.

23 subcommands seen with the binary in the docs or README:
expand to read them

ads, agency, ai, analytics, best-time, brand, brands, calendar, competitors, counters, dashboard, gif, hashtags, inbox, library, media, ping, post, reports, smartlinks, subscription, suggestions, user

Where it was documented:

- [https://github.com/Purple-Horizons/metricool-cli](https://github.com/Purple-Horizons/metricool-cli) (the repository that documented it)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-08.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (for MCP) - the vendor FAQ states "MCP is an AI client connector for natural language. It works on any plan, including Free. The Metricool API is for programmatic HTTP access and is available only on Advanced and Custom." The pricing page lists Free $0, Starter from about $16 to $20/month, Advanced from about $43 to $67/month (currency dependent) and Custom, and its feature table shows "Metricool API (Zapier, Make, and MCP)" as an Advanced-and-above line.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/metricool/mcp-metricool](https://github.com/metricool/mcp-metricool)

**On GitHub**

[github.com/metricool](https://github.com/metricool) tied to the vendor by rule 2, account website https://metricool.com has the vendor's domain, confidence strong

- **Public repositories**: 0, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: not recorded

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://help.metricool.com/how-to-connect-metricools-mcp-eqp9h](https://help.metricool.com/how-to-connect-metricools-mcp-eqp9h)
- [https://help.metricool.com/faqs-about-the-metricool-mcp-1i3w0](https://help.metricool.com/faqs-about-the-metricool-mcp-1i3w0)
- [https://metricool.com/pricing/](https://metricool.com/pricing/)
- [https://www.metricool.com/mcp/](https://www.metricool.com/mcp/)
- [https://ai.metricool.com/mcp](https://ai.metricool.com/mcp)

5 source URLs. Raw sources field, verbatim:

https://help.metricool.com/how-to-connect-metricools-mcp-eqp9h, https://help.metricool.com/faqs-about-the-metricool-mcp-1i3w0, https://metricool.com/pricing/, https://www.metricool.com/mcp/, https://ai.metricool.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://ai.metricool.com/mcp returned HTTP 401 with JSON reading "This endpoint requires authentication"; the control POST to /zzz-not-a-route returned 404 with a JSON body naming the path. Live first-party auth-gated server. The vendor's own pages disagree on the gate: the help-centre FAQ says MCP "works on any plan, including Free" and only the HTTP API needs Advanced, while the pricing page's feature table lists "Metricool API (Zapier, Make, and MCP)" under Advanced and above. Both statements are recorded; the api_gate follows the FAQ, which is the more specific page, and the pricing-table line is flagged as the contradiction a buyer should test on a Free account. The www.metricool.com/mcp/ page served in Spanish on this date. 2026-09-07: https://ai.metricool.com/mcp returned 401 to an MCP initialize POST (https://ai.metricool.com/mcp).

**Provenance**

- **Entry id**: 15-metricool

- **Source file**: 15-community-dark-social.md

- **Source line**: 350

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
