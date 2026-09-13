# Chorus: MCP server status, API access gate and what it does

> Records, transcribes, and analyzes sales calls, meetings, and emails, and syncs the resulting insights into... Community MCP, Enterprise only. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Conversation Intel](../categories/conversation-intel.md) /
Chorus

# Chorus

[Community MCP](../mcp/community.md)
[Enterprise only](../gates/enterprise-only.md)
[Conversation Intel](../categories/conversation-intel.md)
RESEARCHED
Checked 2026-09-02
CLI: gtm

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [zoominfo.com/products/chorus](https://zoominfo.com/products/chorus) · entry id 03-chorus · source 03-conversation-intel.md line 68

**What it does**
Records, transcribes, and analyzes sales calls, meetings, and emails, and syncs the resulting insights into the CRM.

**AI features, separated from automation with an AI label on it**
Talk-ratio and sentiment scoring, competitor-mention detection, deal-risk/momentum scoring (declining engagement, negative sentiment trends, stalled deals), and coaching scorecards tracking methodology adherence. Transcription itself is standard ASR. Vendor "14 patents" marketing language was not independently verified.

**RevOps role**
Call-capture and coaching layer, differentiated from standalone conversation-intelligence tools by direct access to ZoomInfo's B2B contact/firmographic database.

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: Community server: Chorus API key in the CHORUS_API_KEY environment variable (stdio via npx @opensourceops/chorus-mcp), with CHORUS_TOOL_MODE defaulting to readonly. The REST API uses a per-user API token generated in Chorus's Personal Settings page.

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: repo or package: install and run locally
- **Docs URL**: [https://github.com/opensourceops/chorus-mcp-server](https://github.com/opensourceops/chorus-mcp-server)
- **Probed**: 2026-09-04, HTTP 200

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established by hand on 2026-09-02. On 2026-09-04 the recorded URL was a reachable repository or package: a server you install and run on your own machine over stdio. Callable after an install, not a remote endpoint.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/opensourceops/chorus-mcp-server (unofficial; its README states it is not affiliated with or maintained by Chorus.ai or ZoomInfo)

- [https://github.com/opensourceops/chorus-mcp-server](https://github.com/opensourceops/chorus-mcp-server)

**What this server exposes**

- **Tools named**: 39
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-13
- **Repo read**: opensourceops/chorus-mcp-server
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **chorus_create_moment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_delete_moment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_delete_recording** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_execute_saved_search** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_filter_engagements** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_activity_metrics** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_conversation** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_conversation_trackers** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_email** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_engagement** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_integration** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_moment** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_playlist** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_report** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_saved_search** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_scorecard** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_scorecard_template** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_session** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_team** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_team_members** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_transcript** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_user** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_get_video_conference** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_conversations** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_emails** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_integrations** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_moments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_playlist_moments** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_playlists** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_reports** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_saved_searches** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_scorecard_templates** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_scorecards** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_teams** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_users** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_list_video_conferences** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_search_conversations** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_search_users** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **chorus_upload_recording** No description was recorded with the name. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-13. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: gtm
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-13

Install, as the source shows it:

```
npm install -g @zoominfo/gtm-ai-cli
```

quoted from [https://www.npmjs.com/package/@zoominfo/gtm-ai-cli](https://www.npmjs.com/package/@zoominfo/gtm-ai-cli) on 2026-09-13, via npm

Packages seen, with the version on 2026-09-13:

- [npm: @zoominfo/gtm-ai-cli 1.1.0](https://www.npmjs.com/package/@zoominfo/gtm-ai-cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-13.

**Access gate**

- **Gate bucket**: Enterprise only

- **Can a solo operator reach it**: Not without a contract

api_gate, verbatim from the file:

enterprise-only (inferred, not an explicit vendor statement). No public self-serve pricing exists - the product page routes only to "Request Demo," and secondary sources note API access is not included on every ZoomInfo/Chorus plan.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/opensourceops/chorus-mcp-server](https://github.com/opensourceops/chorus-mcp-server)

**On GitHub**

[github.com/Zoominfo](https://github.com/Zoominfo) tied to the vendor by rule 3, account website https://www.zoominfo.com has the vendor's domain, confidence strong

- **Public repositories**: 8, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 1 of them
- **Latest push**: 2026-09-03

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [zoominfo-mcp-plugin](https://github.com/Zoominfo/zoominfo-mcp-plugin) | MCP server | ZoomInfo MCP plugin | 7 | 2026-09-03 | |
| [n8n-nodes-zoominfo](https://github.com/Zoominfo/n8n-nodes-zoominfo) | plugin or integration | n8n community node for the ZoomInfo GTM API | 0 | 2026-09-02 | v1.0.0 |
| [gtm-ai-cli](https://github.com/Zoominfo/gtm-ai-cli) | CLI | A command-line tool for searching ZoomInfo's go-to-market data | 1 | 2026-08-30 | v1.1.0 |
| [homebrew-gtm-ai](https://github.com/Zoominfo/homebrew-gtm-ai) | infrastructure | Homebrew tap for gtm-ai formulae | 0 | 2026-08-26 | |
| [api-auth-java-client](https://github.com/Zoominfo/api-auth-java-client) | SDK | Zoominfo API's Java Authentication Client | 2 | 2026-06-30 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Fetch a call transcript](../jobs/fetch-call-transcript.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Score rep performance](../jobs/score-rep-performance.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.zoominfo.com/products/chorus](https://www.zoominfo.com/products/chorus)
- [https://api-docs.chorus.ai/](https://api-docs.chorus.ai/)
- [https://www.claap.io/blog/chorus-ai-api](https://www.claap.io/blog/chorus-ai-api)
- [https://pipeline.zoominfo.com/sales/introducing-zoominfo-chorus](https://pipeline.zoominfo.com/sales/introducing-zoominfo-chorus)
- [https://github.com/opensourceops/chorus-mcp-server](https://github.com/opensourceops/chorus-mcp-server)

5 source URLs. Raw sources field, verbatim:

https://www.zoominfo.com/products/chorus, https://api-docs.chorus.ai/, https://www.claap.io/blog/chorus-ai-api, https://pipeline.zoominfo.com/sales/introducing-zoominfo-chorus, https://github.com/opensourceops/chorus-mcp-server

**Notes, verbatim from the file**
2026-09-02: mcp_status none-found -> community. https://github.com/opensourceops/chorus-mcp-server is a 39-tool Apache-2.0 MCP server for Chorus (conversations, transcripts, scorecards, playlists, emails, engagements, reports; 6 resources and 6 workflow prompts) whose README states it is an unofficial, community-maintained project not affiliated with or maintained by Chorus.ai or ZoomInfo. No first-party ZoomInfo or Chorus server was found on the vendor site or in the official MCP registry (zero hits for chorus).

**Provenance**

- **Entry id**: 03-chorus

- **Source file**: 03-conversation-intel.md

- **Source line**: 68

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-13

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
