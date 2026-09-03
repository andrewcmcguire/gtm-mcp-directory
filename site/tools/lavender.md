# Lavender: MCP server status, API access gate and what it does

> A Chrome extension and browser sidebar that sits inside Gmail, Outlook, and sales engagement tools and scores... No MCP found, Gate unknown. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Enablement & Coaching](../categories/enablement-coaching.md) /
Lavender

# Lavender

[No MCP found](../mcp/none-found.md)
[Gate unknown](../gates/unknown.md)
[Enablement & Coaching](../categories/enablement-coaching.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [lavender.ai](https://lavender.ai) · entry id 11-lavender · source 11-enablement-coaching.md line 254

**What it does**
A Chrome extension and browser sidebar that sits inside Gmail, Outlook, and sales engagement tools and scores a rep's email draft 1-100 in real time while suggesting rewrites, with a team dashboard that turns those scores into coaching data.

**AI features, separated from automation with an AI label on it**
Genuinely model-driven in part - the vendor describes the scoring and rewrite suggestions as running on "Open AI systems, self-hosted fine-tuned large language models, and LLMs powered by billions of custom data points," plus an AI Email Writer and personalization assistant that pulls prospect context. Vendor-stated, not independently verified. The scoring rubric itself (length, reading level, question placement, tone, mobile-friendliness) reads closer to a heuristic checklist than a model output. A separate 2026 product, Ora, is an autonomous agent that researches prospects and writes and sends cold email; it is a different SKU, not part of the Email Coach.

**RevOps role**
Coaching and quality-control layer on top of whatever sending tool the team already uses; it does not own the sequence, the inbox, or the send.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-09-02.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

none

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown - there is no docs.lavender.ai, no developer or API page, and no API reference on lavender.ai. APITracker's Lavender profile shows dashes for "Developer docs," "API Reference," and "Authentication." Lavender's capability is reachable programmatically only as a third-party integration, notably Clay's native "Rate Your Emails with Lavender" enrichment action, which is billed in Clay credits and is not a Lavender-issued API key. Recorded as unknown rather than none, because the absence of a public docs page is not proof that no partner API exists.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

[https://www.lavender.ai/coach (no developer or API documentation exists; the only support resource is the vendor Knowledge Library)](https://www.lavender.ai/coach (no developer or API documentation exists; the only support resource is the vendor Knowledge Library))

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.lavender.ai/](https://www.lavender.ai/)
- [https://www.lavender.ai/coach](https://www.lavender.ai/coach)
- [https://www.lavender.ai/paid-ai-email-coach](https://www.lavender.ai/paid-ai-email-coach)
- [https://lavender.ai/ora](https://lavender.ai/ora)
- [https://apitracker.io/a/trylavender](https://apitracker.io/a/trylavender)
- [https://www.clay.com/integrations/action/rate-your-emails-lavender](https://www.clay.com/integrations/action/rate-your-emails-lavender)
- [https://www.pulsemcp.com/servers?q=lavender](https://www.pulsemcp.com/servers?q=lavender)
- [https://glama.ai/mcp/servers?query=lavender](https://glama.ai/mcp/servers?query=lavender)

8 source URLs. Raw sources field, verbatim:

https://www.lavender.ai/, https://www.lavender.ai/coach, https://www.lavender.ai/paid-ai-email-coach, https://lavender.ai/ora, https://apitracker.io/a/trylavender, https://www.clay.com/integrations/action/rate-your-emails-lavender, https://www.pulsemcp.com/servers?q=lavender, https://glama.ai/mcp/servers?query=lavender

**Notes, verbatim from the file**
Added 2026-08-25 to close a known directory gap (Lavender was missing entirely). Pricing from the vendor's own page, annual billing: Basic free (5 emails/month analyzed, 5 personalized, Gmail and Outlook 365), Starter $27/mo, Individual Pro $45/mo (adds integrations), Team $89/seat/mo (adds the Coaching Dashboard, aggregated email analytics, and human-led coaching). Monthly billing is $29 / $49 / $99. Free for students, jobseekers, and bootstrapped founders. Ora is priced separately, free to build an agent then roughly $500/agent/month at launch per third-party trackers, not confirmed on the vendor site. MCP search was negative across PulseMCP (0 results), Glama (0 results), GitHub-scoped search, and general web search; Lavender's own site has no MCP mention. Listed integrations: Gmail, Outlook, Outreach, Salesloft, HubSpot, Apollo, Groove, Gong. CATEGORY CALL: filed here rather than in 02-engagement-outbound because the paid product is a scoring and critique layer around a human writing in a tool someone else owns, and its team tier is literally a coaching dashboard plus human-led coaching. Ora is the piece that would belong in 02 or 04 and deserves its own entry there if it grows. [api_gate 2026-08-25] Re-checked and left unknown, honestly: pricing is fully published and self-serve (Basic free forever $0, Starter $27/mo annual, Individual Pro $45, Team $89 per seat, plus Ora at $500 per agent per month) but no tier mentions API or developer access, higher tiers say only integrations, and no API docs are reachable (/api 404s, docs.lavender.ai returns 403). Checked against https://www.lavender.ai/coach. 2026-09-02: re-checked lavender.ai (no llms.txt), the official MCP registry (no entry) and a web search; no MCP server found.

**Provenance**

- **Entry id**: 11-lavender

- **Source file**: 11-enablement-coaching.md

- **Source line**: 254

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
