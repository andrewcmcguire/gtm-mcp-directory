# mcp.run / TurboMCP: MCP server status, API access gate and what it does

> An enterprise self-hosted MCP gateway and management platform - a trusted, admin-curated registry plus... Official MCP, Enterprise only. Checked 2026-09-07.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
mcp.run / TurboMCP

# mcp.run / TurboMCP

[Official MCP](../mcp/official.md)
[Enterprise only](../gates/enterprise-only.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-07

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [turbomcp.ai (mcp.run now 301-redirects here)](https://turbomcp.ai (mcp.run now 301-redirects here)) · entry id 07-mcp-run-turbomcp · source 07-mcp-infrastructure.md line 80

**What it does**
An enterprise self-hosted MCP gateway and management platform - a trusted, admin-curated registry plus RBAC-controlled deployment of MCP servers across a team's own infrastructure (K8s, PaaS, VMs).

**AI features, separated from automation with an AI label on it**
none - this is a gateway/governance layer for MCP traffic, not an AI product.

**RevOps role**
Relevant to a RevOps/IT team that wants centralized control over which MCP servers its agents can reach, rather than an individual operator's connector of choice.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Integrates with a team's own OIDC-compatible identity provider; handles OAuth and Dynamic Client Registration for the servers it fronts.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://turbomcp.ai](https://turbomcp.ai)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-07. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official (this is infrastructure for running/gating other servers' MCP endpoints, not a single server itself)

mcp_url, verbatim from the file:

https://github.com/dylibso/mcp.run-servlets ; https://turbomcp.ai

- [https://github.com/dylibso/mcp.run-servlets](https://github.com/dylibso/mcp.run-servlets)
- [https://turbomcp.ai](https://turbomcp.ai)

**What this server exposes**

- **Tools named**: 55
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: dylibso/mcp.run-servlets
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **auth_get_url** Get a Trello authorization URL that will display an API token. This token is required for other Trello tools. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **bcrypt** Hash a string using bcrypt (recommended for passwords) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_add_member** Add a member to a board by email evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_create** Create a new Trello board. Note: when creating a board, some lists are automatically created. Check the existing lists before creating new ones. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_get** Get details about a Trello board evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_get_cards** Get all cards on a board evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_get_labels** Get all labels on a board evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_get_lists** Get all lists on a board evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_get_members** Get all members of a board evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_list** List all boards for the authenticated user evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **board_remove_member** Remove a member from a board evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **card_add_comment** Add a comment to a card evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **card_add_member** Assign a member to a card evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **card_create** Create a new card in a list evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **card_get_comments** Get all comments on a card evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **card_get_members** Get all members assigned to a card evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **card_move** Move a card to a different list and/or position evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **card_remove_member** Remove a member from a card evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **checklist_add_item** Add an item to a checklist evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **checklist_create** Create a new checklist on a card evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **comment_delete** Delete a comment from a card evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **gif-search** Search for GIFs on Tenor evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **google-maps-static-api-center** Returns an image, centered on the given evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **google-maps-static-api-markers** Returns an image, centered around the given evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **historical-flight-api** Get the flight arrivals and departures for a given airport by ICAO identifier within a given time range; or get the details and picture of a flight by callsign and ICAO24 hex code. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **label_create** Create a new label on a board evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **label_delete** Delete a label evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_archive_cards** Archive all cards in a list evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_create** Create a new list on a board evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_get_cards** Get all cards in a list with pagination evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_move** Move a list to a different board evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **maps_directions** Get directions between two points evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **maps_distance_matrix** Calculate travel distance and time for multiple origins and destinations evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **maps_elevation** Get elevation data for locations on the earth evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **maps_geocode** Convert an address into geographic coordinates evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **maps_place_details** Get detailed information about a specific place evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **maps_reverse_geocode** Convert coordinates into an address evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **maps_search_places** Search for places using Google Places API evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **md5** Hash a string using MD5 (Note: MD5 is not cryptographically secure, use for checksums only) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **sha1** Hash a string using SHA-1 (Note: SHA-1 is not recommended for new applications) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **sha256** Hash a string using SHA-256 (also called SHA2, cryptographically secure) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **transcribe** Transcribes an audio file using AssemblyAI and returns the transcription as text. Supports common audio formats (mp3, wav, FLAC, AAC, M4A, etc). Audio can be provided either as a file path or base64-encoded string. on windows, if the user g evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_category_create** Create a new WordPress category evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_category_list** List all WordPress categories evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_comment_approve** Approve a WordPress comment evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_comment_delete** Remove a WordPress comment evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_comment_list** List WordPress comments, optionally filtered by post evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_post_create** Create a new WordPress post evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_post_delete** Delete a WordPress post evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_post_edit** Edit an existing WordPress post evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_post_get** Get a single WordPress post by ID evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_post_list** List WordPress posts with pagination and filtering evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_post_schedule** Schedule a post for future publication evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_tag_create** Create a new WordPress tag evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **wp_tag_list** List all WordPress tags evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 264 entries that record an official or community MCP server carry a harvested tool list. The other 145 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (mcp.run 301s to turbomcp.ai, which publishes no pricing at all and positions as a self-hosted enterprise MCP gateway with only run-Turbo-MCP contact and book-a-demo as entry points)

**API documentation**

No documentation URL recorded.

400 of 514 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/dylibso/mcp.run-servlets](https://github.com/dylibso/mcp.run-servlets)

**On GitHub**

No GitHub organisation could be tied to turbomcp.ai with evidence on 2026-09-08.

Recorded by the harvest: github candidates were seen but none passed the evidence rules.

2 candidate accounts seen and rejected by the evidence rules: dylibso, mcp-run. A name match alone is never accepted; the account has to point at the vendor domain.

**Jobs it can do**

- [Discover MCP servers](../jobs/discover-mcp-servers.md)
- [Proxy tool calls to SaaS apps](../jobs/proxy-tool-calls-to-saas.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 514 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.mcp.run](https://www.mcp.run)
- [https://turbomcp.ai](https://turbomcp.ai)
- [https://github.com/dylibso/mcp.run-servlets](https://github.com/dylibso/mcp.run-servlets)
- (redirects to turbomcp.ai, confirmed 301)

3 source URLs. Raw sources field, verbatim:

https://www.mcp.run (redirects to turbomcp.ai, confirmed 301), https://turbomcp.ai, https://github.com/dylibso/mcp.run-servlets

**Notes, verbatim from the file**
mcp.run - originally a lightweight community MCP server registry - now redirects permanently to TurboMCP, an enterprise self-hosted gateway product. The fetched TurboMCP page does not mention its mcp.run history, so the nature/terms of that transition are unconfirmed; flagged as a gap rather than guessed. [api_gate 2026-08-25] Reclassified unknown -> enterprise-only from the vendor's own page (https://turbomcp.ai): mcp.run 301s to turbomcp.ai, which publishes no pricing at all and positions as a self-hosted enterprise MCP gateway with only run-Turbo-MCP contact and book-a-demo as entry points. 2026-09-02: re-verified. https://www.mcp.run/ still 301s to https://turbomcp.ai/, which loaded today as "the leading standards-compliant, self-hosted MCP gateway and management platform" (OIDC identity-provider integration, OAuth with dynamic client registration, RBAC approvals, centralized audit logs, kill switch) with no pricing, no docs link, and still no mention of its mcp.run history. The what_it_does and ai_features copy above already describes the TurboMCP product rather than the old hosted registry, so no rewrite was needed; mcp_status unchanged. 2026-09-07: THIS ROW CONFLATES TWO VENDORS AND NEEDS SPLITTING. mcp.run is dylibso, and the verified artifact is https://github.com/dylibso/mcp.run-servlets, whose README reads "These are the official servlets for the @dylibso account on mcp.run" and which is now ARCHIVED (archived=true, last push 2025-11-20). TurboMCP is a different project from a different owner: Epistates/turbomcp (https://github.com/Epistates/turbomcp), a Rust MCP SDK at turbomcp.org, which is what this row's vendor_domain turbomcp.ai points at. Two vendors in one row: split before publishing. Not split by this pass.

**Provenance**

- **Entry id**: 07-mcp-run-turbomcp

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 80

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-07

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
