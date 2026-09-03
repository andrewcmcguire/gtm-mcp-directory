# WorkRamp: MCP server status, API access gate and what it does

> Corporate learning and training platform ("Business Academy") for employee onboarding, sales enablement, and... Community MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Enablement & Coaching](../categories/enablement-coaching.md) /
WorkRamp

# WorkRamp

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Enablement & Coaching](../categories/enablement-coaching.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [workramp.com (301s to confirm.com/scale-up/products/learn-up as of 2026-09-02; the product is now sold as Learn:Up by Confirm, "formerly WorkRamp")](https://workramp.com (301s to confirm.com/scale-up/products/learn-up as of 2026-09-02; the product is now sold as Learn:Up by Confirm, "formerly WorkRamp")) · entry id 11-workramp · source 11-enablement-coaching.md line 140

**What it does**
Corporate learning and training platform ("Business Academy") for employee onboarding, sales enablement, and customer education content, with AI-assisted content creation.

**AI features, separated from automation with an AI label on it**
"AI Assist" generates and personalizes learning content and recommendations - content-generation/recommendation AI layered on a traditional LMS core, not conversational roleplay or buyer simulation.

**RevOps role**
Onboarding/enablement LMS layer, reachable by AI agents only through third-party automation platforms (Zapier, viaSocket) rather than a vendor-hosted MCP server.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Rides Zapier's/viaSocket's own hosted-connector auth (their MCP gateway at mcp.zapier.com), not a WorkRamp-issued credential.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL[https://zapier.com/mcp/workramp](https://zapier.com/mcp/workramp)Probed**: 2026-09-03, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-03 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://zapier.com/mcp/workramp ; https://viasocket.com/mcp/workramp

- [https://zapier.com/mcp/workramp](https://zapier.com/mcp/workramp)
- [https://viasocket.com/mcp/workramp](https://viasocket.com/mcp/workramp)

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (the developer docs state this is a private API and you must contact support to see if you are eligible and request access, and it requires an enterprise account provisioned for Learn:Up - even though Learn:Up itself is self-serve from $9/user/mo)

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: no-job-fits. Corporate LMS, same call as Continu.

22 of 293 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://zapier.com/mcp/workramp](https://zapier.com/mcp/workramp)
- [https://viasocket.com/mcp/workramp](https://viasocket.com/mcp/workramp)
- [https://www.vendr.com/marketplace/workramp](https://www.vendr.com/marketplace/workramp)
- [https://getcor.ai/blog/reviews/workramp-pricing](https://getcor.ai/blog/reviews/workramp-pricing)
- [https://developers.workramp.com/](https://developers.workramp.com/)
- [https://www.confirm.com/scale-up/products/learn-up](https://www.confirm.com/scale-up/products/learn-up)

6 source URLs. Raw sources field, verbatim:

https://zapier.com/mcp/workramp, https://viasocket.com/mcp/workramp, https://www.vendr.com/marketplace/workramp, https://getcor.ai/blog/reviews/workramp-pricing, https://developers.workramp.com/, https://www.confirm.com/scale-up/products/learn-up

**Notes, verbatim from the file**
Both MCP entries are third-party hosted connectors (Zapier and viaSocket), not a WorkRamp-published server - hence community, not official. Exposes 11 triggers plus create-assignment/onboard-user/update-profile write actions per Zapier's documented action list. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://developers.workramp.com/): the developer docs state this is a private API and you must contact support to see if you are eligible and request access, and it requires an enterprise account provisioned for Learn:Up - even though Learn:Up itself is self-serve from $9/user/mo. 2026-09-02: rebrand confirmed. https://www.workramp.com/ 301s to https://www.confirm.com/scale-up/products/learn-up, where the product is branded Learn:Up, "Formerly WorkRamp", an AI-driven LMS inside Confirm's suite; that page has no MCP mention. https://zapier.com/mcp/workramp still returned 200 today, so mcp_status community (third-party hosted connectors) is unchanged.

**Provenance**

- **Entry id**: 11-workramp

- **Source file**: 11-enablement-coaching.md

- **Source line**: 140

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-03

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
