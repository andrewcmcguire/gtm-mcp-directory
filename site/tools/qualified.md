# Qualified: MCP server status, API access gate and what it does

> Website chat/pipeline-generation platform built for account-based and inbound motions - its "Piper" AI SDR... No MCP found, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Qualified

# Qualified

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [qualified.com](https://qualified.com) · entry id 14-qualified · source 14-inbound-plg-chat.md line 7

**What it does**
Website chat/pipeline-generation platform built for account-based and inbound motions - its "Piper" AI SDR agent engages known target-account visitors in real time, qualifies them, and books meetings, then follows up over email and Slack.

**AI features, separated from automation with an AI label on it**
Piper is marketed as a full AI SDR agent across five modules (Conversations, Email, Meetings, Offers, Slack) that holds live text/voice/video conversations with site visitors and personalizes outreach using CRM/intent data, plus an "Agentic Product-Led Growth" mode for converting free-trial users. All vendor-described; no independent verification of the underlying model or methodology was found.

**RevOps role**
ABM-aligned inbound chat/qualification layer, positioned as an AI SDR for known target accounts rather than a general-purpose support widget.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 1 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

none shipped. The vendor announced on 2026-07-15 that it is "building a Qualified Model Context Protocol (MCP) client and server" so Piper can communicate with other Agentforce agents, with an availability target of Q3 2026: https://www.qualified.com/plus/articles/qualified-agentforce-better-together. No endpoint, docs page, or registry listing exists as of 2026-08-25. Re-check this one.

- [https://www.qualified.com/plus/articles/qualified-agentforce-better-together](https://www.qualified.com/plus/articles/qualified-agentforce-better-together)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only. No public self-serve pricing exists: the pricing page lists three tiers (Premier, Enterprise, Ultimate), all gated behind "Schedule a demo," and "Enterprise-Grade APIs" is explicitly reserved for the Enterprise tier and above. Third-party integration docs (Hightouch) confirm the practical gate, requiring an API key "generated with access to the Enterprise bulk endpoints."

**API documentation**

[https://www.qualified.com/api](https://www.qualified.com/api)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)
- [Book a meeting](../jobs/book-a-meeting.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Score and prioritize leads](../jobs/score-and-prioritize-leads.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Qualified (Piper)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: No MCP found

- **Gate there**: Enterprise only

- **Source**: 04-ai-sdr-agents.md line 49

- **Canonical page**: [Qualified](../tools/qualified.md)

What that listing says it does: A conversational AI agent ("Piper") that engages inbound website visitors in real time (text/voice/video chat), sends follow-up nurture emails, and books meetings for qualified visitors.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://qualified.com/](https://qualified.com/)
- [https://qualified.com/pricing](https://qualified.com/pricing)
- [https://qualified.com/api](https://qualified.com/api)
- [https://www.qualified.com/plus/articles/qualified-agentforce-better-together](https://www.qualified.com/plus/articles/qualified-agentforce-better-together)
- [https://www.qualified.com/plus/articles/6-key-ways-to-use-the-qualified-reporting-api](https://www.qualified.com/plus/articles/6-key-ways-to-use-the-qualified-reporting-api)

5 source URLs. Raw sources field, verbatim:

https://qualified.com/, https://qualified.com/pricing, https://qualified.com/api, https://www.qualified.com/plus/articles/qualified-agentforce-better-together, https://www.qualified.com/plus/articles/6-key-ways-to-use-the-qualified-reporting-api

**Notes, verbatim from the file**
CANONICAL ENTRY for Qualified (per INDEX.md). The 04-ai-sdr-agents.md entry is a cross-reference pointer only; fact fixes land here first. Checked GitHub, mcp.so, glama.ai, and PulseMCP for a Qualified MCP server: the only near-match (a community "Lead Qualifier" server) is an unrelated third-party tool named for its generic function, not affiliated with Qualified.com, and is not counted as this vendor's MCP. An announced roadmap server is not a shipped server, so mcp_status stays none-found. Name-collision warning: docs.qualified.io (Qualified.io, a developer-assessment company) is a different company from qualified.com; several search engines conflate the two. The docs_url above is a JS-rendered app, so it does not fetch as static text, but it is the vendor's stated developer entry point. 2026-09-02: re-checked. https://www.qualified.com/llms.txt has no MCP mention, the official MCP registry has no qualified entry, a web search finds only the unrelated Piper TTS server, and the 2026-07-15 announcement still reads "An MCP client and server to share context across agents in real time, available Q3 2026" with no endpoint or docs. Q3 has not closed; still none-found. Re-check after 2026-10-01.

**Provenance**

- **Entry id**: 14-qualified

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 7

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
