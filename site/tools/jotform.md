# Jotform: MCP server status, API access gate and what it does

> An online form builder (forms, approvals, tables, e-sign, payment collection and conversational "AI Agents")... Official MCP, Free to start. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Jotform

# Jotform

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [jotform.com](https://jotform.com) · entry id 14-jotform · source 14-inbound-plg-chat.md line 352

**What it does**
An online form builder (forms, approvals, tables, e-sign, payment collection and conversational "AI Agents") with a REST API and a hosted MCP server.

**AI features, separated from automation with an AI label on it**
The vendor sells "AI Agents", conversational form-filling agents, capped at 5 active agents and 100 monthly conversations on the free Starter plan. The MCP server is a connectivity feature exposing five tools: list forms, create form, edit form, create submission, get submissions.

**RevOps role**
An intake and approvals form layer with payments and e-sign, sitting under lead routing; the MCP is read and write over forms and submissions.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth only. The vendor's MCP page states "Bearer-token access is not supported; OAuth 2.0 is required for all connections." Rate limits by plan: "60 requests per minute" on Free and "600 requests per minute" on Enterprise.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.jotform.com (docs: https://www.jotform.com/mcp/) ; repo https://github.com/jotform/mcp-server

- [https://mcp.jotform.com](https://mcp.jotform.com)
- [https://www.jotform.com/mcp/](https://www.jotform.com/mcp/)
- [https://github.com/jotform/mcp-server](https://github.com/jotform/mcp-server)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 521 entries that record an official or community MCP server carry a harvested tool list. The other 402 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the MCP page states "The Jotform MCP server is completely free to use, there are no additional charges beyond your existing Jotform subscription." The pricing page lists Starter "Free" ($0, 5 forms, 100 monthly submissions), Bronze "$39/month or $408/year", Silver "$49/month or $468/year", Gold "$129/month or $1,188/year" and Enterprise custom. The API docs give Starter "1000 requests per day" on an API key, rising to "100000 requests per day" on Gold, and "Jotform Enterprise has no limits to the number of daily API calls."

**API documentation**

No documentation URL recorded.

635 of 1032 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/jotform/mcp-server](https://github.com/jotform/mcp-server)

**On GitHub**

[github.com/jotform](https://github.com/jotform) tied to the vendor by rule 3, account website https://www.jotform.com has the vendor's domain, confidence strong

- **Public repositories**: 24, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [dnd-builder](https://github.com/jotform/dnd-builder) | other | | 57 | 2026-09-08 | v3.9.5 |
| [zenith](https://github.com/jotform/zenith) | other | Lightning-fast javascript monorepo build tool with remote/local caching ability /w pnpm | 16 | 2026-09-03 | v3.7.0 |
| [mobile-patches](https://github.com/jotform/mobile-patches) | app | | 0 | 2026-08-18 | |
| [wordpress-embed-plugin](https://github.com/jotform/wordpress-embed-plugin) | plugin or integration | Wordpress Embed | 1 | 2026-08-14 | |
| [wordpress-feedback-plugin](https://github.com/jotform/wordpress-feedback-plugin) | plugin or integration | WordPress Feedback | 1 | 2026-08-14 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

761 of 1,032 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.jotform.com/mcp/](https://www.jotform.com/mcp/)
- [https://www.jotform.com/pricing/](https://www.jotform.com/pricing/)
- [https://api.jotform.com/docs/](https://api.jotform.com/docs/)
- [https://mcp.jotform.com](https://mcp.jotform.com)

4 source URLs. Raw sources field, verbatim:

https://www.jotform.com/mcp/, https://www.jotform.com/pricing/, https://api.jotform.com/docs/, https://mcp.jotform.com

**Notes, verbatim from the file**
Probed 2026-09-07: POST of an MCP initialize to https://mcp.jotform.com (and to /mcp on the same host) returned HTTP 401 with JSON reading "NO_AUTH_HEADER"; the control POST to /zzz-not-a-route returned the same 401 NO_AUTH_HEADER. A 401 on both paths is an auth wall across the host, not proof that the root path speaks MCP; the vendor's own MCP page naming https://mcp.jotform.com as the server address is the evidence, and the probe is consistent with it without confirming it. The 401 body is the vendor's own error shape, not a CDN's, so the host is the vendor's. 2026-09-07: https://mcp.jotform.com returned 401 to an MCP initialize POST (https://mcp.jotform.com). 2026-09-12 (P6-04 repo sweep): first-party repository recorded at https://github.com/jotform/mcp-server - the server's own repository. Evidence: the org jotform, and the README reads "A Model Context Protocol (MCP) server for Jotform" and publishes the remote server URL https://mcp.jotform.com.

**Provenance**

- **Entry id**: 14-jotform

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 352

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
