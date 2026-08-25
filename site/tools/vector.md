# Vector (vector.co): MCP server status, API access gate and what it does

> Identifies named individual buyers (not just companies) by resolving anonymous website visitors and ad-click... No MCP found, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Vector (vector.co)

# Vector (vector.co)

[No MCP found](../mcp/none-found.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.vector.co](https://www.vector.co) · entry id 05-vector · source 05-signals-intent-abm.md line 183

**What it does**
Identifies named individual buyers (not just companies) by resolving anonymous website visitors and ad-click engagement to real contacts, then tracks their behavior (job changes, CRM activity, ad engagement) across the buyer journey via a "Shared Experience Graph."

**AI features, separated from automation with an AI label on it**
Vendor claims a "proprietary AI model" for relationship/signal scoring - unverified marketing language. The announced "Vector MCP" is a genuine LLM-integration point, but the intelligence lives in the connected LLM client, not in a Vector-owned model.

**RevOps role**
Contact-level (not just account-level) intent capture feeding both sales alerting and paid-ad audience activation.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: unknown - not confirmed live

- **Parsed URLs**: 1 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers (vendor's own announcement - describes MCP as "rolling out soon," gated behind a waitlist, not a live repo/endpoint)

- [https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers](https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers)

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Track job changes](../jobs/track-job-changes.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.vector.co/](https://www.vector.co/)
- [https://www.vector.co/pricing](https://www.vector.co/pricing)
- [https://www.vector.co/blog/product-release-what-does-vector-do](https://www.vector.co/blog/product-release-what-does-vector-do)
- [https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers](https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers)
- [https://www.ycombinator.com/companies/vector](https://www.ycombinator.com/companies/vector)
- [https://www.prnewswire.com/news-releases/vector-raises-10m-series-a-to-build-the-ai-ad-platform-that-makes-marketers-better-not-obsolete-302770353.html](https://www.prnewswire.com/news-releases/vector-raises-10m-series-a-to-build-the-ai-ad-platform-that-makes-marketers-better-not-obsolete-302770353.html)

6 source URLs. Raw sources field, verbatim:

https://www.vector.co/, https://www.vector.co/pricing, https://www.vector.co/blog/product-release-what-does-vector-do, https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers, https://www.ycombinator.com/companies/vector, https://www.prnewswire.com/news-releases/vector-raises-10m-series-a-to-build-the-ai-ad-platform-that-makes-marketers-better-not-obsolete-302770353.html

**Notes, verbatim from the file**
Disambiguated as the YC-backed, HubSpot Ventures/SignalFire-funded contact-based marketing "Vector" (Reveal + Target products), not any dev-tools product of the same name. Reveal plan is self-serve ($399-$999/mo, 14-day trial); Target (ad activation) requires an annual contract from $3,000/mo. Checked mcp.so and glama.ai directly - no listing found on either, consistent with waitlist-stage MCP.

**Provenance**

- **Entry id**: 05-vector

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 183

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
