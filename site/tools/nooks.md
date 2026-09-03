# Nooks: MCP server status, API access gate and what it does

> AI parallel dialer and "virtual salesfloor" combining multi-line dialing, live manager coaching, and... Official MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Nooks

# Nooks

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [nooks.ai](https://nooks.ai) · entry id 02-nooks · source 02-engagement-outbound.md line 45

**What it does**
AI parallel dialer and "virtual salesfloor" combining multi-line dialing, live manager coaching, and prospecting assistance for SDR teams.

**AI features, separated from automation with an AI label on it**
Genuinely AI: sub-0.5-second pickup detection that filters voicemail/dead air across up to 5 parallel lines, AI call summaries/dispositions, AI roleplay-coaching bots trained on real call recordings, and "AI Prospector" for buying-signal detection and email drafting. Plain automation: the multi-line dialing mechanism itself, waterfall phone-number enrichment, and local-presence number rotation. Live "whisper coaching" is a human-manager feature, not AI.

**RevOps role**
Outbound calling execution and coaching layer, typically integrated with Salesforce/HubSpot and enrichment providers.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 authorization code with PKCE (S256), issuer https://oauth.nooks.in, per the server's own /.well-known/oauth-authorization-server metadata; a third-party listing reports 'Requires Login'. No vendor docs found.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp.nooks.in/mcp](https://mcp.nooks.in/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.nooks.in/mcp (no public docs page found; OAuth metadata at https://mcp.nooks.in/.well-known/oauth-authorization-server)

- [https://mcp.nooks.in/mcp](https://mcp.nooks.in/mcp)
- [https://mcp.nooks.in/.well-known/oauth-authorization-server](https://mcp.nooks.in/.well-known/oauth-authorization-server)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (pricing is quote-only; self-serve OAuth app creation exists but requires workspace admin plus a Nooks Sequencing or Coaching seat)

**API documentation**

[https://developer.nooks.in/](https://developer.nooks.in/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/NooksApp](https://github.com/NooksApp)

**Jobs it can do**

- [Find a phone number](../jobs/find-phone-number.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Score rep performance](../jobs/score-rep-performance.md)
- [Run a sales roleplay practice](../jobs/run-sales-roleplay-practice.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.nooks.ai/ai-dialer](https://www.nooks.ai/ai-dialer)
- [https://www.nooks.ai/ai-sequencing](https://www.nooks.ai/ai-sequencing)
- [https://www.nooks.ai/pricing](https://www.nooks.ai/pricing)
- [https://developer.nooks.in/](https://developer.nooks.in/)
- [https://github.com/NooksApp](https://github.com/NooksApp)
- [https://pipeline.zoominfo.com/sales/nooks-ai-zoominfo-gtm-ai-integration](https://pipeline.zoominfo.com/sales/nooks-ai-zoominfo-gtm-ai-integration)
- [https://mcp.nooks.in/.well-known/oauth-authorization-server](https://mcp.nooks.in/.well-known/oauth-authorization-server)
- [https://tedix.dev/apps/nooks/](https://tedix.dev/apps/nooks/)
- [https://www.linkedin.com/pulse/nooks-product-release-mcp-servers-bonus-numbers-dialing-jortberg-gjjsc](https://www.linkedin.com/pulse/nooks-product-release-mcp-servers-bonus-numbers-dialing-jortberg-gjjsc)

9 source URLs. Raw sources field, verbatim:

https://www.nooks.ai/ai-dialer, https://www.nooks.ai/ai-sequencing, https://www.nooks.ai/pricing, https://developer.nooks.in/, https://github.com/NooksApp, https://pipeline.zoominfo.com/sales/nooks-ai-zoominfo-gtm-ai-integration, https://mcp.nooks.in/.well-known/oauth-authorization-server, https://tedix.dev/apps/nooks/, https://www.linkedin.com/pulse/nooks-product-release-mcp-servers-bonus-numbers-dialing-jortberg-gjjsc

**Notes, verbatim from the file**
No MCP server found on GitHub, mcp.so, glama.ai, or pulsemcp.com (pulsemcp returned zero results). A developer.nooks.in portal with OAuth2/API keys exists, but the pricing page only offers custom quotes with no disclosed API tier; the custom-quote sales motion suggests enterprise-leaning access, but that is inference, not a confirmed fact. RE-CHECKED 2026-08-25 on a specific pointer that Nooks had shipped something in the MCP/agent space. What was found is not a Nooks MCP server: it is Nooks positioning itself as an "Agent Workspace for Intelligent Outbound" (AI Dialing Assistant, AI Coaching Assistant, AI Prospector, AI Sequencing) and a native bidirectional integration with ZoomInfo's GTM.AI context layer, where mutual customers connect a ZoomInfo entitlement to Nooks through a native connector and Nooks engagement signals flow back through a Custom Data Connector inside ZoomInfo's GTM Studio. ZoomInfo's own write-up does not state whether Nooks consumes GTM.AI over MCP or over REST, and does not claim Nooks exposes an MCP server of its own. So Nooks is an MCP *consumer* story at best, not an MCP provider; mcp_status stays none-found. If Nooks ships a first-party server this is the entry to update. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.nooks.ai/pricing): pricing is quote-only; self-serve OAuth app creation exists but requires workspace admin plus a Nooks Sequencing or Coaching seat. 2026-09-02: CHANGED none-found -> official. A first-party endpoint answers at https://mcp.nooks.in/mcp (HTTP 405 to a plain GET, the expected response of a streamable-HTTP MCP server that only accepts POST) and https://mcp.nooks.in/.well-known/oauth-authorization-server returns OAuth metadata with issuer https://oauth.nooks.in, authorization, token and revocation endpoints, authorization-code flow and PKCE S256. The pointer came from a LinkedIn release note titled 'Nooks Product Release: MCP Servers, Bonus Numbers, Dialing' (login-walled, not read) and a third-party listing at tedix.dev/apps/nooks that names the same endpoint and reports 'Requires Login'. CAVEAT: developer.nooks.in, nooks.ai/llms.txt and a site search of nooks.ai contain no MCP documentation, the MCP registry returns nothing for nooks, and tedix reports protocol-handshake failures, so tools, scopes and plan gating are unverified. Official on the strength of a vendor-domain endpoint that answers; needs a hands-on connect before use on camera.

**Provenance**

- **Entry id**: 02-nooks

- **Source file**: 02-engagement-outbound.md

- **Source line**: 45

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
