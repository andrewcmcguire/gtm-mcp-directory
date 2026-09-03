# Amplemarket: MCP server status, API access gate and what it does

> An all-in-one sales engagement platform that finds leads, runs multichannel outbound sequences... Official MCP, Enterprise leaning. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Amplemarket

# Amplemarket

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [amplemarket.com](https://amplemarket.com) · entry id 02-amplemarket · source 02-engagement-outbound.md line 445

**What it does**
An all-in-one sales engagement platform that finds leads, runs multichannel outbound sequences (email/social/phone/voice), and optimizes email deliverability.

**AI features, separated from automation with an AI label on it**
Vendor markets "Duo Copilot" as an AI sales agent - generative personalization/objection handling in outreach copy, AI-driven signal detection across job changes/reviews/social/website visits, AI voice cloning for personalized voice notes, and AI company research/copywriting. Vendor-stated only; independent verification of what is genuinely ML-driven vs. templated was not possible from public sources.

**RevOps role**
Outbound execution layer (sequencing, deliverability, unified inbox) that would sit downstream of a data/enrichment source, feeding activity data into a CRM.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 sign-in with the Amplemarket account in the browser; the knowledge article says no API keys are needed. Rate limit 100 requests per minute per user.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-03, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-03 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server (endpoint https://mcp.amplemarket.com/mcp; product page https://www.amplemarket.com/mcp)

- [https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server](https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server)
- [https://mcp.amplemarket.com/mcp](https://mcp.amplemarket.com/mcp)
- [https://www.amplemarket.com/mcp](https://www.amplemarket.com/mcp)

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning (any customer can self-generate a key at Settings > API, but there is no card checkout - every tier's CTA is a sales form and the lowest published tier is Startup at $600/mo annual)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)
- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Amplemarket (Duo Copilot)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: Official MCP

- **Gate there**: Paid, self-serve

- **Source**: 04-ai-sdr-agents.md line 410

- **Canonical page**: [Amplemarket](../tools/amplemarket.md)

What that listing says it does: An all-in-one sales platform (lead gen + multichannel engagement + deliverability) with an AI agent layer ("Duo Copilot") that detects buying signals, writes and A/B-tests email copy (including AI voice-cloned voice notes), runs multichannel sequences, and suggests meeting follow-ups.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.amplemarket.com/](https://www.amplemarket.com/)
- [https://glama.ai/mcp/servers?query=amplemarket](https://glama.ai/mcp/servers?query=amplemarket)
- [https://www.amplemarket.com/pricing](https://www.amplemarket.com/pricing)
- [https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server](https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server)
- [https://www.amplemarket.com/mcp](https://www.amplemarket.com/mcp)

5 source URLs. Raw sources field, verbatim:

https://www.amplemarket.com/, https://glama.ai/mcp/servers?query=amplemarket, https://www.amplemarket.com/pricing, https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server, https://www.amplemarket.com/mcp

**Notes, verbatim from the file**
No public API/developer-docs page was found (an /api path 404'd, help-center subdomain unreachable) - could not confirm whether a general-purpose API exists at all. The one MCP hit indexed under Amplemarket's name (glama.ai/mcp/servers/artem-amplemarket/amplemarket-pylon-mcp) only searches Amplemarket's Pylon-hosted help-center articles, not the sales platform - not counted as a product MCP. [api_gate 2026-08-25] Reclassified unknown -> enterprise-leaning from the vendor's own page (https://www.amplemarket.com/pricing): any customer can self-generate a key at Settings > API, but there is no card checkout - every tier's CTA is a sales form and the lowest published tier is Startup at $600/mo annual. 2026-09-02: mcp_status none-found -> official, reconciled with the Amplemarket (Duo Copilot) entry in 04-ai-sdr-agents.md, which already recorded it. The help-center subdomain is reachable now: https://knowledge.amplemarket.com/articles/8022685319-connecting-to-the-amplemarket-mcp-server returned 200 and documents the endpoint https://mcp.amplemarket.com/mcp (OAuth 2.0 sign-in, no API keys; Claude, ChatGPT, Claude Code, Cursor and any remote-capable client; prospect search, enrichment, sequences, lead lists, workflows, analytics; enrichment via MCP costs 0.5 credits). The endpoint answered 401 with a Bearer challenge today, which is the expected behaviour of an OAuth-gated MCP server. https://www.amplemarket.com/mcp links to the same guide.

**Provenance**

- **Entry id**: 02-amplemarket

- **Source file**: 02-engagement-outbound.md

- **Source line**: 445

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
