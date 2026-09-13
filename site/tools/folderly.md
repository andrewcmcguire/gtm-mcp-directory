# Folderly: MCP server status, API access gate and what it does

> Email deliverability platform combining a spam/inbox-placement test, ongoing deliverability monitoring,... No MCP found, Gate unknown. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Folderly

# Folderly

[No MCP found](../mcp/none-found.md)
[Gate unknown](../gates/unknown.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-09-02
CLI: folderly (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [folderly.com](https://folderly.com) · entry id 09-folderly · source 09-email-deliverability.md line 45

**What it does**
Email deliverability platform combining a spam/inbox-placement test, ongoing deliverability monitoring, technical DNS setup, and spam-trigger content review for B2B outbound teams.

**AI features, separated from automation with an AI label on it**
Vendor markets "deliverability fixes" and spam-trigger detection against best practices; no independent confirmation of model-driven (vs. rules-based checklist) mechanics was found - treat as vendor-stated only.

**RevOps role**
Deliverability-diagnosis and monitoring layer, positioned as a service-plus-software hybrid (the vendor emphasizes hands-on technical setup) rather than a pure self-serve tool.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: folderly
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
npm install -g folderly
```

quoted from [https://www.npmjs.com/package/folderly](https://www.npmjs.com/package/folderly) on 2026-09-12, via npm, a third party source

Packages seen, with the version on 2026-09-12:

- [npm: folderly 0.1.2, third party](https://www.npmjs.com/package/folderly)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

436 of 739 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

510 of 739 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to folderly.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

1 candidate account seen and rejected by the evidence rules: Folderly. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Provision sending infrastructure](../jobs/provision-sending-infrastructure.md)
- [Check inbox placement](../jobs/check-inbox-placement.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 739 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://folderly.com/](https://folderly.com/)
- [https://folderly.com/email-deliverability-monitoring](https://folderly.com/email-deliverability-monitoring)
- [https://folderly.com/products](https://folderly.com/products)
- [https://maildoso.ai/blog/catalog/warmup/folderly](https://maildoso.ai/blog/catalog/warmup/folderly)
- [https://folderly.com/pricing](https://folderly.com/pricing)

5 source URLs. Raw sources field, verbatim:

https://folderly.com/, https://folderly.com/email-deliverability-monitoring, https://folderly.com/products, https://maildoso.ai/blog/catalog/warmup/folderly, https://folderly.com/pricing

**Notes, verbatim from the file**
Search surfaced two unrelated inbox-placement MCP servers (github.com/live-direct-marketing/ldm-inbox-check-mcp and the "Unspam" MCP toolkit) that are NOT Folderly products - do not conflate. Folderly integrates via API/SMTP with major ESPs per its own site, but no self-serve pricing or developer-portal URL was found. [api_gate 2026-08-25] Re-checked and left unknown, honestly: pricing is published ($96/mo per mailbox, plus Inbox Insights free or $79/mo) and states nothing about a customer-facing API; the only API wording on the site is that Folderly integrates via API and SMTP with major email service providers, which describes Folderly consuming ESP APIs rather than offering one. folderly.com/api 404s and docs.folderly.com returned 522. Checked against https://folderly.com/pricing. 2026-09-02: re-checked folderly.com/llms.txt (present, no MCP mention) and web search (hits are Folderr and folder-mcp, unrelated); no MCP server found.

**Provenance**

- **Entry id**: 09-folderly

- **Source file**: 09-email-deliverability.md

- **Source line**: 45

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
