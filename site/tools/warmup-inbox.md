# Warmup Inbox: MCP server status, API access gate and what it does

> Email warmup and deliverability platform running a network of 30,000+ real inboxes that exchange... MCP unknown, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Warmup Inbox

# Warmup Inbox

[MCP unknown](../mcp/unknown.md)
[Free to start](../gates/free.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [warmupinbox.com](https://warmupinbox.com) · entry id 09-warmup-inbox · source 09-email-deliverability.md line 26

**What it does**
Email warmup and deliverability platform running a network of 30,000+ real inboxes that exchange natural-looking email (opens, replies, stars) with a customer's connected accounts to build sender reputation.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed; the warmup mechanic and blacklist monitoring read as automation, not model-driven analysis - treat as plain automation absent further evidence.

**RevOps role**
Deliverability-maintenance layer running behind an outbound sending tool, with programmatic control over creating/connecting inboxes and pulling placement metrics.

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: unknown - the vendor's own API docs describe API-key authentication (api.warmupinbox.com/api-doc, OpenAPI 3.0 spec), but MCP-specific auth was not independently confirmed.

- **Parsed URLs**: 1 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

https://www.warmupinbox.com/blog/product-updates/product-update-new-api/

- [https://www.warmupinbox.com/blog/product-updates/product-update-new-api/](https://www.warmupinbox.com/blog/product-updates/product-update-new-api/)

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free - the vendor states the API is "a free feature on every plan, with no extra charge."

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Warm up an inbox](../jobs/warm-up-inbox.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.warmupinbox.com/blog/product-updates/product-update-new-api/](https://www.warmupinbox.com/blog/product-updates/product-update-new-api/)
- [https://api.warmupinbox.com/api-doc](https://api.warmupinbox.com/api-doc)
- [https://documenter.getpostman.com/view/6493518/2s9YR3dFfb](https://documenter.getpostman.com/view/6493518/2s9YR3dFfb)

3 source URLs. Raw sources field, verbatim:

https://www.warmupinbox.com/blog/product-updates/product-update-new-api/, https://api.warmupinbox.com/api-doc, https://documenter.getpostman.com/view/6493518/2s9YR3dFfb

**Notes, verbatim from the file**
The vendor's own product-update blog post states Warmup Inbox is "SOC 2 compliant, with an API, MCP server, and CLI for automating warm-up across hundreds of domains" - a first-party claim on the vendor's own domain. However, a direct fetch of that page timed out and no dedicated MCP docs page, repo, or registry listing was independently reachable to confirm the claim, so this is left as unknown rather than official per the schema's "no URL, no claim" law - worth a follow-up hand-check.

**Provenance**

- **Entry id**: 09-warmup-inbox

- **Source file**: 09-email-deliverability.md

- **Source line**: 26

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-28

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
