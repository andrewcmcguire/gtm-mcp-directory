# Woodpecker: MCP server status, API access gate and what it does

> Cold email and LinkedIn outreach automation tool with inbox rotation, adaptive sending, and centralized reply... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Woodpecker

# Woodpecker

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [woodpecker.co](https://woodpecker.co) · entry id 02-woodpecker · source 02-engagement-outbound.md line 198

**What it does**
Cold email and LinkedIn outreach automation tool with inbox rotation, adaptive sending, and centralized reply management.

**AI features, separated from automation with an AI label on it**
Vendor advertises an AI email writer (copy drafting) and AI interest-level detection that auto-sorts replies by engagement - both genuinely AI/LLM-adjacent but modest in scope versus competitors' "AI agent" claims. Inbox rotation and adaptive sending are plain automation.

**RevOps role**
Outbound email sequencing/deliverability layer; MCP access is bundled with API/webhook access as one paid add-on.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: hosted OAuth-style flow (Claude-specific) or self-hosted Docker setup using a Woodpecker API key

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://developers.woodpecker.co/docs/mcp/ (Claude-specific setup at https://developers.woodpecker.co/docs/mcp/connect-claude/)

- [https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/)
- [https://developers.woodpecker.co/docs/mcp/connect-claude/](https://developers.woodpecker.co/docs/mcp/connect-claude/)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://woodpecker.co/pricing/](https://woodpecker.co/pricing/)
- [https://developers.woodpecker.co/docs/mcp/](https://developers.woodpecker.co/docs/mcp/)

2 source URLs. Raw sources field, verbatim:

https://woodpecker.co/pricing/, https://developers.woodpecker.co/docs/mcp/

**Notes, verbatim from the file**
"Integrations, API, webhooks, MCP, CLI" is a single $20/month add-on available on top of any pricing tier - not enterprise-gated. Notable discovery gap: this server did not surface via GitHub/glama.ai search (which returned an unrelated "Woodpecker CI" project) - only found by checking the vendor's own site directly.

**Provenance**

- **Entry id**: 02-woodpecker

- **Source file**: 02-engagement-outbound.md

- **Source line**: 198

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
