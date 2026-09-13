# Skyp.ai: MCP server status, API access gate and what it does

> A cold-email outreach platform (campaigns, contacts, per-prospect AI-written emails, tracking, webhooks) that... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Skyp.ai

# Skyp.ai

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [skyp.ai](https://skyp.ai) · entry id 02-skyp-ai · source 02-engagement-outbound.md line 619

**What it does**
A cold-email outreach platform (campaigns, contacts, per-prospect AI-written emails, tracking, webhooks) that markets itself on being driven by AI agents through a native MCP server and REST API rather than through a UI.

**AI features, separated from automation with an AI label on it**
The vendor claims AI-generated personalised emails per prospect and pitches the MCP as the full campaign lifecycle for agents; eight tools are listed on the vendor's MCP page: create_new_campaign, add_contact_to_existing_campaign, get_campaign_details, update_existing_campaign, list_campaigns, create_new_contact, get_account_analytics, get_campaign_threads.

**RevOps role**
A sequencer built to be operated by an agent: campaigns and contacts in via MCP, replies and results out via webhook.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (X-API-Key or Authorization Bearer header) or OAuth. The endpoint's own 401 body reads "Missing credentials. Use X-API-Key or Authorization: Bearer." and the protected-resource document lists authorization_servers ["https://api.skyp.ai"], scopes_supported ["mcp"] and bearer_methods_supported ["header"]. Keys are generated in the vendor's "Agents & API dashboard".

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.skyp.ai/mcp (vendor pages: https://skyp.ai/email-mcp-server and https://skyp.ai/developers; the OAuth protected-resource document at https://api.skyp.ai/.well-known/oauth-protected-resource/mcp names the resource)

- [https://api.skyp.ai/mcp](https://api.skyp.ai/mcp)
- [https://skyp.ai/email-mcp-server](https://skyp.ai/email-mcp-server)
- [https://skyp.ai/developers](https://skyp.ai/developers)
- [https://api.skyp.ai/.well-known/oauth-protected-resource/mcp](https://api.skyp.ai/.well-known/oauth-protected-resource/mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 396 entries that record an official or community MCP server carry a harvested tool list. The other 277 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - the vendor states "MCP access is included on every paid plan, Pro, Team, and Growth. No additional middleware, Workato connector, or Zapier account required." and "API and MCP are included, not an add-on". The pricing page lists Pro at $149/month and Team at $499/month (billed annually) and Growth at custom pricing. No free plan.

**API documentation**

No documentation URL recorded.

555 of 834 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/skyp-ai](https://github.com/skyp-ai) tied to the vendor by rule 3, account website https://skyp.ai has the vendor's domain, confidence strong

- **Public repositories**: 0, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: not recorded

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

563 of 834 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://skyp.ai/email-mcp-server](https://skyp.ai/email-mcp-server)
- [https://skyp.ai/developers](https://skyp.ai/developers)
- [https://skyp.ai/pricing](https://skyp.ai/pricing)
- [https://api.skyp.ai/.well-known/oauth-protected-resource/mcp](https://api.skyp.ai/.well-known/oauth-protected-resource/mcp)
- [https://api.skyp.ai/mcp](https://api.skyp.ai/mcp)

5 source URLs. Raw sources field, verbatim:

https://skyp.ai/email-mcp-server, https://skyp.ai/developers, https://skyp.ai/pricing, https://api.skyp.ai/.well-known/oauth-protected-resource/mcp, https://api.skyp.ai/mcp

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://api.skyp.ai/mcp returned HTTP 401 with JSON reading "Missing credentials. Use X-API-Key or Authorization: Bearer."; the control POST to /zzz-not-a-route returned 404 with JSON reading "Not Found". Live first-party auth-gated server. The endpoint URL does not appear on the vendor's MCP page or developers page, which link to a Swagger shell at api.skyp.ai/docs; it was recovered from the API's OpenAPI document (which lists /.well-known/oauth-protected-resource/mcp) and confirmed by that document's "resource" field. https://skyp.ai/mcp 308-redirects to the /email-mcp-server marketing page and https://app.skyp.ai/mcp is a 404. The vendor also publishes llms.txt with per-topic markdown pages. The candidate row's "endpoint in /developers" note was not borne out; the endpoint is in the API host's well-known document instead. 2026-09-07: https://api.skyp.ai/mcp returned 401 to an MCP initialize POST (https://api.skyp.ai/mcp).

**Provenance**

- **Entry id**: 02-skyp-ai

- **Source file**: 02-engagement-outbound.md

- **Source line**: 619

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
