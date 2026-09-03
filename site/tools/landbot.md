# Landbot: MCP server status, API access gate and what it does

> No-code visual builder for chatbots deployed on websites, WhatsApp, and Messenger, blending rule-based flows... Community MCP, Free to start. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Landbot

# Landbot

[Community MCP](../mcp/community.md)
[Free to start](../gates/free.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [landbot.io](https://landbot.io) · entry id 14-landbot · source 14-inbound-plg-chat.md line 218

**What it does**
No-code visual builder for chatbots deployed on websites, WhatsApp, and Messenger, blending rule-based flows with LLM-powered conversation.

**AI features, separated from automation with an AI label on it**
"AI Agent Chatbots" combine rule-based control with LLM conversation (connects to OpenAI and Google Gemini per the site); an "AI Copilot" gives in-context build guidance and can configure a flow from a plain-language use-case description - vendor-described, not independently verified.

**RevOps role**
Low-friction, self-serve entry point for building an AI-assisted inbound chat flow without an enterprise contract.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: The operator's own Landbot API key stored with Composio; the Zapier connector rides Zapier's hosted auth at mcp.zapier.com.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://composio.dev/toolkits/landbot](https://composio.dev/toolkits/landbot)Probed**: 2026-09-03, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://composio.dev/toolkits/landbot (Composio-hosted, 13 tools); https://zapier.com/mcp/landbot (Zapier-hosted, trigger only)

- [https://composio.dev/toolkits/landbot](https://composio.dev/toolkits/landbot)
- [https://zapier.com/mcp/landbot](https://zapier.com/mcp/landbot)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (limited). Perpetual free tier (EUR0/mo, 100 chats/mo, full builder access, no card required); paid tiers from Starter (EUR32/mo) through Professional (EUR80-160/mo) add webhooks/API and premium CRM integrations (HubSpot, Salesforce, Pipedrive, Zoho); Business tier is custom/enterprise.

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

- [https://landbot.io](https://landbot.io)
- [https://landbot.io/pricing](https://landbot.io/pricing)
- [https://composio.dev/toolkits/landbot](https://composio.dev/toolkits/landbot)
- [https://zapier.com/mcp/landbot](https://zapier.com/mcp/landbot)

4 source URLs. Raw sources field, verbatim:

https://landbot.io, https://landbot.io/pricing, https://composio.dev/toolkits/landbot, https://zapier.com/mcp/landbot

**Notes, verbatim from the file**
Checked PulseMCP directly - zero results for "landbot," consistent with none-found. 2026-09-02: mcp_status none-found -> community. Composio's Landbot toolkit answers today with 13 tools (List Bots, Delete Bot, List Agents, Update Agent, Set Agent Status, Replace Agent, List Customers, List Channels, List WhatsApp Templates, Send Message, Get Brand, Update Brand, Replace Brand) authenticated with your own Landbot API key, and https://zapier.com/mcp/landbot exposes a single Zapier Block Activated trigger. Landbot publishes no MCP of its own: landbot.io has no llms.txt and the official MCP registry has no entry. Third-party hosted connectors only, so community, unofficial.

**Provenance**

- **Entry id**: 14-landbot

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 218

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
