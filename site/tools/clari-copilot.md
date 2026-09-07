# Clari Copilot: MCP server status, API access gate and what it does

> Records and transcribes sales calls in real time and surfaces live coaching prompts, deal-risk flags, and... Official MCP, Paid, self-serve. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Clari Copilot

# Clari Copilot

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [clari.com/products/copilot/](https://clari.com/products/copilot/) · entry id 03-clari-copilot · source 03-conversation-intel.md line 49

**What it does**
Records and transcribes sales calls in real time and surfaces live coaching prompts, deal-risk flags, and auto-generated CRM updates during and after the call.

**AI features, separated from automation with an AI label on it**
Real-time deal-risk / blocker and competitor-mention detection; automatic capture of intent, objections, contacts, and next steps for CRM writeback; AI-generated call summaries and follow-up emails. Live "battlecards"/playbooks are more rules-based coaching content than a distinct AI model.

**RevOps role**
Conversation-intelligence / call-recording layer (Gong-equivalent within the Clari family), feeding call-derived signals up into the broader Clari forecasting platform.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Scalekit-hosted connector uses per-user delegated OAuth-style authorization in Scalekit's own token vault. The underlying Clari Copilot REST API (https://api-doc.copilot.clari.com/) uses a static API Key + API Password pair generated in Workspace Settings → Integrations.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://www.scalekit.com/connectors/claricopilot](https://www.scalekit.com/connectors/claricopilot)Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.clari.com/mcp ; https://www.scalekit.com/connectors/claricopilot (third-party connector, not vendor-built). A Clari community forum thread - https://community.clari.com/product-q-a-6/why-was-copilot-mcp-server-removed-from-the-july-release-notes-2980 - asks why a "Copilot MCP Server" was pulled from July release notes, suggesting an official one may have been planned or briefly shipped. SUPERSEDED 2026-09-07: a first-party Clari MCP endpoint at https://mcp.clari.com/mcp does answer, so this entry is now official; see notes.

- [https://mcp.clari.com/mcp](https://mcp.clari.com/mcp)
- [https://www.scalekit.com/connectors/claricopilot](https://www.scalekit.com/connectors/claricopilot)
- [https://community.clari.com/product-q-a-6/why-was-copilot-mcp-server-removed-from-the-july-release-notes-2980](https://community.clari.com/product-q-a-6/why-was-copilot-mcp-server-removed-from-the-july-release-notes-2980)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid. API access is self-service inside the product (Workspace Settings) once you are an active Copilot subscriber - no separate sales-gated enable step like the main Clari API. Whether a solo operator can become a Copilot customer at all without a sales call is unknown.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.clari.com/products/copilot/](https://www.clari.com/products/copilot/)
- [https://api-doc.copilot.clari.com/](https://api-doc.copilot.clari.com/)
- [https://community.clari.com/product-q-a-6/how-to-use-copilot-apis-2258](https://community.clari.com/product-q-a-6/how-to-use-copilot-apis-2258)
- [https://www.scalekit.com/connectors/claricopilot](https://www.scalekit.com/connectors/claricopilot)
- [https://community.clari.com/product-q-a-6/why-was-copilot-mcp-server-removed-from-the-july-release-notes-2980](https://community.clari.com/product-q-a-6/why-was-copilot-mcp-server-removed-from-the-july-release-notes-2980)
- [https://mcp.clari.com/mcp](https://mcp.clari.com/mcp)

6 source URLs. Raw sources field, verbatim:

https://www.clari.com/products/copilot/, https://api-doc.copilot.clari.com/, https://community.clari.com/product-q-a-6/how-to-use-copilot-apis-2258, https://www.scalekit.com/connectors/claricopilot, https://community.clari.com/product-q-a-6/why-was-copilot-mcp-server-removed-from-the-july-release-notes-2980, https://mcp.clari.com/mcp

**Notes, verbatim from the file**
The removed-from-release-notes thread is worth watching - an official Clari Copilot MCP server may land later and should be re-checked. 2026-09-07: Same first-party endpoint as the Clari entry: https://mcp.clari.com/mcp answered 401 to an MCP initialize while a control path 404d (https://mcp.clari.com/mcp). mcp_status raised community to official on this evidence: mcp.clari.com is Clari's own domain and the control path 404s, so the endpoint is first-party; the previous community status rested on the third-party Scalekit connector, retained below. CAVEAT recorded by the finder: the 401 proves a live first-party Clari MCP server but does not prove that the Clari Copilot tool surface sits behind it.

**Provenance**

- **Entry id**: 03-clari-copilot

- **Source file**: 03-conversation-intel.md

- **Source line**: 49

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-07

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
