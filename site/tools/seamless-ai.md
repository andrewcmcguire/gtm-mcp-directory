# Seamless.AI: MCP server status, API access gate and what it does

> A B2B contact and company database/prospecting tool that lets users search and pull emails, phone numbers,... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
Seamless.AI

# Seamless.AI

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-07
CLI: seamless (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [seamless.ai](https://seamless.ai) · entry id 01-seamless-ai · source 01-data-enrichment.md line 312

**What it does**
A B2B contact and company database/prospecting tool that lets users search and pull emails, phone numbers, and firmographic data from a claimed 1.9B+ contact / 121M+ company index, plus basic list-building, outreach/campaign sending, and CRM sync.

**AI features, separated from automation with an AI label on it**
Marketed heavily as "AI-powered," but the core function - matching a target list against a contact database and returning emails/phones - is lookup plus data-matching/verification, not generative AI. The new MCP server adds a real LLM-agent layer (natural-language prompts driving search/enrichment/campaign actions), and there's an "AI research" account-summarization feature - that layer is genuine LLM use; the underlying contact data itself is a traditional scraped/aggregated database.

**RevOps role**
Top-of-funnel prospecting/contact-discovery source - used to build target lists and pull direct-dial/email data before handoff to outreach tooling; both raw API and (per docs) MCP access are gated behind account-level enablement tied to higher tiers.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.1 or API key; docs state "MCP access must be enabled on your account" - i.e. gated per-account, contact admin/support to turn on

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://docs.seamless.ai/mcp-docs](https://docs.seamless.ai/mcp-docs)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.seamless.ai/mcp ; https://docs.seamless.ai/mcp-docs (hosted endpoint https://mcp.seamless.ai/mcp)

- [https://mcp.seamless.ai/mcp](https://mcp.seamless.ai/mcp)
- [https://docs.seamless.ai/mcp-docs](https://docs.seamless.ai/mcp-docs)

**What this server exposes**

- **Tools named**: 54
- **Strongest evidence**: in the vendor docs
- **Harvested**: 2026-09-12
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **add_contacts_to_campaign** Add saved contacts. evidence: in the vendor docs · calling it writes · required: campaignId, contactIds

- **clone_campaign** Copy campaign (steps, not contacts). evidence: in the vendor docs · calling it reads · required: id

- **create_campaign** Create a campaign; optional inline steps and contactIds. evidence: in the vendor docs · calling it writes · required: name

- **create_campaign_step** Add email, call, or task step. evidence: in the vendor docs · calling it writes · required: campaignId, type, content

- **create_email_draft** Create draft (not sent). evidence: in the vendor docs · calling it writes

- **create_list** Create a new contact list. evidence: in the vendor docs · calling it writes · required: name

- **create_saved_search** Save search filter values as a named saved search. evidence: in the vendor docs · calling it reads · required: type, values

- **create_task** Create email, call, or custom task. evidence: in the vendor docs · calling it writes · required: taskType

- **create_template** Create template with subject and body. evidence: in the vendor docs · calling it writes · required: name, subject, body

- **delete_campaign** Delete campaign and all steps/tasks. evidence: in the vendor docs · calling it writes · required: id

- **delete_campaign_step** Delete a step. evidence: in the vendor docs · calling it writes · required: stepId

- **delete_list** Permanently delete a list (not the contacts). evidence: in the vendor docs · calling it writes

- **delete_saved_search** Permanently delete a saved search. evidence: in the vendor docs · calling it writes

- **delete_task** Permanently delete a task. evidence: in the vendor docs · calling it writes

- **delete_template** Permanently delete a template. evidence: in the vendor docs · calling it writes

- **execute_campaign_action** Control campaign lifecycle: start, pause, resume, complete, archive. evidence: in the vendor docs · calling it writes · required: campaignId, action

- **execute_campaign_step_action** Pause, resume, or skip a step. evidence: in the vendor docs · calling it reads · required: stepId, action

- **execute_task_action** pause, reschedule, complete, cancel, etc. evidence: in the vendor docs · calling it reads

- **get_activity_feed** Engagement feed: opens, replies, bounces, calls. evidence: in the vendor docs · calling it reads

- **get_campaign_metrics** Per-step engagement metrics. evidence: in the vendor docs · calling it reads · required: campaignId

- **get_credits** Current credit balance and usage. evidence: in the vendor docs · calling it reads

- **get_email_draft** Retrieve a draft. evidence: in the vendor docs · calling it reads

- **get_lists** List all contact lists, or get one by ID. evidence: in the vendor docs · calling it reads

- **get_my_companies** Saved/researched companies within a date range (max 30 days). evidence: in the vendor docs · calling it reads · required: startDate, endDate

- **get_my_contacts** Saved/researched contacts within a date range (max 30 days). evidence: in the vendor docs · calling it reads · required: startDate, endDate

- **list_call_dispositions** List disposition options (e.g. Left Voicemail). evidence: in the vendor docs · calling it reads

- **list_call_sentiments** List sentiment options (e.g. Positive). evidence: in the vendor docs · calling it reads

- **list_campaign_contacts** List contacts with engagement status. evidence: in the vendor docs · calling it reads · required: campaignId

- **list_campaign_steps** List steps with type, status, delay. evidence: in the vendor docs · calling it reads · required: campaignId

- **list_campaigns** List campaigns or get one by ID. evidence: in the vendor docs · calling it reads

- **list_email_accounts** List connected sender addresses. evidence: in the vendor docs · calling it reads

- **list_email_footers** List email footers for campaigns and templates. evidence: in the vendor docs · calling it reads

- **list_saved_searches** List all saved searches, or get one by ID. evidence: in the vendor docs · calling it reads

- **list_tasks** List tasks or get one by ID. evidence: in the vendor docs · calling it reads

- **list_templates** List templates or get one by ID. evidence: in the vendor docs · calling it reads

- **log_call** Log call outcome for a contact. evidence: in the vendor docs · calling it reads · required: contactId

- **poll_company_research** Check status of company enrichment requests. evidence: in the vendor docs · calling it reads · required: requestIds

- **poll_contact_research** Check status of contact enrichment requests. evidence: in the vendor docs · calling it reads · required: requestIds

- **remove_contacts_from_campaign** Remove contacts. evidence: in the vendor docs · calling it writes · required: campaignId, contactIds

- **research_companies** Enrich companies for revenue, size, technologies, etc. evidence: in the vendor docs · calling it reads · required: searchResultIds

- **research_contacts** Enrich contacts for verified email and phone. evidence: in the vendor docs · calling it reads

- **search_companies** Search companies by name, domain, industry, size, revenue, and more. Returns a paginated table. evidence: in the vendor docs · calling it reads

- **search_contacts** Search contacts by company, job title, seniority, location, industry, and more. Returns a paginated table. evidence: in the vendor docs · calling it reads

- **send_bulk_email** Send to contacts matching filters. evidence: in the vendor docs · calling it writes

- **send_email** Send in one step. evidence: in the vendor docs · calling it writes · required: contactId, from, to

- **send_email_draft** Send a saved draft. evidence: in the vendor docs · calling it writes

- **send_email_preview** Send preview to yourself before launch. evidence: in the vendor docs · calling it writes

- **update_campaign** Update name, visibility, or linked email accounts. evidence: in the vendor docs · calling it writes · required: id

- **update_campaign_step** Update step content or position. evidence: in the vendor docs · calling it writes · required: stepId

- **update_email_draft** Update draft content. evidence: in the vendor docs · calling it writes

- **update_list** Rename an existing list. evidence: in the vendor docs · calling it reads

- **update_saved_search** Update name, values, or sort options. evidence: in the vendor docs · calling it writes

- **update_task** Update name, due date, priority, status. evidence: in the vendor docs · calling it writes

- **update_template** Update name, subject, or body. evidence: in the vendor docs · calling it writes

119 of the 521 entries that record an official or community MCP server carry a harvested tool list. The other 402 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: seamless
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g seamless-ai-cli
```

quoted from [https://www.npmjs.com/package/seamless-ai-cli](https://www.npmjs.com/package/seamless-ai-cli) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: seamless-ai-cli 0.1.8, third party](https://www.npmjs.com/package/seamless-ai-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only

**API documentation**

No documentation URL recorded.

635 of 1032 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to seamless.ai with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

5 candidate accounts seen and rejected by the evidence rules: seamless-protocol, modelcontextprotocol, SeamlessAI, chainflip-io, seamless-test. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Search people by criteria](../jobs/search-people-by-criteria.md)
- [Search companies by firmographics](../jobs/search-companies-by-firmographics.md)
- [Build a target account list](../jobs/build-target-account-list.md)
- [Find a work email address](../jobs/find-work-email.md)
- [Find a phone number](../jobs/find-phone-number.md)
- [Research an account before a call](../jobs/research-account-for-call-prep.md)
- [Run an email sequence](../jobs/run-email-sequence.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 1,032 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://docs.seamless.ai/mcp-docs](https://docs.seamless.ai/mcp-docs)
- [https://seamless.ai/customers/blog/products/seamless-mcp-server](https://seamless.ai/customers/blog/products/seamless-mcp-server)
- [https://www.prweb.com/releases/seamlessais-new-mcp-server-takes-you-from-prompt-to-closed-won-deal-302839077.html](https://www.prweb.com/releases/seamlessais-new-mcp-server-takes-you-from-prompt-to-closed-won-deal-302839077.html)
- [https://salesintel.io/blog/seamless-ai-pricing/](https://salesintel.io/blog/seamless-ai-pricing/)
- [https://www.spendhound.com/marketplace/seamlessai-pricing](https://www.spendhound.com/marketplace/seamlessai-pricing)
- [https://www.cleanlist.ai/blog/2026-03-19-seamless-ai-pricing-guide](https://www.cleanlist.ai/blog/2026-03-19-seamless-ai-pricing-guide)
- [https://mcp.seamless.ai/mcp](https://mcp.seamless.ai/mcp)

7 source URLs. Raw sources field, verbatim:

https://docs.seamless.ai/mcp-docs, https://seamless.ai/customers/blog/products/seamless-mcp-server, https://www.prweb.com/releases/seamlessais-new-mcp-server-takes-you-from-prompt-to-closed-won-deal-302839077.html, https://salesintel.io/blog/seamless-ai-pricing/, https://www.spendhound.com/marketplace/seamlessai-pricing, https://www.cleanlist.ai/blog/2026-03-19-seamless-ai-pricing-guide, https://mcp.seamless.ai/mcp

**Notes, verbatim from the file**
Multiple independent pricing breakdowns put raw API access on Seamless's Enterprise tier only, with quoted contracts roughly $20k-$100k/year depending on seats/volume; consumer-facing Free/Basic/Pro plans are seat-and-credit based with no documented self-serve API key. Treat "MCP access must be enabled on your account" as effectively the same enterprise gate. 2026-09-07: https://mcp.seamless.ai/mcp returned 401 to an MCP initialize POST (https://mcp.seamless.ai/mcp).

**Provenance**

- **Entry id**: 01-seamless-ai

- **Source file**: 01-data-enrichment.md

- **Source line**: 312

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
