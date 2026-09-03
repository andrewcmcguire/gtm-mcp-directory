# Dialworks: MCP server status, API access gate and what it does

> Sales and support training platform running mock calls, simulated training scenarios, AI call assessment, and... No MCP found, Gate unknown. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Enablement & Coaching](../categories/enablement-coaching.md) /
Dialworks

# Dialworks

[No MCP found](../mcp/none-found.md)
[Gate unknown](../gates/unknown.md)
[Enablement & Coaching](../categories/enablement-coaching.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [dialworks.io](https://dialworks.io) · entry id 11-dialworks · source 11-enablement-coaching.md line 121

**What it does**
Sales and support training platform running mock calls, simulated training scenarios, AI call assessment, and analytics/reporting for rep readiness.

**AI features, separated from automation with an AI label on it**
AI-driven mock-call assessment and simulated training scenarios are the core product per vendor material; the underlying model mechanics (dynamic persona vs. scripted branching) were not independently confirmed in sources reviewed - treat as vendor-stated pending deeper technical documentation.

**RevOps role**
Lower-friction, trial-accessible entrant in the practice/roleplay category, positioned by third-party comparison sites as the "transparent pricing, rapid deployment" option.

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

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown - vendor offers a 30-day free trial with $3,000 in credits and no credit card required (self-serve-friendly), but sources point custom/large-team pricing to a direct sales contact, so full API-tier gating could not be confirmed.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Score rep performance](../jobs/score-rep-performance.md)
- [Run a sales roleplay practice](../jobs/run-sales-roleplay-practice.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://dialworks.io/pricing](https://dialworks.io/pricing)
- [https://www.xpay.sh/saas-pricing/dialworks-io/](https://www.xpay.sh/saas-pricing/dialworks-io/)
- [https://dialfyne.com/blog/ai-sales-roleplay-platform-comparison-2026](https://dialfyne.com/blog/ai-sales-roleplay-platform-comparison-2026)
- [https://www.dialworks.io/pricing](https://www.dialworks.io/pricing)

4 source URLs. Raw sources field, verbatim:

https://dialworks.io/pricing, https://www.xpay.sh/saas-pricing/dialworks-io/, https://dialfyne.com/blog/ai-sales-roleplay-platform-comparison-2026, https://www.dialworks.io/pricing

**Notes, verbatim from the file**
No MCP server found on GitHub, mcp.so, glama.ai, or pulsemcp.com. dialworks.io/pricing returned a TLS certificate error on direct fetch during this pass - pricing facts here are drawn from third-party trackers (xpay.sh) rather than the vendor page directly; re-verify by hand. [api_gate 2026-08-25] Re-checked and left unknown, honestly: the vendor site is unreachable - dialworks.io serves an expired TLS certificate, so neither the homepage nor /pricing could be loaded on www or apex. Worth re-checking on the next weekly verify run; an expired certificate is often the first visible sign of an abandoned product. Checked against https://www.dialworks.io/pricing. 2026-09-02: re-checked. https://dialworks.io/ still serves an expired TLS certificate (a strict fetch fails with "certificate has expired"); with certificate checking disabled the origin answers 200 with a 95 KB HTML page from nginx, so the site is up but unmaintained at the certificate level, and that page contains no MCP mention. The official MCP registry has no dialworks entry. mcp_status none-found unchanged; the certificate is still the open question for the next verify run.

**Provenance**

- **Entry id**: 11-dialworks

- **Source file**: 11-enablement-coaching.md

- **Source line**: 121

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
