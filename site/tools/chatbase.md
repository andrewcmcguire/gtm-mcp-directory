# Chatbase: MCP server status, API access gate and what it does

> No-code AI agent builder for deploying chat/voice/email support-and-sales bots across a website widget and... Community MCP, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Chatbase

# Chatbase

[Community MCP](../mcp/community.md)
[Paid, self-serve](../gates/paid.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [chatbase.co](https://chatbase.co) · entry id 14-chatbase · source 14-inbound-plg-chat.md line 84

**What it does**
No-code AI agent builder for deploying chat/voice/email support-and-sales bots across a website widget and channels like WhatsApp and Slack.

**AI features, separated from automation with an AI label on it**
Lets a builder pick from multiple underlying LLMs (Claude, Gemini, GPT, DeepSeek referenced on the site) and wire up "Actions" (order lookups, invoice retrieval, payment processing) plus a testing sandbox before going live - genuine AI-agent orchestration tooling, though conversation quality depends entirely on the connected model rather than a proprietary Chatbase model.

**RevOps role**
Solo-operator-friendly, self-serve chatbot-builder entry point into inbound AI chat - cheaper and more accessible than most enterprise tools in this category, at the cost of no proprietary conversation-intelligence layer.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Rides Zapier's hosted-connector auth at mcp.zapier.com, not a Chatbase-issued MCP credential.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://zapier.com/mcp/chatbase](https://zapier.com/mcp/chatbase)Probed**: 2026-09-03, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://zapier.com/mcp/chatbase (Zapier-hosted; viaSocket, Activepieces and Pipedream host equivalents)

- [https://zapier.com/mcp/chatbase](https://zapier.com/mcp/chatbase)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid (limited free tier). Free plan: $0/mo, 50 message credits, inactive agents deleted after 14 days, no API access. API access starts at the Standard tier ($150/mo); Hobby ($40/mo) does not include it.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.chatbase.co](https://www.chatbase.co)
- [https://www.chatbase.co/pricing](https://www.chatbase.co/pricing)
- [https://www.chatbase.co/docs](https://www.chatbase.co/docs)
- [https://zapier.com/mcp/chatbase](https://zapier.com/mcp/chatbase)

4 source URLs. Raw sources field, verbatim:

https://www.chatbase.co, https://www.chatbase.co/pricing, https://www.chatbase.co/docs, https://zapier.com/mcp/chatbase

**Notes, verbatim from the file**
Checked mcp.so, glama.ai, and PulseMCP directly for a Chatbase MCP server - PulseMCP returned zero results ("Showing 0-0 of 0 servers"). Domain is chatbase.co (not .com); no redirect was observed. 2026-09-02: mcp_status none-found -> community. https://zapier.com/mcp/chatbase answers today with one trigger (Form Submission) and one write action (Send Prompt to a chatbot); viaSocket, Activepieces and Pipedream list equivalents. Chatbase itself publishes no MCP: chatbase.co has no llms.txt, the official MCP registry has no entry, and a third-party comparison states no public Chatbase MCP server had been announced as of May 2026. Third-party hosted connectors only, so community, unofficial.

**Provenance**

- **Entry id**: 14-chatbase

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 84

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
