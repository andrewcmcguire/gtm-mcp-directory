# Endgame: MCP server status, API access gate and what it does

> A GTM "context graph" platform that ingests calls, deals, emails, and documents into a queryable knowledge... Official MCP, Gate unknown. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Endgame

# Endgame

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.endgame.io/features/mcp-server](https://docs.endgame.io/features/mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://app.endgame.io/api/v1/mcp ; https://docs.endgame.io/features/mcp-server (endpoint https://app.endgame.io/api/v1/mcp)

- [https://app.endgame.io/api/v1/mcp](https://app.endgame.io/api/v1/mcp)
- [https://docs.endgame.io/features/mcp-server](https://docs.endgame.io/features/mcp-server)

**What this server exposes**

- **Tools named**: 26
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **create_digest** Set up a new recurring digest evidence: in the vendor docs · calling it writes

- **delete_digest** Delete a digest so it stops running evidence: in the vendor docs · calling it writes

- **download_skill_assets** Download a skill's supporting files evidence: in the vendor docs · calling it reads

- **find_graph_person** Resolve a person mentioned by name, email, or CRM ID evidence: in the vendor docs · calling it reads

- **get_digest** Load a single digest in full evidence: in the vendor docs · calling it reads

- **get_graph_citations** Open the sources behind a single piece of context-agent output evidence: in the vendor docs · calling it reads

- **get_graph_entities** Load the full record for one or more entities by ID evidence: in the vendor docs · calling it reads

- **get_graph_facts** List the facts known about a specific entity evidence: in the vendor docs · calling it reads

- **get_graph_field_catalog** Get your organization's field catalog evidence: in the vendor docs · calling it reads

- **get_graph_index** Get an overview of your organization's context graph evidence: in the vendor docs · calling it reads

- **get_graph_person** Load full detail for one or more people evidence: in the vendor docs · calling it reads

- **get_graph_relationships** Fetch the relationships of a single entity evidence: in the vendor docs · calling it reads

- **get_my_graph_profile** Resolve the current user to their graph profile evidence: in the vendor docs · calling it reads

- **get_org_rules** Load your organization's writing, style, policy, and product guidance evidence: in the vendor docs · calling it reads

- **list_digests** List your scheduled digests, including any that are paused evidence: in the vendor docs · calling it reads

- **list_graph_entities** Browse entities of a single type with property filters and ordering evidence: in the vendor docs · calling it reads

- **list_graph_relationships** List or aggregate relationships org-wide evidence: in the vendor docs · calling it reads

- **list_my_accounts** List the accounts you own or are assigned to evidence: in the vendor docs · calling it reads

- **list_skills** Discover the expert workflows your organization has authored evidence: in the vendor docs · calling it reads

- **read_skill** Load the full instructions for a specific skill evidence: in the vendor docs · calling it reads

- **search_graph_entities** Search the context graph by display name, graph ID, or source identifier evidence: in the vendor docs · calling it reads

- **search_graph_facts** Semantic search across extracted facts from meetings, emails, and documents evidence: in the vendor docs · calling it reads

- **search_graph_people** Search people by their relationship to accounts and companies evidence: in the vendor docs · calling it reads

- **tell_endgame** Correct or add to the context graph, and send feedback evidence: in the vendor docs · calling it writes

- **update_digest** Change an existing digest's configuration evidence: in the vendor docs · calling it reads

- **verified_sources** Display a verified-source footer alongside an answer evidence: in the vendor docs · calling it reads

119 of the 437 entries that record an official or community MCP server carry a harvested tool list. The other 318 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown/mixed. A self-serve "/signup" flow exists alongside "Get a demo" CTAs, and the docs note "rate limits ... may vary depending on your plan" without publishing any plan or pricing details - could not confirm whether MCP/API access is available below a paid or enterprise tier.

631 of 934 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

604 of 934 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to endgame.io with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: endgameinc, endgame-build, singularity, enqy, Endgame-Labs. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Research an account before a call](../jobs/research-account-for-call-prep.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 934 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://endgame.io](https://endgame.io)
- [https://docs.endgame.io](https://docs.endgame.io)
- [https://docs.endgame.io/features/mcp-server](https://docs.endgame.io/features/mcp-server)
- [https://app.endgame.io/api/v1/mcp](https://app.endgame.io/api/v1/mcp)

4 source URLs. Raw sources field, verbatim:

https://endgame.io, https://docs.endgame.io, https://docs.endgame.io/features/mcp-server, https://app.endgame.io/api/v1/mcp

**Notes, verbatim from the file**
DISAMBIGUATION - verified this is not an unrelated security- or gaming-branded "Endgame"; endgame.io's own case studies (Handle, Monte Carlo, BetterUp, Hex) and GTM-agent framing confirm it is a revenue-intelligence company. However, its current positioning (calls/deals/emails/documents -> context graph) reads as closer to conversation-intelligence/account-context than to a PLG product-usage-signal tool like Pocus/Correlated/Toplyne - the seed framing may reflect an earlier product stage; flagging for whoever updates this entry next. [api_gate 2026-08-25] Re-checked and left unknown, honestly: no pricing page exists (endgame.io/pricing 404s) though a self-serve sign-up is offered; the docs describe an MCP server and API keys with the only stated limit being that only Endgame admins can create API keys, and no tier condition is published. Checked against https://docs.endgame.io/features/mcp-server. 2026-09-07: https://app.endgame.io/api/v1/mcp returned 401 to an MCP initialize POST (https://app.endgame.io/api/v1/mcp).

**Provenance**

- **Entry id**: 14-endgame

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 122

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
