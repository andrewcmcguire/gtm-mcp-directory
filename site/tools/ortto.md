# Ortto: MCP server status, API access gate and what it does

> A combined customer data platform and marketing automation tool for building multi-channel journeys across... Official MCP, Paid, self-serve. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[RevOps Infra](../categories/revops-infra.md) /
Ortto

# Ortto

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[RevOps Infra](../categories/revops-infra.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [ortto.com](https://ortto.com) · entry id 06-ortto · source 06-revops-infra.md line 496

**What it does**
A combined customer data platform and marketing automation tool for building multi-channel journeys across email, SMS, push, in-app and live chat.

**AI features, separated from automation with an AI label on it**
The MCP layer gives natural-language access to campaign, audience and report data. The journey logic itself is rules-based automation, not AI.

**RevOps role**
Customer data and lifecycle-marketing layer sitting beside the CRM, useful for pulling campaign performance into pipeline analysis.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: A scoped JWT key created as an MCP data source inside the Ortto account, passed as a "jwt" query parameter on the URL.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://mcp-api-us.ortto.app/mcp](https://mcp-api-us.ortto.app/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp-api-us.ortto.app/mcp (docs: https://help.ortto.com/a-910-ortto-mcp; region variants at mcp-api-eu and mcp-api-au)

- [https://mcp-api-us.ortto.app/mcp](https://mcp-api-us.ortto.app/mcp)
- [https://help.ortto.com/a-910-ortto-mcp](https://help.ortto.com/a-910-ortto-mcp)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

[https://help.ortto.com/a-910-ortto-mcp](https://help.ortto.com/a-910-ortto-mcp)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Run an email sequence](../jobs/run-email-sequence.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)
- [Run an automation workflow](../jobs/run-automation-workflow.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://help.ortto.com/a-910-ortto-mcp](https://help.ortto.com/a-910-ortto-mcp)
- [https://help.ortto.com/a-911-using-ortto-mcp-with-claude](https://help.ortto.com/a-911-using-ortto-mcp-with-claude)
- [https://ortto.com/](https://ortto.com/)

3 source URLs. Raw sources field, verbatim:

https://help.ortto.com/a-910-ortto-mcp, https://help.ortto.com/a-911-using-ortto-mcp-with-claude, https://ortto.com/

**Notes, verbatim from the file**
Added 2026-08-25 in the coverage sweep. Endpoints are region-pinned: US, EU and AU variants at mcp-api-us, mcp-api-eu and mcp-api-au respectively, so the wrong region simply will not authenticate. SECURITY DESIGN WORTH FLAGGING TO READERS: the credential is passed as a URL query parameter rather than a header, which means it can land in proxy logs, browser history and referrer headers in a way a header-based key does not. That is a vendor design choice, stated here as an observation from the vendor's own documented setup, not as a tested finding. MCP calls consume the standard Ortto API rate limit for the account's plan. NOT VERIFIED: the minimum plan required for MCP; the vendor states only that a 14-day trial exists.

**Provenance**

- **Entry id**: 06-ortto

- **Source file**: 06-revops-infra.md

- **Source line**: 496

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
