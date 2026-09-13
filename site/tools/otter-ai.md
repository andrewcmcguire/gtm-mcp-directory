# Otter.ai: MCP server status, API access gate and what it does

> AI meeting notetaker whose Sales Agent variant pulls CRM context before a call and flags objections,... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Otter.ai

# Otter.ai

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [otter.ai](https://otter.ai) · entry id 03-otter-ai · source 03-conversation-intel.md line 125

**What it does**
AI meeting notetaker whose Sales Agent variant pulls CRM context before a call and flags objections, competitor mentions, and pricing discussion live, then writes summaries and next steps back to the CRM.

**AI features, separated from automation with an AI label on it**
Live objection/competitor-mention flagging, real-time coaching tips, automatic pain-point and next-step summarization, buying-signal extraction feeding forecast updates, auto-drafted follow-up emails. Live transcription/captioning itself is ASR.

**RevOps role**
Live-call-assist layer available at Business tier; broader API/MCP agent access is reserved for Enterprise, making it one of the least solo-operator-friendly tools in this category on the developer-access axis.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - exact auth mechanism not confirmed in public sources; framed under "Otter for Enterprise" with a demo-request CTA.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: did not answer
- **Probed**: 2026-09-04, HTTP None

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 no recorded MCP URL answered.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.otter.ai/mcp ; https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server ; https://otter.ai/blog/otter-mcp-your-meetings-now-power-every-tool-you-use ; https://otter.ai/blog/otter-for-enterprise-connect-ai-to-ai-with-otters-mcp

- [https://mcp.otter.ai/mcp](https://mcp.otter.ai/mcp)
- [https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server](https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server)
- [https://otter.ai/blog/otter-mcp-your-meetings-now-power-every-tool-you-use](https://otter.ai/blog/otter-mcp-your-meetings-now-power-every-tool-you-use)
- [https://otter.ai/blog/otter-for-enterprise-connect-ai-to-ai-with-otters-mcp](https://otter.ai/blog/otter-for-enterprise-connect-ai-to-ai-with-otters-mcp)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

119 of the 337 entries that record an official or community MCP server carry a harvested tool list. The other 218 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. The full roll up is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only for the general API. Otter's Enterprise plan is the only tier explicitly documented to include "Otter API and webhooks" plus SSO/SCIM (limit of 2 API keys/user, 10 req/sec once granted). The Business plan unlocks Sales Agent/CRM sync features but not the general API.

**API documentation**

No documentation URL recorded.

494 of 694 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/otter-ai](https://github.com/otter-ai) tied to the vendor by rule 3, account website https://www.otter.ai has the vendor's domain, confidence strong

- **Public repositories**: 0, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: not recorded

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Summarize a meeting](../jobs/summarize-meeting.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Read CRM records](../jobs/read-crm-records.md)
- [Write CRM records](../jobs/write-crm-records.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 694 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://otter.ai/sales-agent](https://otter.ai/sales-agent)
- [https://otter.ai/pricing](https://otter.ai/pricing)
- [https://otter.ai/blog/otter-for-enterprise-connect-ai-to-ai-with-otters-mcp](https://otter.ai/blog/otter-for-enterprise-connect-ai-to-ai-with-otters-mcp)
- [https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server](https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server)
- [https://mcp.otter.ai/mcp](https://mcp.otter.ai/mcp)

5 source URLs. Raw sources field, verbatim:

https://otter.ai/sales-agent, https://otter.ai/pricing, https://otter.ai/blog/otter-for-enterprise-connect-ai-to-ai-with-otters-mcp, https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server, https://mcp.otter.ai/mcp

**Notes, verbatim from the file**
None. 2026-09-07: https://mcp.otter.ai/mcp returned 401 {"error": "invalid_token", "error_description": "Authentication required"} to an MCP initialize POST (https://mcp.otter.ai/mcp).

**Provenance**

- **Entry id**: 03-otter-ai

- **Source file**: 03-conversation-intel.md

- **Source line**: 125

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
