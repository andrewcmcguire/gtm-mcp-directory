# BetterContact: MCP server status, API access gate and what it does

> A waterfall enrichment orchestrator that queries 20+ third-party email/phone data providers in sequence for a... No MCP found, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
BetterContact

# BetterContact

[No MCP found](../mcp/none-found.md)
[Free to start](../gates/free.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [bettercontact.rocks](https://bettercontact.rocks) · entry id 01-bettercontact · source 01-data-enrichment.md line 274

**What it does**
A waterfall enrichment orchestrator that queries 20+ third-party email/phone data providers in sequence for a given contact, stopping once a verified match is found, rather than sourcing its own proprietary contact data.

**AI features, separated from automation with an AI label on it**
Vendor markets a "BetterAI algorithm" that decides the optimal order to query the 20+ underlying providers for a given contact - this is a sequencing/routing heuristic layered on top of other vendors' data, not a source of new contact data itself. The actual email/phone lookups still come from third-party providers via a 4-layer verification pass; call the "AI" label a thin optimization layer over automation, not a core AI product.

**RevOps role**
A meta-layer/orchestrator that sits above single-provider tools (Prospeo, Findymail, Dropcontact) in a RevOps stack, chaining them together to raise overall match rate rather than replacing them; commonly plugged into Clay, Make, or Zapier workflows.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: not recorded

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

none-found

The mcp_url field is empty on this entry. 21 of 293 entries are.

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

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://composio.dev/toolkits/bettercontact](https://composio.dev/toolkits/bettercontact)
- [https://bettercontact.rocks/pricing/](https://bettercontact.rocks/pricing/)
- [https://bettercontact.rocks/](https://bettercontact.rocks/)
- [https://doc.bettercontact.rocks/quickstart](https://doc.bettercontact.rocks/quickstart)
- [https://www.globenewswire.com/news-release/2025/11/26/3195350/0/en/AI-Powered-Waterfall-Enrichment-Platform-BetterContact-Announces-Partnership-with-Clay-for-Berlin-GTM-Community-Event.html](https://www.globenewswire.com/news-release/2025/11/26/3195350/0/en/AI-Powered-Waterfall-Enrichment-Platform-BetterContact-Announces-Partnership-with-Clay-for-Berlin-GTM-Community-Event.html)

5 source URLs. Raw sources field, verbatim:

https://composio.dev/toolkits/bettercontact, https://bettercontact.rocks/pricing/, https://bettercontact.rocks/, https://doc.bettercontact.rocks/quickstart, https://www.globenewswire.com/news-release/2025/11/26/3195350/0/en/AI-Powered-Waterfall-Enrichment-Platform-BetterContact-Announces-Partnership-with-Clay-for-Berlin-GTM-Community-Event.html

**Notes, verbatim from the file**
No genuine MCP server found despite checking bettercontact.rocks, kb.bettercontact.rocks, and doc.bettercontact.rocks directly - none mention MCP. A GitHub repo ("upivi982/bettercontact") surfaced in search but is an unaffiliated affiliate-marketing README (tracked referral links, no actual code) - not a real MCP server, not counted. BetterContact also appears only via Composio's generic multi-app connector, not counted per the same standard applied to Datagma. BetterContact announced a Clay partnership/co-hosted event (Nov 2025) and is positioned as Clay-compatible. Pricing is self-serve from a 50-credit free trial (no card) and a $15/mo Starter tier (200 credits) with API included; "use your own API keys" is a $199 add-on specifically on the Starter tier (included free at Enterprise, $799/mo+).

**Provenance**

- **Entry id**: 01-bettercontact

- **Source file**: 01-data-enrichment.md

- **Source line**: 274

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
