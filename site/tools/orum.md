# Orum: MCP server status, API access gate and what it does

> AI-powered parallel dialer ("Calling Performance System") that dials up to 10 numbers simultaneously and... No MCP found, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
Orum

# Orum

[No MCP found](../mcp/none-found.md)
[Enterprise only](../gates/enterprise-only.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [orum.com](https://orum.com) · entry id 02-orum · source 02-engagement-outbound.md line 65

**What it does**
AI-powered parallel dialer ("Calling Performance System") that dials up to 10 numbers simultaneously and bridges reps only to live human answers.

**AI features, separated from automation with an AI label on it**
Genuinely AI: real-time human-vs-machine detection during connection across 20+ languages/dialects, driving the auto-hang-up/voicemail-drop decision, plus an "AI coaching suite" for connect-rate analysis. Plain automation: the parallel-dial mechanism and local-presence number rotation.

**RevOps role**
Outbound calling/connect-rate layer, typically bolted onto Salesforce/HubSpot/Salesloft/Apollo as the dialing component of a broader stack.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (no prices published, nine-seat minimum, request-pricing only; the sole developer-facing feature named is a Webhooks add-on)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Place an outbound call](../jobs/place-outbound-call.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.orum.com/](https://www.orum.com/)
- [https://www.orum.com/product-updates/hello-world-orum-goes-global-with-ai-dialing](https://www.orum.com/product-updates/hello-world-orum-goes-global-with-ai-dialing)
- [https://apitracker.io/a/orumhq](https://apitracker.io/a/orumhq)
- [https://www.orum.com/pricing](https://www.orum.com/pricing)

4 source URLs. Raw sources field, verbatim:

https://www.orum.com/, https://www.orum.com/product-updates/hello-world-orum-goes-global-with-ai-dialing, https://apitracker.io/a/orumhq, https://www.orum.com/pricing

**Notes, verbatim from the file**
Do not confuse with orum.io, an unrelated fintech payments company (acquired by Stripe) that does have a documented API and MCP server - that belongs to a different company entirely. No MCP found for the sales dialer at orum.com on GitHub, mcp.so, glama.ai, or pulsemcp.com. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://www.orum.com/pricing): no prices published, nine-seat minimum, request-pricing only; the sole developer-facing feature named is a Webhooks add-on. 2026-09-02: re-checked orum.com/llms.txt (404) and web search; the only MCP hit is docs.orum.io/guides/mcp-server, confirmed by reading it to be the fintech Orum (bank accounts, transfers), not the dialer. No MCP server found for orum.com.

**Provenance**

- **Entry id**: 02-orum

- **Source file**: 02-engagement-outbound.md

- **Source line**: 65

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
