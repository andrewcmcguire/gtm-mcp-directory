# Anymail Finder: MCP server status, API access gate and what it does

> Takes a name plus a company, domain, or LinkedIn URL, verifies the resulting work email against the mail... Official MCP, Free to start. Checked 2026-08-25.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Anymail Finder

# Anymail Finder

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-25

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [anymailfinder.com](https://anymailfinder.com) · entry id 01-anymail-finder · source 01-data-enrichment.md line 639

**What it does**
Takes a name plus a company, domain, or LinkedIn URL, verifies the resulting work email against the mail server in real time, and only charges when the email verifies.

**AI features, separated from automation with an AI label on it**
None, and the vendor does not pretend otherwise. No AI claims appear on the homepage, the pricing page, or the API docs. It is a deterministic email finder and SMTP verifier. The only AI adjacency is that they shipped an MCP server so somebody else's agent can call the deterministic tool, which is the honest version of AI integration and is worth naming as the counter-example to this category's usual marketing.

**RevOps role**
The cheap deterministic waterfall step: an email-find-and-verify primitive you call from Clay, a waterfall, or an agent, right before the sequencer. Not a database you browse, a function you call.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Browser-based OAuth-style sign-in and approval for Claude, ChatGPT and Cursor, with an API key fallback for clients that cannot do browser sign-in.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL[https://api.anymailfinder.com/mcp](https://api.anymailfinder.com/mcp)Probed**: 2026-09-03, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-25. On 2026-09-03 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://api.anymailfinder.com/mcp (guide: https://anymailfinder.com/integrations/mcp)

- [https://api.anymailfinder.com/mcp](https://api.anymailfinder.com/mcp)
- [https://anymailfinder.com/integrations/mcp](https://anymailfinder.com/integrations/mcp)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free

**API documentation**

[https://anymailfinder.com/email-finder-api/docs](https://anymailfinder.com/email-finder-api/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Find a work email address](../jobs/find-work-email.md)
- [Verify an email is deliverable](../jobs/verify-email-deliverable.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://anymailfinder.com/pricing](https://anymailfinder.com/pricing)
- [https://anymailfinder.com/email-finder-api/docs](https://anymailfinder.com/email-finder-api/docs)
- [https://anymailfinder.com/integrations/mcp](https://anymailfinder.com/integrations/mcp)
- [https://api.anymailfinder.com/openapi.json](https://api.anymailfinder.com/openapi.json)

4 source URLs. Raw sources field, verbatim:

https://anymailfinder.com/pricing, https://anymailfinder.com/email-finder-api/docs, https://anymailfinder.com/integrations/mcp, https://api.anymailfinder.com/openapi.json

**Notes, verbatim from the file**
Added 2026-08-25, closing a named warm lead from this file's previous sweep notes. Fully self-serve, no sales gate, API on every tier. 100 free credits to trial; card verification required but not charged. Monthly: 400 credits $29, 1k $49, 2k $89, 5k $149, 10k $199, 25k $299, 50k $499, 100k $799. Yearly roughly 33% off, 4.8k $228 through 1.2M $6,420. Billing is pay-per-verified-result: 1 credit per valid email, 2 for decision-maker searches, 0.2 for a verification, nothing for unverified results or repeat searches within 30 days. MCP exposes five tools sharing the same credit pool as the app and API. The OpenAPI 3.0.0 spec was fetched and validated independently: 16 endpoints on /v5.1/, apiKey in the Authorization header. The "86.4% coverage, 98.9% accuracy" benchmark cites an unlinked independent study; treat as vendor marketing, not as a verified figure. UK entity AMF Internet Services Limited, company number 10586048.

**Provenance**

- **Entry id**: 01-anymail-finder

- **Source file**: 01-data-enrichment.md

- **Source line**: 639

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-25

- **Data baked**: 2026-09-04

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
