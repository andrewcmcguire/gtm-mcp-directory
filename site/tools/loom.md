# Loom: MCP server status, API access gate and what it does

> Async video-messaging platform; in its sales use case, reps record personalized video messages with... Community MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Loom

# Loom

[Community MCP](../mcp/community.md)
[Free to start](../gates/free.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [loom.com](https://loom.com) · entry id 08-loom · source 08-video-prospecting.md line 33

**What it does**
Async video-messaging platform; in its sales use case, reps record personalized video messages with name/company variables, track prospect views, and embed CTAs/booking links directly in the video.

**AI features, separated from automation with an AI label on it**
Vendor states (Business+AI / Enterprise tiers only) AI-generated titles/summaries/auto-chapters, automatic filler-word/silence removal, an AI-drafted follow-up email companion, and transcription/captioning in 50+ languages (base transcription ships even on the free tier; the AI enrichment layer is gated). Variable-based name/company personalization, view tracking, and CTA embedding are plain templating/automation, not AI, despite being marketed alongside the AI features. Vendor's own 18% engagement-lift claim not independently verified.

**RevOps role**
Lower-overhead async video touch for individual AEs/SDRs/CSMs - follow-ups and lightweight prospecting rather than a managed outbound-campaign engine.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: karbassi/mcp-loom uses Loom's undocumented internal GraphQL API via a browser session cookie (connect.sid) manually extracted from a logged-in session - no official API key exists for this per the project's own README.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/karbassi/mcp-loom (largest community implementation, ~58 tools against Loom's internal GraphQL API); smaller variants at https://github.com/m2ai-mcp-servers/loom-mcp and https://github.com/CaliLuke/loom-mcp

- [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom)
- [https://github.com/m2ai-mcp-servers/loom-mcp](https://github.com/m2ai-mcp-servers/loom-mcp)
- [https://github.com/CaliLuke/loom-mcp](https://github.com/CaliLuke/loom-mcp)

**What this server exposes**

- **Tools named**: 60
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: karbassi/mcp-loom
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **add_comment_reaction** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **add_reaction** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **add_to_watch_later** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **approve_task** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **archive_videos** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_comment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_folder** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_task** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_comment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_folders** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_reaction** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_task** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_video** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **duplicate_video** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **edit_comment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_backlinks** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_captions** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_chapters** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_comment_reactions** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_comments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_confluence_pages** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_description** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_download_url** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_folder** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_frequent_reactions** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_key_takeaways** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_last_watch_time** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_meeting_notes** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_reactions** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_space** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_summary** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_tags** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_tasks** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_total_videos_count** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_transcript** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_user** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_video** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_video_details** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_watch_later_count** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_folders** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_spaces** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_videos** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **move_folders** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **move_videos** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **pin_video** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **recover_video** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **regenerate_mp4** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **remove_from_watch_later** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **rename_folder** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **respond_to_task** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_folders** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_videos** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **search_workspace_tags** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **share_videos_to_spaces** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **toggle_following** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **toggle_following_tag** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_task** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_video_description** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_video_name** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_video_settings** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 251 entries that record an official or community MCP server carry a harvested tool list. The other 132 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free (recordSDK and embedSDK are self-serve via a developer-portal account and Loom's own dev site says start building with recordSDK today for free; this is a record/embed SDK rather than a general REST API and no SDK pricing tiers are published)

**API documentation**

No documentation URL recorded.

374 of 468 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/CaliLuke/loom-mcp](https://github.com/CaliLuke/loom-mcp)
- [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom)
- [https://github.com/m2ai-mcp-servers/loom-mcp](https://github.com/m2ai-mcp-servers/loom-mcp)

**On GitHub**

[github.com/loomhq](https://github.com/loomhq) tied to the vendor by rule 3, account website https://www.loom.com has the vendor's domain, confidence strong

- **Public repositories**: 5, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [eks-ng-ami-updater](https://github.com/loomhq/eks-ng-ami-updater) | infrastructure | EKS NG AMI Updater is an open source project that can be used to update kubernetes node group images. | 28 | 2026-09-08 | |
| [lock-exec](https://github.com/loomhq/lock-exec) | CLI | A CLI tool for running any shell based commands in a distributed environment with DynamoDB locking. | 7 | 2026-09-04 | v2.3.0 |
| [datadog-exporter](https://github.com/loomhq/datadog-exporter) | other | export and backup datadog resource definitions locally | 1 | 2026-09-03 | v1.2.0 |
| [cmake-orb](https://github.com/loomhq/cmake-orb) | other | CircleCI Orb for CMake Installation and Caching | 0 | 2023-02-03 | 1.0.0 |
| [ElectronMacOSClickThrough](https://github.com/loomhq/ElectronMacOSClickThrough) | other | An Add On workaround for transparent window click through issues on electron v8 and above | 8 | 2021-04-16 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Create and send a prospecting video](../jobs/create-and-send-prospecting-video.md)
- [Read outreach performance](../jobs/read-outreach-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 468 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.loom.com/use-case/sales](https://www.loom.com/use-case/sales)
- [https://www.loom.com/pricing](https://www.loom.com/pricing)
- [https://www.loom.com/sdk](https://www.loom.com/sdk)
- [https://github.com/karbassi/mcp-loom](https://github.com/karbassi/mcp-loom)
- [https://jira.atlassian.com/browse/LOOM-690](https://jira.atlassian.com/browse/LOOM-690)
- [https://dev.loom.com/](https://dev.loom.com/)

6 source URLs. Raw sources field, verbatim:

https://www.loom.com/use-case/sales, https://www.loom.com/pricing, https://www.loom.com/sdk, https://github.com/karbassi/mcp-loom, https://jira.atlassian.com/browse/LOOM-690, https://dev.loom.com/

**Notes, verbatim from the file**
Loom's dominant real-world use case remains general screen-recording/async communication, not outbound sales specifically - this entry evaluates only the sales-messaging angle per research scope. Watch for name collisions: several "Loom MCP" search results (e.g. a PulseMCP listing, maxsloef/loom-mcp) belong to an unrelated text/prompt-exploration tool that also happens to be called "loom." [api_gate 2026-08-25] Reclassified unknown -> free from the vendor's own page (https://dev.loom.com/): recordSDK and embedSDK are self-serve via a developer-portal account and Loom's own dev site says start building with recordSDK today for free; this is a record/embed SDK rather than a general REST API and no SDK pricing tiers are published.

**Provenance**

- **Entry id**: 08-loom

- **Source file**: 08-video-prospecting.md

- **Source line**: 33

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
