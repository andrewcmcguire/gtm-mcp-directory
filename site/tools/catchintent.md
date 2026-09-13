# CatchIntent: MCP server status, API access gate and what it does

> A B2B intent tool that monitors social and web sources for buying signals, ranks the people behind them by... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
CatchIntent

# CatchIntent

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [catchintent.com](https://catchintent.com) · entry id 05-catchintent · source 05-signals-intent-abm.md line 668

**What it does**
A B2B intent tool that monitors social and web sources for buying signals, ranks the people behind them by warmth, enriches the profiles and drafts personalised openers, then pushes leads to a CRM or outreach account.

**AI features, separated from automation with an AI label on it**
The vendor names "Bedrock-powered enrichment" to fill buyer profiles and AI-drafted openers matching brand voice; the signal detection itself is listening plus ranking. Its changelog frames the MCP server as the agent surface: "Connect Claude, Cursor, or any MCP-compatible AI tool to your CatchIntent workspace."

**RevOps role**
A signal-to-outreach layer for small teams: social-listening intent in, ranked warm leads with drafted openers out, feeding a CRM or a sequencer.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The vendor's MCP page states "One-time OAuth 2.1 authorization. Your MCP client opens a browser, you sign into CatchIntent, pick the workspace, and approve the requested scopes."

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://engine.catchintent.com/mcp (vendor page: https://catchintent.com/mcp; changelog v3.0.0 dated 2026-05-13: https://catchintent.com/changelog/) ; repo https://github.com/CatchIntent/skills

- [https://engine.catchintent.com/mcp](https://engine.catchintent.com/mcp)
- [https://catchintent.com/mcp](https://catchintent.com/mcp)
- [https://catchintent.com/changelog/](https://catchintent.com/changelog/)
- [https://github.com/CatchIntent/skills](https://github.com/CatchIntent/skills)

**What this server exposes**

- **Tools named**: 14
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **lead_enrich** Trigger full LinkedIn profile enrichment via Apify (~$0.002, idempotent). evidence: answered tools/list · calling it reads · required: leadId

- **lead_get** Get full details of one lead: profile, discovery context (fit reason, pain hypothesis, role signals, disqualifiers), the AI-drafted outreach sequence (lead.outreach), warmth score, and status. evidence: answered tools/list · calling it reads · required: leadId

- **lead_push_to_crm** Push leads to your connected CRM (HubSpot, Close, Pipedrive, Zoho). Each lead becomes a contact / deal in the destination. Lead status does not change automatically - call lead_update_status to mark as `pushed` once CRM confirms. evidence: answered tools/list · calling it writes · required: leadIds

- **lead_regenerate_sequence** Re-draft the lead's AI outreach sequence (LinkedIn/X steps). Optional instructions steer the rewrite. Capped per lead - edit directly once the cap is hit. evidence: answered tools/list · calling it reads · required: leadId

- **lead_search** Search leads in the workspace. A lead is always a person discovered on LinkedIn. Filter by warmth, status, or text. evidence: answered tools/list · calling it reads

- **lead_update_sequence** Replace the lead's outreach sequence steps with edited versions (marks the sequence as edited). evidence: answered tools/list · calling it reads · required: leadId, steps

- **lead_update_status** Move a lead through the triage funnel. Valid transitions: NEW → SEEN/SAVED/PUSHED/ARCHIVED, SEEN ↔ SAVED, SAVED → PUSHED/ARCHIVED, PUSHED → ARCHIVED, ARCHIVED → SEEN. PUSHED is irreversible - it marks handoff to an outreach tool / CRM. evidence: answered tools/list · calling it writes · required: leadId, status

- **product_create** Create a new product. You can set sell (name/description/keywords/competitors), the structured offer, voice, and reach (roles/seniority/functions). Company firmographics (industries/size/country) are set in the dashboard, not here. Brand fi evidence: answered tools/list · calling it writes · required: name

- **product_delete** Delete a product. Fails only if it's the workspace's only product. Its audience and leads cascade-delete. evidence: answered tools/list · calling it writes · required: productId

- **product_get** Resolved brand profile for a product, returned as nested sections with human-readable labels: sell (name/description/keywords/competitors/offer), fit (company firmographics), reach (roles/seniority/functions), plus offer, voice, and domain. evidence: answered tools/list · calling it reads · required: productId

- **product_list** List every product/brand tracked by this workspace. Each product has its own brand profile, audience, and leads. Returns id, name, and timestamps. evidence: answered tools/list · calling it reads

- **product_update** Update a product. Partial - only provided fields change. You can set sell (name/description/keywords/competitors), the structured offer, voice, and reach (roles/seniority/functions). Company firmographics (industries/size/country) are set... evidence: answered tools/list · calling it writes · required: productId

- **workspace_icp_options** Get the valid Seniority Level and Job Function labels for product targeting (the reach dimensions MCP can set; roles are free text). Call this before product_update - unknown labels are rejected, never silently dropped. evidence: answered tools/list · calling it reads

- **workspace_usage** Current workspace usage vs plan limits: leads delivered this billing period, team members, products, AI compute budget, daily/monthly caps. evidence: answered tools/list · calling it spends money

119 of the 239 entries that record an official or community MCP server carry a harvested tool list. The other 120 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor's MCP page states "MCP access is included on every plan, Growth, Scale, and Enterprise. The free 7-day trial includes full MCP access." The pricing page lists Growth (1,000 leads/month), Scale (4,000 leads/month) and Enterprise (25,000+ leads/month) without dollar figures, plus a Done-for-You service "Starting at $1,999/mo, 3-month minimum"; "Card on file is required" for the trial. No free plan.

**API documentation**

No documentation URL recorded.

347 of 422 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/CatchIntent/skills](https://github.com/CatchIntent/skills)

**On GitHub**

[github.com/CatchIntent](https://github.com/CatchIntent) tied to the vendor by rule 3, account website https://catchintent.com has the vendor's domain, confidence strong

- **Public repositories**: 1, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-06-30

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [skills](https://github.com/CatchIntent/skills) | other | 📡 The intent layer for B2B outbound. | 0 | 2026-06-30 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

151 of 422 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://catchintent.com/mcp](https://catchintent.com/mcp)
- [https://catchintent.com/changelog/](https://catchintent.com/changelog/)
- [https://catchintent.com/pricing](https://catchintent.com/pricing)
- [https://engine.catchintent.com/mcp](https://engine.catchintent.com/mcp)

4 source URLs. Raw sources field, verbatim:

https://catchintent.com/mcp, https://catchintent.com/changelog/, https://catchintent.com/pricing, https://engine.catchintent.com/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://engine.catchintent.com/mcp with no credentials returned HTTP 200 with a JSON-RPC result, serverInfo name "catchintent" version "2.0.0"; the control POST to /zzz-not-a-route returned 404 with a JSON body reading "Cannot POST /zzz-not-a-route". Live first-party server; initialize is open and the OAuth gate sits at tool-call time. The vendor's own MCP page says "28+ typed tools across six surfaces" while the v3.0.0 changelog line says "27 typed tools"; both vendor figures are recorded as found, not reconciled. The pricing page publishes plan sizes but no plan prices, so the api_gate is paid on the vendor's own statement that every plan is paid, with the amount unknown. The catchintent.com/mcp page is not linked from the homepage; it was reached via the registry listing that named the endpoint. 2026-09-07: https://engine.catchintent.com/mcp returned 200 with a JSON-RPC initialize result to an MCP initialize POST (https://engine.catchintent.com/mcp). 2026-09-12 (P6-04 repo sweep): first-party repository recorded at https://github.com/CatchIntent/skills - first-party agent skills that wire the hosted server, NOT the server source. Evidence: the org CatchIntent, whose profile site is catchintent.com, and whose README install line is "claude mcp add catchintent --transport http https://engine.catchintent.com/mcp", which is the endpoint this entry already records.

**Provenance**

- **Entry id**: 05-catchintent

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 668

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
