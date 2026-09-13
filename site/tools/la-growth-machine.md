# La Growth Machine: MCP server status, API access gate and what it does

> Multi-channel prospecting platform that sequences outreach across LinkedIn, email, Twitter/X, and voice... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
La Growth Machine

# La Growth Machine

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [lagrowthmachine.com](https://lagrowthmachine.com) · entry id 02-la-growth-machine · source 02-engagement-outbound.md line 388

**What it does**
Multi-channel prospecting platform that sequences outreach across LinkedIn, email, Twitter/X, and voice notes/calls from one campaign builder, with built-in lead enrichment.

**AI features, separated from automation with an AI label on it**
"Magic Messages" (Pro/Ultimate plans) auto-generates message copy; "AI Comment Automation" posts contextual comments on a prospect's LinkedIn activity pre-connection; the Ultimate plan adds AI-personalized voice notes. Vendor-stated LLM-generation features, not independently verified.

**RevOps role**
Multichannel (LinkedIn-centric) outbound execution + enrichment layer that can be driven conversationally via its own open-source MCP/Claude-skills bundle.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - no API key needed; first use opens a browser sign-in directly to the user's La Growth Machine account.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/LaGrowthMachine/gtm-system ; https://lagrowthmachine.com/mcp-server/

- [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system)
- [https://lagrowthmachine.com/mcp-server/](https://lagrowthmachine.com/mcp-server/)

**What this server exposes**

- **Tools named**: 34
- **Strongest evidence**: in a README table
- **Harvested**: 2026-09-12
- **Repo read**: LaGrowthMachine/gtm-system
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **Skill** Type evidence: in a README table · calling it reads

- **add_campaign_step_message** Write the message for an empty campaign step evidence: in a README table · calling it writes

- **audience-icp-filter** Filters a CSV you paste - you re-import the segmented buckets by hand evidence: in a README table · calling it writes

- **campaign-challenger** Benchmarks against stats you paste evidence: in a README table · calling it reads

- **campaign-impact-analyzer** Works on pasted campaigns and deals evidence: in a README table · calling it reads

- **create_audience_from_linkedin_url** Build an audience from a LinkedIn / Sales Navigator search or a post's engagers evidence: in a README table · calling it writes

- **duplicate_campaign** Copy a campaign into an editable draft, without launching it evidence: in a README table · calling it reads

- **edit_campaign_message** Rewrite a campaign step's message evidence: in a README table · calling it reads

- **get_audience** Details and import status of an audience evidence: in a README table · calling it writes

- **get_audience_leads** Leads in an audience (name, company, title, email, LinkedIn) evidence: in a README table · calling it reads

- **get_campaign_messages** The message sequence of a campaign evidence: in a README table · calling it reads

- **get_campaign_stats** Acceptance, reply and conversion rates for a campaign evidence: in a README table · calling it reads

- **get_campaign_steps** The steps of a campaign sequence - channel, order, whether a message is attached evidence: in a README table · calling it reads

- **get_conversation_messages** The full message thread of a conversation evidence: in a README table · calling it reads

- **get_conversations_to_reply** Conversations waiting on your reply evidence: in a README table · calling it reads

- **get_favourite_conversations** Starred conversations evidence: in a README table · calling it reads

- **get_lead_conversations** A lead's conversations across channels evidence: in a README table · calling it reads

- **get_lead_logs** Activity log for a lead (sent, accepted, replied…) evidence: in a README table · calling it reads

- **get_linkedin_post** Read a LinkedIn post's content and engagement from its URL evidence: in a README table · calling it writes

- **get_unread_conversations** Unread conversations evidence: in a README table · calling it reads

- **list_campaigns** List your campaigns and their status evidence: in a README table · calling it reads

- **list_identities** Your connected LinkedIn / email identities evidence: in a README table · calling it reads

- **list_members** The members of your LGM account evidence: in a README table · calling it reads

- **multichannel-campaign-builder** Sequence ready to copy into your tool evidence: in a README table · calling it reads

- **objection-analyzer** Builds the playbook from a CSV export or threads you paste evidence: in a README table · calling it reads

- **post-to-campaign** Writes the outreach sequence from the post evidence: in a README table · calling it writes

- **reply-draft-assistant** Drafts answers for a conversation you paste evidence: in a README table · calling it reads

- **sales-nav-search-builder** Sales Nav URL to open and import manually evidence: in a README table · calling it writes

- **search_conversations** Filter the whole inbox (campaign, channel, date, status…) evidence: in a README table · calling it reads

- **send_email_message** Send an email, with thread-aware replies evidence: in a README table · calling it writes

- **send_linkedin_message** Send a LinkedIn message (text or voice note) evidence: in a README table · calling it writes

- **team-performance-dashboard** Needs the LGM MCP - the dashboard is built from live LGM data evidence: in a README table · calling it reads

- **weekly-performance-advisor** Needs the LGM MCP - the dashboard is built from live LGM data evidence: in a README table · calling it reads

- **won-deal-icp-finder** Works on a HubSpot export you paste evidence: in a README table · calling it reads

119 of the 740 entries that record an official or community MCP server carry a harvested tool list. The other 621 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

727 of 1251 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system)

**On GitHub**

[github.com/LaGrowthMachine](https://github.com/LaGrowthMachine) tied to the vendor by rule 1, account website https://lagrowthmachine.com/ has the vendor's domain, confidence strong

- **Public repositories**: 9, forks excluded, as read on 2026-09-08
- **Mention MCP**: 2 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [gtm-system](https://github.com/LaGrowthMachine/gtm-system) | MCP server | Open-source Claude skills and an MCP server for Sales and GTM teams: build Sales Navigator searches, write multichannel... | 36 | 2026-09-08 | |
| [lgm-web-comps](https://github.com/LaGrowthMachine/lgm-web-comps) | app | tests de séparation des compos figma | 0 | 2026-09-01 | |
| [n8n-templates](https://github.com/LaGrowthMachine/n8n-templates) | docs or examples | Ready-to-import n8n workflows for the official La Growth Machine node | 0 | 2026-08-11 | |
| [n8n-nodes-lagrowthmachine](https://github.com/LaGrowthMachine/n8n-nodes-lagrowthmachine) | plugin or integration | | 0 | 2026-08-11 | v1.0.4 |
| [lgm-mcp](https://github.com/LaGrowthMachine/lgm-mcp) | MCP server | MCP server exposing La Growth Machine (multichannel B2B outreach) to AI clients - Claude Desktop, Claude.ai, Cursor,... | 0 | 2026-07-23 | v1.4.2 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 1,251 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://lagrowthmachine.com/best-linkedin-automation-tools/](https://lagrowthmachine.com/best-linkedin-automation-tools/)
- [https://github.com/LaGrowthMachine/gtm-system](https://github.com/LaGrowthMachine/gtm-system)
- [https://lagrowthmachine.com/mcp-server/](https://lagrowthmachine.com/mcp-server/)

3 source URLs. Raw sources field, verbatim:

https://lagrowthmachine.com/best-linkedin-automation-tools/, https://github.com/LaGrowthMachine/gtm-system, https://lagrowthmachine.com/mcp-server/

**Notes, verbatim from the file**
API, Zapier, and CRM integrations are vendor-stated as available only on upper-tier plans (base plan starts ~$70/mo/identity, which reportedly excludes API). Notably the most "agent-native" tool in this category - ships an open-source repo bundling both Claude skills and an MCP server together, more mature agent tooling than most competitors here.

**Provenance**

- **Entry id**: 02-la-growth-machine

- **Source file**: 02-engagement-outbound.md

- **Source line**: 388

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
