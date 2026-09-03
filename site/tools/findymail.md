# Findymail: MCP server status, API access gate and what it does

> An email finder and verifier that locates a person's work email from a name+domain, domain-only search, or... No MCP found, Free to start. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Findymail

# Findymail

[No MCP found](../mcp/none-found.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [findymail.com](https://findymail.com) · entry id 01-findymail · source 01-data-enrichment.md line 217

**What it does**
An email finder and verifier that locates a person's work email from a name+domain, domain-only search, or LinkedIn profile URL, verifies deliverability, and can also retrieve a phone number from a LinkedIn URL.

**AI features, separated from automation with an AI label on it**
No AI claims found on the vendor's own API/pricing pages. Functionality is standard email-pattern generation plus SMTP/deliverability verification - a lookup-and-verify tool, not AI-branded by the vendor in the sources reviewed.

**RevOps role**
Verification-heavy email/phone finder typically used as a secondary or tertiary step in a waterfall (e.g., after Prospeo/Datagma) to catch valid emails other providers miss before handoff to outreach tools.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: not recorded

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 17 of 293 entries are.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.findymail.com/pricing/](https://www.findymail.com/pricing/)
- [https://www.findymail.com/api/](https://www.findymail.com/api/)
- [https://app.findymail.com/docs/](https://app.findymail.com/docs/)
- [https://composio.dev/toolkits/findymail](https://composio.dev/toolkits/findymail)
- [https://university.clay.com/docs/findymail-integration-overview](https://university.clay.com/docs/findymail-integration-overview)

5 source URLs. Raw sources field, verbatim:

https://www.findymail.com/pricing/, https://www.findymail.com/api/, https://app.findymail.com/docs/, https://composio.dev/toolkits/findymail, https://university.clay.com/docs/findymail-integration-overview

**Notes, verbatim from the file**
A GitHub repo titled "Meerkats-Ai/findymail-mcp-server" surfaced in search results but returns HTTP 404 on direct fetch (no longer public), so per the hard law against inferring unverified MCPs this is recorded as none-found. Findymail is otherwise reachable only through generic no-code MCP-aggregator platforms (Composio, Zapier, Pipedream, Gumloop) that wrap thousands of apps uniformly - not a dedicated, independently-maintained Findymail MCP, so not counted. Findymail is a confirmed Clay "data provider" (using your own API key inside Clay requires Clay's Starter plan, $149/mo). Findymail's own API is self-serve: instant API key on signup, free trial 10 credits/no card, paid plans start $49-99/mo, Enterprise is custom/sales-gated only for high volume. 2026-09-02: re-checked findymail.com/llms.txt (404), app.findymail.com/docs (no MCP mention) and github.com/Meerkats-Ai/findymail-mcp-server (still 404); only aggregator wrappers (Pipedream, Zapier, Gumloop, Composio) surface, no MCP server found.

**Provenance**

- **Entry id**: 01-findymail

- **Source file**: 01-data-enrichment.md

- **Source line**: 217

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
