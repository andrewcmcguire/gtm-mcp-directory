# MailGenius: MCP server status, API access gate and what it does

> Free/paid email deliverability and spam-testing tool - checks SPF/DKIM/DMARC authentication, scans... No MCP found, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
MailGenius

# MailGenius

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-09-02
CLI: genius (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [mailgenius.com](https://mailgenius.com) · entry id 09-mailgenius · source 09-email-deliverability.md line 83

**What it does**
Free/paid email deliverability and spam-testing tool - checks SPF/DKIM/DMARC authentication, scans blacklists, previews inbox rendering across Gmail/Outlook, and scores spam likelihood.

**AI features, separated from automation with an AI label on it**
No AI-specific capability confirmed; diagnostic checks (authentication records, header analysis, spam-trigger content scan) read as rules-based testing, not model-driven - treat as plain automation.

**RevOps role**
Pre-send deliverability-testing layer, typically run before a cold-email campaign launches rather than continuously in the background like a warmup tool.

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

- **Binary**: genius
- **Status**: community CLI, third party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-10

Install, as the source shows it:

```
npm install -g mailgenius-cli
```

quoted from [https://www.npmjs.com/package/mailgenius-cli](https://www.npmjs.com/package/mailgenius-cli) on 2026-09-10, via npm, a third party source

```
pip install mailgenius
```

quoted from [https://pypi.org/project/mailgenius/](https://pypi.org/project/mailgenius/) on 2026-09-10, via pypi, a third party source

Packages seen, with the version on 2026-09-10:

- [npm: mailgenius-cli 0.1.0, third party](https://www.npmjs.com/package/mailgenius-cli)
- [pypi: mailgenius 0.1.0, third party](https://pypi.org/project/mailgenius/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-10.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - a whitelabel/API tier exists but requires applying for access (mailgenius.com/api-application), not self-serve signup.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to mailgenius.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

1 candidate account seen and rejected by the evidence rules: mailgenius-com. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Check inbox placement](../jobs/check-inbox-placement.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.mailgenius.com/](https://www.mailgenius.com/)
- [https://www.mailgenius.com/api-application/](https://www.mailgenius.com/api-application/)
- [https://mcp.pipedream.com/app/mailgenius](https://mcp.pipedream.com/app/mailgenius)
- [https://coldiq.com/tools/mailgenius](https://coldiq.com/tools/mailgenius)

4 source URLs. Raw sources field, verbatim:

https://www.mailgenius.com/, https://www.mailgenius.com/api-application/, https://mcp.pipedream.com/app/mailgenius, https://coldiq.com/tools/mailgenius

**Notes, verbatim from the file**
A "MailGenius MCP Server" listing exists at mcp.pipedream.com/app/mailgenius, but Pipedream is a generic workflow-automation platform that auto-generates MCP wrappers around thousands of apps' APIs - it is not a MailGenius-published or dedicated community server, so this is marked none-found per this directory's convention (consistent with how Zapier-MCP-only listings are treated elsewhere in this file and the wider directory). 2026-09-02: re-checked mailgenius.com/llms.txt (404) and web search; only Pipedream and Runbear aggregator listings surface, no MCP server found.

**Provenance**

- **Entry id**: 09-mailgenius

- **Source file**: 09-email-deliverability.md

- **Source line**: 83

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-10

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
