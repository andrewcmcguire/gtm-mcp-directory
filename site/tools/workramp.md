# WorkRamp: MCP server status, API access gate and what it does

> Corporate learning and training platform ("Business Academy") for employee onboarding, sales enablement, and... Community MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Enablement & Coaching](../categories/enablement-coaching.md) /
WorkRamp

# WorkRamp

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Enablement & Coaching](../categories/enablement-coaching.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

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

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://zapier.com/mcp/workramp](https://zapier.com/mcp/workramp)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://app.workramp.com/mcp ; https://zapier.com/mcp/workramp ; https://viasocket.com/mcp/workramp ; repo https://github.com/msdanyg/workramp-mcp

- [https://app.workramp.com/mcp](https://app.workramp.com/mcp)
- [https://zapier.com/mcp/workramp](https://zapier.com/mcp/workramp)
- [https://viasocket.com/mcp/workramp](https://viasocket.com/mcp/workramp)
- [https://github.com/msdanyg/workramp-mcp](https://github.com/msdanyg/workramp-mcp)

**What this server exposes**

- **Tools named**: 31
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-08
- **Repo read**: msdanyg/workramp-mcp
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **workramp_academy_get_registrations** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_academy_list_certifications** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_academy_list_collections** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_academy_list_contacts** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_academy_list_paths** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_academy_list_trainings** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_create_guide_assignment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_create_item_folder** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_create_path_assignment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_create_user** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_get_certification_awards** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_get_content_catalog** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_get_group_users** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_get_item_folder** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_get_user_assignments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_get_user_awards** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_certifications** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_events** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_groups** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_guide_assignments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_guides** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_item_folders** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_path_assignments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_paths** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_resources** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_scorm_assignments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_scorm_courses** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_list_users** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_search_libraries** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_test_connection** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **workramp_update_user** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

122 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 103 are unmeasured, which is not the same as empty. Harvest last run 2026-09-08. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-08 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (the developer docs state this is a private API and you must contact support to see if you are eligible and request access, and it requires an enterprise account provisioned for Learn:Up - even though Learn:Up itself is self-serve from $9/user/mo)

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/msdanyg/workramp-mcp](https://github.com/msdanyg/workramp-mcp)

**On GitHub**

No GitHub organisation could be tied to workramp.com with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

2 candidate accounts seen and rejected by the evidence rules: msdanyg, workramp. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: no-job-fits. Corporate LMS, same call as Continu.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://zapier.com/mcp/workramp](https://zapier.com/mcp/workramp)
- [https://viasocket.com/mcp/workramp](https://viasocket.com/mcp/workramp)
- [https://www.vendr.com/marketplace/workramp](https://www.vendr.com/marketplace/workramp)
- [https://getcor.ai/blog/reviews/workramp-pricing](https://getcor.ai/blog/reviews/workramp-pricing)
- [https://developers.workramp.com/](https://developers.workramp.com/)
- [https://www.confirm.com/scale-up/products/learn-up](https://www.confirm.com/scale-up/products/learn-up)
- [https://github.com/msdanyg/workramp-mcp](https://github.com/msdanyg/workramp-mcp)
- [https://app.workramp.com/mcp](https://app.workramp.com/mcp)

8 source URLs. Raw sources field, verbatim:

https://zapier.com/mcp/workramp, https://viasocket.com/mcp/workramp, https://www.vendr.com/marketplace/workramp, https://getcor.ai/blog/reviews/workramp-pricing, https://developers.workramp.com/, https://www.confirm.com/scale-up/products/learn-up, https://github.com/msdanyg/workramp-mcp, https://app.workramp.com/mcp

**Notes, verbatim from the file**
Both MCP entries are third-party hosted connectors (Zapier and viaSocket), not a WorkRamp-published server - hence community, not official. Exposes 11 triggers plus create-assignment/onboard-user/update-profile write actions per Zapier's documented action list. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://developers.workramp.com/): the developer docs state this is a private API and you must contact support to see if you are eligible and request access, and it requires an enterprise account provisioned for Learn:Up - even though Learn:Up itself is self-serve from $9/user/mo. 2026-09-02: rebrand confirmed. https://www.workramp.com/ 301s to https://www.confirm.com/scale-up/products/learn-up, where the product is branded Learn:Up, "Formerly WorkRamp", an AI-driven LMS inside Confirm's suite; that page has no MCP mention. https://zapier.com/mcp/workramp still returned 200 today, so mcp_status community (third-party hosted connectors) is unchanged. 2026-09-07: msdanyg/workramp-mcp is a real server (pyproject.toml, src/workramp_mcp/server.py + client.py; README: "An MCP server for the WorkRamp LMS API ... enroll users, assign learning paths, audit certifications") but the owner is an individual (homepage cmoconfessions.com), so it supports community only (https://github.com/msdanyg/workramp-mcp).

**Provenance**

- **Entry id**: 11-workramp

- **Source file**: 11-enablement-coaching.md

- **Source line**: 140

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-08

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
