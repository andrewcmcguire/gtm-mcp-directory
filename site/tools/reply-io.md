# Reply.io: MCP server status, API access gate and what it does

> Multichannel sales engagement platform for email, LinkedIn, call, and SMS outreach with an AI SDR product... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Reply.io

# Reply.io

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [reply.io](https://reply.io) · entry id 02-reply-io · source 02-engagement-outbound.md line 179

**What it does**
Multichannel sales engagement platform for email, LinkedIn, call, and SMS outreach with an AI SDR product layered on top.

**AI features, separated from automation with an AI label on it**
"Jason," Reply.io's AI SDR agent, claims to autonomously find prospects, send personalized messages, and manage responses - vendor-stated, genuinely LLM-driven per description but not independently verified. AI-generated icebreakers, first-step emails, and reply categorization are also vendor-claimed AI. Core sequencing/warmup/analytics are plain automation.

**RevOps role**
Multichannel outbound sequencing layer with an AI SDR agent tier positioned as a semi-autonomous prospecting add-on.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key (personal API key over HTTPS, included in free trial)

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-03, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-03 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://reply.io/mcp/

- [https://reply.io/mcp/](https://reply.io/mcp/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Place an outbound call](../jobs/place-outbound-call.md)
- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)
- [Warm up an inbox](../jobs/warm-up-inbox.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Reply.io (Jason AI)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: Official MCP

- **Gate there**: Paid, self-serve

- **Source**: 04-ai-sdr-agents.md line 182

- **Canonical page**: [Reply.io](../tools/reply-io.md)

What that listing says it does: A multichannel sales engagement platform whose AI layer ("Jason AI," per widely reported branding) generates outreach emails/follow-ups and automates sequencing across email, calls, and tasks.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://reply.io/mcp/](https://reply.io/mcp/)
- [https://reply.io/](https://reply.io/)

2 source URLs. Raw sources field, verbatim:

https://reply.io/mcp/, https://reply.io/

**Notes, verbatim from the file**
Vendor states API/webhook access is included across all pricing tiers starting at Standard ($59/mo); some MCP operations consume metered API credits. Site returned HTTP 403 to direct fetch and was retrieved via a read-only proxy - treat pricing figures as slightly less certain than directly-fetched pages.

**Provenance**

- **Entry id**: 02-reply-io

- **Source file**: 02-engagement-outbound.md

- **Source line**: 179

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
