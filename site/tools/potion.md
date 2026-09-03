# Potion: MCP server status, API access gate and what it does

> AI video-personalization tool for outbound sales - record one template video, and Potion overlays a... No MCP found, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Potion

# Potion

[No MCP found](../mcp/none-found.md)
[Gate unknown](../gates/unknown.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [sendpotion.com](https://sendpotion.com) · entry id 08-potion · source 08-video-prospecting.md line 109

**What it does**
AI video-personalization tool for outbound sales - record one template video, and Potion overlays a personalized version per prospect (dynamic name/logo/background) for cold email and LinkedIn outreach at scale.

**AI features, separated from automation with an AI label on it**
Vendor states personalization at scale (dynamic salutation, logo, and website/background overlay per prospect on a static template), a text-to-video option, AI demo-summarization, and (Enterprise tier) AI voice cloning. The core mechanism as described by the vendor is overlaying dynamic elements onto one recorded template rather than fully regenerating video per recipient - closer to templated personalization than generative AI video for most tiers. Not independently verified beyond vendor/third-party review pages.

**RevOps role**
Personalization layer bolted onto cold email/LinkedIn sequences (Outreach, Salesloft, HubSpot, Salesforce) to lift reply/booking rates - top-of-funnel only, not a broader video-hosting/CX platform.

**MCP server**

- **Status bucket**: No MCP found

- **Auth**: n/a

- **Parsed URLs**: 0 found in the mcp_url field

No server was found at the time of the check. That is a statement about the search, not a promise that none exists. The status was established on 2026-08-24.

mcp_status, verbatim from the file:

none-found

mcp_url, verbatim from the file:

n/a

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown. A personal API token exists (used to connect Zapier) but no public developer-API documentation or portal was found; API-related questions are routed to a support email rather than public docs.

32 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://sendpotion.com/ai-video-prospecting-software/](https://sendpotion.com/ai-video-prospecting-software/)
- [https://www.capterra.com/p/232470/Potion/](https://www.capterra.com/p/232470/Potion/)
- [https://coldiq.com/tools/potion](https://coldiq.com/tools/potion)
- [https://help.sendpotion.com/how-to-set-up-potion-and-zapier](https://help.sendpotion.com/how-to-set-up-potion-and-zapier)
- [https://www.sendpotion.com/pricing](https://www.sendpotion.com/pricing)

5 source URLs. Raw sources field, verbatim:

https://sendpotion.com/ai-video-prospecting-software/, https://www.capterra.com/p/232470/Potion/, https://coldiq.com/tools/potion, https://help.sendpotion.com/how-to-set-up-potion-and-zapier, https://www.sendpotion.com/pricing

**Notes, verbatim from the file**
Third-party pricing figures conflict meaningfully ($99/mo vs $250/mo "starting price," different video-volume caps); vendor's own pricing page was not successfully fetched in this research pass, so treat all price figures as third-party-reported, not primary-sourced. Search noise: "Potion" collides with an unrelated Minecraft server community and a Notion-API-clone GitHub project - neither relates to sendpotion.com. [api_gate 2026-08-25] Re-checked and left unknown, honestly: pricing is published (Starter $99/mo, Professional $299/mo, Enterprise custom) but never mentions an API - the only programmatic feature listed is Zapier Webhooks on Professional - and sendpotion.com/api returns 404. Checked against https://www.sendpotion.com/pricing.

**Provenance**

- **Entry id**: 08-potion

- **Source file**: 08-video-prospecting.md

- **Source line**: 109

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
