# Vector (vector.co): MCP server status, API access gate and what it does

> Identifies named individual buyers (not just companies) by resolving anonymous website visitors and ad-click... MCP unknown, Paid, self-serve. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Signals & Intent](../categories/signals-intent-abm.md) /
Vector (vector.co)

# Vector (vector.co)

[MCP unknown](../mcp/unknown.md)
[Paid, self-serve](../gates/paid.md)
[Signals & Intent](../categories/signals-intent-abm.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [https://www.vector.co](https://www.vector.co) · entry id 05-vector · source 05-signals-intent-abm.md line 183

**What it does**
Identifies named individual buyers (not just companies) by resolving anonymous website visitors and ad-click engagement to real contacts, then tracks their behavior (job changes, CRM activity, ad engagement) across the buyer journey via a "Shared Experience Graph."

**AI features, separated from automation with an AI label on it**
Vendor claims a "proprietary AI model" for relationship/signal scoring - unverified marketing language. The announced "Vector MCP" is a genuine LLM-integration point, but the intelligence lives in the connected LLM client, not in a Vector-owned model.

**RevOps role**
Contact-level (not just account-level) intent capture feeding both sales alerting and paid-ad audience activation.

**MCP server**

- **Status bucket**: MCP unknown

- **Auth**: unknown - the vendor says the MCP 'lives in Claude' but publishes no auth or setup details

- **Parsed URLs**: 1 found in the mcp_url field

The check could not settle it either way. Unknown is a legal answer and it is published rather than guessed. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

unknown

mcp_url, verbatim from the file:

https://www.vector.co/blog/we-built-an-mcp-for-marketing-heres-what-it-actually-does (vendor's own launch post, 2026-05-06, early-access signup only; no endpoint, docs or repo published)

- [https://www.vector.co/blog/we-built-an-mcp-for-marketing-heres-what-it-actually-does](https://www.vector.co/blog/we-built-an-mcp-for-marketing-heres-what-it-actually-does)

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

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 293 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.vector.co/](https://www.vector.co/)
- [https://www.vector.co/pricing](https://www.vector.co/pricing)
- [https://www.vector.co/blog/product-release-what-does-vector-do](https://www.vector.co/blog/product-release-what-does-vector-do)
- [https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers](https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers)
- [https://www.ycombinator.com/companies/vector](https://www.ycombinator.com/companies/vector)
- [https://www.prnewswire.com/news-releases/vector-raises-10m-series-a-to-build-the-ai-ad-platform-that-makes-marketers-better-not-obsolete-302770353.html](https://www.prnewswire.com/news-releases/vector-raises-10m-series-a-to-build-the-ai-ad-platform-that-makes-marketers-better-not-obsolete-302770353.html)
- [https://www.vector.co/blog/we-built-an-mcp-for-marketing-heres-what-it-actually-does](https://www.vector.co/blog/we-built-an-mcp-for-marketing-heres-what-it-actually-does)
- [https://www.vector.co/blog/how-vector-uses-vector-mcp](https://www.vector.co/blog/how-vector-uses-vector-mcp)
- [https://www.vector.co/llms.txt](https://www.vector.co/llms.txt)

9 source URLs. Raw sources field, verbatim:

https://www.vector.co/, https://www.vector.co/pricing, https://www.vector.co/blog/product-release-what-does-vector-do, https://www.vector.co/blog/what-is-an-mcp-and-why-were-building-it-for-marketers, https://www.ycombinator.com/companies/vector, https://www.prnewswire.com/news-releases/vector-raises-10m-series-a-to-build-the-ai-ad-platform-that-makes-marketers-better-not-obsolete-302770353.html, https://www.vector.co/blog/we-built-an-mcp-for-marketing-heres-what-it-actually-does, https://www.vector.co/blog/how-vector-uses-vector-mcp, https://www.vector.co/llms.txt

**Notes, verbatim from the file**
Disambiguated as the YC-backed, HubSpot Ventures/SignalFire-funded contact-based marketing "Vector" (Reveal + Target products), not any dev-tools product of the same name. Reveal plan is self-serve ($399-$999/mo, 14-day trial); Target (ad activation) requires an annual contract from $3,000/mo. Checked mcp.so and glama.ai directly - no listing found on either, consistent with waitlist-stage MCP. 2026-09-02: CHANGED none-found -> unknown. Vector's own blog now carries a launch series: 'We built an MCP for marketing. Here's what it actually does.' (2026-05-06), 'How Vector uses Vector MCP' (2026-05-14) and 'What can you actually ask your ads with Vector MCP?' (2026-05-26). The launch post describes V1 as read-only access to LinkedIn Ads performance plus de-anonymized site visitors and says the MCP 'lives in Claude', but the only call to action is 'Sign up for early access', and vector.co/mcp returns 404. No endpoint, setup docs, auth method or registry listing (registry search for vector.co is empty), so per law 1 this is a first-party claim without a URL that answers: unknown, not official.

**Provenance**

- **Entry id**: 05-vector

- **Source file**: 05-signals-intent-abm.md

- **Source line**: 183

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
