# Offorte: MCP server status, API access gate and what it does

> Proposal software (templates, interactive web proposals, e-signature, open and read tracking, automation... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Proposals & Deals](../categories/proposals-deals.md) /
Offorte

# Offorte

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Proposals & Deals](../categories/proposals-deals.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [offorte.com](https://offorte.com) · entry id 13-offorte · source 13-proposals-deals.md line 281

**What it does**
Proposal software (templates, interactive web proposals, e-signature, open and read tracking, automation sets) for small businesses, with a REST API, webhooks and an MCP server published by the vendor.

**AI features, separated from automation with an AI label on it**
The vendor markets AI writing assistance for proposal text; the MCP server is the agent surface (17 tools across context, account, automations, contacts, favorites, proposals and settings) and a vendor blog post demonstrates a voice-to-sent-proposal flow through it.

**RevOps role**
A proposal-and-signature step at the bottom of the funnel for small teams; the MCP lets an agent create, fill and send a proposal from CRM context without opening the app.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key. The repo README lists an "Offorte API Key (see Authentication Section of the Offorte API Docs)"; the server runs locally with npx -y @offorte/mcp-server over stdio by default, with an SSE mode ("Set to sse to enable Server-Sent Events (SSE) mode, or leave unset/default for stdio").

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/offorte/offorte-mcp-server (vendor pages: https://www.offorte.com/for-developers and https://www.offorte.com/en/blog/proposal-software/handsfree-proposal-sending-with-mcp)

- [https://github.com/offorte/offorte-mcp-server](https://github.com/offorte/offorte-mcp-server)
- [https://www.offorte.com/for-developers](https://www.offorte.com/for-developers)
- [https://www.offorte.com/en/blog/proposal-software/handsfree-proposal-sending-with-mcp](https://www.offorte.com/en/blog/proposal-software/handsfree-proposal-sending-with-mcp)

**What this server exposes**

- **Tools named**: 15
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: offorte/offorte-mcp-server
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **create_contact** Create a new contact (organisation or person/individual) evidence: in the server source · calling it writes

- **create_proposal** Create a new proposal evidence: in the server source · calling it writes

- **get_account_users** Lists all account users for the current account evidence: in the server source · calling it reads

- **get_automation_sets** Lists automation sets which are used as an optional input to create a new proposal evidence: in the server source · calling it writes

- **get_contact_details** Get all details for a contact by id evidence: in the server source · calling it reads

- **get_design_templates** Lists available design templates which are used to create new proposals evidence: in the server source · calling it writes

- **get_email_templates** Lists available email templates which are used to send proposals evidence: in the server source · calling it writes

- **get_initial_context** IMPORTANT: This tool must be called before using any other tools. It will get usage instructions & Offorte context for this MCP server. evidence: in the server source · calling it reads

- **get_proposal_directories** Get all proposal directories grouped by status (edit, open, won, lost, closed) evidence: in the server source · calling it reads

- **get_proposal_templates** Lists proposal templates which are used as starting points to create new proposals evidence: in the server source · calling it writes

- **get_text_templates** Lists available language text templates which are used to create new proposals evidence: in the server source · calling it writes

- **search_contact_organisations** Search for organisations by name in the contacts evidence: in the server source · calling it reads

- **search_contact_people** Search for people by name in the contacts evidence: in the server source · calling it reads

- **search_proposals** Search for proposals by query evidence: in the server source · calling it reads

- **send_proposal** Send a proposal to its assigned contacts evidence: in the server source · calling it writes

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the pricing page states "A technical API is available with which programmers can control Offorte via code" under the Premium plan (from EUR 49/month for 5 users, EUR 390/year), which also lists "Create & send proposals via API", webhooks and Zapier; the Standard plan (from EUR 12.50/month, 1 user) does not list API access.

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/offorte/offorte-mcp-server](https://github.com/offorte/offorte-mcp-server)

**On GitHub**

[github.com/offorte](https://github.com/offorte) tied to the vendor by rule 1, account website https://www.offorte.com has the vendor's domain, confidence strong

- **Public repositories**: 2, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-04

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [show-doc](https://github.com/offorte/show-doc) | docs or examples | Create compact, readable HTML artifacts with Offorte ShowDoc components and Markdown | 1 | 2026-09-04 | show-doc-v0.0.3 |
| [offorte-mcp-server](https://github.com/offorte/offorte-mcp-server) | MCP server | MCP server for the Offorte API - Create & send proposals using AI | 5 | 2026-03-19 | v1.2.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

288 of 559 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://github.com/offorte/offorte-mcp-server](https://github.com/offorte/offorte-mcp-server)
- [https://www.offorte.com/en/pricing](https://www.offorte.com/en/pricing)
- [https://www.offorte.com/for-developers](https://www.offorte.com/for-developers)
- [https://www.offorte.com/en/blog/proposal-software/handsfree-proposal-sending-with-mcp](https://www.offorte.com/en/blog/proposal-software/handsfree-proposal-sending-with-mcp)

4 source URLs. Raw sources field, verbatim:

https://github.com/offorte/offorte-mcp-server, https://www.offorte.com/en/pricing, https://www.offorte.com/for-developers, https://www.offorte.com/en/blog/proposal-software/handsfree-proposal-sending-with-mcp

**Notes, verbatim from the file**
This is a repo-local server: there is no vendor-hosted MCP endpoint to probe, so no initialize POST was made on 2026-09-07. The repository sits under the offorte GitHub organisation and is linked from the vendor's own developer page, which meets the first-party test. MIT licensed, 28 commits on main at the time of reading; the vendor's June 2025 blog post notes the server "has only been tested with Claude Desktop". Pricing is published in EUR with no USD list.

**Provenance**

- **Entry id**: 13-offorte

- **Source file**: 13-proposals-deals.md

- **Source line**: 281

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
