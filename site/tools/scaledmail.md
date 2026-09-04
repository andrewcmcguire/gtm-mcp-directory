# Scaledmail: MCP server status, API access gate and what it does

> Cold-email infrastructure provider - sets up sending domains, configures DNS authentication (SPF/DKIM/DMARC)... No MCP found, Free to start. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Scaledmail

# Scaledmail

[No MCP found](../mcp/none-found.md)
[Free to start](../gates/free.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [scaledmail.com](https://scaledmail.com) · entry id 09-scaledmail · source 09-email-deliverability.md line 178

**What it does**
Cold-email infrastructure provider - sets up sending domains, configures DNS authentication (SPF/DKIM/DMARC) from day one, and rotates inboxes so outbound sequences land in the primary tab.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed; domain/DNS setup and inbox rotation read as infrastructure automation, not model-driven.

**RevOps role**
Cold-email infrastructure layer comparable to Maildoso/Mailforge/Hypertide - DNS/domain/inbox setup that feeds a sequencer, with warmup run inside the customer's own sequencer post-setup rather than as a Scaledmail feature.

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

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (public API docs with the key self-served from account settings and signup is a free account with no credit card; no plan gate on the API is stated, though paid usage starts at $3.50/mailbox/mo)

**API documentation**

No documentation URL recorded.

264 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.scaledmail.com/](https://www.scaledmail.com/)
- [https://www.scaledmail.com/blogs/effortless-email-outreach-with-scaledmail](https://www.scaledmail.com/blogs/effortless-email-outreach-with-scaledmail)
- [https://www.infraforge.ai/blog/best-email-apis-for-cold-outreach](https://www.infraforge.ai/blog/best-email-apis-for-cold-outreach)
- [https://api.scaledmail.com/](https://api.scaledmail.com/)

4 source URLs. Raw sources field, verbatim:

https://www.scaledmail.com/, https://www.scaledmail.com/blogs/effortless-email-outreach-with-scaledmail, https://www.infraforge.ai/blog/best-email-apis-for-cold-outreach, https://api.scaledmail.com/

**Notes, verbatim from the file**
Pricing starts at $99/mo per one sourced comparison. No API, developer portal, or MCP server was found for Scaledmail in any of the standard registries checked (GitHub, mcp.so, glama.ai, pulsemcp.com). [api_gate 2026-08-25] Reclassified unknown -> free from the vendor's own page (https://api.scaledmail.com/): public API docs with the key self-served from account settings and signup is a free account with no credit card; no plan gate on the API is stated, though paid usage starts at $3.50/mailbox/mo. 2026-09-02: re-checked scaledmail.com/llms.txt (404), scaledmail.com and api.scaledmail.com (neither mentions MCP) and web search; the 'API & MCP Automation' phrase in search snippets is Maildoso's own product copy on its review pages, not Scaledmail's. No MCP server found.

**Provenance**

- **Entry id**: 09-scaledmail

- **Source file**: 09-email-deliverability.md

- **Source line**: 178

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
