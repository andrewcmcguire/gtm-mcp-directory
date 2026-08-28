# Salesforge: MCP server status, API access gate and what it does

> Multi-channel cold outreach platform (email + LinkedIn) with an AI SDR product ("Agent Frank") layered on top... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Salesforge

# Salesforge

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [salesforge.ai](https://salesforge.ai) · entry id 02-salesforge · source 02-engagement-outbound.md line 236

**What it does**
Multi-channel cold outreach platform (email + LinkedIn) with an AI SDR product ("Agent Frank") layered on top of standard sequencing.

**AI features, separated from automation with an AI label on it**
Agent Frank generates dynamically-written emails per selected tone (Playful, Formal, Curious, Urgent, etc.) - genuinely LLM-based copy generation, not static templates, per vendor description. Vendor claims Frank is "trained on proprietary data lake" and "modeled after top 1% reps" - unverifiable marketing language, flagged as vendor-stated only. Core sequencing/reply capture is plain automation with AI analysis layered on top.

**RevOps role**
Multichannel outbound sequencing with an AI SDR agent as an optional higher tier for more autonomous prospecting.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: api key via HTTP header (X-Salesforge-Key)

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://github.com/SalesforgeAI/forge-mcp

- [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp)

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

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp)

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Run an autonomous SDR agent](../jobs/run-autonomous-sdr-agent.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Also listed in another category**

This page is the canonical home. The listing below is the same product, counted separately in the source markdown.

- **Listed as**: Salesforge (Agent Frank)

- **Category**: [AI SDRs](../categories/ai-sdr-agents.md)

- **MCP status there**: Official MCP

- **Gate there**: Paid, self-serve

- **Source**: 04-ai-sdr-agents.md line 372

- **Canonical page**: [Salesforge](../tools/salesforge.md)

What that listing says it does: An AI agent ("Agent Frank") that prospects, writes tailored outreach, sends across email and LinkedIn, manages follow-up sequences, and books meetings - positioned to either join a human team or fully replace one rep.

16 of the 293 entries are cross listed like this. They are why the entry count is 293 and the unique product count is 277. The canonical home is declared in INDEX.md, not chosen by the parser.

**Sources**

- [https://www.salesforge.ai/](https://www.salesforge.ai/)
- [https://www.salesforge.ai/pricing](https://www.salesforge.ai/pricing)
- [https://github.com/SalesforgeAI/forge-mcp](https://github.com/SalesforgeAI/forge-mcp)

3 source URLs. Raw sources field, verbatim:

https://www.salesforge.ai/, https://www.salesforge.ai/pricing, https://github.com/SalesforgeAI/forge-mcp

**Notes, verbatim from the file**
Both API and MCP access are restricted to the Growth plan ($80/mo) and up, not the base Pro plan ($40/mo); not enterprise-only. A standalone Agent Frank plan runs $499/mo. The "top 1% sales rep" / proprietary-data-lake claims are unverified marketing and should not be repeated as fact.

**Provenance**

- **Entry id**: 02-salesforge

- **Source file**: 02-engagement-outbound.md

- **Source line**: 236

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
