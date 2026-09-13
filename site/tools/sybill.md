# Sybill: MCP server status, API access gate and what it does

> AI sales assistant that analyzes call recordings, emails, and CRM data to produce deal insights, call... Official MCP, Enterprise leaning. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Sybill

# Sybill

[Official MCP](../mcp/official.md)
[Enterprise leaning](../gates/enterprise-leaning.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [sybill.ai](https://sybill.ai) · entry id 03-sybill · source 03-conversation-intel.md line 239

**What it does**
AI sales assistant that analyzes call recordings, emails, and CRM data to produce deal insights, call summaries, and behavioral/sentiment reads on prospects.

**AI features, separated from automation with an AI label on it**
Conversational Q&A over calls, deals, people, and companies; deal-insight generation; auto-generated summaries. Vendor also markets "real-time risk intelligence" and behavioral-analysis claims that are vendor copy and were not independently verified here.

**RevOps role**
Chat-first conversation-intelligence layer aimed at individual AEs, with a still-experimental developer surface.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Browser-based sign-in / OAuth on first connection from an MCP client such as Claude Desktop.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.sybill.ai/mcp ; https://api.sybill.ai/docs/mcp.html (server https://mcp.sybill.ai/mcp)

- [https://mcp.sybill.ai/mcp](https://mcp.sybill.ai/mcp)
- [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html)

**What this server exposes**

- **Tools named**: 8
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **ask_sybill** Ask Sybill AI about your sales calls, deals, people, companies, emails, and more. evidence: in the vendor docs · calling it reads · required: message

- **get_account** Get the available details of a single CRM account evidence: in the vendor docs · calling it reads · required: account_id

- **get_ask_sybill_result** Fetch the status and final answer for a previously submitted ask_sybill run evidence: in the vendor docs · calling it reads · required: thread_id, run_id

- **get_conversation** Get the available details of a single conversation or meeting evidence: in the vendor docs · calling it reads · required: conversation_id

- **get_deal** Get the available details of a single CRM deal evidence: in the vendor docs · calling it reads · required: deal_id

- **list_accounts** List CRM accounts available to the signed-in user evidence: in the vendor docs · calling it reads

- **list_conversations** List sales conversations and meetings available to the signed-in user evidence: in the vendor docs · calling it reads

- **list_deals** List CRM deals available to the signed-in user evidence: in the vendor docs · calling it reads

119 of the 396 entries that record an official or community MCP server carry a harvested tool list. The other 277 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise leaning

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-leaning (API and MCP access appear only on Business at $90/user/mo and Enterprise; Free and Pro carry neither, and the Business CTA is book-a-demo rather than a self-serve checkout)

**API documentation**

No documentation URL recorded.

555 of 834 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to sybill.ai with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: sybill-ai-engineering, sybilla, SybillaTechnologies, sybill-gtm-engineering, sybill-ai-copilot-users. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Search across recorded calls](../jobs/search-call-library.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 834 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://api.sybill.ai/docs/mcp.html](https://api.sybill.ai/docs/mcp.html)
- [https://api.sybill.ai/docs/introduction.html](https://api.sybill.ai/docs/introduction.html)
- [https://www.sybill.ai/pricing](https://www.sybill.ai/pricing)
- [https://help.sybill.ai/en/articles/15384825-sybill-ai-credits-guide-pricing-overview](https://help.sybill.ai/en/articles/15384825-sybill-ai-credits-guide-pricing-overview)
- [https://mcp.sybill.ai/mcp](https://mcp.sybill.ai/mcp)

5 source URLs. Raw sources field, verbatim:

https://api.sybill.ai/docs/mcp.html, https://api.sybill.ai/docs/introduction.html, https://www.sybill.ai/pricing, https://help.sybill.ai/en/articles/15384825-sybill-ai-credits-guide-pricing-overview, https://mcp.sybill.ai/mcp

**Notes, verbatim from the file**
None. [api_gate 2026-08-25] Reclassified unknown -> enterprise-leaning from the vendor's own page (https://www.sybill.ai/pricing): API and MCP access appear only on Business at $90/user/mo and Enterprise; Free and Pro carry neither, and the Business CTA is book-a-demo rather than a self-serve checkout. 2026-09-07: https://mcp.sybill.ai/mcp returned 401 to an MCP initialize POST (https://mcp.sybill.ai/mcp).

**Provenance**

- **Entry id**: 03-sybill

- **Source file**: 03-conversation-intel.md

- **Source line**: 239

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
