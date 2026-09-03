# Airspeed (formerly Glyphic): MCP server status, API access gate and what it does

> Records and analyses sales calls, then scores deals against playbooks and writes structured output back into... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Airspeed (formerly Glyphic)

# Airspeed (formerly Glyphic)

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [goairspeed.com](https://goairspeed.com) · entry id 03-airspeed · source 03-conversation-intel.md line 391

**What it does**
Records and analyses sales calls, then scores deals against playbooks and writes structured output back into the CRM.

**AI features, separated from automation with an AI label on it**
Genuinely AI-led: automatic call summarisation, MEDDIC-style qualification breakdowns, and agent runs whose structured outputs are retrievable as their own MCP tool rather than only as text.

**RevOps role**
Conversation capture and deal-scoring layer sitting between the call and the pipeline review.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Airspeed API key passed as an X-API-Key header.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://api.glyphic.ai/mcp](https://api.glyphic.ai/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.glyphic.ai/mcp (docs: https://www.goairspeed.com/product/mcp)

- [https://api.glyphic.ai/mcp](https://api.glyphic.ai/mcp)
- [https://www.goairspeed.com/product/mcp](https://www.goairspeed.com/product/mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://www.goairspeed.com/product/api](https://www.goairspeed.com/product/api)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.goairspeed.com/product/mcp](https://www.goairspeed.com/product/mcp)
- [https://www.goairspeed.com/](https://www.goairspeed.com/)
- [https://www.pulsemcp.com/servers/glyphic](https://www.pulsemcp.com/servers/glyphic)
- [https://www.goairspeed.com/product/api](https://www.goairspeed.com/product/api)

4 source URLs. Raw sources field, verbatim:

https://www.goairspeed.com/product/mcp, https://www.goairspeed.com/, https://www.pulsemcp.com/servers/glyphic, https://www.goairspeed.com/product/api

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. REBRAND FOUND: Glyphic became Airspeed, glyphic.ai now 301-redirects to goairspeed.com, but the MCP endpoint still lives on the old api.glyphic.ai host, and most registry listings still say "Glyphic". That mismatch is a directly usable staleness signal for the registry-diff mechanism: a name-keyed diff would never catch this rebrand. Eleven tools across calls, playbooks and agent runs. GOVERNANCE CAVEAT worth saying out loud: API keys carry org-wide read access to every call, so an agent given this key can read the whole company's call library, not just the holder's. NOT VERIFIED: which Airspeed plan grants API keys.

**Provenance**

- **Entry id**: 03-airspeed

- **Source file**: 03-conversation-intel.md

- **Source line**: 391

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
