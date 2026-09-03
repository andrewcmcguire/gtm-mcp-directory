# Forethought (now "Forethought AI Agents by Zendesk"): MCP server status, API access gate and what it does

> Omnichannel AI agent ("Solve") that resolves customer support and pre-sales issues across chat, email, voice,... MCP unknown, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Forethought (now "Forethought AI Agents by Zendesk")

# Forethought (now "Forethought AI Agents by Zendesk")

[MCP unknown](../mcp/unknown.md)
[Enterprise only](../gates/enterprise-only.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [forethought.ai](https://forethought.ai) · entry id 14-forethought · source 14-inbound-plg-chat.md line 256

**What it does**
Omnichannel AI agent ("Solve") that resolves customer support and pre-sales issues across chat, email, voice, and a headless API, trained on a company's past tickets and help-center content.

**AI features, separated from automation with an AI label on it**
Vendor describes "agentic reasoning" - the system reasons, decides, and takes action per configured business policies, aiming for end-to-end resolution rather than hand-off-only assistance; self-improvement claims from Zendesk's acquisition announcement were not independently verified.

**RevOps role**
Enterprise inbound support-AI layer, now being integrated into Zendesk's broader Resolution Platform rather than sold as a fully independent product.

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: unknown

- **Parsed URLs**: 1 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

none published. Forethought's own headless page https://forethought.ai/channels/headless carries an "MCP" section ("SDK + API + MCP") with no endpoint, docs or setup guide.

- [https://forethought.ai/channels/headless](https://forethought.ai/channels/headless)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only. No published pricing; the pricing page lists Team/Professional/Enterprise tiers all behind "Get a Quote," and the FAQ states Forethought offers a "Proof of Value (POV) instead of a traditional free trial."

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.forethought.ai](https://www.forethought.ai)
- [https://www.forethought.ai/pricing](https://www.forethought.ai/pricing)
- [https://www.zendesk.com/newsroom/press-releases/zendesk-completes-acquisition-of-forethought/](https://www.zendesk.com/newsroom/press-releases/zendesk-completes-acquisition-of-forethought/)
- [https://forethought.ai/channels/headless](https://forethought.ai/channels/headless)

4 source URLs. Raw sources field, verbatim:

https://www.forethought.ai, https://www.forethought.ai/pricing, https://www.zendesk.com/newsroom/press-releases/zendesk-completes-acquisition-of-forethought/, https://forethought.ai/channels/headless

**Notes, verbatim from the file**
STATUS FLAG - ACQUIRED. Zendesk announced intent to acquire Forethought on March 11, 2026 and completed the acquisition March 26, 2026. forethought.ai now carries a banner reading "A new chapter begins: Forethought is now part of Zendesk," and Zendesk is rebranding the technology "Forethought AI Agents by Zendesk" for deployment across its own Resolution Platform. Checked PulseMCP for an MCP server - zero results. 2026-09-02: mcp_status none-found -> unknown. https://forethought.ai/channels/headless is titled "Headless CX AI Platform: SDK + API + MCP" and its MCP section reads only "Connect your systems, data, and business rules to agentic AI so every interaction is grounded in real context"; a search snippet of the same page describes the offer as "Agent SDK, API access, and MCP Client", which would make Forethought a consumer of MCP servers rather than a publisher. No endpoint, docs or auth are published, forethought.ai has no llms.txt and the official MCP registry has no entry. A first-party mention that does not even settle server versus client is unknown, not official. Zendesk's own MCP server (announced at Relate, May 2026) is a separate question for the Zendesk backlog item.

**Provenance**

- **Entry id**: 14-forethought

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 256

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
