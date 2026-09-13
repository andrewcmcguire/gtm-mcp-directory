# Harmonic: MCP server status, API access gate and what it does

> A startup and private-company database built for early discovery, tracking a stated 40 million companies, 200... Official MCP, Enterprise leaning. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Harmonic

# Harmonic

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [harmonic.ai](https://harmonic.ai) · entry id 01-harmonic · source 01-data-enrichment.md line 777

**What it does**
A startup and private-company database built for early discovery, tracking a stated 40 million companies, 200 million people and 250 thousand investors, with company search, similar-company lookup, people lookup and saved lists exposed through a console, a REST API and an MCP server.

**AI features, separated from automation with an AI label on it**
"Scout" is a vendor-named AI layer described on the pricing page as "the AI that knows startups"; the differentiator the vendor actually argues for is coverage and freshness (finding companies at formation) rather than model inference. No model detail is published, so Scout is recorded as a vendor claim, not a verified capability.

**RevOps role**
Early-signal company discovery for teams selling into startups and for investor-adjacent research, sitting upstream of the CRM as a sourcing and lookalike layer rather than a contact-detail provider.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: oauth. The server publishes OAuth protected-resource metadata at https://mcp.api.harmonic.ai/.well-known/oauth-protected-resource declaring itself as its own authorization server, with read and write scopes and bearer tokens carried in the header.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: not probed yet

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-09-07 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.api.harmonic.ai (vendor docs path: https://console.harmonic.ai/docs/mcp-server)

- [https://mcp.api.harmonic.ai](https://mcp.api.harmonic.ai)
- [https://console.harmonic.ai/docs/mcp-server](https://console.harmonic.ai/docs/mcp-server)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 281 entries that record an official or community MCP server carry a harvested tool list. The other 162 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning - Harmonic publishes no price for any tier. Its pricing page lists three packages (Console access, API access, Bulk data), each with the same "Get pricing" call to action and a "Book a demo" header CTA, and no self-serve signup path was found. MCP appears twice on that page as a feature line: "MCP trial credits" on the Console tier and "Full MCP access for your agents or LLMs" on the API tier.

**API documentation**

No documentation URL recorded.

428 of 559 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to harmonic.ai with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: harmonic, harmonic-ai, HarmonicLabs, harmonicinc-com, harmonicinc-video. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

No job tag on this entry.

288 of 559 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://harmonic.ai/pricing](https://harmonic.ai/pricing)
- [https://mcp.api.harmonic.ai/.well-known/oauth-protected-resource](https://mcp.api.harmonic.ai/.well-known/oauth-protected-resource)
- [https://console.harmonic.ai/docs/mcp-server](https://console.harmonic.ai/docs/mcp-server)
- [https://mcp.api.harmonic.ai](https://mcp.api.harmonic.ai)

4 source URLs. Raw sources field, verbatim:

https://harmonic.ai/pricing, https://mcp.api.harmonic.ai/.well-known/oauth-protected-resource, https://console.harmonic.ai/docs/mcp-server, https://mcp.api.harmonic.ai

**Notes, verbatim from the file**
Verified 2026-09-07: POST of an MCP initialize to https://mcp.api.harmonic.ai returned HTTP 401 with an invalid_token error instructing the client to clear its tokens and reconnect, which is how a live OAuth-gated MCP server behaves, and the OAuth protected-resource document at the same host resolved and declared read and write scopes. HONEST LIMIT: console.harmonic.ai/docs/mcp-server returns HTTP 200 but is a client-rendered dashboard shell, so no human-readable MCP documentation could be read by an automated fetch on this date. The official call therefore rests on the first-party endpoint plus the two MCP feature lines on harmonic.ai/pricing, not on a docs page whose contents anyone has verified. The tier split is the useful finding for a solo operator: "MCP trial credits" and "Full MCP access" are different things on different packages and neither carries a published price. Cross-reference: this is also a signals product and 05-signals-intent-abm.md could reasonably cross-list it; 01 is treated as canonical. 2026-09-07: https://mcp.api.harmonic.ai returned 401 to an MCP initialize POST (https://mcp.api.harmonic.ai).

**Provenance**

- **Entry id**: 01-harmonic

- **Source file**: 01-data-enrichment.md

- **Source line**: 777

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
