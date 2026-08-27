# Endgame: MCP server status, API access gate and what it does

> A GTM "context graph" platform that ingests calls, deals, emails, and documents into a queryable knowledge... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Endgame

# Endgame

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [endgame.io](https://endgame.io) · entry id 14-endgame · source 14-inbound-plg-chat.md line 122

**What it does**
A GTM "context graph" platform that ingests calls, deals, emails, and documents into a queryable knowledge base for AI agents and reps - positioned today as broader account/revenue-intelligence infrastructure, not narrowly a PLG-product-signal tool.

**AI features, separated from automation with an AI label on it**
Combines a knowledge graph with cited, source-linked answers ("140x faster," "98% accuracy," "113,000+ answers" - vendor-stated, not independently verified) and an official MCP server exposing structured entity, people, facts/evidence, account-ownership, and org-policy data to AI assistants.

**RevOps role**
Account-context and revenue-intelligence layer for AI agents, disambiguated here from the narrower PLG-signal companies (Pocus, Correlated, Toplyne) it was grouped with in early research framing.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (browser-based) for individual users via Claude/ChatGPT/Claude Code/Codex connectors; Bearer-token service-account API keys (issued at app.endgame.io/settings/api-keys) for managed/agent use.

- **Parsed URLs**: 2 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://docs.endgame.io/features/mcp-server (endpoint https://app.endgame.io/api/v1/mcp)

- [https://docs.endgame.io/features/mcp-server](https://docs.endgame.io/features/mcp-server)
- [https://app.endgame.io/api/v1/mcp](https://app.endgame.io/api/v1/mcp)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown/mixed. A self-serve "/signup" flow exists alongside "Get a demo" CTAs, and the docs note "rate limits ... may vary depending on your plan" without publishing any plan or pricing details - could not confirm whether MCP/API access is available below a paid or enterprise tier.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Research an account before a call](../jobs/research-account-for-call-prep.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://endgame.io](https://endgame.io)
- [https://docs.endgame.io](https://docs.endgame.io)
- [https://docs.endgame.io/features/mcp-server](https://docs.endgame.io/features/mcp-server)

3 source URLs. Raw sources field, verbatim:

https://endgame.io, https://docs.endgame.io, https://docs.endgame.io/features/mcp-server

**Notes, verbatim from the file**
DISAMBIGUATION - verified this is not an unrelated security- or gaming-branded "Endgame"; endgame.io's own case studies (Handle, Monte Carlo, BetterUp, Hex) and GTM-agent framing confirm it is a revenue-intelligence company. However, its current positioning (calls/deals/emails/documents -> context graph) reads as closer to conversation-intelligence/account-context than to a PLG product-usage-signal tool like Pocus/Correlated/Toplyne - the seed framing may reflect an earlier product stage; flagging for whoever updates this entry next. [api_gate 2026-08-25] Re-checked and left unknown, honestly: no pricing page exists (endgame.io/pricing 404s) though a self-serve sign-up is offered; the docs describe an MCP server and API keys with the only stated limit being that only Endgame admins can create API keys, and no tier condition is published. Checked against https://docs.endgame.io/features/mcp-server.

**Provenance**

- **Entry id**: 14-endgame

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 122

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
