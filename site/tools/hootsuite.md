# Hootsuite (Social OS): MCP server status, API access gate and what it does

> A social-media management suite split into four named products, each with its own MCP server: Perch for... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Community & Dark Social](../categories/community-dark-social.md) /
Hootsuite (Social OS)

# Hootsuite (Social OS)

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Community & Dark Social](../categories/community-dark-social.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [hootsuite.com](https://hootsuite.com) · entry id 15-hootsuite · source 15-community-dark-social.md line 330

**What it does**
A social-media management suite split into four named products, each with its own MCP server: Perch for content creation, planning and publishing, Nest for social inbox and customer care, Lumen for listening and insights, and Parliament for employee advocacy.

**AI features, separated from automation with an AI label on it**
"Wisdom" is the vendor's social-first AI layer across the suite, and the listening product is the Talkwalker technology Hootsuite acquired. The MCP servers themselves are access surfaces; the vendor's framing is that the chat client becomes the interface, so the reasoning happens in the AI tool rather than in Hootsuite.

**RevOps role**
The publishing, inbox and listening layer for a company-level social motion, and, unusually for this category, one where the listening data and the inbox are reachable by an agent through separate scoped servers rather than one blanket connection.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor's setup steps end with "Sign in with your Hootsuite workspace when prompted. Authorization is one-time."

- **Parsed URLs**: 5 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.hootsuite.com/perch, https://mcp.hootsuite.com/nest, https://mcp.hootsuite.com/lumen and https://mcp.hootsuite.com/parliament (docs: https://www.hootsuite.com/integrations/mcp)

- [https://mcp.hootsuite.com/perch](https://mcp.hootsuite.com/perch)
- [https://mcp.hootsuite.com/nest](https://mcp.hootsuite.com/nest)
- [https://mcp.hootsuite.com/lumen](https://mcp.hootsuite.com/lumen)
- [https://mcp.hootsuite.com/parliament](https://mcp.hootsuite.com/parliament)
- [https://www.hootsuite.com/integrations/mcp](https://www.hootsuite.com/integrations/mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's plans page states "Paid plans start at $99 for a Standard plan, $199 for a Professional plan, and range up to $399 for an Advanced plan", with Enterprise routed to "Contact for pricing", and offers a 14-day free trial that its own FAQ confirms needs no credit card and does not auto-charge. The MCP servers carry no separate price and no plan floor is published for them.

**API documentation**

No documentation URL recorded.

374 of 468 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/hootsuite](https://github.com/hootsuite) tied to the vendor by rule 3, account website code.hootsuite.com has the vendor's domain, confidence strong

- **Public repositories**: 12, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-07-28

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [copyable-macro](https://github.com/hootsuite/copyable-macro) | other | Copyable is a Swift Macro used to bring Kotlin's `copy` functionality to Swift. | 6 | 2026-07-28 | v1.1.0 |
| [embedded-apps-template](https://github.com/hootsuite/embedded-apps-template) | docs or examples | Embedded sample app | 0 | 2026-04-20 | |
| [token-ui](https://github.com/hootsuite/token-ui) | app | Text input components that allows to add 'tokens' rendered as pills. | 42 | 2026-03-10 | v8.3.4 |
| [nachos](https://github.com/hootsuite/nachos) | other | Material Chips for Android | 448 | 2025-12-16 | 2.0.0 |
| [hootsuite-app-express](https://github.com/hootsuite/hootsuite-app-express) | docs or examples | Sample Hootsuite app directory app using Express and Node.js | 0 | 2025-08-27 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

197 of 468 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.hootsuite.com/integrations/mcp](https://www.hootsuite.com/integrations/mcp)
- [https://www.hootsuite.com/plans](https://www.hootsuite.com/plans)
- [https://mcp.hootsuite.com/perch](https://mcp.hootsuite.com/perch)

3 source URLs. Raw sources field, verbatim:

https://www.hootsuite.com/integrations/mcp, https://www.hootsuite.com/plans, https://mcp.hootsuite.com/perch

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.hootsuite.com/perch returned HTTP 401 with {"error":"no_suitable_provider","error_description":"No OAuth provider is configured to handle this request"}, confirming a live OAuth-gated server; the other three addresses are printed on the same vendor page and follow the same pattern. FOUR SCOPED SERVERS, NOT ONE, which is the same governance pattern Zoho CRM uses in 06-revops-infra.md and is worth naming as an emerging design: an operator connects only the surface a task needs, so a listening agent never holds publishing rights. CROSS-FILE CORRECTION FLAGGED, NOT MADE: the Lumen server is the Talkwalker listening product, and this file already carries a separate "Talkwalker (Lumen by Talkwalker)" entry. Those two entries now describe overlapping products under two vendor names and should be reconciled by the directory maintainer, either as a declared cross-listing in INDEX.md or as a merge; that decision is editorial and is not made here. The vendor states setup is "no technical setup required" for ChatGPT and Claude via pre-built connectors, with a manual server-URL path for Gemini and Copilot. Publishing and inbox write access are both in scope, so an agent connected to Perch or Nest can post publicly and reply to customers. 2026-09-07: All four documented Social OS servers answered 401 to an MCP initialize POST: https://mcp.hootsuite.com/perch, /nest, /lumen and /parliament (https://mcp.hootsuite.com/perch).

**Provenance**

- **Entry id**: 15-hootsuite

- **Source file**: 15-community-dark-social.md

- **Source line**: 330

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
