# Onsa: MCP server status, API access gate and what it does

> Find scored B2B leads, read campaign replies and send approved LinkedIn outreach. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Onsa

# Onsa

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-12

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://api.onsa.ai/api/mcp](https://api.onsa.ai/api/mcp) · entry id 02-onsa · source 02-engagement-outbound.md line 3108

**What it does**
Find scored B2B leads, read campaign replies and send approved LinkedIn outreach.

**AI features, separated from automation with an AI label on it**
Not evidenced from fetched pages this pass; no AI feature claims recorded without a source URL.

**RevOps role**
Outbound engagement or dialer/sequencing layer used by sales teams

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://api.onsa.ai/api/mcp

- [https://api.onsa.ai/api/mcp](https://api.onsa.ai/api/mcp)

**What this server exposes**

- **Tools named**: 13
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-18
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **continue_campaign** Sends an instruction to the agent inside an existing campaign and returns a jobId to read with fetch_leads. This is the tool that grows or steers a cohort in place - 'find 5 more like these', 'look at Singapore and the Gulf instead of US in evidence: answered tools/list · calling it reads · required: campaignId, message

- **fetch_leads** Returns the status and any results of a find_leads job, by jobId. Status values: "pending" - the search is still running, though `leads` may already hold a partial list; "completed" - the agent delivered a batch, which is not a guarantee th evidence: answered tools/list · calling it reads · required: jobId

- **find_leads** Starts a live B2B lead search with Onsa's agent, matching real people (with LinkedIn profiles) against the workspace's ICP. Takes a natural-language brief - titles, company type, geography, e.g. 'find 5 fintech founders in NYC'. Returns a j evidence: answered tools/list · calling it reads · required: query

- **get_campaign** Returns one campaign's ICP - the ideal-customer profile the agent derived and scores leads against - plus its outreach template and settings. The ICP comes back exactly as stored, in snake_case: `perfect_lead` and `reachable_market` are one evidence: answered tools/list · calling it reads · required: campaignId

- **get_campaign_leads** Returns the leads of any campaign by campaignId, with the same fields as fetch_leads, including score and scoreExplanation. It covers campaigns not started in this session, which fetch_leads cannot reach because fetch_leads requires a jobId evidence: answered tools/list · calling it reads · required: campaignId

- **get_campaign_stats** Returns the outreach funnel for one campaign: invites sent, invites accepted, messages sent, and replies split into positive / negative / other by sentiment. LinkedIn and email are merged, as on Onsa's Overview page. These count leads rathe evidence: answered tools/list · calling it reads · required: campaignId

- **get_lead_memo** Returns the research memo Onsa's agent wrote about one lead: role history, company size and stage, what they have said publicly, and the angle on them. It is usually far richer than scoreExplanation, and it is the source material for outrea evidence: answered tools/list · calling it reads · required: leadId

- **list_campaigns** Lists the campaigns (past lead searches) in this workspace that the user takes part in, newest first. Returns the newest `limit` of them, default 50; `returned` against `total` shows whether older campaigns were omitted. Each entry has id, evidence: answered tools/list · calling it reads

- **list_next_steps** Returns what this campaign still needs from a human, as a ranked to-do list: people who replied, people who accepted an invite but were never messaged, drafts waiting for approval, leads found but never contacted, and setup that is missing. evidence: answered tools/list · calling it reads · required: campaignId

- **list_pending_outreach** Lists outreach messages the agent has drafted that are waiting for a human to approve - the 'a message for X is ready' queue. Each entry carries the draft text, the lead it is for, and why that lead scored as it did. Omitting campaignId cov evidence: answered tools/list · calling it reads

- **list_replies** Returns the text of what prospects replied, for every lead in the campaign that answered, paired with the outbound message it answers. get_campaign_stats counts replies and labels them; this returns the words. `sentiment` is Onsa's own labe evidence: answered tools/list · calling it reads · required: campaignId

- **rewrite_outreach** Replaces the text of an outreach draft that is waiting for approval. The current draft and the lead's scoreExplanation come from list_pending_outreach; get_lead_memo carries the richer research on that person. The rewritten draft stays in t evidence: answered tools/list · calling it reads · required: leadId, text

- **send_outreach** Queues one already-approved outreach draft for delivery to a real person on LinkedIn. It requires `confirmText`, the draft body character-for-character as stored, and `confirmName`, the recipient's name: drafts are often near-identical betw evidence: answered tools/list · calling it reads · required: leadId, confirmText, confirmName

140 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 601 are unmeasured, which is not the same as empty. Harvest last run 2026-09-18. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-18 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

727 of 1252 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to api.onsa.ai with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://api.onsa.ai/api/mcp](https://api.onsa.ai/api/mcp)

1 source URL. Thin. The standing rule is at least two independent sources with the vendor's own site unable to be both of them, and this entry does not meet it. 100 entries are in the same state and they are listed on the methodology page. Raw sources field, verbatim:

https://api.onsa.ai/api/mcp

**Notes, verbatim from the file**
Homepage fetch failed (HTTPError 401); what_it_does used staging desc. mcp_status=community from official-mcp-registry listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave T 2026-09-12.

**Provenance**

- **Entry id**: 02-onsa

- **Source file**: 02-engagement-outbound.md

- **Source line**: 3108

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-21

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
